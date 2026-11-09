"""Terra Coletiva — financial scenario model.

All amounts in BRL. Time in months (0-indexed): a member with ``start_month=s``
makes their first contribution in month ``s``; balances are cumulative through
the end of each month. After ``T`` months, contributions occur in months ``0..T-1``.

A "unit" = one full share. A family = 1 unit (2 adults jointly); a single friend
= 1 unit. A unit contributes ``standard_monthly`` per month (configurable per member).

Late-joiner strategies (``Member.strategy``):
- ``constant``    : normal from their start month.
- ``backpay``     : at join, pay a lump sum equal to the months they "missed", then
                    continue at the standard pace -> full parity with a founder.
- ``accelerated`` : no lump; pay ``monthly * accel_factor`` until their land-reserve
                    contribution catches up to a founder's, then standard pace.
- ``reduced``     : no lump; standard pace from join -> permanently smaller share.

Life events:
- ``stop_month``    : member stops contributing from this month (default -> dilution).
- ``withdraw_month``: member exits at this month (nominal principal paid back).

Withdrawal payout order (documented assumption): **cash first** (their principal is
liquid), then **insurance reserve** (the self-insurance pool), then **partial land
sale** as the last resort. This answers the core question: can an exit be paid
without forcing a land sale?

Land: money in the land reserve is either ``cash`` (uninvested) or ``land_asset``
(owned parcel). The group buys the first (cheap) tier as soon as cash allows, then
sells and trades up when cash + land value covers the next tier's price.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

# Nominal land-appreciation scenarios (BRL/year) for planning.
# Recent 5y (2019-2024): ~+16%/yr nominal (Scot Consultoria via Canal Rural).
# Long-run real: ~5-8%/yr over IPCA ~4.5% -> ~9-13% nominal. We stay conservative:
LAND_APPRECIATION = {
    "pessimista": 0.00,   # flat nominal -> ~4-5%/yr real loss to inflation
    "realista":   0.06,   # modest real gain (~1-2%/yr), still below history
    "otimista":   0.10,   # near the long-run average
}


@dataclass
class Params:
    insurance_rate: float = 0.10                     # x% of each contribution -> insurance reserve
    standard_monthly: float = 1500.0                 # BRL per full share per month
    horizon_months: int = 120                        # 10 years
    land_tiers: tuple = (300_000.0, 800_000.0, 1_500_000.0)  # entry -> bigger -> ideal
    land_appreciation_annual: float = 0.0            # 0 = flat land value
    rental_yield_annual: float = 0.0                 # rent = land value × yield/12, REINVESTED (never distributed)


@dataclass
class Member:
    name: str
    start_month: int = 0
    monthly: float | None = None                     # None -> Params.standard_monthly
    strategy: str = "constant"                       # constant | backpay | accelerated | reduced
    accel_factor: float = 2.0
    stop_month: int | None = None                    # stop contributing from this month
    withdraw_month: int | None = None                # exit at this month
    pause_months: tuple | None = None                # (start, end): contribute 0 in [start, end)

    def base_monthly(self, p: Params) -> float:
        return p.standard_monthly if self.monthly is None else self.monthly


def simulate(members: list[Member], p: Params) -> pd.DataFrame:
    T = p.horizon_months
    x = p.insurance_rate
    apr = p.land_appreciation_annual

    land = {m.name: np.zeros(T + 1) for m in members}
    total = {m.name: np.zeros(T + 1) for m in members}
    caught = {m.name: (m.strategy != "accelerated") for m in members}
    active = list(members)
    withdraw_month = {m.name: m.withdraw_month for m in members}

    land_fund = np.zeros(T + 1)        # total land-reserve contributions of ACTIVE members
    insurance_fund = np.zeros(T + 1)
    cash = np.zeros(T + 1)
    land_asset = np.zeros(T + 1)
    tier = np.zeros(T + 1, dtype=int)
    rental_income = np.zeros(T + 1)   # cumulative reinvested rent (collective capital)

    founder_land = np.zeros(T + 1)     # hypothetical founder reference (start 0)

    lf = 0.0
    ins = 0.0
    cash_bal = 0.0
    land_value = 0.0
    rent_cum = 0.0
    owned = -1
    events: list[tuple] = []
    exits: dict = {}

    for t in range(T):
        month = t
        founder_land[month + 1] = founder_land[month] + p.standard_monthly * (1 - x)

        # ---- contributions ----
        this_land = 0.0
        this_ins = 0.0
        for m in active:
            if m.start_month > month:
                continue
            if m.stop_month is not None and month >= m.stop_month:
                continue
            if m.withdraw_month is not None and month >= m.withdraw_month:
                continue
            if m.pause_months is not None and m.pause_months[0] <= month < m.pause_months[1]:
                continue
            base = m.base_monthly(p)
            if m.strategy == "backpay" and month == m.start_month:
                pay = base * (m.start_month + 1)   # lump for missed months + this month
            elif m.strategy == "accelerated" and not caught[m.name]:
                pay = base * m.accel_factor
            else:
                pay = base

            lp = pay * (1 - x)
            ip = pay * x
            land[m.name][month + 1] = land[m.name][month] + lp
            total[m.name][month + 1] = total[m.name][month] + pay
            this_land += lp
            this_ins += ip

            if m.strategy == "accelerated" and not caught[m.name]:
                if land[m.name][month + 1] >= founder_land[month + 1]:
                    caught[m.name] = True

        lf += this_land
        ins += this_ins
        cash_bal += this_land

        # ---- rental income (reinvested collective capital, never distributed) ----
        rent_this = 0.0
        if owned != -1 and p.rental_yield_annual > 0:
            rent_this = land_value * p.rental_yield_annual / 12
        rent_cum += rent_this
        cash_bal += rent_this

        # ---- appreciation ----
        if land_value > 0:
            land_value *= (1 + apr / 12)

        # ---- buy / trade up ----
        while True:
            if owned == -1:
                if cash_bal >= p.land_tiers[0]:
                    cash_bal -= p.land_tiers[0]
                    land_value = p.land_tiers[0]
                    owned = 0
                    events.append((month, "buy", 1, p.land_tiers[0]))
                else:
                    break
            elif owned < len(p.land_tiers) - 1:
                nxt = owned + 1
                if cash_bal + land_value >= p.land_tiers[nxt]:
                    cash_bal += land_value             # sell current
                    cash_bal -= p.land_tiers[nxt]      # buy bigger
                    land_value = p.land_tiers[nxt]
                    owned = nxt
                    events.append((month, "upgrade", owned + 1, p.land_tiers[nxt]))
                else:
                    break
            else:
                break

        # ---- withdrawals (exits) ----
        for m in list(active):
            if m.withdraw_month is not None and m.withdraw_month == month:
                principal = land[m.name][month]          # nominal principal owed
                owed = principal
                from_cash = min(owed, cash_bal)
                cash_bal -= from_cash
                owed -= from_cash
                from_ins = min(owed, ins)
                ins -= from_ins
                owed -= from_ins
                from_land = min(owed, land_value)
                land_value -= from_land
                owed -= from_land
                lf -= principal                           # their stake leaves the pool
                active.remove(m)
                exits[m.name] = {
                    "month": month,
                    "principal": principal,
                    "from_cash": from_cash,
                    "from_ins": from_ins,
                    "from_land": from_land,
                    "uncovered": owed,
                }
                events.append((month, "withdraw", m.name, principal))
                if from_land > 0:
                    events.append((month, "forced-sale", owned + 1, from_land))

        land_fund[month + 1] = lf
        insurance_fund[month + 1] = ins
        cash[month + 1] = cash_bal
        land_asset[month + 1] = land_value
        tier[month + 1] = owned + 1
        rental_income[month + 1] = rent_cum

    df = pd.DataFrame(
        {
            "land_fund": land_fund,
            "insurance_fund": insurance_fund,
            "cash": cash,
            "land_asset": land_asset,
            "tier": tier,
            "rental_income": rental_income,
        }
    )
    # buying capacity = cash + land = members' land fund + reinvested rent
    df["net_worth"] = df["cash"] + df["land_asset"] + df["insurance_fund"]
    df.index.name = "month"

    denom = land_fund.copy()
    for m in members:
        df[f"land_{m.name}"] = land[m.name]
        df[f"total_{m.name}"] = total[m.name]
        df[f"stake_{m.name}"] = np.divide(
            land[m.name], denom, out=np.full_like(denom, np.nan), where=denom > 0
        )
        # a withdrawn member has no stake after their exit month
        if m.withdraw_month is not None:
            df.loc[df.index >= m.withdraw_month, f"stake_{m.name}"] = np.nan

    df.attrs["events"] = events
    df.attrs["exits"] = exits
    return df


def milestones(df: pd.DataFrame, p: Params) -> dict:
    """First month each land tier is reached (None if never)."""
    out = {}
    for k in range(1, len(p.land_tiers) + 1):
        hit = df.index[df["tier"] >= k]
        out[k] = int(hit.min()) if len(hit) else None
    return out


def fmt_brl(v: float) -> str:
    return f"R$ {v:,.0f}".replace(",", ".")
