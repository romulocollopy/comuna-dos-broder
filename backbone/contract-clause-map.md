# Contract — Clause Map

The skeleton of the eventual agreement. Each clause states **what it must do** and the **open parameters** a lawyer finalizes. This is branch-agnostic with a Brazil-primary bias (BRL, Brazilian vehicle); Canadian/other branch deltas are noted inline.

> ⚠️ Not a contract. A clause map — the structured brief a lawyer turns into final language after the securities + cross-border opinions land.

---

## 0. Parties, recitals, and governing law
- Identify each member (and their **residency profile** per `docs/cross-border.md` §1: resident / non-resident / non-Brazilian-national).
- Identify the vehicle (SPE/cooperativa — BR branch) and the organizer(s).
- **Recitals** must state the **shared-living purpose** explicitly (not investment, not profit). This is the single most protective sentence in the document.
- Governing law = law of the land's jurisdiction; the contract's obligations otherwise follow that law. Language: PT with a working EN version.

## 1. Definitions
Incorporate `backbone/glossary.md` verbatim. Capitalized terms = defined terms.

## 2. Purpose and nature
- Declare: a **community land-and-living arrangement**, not an investment product, not a security, not insurance.
- Members join as **co-owners and co-decision-makers**, not passive investors.
- Non-profit orientation for the *living* phase; capital is returned/recovered, not "invested for return."

## 3. Membership
- **Resolved:** individuals are the legal members; a **family unit** = the named individuals of one household jointly holding one **severable share**. See `backbone/membership.md`.
- Both co-holders are named parties; the share is joint and flagged as matrimonial property.
- Admission (supermajority), removal (cause), resignation (→ §8).
- Voting: a joint family share votes as one (single delegate); a split share votes independently per holder.

## 4. Contributions
- Types: money (BRL), services, goods. Valuation of money-equivalents at agreed FMV, documented by a **contribution statement** each time.
- **BRL unit of account.** Foreign members convert at the câmbio rate on the contribution date (record the rate).
- Cadence (encourage less-frequent/larger for members abroad — see cross-border §3).
- **Temporary postponement / discount (hardship):** a member in financial difficulty may pause or reduce contributions for a defined period, with written notice + group approval; the shortfall is absorbed by reinvested rental income (and/or the reserve), **not** by the other members' stakes.
- Each member's minimum/expected commitment; consequences of varying.

## 5. Reserves
- **Land reserve** (`100% − x%`) and **safety reserve** (`x%`, default 10%). `x` is a contract parameter, amendable by supermajority.
- Segregated sub-accounts in the vehicle.
- **Rental income (reinvested):** any rent the land earns flows into the **land reserve** as collective capital — **never distributed** to members. It accelerates the fund (members stop paying earlier) and backs the hardship-postponement mechanism (§4).
- **Reversion:** on the defined **success milestone(s)** (e.g. land purchased + registered in the vehicle's name), the unused safety reserve reverts to the land reserve / is distributed pro-rata.
- Explicit statement: the safety reserve is a **contractual reserve fund, not insurance** (mitigates insurance-regulation risk).

## 6. Ownership and stakes
- Stake = accumulated land-reserve contributions, adjusted for dilution/forfeiture/reversion.
- Mapping stake → quota/share ownership in the vehicle (SPE quotaholders).
- Unequal stakes are expected; no minimum parity.

## 7. Governance and voting
- Decision matrix (from `backbone/model.md` §8): delegated admin vs supermajority reserved matters vs per-person communal votes.
- **Organizer-as-participant safeguards** (Romulo is both): no self-dealing; the organizer's admin acts are documented and reviewable; on any matter where the organizer has a material personal interest, the organizer abstains from the deciding vote; independent valuation on organizer-adjacent transactions.
- Anti-deadlock: shotgun / buy-sell clause.

## 8. Withdrawal (exit)
- Cooling-off window (e.g. 30–60 days) → 100% of contribution.
- **Valuation method** (choose one, fixed in contract): nominal / nominal+index (IPCA) / pro-rata market. Given the shared-living purpose, **nominal + inflation index** is the recommended default (recovers purchasing power without speculation).
- **Vesting/penalty schedule** (graduated by phase).
- **Payout waterfall:** safety reserve → replacement member → other members (right of first refusal) → partial land liquidation (last resort, group vote).
- **Queue rule** for simultaneous withdrawals (pro-rata + FIFO).

## 9. Default and forfeiture
- Grace period → cure → dilution → forfeiture. Forfeited amounts → safety reserve.
- No acceleration that forces land sale.

## 10. Death, incapacity, divorce, bankruptcy
- **Death/incapacity:** buy-sell at formula price (group or members have right of first refusal); on death of one co-holder, the survivor's half is preserved.
- **Divorce/separation (family share) — the four pre-agreed outcomes** (`backbone/membership.md`): (1) withdraw individually · (2) compensate/buyout · (3) **split in two** into independent half-shares · (4) **top up** a half-share back to full. Default if the ex-partners can't agree: split (outcome 3) `[confirm with lawyer]`.
- **Bankruptcy/creditors:** land held in the vehicle (creditors reach shares, not land); transfer restricted by right of first refusal.

## 11. The land purchase
- Pre-agreed **purchase criteria** (location, price cap, zoning, buildability).
- **Due diligence** before purchase: title, zoning, environmental, access, utilities — plus **rural vs urban** determination (Lei 5.709/71 if rural + non-Brazilian members).
- Purchase requires supermajority. Title registered **in the vehicle's name**.

## 12. Build and occupation phase
- Once homes exist, a **condominium/co-op layer** governs occupation (Lei 4.591/64 in BR), while the vehicle remains landowner.
- Rules for common areas, costs, maintenance, and long-term governance (one-person-one-vote for communal matters).

## 13. Currency, indexation, and cross-border
- BRL unit of account; index long-term obligations to IPCA.
- Each member's residency profile determines their tax/remittance obligations (see `docs/cross-border.md`).
- Vehicle obligations: IED registration and IRRF withholding for non-resident members.

## 14. Tax
- Allocation: each member is responsible for their own residency's tax (T1135 in CA, CBE in BR, EU equivalents); the vehicle handles Brazilian withholding.
- Brazil–Canada treaty (Decreto 92.318/86) for double-taxation relief.
- Money-equivalent contributions treated as taxable barter.

## 15. Dispute resolution
- Mediation first, then arbitration (Lei 9.307/96 in BR), with a defined seat and the land's governing law.

## 16. Amendment
- Supermajority to amend; unanimous for the purpose clause and the reserve % (or supermajority — decide).

## 17. Term, termination, and winding down
- Duration (e.g. until success milestone + occupation, or perpetual with exit).
- Voluntary/forced liquidation: pro-rata distribution; sale process; order of distribution.

## 18. Representations and warranties
- Each member confirms: tax-residency status (per self-declaration), no reliance on investment returns, understanding that this is **not an investment product**.
- This clause is the securities defense made contractual.

## 19. Miscellaneous
- Severability, notices, entire agreement, force majeure.

---

### Annex A — worked example
A one-page, plain-language example: "Maria contributes R$X/month; after 3 years she withdraws; here's exactly what she gets back, step by step." This is what you hand to a hesitant friend.

### Open parameters still to fix
- `x` (safety-reserve %), valuation method, vesting schedule, success milestone(s), vote thresholds, family-vs-individual membership, cooling-off length, land-type (rural/urban), land location.
