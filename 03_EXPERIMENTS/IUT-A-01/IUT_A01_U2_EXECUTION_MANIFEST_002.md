# IUT-A-01 — U2 Decision-Performance Execution Manifest 002

**Date:** 2026-09-11  
**Status:** `PROPOSED — PRE-EXECUTION ALIGNMENT GATE`  
**Protocol:** `IUT_A01_U2_DECISION_PERFORMANCE_PROTOCOL_001.md`  
**Metric design:** `IUT_A01_U2_METRIC_DESIGN_REVISION_001.md`  
**Fixture:** `IUT_A01_U2_FIXTURE_SPECIFICATION_002.md`  
**Executor target:** `execute_iut_a01_u2_pilot_v03.py`

## 1. Pilot objective

Run a reproducible computational pilot comparing the conventional decision procedure with the TGCV-assisted decision procedure on the same frozen Fixture 002 decision-task universe.

This execution is methodological and fixture-bounded. It is not an industrial deployment study.

Manifest 002 applies the registered metric-design revision: M1 is the primary metric, M2 is the secondary metric, and M3 is retired.

## 2. Protocol precedence and version relationship

Protocol 001 remains the historical U2 design baseline and is not edited. For this concrete Fixture 002 execution, `IUT_A01_U2_METRIC_DESIGN_REVISION_001` explicitly determines the active metric set and supersedes the earlier M3 metric selection.

No historical execution is modified or reclassified by this manifest.

## 3. Trial universe

`N_TRIALS = 40`

The 40 trials are balanced across four classes:

- `DIRECT_FEASIBILITY`: 10
- `DEPENDENCY`: 10
- `CONSTRAINT_CONFLICT`: 10
- `ALTERNATIVE_SPACE`: 10

Each trial exists exactly once in the frozen underlying universe. Both conditions receive the same underlying trial facts.

The executor must derive `viable_options` and `preferred_option` from the frozen option/state semantics and must block execution on any mismatch with the fixture invariants.

## 4. Conditions

Each trial is evaluated under:

- `CONTROL_BASELINE`
- `TGCV_ASSISTED`

The paired design preserves the same underlying task while changing only the intended representation/procedure layer.

Execution of one condition must not leak its resulting decision into the other condition.

## 5. Active metrics

### M1 — Decision correctness — PRIMARY

`M1 = proportion of trials in which selected_option == frozen preferred_option`.

M1 is the primary U2 performance metric.

### M2 — Decision time — SECONDARY

Elapsed decision time from presentation of the condition-specific representation to emitted decision, using the predeclared timing basis. Tool/runtime overhead is captured separately.

M2 is the secondary U2 performance metric.

### M3 — RETIRED

M3 is not an active metric for Fixture 002. It must not be collected, calculated, thresholded, reported, or used for classification.

No replacement alternative-space metric may be introduced post hoc.

## 6. Practical-significance thresholds

`M1_DEGRADATION_LIMIT = 5 percentage points`.

M1 passes the material-degradation gate when TGCV M1 is not more than 5 percentage points below control M1.

`M2_RELATIVE_REDUCTION_THRESHOLD = 10%` reduction in median elapsed decision time.

U2-POSITIVE requires M1 to pass its degradation gate and M2 to meet or exceed the 10% relative-reduction threshold.

If M1 passes but M2 does not, the result is not U2-POSITIVE under this manifest.

No M3 threshold exists in Manifest 002.

## 7. Integrity controls

The executor must verify before scoring:

- fixture 002 exists and its frozen Git blob identity matches the manifest;
- manifest identity is verified by the executor;
- metric-design revision identity is recorded;
- 40 trials exist with 10/10/10/10 class balance;
- trial identifiers are unique;
- `viable_options` equals the independently computed feasible set for every trial;
- `preferred_option` equals the independently computed objective argmax for every trial;
- preferred option is viable for every trial;
- same frozen option universe is used by both arms;
- no analyst-generated options are added;
- outcome information is unavailable during decision;
- no external data are used;
- ground truth is immutable;
- M3 logic is absent from active scoring;
- all output records are deterministically hashable.

## 8. Expected fixture reference properties

The following are pre-execution fixture expectations, not results:

- preferred option counts: A=25, B=15, C=0;
- expected control M1: 25/40 = 62.5%;
- expected TGCV M1: 40/40 = 100%.

These values must be checked as construction/reference invariants, not treated as observed outcomes.

## 9. Timing integrity

M2 uses `perf_counter_ns` around the single decision invocation for each condition. Tool/runtime overhead is recorded separately. A deterministic timing proxy may be retained only as diagnostic metadata and is not M2.

The executor must report task-level elapsed-time observations and medians, rather than replacing measured time with a proxy.

## 10. Classification

- `U2-POSITIVE`: M1 passes the degradation gate and M2 meets the 10% relative-reduction threshold, with no material integrity violation.
- `U2-NULL`: M1 passes but M2 fails to meet the threshold, with no integrity violation and no other predeclared active secondary criterion.
- `U2-MIXED`: a material M1 degradation occurs alongside a favorable M2 direction, or another material trade-off is identified within the active metrics.
- `U2-INDETERMINATE`: fixture, reference, information symmetry, metric integrity, or execution integrity fails.

No result may be promoted to positive status by a retired or post-hoc metric.

## 11. Interpretation boundary

A positive result supports only:

`DECISION_PERFORMANCE_UTILITY_WITHIN_IUT_A01_FIXTURE = SUPPORTED`

It does not establish explanatory superiority, discriminatory superiority, industrial utility, financial/value realization, general validity, causal generalisation, or any TGCV Core modification.

## 12. Execution gate

Manifest 002 does not authorize execution by itself. Execution requires:

1. Fixture 002 freeze after Manifest/Executor alignment audit;
2. exact manifest/fixture/executor version and hash verification;
3. successful local dry-run;
4. no unresolved integrity defect.

No AWS execution is required.

## 13. Versioning

Manifest 001 remains immutable historical evidence. Manifest 002 is a new execution artifact tied to Fixture 002 and Metric Design Revision 001.

**EXECUTION_AUTHORIZATION = NOT_GRANTED**
