# Pitfalls, Risks & Open Questions

The register of things that can go wrong, each with the mitigation we're baking in. This is the "we've thought about the scary parts" document — both a working risk log and (plain-language) an appendix to the proposal.

**Legend:** 🔴 legal blocker · 🟠 major financial risk · 🟡 operational risk · ⚪ design decision

---

## 🔴 The securities-law elephant

Pooling money from multiple people to invest with an expectation of profit can make the arrangement a **collective investment scheme / security**, pulling in regulators (CVM in BR; provincial securities commissions in CA).

- **BR:** Lei 6.385/76, art. 2º, IX — "contrato de investimento coletivo" is a broad catch-all. A genuine company (SPE) whose members are *also* owners and co-decision-makers is less likely to be recharacterized than a "manager pools money" arrangement.
- **CA:** the "investment contract" test (adopted in *Pacific Coast Coin Exchange v. OSC*, from the US *Howey* test). Private placements to friends/family may rely on prospectus exemptions (NI 45-106), but "pooled fund → buy land → expect appreciation" smells like a security.

**Mitigation:** structure as genuine co-ownership/company with active members (not passive investors), document the *shared-living purpose* (not speculation), keep it private and relationship-based, and get a lawyer's opinion before anyone contributes. 🔴 **Do not collect money before this is confirmed.**

## 🔴 "Insurance" framing

Calling the reserve "insurance" can trigger **insurance regulation** (unlicensed insurance activity). It must be a **contractual reserve fund** in the vehicle's own money — never "we insure your investment."

**Mitigation:** name it "reserve fund / safety reserve," draft it as a contractual pool, and have a lawyer confirm the wording.

## 🟠 Withdrawal liquidity (illiquid land)

After purchase, the money is in land. Paying a withdrawing member in cash can force a bad sale.

**Mitigation:** the insurance reserve is *for exactly this*; plus a defined payout waterfall (reserve → new member → other members → land liquidation as last resort), plus a queuing rule for simultaneous exits.

## 🟠 Simultaneous exits ("run on the reserve")

Multiple withdrawals at once can exhaust the reserve.

**Mitigation:** explicit pro-rata + queue rule (model §6.4); reserve sized to a stress scenario.

## 🟠 Valuation disputes on exit

"Your stake is worth X" is inherently contentious mid-project.

**Mitigation:** choose the valuation method in the contract (nominal / indexed / pro-rata market) and fix an independent appraiser; never leave valuation to exit-time negotiation.

## 🟠 Uneven contributions and control

A large contributor can dominate; small contributors can feel locked out.

**Mitigation:** capital-weighted votes for financial matters, per-person votes for communal matters (model §8).

## 🟠 Default on future contributions

Someone stops paying.

**Mitigation:** grace period → cure → dilution/forfeiture schedule, with forfeited amounts feeding the insurance reserve (so the group, not the defaulter, benefits).

## 🟠 Death / incapacity

A member's stake passes to heirs who may not want to live there.

**Mitigation:** buy-sell on death (the group or a member buys the stake at a formula price); keep heirs informed at formation.

## 🟠 Divorce / matrimonial claims

A spouse may claim part of the stake.

**Mitigation:** spousal awareness/waiver at formation; the vehicle structure can isolate the stake.

## 🟠 Bankruptcy / creditors

A member's creditors can reach their stake.

**Mitigation:** holding the land in a vehicle (company/partnership) means creditors reach *shares*, not the land directly, and the contract can restrict transfer (right of first refusal).

## 🟠 Currency & FX

BRL and CAD contributions over 10 years = real FX risk and reporting burden.

**Mitigation:** fix a unit of account; index to inflation; report cross-border holdings (BR: CBE/capitais; CA: T1135).

## 🟠 Tax on "money-equivalent" contributions

Barter (services/goods for a stake) is taxable income.

**Mitigation:** value at fair market value, document as invoice-equivalent, and treat as taxable on both sides.

## 🟠 Appreciation vs loss

Land can lose value. Who bears it?

**Mitigation:** proportional sharing of gain *and* loss, stated plainly — no "you can't lose" promises.

## 🟡 Decision deadlock

Group splits 50/50 on a big call.

**Mitigation:** supermajority thresholds + a shotgun/buy-sell clause.

## 🟡 The "right land" disagreement

Members disagree on what/where to buy.

**Mitigation:** pre-agree purchase criteria (location, price cap, zoning) and vote thresholds before the fund is large enough to buy.

## 🟡 Zoning / permits / buildability

The land can't be built on (rural zoning, environmental restrictions, lack of permits).

**Mitigation:** due diligence before purchase: title, zoning, environmental, access, utilities. BR: Estatuto da Cidade (Lei 10.257/2001) and municipal zoning; CA: municipal zoning/by-laws + provincial planning acts.

## 🟡 Maintenance & liability pre-build

Vacant land still needs care, taxes, and liability coverage.

**Mitigation:** budget ongoing costs into the reserve; liability insurance for the vehicle.

## 🟡 Two-phase governance (buy → live)

Before homes: financial governance. After homes: communal governance (condominium / housing co-op).

**Mitigation:** design both phases up front; the vehicle holds the land, and a condominium/co-op layer governs occupation (Lei 4.591/64 in BR; housing co-op / condo rules in CA).

## ⚪ What "success" means

When does the insurance reserve revert? Ambiguity = dispute.

**Mitigation:** define success milestones explicitly in the contract.

## ⚪ Reserve percentage

The % to the insurance reserve is a design choice, not a law.

**Mitigation:** pick a default (e.g. 10%), stress-test it, allow supermajority amendment.

## ⚪ Reusable template vs specific group

Whether this is a general structure for others or one specific group changes everything downstream.

**Mitigation:** resolve the open questions first (see research plan).
