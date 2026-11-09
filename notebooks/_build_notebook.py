"""Build the Terra Coletiva scenarios notebook with real computed outputs.

Run with the project venv python:
    ./.venv/bin/python notebooks/_build_notebook.py
"""

import nbformat as nbf
from nbclient import NotebookClient

MD = lambda s: nbf.v4.new_markdown_cell(s)
CODE = lambda s: nbf.v4.new_code_cell(s)

cells = []

# ---------------------------------------------------------------------------
cells.append(MD(
    "# Terra Coletiva — Financial Scenarios, Stress Tests & Worked Examples\n\n"
    "Models the collective land fund across: founding alone vs with friends, late joiners "
    "(2y / 5y) under different **top-up** strategies, the **buy-cheap → trade-up** path, and "
    "**stress tests** (withdrawals, a run on the reserve, appreciation/depreciation, asymmetric "
    "contributions, defaults).\n\n"
    "**Everything is illustrative** — the numbers are assumptions you change in one place "
    "(the `Params` block). The *mechanics* are the point. Imports `financial_model.py` "
    "(same folder); needs `pandas` + `matplotlib` (see the project `.venv`)."
))

cells.append(MD(
    "## Assumptions (single source of truth)\n\n"
    "| Parameter | Value | Meaning |\n"
    "|---|---|---|\n"
    "| `insurance_rate` | 10% | share of every contribution routed to the **insurance reserve** (self-insurance for exits) |\n"
    "| `standard_monthly` | R$ 1.500 | monthly contribution of **one full share** (a family = 1 share; a single friend = 1 share) |\n"
    "| `horizon_months` | 120 | 10 years |\n"
    "| `land_tiers` | R$ 300k → 800k → 1.5M | entry (cheap) → bigger → **ideal** |\n"
    "| `land_appreciation_annual` | 0% | flat land value (conservative; flip it to test) |\n"
"| `rental_yield_annual` | 0% | rent (as % of land value) **reinvested into the fund**, never distributed |\n\n"
    "> **Ideal size** = **10 families × R$ 150k of land each = R$ 1.5M** (tier 3). "
    "Tiers are intermediate purchase targets on the way there.\n\n"
    "**Withdrawal assumption** (documented): an exit pays the member's *nominal principal* "
    "(their land-reserve contribution), funded **cash first → insurance reserve → partial land "
    "sale** as the last resort."
))

cells.append(CODE(
    "%matplotlib inline\n"
    "import matplotlib.pyplot as plt\n"
    "import numpy as np\n"
    "import pandas as pd\n"
    "import financial_model as fm\n\n"
    "plt.rcParams['figure.dpi'] = 110\n\n"
    "P = fm.Params(\n"
    "    insurance_rate=0.10,\n"
    "    standard_monthly=1500.0,\n"
    "    horizon_months=120,\n"
    "    land_tiers=(300_000.0, 800_000.0, 1_500_000.0),\n"
    "    land_appreciation_annual=0.0,\n"
    ")\n"
    "print('Model loaded. Defaults:', P)"
))

# ---------------------------------------------------------------------------
cells.append(MD(
    "## 1. Scenarios: who's in, from when\n\n"
    "- **Scenario A** — *\"I found it alone, with my family\"* → 1 unit.\n"
    "- **Scenario B** — *\"one more family and a single friend\"* → 3 units from the start.\n"
    "- **Ideal scale** — 10 families, all founders (to show the full trade-up path).\n\n"
    "A `unit` = one full share. Contributions are constant unless a late-joiner strategy says otherwise."
))

