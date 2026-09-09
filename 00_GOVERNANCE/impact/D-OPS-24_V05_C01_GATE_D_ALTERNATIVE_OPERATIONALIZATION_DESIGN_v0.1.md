# D-OPS-24 / C-01 Gate-D Alternative Operationalization Design v0.1

**Date:** 2026-09-09  
**Status:** DRAFT / DESIGN — EXECUTION NOT AUTHORIZED  
**Authorization basis:** EXT-UPD-4.5

## 1. Purpose

Define a materially different operational route for testing the downstream TGCV chain in C-01 after the first Gate-D route remained INDETERMINATE:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

The alternative route must determine whether the boundary identified in C-01 is an operationalization problem rather than a limitation of the extension itself.

## 2. Alternative principle

The first route attempted to construct Reach and Trajectory primarily as explicit downstream sets derived from native successor/reachability rules. The alternative route will use a **finite decision-tree / transition-graph construction over explicitly enumerated candidate control reconfigurations**, rather than requiring the source to supply a pre-existing native Reach or Trajectory object.

The construction is analytical, not outcome-driven:

1. Freeze a single C-01 aircraft/control state and context.
2. Construct a bounded candidate transformation universe `Uτ,D` from the documented control-effectors and admissible restructuring operations.
3. Evaluate each candidate against pre-outcome native feasibility constraints.
4. For every feasible candidate, construct its native successor configuration using the documented control/model relation.
5. The resulting successor nodes form the bounded one-step Reach set.
6. Reapply the same rule recursively for a fixed finite horizon `h`, producing a generated trajectory tree.
7. Only after the upstream graph is frozen, introduce documented engineering performance/outcome evidence.
8. Introduce Value only if an independent native valuation criterion exists.

Thus Reach and Trajectory are **generated analytical sets**, while observed redesign sequences are retained only as separate evidence.

## 3. Formal objects

For a frozen C-01 state/context `(S_t,C_t)`:

- `Uτ,D*` = bounded, explicitly enumerated native candidate transformations relevant to the selected control-system configuration.
- `Pτ,D(S_t,C_t)` = native pre-outcome feasibility predicate.
- `T_acc,D,t = {τ ∈ Uτ,D* | Pτ,D(S_t,C_t)=1}`.
- `Succ_D(S_t,C_t,τ)` = independently specified native successor configuration/set for feasible `τ`.
- `Reach_D^1(t) = {Succ_D(S_t,C_t,τ) | τ ∈ T_acc,D,t}`.
- `Reach_D^h(t)` = recursively generated reachable configuration set up to fixed horizon `h`.
- `ΔReach_D` = controlled difference between Reach sets under two frozen comparison conditions.
- `Traj_D^h` = set of generated ordered paths through the reachable transition graph up to horizon `h`.
- `ΔTrajectory_D` = controlled difference between generated trajectory sets under the same comparison rule.
- `Outcome_D` = downstream engineering event/performance state introduced only after the upstream graph is frozen.
- `Value_D` = native-domain valuation/desirability construct only if independently evidenced.

No object is defined by observed success.

## 4. D1 — ΔT_acc → ΔReach

### Required construction

A D1 PASS requires:

D1.1 A finite or explicitly bounded `Uτ,D*` can be constructed without using downstream outcomes.

D1.2 Each candidate transformation is distinguishable at the native engineering level.

D1.3 `Pτ,D` is evaluated from pre-outcome state/context and native feasibility constraints.

D1.4 Each accessible transformation has an independently evaluable `Succ_D` rule.

D1.5 `Reach_D^1` can therefore be constructed without treating the observed redesign as the reachable set.

D1.6 Two controlled states/contexts can be compared while holding common dimensions fixed or explicitly accounting for differences.

D1.7 `ΔReach_D` is computed as a change in generated reachable configuration membership, not a change in performance.

D1.8 Empty reachable sets are representable.

### D1 decision

PASS only if D1.1–D1.8 pass. Otherwise INDETERMINATE unless a direct contradiction establishes FAIL.

