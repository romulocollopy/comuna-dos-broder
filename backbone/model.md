# Backbone — Model

The jurisdiction-agnostic skeleton. Everything here must work under both Brazilian and Canadian law; where it can't, the divergence moves into a branch and is flagged here with a `⚠️ BRANCH` note.

---

## 1. Actors and roles

| Actor | Role |
|---|---|
| **Member (Participante)** | A natural person who opts in by contract. Contributes money or money-equivalent; owns a stake; votes. |
| **Organizer (Organizador)** | The person/people who set it up, run the process, hold the fund's administration. May also be a member. |
| **Vehicle (Veículo)** | The legal entity that owns the land and holds the fund (an SPE/company in BR; a corporation/partnership/co-op in CA). See branches. |
| **Administrator** | Operates the bank account, bookkeeping, and the reserves. Can be a member, a professional, or a regulated administrator depending on vehicle. |
| **Appraiser/valuator** | Independent party who values the land and, if needed, money-equivalent contributions. |

> **Resolved:** legal members are **individuals**; a "family unit" = the named individuals of one household jointly holding one **severable share** (4 divorce outcomes: withdraw / buyout / split / top-up). See `backbone/membership.md`.

## 2. Contribution types and valuation

1. **Money** — the clean case. Recorded at face value in the unit of account.
2. **Services (money-equivalent)** — e.g. legal, accounting, construction, project management work contributed instead of cash. Valuated at an *agreed, written rate at the time of contribution* (invoice-equivalent), never retroactively.
   - ⚠️ Tax: barter is taxable income in both countries. Treat as if paid in cash and contributed.
3. **Goods (money-equivalent)** — e.g. materials, equipment. Valuated at *fair market value at contribution*, with a written record.

**Rule:** every contribution gets a dated, signed "contribution statement" recording type, value, unit of account, and which reserves it feeds. No undocumented contribution counts.

## 3. The two reserves

Every monetary contribution splits into:

| Reserve | Share of contribution | Purpose |
|---|---|---|
| **Land reserve** | `100% − x%` | Accumulates to buy land; backs ownership stake |
| **Insurance reserve** | `x%` (proposed default: 10%) | Liquidity pool for withdrawals; reverts to principal on success |

- `x` is a design parameter, fixed in the contract and changeable only by supermajority.
- Both reserves are held in segregated sub-accounts of the vehicle.
- Money-equivalent contributions feed the land reserve only, unless the member opts to also fund the insurance reserve in cash.

### The insurance reserve is *not* insurance
It is a **contractual reserve fund** (cf. cooperative/condominium reserve funds). It pays withdrawals from *the group's own pooled money*. It is not underwritten by a regulated insurer and must not be described as an insurance product.

### Success → reversion
Define the **success milestone(s)** explicitly, e.g.: "land purchased and title registered in the vehicle's name" and/or "homes built and habitable." On success, the *unused* insurance reserve reverts to the land reserve / is distributed pro-rata or credited against future obligations. Unused = not consumed by withdrawals, defaults, or losses.

## 4. Ownership and stake

Each member's stake = the sum of their land-reserve contributions (adjusted by any dilution, forfeiture, or reversion). Ownership of the vehicle's shares/quotas and of the eventual land follows this stake proportionally.

- Unequal contributions → unequal stakes. This is expected and fine.
- A member's stake is **liquid in the fund, illiquid in the land** (see §6).

## 5. Phases

| Phase | Description | Withdrawal treatment |
|---|---|---|
| **0. Formation** | Signing, first contributions, cooling-off | Free exit within cooling-off window |
| **1. Accumulation** | Monthly/periodic contributions; fund still cash | Return of contributions (net of reserve) per schedule |
| **2. Purchase** | Vehicle buys land | Most restrictive: money is now in land |
| **3. Build** (optional) | Homes built on the land | As phase 2, plus build contributions |
| **4. Live** | Members occupy; condominium/co-op governance | Stakes convert to housing rights |
| **5. Wind-down** | Voluntary or forced liquidation | Pro-rata distribution |

