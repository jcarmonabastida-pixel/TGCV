# C10-S F5 G7 — replay discrepancy audit

**Date:** 2026-11-22  
**Status:** REPLAY INTEGRITY FAILED — COVERAGE ADJUDICATION NOT PERFORMED  
**Run:** [44969714756](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44969714756)  
**Approved code commit:** `50ffc628a40b7649c716aaf66a4c83c53983102e`  
**Authorization:** `G7-20261122-0100` (one-use; consumed by the run)  
**Scope:** F5 G7 Tier-A calibration only. This audit does not alter the frozen protocol or any scientific claim.

## 1. Executive finding

The staged primary and clean-source replay completed all 40 shards per phase (2,000 records per phase across the two frozen cells). The final aggregator failed on a shard record-digest mismatch. The mismatch is reproducible in **8 of 40 primary/replay shard pairs**:

| Cell | Shard starts with mismatch |
|---|---|
| `F5_beta22_M10_R5` | 300, 600, 800, 950 |
| `F5_beta22_M30_R20` | 100, 300, 700, 750 |

The other 32 shard pairs have exactly matching record digests. Every primary and replay shard job completed; the failure occurred at final integrity aggregation. No coverage adjudication was performed. The G7 result is therefore **INDETERMINATE**, not PASS and not a coverage-based NOT_VALIDATED result.

## 2. Full-bank artifact comparison

All 80 primary/replay shard artifacts were retrieved from run 44969714756 and compared record by record.

Across all **2,000 paired records**:

- 2,000/2,000 have identical dataset IDs and all three seeds.
- 2,000/2,000 have identical `rows_sha256` values.
- 2,000/2,000 have identical analytical truth records.
- 2,000/2,000 have identical C0 baseline records.
- 2,000/2,000 have identical C5 point estimates, interval endpoints, boundary flags and other comparison fields, except for the abstention reason in seven records.
- 2,000/2,000 have exactly identical within and raw-between interval endpoints.
- 1,993/2,000 have identical C5 abstention reasons; the remaining seven are the only differences in the inferential comparison output.

The 400 records belonging to the eight mismatching shards differ in raw optimizer diagnostics and optimizer-derived provenance. Those differences change the full-record digest even when the inferential outputs are identical.

### 2.1 The seven inferential-status differences

All seven occur in `F5_beta22_M10_R5`:

| Replicate | Primary | Replay |
|---:|---|---|
| 328 | `MLE_NONCONVERGENCE` | `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED` |
| 635 | `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED` | `MLE_NONCONVERGENCE` |
| 639 | `MLE_NONCONVERGENCE` | `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED` |
| 801 | `MLE_NONCONVERGENCE` | `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED` |
| 807 | `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED` | `MLE_NONCONVERGENCE` |
| 972 | `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED` | `MLE_NONCONVERGENCE` |
| 975 | `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED` | `MLE_NONCONVERGENCE` |

In every case, the phase that obtained a successful numerical fit proceeded to the exact global-MLE certificate and classified the likelihood winner as a boundary supremum. The other phase returned early with `MLE_NONCONVERGENCE`. No interval was emitted in either phase for these seven records.

## 3. Root cause in the execution path

In `c10s_fitted_beta_binomial_bootstrap.py`, `fitted_beta_binomial_parametric_bootstrap(..., require_global_mle_certificate=True)` currently:

1. runs `fit_beta_binomial_counts`, which uses three finite-difference L-BFGS-B starts;
2. returns immediately if all three starts are marked unsuccessful;
3. only after an admissible optimizer fit, calls `beta_binomial_global_mle_certificate`.

Consequently, a numerical optimizer termination difference can prevent the exact certificate from running. For the seven records above, one phase reported an optimizer failure while the other reached the exact certificate and found a deterministic boundary supremum. The exact global classification is therefore subordinated to a floating-point optimizer's success flag.

The full-record digest also includes optimizer audit JSON and optimizer-derived provenance. Those fields vary between clean hosted-runner executions even when the inferential outputs are identical.

