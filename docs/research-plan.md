# Research Plan & Open Questions

What still needs to be gathered or decided before we can draft a lawyer-ready contract.

---

## A. Decisions (locked) & what's still open

**Locked (2026-11-09):**
1. Specific group (not a public template).
2. Land location: depends on the group (BR joiners in BR/CA/EU).
3. Unit of account: **BRL**.
4. Purpose: **shared-living/community**.
5. Scale: ~10 people/families.
6. Role: **both** organizer + participant.

**Still open:**
- Land location (which country) — land-type posture now rural-oriented default, urban possible (`docs/land-type-catches.md`).
- Design parameters (reserve %, valuation method, vesting schedule, vote thresholds, success milestone, cooling-off).

**Resolved:**
- Membership = individuals as legal members; family = jointly-held severable share with 4 divorce outcomes (`backbone/membership.md`).

## B. Statute deep-read (next, after A)

For each fetched statute, extract the exact articles that back each mechanism, and write a short "how this article supports clause X" note. Key targets:

**BR (`legislation/br/`):**
- Lei 10.406/2002 (Código Civil) — arts. 981–1.141 (sociedades; esp. 997–1.038 sociedade simples, 1.052–1.087 limitada); arts. 1.314–1.358 (condomínio); arts. 53–61 (associações). **The keystone.**
- Lei 6.404/76 — SA form; withdrawal/amortization of quotas.
- Lei 5.764/71 — cooperatives (democratic, capital-return limits).
- Lei 11.795/2008 — consórcio (pooled-payment mechanics; requires regulated administrator — likely *not* our vehicle, but the closest analogy to "pool monthly → property").
- Lei 6.385/76 — securities; art. 2º, IX (contrato de investimento coletivo) — the risk to neutralize.
- Lei 4.591/64 — condominium & incorporação (build phase).
- Lei 8.668/93 — FII (rejected: regulated, securities).
- Decreto 92.318/86 — Brazil–Canada tax treaty (double taxation).

**CA (`legislation/ca/`):**
- Canada Cooperatives Act (S.C. 1998, c. 1) — housing co-op route.
- Canada Business Corporations Act (R.S.C. 1985, c. C-44) — corporation route.
- *To fetch:* Ontario Business Corporations Act, Ontario Limited Partnerships Act, Partnerships Act, Securities Act (Ontario) + NI 45-106, Income Tax Act (co-op/non-profit provisions), provincial land-titles acts.

## C. Legal work to commission (lawyer)

1. **Securities opinion** (both jurisdictions) — confirm this is *not* an unregistered scheme, before any money is collected. 🔴
2. **Vehicle selection** — SPE (Ltda) vs cooperativa in BR; corporation vs LP vs co-op in CA.
3. **Insurance-law wording** — confirm "reserve fund" framing avoids insurance regulation.
4. **Cross-border tax memo** — treatment of contributions, barter, reversion, and the tax-treaty position.
5. **Final contract** — draft/red-line the agreement(s) we produce.

## D. Parameters to fix (design decisions)

- Insurance-reserve % (default 10%)
- Valuation method on exit (nominal / indexed / pro-rata)
- Vesting/penalty schedule
- Unit of account + indexation
- Success milestone(s)
- Voting thresholds (supermajority %, min-member count)
- Cooling-off period

## E. Sources & retrieval status

- **Fetched (local snapshots):** 11 BR via `lexml.gov.br`, 2 CA via `laws-lois.justice.gc.ca`. See `legislation/INDEX.md`.
- **Blocked:** `planalto.gov.br` (IP denied) — use LexML/Senado/Câmara instead.
- **Not yet fetched:** Ontario/other provincial statutes, Income Tax Act, NI 45-106.
- **Cross-border research:** now in `docs/cross-border.md` (saída fiscal, non-resident investors, IED/IRRF, Lei 5.709/71, T1135/CRS, treaty).

## F. Parked topics (to brainstorm later)

- **Land-finding mechanism** — scraping sites (realtor.ca, Brazilian equivalents), APIs, or a dedicated person. To design later.
- **Two-phase location strategy** — *initial* investments: any location will do; *final* land: decided between members once the group and target are clearer.
- **Renting the land before moving** — to third parties or to members. **Decision: rent is reinvested into the fund (collective capital), never distributed** → members stop paying earlier / hardship postponements. This *resolves* the "rent vs non-profit" tension: no income flows to members. ⚠️ still confirm vehicle-level tax on rental income with the lawyer.