cells.append(CODE(
    "def run(*members):\n"
    "    return fm.simulate(list(members), P)\n\n"
    "# Scenario A — I found it alone, with my family (1 unit)\n"
    "A = run(fm.Member('Familia R', 0))\n\n"
    "# Scenario B — + one more family and a single friend (3 units)\n"
    "B = run(fm.Member('Familia R', 0), fm.Member('Familia B', 0), fm.Member('Amigo C', 0))\n\n"
    "# Ideal scale — 10 families, all founders\n"
    "IDEAL = run(*[fm.Member(f'F{i}', 0) for i in range(1, 11)])\n\n"
    "print('Scenario A (1 unit)   milestones:', fm.milestones(A, P))\n"
    "print('Scenario B (3 units)  milestones:', fm.milestones(B, P))\n"
    "print('IDEAL (10 units)      milestones:', fm.milestones(IDEAL, P))"
))

# ---------------------------------------------------------------------------
cells.append(MD(
    "## 2. Constant members — where the money goes\n\n"
    "Stacked: **cash** (land reserve, not yet spent) + **land owned** + **insurance reserve**. "
    "The purple line is the total **land fund** (the stake basis). Dotted grey lines are the land tiers."
))

cells.append(CODE(
    "fig, axes = plt.subplots(1, 2, figsize=(13, 3.9))\n"
    "for ax, (name, df) in zip(axes, [('Scenario A — 1 family', A), ('Scenario B — 2 families + 1 single', B)]):\n"
    "    m = df.index\n"
    "    ax.stackplot(m, df['cash'], df['land_asset'], df['insurance_fund'],\n"
    "                 labels=['cash (land reserve)', 'land owned', 'insurance reserve'],\n"
    "                 colors=['#4C78A8', '#72B7B2', '#F58518'], alpha=0.85)\n"
    "    ax.plot(m, df['land_fund'], color='#7A4EA8', lw=1.5, label='land fund (stake basis)')\n"
    "    for k, price in enumerate(P.land_tiers, start=1):\n"
    "        ax.axhline(price, color='gray', ls=':', lw=1)\n"
    "        ax.text(0, price, f'  tier {k}', fontsize=8, va='bottom', color='gray')\n"
    "    for (mo, ev, tk, price) in df.attrs['events']:\n"
    "        if ev in ('buy', 'upgrade'):\n"
    "            ax.scatter([mo], [price], color='black', zorder=5)\n"
    "            ax.annotate(f'{ev} tier {tk}', (mo, price), fontsize=7, xytext=(5, 6), textcoords='offset points')\n"
    "    ax.set_title(name, fontsize=11)\n"
    "    ax.set_xlabel('month'); ax.set_ylabel('BRL')\n"
    "    ax.legend(fontsize=7, loc='upper left')\n"
    "plt.tight_layout()\n"
    "plt.show()"
))

cells.append(CODE(
    "rows = []\n"
    "for name, df in [('A (1 unit)', A), ('B (3 units)', B), ('IDEAL (10 units)', IDEAL)]:\n"
    "    ms = fm.milestones(df, P)\n"
    "    rows.append({\n"
    "        'scenario': name,\n"
    "        'final land fund': fm.fmt_brl(df['land_fund'].iloc[-1]),\n"
    "        'insurance reserve': fm.fmt_brl(df['insurance_fund'].iloc[-1]),\n"
    "        'land owned (10y)': fm.fmt_brl(df['land_asset'].iloc[-1]),\n"
    "        'cash left': fm.fmt_brl(df['cash'].iloc[-1]),\n"
    "        'tier 1 @': f\"month {ms[1]}\" if ms[1] is not None else '—',\n"
    "        'tier 2 @': f\"month {ms[2]}\" if ms[2] is not None else '—',\n"
    "        'tier 3 @': f\"month {ms[3]}\" if ms[3] is not None else '—',\n"
    "    })\n"
    "display(pd.DataFrame(rows).set_index('scenario'))"
))

# ---------------------------------------------------------------------------
cells.append(MD(
    "## 3. Late joiners — three top-up strategies\n\n"
    "A **new member joins after 2 or 5 years**, on top of the 3 founding units. Three ways to enter:\n\n"
    "- **backpay** — pays a lump sum equal to the months they missed, then the standard pace → **full parity** (25%).\n"
    "- **accelerated** — no lump; pays **2× monthly** until their land contribution catches up to a founder's → reaches parity over time.\n"
    "- **reduced** — no lump; standard pace from their join date → a **permanently smaller share**.\n\n"
    "The grey dashed line is the **equal 4-way split (25%)** — where a \"full\" member sits."
))

