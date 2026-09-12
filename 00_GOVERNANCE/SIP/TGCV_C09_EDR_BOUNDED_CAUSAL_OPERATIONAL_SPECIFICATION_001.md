# TGCV — C09 EDR Bounded Causal Operational Specification 001

**Status:** `CONTROLLED DESIGN / PREFLIGHT REQUIRED / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Candidate:** Southwestern-China Emergency Demand Response (EDR), 2019
**Parent:** `D-OPS-23_DEMAND_RESPONSE_BOUNDED_FORMAL_RULE_UTAU_PTAU_ADMISSIBILITY_AUDIT_v0.1.md`

## 1. Purpose

Freeze the minimum bounded operational specification required to decide whether the EDR experiment can support a C09 causal execution.

This specification is deliberately bounded. It does not require universal coverage of demand-response transformations or cross-domain validity.

## 2. Frozen analytical unit

**Unit:** one household-event observation.

**Decision time:** immediately before the EDR access/notification assignment for the declared event.

**Pre-treatment state:** `S0`, reconstructed only from information available before assignment.

**Pre-treatment context:** `C0`, including event window, programme conditions and applicable baseline/eligibility information.

**Outcome horizon:** the declared event window plus the prespecified post-event trajectory window. No extension after outcome inspection is permitted.

The published experiment used 15-minute smart-meter observations and six EDR trials between 18 July and 21 August 2019, with a final sample of 205,129 households.

## 3. Bounded transformation universe U_tau

`U_tau` is not the universe of every physically possible household action.

It is the **frozen operational action profile** for the declared event and observation resolution. Every admissible transformation class must be enumerable before treatment outcomes are inspected.

Minimum representation:

`U_tau = {tau_1, ..., tau_k}`

where each `tau_i` is a predeclared demand-side transformation class observable/reconstructible at the selected temporal resolution.

Examples may include bounded changes in controllable load timing, temporary reduction, or temporary increase, but no class may be added after observing treatment outcomes.

**Completeness criterion:** `U_tau` is complete if every transformation class admitted by the frozen operational profile is represented. This is bounded completeness, not universal completeness.

## 4. Accessibility rule P_tau

`P_tau(S0,C0,L)` must be frozen before outcome observation.

It may use only:

- pre-event household/state variables;
- declared event conditions;
- programme eligibility conditions;
- the frozen operational action profile;
- protocol-defined accessibility requirements.

It must not use:

- post-treatment consumption;
- realized reduction/increase;
- earned reward;
- realized trajectory;
- post-event state;
- any variable generated after assignment.

`T_acc,0 = {tau ∈ U_tau | P_tau(S0,C0,L)=1}`.

## 5. Accessibility intervention Z

The candidate intervention is randomized EDR access/notification assignment.

The treatment is admissible only if the frozen reconstruction demonstrates:

`T_acc,1(Z=1) ≠ T_acc,0(Z=0)`

for the relevant treated profile.

The assignment must not directly specify which consumption trajectory a household will realize. It changes the opportunity/eligibility/information condition through which demand-response transformations become accessible.

The published experiment reports randomized assignment to EDR conditions, including notification/access groups, supporting this identification structure.

## 6. Causal estimand

Primary estimand:

`τ = E[Y(1) − Y(0)]`

where `Y` is a prespecified trajectory representation rather than a generic immediate consumption outcome.

A minimum trajectory representation is an ordered sequence of post-decision transformation/state observations over the frozen horizon.

If the available evidence supports only a one-step endpoint, the claim is restricted to `H=1` and cannot be generalized to arbitrary multi-step trajectory effects.

## 7. Identification requirements

Before execution the preflight must verify:

1. treatment assignment is randomized according to the frozen protocol;
2. treatment/control eligibility is reconstructible independently;
3. baseline state/context precede assignment;
4. `T_acc,0` can be reconstructed without outcome leakage;
5. treatment changes accessibility rather than directly imposing `Y`;
6. the trajectory endpoint is fixed ex ante;
7. missingness/attrition rules are fixed before outcome inspection;
8. interference/spillover assumptions are explicitly recorded;
9. deviations from randomized assignment are independently identifiable;
10. all source provenance required for reconstruction is frozen.

## 8. Critical distinction: incentive versus accessibility

A monetary or informational treatment is not automatically a TGCV accessibility intervention.

The preflight must demonstrate that the treatment changes the set/structure of transformations that satisfy the frozen accessibility predicate. If treatment only changes the payoff attached to an unchanged `T_acc`, then the C09 accessibility manipulation fails.

Therefore:

`Z → ΔT_acc` must be independently demonstrated before interpreting `Z → Y` as evidence for C09.

## 9. Falsifiers

C09 execution is blocked if any condition holds:

- `T_acc,1 = T_acc,0` under the frozen operational representation;
- `U_tau` requires post-treatment information for enumeration;
- `P_tau` uses realized outcomes;
- treatment directly prescribes the trajectory;
- treatment changes the transition mechanism independently of accessibility in a way that cannot be separated;
- counterfactual/control reconstruction fails;
- trajectory cannot be independently reconstructed;
- missingness or attrition invalidates the identification strategy;
- the operational profile is changed after observing results.

## 10. Preflight evidence package

Required before any execution authorization:

- frozen event identifier;
- frozen unit inclusion/exclusion rule;
- frozen `S0` and `C0` schema;
- frozen `U_tau` enumeration and completeness justification;
- frozen `P_tau` specification;
- treatment-assignment record/provenance;
- explicit mapping demonstrating `Z → ΔT_acc`;
- trajectory schema and fixed horizon;
- counterfactual/control definition;
- missingness and attrition protocol;
- information-firewall declaration;
- integrity hashes for all frozen inputs;
- independent reconstruction procedure.

## 11. Decision boundary

This artifact is a **controlled operational specification**, not an execution authorization.

`EXECUTION AUTHORIZATION = NONE`

A successful preflight may authorize a separate C09 execution package. Failure of any critical gate produces `BLOCKED` or `INCONCLUSIVE` without redesign toward a positive result.

## 12. Claim boundary

Even a bounded causal PASS would support only the tested relation under the frozen EDR population, intervention, action profile, temporal horizon and identification assumptions.

It would not establish universality, cross-domain validity, predictive superiority, value creation, industrial utility or superiority over existing theories.

**Current disposition:** `READY FOR BOUNDED PREFLIGHT — NO EXECUTION AUTHORIZED`.
