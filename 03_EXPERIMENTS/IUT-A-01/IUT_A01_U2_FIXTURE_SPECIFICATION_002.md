# IUT-A-01 — U2 Fixture Specification 002

**Status:** `PROPOSED FROZEN FIXTURE DESIGN — PRE-EXECUTION CONSISTENCY GATE REQUIRED`  
**Revision:** `002`  
**Supersedes for future execution:** `001` only; fixture 001 remains immutable historical evidence  
**Purpose:** repair semantic consistency identified by `IUT_A01_U2_FIXTURE_CONSISTENCY_AUDIT_001.md`

## 1. Design objective

Fixture 002 preserves the original U2 research question while ensuring that the frozen decision objective, feasibility relation, admissible decision set, preferred decision and scoring rule describe the same decision problem.

The experiment tests whether the TGCV representation of accessibility/dependency relations can improve decision performance when the same underlying task facts are available to both arms.

## 2. Core semantic rule

For every trial:

1. `feasible(option, state)` defines the admissible transformation/decision space.
2. `viable_options` is exactly the set of options satisfying the frozen feasibility relation.
3. `preferred_option` is the highest `objective_score` option in `viable_options`, with a deterministic tie-break rule.
4. M1 compares the selected option against `preferred_option`.
5. M3 counts a miss only when the selected option is outside `viable_options` while at least two viable options exist.

Therefore the scoring reference cannot disagree with the frozen objective function by construction.

## 3. Option universe

Each trial contains the same three option identities:

| Option | Objective score | Requirements | Dependencies | Hard constraints | Role |
|---|---:|---|---|---|---|
| A | `80 + cycle` | `R0` | none | none | directly accessible baseline |
| B | `85 + cycle` | `R0,R1` | `D1` | none | higher-value dependent alternative |
| C | `70 + cycle` | `R0` | none | `BLOCK_C` | lower-value distractor / constraint-sensitive option |

The critical repair is that C is no longer assigned an objective score above the preferred A/B options while simultaneously being excluded from the viable set.

## 4. State generation

Every trial has:

- `R0 = true`
- `R1 = true` for `DEPENDENCY` and `ALTERNATIVE_SPACE`; otherwise `false`
- `D1 = true` for `ALTERNATIVE_SPACE`; for `DEPENDENCY`, true on even cycles and false on odd cycles; otherwise `false`
- `BLOCK_C = true` for `CONSTRAINT_CONFLICT`; otherwise `false`

No external data are used.

## 5. Ground-truth derivation

The fixture generator must derive, rather than independently hand-code, the reference values:

```text
computed_viable = [option for option in options if feasible(option, state)]
preferred_option = argmax(objective_score, deterministic_tie_break)
```

The generated `viable_options` MUST equal `computed_viable` exactly.

The generated `preferred_option` MUST equal the computed argmax exactly.

Any mismatch is a fixture-construction failure and must block execution.

## 6. Expected class semantics

### DIRECT_FEASIBILITY

B is unavailable because `D1=false`; C remains feasible but has lower objective score. Therefore A is preferred and A is the sole preferred decision.

### DEPENDENCY

When `D1=true`, B is accessible and has the highest objective score, so B is preferred and both A/B are viable. When `D1=false`, B is inaccessible and A is preferred; C remains a lower-scoring viable distractor.

### CONSTRAINT_CONFLICT

C has a hard constraint conflict (`BLOCK_C=true`). B remains dependency-inaccessible in this class, so A is preferred and is the sole preferred decision.

### ALTERNATIVE_SPACE

D1 is true, making B accessible. B is the highest-scoring viable option and is preferred; A remains viable as an alternative.

## 7. Expected aggregate reference properties

For 40 balanced trials:

- DIRECT_FEASIBILITY: 10 trials, preferred A.
- DEPENDENCY: 10 trials, preferred B on 5 even-cycle trials and A on 5 odd-cycle trials.
- CONSTRAINT_CONFLICT: 10 trials, preferred A.
- ALTERNATIVE_SPACE: 10 trials, preferred B.

Expected preferred counts:

- A = 25
- B = 15
- C = 0

Expected multi-viable denominator for M3: 15 trials (the 5 dependency trials with D1=true plus the 10 alternative-space trials).

Because each selected option can contribute at most one miss per trial, M3 is mathematically bounded to `[0,1]`.

## 8. Control arm

The control procedure retains the frozen conventional limitation used by U2: dependency-bearing options are not admitted as directly executable decisions.

Expected control decision pattern under the fixture:

- A for all DIRECT_FEASIBILITY trials.
- A for all DEPENDENCY trials, including the five trials where B is viable and preferred.
- A for all CONSTRAINT_CONFLICT trials.
- A for all ALTERNATIVE_SPACE trials, missing B as the preferred reachable alternative.

Expected control M1 accuracy: `25/40 = 62.5%`.

## 9. TGCV arm

The TGCV procedure evaluates the explicit feasibility/accessibility relation and selects the highest objective option within the resulting accessible decision space.

Expected TGCV decision pattern:

- A for DIRECT_FEASIBILITY.
- B when D1=true in DEPENDENCY; A otherwise.
- A in CONSTRAINT_CONFLICT because C is blocked and B is dependency-inaccessible.
- B in ALTERNATIVE_SPACE.

Expected TGCV M1 accuracy: `40/40 = 100%`.

These are fixture-derived expectations only; they are not experimental results.

## 10. M3 definition

For each trial where `len(viable_options) > 1`, a miss is:

```text
selected_option not in viable_options
```

M3 denominator is the number of multi-viable trials.

No numerator can exceed the denominator. The executor must assert this invariant and block execution if violated.

## 11. Mandatory pre-execution consistency invariants

Fixture 002 is not executable until all checks below pass:

- `objective_preference_consistent = true` for every trial.
- `viable_options_exact = true` for every trial.
- `preferred_option in viable_options = true` for every trial.
- `m3_denominator > 0`.
- `m3_numerator_control <= m3_denominator`.
- `m3_numerator_tgcv <= m3_denominator`.
- all M3 rates in `[0,1]`.
- class balance = 10/10/10/10.
- no analyst-generated options.
- same frozen universe for both arms.
- outcome blind.
- immutable ground truth.

## 12. Versioning rule

Fixture 001 is not edited. Fixture 002 is a new artifact with independent Git and SHA-256 identities. Any executor using fixture 002 must verify those identities before running.

A full pilot against fixture 002 is prohibited until the dedicated consistency audit passes.