cells.append(CODE(
    "BASE = [fm.Member('Familia R', 0), fm.Member('Familia B', 0), fm.Member('Amigo C', 0)]\n\n"
    "def late_join_sims(join_month):\n"
    "    return {\n"
    "        'backpay': run(*BASE, fm.Member('novo_backpay', join_month, strategy='backpay')),\n"
    "        'accelerated': run(*BASE, fm.Member('novo_accelerated', join_month, strategy='accelerated', accel_factor=2.0)),\n"
    "        'reduced': run(*BASE, fm.Member('novo_reduced', join_month, strategy='reduced')),\n"
    "    }\n\n"
    "join24 = late_join_sims(24)\n"
    "join60 = late_join_sims(60)"
))

cells.append(CODE(
    "def plot_join(join_sims, join_month, title):\n"
    "    fig, ax = plt.subplots(figsize=(9, 3.8))\n"
    "    m = join_sims['backpay'].index\n"
    "    style = {'backpay': ('#4C78A8', 'backpay — lump sum → full parity'),\n"
    "             'accelerated': ('#72B7B2', 'accelerated — 2× monthly until caught up'),\n"
    "             'reduced': ('#F58518', 'reduced — no catch-up, smaller share')}\n"
    "    for strat, (c, lab) in style.items():\n"
    "        ax.plot(m, join_sims[strat][f'stake_novo_{strat}'], color=c, lw=1.8, label=lab)\n"
    "    ax.axhline(0.25, color='gray', ls='--', lw=1)\n"
    "    ax.text(0, 0.252, 'equal 4-way split (25%)', fontsize=8, va='bottom', color='gray')\n"
    "    ax.axvline(join_month, color='black', lw=0.7)\n"
    "    ax.text(join_month + 1, 0.30, 'join', fontsize=8)\n"
    "    ax.set_xlabel('month'); ax.set_ylabel('stake share'); ax.set_ylim(0, 0.32)\n"
    "    ax.set_title(title); ax.legend(fontsize=8, loc='center right')\n"
    "    plt.tight_layout(); plt.show()\n\n"
    "plot_join(join24, 24, 'Late joiner at 2 years (month 24) — stake share by strategy')\n"
    "plot_join(join60, 60, 'Late joiner at 5 years (month 60) — stake share by strategy')"
))

cells.append(CODE(
    "rows = []\n"
    "for label, sims in [('2 years (24)', join24), ('5 years (60)', join60)]:\n"
    "    for strat, df in sims.items():\n"
    "        rows.append({\n"
    "            'join': label, 'strategy': strat,\n"
    "            'final stake': f\"{df[f'stake_novo_{strat}'].iloc[-1]:.1%}\",\n"
    "            'total paid (10y)': fm.fmt_brl(df[f'total_novo_{strat}'].iloc[-1]),\n"
    "            'land contributed': fm.fmt_brl(df[f'land_novo_{strat}'].iloc[-1]),\n"
    "        })\n"
    "display(pd.DataFrame(rows))"
))

# ---------------------------------------------------------------------------
cells.append(MD(
    "## 4. Buy cheap → trade up → ideal size\n\n"
    "The group buys the **cheapest tier** as soon as cash allows, then **sells and trades up** "
    "as the fund grows. This shows that path for Scenario B (3 units) vs the Ideal scale (10 families)."
))