## 5. D2 — ΔReach → ΔTrajectory

### Required construction

D2.1 Fix a finite horizon `h` before outcome evidence is consulted.

D2.2 Generate trajectories from the Reach transition graph.

D2.3 Preserve temporal ordering of generated transformations/configurations.

D2.4 Distinguish generated trajectory set from the historically observed aircraft sequence.

D2.5 Construct `ΔTrajectory_D` through the same controlled comparison used for `ΔReach_D`.

D2.6 Empty/no-path cases are representable.

### D2 decision

PASS only if D2.1–D2.6 pass. Otherwise INDETERMINATE unless a direct contradiction establishes FAIL.

## 6. D3 — ΔTrajectory → Outcome

Outcome evidence is introduced only after `Traj_D^h` and `ΔTrajectory_D` are frozen.

Required:

D3.1 Outcome is independently identifiable.

D3.2 Outcome is temporally downstream.

D3.3 Outcome evidence cannot alter upstream accessibility, Reach or generated Trajectory construction.

D3.4 No causal claim is inferred from temporal ordering alone.

D3.5 Unresolved/neutral outcomes remain representable.

D3 PASS requires a traceable mapping from the generated trajectory comparison to a distinct downstream outcome construct. Otherwise INDETERMINATE.

## 7. D4 — Outcome → Value

Value remains the strictest extension test.

Required:

D4.1 A native engineering source independently defines desirability, utility, preference, mission suitability, economic value or equivalent valuation.

D4.2 The criterion is not invented from TGCV Value.

D4.3 Outcome and Value are analytically distinct.

D4.4 Positive, neutral, negative and unresolved valuation cases are representable.

D4.5 The value criterion is introduced only after Outcome has been frozen.

D4.6 Engineering performance alone is classified as Outcome unless an independent native valuation rule explicitly makes it Value.

D4.7 No optimization objective is introduced.

If D4.1–D4.7 cannot be demonstrated, D4 = INDETERMINATE.

## 8. Evidence protocol

Evidence hierarchy:

1. C-01 primary engineering source;
2. explicit mathematical/control specifications contained in or directly supporting C-01;
3. authoritative native-domain documentation required to specify control/reconfiguration rules;
4. reproducible native model or calculation;
5. worked engineering example;
6. secondary interpretation only as contextual support.

Every evidence record must contain:

`upstream construct → downstream construct → native rule → construction order → evidence → non-circularity test → non-collapse test → unresolved cases → decision`.

## 9. Counterfactual safeguard

The observed redesign/reconfiguration cannot be treated as the complete accessible set.

The alternative route succeeds only if at least the relevant competing candidate transformations can be generated and evaluated independently of which transformation was historically observed.

If the native record permits only reconstruction of the observed redesign, but not independent candidate generation/evaluation, the corresponding gate is INDETERMINATE.

## 10. Decision rule

Each D1–D4 receives `PASS`, `INDETERMINATE` or `FAIL`.

Overall:

- `PASS` = D1, D2, D3 and D4 all PASS;
- `INDETERMINATE` = no mandatory contradiction, but at least one component is INDETERMINATE;
- `FAIL` = a mandatory frozen constraint is demonstrably violated.

A D outcome does not retroactively modify A-C.

## 11. Execution boundary

This document is design only.

No execution, new source search, dataset acquisition, empirical calculation, outcome analysis, Value analysis, causal inference or second-domain search is authorized by this design.

Execution requires:

`design → design audit → preflight → explicit execution authorization`.

## 12. Expected diagnostic value

The route is deliberately diagnostic rather than confirmatory.

If it passes, C-01 may support a bounded downstream extension through the generated transition graph.

If D1/D2 remain indeterminate, the limitation is likely a lack of independently reconstructable native transition rules in the source.

If D4 remains indeterminate while D1-D3 pass, the result isolates Value as the extension boundary rather than treating that boundary as a failure of the Core.

If the route fails because the construction necessarily imports outcome information or collapses native and TGCV objects, the second-domain option should be considered only after propagation and a new governance decision.
