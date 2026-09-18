# TGCV — VSL Experimental Protocol B v0.1
## Petroleum / Petrochemical / Natural-Gas LCC

**Status:** DRAFT — NOT FROZEN  
**Date:** 2026-09-19  
**Frozen VSL:** `TGCV_VSL_DOMAIN_SPECIFIC_FREEZE_B_PETROLEUM_LCC_v0.1.md`

## 1. Experimental question

Can a pre-specified intervention that changes the accessible transformation space of a petroleum/petrochemical/natural-gas facility or option system produce a reproducible change in downstream trajectories and in the independently frozen LCC-based Value construct?

This is a protocol question, not a universal causal claim.

## 2. Unit and domain

One explicitly identified facility/associated-activity option comparison. Facility scope, population/context and admissible transformations must be frozen before execution.

## 3. Treatment/intervention

The treatment is a pre-specified modification intended to alter `T_acc` without modifying the Value layer. Exact intervention and assignment mechanism remain protocol-specific and must be frozen before execution.

## 4. Baseline and accessibility

Freeze `S_0`, `C_0`, `T_acc,0`, the admissibility predicate, and the procedure for constructing `T_acc,1`.

`ΔT_acc = T_acc,1 − T_acc,0` must be computed independently of Outcome and V*.

## 5. Reference/counterfactual

Freeze the competing option/baseline before observing post-treatment results. Reference and treatment must use the same frozen valuation scope and analysis period.

## 6. Trajectory

Freeze trajectory-selection/execution before results. No trajectory may be selected because it improves LCC, NPV or V*.

## 7. Outcome

Outcome is the pre-specified life-cycle cost/economic evaluation quantity for the frozen option comparison and analysis period. Outcome construction precedes and remains independent of V*.

## 8. Value

Use only the frozen B VSL. No post-hoc change to perspective, reference, scope, horizon, directionality, aggregation, or missingness rules is permitted.

## 9. Design / controls

Where a causal effect is intended, specify assignment/randomization, control/null condition, sample or scenario generation, and blocking/stratification before execution.

## 10. Metrics

Minimum recorded quantities:
- `ΔT_acc`;
- trajectory identity/metrics;
- Outcome/LCC;
- `V*`;
- treatment/reference contrast;
- missingness and uncertainty indicators.

## 11. Integrity

Freeze inputs, code/version, dataset/configuration hashes, runtime environment, random seeds where applicable, and execution logs.

## 12. Independent reconstruction

An independent executor must receive the frozen package without prior outcome interpretation and reconstruct all critical objects required by the claim.

## 13. Stopping/failure rules

Execution stops or is classified non-evidence if frozen inputs, admissibility, reference, trajectory rule, VSL or integrity checks fail.

## 14. Claim boundary

Even a successful run does not establish universal Value, cross-domain comparability, or a universal causal law.

## 15. Freeze blockers

Not yet frozen: concrete intervention, population/context, assignment/randomization, sample/scenario generation, exact control/null, thresholds, and complete executable bundle.

**Current disposition:** `PROTOCOL_NOT_FROZEN`.