cells.append(CODE(
    "fig, axes = plt.subplots(1, 2, figsize=(13, 3.9))\n"
    "for ax, (name, df) in zip(axes, [('Scenario B (3 units)', B), ('Ideal scale (10 families)', IDEAL)]):\n"
    "    m = df.index\n"
    "    ax.plot(m, df['cash'], color='#4C78A8', lw=1.5, label='cash')\n"
    "    ax.plot(m, df['land_asset'], color='#72B7B2', lw=1.5, label='land owned')\n"
    "    ax.plot(m, df['net_worth'], color='#7A4EA8', lw=1.2, ls='--', label='total fund')\n"
    "    for k, price in enumerate(P.land_tiers, start=1):\n"
    "        ax.axhline(price, color='gray', ls=':', lw=1)\n"
    "        ax.text(0, price, f'  tier {k}', fontsize=8, va='bottom', color='gray')\n"
    "    for (mo, ev, tk, price) in df.attrs['events']:\n"
    "        if ev in ('buy', 'upgrade'):\n"
    "            ax.scatter([mo], [price], color='black', zorder=5)\n"
    "            ax.annotate(f'{ev} tier {tk}', (mo, price), fontsize=8, xytext=(4, 6), textcoords='offset points')\n"
    "    ax.set_title(name, fontsize=11); ax.set_xlabel('month'); ax.set_ylabel('BRL')\n"
    "    ax.legend(fontsize=8)\n"
    "plt.tight_layout(); plt.show()"
))

cells.append(CODE(
    "print('KEY NUMBERS')\n"
    "print('A (1 family, 10y):   land fund', fm.fmt_brl(A['land_fund'].iloc[-1]),\n"
    "      '→ cannot even reach tier 1 (R$ 300k).')\n"
    "print('B (3 units, 10y):    land fund', fm.fmt_brl(B['land_fund'].iloc[-1]),\n"
    "      '→ reaches tier 1 only; cannot afford tier 2 (R$ 800k).')\n"
    "print('IDEAL (10 families):  land fund', fm.fmt_brl(IDEAL['land_fund'].iloc[-1]),\n"
    "      '→ reaches tier 3 (ideal, R$ 1.5M).')\n"
    "print()\n"
    "print('To reach tier 2 (R$ 800k) in 10y you need roughly',\n"
    "      int(np.ceil(800_000 / (120 * 1500 * 0.9))), 'units contributing R$ 1.500/mo;')\n"
    "print('to reach tier 3 (R$ 1.5M) in 10y you need roughly',\n"
    "      int(np.ceil(1_500_000 / (120 * 1500 * 0.9))), 'units.')"
))

# ---------------------------------------------------------------------------
cells.append(MD(
    "## 5. Stress tests\n\n"
    "The scenarios above assume everyone stays and pays. Life doesn't. These stress the "
    "structure at its weak points."
))

cells.append(MD(
    "### 5.1 Withdrawal timing — before vs after the land purchase\n\n"
    "One member exits **before** the land is bought (money still liquid) vs **after** "
    "(money tied up in land). The difference is everything."
))

cells.append(CODE(
    "pre  = fm.simulate([fm.Member('A',0), fm.Member('B',0), fm.Member('C',0, withdraw_month=24)], P)\n"
    "post = fm.simulate([fm.Member('A',0), fm.Member('B',0), fm.Member('C',0, withdraw_month=90)], P)\n\n"
    "for label, df in [('PRE-purchase  (exit month 24)', pre), ('POST-purchase (exit month 90)', post)]:\n"
    "    e = df.attrs['exits']['C']\n"
    "    forced = 'YES — forced land sale' if e['from_land'] > 0 else 'no forced sale'\n"
    "    print(f\"{label}: principal {fm.fmt_brl(e['principal'])} | \"\n"
    "          f\"cash {fm.fmt_brl(e['from_cash'])} + insurance {fm.fmt_brl(e['from_ins'])} + land {fm.fmt_brl(e['from_land'])} → {forced}\")"
))

