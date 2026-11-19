# C10-S F1 — Deterministic numerical stress result 001

**Result state:** EXECUTED — MIXED RESULT; ROBUSTNESS NOT ESTABLISHED  
**Workflow run:** [44541521548](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44541521548)  
**Run conclusion:** SUCCESS — one primary execution, attempt 1  
**Authorization:** `C10S-F1-NUMERICAL-STRESS-20261119-003` — CONSUMED AND CLOSED  
**Authorization commit:** `7bd8713178faf68e9e2a47d11f861f4c00e1bac9`  
**Frozen source commit:** `d5edc0010f7a8c6587677eb2004b545367fc4b35`  
**Workflow blob:** `1570c248df7709c3c9f2efff049d91f81a88e582`  
**Artifact:** `c10s-f1-numerical-stress-44541521548` (ID `14538327928`)  
**Artifact SHA-256:** `6ebbda5f4cbb64d4f89439497c467ed64bbf04d0bcf56f541a9f00863355629f`

## 1. Execution integrity

GitHub Actions completed all steps successfully:
- authorization/workflow snapshot checkout;
- Python 3.12.3 setup;
- one-shot authorization and workflow identity preflight;
- frozen source checkout and verification of all six Git blobs;
- pinned NumPy 2.1.3 / SciPy 1.14.1 installation;
- provenance preparation;
- authorization consumption before the primary numerical command;
- one invocation of the deterministic stress CLI;
- evidence artifact upload.

Runtime: CPython 3.12.3, NumPy 2.1.3, SciPy 1.14.1, ubuntu-24.04. Runner exit code: 0. stderr was empty. The authorization was consumed by run 44541521548 and subsequently closed; no retry or replay is authorized.

The downloaded artifact ZIP SHA-256 matches the GitHub artifact digest. Internal file hashes independently match the manifest:
- records JSONL: `7cef9e60c80f12c2f948c0b0fb29ad87f775c8d9abab9fe1f5eac02194c930ef`;
- summary JSON: `be2e5391fc66dbe07a8cedd0f9ac29d9fd74433fb5581433856da2862d8b7801`;
- manifest JSON: `f7f55df7752453f13bf449f64fc254bb881783d36df6a836b63508dab7a64792`.

The artifact contains 122 records: 115 polynomial/Sturm records and 7 F1 end-to-end scale records.

## 2. Summary

| Lane | Planned | Returned/generated | Result |
|---|---:|---:|---|
| Polynomial/Sturm N1–N3, N5–N6 | 115 | 115 | Mixed resolved / unresolved / representation-unresolved |
| F1 end-to-end N4 | 7 | 7 | 5 equivariance PASS; 2 FAIL |
| Combined | 122 | 122 | Execution complete; robustness not established |

Polynomial/Sturm statuses:
- `ROOTS_ISOLATED`: 54;
- `ROOTS_UNRESOLVED`: 57;
- `REPRESENTATION_UNRESOLVED`: 2;
- `NO_ROOTS_CONSTANT_POLYNOMIAL`: 1;
- `IDENTICALLY_ZERO_POLYNOMIAL_UNRESOLVED`: 1.

The 113/115 binary64-representable count means the coefficient vectors converted to finite non-erased binary64 values. It does **not** mean their ideal root topology was preserved.

## 3. N1 — progressive root coalescence

- Exponents 4, 8, 16, 24 and 32: all 10 simple-pair / pair-plus-negative fixtures were isolated with their ideal distinct-root counts.
- Exponents 40 and 48: all 4 fixtures returned `ROOTS_UNRESOLVED`; this is an explicit abstention at the configured absolute isolation width.
- Exponent 52: the simple-pair fixture returned `ROOTS_ISOLATED` with zero roots, versus two ideal roots; the pair-plus-negative fixture returned one distinct root versus three ideal roots.
- Exponent 54: the simple-pair fixture returned one distinct root versus two ideal roots; the pair-plus-negative fixture returned three distinct roots versus three ideal roots.
- Double-plus-simple and triple-root fixtures returned two and one distinct roots respectively, consistent with distinct-root counting and multiplicity representation.

**Interpretation:** near binary64 coefficient degeneracy, the represented polynomial can have a different real-root topology from the exact ideal polynomial. `ROOTS_ISOLATED` certifies isolation for the exact rationalization of the supplied binary64 coefficients; it does not certify preservation of the ideal polynomial's roots. The harness records both ideal and represented coefficients, but its current summary does not calculate a formal topology-preservation rate. The N1 E52/E54 cases are therefore explicit representation-induced topology discrepancies found by post-run comparison, not successful recovery of the ideal roots.

## 4. N2 — one- and two-ULP coefficient perturbations

All 16 predeclared perturbation records (four coefficients × four signed ULP shifts) were binary64-representable and returned `ROOTS_ISOLATED`, with three distinct isolated roots per record.

This establishes successful isolation for these 16 represented perturbed polynomials. It does not establish a general ULP robustness envelope: the fixture family is one base cubic, and the result summary does not include a predeclared quantitative root-location error or topology-discrepancy metric across a broader conditioning range.

## 5. N3 — amplitude and variable scaling

Amplitude scaling: all 7 factors (2^-500 through 2^500) returned `ROOTS_ISOLATED`.

Variable scaling:
- 2^0 and 2^50: `ROOTS_ISOLATED`;
- 2^-50, 2^-200 and 2^200: `ROOTS_UNRESOLVED`;
- 2^-500 and 2^500: `REPRESENTATION_UNRESOLVED` because conversion erased or made a nonzero coefficient non-finite.

