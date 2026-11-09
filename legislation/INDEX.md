# Legislation Index

Map of law → what it backs → source → fetch status.

## Brazil (LexML snapshots in `br/`)

| Law | What it backs | File | Status |
|---|---|---|---|
| **Lei 10.406/2002 — Código Civil** | Sociedades (arts. 981–1.141), sociedade limitada (1.052–1.087), condomínio (1.314–1.358), associações (53–61). Keystone for the vehicle. | `codigo-civil-lei-10406-2002.html` | ✅ fetched (LexML) |
| **Lei 6.404/76 — S.A.** | Corporation form; quota amortization/withdrawal mechanics. | `lei-6404-1976-sociedades-anonimas.html` | ✅ fetched |
| **Lei 5.764/71 — Cooperativismo** | Cooperative vehicle (democratic, capital-return limits). | `lei-5764-1971-cooperativismo.html` | ✅ fetched |
| **Lei 11.795/2008 — Consórcio** | Closest analogy to pooled-payment mechanics; requires regulated administrator (likely rejected as vehicle). | `lei-11795-2008-consorcio.html` | ✅ fetched |
| **Lei 6.385/76 — Valores Mobiliários** | Securities risk: art. 2º, IX (contrato de investimento coletivo). | `lei-6385-1976-valores-mobiliarios.html` | ✅ fetched |
| **Lei 4.591/64 — Condomínio/Incorporações** | Build/occupation phase (condominium). | `lei-4591-1964-condominio-incorporacoes.html` | ✅ fetched |
| **Lei 8.668/93 — FII** | Real-estate investment fund (rejected: regulated securities). | `lei-8668-1993-fii.html` | ✅ fetched |
| **Decreto 92.318/86 — BR–CA tributação** | Brazil–Canada tax treaty (double taxation). | `decreto-92318-1986-br-ca-tributacao.html` | ✅ fetched |
| **Lei 5.709/71 — Aquisição de terra rural por estrangeiro** | Rural-land restrictions for non-Brazilian nationals (critical if land is rural). | `lei-5709-1971-aquisicao-terra-rural-estrangeiro.html` | ✅ fetched |
| Lei 9.307/96 — Arbitragem | Dispute resolution clause. | `lei-9307-1996-arbitragem.html` | ✅ fetched |
| Lei 10.257/2001 — Estatuto da Cidade | Urban planning/zoning (if urban land). | `lei-10257-2001-estatuto-cidade.html` | ✅ fetched |
| Lei 13.097/2015 — Patrimônio de afetação | Ring-fencing project assets (optional). | — | ⬜ to fetch |

## Canada (justice.gc.ca snapshots in `ca/`)

| Law | What it backs | File | Status |
|---|---|---|---|
| **Canada Cooperatives Act (S.C. 1998, c. 1)** | Housing co-op route (federal). | `canada-cooperatives-act.html` | ✅ fetched |
| **Canada Business Corporations Act (R.S.C. 1985, c. C-44)** | Corporation route (federal). | `canada-business-corporations-act.html` | ✅ fetched |
| Ontario Business Corporations Act (R.S.O. 1990, c. B.16) | Corporation route (provincial). | — | ⬜ to fetch (ontario.ca/laws) |
| Ontario Limited Partnerships Act (R.S.O. 1990, c. L.16) | LP route (GP + LPs). | — | ⬜ to fetch |
| Partnerships Act (Ontario) (R.S.O. 1990, c. P.5) | General partnership. | — | ⬜ to fetch |
| Securities Act (Ontario) (R.S.O. 1990, c. S.5) + NI 45-106 | Securities risk + private-placement exemptions. | — | ⬜ to fetch |
| Income Tax Act (Canada) | Capital gains; co-op/non-profit provisions (s. 135.1, 136). | — | ⬜ to fetch |
| Land Titles / Registry Act (Ontario) | Land registration/co-ownership. | — | ⬜ to fetch |
| Trustee Act (Ontario) | Trust holding route (if used). | — | ⬜ to fetch |

## Retrieval method notes

- BR: LexML URNs (`urn:lex:br:federal:lei:YYYY-MM-DD;NNNN`) — rendered HTML snapshots.
- CA: `laws-lois.justice.gc.ca/eng/acts/<code>/FullText.html`.
- `planalto.gov.br` blocks this host's IP ("Acesso Negado") — do not rely on it; use LexML/Senado (`legis.senado.leg.br`) / Câmara (`camara.leg.br`).
- Snapshots are reference copies captured 2026-11-09; always re-verify against the official source before citing in a contract.
