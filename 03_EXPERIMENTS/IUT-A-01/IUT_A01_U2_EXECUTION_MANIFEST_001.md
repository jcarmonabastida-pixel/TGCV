# IUT-A-01 — U2 Decision-Performance Execution Manifest 001

**Date:** 2026-09-11  
**Status:** `EXECUTION MANIFEST FROZEN — EXECUTOR NOT YET RUN`  
**Protocol:** `IUT_A01_U2_DECISION_PERFORMANCE_PROTOCOL_001.md`  
**Fixture:** `IUT_A01_U2_FIXTURE_SPECIFICATION_001.md`

## 1. Pilot objective

Run a reproducible computational pilot that compares a conventional decision procedure with a TGCV-assisted decision procedure on the same frozen decision-task universe.

This first U2 execution is methodological and fixture-bounded. It is not an industrial deployment study.

## 2. Trial universe

`N_TRIALS = 40`

The 40 trials are balanced across four trial classes:

- Direct-feasibility: 10
- Dependency: 10
- Constraint-conflict: 10
- Alternative-space: 10

Each trial exists exactly once in the frozen underlying universe. The control and TGCV procedures receive the same underlying trial facts.

## 3. Conditions

Each trial is evaluated under both procedures:

- `CONTROL_BASELINE`
- `TGCV_ASSISTED`

The paired design is used because it allows the same underlying decision problem to serve as its own comparison while preserving representation-level intervention.

The implementation must ensure that execution in one condition cannot leak the resulting decision into the other condition.

## 4. Primary metrics

### M1 — Decision correctness

`M1 = proportion of trials on which the selected option matches the frozen preferred admissible decision.`

### M2 — Decision time

`M2 = elapsed decision time per trial.`

For the computational pilot, elapsed time is measured from presentation of the condition-specific representation to the emitted decision. Tool/runtime overhead must be recorded separately so that it cannot silently contaminate the interpretation.

### M3 — Missed viable alternative rate

`M3 = proportion of trials with a frozen viable preferred alternative that the procedure fails to select when that alternative is the correct decision.`

## 5. Practical-success threshold

`U2_POSITIVE_THRESHOLD_M1 = +0 percentage points minimum; no degradation permitted beyond 5 percentage points.`

`U2_POSITIVE_THRESHOLD_M2 = >=10% relative reduction in median decision time.`

`U2_POSITIVE_THRESHOLD_M3 = >=20% relative reduction in missed viable alternatives.`

U2 is classified `POSITIVE` when M1 is not materially degraded and either M2 or M3 exceeds its threshold.

If M1 improves materially but neither M2 nor M3 crosses threshold, classification is `MIXED/PROMISING` and does not count as U2-POSITIVE under this manifest.

## 6. Null / mixed criteria

- `NULL`: no primary metric reaches the practical-significance threshold and no material accuracy advantage is observed.
- `MIXED`: one or more metrics improve while another primary metric materially degrades, or gains are internally inconsistent across trial classes.
- `INDETERMINATE`: fixture integrity, information symmetry, scoring, or execution integrity fails.
- `POSITIVE`: criteria in Section 5 are satisfied without material integrity violations.

## 7. Controls

The executor must verify before execution:

- identical underlying trial facts in both arms;
- frozen trial universe hash matches manifest;
- no outcome data is present in decision-time inputs;
- no analyst-generated option is added after freeze;
- control and TGCV representations differ only in the intended representation layer;
- scoring reference is immutable;
- trial order is randomized or deterministically counterbalanced;
- tool/runtime overhead is separately captured;
- all outputs are deterministically hashable.

## 8. Interpretation boundary

A `POSITIVE` result supports only:

`DECISION_PERFORMANCE_UTILITY_WITHIN_IUT_A01_FIXTURE = SUPPORTED`

It does not establish:

- explanatory superiority;
- discriminatory superiority;
- action/outcome utility;
- industrial utility;
- financial/value realization;
- generalization beyond the fixture;
- causal claims outside the controlled experiment;
- any TGCV Core modification.

## 9. Execution gate

Execution is authorized only after the executor verifies this manifest and fixture specification are unchanged and hashes them into the run record.

No AWS execution is involved. The blocked AWS B1 route is therefore not required for this U2 pilot.

## 10. Next operation

Generate the deterministic U2 computational executor and local dry-run against this manifest before collecting the final comparison result.
