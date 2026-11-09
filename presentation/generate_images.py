"""Generate the charts for the Terra Coletiva presentation site.

Run with the project venv python:
    ./.venv/bin/python presentation/generate_images.py
Writes PNGs to presentation/images/.
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "notebooks"))
import financial_model as fm  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
os.makedirs(IMG, exist_ok=True)

# ---- shared style (earth palette, matches the site) ----
C_CASH = "#4C78A8"
C_LAND = "#3d6b46"
C_INS = "#b05b2c"
C_FUND = "#7A4EA8"
C_TEAL = "#72B7B2"
C_ORANGE = "#F58518"
C_GRAY = "#8b847a"

plt.rcParams.update({
    "figure.dpi": 120,
    "font.family": "DejaVu Sans",
    "axes.edgecolor": "#d8d2c6",
    "axes.labelcolor": "#1c1a17",
    "axes.titlecolor": "#1c1a17",
    "text.color": "#1c1a17",
    "xtick.color": "#6b6459",
    "ytick.color": "#6b6459",
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

P = fm.Params(
    insurance_rate=0.10,
    standard_monthly=1500.0,
    horizon_months=120,
    land_tiers=(300_000.0, 800_000.0, 1_500_000.0),
    land_appreciation_annual=0.0,
)
P_RENT = fm.Params(rental_yield_annual=0.03)

A = fm.simulate([fm.Member("Familia R", 0)], P)
B = fm.simulate([fm.Member("Familia R", 0), fm.Member("Familia B", 0), fm.Member("Amigo C", 0)], P)
IDEAL = fm.simulate([fm.Member(f"F{i}", 0) for i in range(1, 11)], P)


def tier_lines(ax):
    for k, price in enumerate(P.land_tiers, start=1):
        ax.axhline(price, color=C_GRAY, ls=":", lw=1)
        ax.text(0, price, f"  terra {k}", fontsize=8, va="bottom", color=C_GRAY)


def save(fig, name):
    fig.savefig(os.path.join(IMG, name), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


# ---- 1. fund growth (A vs B) ----
fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.6))
for ax, (name, df) in zip(axes, [("1 família", A), ("2 famílias + 1 amigo", B)]):
    ax.stackplot(df.index, df["cash"], df["land_asset"], df["insurance_fund"],
                 labels=["caixa", "terra comprada", "reserva de garantia"],
                 colors=[C_CASH, C_TEAL, C_INS], alpha=0.85)
    ax.plot(df.index, df["land_fund"], color=C_FUND, lw=1.5, label="reserva de terra (base da cota)")
    tier_lines(ax)
    ax.set_title(name, fontsize=11)
    ax.set_xlabel("mês"); ax.set_ylabel("R$")
    ax.legend(fontsize=7, loc="upper left")
fig.suptitle("Para onde vai o dinheiro (contribuições constantes)", fontsize=12, y=1.02)
save(fig, "fund-growth.png")

# ---- 2. trade-up (B vs IDEAL) ----
fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.6))
for ax, (name, df) in zip(axes, [("3 cotas", B), ("escala ideal (10 famílias)", IDEAL)]):
    ax.plot(df.index, df["cash"], color=C_CASH, lw=1.5, label="caixa")
    ax.plot(df.index, df["land_asset"], color=C_LAND, lw=1.5, label="terra comprada")
    ax.plot(df.index, df["net_worth"], color=C_FUND, lw=1.2, ls="--", label="fundo total")
    tier_lines(ax)
    for (mo, ev, tk, price) in df.attrs["events"]:
        if ev in ("buy", "upgrade"):
            ax.scatter([mo], [price], color="black", zorder=5, s=14)
    ax.set_title(name, fontsize=11); ax.set_xlabel("mês"); ax.set_ylabel("R$")
    ax.legend(fontsize=8)
fig.suptitle("Comprar barato → trocar por terra maior", fontsize=12, y=1.02)
save(fig, "trade-up.png")

# ---- 3. late joiners ----
BASE = [fm.Member("Familia R", 0), fm.Member("Familia B", 0), fm.Member("Amigo C", 0)]
def late(join):
    return {
        "complemento": fm.simulate(BASE + [fm.Member("novo", join, strategy="backpay")], P),
        "acelerado": fm.simulate(BASE + [fm.Member("novo", join, strategy="accelerated", accel_factor=2.0)], P),
        "reduzido": fm.simulate(BASE + [fm.Member("novo", join, strategy="reduced")], P),
    }
join24, join60 = late(24), late(60)
style = {"complemento": (C_CASH, "complemento (paridade plena)"),
         "acelerado": (C_TEAL, "acelerado (2× até alcançar)"),
         "reduzido": (C_ORANGE, "reduzido (cota menor)")}
fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.6))
for ax, (title, sims, jm) in zip(axes, [("entra aos 2 anos", join24, 24), ("entra aos 5 anos", join60, 60)]):
    for strat, (c, lab) in style.items():
        ax.plot(sims[strat].index, sims[strat]["stake_novo"], color=c, lw=1.8, label=lab)
    ax.axhline(0.25, color=C_GRAY, ls="--", lw=1)
    ax.text(0, 0.253, "divisão igual (25%)", fontsize=7, va="bottom", color=C_GRAY)
    ax.axvline(jm, color="black", lw=0.7); ax.text(jm + 1, 0.30, "entra", fontsize=8)
    ax.set_title(title, fontsize=11); ax.set_xlabel("mês"); ax.set_ylabel("participação"); ax.set_ylim(0, 0.32)
    ax.legend(fontsize=7, loc="center right")
fig.suptitle("Quem entra depois — três formas de top-up", fontsize=12, y=1.02)
save(fig, "late-joiners.png")

# ---- 4. withdrawal (post-purchase) ----
post = fm.simulate([fm.Member("A", 0), fm.Member("B", 0), fm.Member("C", 0, withdraw_month=90)], P)
fig, ax = plt.subplots(figsize=(7.5, 3.4))
ax.plot(post.index, post["cash"], label="caixa", color=C_CASH)
ax.plot(post.index, post["land_asset"], label="terra comprada", color=C_LAND)
ax.plot(post.index, post["insurance_fund"], label="reserva de garantia", color=C_INS)
ax.axvline(90, color="black", lw=0.7); ax.text(90.5, 50000, "saída", fontsize=8)
ax.set_title("Saída depois da compra da terra — a garantia é usada e vende-se um pedaço")
ax.set_xlabel("mês"); ax.set_ylabel("R$"); ax.legend(fontsize=8)
save(fig, "withdrawal.png")

# ---- 5. run on reserve ----
run_df = fm.simulate([fm.Member("A", 0, withdraw_month=90), fm.Member("B", 0, withdraw_month=90), fm.Member("C", 0)], P)
fig, ax = plt.subplots(figsize=(7.5, 3.4))
ax.plot(run_df.index, run_df["cash"], label="caixa", color=C_CASH)
ax.plot(run_df.index, run_df["land_asset"], label="terra comprada", color=C_LAND)
ax.plot(run_df.index, run_df["insurance_fund"], label="reserva de garantia", color=C_INS)
ax.axvline(90, color="black", lw=0.7); ax.text(90.5, 50000, "2 saídas", fontsize=8)
ax.set_title("Corrida: duas saídas ao mesmo tempo forçam vender quase metade da terra")
ax.set_xlabel("mês"); ax.set_ylabel("R$"); ax.legend(fontsize=8)
save(fig, "run-reserve.png")

# ---- 6. appreciation (pessimista vs realista, nominal) ----
fig, ax = plt.subplots(figsize=(7.5, 3.4))
for label, r, c in [("pessimista (0% a.a.)", fm.LAND_APPRECIATION["pessimista"], C_ORANGE),
                    ("realista (+6% a.a.)", fm.LAND_APPRECIATION["realista"], C_LAND)]:
    d = fm.simulate([fm.Member("A", 0), fm.Member("B", 0), fm.Member("C", 0)], fm.Params(land_appreciation_annual=r))
    ax.plot(d.index, d["net_worth"], color=c, label=f"{label} → {fm.fmt_brl(d['net_worth'].iloc[-1])}")
ax.set_title("Preço da terra: pessimista (0%) vs realista (+6% nominal)")
ax.set_xlabel("mês"); ax.set_ylabel("R$"); ax.legend(fontsize=8)
save(fig, "appreciation.png")

# ---- 7. asymmetric ----
asym = fm.simulate([fm.Member("Rico (2×)", 0, monthly=3000), fm.Member("Médio (1×)", 0, monthly=1500), fm.Member("Enxuto (0.5×)", 0, monthly=750)], P)
fig, ax = plt.subplots(figsize=(7.5, 3.4))
for name, c in [("Rico (2×)", C_CASH), ("Médio (1×)", C_TEAL), ("Enxuto (0.5×)", C_ORANGE)]:
    ax.plot(asym.index, asym[f"stake_{name}"], color=c, label=f"{name} → {asym[f'stake_{name}'].iloc[-1]:.0%}")
ax.set_title("Contribuições desiguais → participação proporcional (57% / 29% / 14%)")
ax.set_xlabel("mês"); ax.set_ylabel("participação"); ax.set_ylim(0, 0.65); ax.legend(fontsize=8)
save(fig, "asymmetric.png")

# ---- 8. default ----
stop = fm.simulate([fm.Member("A", 0), fm.Member("B", 0), fm.Member("C (para aos 60)", 0, stop_month=60)], P)
fig, ax = plt.subplots(figsize=(7.5, 3.4))
for name, c in [("A", C_CASH), ("B", C_TEAL), ("C (para aos 60)", C_ORANGE)]:
    ax.plot(stop.index, stop[f"stake_{name}"], color=c, label=f"{name} → {stop[f'stake_{name}'].iloc[-1]:.0%}")
ax.axvline(60, color="black", lw=0.7); ax.text(60.5, 0.28, "para de pagar", fontsize=8)
ax.set_title("Quem para de pagar é diluído (33% → 20%)")
ax.set_xlabel("mês"); ax.set_ylabel("participação"); ax.set_ylim(0, 0.45); ax.legend(fontsize=8)
save(fig, "default.png")

# ---- 9. rental ----
no_rent = IDEAL
with_rent = fm.simulate([fm.Member(f"F{i}", 0) for i in range(1, 11)], P_RENT)
pause = [fm.Member("F1", 0, pause_months=(24, 48))] + [fm.Member(f"F{i}", 0) for i in range(2, 11)]
p_no = fm.simulate(pause, P)
p_yes = fm.simulate(pause, P_RENT)
fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.6))
ax = axes[0]
ax.plot(no_rent.index, no_rent["cash"] + no_rent["land_asset"], label="sem aluguel", color=C_CASH)
ax.plot(with_rent.index, with_rent["cash"] + with_rent["land_asset"], label="aluguel reinvestido", color=C_LAND)
tier_lines(ax)
ax.set_title("Aluguel antecipa a terra ideal", fontsize=11); ax.set_xlabel("mês"); ax.set_ylabel("R$"); ax.legend(fontsize=8)
ax = axes[1]
ax.plot(no_rent.index, no_rent["cash"] + no_rent["land_asset"], label="base (sem pausa)", color=C_CASH, ls="--")
ax.plot(p_no.index, p_no["cash"] + p_no["land_asset"], label="pausa, sem aluguel", color=C_ORANGE)
ax.plot(p_yes.index, p_yes["cash"] + p_yes["land_asset"], label="pausa + aluguel", color=C_LAND)
tier_lines(ax)
ax.set_title("Aluguel absorve a pausa de um membro", fontsize=11); ax.set_xlabel("mês"); ax.set_ylabel("R$"); ax.legend(fontsize=8)
fig.suptitle("Renda da terra = capital coletivo (nunca distribuída)", fontsize=12, y=1.02)
save(fig, "rental.png")

print("done:", sorted(os.listdir(IMG)))
