# TGCV — TR-131 Scientific Operational Bundle Specification v0.1

**Status:** CONSTRUCTION — NOT FROZEN
**Scientific execution:** NOT AUTHORIZED
**Purpose:** define the complete scientific instance required before freeze and G8 authorization.

## 1. Scientific contrast

The proposed controlled contrast uses the same frozen system state, context, accessible transformation space, admissibility rules and transition function in Cases A and B.

Only the realization/selection condition X differs:

- Case A: `policy_A` selects `tau_accept`.
- Case B: `policy_B` selects `tau_reject`.

The scientific fixture must implement these as independently declared realization policies rather than hard-coding a trajectory outcome.

## 2. Frozen non-target representation

The scientific instance shall freeze:

- `S0` canonical representation;
- `C` canonical representation;
- `T_acc` canonical ordered representation and hash;
- transformation definitions;
- admissibility rules;
- transition function;
- observation window;
- trajectory representation;
- execution environment;
- source commit and configuration hashes.

Cases A and B must be generated from the same canonical baseline.

## 3. X isolation

X is the realization/selection policy and is declared before the first realization.

Required declarations:

- `X_definition = realization_policy`;
- `X_A = policy_A`;
- `X_B = policy_B`;
- admissible X values are frozen;
- X is not derived from H, O, V or T_real;
- X does not modify S0, C, T_acc, admissibility or transition rules.

## 4. Realization rule

For each case, the realization operator receives `(S,C,T_acc,X)` and selects one admissible transformation from T_acc according to the frozen policy.

The operator must expose the selected transformation in the transition trace before the resulting state is generated.

No post hoc selection is permitted.

## 5. Primary trajectory outcome

The primary outcome is exact equality or inequality of the canonical realized-transformation sequence H.

`H_A = H_B` is a null trajectory contrast.

`H_A != H_B` is the pre-specified positive trajectory contrast.

No secondary value or outcome variable is required for TR-131.

## 6. Scientific trace

Each transition record must contain:

`case_id, step, S_t, C_t, T_acc_t, X_t, T_real_t, S_t1`

The trace must permit independent reconstruction of T_real and H.

## 7. Controls and invariants

The scientific runner must fail closed if any of the following differ between A and B without being explicitly designated as X:

- S0;
- C;
- T_acc;
- transformation definitions;
- admissibility rules;
- transition function;
- observation window;
- measurement procedure;
- environment or analysis code.

## 8. Executor-2 package

Executor-2 must receive only the frozen scientific package, including:

1. protocol;
2. scientific bundle;
3. configuration;
4. environment specification;
5. execution command;
6. integrity manifest;
7. audit worksheet;
8. reconstruction instructions.

Executor-2 must not receive Executor-1 results, trajectory outputs, interpretation, or post-execution tuning.

## 9. Required artifacts before freeze

The repository must contain:

- executable scientific fixture;
- scientific configuration;
- X declaration schema/record;
- canonical S0/C/T_acc artifacts or deterministic constructors;
- trace schema;
- trajectory derivation procedure;
- environment specification;
- Executor-2 reconstruction package;
- integrity manifest;
- audit worksheet;
- freeze audit;
- G8 authorization record.

## 10. Current disposition

This specification does not authorize execution.

The current PREFLIGHT_PASS remains fixture-integrity evidence only.

Before G8, the executable scientific mode must be implemented, independently audited, and reconstructed by Executor-2 from the frozen package.

**Disposition:** `SCIENTIFIC BUNDLE SPECIFIED — IMPLEMENTATION AND INDEPENDENT RECONSTRUCTION PENDING`.