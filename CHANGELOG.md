# Changelog

All notable changes to Terra Coletiva.

## 2026-11-09 — Phase 0 scaffold
- Created repository structure (backbone / branches / legislation / docs).
- Fetched 10 primary-source statutes: 8 BR via LexML, 2 CA via justice.gc.ca.
  (planalto.gov.br blocks this host's IP — LexML/Senado/Câmara used instead.)
- Drafted: README, PRINCIPLES.md, backbone/model.md, backbone/glossary.md,
  backbone/proposal-template.md, docs/pitfalls.md, docs/research-plan.md,
  legislation/INDEX.md, branches/br/legal-framework.md, branches/ca/legal-framework.md.
- Registered project in the projects registry.
- Status: Phase 0. Next: resolve open questions → deep-read statutes → contract draft.

## 2026-11-09 (later) — Decisions locked, cross-border + clause map
- Locked decisions: specific group · shared-living/community · BRL · ~10 families · organizer+participant.
- Added docs/cross-border.md (saída fiscal, non-resident members, IED/IRRF, Lei 5.709/71, T1135/CRS, treaty).
- Added backbone/contract-clause-map.md (clause skeleton → lawyer).
- Fetched 3 more BR laws (Lei 5.709/71, 9.307/96, 10.257/2001).
- Status: Phase 1. Next: land location + land-type → securities/cross-border opinions → full contract.

## 2026-11-09 (evening) — land-type posture + membership severability
- Land-type posture: **rural-oriented default, urban possible** — added `docs/land-type-catches.md` (Lei 5.709/71 for rural+foreign; incorporação for urban condo; fração mínima de parcelamento → one-title co-ownership).
- Membership **resolved**: individuals are legal members; family = jointly-held severable share with 4 divorce outcomes (withdraw / buyout / split / top-up) — added `backbone/membership.md`; updated clause map §3 & §10.
- 5.709/71 workarounds mapped (tenant / surface-right / urban / minority-stake; non-owner participant class).

## 2026-11-09 (night) — financial scenario notebook
- Added `notebooks/` with `financial_model.py` (Params/Member/simulate; two reserves, late-joiner strategies backpay/accelerated/reduced, land buy→trade-up) and an **executed** `scenarios.ipynb` (4 charts + tables, built via nbclient in a project `.venv` with pandas 3.1.1 / matplotlib 3.11.2).
- Key computed findings: 1 family can't reach tier 1 (R$300k) in 10y; 3 units reach tier 1 only; ~5 units needed for tier 2 (R$800k), ~10 units for tier 3 (R$1.5M ideal); backpay = exact 25% parity, reduced@5y = 14.3%.

## 2026-11-09 (night, 2nd) — stress tests
- `financial_model.py` gained `stop_month` (default/dilution) + `withdraw_month` (exit; cash→insurance→forced-sale payout order).
- Notebook rebuilt with §5 stress tests (28 cells, 8 charts): withdrawal timing, run-on-reserve, appreciation/depreciation, asymmetric contributions, default.
- Findings: pre-purchase exit clean (cash); post-purchase exit drains insurance + forces R$13.5k land sale; run (2 exits after purchase) drains reserve + forces ~R$136.5k of R$300k land sale. Parked topics added to research-plan §F: land-finding mechanism, two-phase location, renting land for social purpose.

## 2026-11-09 (night, 3rd) — rental income reinvested (not distributed)
- Decision: rent the land (third parties / members pre-move) but **reinvest all rental income into the fund** — never distribute to participants. Effects: members stop paying earlier; hardship postponements/discounts. Resolves the "rent vs non-profit" tension and strengthens the securities posture.
- Model: added `rental_yield_annual` (rent = land value × yield/12, reinvested) + `pause_months` (temporary pause) to `financial_model.py`; notebook §6 added (33 cells, 10 charts).
- Computed: 3% rent on the 10-family land = R$180k/10y → tier 3 reached 9 months earlier (month 103 vs 112); a 2-year member pause is almost fully absorbed by rent (tier 3 @105 vs 103 baseline, @114 without rent).
- Docs: PRINCIPLES #10 (income is collective capital, not profit); clause map §4 hardship + §5 rental reinvestment; research-plan §F updated.

## 2026-11-09 (night, 4th) — first-draft contract (BR, PT)
- Drafted `branches/br/contract-draft.md`: master agreement in Portuguese (19 clauses + 2 annexes) implementing the clause map — purpose/nature, membership+severable share, contributions+reserves+rental reinvestment, governance+organizer safeguards+shotgun, withdrawal (cooling-off/valuation/vesting/waterfall/queue), default, death/divorce (4 outcomes)/bankruptcy, land purchase (Lei 5.709/71), build/occupation, currency/cross-border, tax, arbitration, amendments, winding-down, representations.
- 11 open parameters + 8 lawyer points flagged (securities opinion, insurance framing, contrato social, 5.709/71, fractional quotas, rental tax, arbitration clause, cross-border).
- README repo map + status updated.

## 2026-11-09 (night, 5th) — concept one-pager (pt-BR HTML)
- Added `one-pager.html` — self-contained, framework/JS-free, inspired by the Frente UX aesthetic (blunt clarity, honest voice, semantic + accessible, reduced-motion, earth palette).
- Sections: what it is · how the money works (two reserves + buy→trade-up) · "e se a vida acontecer" (exit/divorce/hardship/uneven/late-joiner) · land income reinvested · honest numbers · legal solidity. pt-BR.

## 2026-11-09 (night, 6th) — static presentation site
- Added `presentation/{css,html,images}`: 4 linked pt-BR pages (index/cenarios/estresse/renda) with a shared stylesheet, plus `generate_images.py` that renders 9 charts from `financial_model.py` into `images/` (fund-growth, trade-up, late-joiners, withdrawal, run-reserve, appreciation, asymmetric, default, rental).
- Served via `python -m http.server 8080` (left running, PID on the box) at `http://localhost:8080/presentation/html/index.html`.

## 2026-11-09 (night, 7th) — realistic/pessimistic land-price scenarios
- Researched Brazilian land prices: nominal devaluation is rare; recent 5y (2019-2024) +113% (~16%/yr) — Scot Consultoria via Canal Rural; long-run real ~5-8%/yr.
- `financial_model.py`: added `LAND_APPRECIATION = {pessimista: 0.0, realista: 0.06, otimista: 0.10}` (nominal/yr).
- Regenerated `appreciation.png` (pessimista 0% vs realista +6%) + rebuilt the notebook §5.3; updated estresse.html text with the source.

## 2026-11-09 (night, 8th) — risks & advantages page
- Added `presentation/html/riscos.html`: full text description (idea, money mechanism, phases, legal structure, governance, life events, land income) + advantages list + honest risks table (risk → mitigation, 11 items).
- Added "Riscos & Vantagens" to the nav on all 5 pages; linked from index (solidez) and renda pagenav.

## 2026-11-09 (night, 9th) — contract as an HTML page
- Added `presentation/build_contract.py` (markdown→HTML via python-markdown) rendering `branches/br/contract-draft.md` → `presentation/html/contrato.html` (5 tables, 3 blockquotes).
- Added table/blockquote/code/hr styles to `style.css`; added "Contrato" to the nav on all 6 pages and footer links on index + riscos.
