# TGCV — VSL Experimental Protocol A Operationalization v0.1
## Built Assets / Infrastructure LCC

**Status:** OPERATIONAL DRAFT — NOT FROZEN  
**Date:** 2026-09-19  
**Parent:** `TGCV_VSL_EXPERIMENTAL_PROTOCOL_A_BUILT_ASSETS_LCC_v0.1.md`  
**Frozen VSL:** `TGCV_VSL_DOMAIN_SPECIFIC_FREEZE_A_BUILT_ASSETS_LCC_v0.1.md`

## 1. Operational unit
One synthetic, fully specified built-asset decision unit represented as a finite transformation system. The synthetic unit is used to isolate the TGCV mechanism; it is not evidence about a real building.

## 2. Treatment
Treatment is a pre-frozen structural accessibility intervention that changes the admissible transformation relation while leaving the valuation contract unchanged. The exact transformation graph and intervention operator must be generated from the frozen fixture before execution.

## 3. Baseline / reference / null
- Baseline: frozen state `S_0` and context `C_0`.
- Reference/null: identical frozen fixture with no accessibility intervention.
- Treatment: identical fixture with the specified accessibility intervention.
- Reference and treatment share the same VSL scope and analysis horizon.

## 4. Accessibility
`T_acc,0` is generated from the frozen admissibility predicate. `T_acc,1` is generated after the intervention using the same predicate. `ΔT_acc` is the structural difference between the two frozen representations.

## 5. Assignment
Primary design: paired within-fixture intervention/reference comparison. If multiple fixtures are used, fixture generation, assignment and random seed must be frozen before execution.

## 6. Trajectory
Trajectory execution is deterministic under the frozen trajectory-selection rule. The rule cannot inspect LCC, V* or post-intervention outcome.

## 7. Outcome
Outcome is the frozen A-VSL life-cycle cost for the decision unit over the frozen horizon. In a synthetic fixture, each cost component must be explicitly generated from pre-frozen state/transition attributes; no component may depend on observed V*.

## 8. V*
`V* = -LCC` exactly as frozen in A VSL. No alternative valuation rule is permitted.

## 9. Metrics
- `ΔT_acc` size and identity;
- trajectory identity/coverage;
- LCC and `V*`;
- paired treatment-reference difference;
- reconstruction equality;
- missingness/uncertainty status.

## 10. Executor-2
Executor-2 receives only the frozen fixture, protocol, VSL, code/version and integrity manifest. Executor-2 must reconstruct baseline, treatment, `T_acc,0`, `T_acc,1`, trajectory, LCC and V* without access to Executor-1 interpretation.

## 11. Required freeze blockers
Before protocol freeze, specify the exact finite fixture schema, state variables, transformation operators, admissibility predicate, intervention operator, trajectory rule, cost-generation rule, number of fixtures, randomization/seed rule, thresholds, and complete executable bundle.

**Disposition:** `OPERATIONALIZATION_NOT_FROZEN`.