## 6. Withdrawal mechanics (the hard part)

Withdrawal = a member voluntarily leaves and wants part/all of their money back.

### 6.1 Source of the payout
Order of taps: **(1)** the insurance reserve (up to its balance), then **(2)** replacement by a new member buying the departing stake, then **(3)** other members buying the stake (right of first refusal), then **(4)** partial liquidation of land (last resort, only by group vote).

### 6.2 Valuation methods (pick one in the contract)
- **Nominal** — return of contributions only, no appreciation. (Simplest, punitive to early exit, protective of the group.)
- **Nominal + inflation index** (IPCA in BR / CPI in CA) — preserves purchasing power.
- **Pro-rata market** — the departing member's share of the appraised land value. (Fair late, harsh to the group if forced to sell land.)

### 6.3 Vesting / penalty schedule
Recommend a graduated schedule so early exits are cheaper to the group and late exits are fair to the member:

| Exit in | Member receives |
|---|---|
| Cooling-off (first ~30–60 days) | 100% of contribution, fees only |
| Year 1–3 | Nominal contributions (less reserve consumed) |
| Year 4–7 | Nominal + partial appreciation (e.g. 50%) |
| Year 8–10+ | Pro-rata share of appraised value |

Exact numbers are design parameters — fixed in the contract, not invented later.

### 6.4 Simultaneous withdrawals (run on the reserve)
If reserves are exhausted: payouts are pro-rated against available insurance reserve, then queued (first-in-first-out) against future contributions/refills. The contract must state this explicitly to avoid a "bank run" that forces land liquidation.

## 7. Default and forfeiture

A member who *stops contributing* (default):
1. Grace period (e.g. 90 days) with written notice.
2. Cure (catch up) or convert to reduced stake.
3. Persistent default → stake is **diluted** or **forfeited** per a schedule; forfeited amounts go to the insurance reserve (helping the remaining members, not to the defaulter).

Death, incapacity, divorce, bankruptcy → treated in `docs/pitfalls.md`; each needs a contract clause (buy-sell on death; spousal waiver; creditor protection via the vehicle).

## 8. Governance — decision matrix

| Matter | Threshold |
|---|---|
| Routine administration, bookkeeping, day-to-day | Administrator (delegated) |
| Buying the specific parcel of land | Supermajority (e.g. 2/3) by stake **and** a minimum count of members |
| Selling/encumbering the land | Supermajority + a right of first refusal to members |
| Admitting a new member | Supermajority |
| Amending the contract / changing the reserve % | Supermajority |
| Winding down / liquidation | Supermajority |
| Changing the land's use or the shared-living rules | Per-person majority (democratic, not capital-weighted) |

**Anti-deadlock:** include a buy-sell / "shotgun" clause (a member offers to buy another's stake at a stated price; the other must either sell or buy the offerer out at that price) — standard in both jurisdictions.

## 9. Currency and indexation (BRL — decided)

- **Unit of account: BRL.** Foreign members convert at the câmbio rate on each contribution date (record the rate). See `docs/cross-border.md`.
- Long horizon ⇒ index long-term obligations to inflation (IPCA).
- ⚠️ Cross-border contributions trigger reporting on both sides (Brazil: CBE/declaração de capitais; Canada: T1135) and, for non-resident members, IED registration + IRRF withholding. See `docs/cross-border.md`.

## 10. Dispute resolution

Arbitration is common and private in both BR (Lei 9.307/96) and CA. Recommend: local arbitration with a defined seat, choice of law = law of the land's jurisdiction, and mediation first. Keep the clause simple; a lawyer finalizes it.

---

*Open parameters to fix before contract drafting: reserve % (x), valuation method, penalty schedule, unit of account, success milestone, thresholds. All listed in `docs/research-plan.md`.*