cells.append(CODE(
    "fig, ax = plt.subplots(figsize=(9, 3.8))\n"
    "m = post.index\n"
    "ax.plot(m, post['cash'], label='cash', color='#4C78A8')\n"
    "ax.plot(m, post['land_asset'], label='land owned', color='#72B7B2')\n"
    "ax.plot(m, post['insurance_fund'], label='insurance reserve', color='#F58518')\n"
    "ax.axvline(90, color='black', lw=0.7); ax.text(90.5, 50_000, 'exit', fontsize=8)\n"
    "ax.set_title('Post-purchase exit at month 90 — the insurance reserve is drained, then land is partly sold')\n"
    "ax.set_xlabel('month'); ax.set_ylabel('BRL'); ax.legend(fontsize=8)\n"
    "plt.tight_layout(); plt.show()"
))

cells.append(MD(
    "### 5.2 Run on the reserve — two members exit at once (after purchase)\n\n"
    "The worst case for a self-insured pool: two simultaneous exits when the money is in land."
))

cells.append(CODE(
    "run_df = fm.simulate([fm.Member('A',0, withdraw_month=90), fm.Member('B',0, withdraw_month=90), fm.Member('C',0)], P)\n"
    "for n, e in run_df.attrs['exits'].items():\n"
    "    print(f\"{n}: principal {fm.fmt_brl(e['principal'])}, from cash {fm.fmt_brl(e['from_cash'])}, \"\n"
    "          f\"insurance {fm.fmt_brl(e['from_ins'])}, land sale {fm.fmt_brl(e['from_land'])}\")\n"
    "print('land owned after the run:', fm.fmt_brl(run_df['land_asset'].iloc[-1]), '(was R$ 300.000)')\n"
    "print('insurance reserve after:', fm.fmt_brl(run_df['insurance_fund'].iloc[-1]))"
))

cells.append(MD(
    "### 5.3 Land price — pessimista vs realista\n\n"
    "Nominal depreciation of Brazilian land is rare (recent 5y: +113% — Scot/Canal Rural). "
    "So we compare a **pessimistic** 0%/yr (flat nominal = real loss ~4-5%/yr) against a "
    "**realistic** +6%/yr (still well below the ~16%/yr recent average)."
))

cells.append(CODE(
    "fig, ax = plt.subplots(figsize=(9, 3.8))\n"
    "for label, r in [('pessimista 0%/yr', fm.LAND_APPRECIATION['pessimista']), ('realista +6%/yr', fm.LAND_APPRECIATION['realista'])]:\n"
    "    p2 = fm.Params(land_appreciation_annual=r)\n"
    "    d = fm.simulate([fm.Member('A',0), fm.Member('B',0), fm.Member('C',0)], p2)\n"
    "    ms = fm.milestones(d, p2)\n"
    "    ax.plot(d.index, d['net_worth'], label=f\"{label} → {fm.fmt_brl(d['net_worth'].iloc[-1])} (tier1 @ {ms[1]})\")\n"
    "ax.set_title('Total fund value — land price pessimista (0%) vs realista (+6% nominal)')\n"
    "ax.set_xlabel('month'); ax.set_ylabel('BRL'); ax.legend(fontsize=8)\n"
    "plt.tight_layout(); plt.show()"
))

cells.append(MD(
    "### 5.4 Asymmetric contributions\n\n"
    "Three members putting in **2× / 1× / 0.5×** of the standard rate. Stakes should track "
    "contributions — that's the proportionality principle, not a bug."
))

cells.append(CODE(
    "asym = fm.simulate([fm.Member('Rich (2×)',0, monthly=3000), fm.Member('Mid (1×)',0, monthly=1500), fm.Member('Lean (0.5×)',0, monthly=750)], P)\n"
    "fig, ax = plt.subplots(figsize=(9, 3.6))\n"
    "m = asym.index\n"
    "for name, c in [('Rich (2×)', '#4C78A8'), ('Mid (1×)', '#72B7B2'), ('Lean (0.5×)', '#F58518')]:\n"
    "    ax.plot(m, asym[f'stake_{name}'], color=c, label=f\"{name} → {asym[f'stake_{name}'].iloc[-1]:.0%}\")\n"
    "ax.set_title('Stake share under asymmetric contributions (settles to 57% / 29% / 14%)')\n"
    "ax.set_xlabel('month'); ax.set_ylabel('stake share'); ax.set_ylim(0, 0.65); ax.legend(fontsize=8)\n"
    "plt.tight_layout(); plt.show()"
))

