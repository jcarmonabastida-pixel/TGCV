# IUT-A-01 — U2 Fixture Specification 002

**Status:** `PROPOSED FROZEN FIXTURE DESIGN — PRE-EXECUTION CONSISTENCY GATE REQUIRED`  
**Revision:** `002`  
**Metric design:** `IUT_A01_U2_METRIC_DESIGN_REVISION_001`  
**Supersedes for future execution:** `001` only; fixture 001 remains immutable historical evidence  
**Purpose:** repair semantic consistency identified by `IUT_A01_U2_FIXTURE_CONSISTENCY_AUDIT_001.md` and align the fixture with the approved U2 metric design revision.

## 1. Design objective

Fixture 002 preserves the original U2 research question while ensuring that the frozen decision objective, feasibility relation, admissible decision set, preferred decision and scoring rule describe the same decision problem.

The experiment tests whether the TGCV representation of accessibility/dependency relations can improve decision performance when the same underlying task facts are available to both arms.

The active U2 metric set for this fixture is:

- **M1 — Decision correctness:** primary metric.
- **M2 — Decision time:** secondary metric.
- **M3:** retired and not collected, scored, or interpreted in Fixture 002.

## 2. Core semantic rule

For every trial:

1. `feasible(option, state)` defines the admissible transformation/decision space.
2. `viable_options` is exactly the set of options satisfying the frozen feasibility relation.
3. `preferred_option` is the highest `objective_score` option in `viable_options`, with a deterministic tie-break rule.
4. M1 compares the selected option against `preferred_option`.
5. M2 measures decision time using the predeclared timing basis; timing overhead is reported separately.
6. M3 is not a Fixture 002 metric and must not be used as a primary, secondary, exploratory, or post-hoc performance result.

Therefore the M1 scoring reference cannot disagree with the frozen objective function by construction.

## 3. Option universe

Each trial contains the same three option identities:

| Option | Objective score | Requirements | Dependencies | Hard constraints | Role |
|---|---:|---|---|---|---|
| A | `80 + cycle` | `R0` | none | none | directly accessible baseline |
| B | `85 + cycle` | `R0,R1` | `D1` | none | higher-value dependent alternative |
| C | `70 + cycle` | `R0` | none | `BLOCK_C` | lower-value distractor / constraint-sensitive option |

The repaired objective ordering is explicit: C has a lower objective score than A and B at every cycle. Its exclusion under `BLOCK_C` therefore cannot create a contradiction between objective value and feasibility.

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

These are fixture-derived expectations only; they are not experimental results.

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

## 10. Active metric definitions

### M1 — Decision correctness

```text
M1 = proportion of trials in which selected_option == frozen preferred_option
```

The preferred option is derived from the frozen objective over the frozen feasible set. M1 is the primary U2 performance metric.

### M2 — Decision time

Elapsed decision time from presentation of the frozen trial input to emitted decision, using the predeclared timing basis. Timing overhead is reported separately. M2 is the secondary U2 performance metric.

### M3 — Retired

M3 is withdrawn from the current U2 pilot family by `IUT_A01_U2_METRIC_DESIGN_REVISION_001`.

Fixture 002 MUST NOT:

- collect an M3 score;
- calculate an M3 numerator or denominator;
- use an M3 threshold;
- report M3 as an outcome;
- introduce a replacement alternative-space metric post hoc.

A future reachable-alternative metric requires an independently versioned design and predeclared scoring rule and is outside Fixture 002.

## 11. Mandatory pre-execution consistency invariants

Fixture 002 is not executable until all checks below pass:

- `objective_preference_consistent = true` for every trial.
- `viable_options_exact = true` for every trial.
- `preferred_option in viable_options = true` for every trial.
- M1 definition matches the active metric design revision exactly.
- M2 definition matches the active metric design revision exactly.
- M3 is absent from active scoring and interpretation logic.
- class balance = 10/10/10/10.
- no analyst-generated options.
- same frozen universe for both arms.
- outcome blind.
- immutable ground truth.
- expected reference values are declared as fixture expectations only, not results.

## 12. Versioning rule

Fixture 001 is not edited. Fixture 002 is a new artifact with independent Git and SHA-256 identities. Any executor using fixture 002 must verify those identities before running.

The metric design dependency is explicitly versioned as `IUT_A01_U2_METRIC_DESIGN_REVISION_001`.

A full pilot against fixture 002 is prohibited until the dedicated consistency audit passes.
