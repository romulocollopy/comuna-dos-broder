# Branch CA — Legal Framework (Canada)

Where the land is in Canada, Canadian (federal/provincial) law governs. This branch implements the backbone's model in Canadian form.

> ⚠️ Draft analysis for discussion. A Canadian lawyer must confirm before any money moves — especially the securities characterization.

## Vehicle options

| Vehicle | Law | Fit | Verdict |
|---|---|---|---|
| **Corporation** | Canada Business Corporations Act (R.S.C. 1985, c. C-44) or provincial (e.g. OBCA) | Shareholders proportional to contribution; clean exit via share transfer; limited liability | ✅ **Recommended** (analog of BR SPE) |
| **Limited partnership** | Ontario Limited Partnerships Act (R.S.O. 1990, c. L.16) | GP manages + LPs contribute capital with limited liability; flexible profit split | 🟡 Good, but needs at least one GP with unlimited liability |
| **Co-ownership (tenancy in common)** | Common law / provincial Land Titles/Registry Acts | Unequal, divisible shares; direct land ownership | 🟡 For the *land-holding* layer, not the pooled-contribution phase |
| **Housing co-operative** | Canada Cooperatives Act (S.C. 1998, c. 1) or provincial Co-operative Corporations Acts | Democratic, non-profit; purpose-built for collective living | 🟡 Excellent for the *living* phase; constrains capital return/appreciation |
| **Trust** | Common law / provincial Trustee Acts | Trustee holds land for member beneficiaries | 🟡 Can pair with co-ownership; more complexity |
| **REIT** | Securities regulation | Real-estate investment trust | ❌ Regulated securities — not for friends |

## Recommended structure (hybrid)

1. **A corporation** holds the **fund and the land**; members are shareholders proportional to land-reserve contributions. Shareholders' agreement (unanimous shareholders' agreement) carries the custom rules (reserves, withdrawal, vesting, shotgun).
2. **Tenancy in common / co-ownership** or a **housing co-op** can govern the **build/occupation phase** once homes exist, while the corporation remains landowner.
3. A **housing co-operative** is the alternative if the group wants democratic, non-speculative co-housing — but it limits appreciation capture and asymmetric capital, so it suits a different, more egalitarian group.

## Key legal points to lock down

- **Unequal contributions → unequal shares:** use a corporation with classes or a shareholders' agreement allocating shares proportionally; tenancy in common explicitly allows unequal undivided interests.
- **Securities risk:** the "investment contract" test (*Pacific Coast Coin Exchange v. OSC*, adopting *Howey*). A pooled fund to buy land with expected appreciation looks like a security. Defenses: genuine co-ownership/active shareholders, shared-living purpose (not speculation), and reliance on a private-placement prospectus exemption (NI 45-106 — friends/family/accredited). Get a securities opinion before collecting money. 🔴
- **Purpose confirmed = shared-living/community.** This materially reduces the securities risk and elevates the housing-cooperative/co-ownership *occupation* layer; the corporation remains for asymmetric capital + withdrawal. (For the Brazilian-primary structure, see the BR branch — this CA branch is the alternate.)
- **"Insurance" wording:** a reserve fund, not insurance — avoid insurance-regulation risk (unlicensed insurance activity). 🔴
- **Barter taxation:** services/goods for shares is taxable; value at fair market value; Income Tax Act share-issuance rules (s. 51, rollover complexities).
- **Cross-border:** if some members are Brazilian-resident, the Canada–Brazil tax convention applies; Canadian residents with foreign property ≥ $100k file T1135. Consult a cross-border tax professional.
- **Land transfer & zoning:** provincial planning acts + municipal zoning/by-laws for buildability; due diligence before purchase.
- **Dispute resolution:** arbitration clauses are enforceable; recommend mediation first, local seat, law of the land's province.

## What this branch still needs
- Fetch provincial statutes (OBCA, LP Act, Partnerships Act, Securities Act, NI 45-106, Land Titles Act, Income Tax Act excerpts) — see `legislation/INDEX.md`.
- Choice: corporation vs LP vs co-op — resolved by purpose (open question #4).
- Contract draft → `branches/ca/contract-draft.md`.
