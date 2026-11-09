# Branch BR — Legal Framework (Brazil)

Where the land is in Brazil, Brazilian law governs the property (*lex rei sitae*) and the vehicle. This branch implements the backbone's model in Brazilian form.

> ⚠️ Draft analysis for discussion. A Brazilian lawyer must confirm before any money moves — especially the securities characterization.

## Vehicle options

| Vehicle | Law | Fit | Verdict |
|---|---|---|---|
| **SPE — Sociedade Limitada (Ltda)** | Código Civil arts. 1.052–1.087 (Lei 10.406/2002) | Proportional capital; withdrawal = quota amortization; flexible buy-sell; single purpose | ✅ **Recommended** |
| **Cooperativa habitacional** | Lei 5.764/71 + Lei 4.591/64 | Democratic (1 member/1 vote), non-profit; strong for "build homes together" | 🟡 Good for the *living* phase; weak for asymmetric capital + withdrawal |
| **Consórcio imobiliário** | Lei 11.795/2008 | Pooled monthly payments → property, BUT requires an authorized consórcio administrator | ❌ Not self-managed by friends; each member gets *their own* property, not shared land |
| **FII** | Lei 8.668/93, Instrução CVM 472 | Real-estate investment fund | ❌ Regulated securities product — not for friends |
| **Condomínio (co-propriedade)** | Código Civil arts. 1.314–1.358 | Direct co-ownership of the land | 🟡 Simple, but no legal personality and no pooled-contribution mechanics for the 10-year accumulation phase |
| **Associação** | Código Civil arts. 53–61 | Non-profit, democratic | ❌ No capital return/profit — wrong for investment contributions |

## Recommended structure (hybrid)

1. **SPE (Ltda)** holds the **fund and the land** — handles contributions, reserves, withdrawal, ownership stakes. Members are *quotaholders* (sócios), proportional to land-reserve contributions.
2. **A condomínio layer** (Lei 4.591/64; Código Civil arts. 1.331–1.358) governs the **build/occupation phase** — once homes exist, occupation and common areas run as a condominium, while the SPE remains the landowner.
3. A **cooperativa** is an alternative if the group truly wants democratic, non-speculative co-housing — but it constrains capital return and asymmetric stakes, so it fits a *different* (more egalitarian) group.

## Key legal points to lock down

- **Withdrawal → amortização de quotas** (Código Civil art. 1.032 for sociedades; quota buyback rules). The contract's vesting/valuation schedule must map onto the quota-amortization mechanics.
- **Securities risk:** Lei 6.385/76, art. 2º, IX ("contrato de investimento coletivo"). A real SPE with active sócios, a written social purpose of co-living, and private relationship-based membership is the main defense. Get a CVM-informed legal opinion. 🔴
- **Purpose confirmed = shared-living/community** (not investment). This materially reduces the securities risk and makes the condominium/cooperative *occupation* layer central. The SPE remains for asymmetric capital + withdrawal.
- **Rural land + foreign members (Lei 5.709/71):** restricts rural-land acquisition by *non-Brazilian nationals*. Brazilian nationals — even non-resident for tax — are not "foreigners" under this law `[confirm interpretation]`. If any member is a non-Brazilian national and the land is rural, plan the title/vehicle around it. See `docs/cross-border.md` §4.
- **"Insurance" wording:** use *fundo de reserva* (reserve fund), mirroring condominium/cooperative reserve funds (Lei 4.591/64 has condominium fund provisions). Avoid anything that reads as unlicensed insurance. 🔴
- **Barter taxation:** services/goods contributions are taxable income; document at fair market value.
- **Cross-border:** if some members are Canadian-resident, the Brazil–Canada tax treaty (Decreto 92.318/86) applies; Brazilian residents with foreign assets must file CBE (Banco Central); consult a tax professional.
- **Arbitration:** Lei 9.307/96 allows arbitration clauses; recommend local arbitration with mediation first.

## What this branch still needs
- Exact article extraction from `legislation/br/*.html` (see research plan §B).
- Choice: SPE vs cooperativa vs hybrid — resolved by purpose (open question #4).
- Contract draft → `branches/br/contract-draft.md`.
