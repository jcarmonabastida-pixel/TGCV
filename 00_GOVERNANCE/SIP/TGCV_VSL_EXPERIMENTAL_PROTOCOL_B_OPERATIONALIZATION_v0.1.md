# TGCV — VSL Experimental Protocol B Operationalization v0.1
## Petroleum / Petrochemical / Natural-Gas LCC

**Status:** OPERATIONAL DRAFT — NOT FROZEN  
**Date:** 2026-09-19  
**Parent:** `TGCV_VSL_EXPERIMENTAL_PROTOCOL_B_PETROLEUM_LCC_v0.1.md`  
**Frozen VSL:** `TGCV_VSL_DOMAIN_SPECIFIC_FREEZE_B_PETROLEUM_LCC_v0.1.md`

## 1. Operational unit
One synthetic, fully specified facility/option decision system represented as a finite transformation system. The synthetic unit isolates TGCV mechanism and is not evidence about a real petroleum facility.

## 2. Treatment
Treatment is a pre-frozen structural accessibility intervention that changes the admissible transformation relation while leaving the valuation contract unchanged. Exact graph and intervention operator must be generated from the frozen fixture.

## 3. Baseline / reference / null
- Baseline: frozen state `S_0` and context `C_0`.
- Reference/null: identical fixture with no accessibility intervention.
- Treatment: identical fixture with the specified accessibility intervention.
- Reference and treatment share the same VSL scope and analysis horizon.

## 4. Accessibility
`T_acc,0` is generated from the frozen admissibility predicate. `T_acc,1` is generated after intervention using the same predicate. `ΔT_acc` is their structural difference.

## 5. Assignment
Primary design: paired within-fixture intervention/reference comparison. If multiple fixtures are used, fixture generation, assignment and random seed must be frozen before execution.

## 6. Trajectory
Trajectory execution is deterministic under the frozen rule and cannot inspect LCC, NPV, V* or post-intervention outcome.

## 7. Outcome
Outcome is the frozen B-VSL life-cycle economic evaluation quantity over the frozen horizon. Each cost/economic component in the synthetic fixture must be generated from pre-frozen state/transition attributes and cannot depend on observed V*.

## 8. V*
`V* = -LCC` exactly as frozen in B VSL. NPV may be retained as a secondary outcome but cannot replace V*.

## 9. Metrics
- `ΔT_acc` size and identity;
- trajectory identity/coverage;
- LCC and `V*`;
- paired treatment-reference difference;
- reconstruction equality;
- missingness/uncertainty status.

## 10. Executor-2
Executor-2 receives only the frozen fixture, protocol, VSL, code/version and integrity manifest and independently reconstructs all critical objects without Executor-1 interpretation.

## 11. Required freeze blockers
Before protocol freeze, specify exact facility/option fixture schema, state variables, transformation operators, admissibility predicate, intervention operator, trajectory rule, economic-generation rule, number of fixtures, assignment/seed rule, thresholds, and complete executable bundle.

**Disposition:** `OPERATIONALIZATION_NOT_FROZEN`.