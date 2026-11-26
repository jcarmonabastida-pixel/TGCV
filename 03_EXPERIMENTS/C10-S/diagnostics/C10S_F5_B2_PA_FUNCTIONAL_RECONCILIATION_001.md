# C10-S — Historical F5 production/analytic fit comparison on W/B functionals

**Date:** 2026-11-26  
**Status:** POST-HOC DESCRIPTIVE DEVELOPMENT DIAGNOSTIC — NO METHOD SELECTION / NO THRESHOLD  
**Branch:** `research/c10s-instrumental-autonomous-workpackage-20261126`  
**Historical run:** `44615173745`  
**Historical code commit:** `cdd8617f13296556fd5eb463834fb60c0f051f7c`  
**Artifact ID:** `14586221304`  
**Artifact ZIP SHA-256:** `b3ddcaab1c1028c934f37e3edebf9a176248b21150ab6c2212466b810085f02f` (downloaded artifact digest verified)

## 1. Scope and restriction

This is a deterministic, offline re-expression of terminal production/analytic fit parameters already retained in the four historical B2 JSONL banks. It performs no data generation, refitting, bootstrap, calibration, adjudication, or coverage recomputation.

The artifact is historical development evidence. It is not confirmatory evidence and is not used here to select M1/M2, tune an estimator, set a numerical tolerance, alter the frozen specification, or revise B2/B3 outcomes. The purpose is narrowly diagnostic: determine whether the recorded production/analytic parameter differences also imply differences in the two target functionals.

The production/analytic reconciliation was added after the original B2 artifact was generated. Accordingly, the two fit paths are reconstructed from the parameters already stored in the historical optimizer audit; no missing values are imputed.

## 2. Functional reconstruction

For each stored production fit ((\hat\mu_P,\hat\kappa_P)) and analytic fit ((\hat\alpha_A,\hat\beta_A)), reconstruct:

[
\hat\mu_A=\frac{\hat\alpha_A}{\hat\alpha_A+\hat\beta_A},
\qquad
\hat\kappa_A=\hat\alpha_A+\hat\beta_A,
]

[
\hat W=\mu(1-\mu)\frac{\kappa}{\kappa+1},
\qquad
\hat B=\mu(1-\mu)\frac{1}{\kappa+1}.
]

The frozen beta22 truths are (W=0.20) and (B=0.05). The comparison uses the exact values stored in the artifact, with ordinary binary64 evaluation of the two algebraic functionals.

## 3. P/A functional differences

For each bank/cell, the table reports records with both parameterizations available, missing analytic terminal-parameter records, the 95th percentile and maximum of (max(|\Delta W|,|\Delta B|)), and the number of records where either functional difference exceeds (10^{-6}). The (10^{-6}) count is descriptive only; it is not an acceptance threshold.

| Cell | Bank | P/A available | Analytic params missing | 95th percentile max(|ΔW|,|ΔB|) | Maximum | Records > 1e-6 |
|---|---:|---:|---:|---:|---:|---:|
| M10/R5 | Calibration | 4,897/5,000 | 103 | 1.084e-9 | 1.537e-5 | 18 |
| M10/R5 | Validation | 4,879/5,000 | 121 | 1.036e-9 | 2.922e-5 | 14 |
| M30/R20 | Calibration | 5,000/5,000 | 0 | 3.529e-10 | 5.798e-9 | 0 |
| M30/R20 | Validation | 5,000/5,000 | 0 | 3.084e-10 | 5.323e-9 | 0 |

Component-specific summaries:

- **M10/R5 calibration:** (Q_{0.95}(|\Delta W|)=1.036e-9), max (1.537e-5); (Q_{0.95}(|\Delta B|)=1.377e-10), max (1.646e-8).
- **M10/R5 validation:** (Q_{0.95}(|\Delta W|)=1.017e-9), max (2.922e-5); (Q_{0.95}(|\Delta B|)=1.336e-10), max (4.613e-9).
- **M30/R20 calibration:** (Q_{0.95}(|\Delta W|)=3.211e-10), max (5.531e-9); (Q_{0.95}(|\Delta B|)=2.269e-10), max (5.798e-9).
- **M30/R20 validation:** (Q_{0.95}(|\Delta W|)=2.770e-10), max (4.888e-9); (Q_{0.95}(|\Delta B|)=1.809e-10), max (5.323e-9).

The historical runner's `fit_status_counts` recorded 5,000/5,000 `INTERIOR` production fits in each bank/cell. Missing P/A terminal values therefore denote missing analytic comparison values, not missing production fit records or a new estimate of production emission.

## 4. Fitted functional point-estimate summaries

These means/RMSEs are also descriptive summaries of the historical fitted functional point estimates, not coverage results:

| Cell | Bank | Production mean W | Production mean B |
|---|---|---:|---:|
| M10/R5 | Calibration | 0.197953 | 0.043079 |
| M10/R5 | Validation | 0.198258 | 0.042738 |
| M30/R20 | Calibration | 0.200390 | 0.047662 |
| M30/R20 | Validation | 0.200261 | 0.047742 |

The corresponding P/A means agree to the displayed precision. Relative to the beta22 truths, the fitted B point estimates are lower on average, particularly in M10/R5. This is a separate statistical property from numerical P/A agreement and is not resolved by the present diagnostic.

## 5. Interpretation and limits

1. The M10/R5 concentration/shape ridge and parameter-level optimizer discrepancies do not automatically imply equally large disagreement in (W) or (B). On the records where both paths return parameters, the two functional values are usually much closer than the parameter coordinates suggest.
2. This supports an estimand-specific fit-state investigation: parameter distance alone should not be treated as proof that the target functional is numerically unresolved.
3. It does **not** establish global MLE status. The analytic audit's independent BFGS check is initialized from the analytic fit; it is not an independent global search.
4. It does **not** validate M1-PCT, M1-BASIC, or M2. No refitted functional bootstrap was performed.
5. It does **not** repair the historical C5 within/raw-between coverage failures, explain their causes, or justify ignoring unresolved optimizer records.
6. No numerical threshold is proposed. A prospective fit-state rule must be justified independently and frozen before any new development comparison.

## 6. Disposition

**Retain as a descriptive historical diagnostic only.** It motivates evaluating functional-specific stability in the prospective M1 fit contract, but it does not select M1, set tolerances, or replace a fresh development comparison. B2/B3 outcomes and adjudications remain unchanged.
