# C10-S — Post-holdout F1/F5 resource preflight result

**Record:** C10S-POST-HOLDOUT-F1-F5-RESOURCE-PREFLIGHT-RESULT-001  
**Date:** 2026-11-19  
**Run:** 44603264310 — SUCCESS  
**Authorization:** C10S-PF-20261119-01  
**Authorization commit:** c5c752c5fe16d489d6ed80c9d0233460fd2e128e  
**Approved code commit:** b44489341e4ee99aa279b15d6cb635e744a1665e  
**Artifact:** `c10s-post-holdout-resource-preflight-C10S-PF-20261119-01-b44489341e4ee99aa279b15d6cb635e744a1665e`  
**Artifact SHA-256:** `79d1fce857aeee9fde993dd2ba690d6a623feaacee486cc835f8e15a8dbab56a`  
**Scope:** resource-only; no coverage adjudication, calibration, validation, holdout or causal C10 execution.

## 1. Execution and integrity

The workflow completed successfully. All steps passed: one-use authorization and hash validation, exact approved-parent check, checkout of the approved code commit, hash-locked dependency installation, bounded sample execution, and artifact upload.

The downloaded ZIP digest matches GitHub's artifact digest. It contains:
- `post_holdout_resource_preflight.json`
- `post_holdout_resource_preflight_summary.json`

The manifest records 200 unique dataset IDs and 200 distinct row hashes, with 200 distinct dataset seeds and C0 seeds; the 100 F5 records also have 100 distinct seeds for each C5 stream. No untyped execution errors occurred.

Historical seed separation: PASS. The check reports 64,000 historical seed values checked across 8 cells × 1,000 replicates and three historical schedules; 600 new preflight stream seeds were collision-checked.

Environment: Python 3.12.10, NumPy 2.3.5, Ubuntu Linux x86_64. Source, spec, dependency-lock, authorization and workflow identities are recorded in the artifact.

## 2. Measured resource results

| Cell | K | Total elapsed | Seconds/dataset | Comparison path | Additional path | Peak RSS high-water |
|---|---:|---:|---:|---:|---:|---:|
| F1 balanced M30/R20 | 100 | 5.656 s | 0.05656 s | 2.466 s | A2 profile statistic 0.110 s; full profile inversion 2.971 s | 116.72 MiB |
| F5 beta22 M30/R20 | 100 | 165.226 s | 1.65226 s | C0/C5 B=1,000: 46.244 s | C5 B=4,000 incremental: 118.901 s | 119.00 MiB |

RSS is a process-lifetime cumulative high-water mark, not an independent per-cell peak. The process maximum was 119.00 MiB.

## 3. F1 technical observations

All 100 F1 datasets completed the profile inversion with:
- `PROFILE_LR_INTERVAL_ROOT_SOLVED`;
- `POLYNOMIAL_SCORE_BOUNDED_OPTIMIZER_CONCORDANT`;
- `ANALYTIC_CONNECTEDNESS_ARGUMENT_APPLIED`.

There were no F1 typed abstentions or untyped execution failures in this sample. The LR cutoff was a computational benchmark only and was not used for coverage or calibration. These observations establish successful execution of this representative computational path; they do not establish coverage or calibration.

## 4. F5 critical limitation

All 100 F5 primary comparison records reported an interior fit (`INTERIOR`), but all 100 also carried:
`F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED`.

The same reason appears in all 100 B=4,000 sensitivity records. In the estimator implementation, the MCSE interval is deliberately left unset and the failure reason is emitted because the boundary-aware joint inference method is not implemented. Thus:
- optimizer fitting and bootstrap workload were executed and timed;
- a valid C5 MCSE interval was **not** produced;
- the B=4,000 measurement is a runtime benchmark, not evidence of inferential readiness;
- this preflight does not clear F5 for calibration/validation.

This is a fail-closed methodological limitation, not an execution crash. Do not reinterpret `INTERIOR` fit status as an emitted or valid interval.

## 5. Full-workload projection

Linear extrapolation from one M30/R20 representative cell per family gives:

| Work package | Projected work | Projected time |
|---|---:|---:|
| F1 A2 calibration statistic | 30,000 datasets | 32.934 s |
| F1 A3 comparison + profile inversion | 30,000 datasets | 1,663.924 s |
| F5 B2 C0/C5 B=1,000 | 20,000 datasets | 9,265.149 s |
| F5 B3 incremental C5 B=4,000 | 500 selected datasets | 594.503 s |
| **Total** | | **11,556.509 s = 3.210 h** |

The projection is advisory and assumes linear scaling. It is not a runtime guarantee; it excludes workflow/setup overhead and may not capture variation across other M/R cells. The F5 projected work remains computationally measurable but is not inferentially actionable until the MCSE joint boundary method is implemented and independently validated.

## 6. Gate adjudication

| Gate | Result |
|---|---|
| Authorized resource-only workflow | PASS |
| Exact code/spec/dependency provenance | PASS |
| Seed separation | PASS |
| 200-dataset sample and row integrity | PASS |
| F1 representative computational path | PASS |
| F5 optimizer/bootstrap resource path | PASS, with explicit inference abstention |
| F5 C5 interval/inferential readiness | **BLOCKED — method not implemented** |
| Coverage/calibration/validation | NOT RUN |
| Tier B / causal C10 execution | NOT AUTHORIZED and NOT RUN |

**Overall:** RESOURCE_PREFLIGHT_EXECUTION_PASS / F5_INFERENTIAL_READINESS_BLOCKED.

No frozen specification value, dataset denominator, acceptance criterion or historical result was changed. The next scientific-development task is to close the F5 joint MCSE boundary-inference method and its tests before any F5 calibration or validation execution is proposed. The 3.21-hour projection must not be used to imply that the full F1/F5 calibration programme is ready to run.
