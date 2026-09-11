# IUT-A-01 — U2 Manifest/Executor Alignment Audit 001

**Status:** `PASS — PRE-FREEZE ALIGNMENT AUDIT`  
**Manifest:** `IUT_A01_U2_EXECUTION_MANIFEST_002.md`  
**Fixture:** `IUT_A01_U2_FIXTURE_SPECIFICATION_002.md`  
**Metric design:** `IUT_A01_U2_METRIC_DESIGN_REVISION_001.md`  
**Executor:** `execute_iut_a01_u2_pilot_v03.py`

## 1. Scope

This audit checks whether Manifest 002 and Executor 002 are structurally and semantically aligned with Fixture 002 and the registered metric-design decision before any execution authorization.

## 2. Alignment checks

| Check | Result | Finding |
|---|---|---|
| Fixture version | PASS | Manifest targets Fixture 002; Executor resolves Fixture 002. |
| Metric design version | PASS | Manifest explicitly binds Metric Design Revision 001; active metrics are M1/M2 only. |
| M1 primary | PASS | Both manifest and executor define decision correctness as selected option equals frozen preferred option. |
| M2 secondary | PASS | Both define elapsed decision time using `perf_counter_ns`; proxy is not used as M2. |
| M3 retired | PASS | Manifest has no M3 threshold; Executor contains no M3 scoring path and asserts `m3_active=False`. |
| Ground-truth derivation | PASS | Executor derives viable options and preferred option from feasibility/objective semantics. |
| Construction mismatch blocking | PASS | Executor blocks when viable/preferred reference checks fail. |
| Preferred admissibility | PASS | Executor verifies preferred option is viable. |
| Class balance | PASS | Executor requires 40 trials and 10 per class. |
| Same universe | PASS | Paired control/TGCV procedures operate on the same generated trial universe. |
| Outcome blindness | PASS | Outcome-blind integrity flag is required before scoring. |
| No external data | PASS | Executor declares and enforces fixture-bounded execution with no external data. |
| Historical immutability | PASS | Manifest 001 and Executor 0.2.1 remain untouched. |
| Execution authorization | PASS | Neither manifest nor executor grants authorization; dry-run/final gate remains required. |

## 3. Important non-blocking observation

Manifest 002 deliberately does not reproduce the retired M3 thresholds from Manifest 001. This is required by Metric Design Revision 001 and is not a loss of historical provenance. Manifest 001 remains immutable historical evidence.

## 4. Audit result

Manifest 002 and Executor 002 are aligned with Fixture 002 and the registered metric decision.

**ALIGNMENT_AUDIT_RESULT=PASS**  
**FIXTURE_FREEZE=READY**  
**EXECUTION_AUTHORIZATION=NOT_GRANTED**

The next operation is a local dry-run of Executor 002 against the exact GitHub-derived Fixture/Manifest state. The dry-run must be audited before any FULL_PILOT execution.
