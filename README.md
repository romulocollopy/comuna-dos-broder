# Terra Coletiva — Collective Land Initiative

**One-liner:** A legally-backed structure that lets a group of people voluntarily pool money (or money-equivalent contributions) over ~10 years to buy land together — with fair rules for uneven contributions, mid-way withdrawal, and self-insurance.

---

## What this is

People opt into a contract (as co-owners of a company/vehicle, not passive investors) to build a shared fund. The fund buys land. Over time the group may build homes and live there — e.g. ten friends retiring together on shared land.

The hard part is not the vision, it's the *edge cases*: people contribute different amounts, some leave mid-way and need money back, some default, some die. This repository exists to nail those down — in writing, backed by legislation — and end with a contract a lawyer can review and a proposal the group can sign off on.

## The two-reserve mechanism (core idea)

Every contribution is split into two buckets:

| Reserve | Purpose | What happens to it |
|---|---|---|
| **Land reserve** (principal) | Buys the land/property | Stays invested; backs each member's ownership stake |
| **Insurance reserve** (self-insurance) | Pays out members who withdraw mid-way | A % of each contribution; if the project succeeds, the remainder reverts to the principal |

This is **self-insurance**, not an insurance product. Framing matters: calling it "insurance" could pull in insurance regulation. Legally it is a **contractual reserve fund** (like a cooperative or condominium reserve fund).

## Backbone / branch architecture

The rules that are the same everywhere live in the **backbone**. The rules that depend on *where the land is and where members live* live in **branches**.

- **Backbone** (jurisdiction-agnostic): the financial model, reserves, withdrawal mechanics, governance, principles, and the proposal template.
- **Branch BR** and **Branch CA**: the legal vehicle, securities treatment, tax treatment, and property mechanics — these differ fundamentally between Brazil and Canada and follow the *lex rei sitae* (law of where the land sits).

**Why it must branch:** land follows local law, securities law differs, tax differs. The contract's financial logic can be shared; the legal container cannot.

## Repository map

```
backbone/
  model.md             # financial + governance model (the "skeleton")
  glossary.md          # defined terms (a contract needs these)
  membership.md        # family units + severable-share rules (divorce outcomes)
  proposal-template.md # fill-in-the-blanks pitch for the group
  contract-clause-map.md # the agreement's clause skeleton (→ lawyer)
branches/
  br/legal-framework.md  # Brazilian vehicle analysis + citations
  ca/legal-framework.md  # Canadian vehicle analysis + citations
  br/contract-draft.md   # master agreement draft (PT, BR-primary) — for lawyer review
  ca/contract-draft.md   # (later) draft agreement, CA
legislation/
  INDEX.md             # law → what it backs → source → fetch status
  br/*.html            # primary-source snapshots (LexML)
  ca/*.html            # primary-source snapshots (justice.gc.ca)
docs/
  pitfalls.md          # risks, uncertainties, open questions
  cross-border.md      # saída fiscal, international members, BRL mechanics
  land-type-catches.md # rural vs urban: the legal catches for each path
  research-plan.md     # what still needs gathering + lawyer review
notebooks/
  scenarios.ipynb      # financial scenarios & worked examples (executed, charts embedded)
  financial_model.py   # the simulation engine (Params/Member/simulate)
  _build_notebook.py   # regenerates the notebook from scratch
.venv/                 # python env with pandas + matplotlib (run the notebook here)
one-pager.html         # concept one-pager (pt-BR, self-contained HTML — inspired by Frente UX)
presentation/          # static site (css / html / images) built from the one-pager
  css/style.css        #   shared stylesheet
  html/*.html          #   index · cenarios · estresse · renda · riscos · contrato
  images/*.png         #   charts generated from the simulation (generate_images.py)
  build_contract.py    #   renders branches/br/contract-draft.md → html/contrato.html
PRINCIPLES.md          # the principles the whole thing is built on
```

## Current status

**Phase 1 — Decisions locked; contract clause map drafted.**

- [x] Phase 0: repository scaffolded; 11 keystone statutes fetched (11 BR via LexML, 2 CA via justice.gc.ca)
- [x] Core decisions locked (see below): specific group · shared-living purpose · BRL · ~10 families · organizer+participant
- [x] Backbone model, principles, pitfalls, cross-border analysis, and both legal-framework maps drafted
- [x] Contract clause map drafted (`backbone/contract-clause-map.md`)
- [x] Financial scenario notebook (`notebooks/scenarios.ipynb`): late joiners, top-up strategies, land trade-up
- [ ] Land location (country) — land-type posture locked: rural-oriented, urban possible
- [ ] Deep-read the fetched statutes; extract exact articles backing each mechanism
- [ ] Securities + cross-border tax opinions (before any money moves)
- [x] First-draft contract (BR-primary, PT) — `branches/br/contract-draft.md`
- [ ] Tailor the proposal to the actual group

## Decisions (locked 2026-11-09)

1. **Specific group** (yours), not a public template — generalize later if needed.
2. **Land location:** depends on the group; mostly Brazilian joiners in Brazil, Canada, and Europe.
3. **Unit of account: BRL.** Cross-border is a first-class concern (saída fiscal, non-resident investors) — see `docs/cross-border.md`.
4. **Purpose: shared-living/community** — not investment. This is decisive: it de-risks the securities analysis and elevates the cooperative/condominium occupation layer.
5. **Scale:** ~10 people/families is a huge success; 50+ unrealistic.
6. **Your role: both** organizer and participant → governance safeguards (no self-dealing) baked into the clause map.

## Still open (next decisions)

- **Land location (which country).** Land-type now has a posture: **rural-oriented default, urban possible** — see `docs/land-type-catches.md` for the catches (Lei 5.709/71 for rural + foreign members; incorporation regime for urban condo).
- **Design parameters:** reserve %, valuation method, vesting schedule, vote thresholds, success milestone (in `backbone/model.md` and the clause map).
