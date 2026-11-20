# C10-S F5 — G7 prospective Tier-A calibration protocol 001

**Record:** C10S-F5-G7-TIERA-PROSPECTIVE-001  
**Version:** 1.0  
**Status:** FROZEN RESEARCH PROTOCOL — EXECUTION AUTHORIZED BY USER ON 2026-11-20; ONE-USE WORKFLOW GATE REQUIRED  
**Scope:** F5 beta-binomial Tier-A relevance and coverage only  
**Parent:** F5 end-to-end closure dossier G7; frozen Tier-A comparability criteria  
**Branch:** `research/c10s-f1-integrated-correction-20261119`

## 1. Purpose and boundary

This is the prospective G7 test of whether the F5 beta-binomial fitting and interval procedure, after the G1–G6 global-MLE certification work, is reliable enough for the F5 component of C10-S. It is an instrumental calibration gate, not the C10 causal experiment and not evidence for `ΔT_acc → Value`.

The prior v1.0 eight-cell comparative holdout (run 44572812481) is consumed, unblinded and NOT_VALIDATED. Its data, seeds, summaries and results are excluded from all G7 denominators, tuning and calibration. The original v002 Tier-A bank and B2/B3 development outputs are also excluded.

The existing C5 fitted beta-binomial percentile interval method is retained. The only F5 fit change is a fail-closed exact global-MLE certification gate: the three-start production optimizer's selected fit is used only when the exact Bernstein/conditional-mean/Krawczyk certificate returns `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED` and the fitted (mean, compactified concentration) lies inside the certified unique-root box. Otherwise C5 abstains with a typed reason. No interval formula, percentile rule or target is changed.

## 2. Frozen target cells and replication

Exactly two F5 beta(2,2) cells are included:

| Cell | M | R | K | Within truth | Raw-between truth |
|---|---:|---:|---:|---:|---:|
| F5 beta22 M10/R5 | 10 | 5 | 1,000 | 0.20 | 0.05 |
| F5 beta22 M30/R20 | 30 | 20 | 1,000 | 0.20 | 0.05 |

C0 uses the frozen v002 two-stage percentile bootstrap with B=1,000. C5 uses the existing fitted beta-binomial parametric percentile procedure with B=1,000, plus the exact global-MLE certification gate above. Both methods receive the same generated M×R dataset. Analytical truth is generated independently and is never passed to C5.

## 3. Seed separation and resource preflight

- Holdout seed schedule: `C10S_F5_G7_TIERA_SEEDS_1.0`.
- Holdout namespace: `c10s_f5_g7_holdout_v1`.
- Resource-only namespace: `c10s_f5_g7_resource_v1`.
- Dataset, C0 and C5 seeds are separately derived by SHA-256 from schedule, namespace, stream, cell ID and replicate index.
- The implementation checks for within-bank collisions and collisions against the consumed v1.0 comparative holdout schedule. Resource seeds are disjoint from holdout seeds.
- Before the holdout, run a resource-only preflight of K=100 per cell with C0/C5 B=1,000 and global-MLE certification. It must not call coverage adjudication or inspect interval success. The preflight uses a separate namespace and its datasets never enter the holdout.
- If the linear primary-plus-replay projection exceeds 4.5 hours, stop before generating holdout data.

## 4. Methods, metrics and acceptance

The confirmatory targets are within variance and untruncated raw-between variance. MCSE remains explicitly non-confirmatory and abstained for C5.

For each cell × method × component, report:
- K and point/interval emission rates;
- conditional coverage and its two-sided 95% Wilson interval;
- unconditional cover rate;
- lower/upper miss rates;
- point bias, RMSE, median absolute error and mean interval width;
- typed abstentions, fit/certificate statuses and convergence/boundary diagnostics;
- exact dataset/method/truth accounting and raw-between negative values;
- runtime/resource preflight and primary/replay identity.

A C5 component-cell passes only if:
1. conditional coverage is in [0.93, 0.97];
2. the two-sided 95% Wilson interval contains 0.95;
3. interval emission is at least 0.95;
4. all 1,000 datasets are accounted for exactly once with the expected C0/C5 roster and independent truth pairing;
5. all emitted endpoints are finite and ordered;
6. raw-between estimates and endpoints are untruncated.

G7 passes for F5 only if C5 passes all four component cells (two targets × two M/R cells). No pooling or averaging is permitted. C0 is retained as the matched baseline reference; its failure does not substitute for or rescue C5. If any C5 component fails, G7 is NOT_VALIDATED for that target regime. If the criterion cannot be evaluated because of integrity/resource failure, G7 is INDETERMINATE.

## 5. Execution, replay and exclusions

Run the full two-cell primary bank, then a clean-source replay with identical code, protocol, inputs and seeds. Primary/replay per-cell records, summaries and digests must match exactly. Any mismatch blocks coverage adjudication.

The workflow is one-use and hash-bound to protocol, code, fitter, exact-certificate module, inference engine, fixture generator, dependency lock, validator, executor and workflow. The authorization is bound to the exact code commit as the sole parent of a commit changing only the authorization JSON.

Explicit exclusions: F1, Tier B, F2, B2/B3 development banks, the consumed v1.0 holdout, original v002 Tier-A data, new stress cells, M1/M2 interval alternatives, F5 MCSE coverage, C10 Generator/Analyzer/Evaluator, and any causal/Value claim.

## 6. Decision consequences

- **PASS:** F5's existing C5 within/raw-between percentile procedure is calibrated for the declared beta(2,2) M10/R5 and M30/R20 synthetic regimes, subject to the exact global-fit certificate and stated limits. This does not establish F5 for other distributions/designs or C10 causal validity.
- **NOT_VALIDATED:** one or more predeclared C5 coverage/emission criteria fail; preserve the limiting evidence and do not retune on the G7 bank.
- **INDETERMINATE:** execution integrity, resource or replay requirements prevent valid adjudication.

No result automatically changes C10 claims, Core, RMA, Evidence→Claim Matrix, STATUS or main.