cells.append(MD(
    "### 5.5 Default — a member stops contributing at year 5\n\n"
    "They keep their *accumulated* stake (no forfeiture here — that's a policy knob), but it "
    "dilutes as the others keep paying."
))

cells.append(CODE(
    "stop = fm.simulate([fm.Member('A',0), fm.Member('B',0), fm.Member('C (stops @60)',0, stop_month=60)], P)\n"
    "fig, ax = plt.subplots(figsize=(9, 3.6))\n"
    "for name, c in [('A', '#4C78A8'), ('B', '#72B7B2'), ('C (stops @60)', '#F58518')]:\n"
    "    ax.plot(stop.index, stop[f'stake_{name}'], color=c, label=f\"{name} → {stop[f'stake_{name}'].iloc[-1]:.0%}\")\n"
    "ax.axvline(60, color='black', lw=0.7); ax.text(60.5, 0.28, 'stops paying', fontsize=8)\n"
    "ax.set_title('Default: C stops at month 60 — stake dilutes from 33% to 20%')\n"
    "ax.set_xlabel('month'); ax.set_ylabel('stake share'); ax.set_ylim(0, 0.45); ax.legend(fontsize=8)\n"
    "plt.tight_layout(); plt.show()"
))

# ---------------------------------------------------------------------------
cells.append(MD(
    "## 6. Rental income — social purpose, not profit\n\n"
    "Once land is owned it can be rented (to third parties, or to members before they move). "
    "**Rental income is reinvested into the fund — never distributed back to participants.** "
    "Two effects:\n\n"
    "- **Members can stop paying earlier** — rent accelerates the fund toward its target.\n"
    "- **Hardship buffer** — rent can offset a member's *temporary* pause / postponement.\n\n"
    "Reinvesting (not distributing) also **strengthens the legal posture**: no profit flows to members, "
    "so the arrangement reads as a collective purpose, not an investment."
))

cells.append(CODE(
    "p_rent = fm.Params(rental_yield_annual=0.03)\n"
    "no_rent   = fm.simulate([fm.Member(f'F{i}',0) for i in range(1,11)], P)\n"
    "with_rent = fm.simulate([fm.Member(f'F{i}',0) for i in range(1,11)], p_rent)\n\n"
    "m0 = fm.milestones(no_rent, P); m1 = fm.milestones(with_rent, p_rent)\n"
    "print('without rent: tier2 @', m0[2], ' tier3 @', m0[3])\n"
    "print('with 3% rent: tier2 @', m1[2], ' tier3 @', m1[3], ' | rent earned by 10y:', fm.fmt_brl(with_rent['rental_income'].iloc[-1]))\n"
    "print('→ members stop paying ~', m0[3]-m1[3], 'months earlier (tier 3)')"
))

cells.append(CODE(
    "fig, ax = plt.subplots(figsize=(9, 3.8))\n"
    "ax.plot(no_rent.index, no_rent['cash'] + no_rent['land_asset'], label='no rent', color='#4C78A8')\n"
    "ax.plot(with_rent.index, with_rent['cash'] + with_rent['land_asset'], label='3% rent reinvested', color='#72B7B2')\n"
    "for k, price in enumerate(P.land_tiers, start=1):\n"
    "    ax.axhline(price, color='gray', ls=':', lw=1)\n"
    "    ax.text(0, price, f'  tier {k}', fontsize=8, va='bottom', color='gray')\n"
    "ax.set_title('Buying capacity (cash + land) with rent reinvested — tier 3 reached sooner')\n"
    "ax.set_xlabel('month'); ax.set_ylabel('BRL'); ax.legend(fontsize=8)\n"
    "plt.tight_layout(); plt.show()"
))

