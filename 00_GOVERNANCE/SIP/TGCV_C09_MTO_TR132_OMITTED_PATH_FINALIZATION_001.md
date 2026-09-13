# TGCV — C09 MTO TR-132 Omitted-Path Finalization 001

**Status:** `COMPLETED — TR-132 PASS FOR BOUNDED CANDIDATE / C09 PRE-FLIGHT NOT YET AUTHORIZED`
**Date:** 2026-09-13
**Candidate:** Moving to Opportunity (MTO)
**Parent:** `TGCV_C09_MTO_TR132_SUFFICIENCY_AUDIT_001.md`
**Gate:** `TGCV_C09_TR132_SUFFICIENCY_GATE_001.md`
**Execution authorization:** `NONE`

## 1. Purpose

Freeze a bounded MTO causal representation sufficiently narrow to permit a C09 operational preflight without requiring complete system-wide housing `T_acc`.

This artifact is a design finalization only. It is not a causal result and does not authorize execution.

## 2. Final bounded transformation profile

`U* = {first residential relocation transformation from baseline dwelling to a dwelling whose census tract satisfies the declared voucher-location predicate during the frozen first-move window}`

The causal contrast is **LPV versus TRV**, not LPV versus no-voucher control.

Rationale: TRV supplies voucher access while removing the LPV low-poverty location restriction, making it the sharper comparator for the specific accessibility mechanism under test.

## 3. Frozen accessibility predicates

For the declared first-move transformation `τ`:

`P_LPV(τ) = eligible household + destination tract satisfies the ex-ante LPV low-poverty rule + transformation occurs within the frozen first-move eligibility window.`

`P_TRV(τ) = eligible household + destination satisfies the corresponding TRV programme eligibility conditions + transformation occurs within the same frozen first-move window.`

The predicates are defined from pre-treatment programme rules and baseline eligibility. Realized post-treatment outcomes must not be used to redefine either predicate.

## 4. Causal estimand boundary

The bounded C09 question is:

> Does assignment to the LPV accessibility rule, relative to the otherwise comparable TRV rule, causally change the subsequent bounded trajectory associated with first residential relocation and its prespecified downstream endpoint?

The claim is deliberately narrower than “housing vouchers cause trajectories” and narrower than any claim about the complete housing transformation space.

## 5. Trajectory endpoint

For the next operational preflight, `Y` must be selected exclusively from an endpoint demonstrably reconstructible from the admissible public-use MTO package.

Residential-history variables are **not** admitted merely because they exist in richer restricted datasets. If the selected endpoint requires restricted quarterly residential histories, the candidate returns to `CONDITIONAL / NOT ADMITTED` rather than importing those data.

The endpoint must be:

- fixed before outcome inspection;
- independent of the accessibility classification;
- observed over a fixed horizon;
- reproducible from the declared public-use package;
- interpretable as a subsequent trajectory/outcome rather than a relabelling of treatment assignment.

## 6. Omitted-path sufficiency test

The bounded profile is considered sufficient only for the following declared causal contrast:

`LPV rule → first-move accessibility contrast → prespecified downstream Y`.

The following are explicitly outside the estimand and cannot be used to reinterpret the result:

- second and later residential moves;
- unrestricted housing-market transformations outside the first-move profile;
- realized take-up as a proxy for accessibility;
- downstream neighbourhood classification used to define treatment;
- post-treatment voucher usage to define `P_tau`.

These omissions do not invalidate the bounded question **provided Y does not require them for its causal interpretation**. Therefore endpoint selection is now the decisive remaining operational condition.

## 7. Direct-effect and mediator boundary

The LPV intervention includes programme components beyond the geographic poverty restriction, including mobility counselling/assistance. Therefore the experiment must not claim that an observed outcome difference is caused *solely* by `ΔT_acc` unless the operational preflight can isolate the location-rule component.

Accordingly, C09 execution may only test the bounded causal effect of the **LPV programme assignment versus TRV assignment as an intervention that changes the declared accessibility regime**.

A stronger mediation claim:

`LPV assignment → ΔT_acc alone → Y`

is **not authorized** by this artifact.

## 8. TR-132 decision

### Mandatory conditions

- bounded `U*`: **PASS**
- ex-ante accessibility predicate: **PASS**
- distinguishable LPV/TRV accessibility regimes: **PASS at rule level**
- credible counterfactual: **PASS**
- no post-treatment leakage: **PASS by design**
- omitted-path sufficiency: **PASS within the explicitly bounded first-move question, conditional on endpoint eligibility**
- independently reconstructible endpoint: **OPEN — final endpoint must be selected and verified**

Therefore:

`TR-132 = PASS FOR BOUNDED DESIGN / OPERATIONAL ENDPOINT GATE OPEN`

## 9. Governance decision

MTO is retained as the **highest-priority active C09 candidate**.

The next operation is **MTO endpoint/public-package preflight**, not causal execution.

No restricted-data request.
No data acquisition.
No model fitting.
No claim upgrade.
No matrix update.
No Core change.
No AWS/Rust/SWIM execution.
No execution authorization.
