# TGCV — C09 SWIM Intervention / Counterfactual Design 001

**Status:** `DESIGN — DIRECT-EFFECT GATE OPEN / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Parent:** `TGCV_C09_DOMAIN_CANDIDATE_SWIM_REACTIVE_001.md`

## 1. Purpose

Define the minimum controlled design needed to determine whether an accessibility-changing intervention can be separated from any direct change to the trajectory-generating mechanism in SWIM Reactive.

This artifact is a design specification only. It authorizes no execution, rerun, dataset acquisition or claim upgrade.

## 2. Causal structure under test

Target chain:

`Z → ΔT_acc → Y`

where `Z` is the intervention, `T_acc` is reconstructed under a frozen accessibility predicate, and `Y` is the prespecified subsequent trajectory.

Forbidden ambiguity:

`Z → direct trajectory mechanism → Y`

If the intervention changes native policy inputs, objective/scoring rules, event ordering, execution capacity or observation procedure independently of accessibility, the design cannot identify the C09 effect without an additional identification strategy.

## 3. Intervention design candidate

The intervention shall modify one enabling condition that is part of the frozen accessibility predicate while keeping the following invariant:

- candidate transformation identities;
- transformation semantics;
- native adaptation policy;
- policy objective/scoring rule;
- trajectory observation procedure;
- post-decision horizon;
- simulator/model version;
- initial decision-time state/context except for the deliberately manipulated accessibility condition.

The intervention must produce a verified:

`T_acc,1 ≠ T_acc,0`.

The intervention is invalid if it directly commands, selects, suppresses or forces the target subsequent transformation sequence.

## 4. Counterfactual construction

Preferred design: matched treatment/control decision points drawn from the same frozen SWIM scenario family, with assignment randomized where technically feasible.

At the decision boundary, both arms must have reconstructible:

`S0, C0, L, Uτ, T_acc,0`.

Treatment receives `Z=1`; control receives `Z=0`.

The post-decision trajectory is then observed under the same native policy and fixed horizon `H`.

Existing Reactive-0 versus Reactive2 runs are **not** accepted as the treatment/control pair because the current evidence does not establish identical predecision state/history; A8 was explicitly classified `NOT_COMPARABLE`.

## 5. Primary outcome

Define the trajectory outcome before execution as an ordered representation of post-decision transformations/state transitions over fixed horizon `H`.

The primary contrast is:

`Y(1) − Y(0)`.

If only `H=1` can be reconstructed, the conclusion is restricted to one-step trajectory evidence and cannot be generalized to multi-step future trajectories.

## 6. Direct-effect exclusion gate

The candidate passes only if all are demonstrable before execution:

1. `Z` changes accessibility under the frozen predicate.
2. `Z` does not directly select or force a target trajectory.
3. Native policy/scoring semantics are unchanged.
4. Observation and measurement procedures are unchanged.
5. Any unavoidable state/context change caused by `Z` is either absent, frozen by design, or explicitly identified as a separate causal pathway.
6. Treatment assignment is not determined by post-treatment trajectory information.

Failure of any item blocks C09 execution authorization.

## 7. Manipulation validation fixture

Before any scientific execution, a design-validation fixture must demonstrate:

- identical candidate universe;
- identical policy and trajectory semantics;
- pre-treatment frozen state/context;
- treatment and control accessibility reconstructions;
- `ΔT_acc ≠ ∅` for treatment relative to control;
- no direct target-trajectory instruction embedded in `Z`.

This fixture validates the intervention mechanism only. It is not C09 causal evidence and must not be propagated as such.

## 8. Confounder register

At minimum inspect:

- baseline state/context imbalance;
- workload/event timing;
- resource availability outside the manipulated condition;
- adaptation-policy state/history;
- objective/scoring configuration;
- execution capacity;
- observation/measurement changes;
- interference between treatment and control runs;
- missing or dropped post-decision events.

Any unresolved material confounder blocks causal attribution.

## 9. Falsification / stop criteria

Stop and classify `INCONCLUSIVE` or `BLOCKED` if:

- `ΔT_acc` cannot be independently verified;
- treatment and control cannot be reconstructed as comparable;
- the intervention directly changes the trajectory mechanism;
- future trajectory information leaks into accessibility classification or treatment assignment;
- the prespecified trajectory cannot be independently reconstructed;
- post-hoc outcome-dependent eligibility is required;
- policy, objective or observation semantics drift between arms.

## 10. Current audit disposition

| Requirement | Disposition |
|---|---|
| Concrete accessibility intervention | `OPEN — mechanism requires fixture validation` |
| Verified `ΔT_acc` under intervention | `OPEN` |
| Direct-effect exclusion | `OPEN — decisive gate` |
| Treatment/control construction | `DESIGNED — not yet instantiated` |
| Randomization | `PREFERRED — feasibility to be audited` |
| Fixed trajectory criterion | `DESIGNABLE — exact operational definition required` |
| Fixed horizon | `DESIGNABLE — exact H required` |
| Confounder register | `DEFINED — protocol must instantiate` |
| Independent reconstruction | `SUPPORTED — exact package not yet frozen` |

## 11. Decision

**DESIGN STATUS = PASS WITH DECISIVE PRE-EXECUTION CONDITION OPEN.**

The causal comparison architecture is now sufficiently specified to proceed to an intervention-mechanism validation fixture. It is not yet sufficient to authorize scientific execution because the accessibility manipulation and direct-effect exclusion have not been empirically validated.

**EXECUTION AUTHORIZATION = NONE.**

**Next operation:** construct and audit the SWIM manipulation-validation fixture; do not execute the C09 treatment/control experiment until the direct-effect gate passes.
