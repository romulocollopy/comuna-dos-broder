# Cross-Border — Saída Fiscal, International Members & BRL Mechanics

The group is **mostly Brazilian nationals spread across Brazil, Canada, and Europe**, contributing in **BRL**, toward land whose location is TBD. This document maps the cross-border friction that creates. It is *not* legal advice — every point below needs a cross-border tax/legal professional to confirm for each member's specific situation.

**Source:** training knowledge + primary-source snapshots (Lei 5.709/71, Decreto 92.318/86 fetched). Norm numbers flagged `[verify]` where they may have been superseded.

---

## 1. The one concept that governs everything: tax residency

Each member's obligations differ entirely based on **where they are a tax resident**, not their nationality. A member is one of:

| Profile | Who | Brazilian tax position |
|---|---|---|
| **A. Brazilian resident** | Lives in Brazil | Worldwide income in BR; annual IRPF; CBE if foreign assets > US$ threshold |
| **B. Brazilian non-resident (did "saída fiscal")** | Brazilian national who left BR permanently and filed saída | Taxed in BR **only on Brazilian-source income** (15% on capital gains, etc.); no IRPF, no CBE |
| **C. Brazilian national abroad who *didn't* file saída** | Moved abroad but never formalized departure | **Still a Brazilian tax resident** → worldwide income in BR + possible double residency |
| **D. Non-Brazilian national** (Canadian, European…) | Friend who is not Brazilian | Foreigner for BR purposes; **restricted from rural land** (see §4) |

**Action for every member before joining:** determine your tax residency in writing (a one-page self-declaration, backed by a professional if unclear). This drives §5 of the contract.

## 2. "Saída fiscal" — what it is and why it matters here

**Saída definitiva do país** = the formal act of a Brazilian tax resident permanently leaving Brazil. Governed by Lei 9.718/98 art. 12 and IN SRF 208/2002 (and successors) `[verify latest IN RFB]`.

- The departing person files a **Comunicação de Saída Definitiva** and a **Declaração de Saída Definitiva do País (DSDP)**, becoming a **non-resident** for BR tax from the departure date.
- **Consequence for this project:** a member who did saída (Profile B) is *non-resident* — they can still participate, but their contributions and any eventual gains follow **non-resident rules** (below). A member who *didn't* (Profile C) is still a BR resident, files IRPF, and may owe BR tax on worldwide income — and possibly be double-resident with Canada/Europe (resolved by treaty tie-breaker rules).

**This is not about whether someone *can* join — it's about which tax regime applies to them.** The contract must not assume everyone is the same. It should classify members by residency profile and allocate the tax consequences accordingly.

## 3. Non-resident members contributing BRL (the mechanics)

A non-resident (Profile B or D) contributing money to a Brazilian vehicle and owning a stake in Brazilian land must go through *registered* channels, not a casual transfer:

1. **Keep a valid CPF** (Brazilian nationals keep theirs; non-Brazilians can obtain one). The CPF is the identifier for holding assets in BR.
2. **Bank account:** non-residents may hold a "conta de não residente" (historically "conta CC5"; now under the current Banco Central foreign-exchange framework) `[verify current Resolution BCB]`. This is where BRL lands.
3. **Remittance = an FX contract (contrato de câmbio)** with a correct purpose code. Sending EUR/CAD → BRL for *investment in a company* is not a personal transfer; it is **foreign direct investment (IED)**.
4. **IED registration:** an equity contribution by a non-resident into a Brazilian company must be registered with the **Banco Central (RDE-IED)** `[verify module]`. This is a real compliance step the vehicle must handle for each non-resident member.
5. **Tax on gains:** when the land is eventually sold, a non-resident quotaholder pays **15% (IRRF)** on the gain, versus **15%–22.5% (progressive)** for residents `[verify rates]`. The vehicle (or its administrator) is the withholding/collection point.

**Practical note:** smaller, frequent monthly contributions from abroad are a compliance nuisance (each remittance = an FX operation). Prefer **less-frequent, larger contributions** (e.g. quarterly/semi-annual) to reduce the number of câmbio/IED events. This is a design input to the contribution schedule.

## 4. 🔴 Rural land & foreign members (Lei 5.709/71)

Brazil restricts acquisition of **rural land** by **foreigners** — Lei 5.709/1971 (fetched: `legislation/br/lei-5709-1971-aquisicao-terra-rural-estrangeiro.html`).

- **Who is restricted:** non-Brazilian *nationals* (Profile D) and Brazilian companies under foreign control. **Brazilian nationals — even non-resident for tax (Profile B) — are *not* "foreigners" under 5.709/71**, because nationality, not tax residency, is the criterion `[confirm interpretation with lawyer]`.
- **So:** if the land is **rural**, any **non-Brazilian-national** member (a Canadian/European friend) faces restrictions (size limits, prior authorization in some cases). If the land is **urban**, foreigners can buy freely (municipal rules aside).
- **Consequence for the design:** this is a reason the *land-type* question (rural vs urban) is now a live decision, not just a preference. If any member is a non-Brazilian national and the land is rural, the vehicle structure (and possibly which members hold title) must be planned around 5.709/71.
- **Workarounds** (tenant / surface-right / urban / minority-stake) are mapped in `docs/land-type-catches.md` — a non-owner can join the community without triggering 5.709/71.

## 5. Canada side (Canadian-resident members — including you, Romulo)

- **T1135 (Foreign Income Verification Statement):** Canadian residents holding "specified foreign property" with a total cost amount **> CAD 100,000** must file annually. A stake in a Brazilian land-owning vehicle = foreign property. Filing is not tax — it's disclosure — but penalties for non-filing are real.
- **Worldwide income + treaty:** Canadian residents are taxed on worldwide income; the **Brazil–Canada tax convention (Decreto 92.318/86 in BR)** prevents double taxation on the same gain/distribution.
- **CRS/FATCA:** Canada and Brazil both participate in automatic exchange of financial-account information. Assume everything is visible to both tax authorities — structure for *compliance*, never for hiding.
- **Your own status:** you're a Brazilian living in Canada. Whether you're Profile B or C depends on whether you filed saída. **Resolve your own residency first** — it's the cleanest way to understand what the others will face.

## 6. Europe side (European-resident members)

- Every EU country (and most others) taxes residents on worldwide income and participates in CRS. Brazil has tax treaties with several (Portugal, Spain, etc.).
- A **per-member note** is out of scope here: the rule is "each member confirms their residency + treaty position with a local professional." The contract allocates each member's tax compliance to that member, while the vehicle handles *Brazilian* withholding.

## 7. Design implications (what this changes)

1. **Membership is profile-aware.** The contract classifies members as resident / non-resident / non-Brazilian-national and assigns the matching tax & remittance rules.
2. **Contribution cadence:** less-frequent, larger contributions reduce câmbio/IED overhead for members abroad.
3. **Land-type is now a hard decision:** rural + non-Brazilian members = Lei 5.709/71 constraints.
4. **BRL is the unit of account;** foreign members convert at the câmbio rate on each contribution date (document the rate).
5. **The vehicle must be able to register IED and withhold IRRF** for non-resident members — a reason to prefer a real company (SPE) with proper accounting over an informal pool.
6. **Reporting is everyone's job:** T1135 (CA), CBE (BR residents), and each EU country's equivalents are member-level obligations stated in the contract, not the vehicle's problem to solve silently.

---

*Next step: after land-location is known, commission a cross-border tax memo covering the specific mix of members.*