cells.append(CODE(
    "pause = [fm.Member('F1',0,pause_months=(24,48))] + [fm.Member(f'F{i}',0) for i in range(2,11)]\n"
    "p_no  = fm.simulate(pause, P)\n"
    "p_yes = fm.simulate(pause, p_rent)\n"
    "print('one member paused 24 months (months 24–48):')\n"
    "print('  baseline (no pause, no rent): tier2 @ 60,  tier3 @ 112')\n"
    "print('  pause, no rent              : tier2 @', fm.milestones(p_no, P)[2], ' tier3 @', fm.milestones(p_no, P)[3])\n"
    "print('  pause + rent                : tier2 @', fm.milestones(p_yes, p_rent)[2], ' tier3 @', fm.milestones(p_yes, p_rent)[3])"
))

cells.append(CODE(
    "fig, ax = plt.subplots(figsize=(9, 3.8))\n"
    "ax.plot(no_rent.index, no_rent['cash'] + no_rent['land_asset'], label='baseline (no pause, no rent)', color='#4C78A8', ls='--')\n"
    "ax.plot(p_no.index, p_no['cash'] + p_no['land_asset'], label='pause, no rent', color='#F58518')\n"
    "ax.plot(p_yes.index, p_yes['cash'] + p_yes['land_asset'], label='pause + rent', color='#72B7B2')\n"
    "for k, price in enumerate(P.land_tiers, start=1):\n"
    "    ax.axhline(price, color='gray', ls=':', lw=1)\n"
    "    ax.text(0, price, f'  tier {k}', fontsize=8, va='bottom', color='gray')\n"
    "ax.set_title('Hardship: one member pauses 2 years — rent offsets the shortfall')\n"
    "ax.set_xlabel('month'); ax.set_ylabel('BRL'); ax.legend(fontsize=8)\n"
    "plt.tight_layout(); plt.show()"
))

cells.append(MD(
    "## Takeaways\n\n"
    "1. **A single family cannot finance even the cheapest tier in 10 years** — the collective is not "
    "optional, it's the whole point.\n"
    "2. **3 units reach only the entry land (tier 1)** at R$ 1.500/mo — bigger land needs more members "
    "and/or higher contributions (~5 units for tier 2, ~10 for tier 3).\n"
    "3. **Late joiners don't break the model.** `backpay` = instant parity; `accelerated` reaches it "
    "gradually; `reduced` = permanently smaller share (14.3% vs 25% at 5y).\n"
    "4. **Withdrawal timing is decisive.** Pre-purchase exits come out of cash (clean). Post-purchase "
    "exits drain the insurance reserve and can force a partial land sale.\n"
    "5. **A run (2 simultaneous exits) after purchase forces selling ~half the land** — this is why the "
    "contract needs the payout waterfall, a queue rule, and a reserve sized to a stress case.\n"
    "6. **The land's price path matters.** Historically Brazilian land *appreciates* (~+16%/yr recent, "
    "+113% in 5y); the **pessimistic** planning floor is flat nominal (0%), the **realistic** is +6%/yr.\n"
    "7. **Asymmetric contributions → proportional stakes** (by design), and **defaults → dilution** "
    "(the stopper's stake shrinks, the others' grow).\n\n"
    "> Change any assumption in the `Params` block and re-run the whole notebook — every chart and table updates."
))

nb = nbf.v4.new_notebook()
nb.cells = cells
nb.metadata = {
    "kernelspec": {"display_name": "Python (terra-coletiva)", "language": "python", "name": "terra-coletiva"},
    "language_info": {"name": "python"},
}

client = NotebookClient(nb, kernel_name="terra-coletiva", timeout=240, allow_errors=False)
client.execute()

out_path = "scenarios.ipynb"
nbf.write(nb, out_path)
print(f"wrote {out_path} with {len(nb.cells)} cells")