**Interpretation and limitation:** the variable-scale lane retains a fixed absolute `max_width=10^-12` and the domain builder has a unit lower bound on its margin. These settings do not transform with the variable scale. Consequently the unresolved outcomes mix isolator behavior with a non-equivariant test configuration. They demonstrate that the current fixed-tolerance interface is not scale-invariant, but do not isolate the arithmetic kernel as the sole cause. A follow-up protocol must explicitly distinguish fixed-absolute-tolerance behavior from scale-covariant tolerance/domain behavior.

## 6. N5 — isolation width/depth ladder

Across 4 fixtures × 3 widths × 5 depths = 60 records:
- `ROOTS_ISOLATED`: 10;
- `ROOTS_UNRESOLVED`: 50.

Resolution was concentrated at depth 64 or 256 and the tighter widths. The large-magnitude pair (roots 2^120 and 2^120+1) produced one isolated distinct root in its three resolved records, despite two ideal roots. This is consistent with loss of root separation in the binary64 coefficient representation; it must not be reported as recovery of both ideal roots. The other close-pair fixtures resolved both roots only in their tighter/deeper configurations.

The ladder shows a strong dependence of resolution/abstention on width and depth, but the 50 abstentions are not false positives: they are explicit unresolved outcomes. The next analysis must preserve these denominators and separate computational-budget abstention from coefficient-representation topology change.

## 7. N6 — degeneracies and endpoints

- Zero and positive endpoint fixture: isolated.
- Negative and upper-edge fixture: isolated.
- Linear fixture: isolated.
- Nonzero constant: correctly classified as no-root constant polynomial.
- Identically-zero polynomial: explicitly unresolved.

No result from this block implies F1 generic-polynomial agreement; the current F1 API does not accept arbitrary polynomial coefficient vectors.

## 8. N4 — F1 end-to-end observation-scale equivariance

All 7 scales returned a profile result and `POLYNOMIAL_ROOTS_ISOLATED`. The base-scale record (2^0) was resolved and adjudicated `ROOTS_AGREE`; no unresolved-baseline condition applied.

| Observation scale | Sturm | Adjudication | Equivariance |
|---|---|---|---|
| 2^-100 | ROOTS_ISOLATED | ROOTS_AGREE | PASS |
| 2^-50 | ROOTS_ISOLATED | ROOTS_AGREE | PASS |
| 2^-20 | ROOTS_ISOLATED | ROOTS_AGREE | PASS |
| 2^0 | ROOTS_ISOLATED | ROOTS_AGREE | PASS (baseline) |
| 2^20 | ROOTS_ISOLATED | ROOTS_AGREE | PASS |
| 2^50 | ROOTS_UNRESOLVED | ROOTS_UNRESOLVED | FAIL |
| 2^100 | ROOTS_UNRESOLVED | ROOTS_UNRESOLVED | FAIL |

Thus:
- profile result returned: 7/7;
- F1 score polynomial status isolated: 7/7;
- independent Sturm reference isolated: 5/7;
- adjudication agreement: 5/7;
- scale-equivariance checks: 5 PASS / 2 FAIL.

At 2^50 and 2^100, the profile and polynomial solver still returned, and the restored MLE/LR endpoints remained numerically close to baseline, but the independent Sturm isolator became unresolved. The adjudicator correctly failed closed rather than claiming agreement. This is the clearest end-to-end adversarial finding of this run: the complete F1 → Sturm → adjudication chain is not equivariant across the full predeclared scale range.

## 9. Scientific interpretation and claim boundary

**Execution gate:** PASS — one authorized primary run completed and evidence integrity checks passed.

**Numerical robustness gate:** NOT PASS / MIXED:
- clear ULP fixture success within the narrow N2 family;
- explicit unresolved transitions in N1 and N5;
- coefficient-representation topology changes in N1 at E52/E54 and the N5 large-magnitude fixture;
- N3 variable-scale results confounded by fixed absolute tolerance/domain settings;
- F1 end-to-end equivariance fails at 2^50 and 2^100 because the independent Sturm reference becomes unresolved.

This run does not establish universal robustness, arbitrary-polynomial F1/Sturm concordance, Monte Carlo calibration, inferential coverage, or any causal/value claim for C10. It does provide bounded adversarial evidence and identifies specific limitations/falsifiers. Do not collapse `ROOTS_ISOLATED`, `ROOTS_UNRESOLVED` and `REPRESENTATION_UNRESOLVED` into one success metric.

## 10. Next scientific operation

Do not rerun this authorization. It is consumed and closed.

The next design iteration should:
1. Add an explicit ideal-vs-binary64 topology comparison (root count, multiplicity and location), with a separate status for representation-induced topology change.
2. Split N3 into fixed-absolute-tolerance and scale-covariant tolerance/domain lanes; predeclare how intervals and domains transform.
3. Retain all unresolved denominators and quantify the width/depth transition surface rather than treating abstentions as failures or dropping them.
4. For N4, localize the scale at which Sturm changes from resolved to unresolved and diagnose the isolator's scale dependence without tuning against the observed outcomes.
5. Freeze a new protocol/source snapshot and request a fresh one-shot authorization before any further numerical execution.

No code in the frozen source was modified by this execution. No unit tests, Monte Carlo calibration, DGP experiment, inferential coverage study or scientific C10-S execution was performed.
