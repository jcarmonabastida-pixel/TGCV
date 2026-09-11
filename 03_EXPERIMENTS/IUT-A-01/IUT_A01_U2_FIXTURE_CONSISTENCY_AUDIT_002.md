# IUT-A-01 — U2 Fixture Consistency Audit 002

**Status:** `PASS — PRE-FREEZE CONSISTENCY AUDIT`  
**Fixture:** `IUT_A01_U2_FIXTURE_SPECIFICATION_002.md`  
**Metric design:** `IUT_A01_U2_METRIC_DESIGN_REVISION_001.md`  
**Audit scope:** semantic consistency of Fixture 002 before Manifest/Executor 002 generation  

## 1. Decision gate

Fixture 002 was revised after the registered metric-design decision:

- M1 = primary U2 performance metric.
- M2 = secondary U2 performance metric.
- M3 = retired and excluded from Fixture 002 execution, scoring, thresholds, and interpretation.

Historical Fixture 001 and prior execution artifacts remain untouched.

**Gate result: PASS.**

## 2. Consistency checks

| Check | Result | Finding |
|---|---|---|
| Metric design dependency explicit | PASS | Fixture 002 names `IUT_A01_U2_METRIC_DESIGN_REVISION_001`. |
| M1 definition | PASS | Matches the registered definition: selected option equals frozen preferred option. |
| M2 definition | PASS | Decision-time basis and separate timing-overhead reporting are retained. |
| M3 primary/secondary status | PASS | M3 is explicitly retired and absent from active U2 scoring. |
| M3 execution collection | PASS | Fixture prohibits M3 collection, numerator/denominator calculation, thresholds, and reporting. |
| M3 post-hoc replacement | PASS | Future alternative-space metric is explicitly outside Fixture 002 and requires independent design. |
| Feasibility semantics | PASS | `viable_options` is derived from `feasible(option,state)`. |
| Preferred-option semantics | PASS | Preferred option is derived from objective score over the frozen viable set. |
| Ground-truth derivation | PASS | Reference values are required to be derived, not independently hand-coded. |
| Preferred option admissibility | PASS | Fixture requires `preferred_option in viable_options`. |
| Objective/feasibility coherence | PASS | C has lower objective score than A/B, removing the previous contradiction. |
| Class balance | PASS | 40 trials specified as 10/10/10/10. |
| Same universe across arms | PASS | Same frozen option universe and task facts are specified. |
| Outcome blindness | PASS | Outcome blind remains a mandatory invariant. |
| Immutable ground truth | PASS | Ground truth remains frozen and mismatch blocks execution. |
| Historical immutability | PASS | Fixture 001 and historical execution artifacts are not modified. |

## 3. Reference-value audit

The fixture declares expected values only as pre-execution reference properties:

- Preferred counts: A=25, B=15, C=0.
- Control M1 expectation: 25/40 = 62.5%.
- TGCV M1 expectation: 40/40 = 100%.

These are explicitly labelled fixture-derived expectations and are not execution results.

## 4. Critical methodological finding

The prior M3 construct is no longer part of the active pilot. Therefore no M3 denominator, numerator, rate, threshold, or outcome may appear in Manifest 002 or Executor 002 as an experimental performance measure.

This is a methodological retirement, not a historical deletion. Historical artifacts remain available for provenance and audit.

## 5. Freeze decision

Fixture 002 is **consistent with the registered metric-design revision** and passes the dedicated pre-execution consistency gate.

This audit does **not** by itself freeze Fixture 002 for execution. The next gate is to generate and audit Manifest 002 and Executor 002 so that their metric declarations and execution logic are exactly aligned with this fixture and the metric revision.

**AUDIT_RESULT=PASS**
**FIXTURE_FREEZE_STATUS=READY_PENDING_MANIFEST_EXECUTOR_ALIGNMENT**
**EXECUTION_AUTHORIZATION=NOT_GRANTED**
