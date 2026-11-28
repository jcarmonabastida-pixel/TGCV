# C10-S — P178 Analyzer replay performance diagnostic 001

**Status:** BOUNDED TECHNICAL PERFORMANCE DIAGNOSTIC — PASS  
**Date:** 2026-11-12  
**Scope:** runtime comparison and deterministic repeatability of the already implemented P178 Analyzer runner. This record does not modify the scientific protocol, estimands, DGP, acceptance criteria, or claim status.

## 1. Canonical source and provenance

- Repository: `jcarmonabastida-pixel/TGCV`
- Source code tested: primary execution commit `689c8f0164e0625ca536a20b1805e555cd63d5fd`
- Primary workflow: `43083651875`
- Recovery replay workflow: `43091630024`
- Bounded performance diagnostic workflow: `43118346835`
- Diagnostic workflow commit: `3bd61ac1520be23fd248fd17de7755ad0140dca7`
- Diagnostic artifact: `13899906259`, SHA-256 `36c2f823ccbffb52e9e0c9ead1ab5254be31f613fe9129708f75bb04b9da9325`
- Primary artifact: `13888821660`, SHA-256 `0218ac9303e588f8d134f43bd73627d51ec59f4281ecac02621a3f20726b288e`

The diagnostic checked out the exact primary source commit, installed the same pinned Python 3.12 / NumPy 2.3.5 / SciPy 1.17.0 environment, and passed the 17 existing software contract tests.

## 2. Verified workflow timings

GitHub Actions job-step timestamps establish the following:

| Operation | Start (UTC) | End (UTC) | Elapsed | Result |
|---|---:|---:|---:|---|
| Primary 27-cell Analyzer Monte Carlo, run 43083651875 | 19:04:09 | 19:28:11 | 24m 02s | PASS |
| Clean-source replay in the same run | 19:28:11 | 19:51:20 | 23m 09s | Cancelled after 26/27 cells |
| Recovery full replay, run 43091630024 | 19:55:29 | 20:24:33 | 29m 04s | Cancelled |

**Correction to the earlier conversational estimate:** for workflow `43083651875`, the primary execution did not take approximately three minutes. GitHub's recorded step timestamps show 24m02s. The original replay ran for 23m09s and completed 26 of 27 cells before cancellation. Thus the original primary and replay had comparable observed throughput; there is no evidence of an order-of-magnitude replay slowdown in that run. The 29m04s recovery attempt was slower, but remains within the same runtime scale and is consistent with runner/runtime variation as a plausible explanation. The available records do not identify a specific environmental cause for that 21% difference.

The recovery workflow is now globally `completed / cancelled`. Its replay compute step is `cancelled`; comparison was skipped; the upload step did not complete. No recovery artifact or full replay PASS was produced.

## 3. Bounded performance diagnostic

Workflow `43118346835` completed successfully in 40 seconds overall. The bounded test ran three representative P178 cells twice, each with 500 replications: 3,000 timed Analyzer invocations in total, plus 100 additional profiled invocations.

- K=2, pi0=0.20, null: 3.025s and 3.040s per 500 replications.
- K=10, pi0=0.50, positive: 3.301s and 3.361s.
- K=50, pi0=0.50, positive: 3.429s and 3.406s.
- Throughput across the six measurements: approximately 146–165 replications/second.
- All three repeated cells produced exactly identical computed metrics (3/3).

The 100-replication cProfile sample recorded 2,365,404 function calls in 1.171s. The principal cumulative costs were:

1. `Analyzer.analyze`: 0.942s across 100 invocations.
2. Student-t critical-value calculation: 0.592s; the custom beta continued-fraction/CDF implementation accounts for most of this.
3. Evidence construction and canonical JSON/hash work: approximately 0.22s.
4. Sealing: approximately 0.146s.

The profile indicates an implementation-level optimization opportunity in repeated Student-t quantile calculation and, secondarily, evidence serialization/sealing. This is a performance observation, not evidence of a statistical defect. No optimization was applied in this diagnostic.

## 4. Interpretation and disposition

- The full primary 27-cell run remains a methodological Analyzer execution with PASS acceptance and a preserved artifact.
- The exact clean-source replay remains **INCOMPLETE / NOT AUDITED**: the first attempt reached 26/27 cells; the recovery attempt was cancelled. No byte-for-byte full replay comparison has passed.
- The bounded repeatability diagnostic is **PASS** for its three sampled cells only. It is not a full replay, does not replace the frozen replay gate, and does not establish full-run byte identity.
- The primary/replay timing discrepancy previously described as approximately 3 minutes versus 45–48 minutes is not supported by the actual timestamps for these workflow IDs. The verified comparison is 24m02s primary, 23m09s first replay attempt, and 29m04s recovery replay attempt.
- No scientific claim, estimand, DGP, acceptance threshold, or confirmatory status is changed.
- `main` is unchanged. This diagnostic and its workflow remain on `research/c10-s-consolidation-draft` under Draft PR #116.

## 5. Next technical action

Do not launch another full 270,000-analysis replay merely to investigate the elapsed-time difference. If a full replay is later required by the frozen execution gate, first instrument and optimize the existing runner without changing its outputs, then verify the optimized implementation against the existing 17 software tests, the one-sample P178 bridge, and exact deterministic reference outputs before any authorized full replay. The custom Student-t quantile path is the first candidate for such an optimization; any replacement must preserve numerical equivalence and be separately reviewed.

