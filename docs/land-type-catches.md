# Land-Type Catches — Rural vs Urban

**Posture (2026-11-09):** rural-oriented default, urban possible, structure stays land-type-agnostic. We do **not** hard-code the land type in the financial model; we keep the *purchase criteria* flexible and pre-map the **catches** for each path, so we can move on whichever type reality offers.

## Why the financial model doesn't care

The fund, reserves, withdrawal, and governance mechanics are identical whether the land is a rural parcel or an urban condo plot. Land-type only changes the **asset layer**:

| | **Rural** | **Urban** |
|---|---|---|
| Asset layer | Single-title land, co-owned via the vehicle (a "condomínio de fato" if shared) | A **condomínio edilício** (Lei 4.591/64 + Código Civil arts. 1.331–1.358) or an **incorporação imobiliária** if built from scratch |
| Legal regime | Lei 5.709/71 (foreign), INCRA, environmental | Estatuto da Cidade (Lei 10.257/2001), Plano Diretor municipal, building permits |
| Tax | ITR (rural) | IPTU (urban) |

## The catches, by path

### 🌾 Rural — the catches to check *before* buying

1. **🔴 Lei 5.709/71 — foreign members.** Acquisition of *rural* land by non-Brazilian **nationals** is restricted (size limits, prior authorization in some cases). Brazilian nationals — even non-resident for tax — are **not** "foreigners" under this law `[confirm interpretation]`. **If any member is a non-Brazilian national, rural land needs a title/vehicle plan around 5.709/71 — or choose urban.**
2. **Fração mínima de parcelamento (INCRA).** Rural land can't be subdivided below a minimum "módulo rural" per municipality. This is the catch behind your "maybe it's a condo" instinct: to give 10 families *individual* homes on rural land, you usually **can't** split the title into 10 lots. Instead: keep **one title** and run it as a co-ownership/condominium arrangement (each family has an exclusive-use area + shared common land). This actually *matches* the collective model well.
3. **Environmental:** CAR (Cadastro Ambiental Rural) registration; **Reserva Legal** (20–35% of the parcel, by biome, can't be cleared); APPs (riparian/hilltop buffers). Building is constrained but co-living on the *legal-reserve-free* portion is usually fine.
4. **Use/conversion:** converting rural to urban use requires municipal approval — slow, not guaranteed. Don't assume "rural now, condominium later" without checking.
5. **Agrarian-reform exposure (INCRA):** negligible at a ~10-family scale, but title due diligence matters (clean chain, no expropriation flags).

### Workarounds for a non-Brazilian participant (rural land)

Principle: Lei 5.709/71 regulates **acquisition of *ownership*** of rural land — its ementa targets "estrangeiro residente no País" and foreign legal entities (verified from the fetched source; the LexML snapshot is metadata-only, so full articles + INCRA/AGU positions need lawyer confirmation). INCRA/AGU interpret it to also reach non-resident foreigners and foreign-controlled Brazilian companies, so **assume non-Brazilian nationals are restricted** and verify.

Workarounds, ranked by legal cleanliness:

1. **Renter / tenant (locação or comodato).** The non-Brazilian pays rent to the vehicle and lives on the land **as a tenant, not an owner**. Clean and standard — possession/use is not "aquisição", so 5.709/71 is not triggered. Trade-off: no equity, no appreciation, no owner vote, less security. This is the "renter instead of owner" option — the safe default.
2. **Direito de superfície (right of surface).** A registrable real right (Código Civil arts. 1.369–1.377; Estatuto da Cidade arts. 21–24) to build/occupy for a term. Stronger than a lease (survives a sale of the land), still not *ownership* of the land. **Uncertain whether 5.709/71 treats it as "acquisition" — lawyer must confirm.** The best middle ground if they want to build a home.
3. **Urban land instead.** If the group accepts urban/peri-urban, 5.709/71 does not apply at all — foreigners own urban land freely.
4. **Minority, non-controlling stake in the SPE.** A Brazilian company is only "foreign-controlled" (and thus restricted) when foreigners hold majority/control. A small, non-controlling stake *may* not trigger it — but it's a **fraus-legis minefield** (indirect acquisition to evade the law) and only for small stakes. **Not recommended as a primary path.**

Also: **don't assume "spouse of a Brazilian" is automatically safe.** Under total community of property (comunhão universal), the foreign spouse acquires a property interest by marriage — which can itself raise a 5.709/71 question. The marriage regime (or a pre-nup) should be deliberate, not assumed.

**Design accommodation:** the structure can include a **"non-owner participant" class** (resident/tenant or surface-holder) alongside **owner members** — a non-Brazilian friend joins the community fully in spirit, without owning, without breaking the core ownership model. See `backbone/membership.md`.

### 🏙️ Urban — the catches to check *before* buying

1. **Zoning (Plano Diretor + municipal laws).** Is the parcel zoned for residential? Density limits? Mixed-use?
2. **Condo build = incorporação imobiliária.** Building a condo from scratch triggers the *incorporação* regime (Lei 4.591/64): memorial de incorporação, registration, construction-phase formalities. Heavier than rural co-ownership.
3. **No 5.709/71 restriction.** Foreigners may buy urban land freely — a real advantage if the group has non-Brazilian-national members.
4. **Permits & alvarás** for construction; municipal approvals add time and cost.
5. **IPTU + condominium costs** are ongoing urban burdens.

## The flexible mechanism (how we stay "not too loose, not too tight")

- The **purchase criteria** (contract §11) are fixed — price cap, location region, access, water/utilities, legal-clean title — but **land-type is a feasibility input, not a pre-commitment**.
- At the moment a specific parcel is considered, run the **land-type due-diligence checklist** above and surface the catches *before* the group votes.
- This keeps decisions concrete when they need to be, without forfeiting whichever opportunity (rural parcel or urban plot) actually appears.

## Highlighted catches (the ones that bite)

1. **Rural + non-Brazilian-national member → Lei 5.709/71.** The single biggest land-type-dependent risk.
2. **Rural → can't subdivide into 10 lots** → one-title co-ownership (a condominium *de fato*) — plan for shared land + exclusive-use areas, not 10 separate deeds.
3. **Rural → Reserva Legal / APPs** restrict buildable area — size the parcel accordingly.
4. **Urban → incorporação regime** if building a condo from scratch — heavier formalities.
5. **Urban → foreigners welcome** — if the group ends up with non-Brazilian members, urban is the frictionless path.

---

*BR-specific. For a Canadian land scenario, the equivalent checks are provincial planning acts + municipal zoning + land-titles due diligence — see the CA branch.*
