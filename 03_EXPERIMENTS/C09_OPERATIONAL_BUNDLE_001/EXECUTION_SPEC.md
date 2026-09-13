# TGCV C09 Operational Execution Bundle 001

**Status:** `FROZEN — EXECUTION NOT YET AUTHORIZED`
**Freeze scope:** operational definitions, fixture, randomization, null control, endpoint, executor contract and reconstruction boundary.
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories.

## 1. Frozen experiment

Synthetic finite transformation system; 256 independent replicas; fixed horizon H=1.

For every unit `u`:
- `U={A,B,C}`.
- `S0 = int(SHA256(unit_id)[0:8],16) mod 10`.
- `C0 = {capacity:1, policy_version:"C09-001"}`.
- Transformation deltas: A=+1, B=+3, C=0.
- Fixed scores: A=1.0, B=2.0, C=0.5.
- B requires resource R1; A and C require no resource.

Accessibility:
- control Z=0: R1=false, therefore `T_acc,0={A,C}`;
- treatment Z=1: R1=true, therefore `T_acc,1={A,B,C}`;
- null arm uses R1=false and must therefore preserve `{A,C}`.

The treatment flag may be consumed only by the accessibility predicate. It must not be read by transition, score, policy, metric, observation, or randomization code.

## 2. Decision policy P

`P(S,C,T_acc)` selects the accessible transformation with maximum fixed score; ties are resolved lexicographically A<B<C. No treatment flag is an input to P.

## 3. Transition rule G

For selected transformation `u`, `S1=S0+delta(u)`. Context remains unchanged. No other state transition exists at H=1.

## 4. Primary endpoint Y

`Y = S1`, encoded as an integer. Primary estimand is the arithmetic mean of Y in randomized treatment minus the arithmetic mean of Y in randomized control.

The trajectory is the ordered one-step structure `(S0, selected_transformation, S1)`. H=1 only; no H>1 inference is authorized.

## 5. Assignment

256 units are assigned 128/128 using deterministic SHA256-based Fisher-Yates permutation with seed `130917`. Assignment is performed after all baseline inputs are frozen. Unit IDs are `u-0000` through `u-0255`.

## 6. Null control

A predeclared null run uses the same units, assignment and frozen generator but sets R1=false for both arms. It is a measurement/control check only and is not part of the primary treatment effect.

## 7. Integrity checks

The executor must verify:
1. `T_acc,0 != T_acc,1` and exact expected values;
2. baseline S0/C0/U equality across arms;
3. G and score definitions are identical across arms;
4. treatment flag is used only in accessibility evaluation;
5. null arm has no accessibility change;
6. assignment has exactly 128/128 units;
7. output schema is canonical JSON;
8. all bundle files match the hash manifest.

Any failed check yields `BLOCKED` and no scientific estimate is emitted.

## 8. Runtime contract

Execution requires CPython 3.11+ with the standard library only. No network access, external package, external dataset, or mutable service is required. The executor shall record the exact `sys.version`, operating-system identifier and SHA-256 of the executed source before scientific execution. That runtime fingerprint is an execution-input record, not an experimental degree of freedom.

## 9. Independence reconstruction

Executor-2 must reconstruct the fixture, assignment, accessibility sets, policy, transition, endpoint and checks from this bundle without reading Executor-1 output. It must use the same canonical definitions but an independently implemented reconstruction path.

## 10. Scope

This bundle supports only the bounded causal test `Z -> ΔT_acc -> Y` in this synthetic domain at H=1. It does not authorize claim upgrade, Core/RMA/Evidence→Claim Matrix modification, or inference to other domains/horizons.