### 3.1 Environment comparison

The primary and replay jobs used the same recorded runner image release (`ubuntu-24.04`, image release `20261116.376`), CPython 3.12.10, NumPy 2.3.5 and SciPy 1.17.0, installed from the same hash-locked dependency file. Dependency or source-revision drift does not explain the observed discrepancy.

## 4. Proposed engineering correction — not yet approved or implemented

The correction must preserve the exact replay gate for scientific outputs; it must not lower thresholds, pool cells, omit replay, or silently replace one artifact.

Recommended design:

1. **Make the exact certificate authoritative and run it first.** For a certified boundary supremum, unresolved ordering or unavailable algebraic certificate, return the corresponding typed abstention before invoking a numerical optimizer. This removes the seven observed status reversals.
2. **For a certified interior maximum, derive the production fit from the certified root enclosure.** Refine the rational Krawczyk enclosure deterministically, then use a canonical rational representative (for example, its midpoint at a predeclared precision) for the beta-binomial parameters. The three-start L-BFGS-B and analytic optimizer audits remain diagnostics; they do not select or override the certified MLE.
3. **Separate scientific records from numerical diagnostics.** The exact replay digest must cover dataset/seed identity, rows hash, truth, C0/C5 inferential outputs, deterministic certificate status and canonical fit provenance. Preserve raw optimizer diagnostics in a separate, independently hashed sidecar. Do not discard them or pretend they are byte-identical.
4. **Add adversarial regressions.** Include cases where L-BFGS-B reports `ABNORMAL` on one execution and succeeds on another while the exact certificate is unchanged; verify deterministic boundary abstention, canonical interior-fit construction, exact scientific replay equality, and preservation of raw diagnostics.
5. **Validate with deterministic tests and a small resource-namespace replay check.** Do not rerun the 2,000-dataset holdout merely to test the correction.

This changes the G7 v1.0 production-fit implementation and the definition of the canonical replay record. It therefore requires a versioned protocol amendment and a new hash-bound one-use authorization before any further holdout execution. No new calibration run is authorized by this audit.

## 5. Independent G7 feasibility warning

The separate resource-only profile (run [44926453920](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44926453920), validated by [44968818184](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44968818184)) recorded, for M10/R5, 67/100 global interior certificates, 18 boundary suprema, 14 unresolved orderings and one missing certificate status. This is **not** a coverage result and must not be substituted for the prospective holdout. It does, however, warn that the frozen G7 minimum interval-emission requirement of 95% may be unattainable for the current C5 candidate in M10/R5. This risk must be addressed before spending another full-bank execution.

## 6. Governance disposition

- G1–G6 remain PASS for their declared bounded target regime.
- G7 primary and replay computations completed, but replay integrity failed; final coverage adjudication did not run.
- F5 remains **OPEN at G7**. No F5 coverage/calibration claim is established.
- The one-use authorization `G7-20261122-0100` is consumed. A new execution requires a new explicit authorization bound to the corrected code and amended protocol.
- No change to `main`, RMA, Evidence→Claim Matrix, STATUS or any C10 scientific claim is made by this audit.
- The original primary/replay artifacts remain immutable evidence. No shard has been replaced and no coverage metric has been reconstructed from the failed run.

## 7. Artifact index for the eight mismatching shard pairs

| Cell / start | Primary artifact ID | Replay artifact ID |
|---|---:|---:|
| M10/R5 — 300 | 14733425693 | 14734427042 |
| M10/R5 — 600 | 14733281372 | 14734810378 |
| M10/R5 — 800 | 14732908993 | 14734535868 |
| M10/R5 — 950 | 14733475357 | 14734247727 |
| M30/R20 — 100 | 14733940334 | 14734434601 |
| M30/R20 — 300 | 14734140221 | 14734593213 |
| M30/R20 — 700 | 14733861136 | 14734774298 |
| M30/R20 — 750 | 14733428732 | 14734093938 |

The run's artifact inventory contains 40 primary and 40 replay shard artifacts. The eight pairs above are the only pairs whose record digests differ.
