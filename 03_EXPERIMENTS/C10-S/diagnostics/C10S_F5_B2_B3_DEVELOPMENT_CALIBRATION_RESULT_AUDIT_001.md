# C10-S — F5 B2/B3 development calibration and validation result audit

**Record:** C10S-F5-B2-B3-DEVELOPMENT-CALIBRATION-RESULT-AUDIT-001  
**Date:** 2026-11-20  
**Status:** PRIMARY EXECUTION INTEGRITY PASS / F5 COMPONENT GATES FAIL / NO VALIDATED F5 INTERVAL METHOD  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Frozen specification:** `C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md`, v1.0 (unchanged)

## 1. Execution identity and authorization

- GitHub Actions run: `44615173745` — `SUCCESS`.
- Run URL: https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44615173745
- Authorization ID: `F5-B2B3-20261119-2202`.
- Authorization commit: `888844bded0f677853535f9603d4523f3397197f`.
- Approved code commit: `cdd8617f13296556fd5eb463834fb60c0f051f7c`.
- The workflow validated the one-use authorization, sole parent, source hashes and F5-only scope before checking out the exact approved code. Hash-locked dependency installation and numerical execution completed successfully.
- Artifact ID: `14586221304`; name `c10s-f5-b2-b3-F5-B2B3-20261119-2202-cdd8617f13296556fd5eb463834fb60c0f051f7c`; 22,441,514 bytes; nine files.
- Artifact ZIP SHA-256: `b3ddcaab1c1028c934f37e3edebf9a176248b21150ab6c2212466b810085f02f`. Independently downloaded ZIP digest matches GitHub artifact metadata.
- Runtime: 9,476.03 s (2 h 37 min 56 s); peak process RSS 463,613,952 bytes.
- Environment: Python 3.12.10, NumPy 2.3.5, SciPy 1.17.0; dependency lock SHA-256 `4bdd6993cd8add430dab560f2e6eabb73028b4693e7f73e73999ecda4b2a30a9`.

## 2. Scope and execution integrity

Exactly the two frozen F5 beta22 cells were run:
- `F5_beta22_M10_R5`
- `F5_beta22_M30_R20`

For each cell:
- 5,000 calibration datasets;
- 5,000 disjoint development-validation datasets;
- C0 and C5 bootstrap B=1,000;
- 250 pre-outcome-selected calibration datasets for B3, with C5 B=1,000 and B=4,000.

Integrity checks on the retrieved artifact:
- All four B2 JSONL banks contain exactly 5,000 rows, unique dataset IDs and unique dataset seeds; replicate indices span 0–4,999.
- Calibration and validation dataset IDs and dataset seeds are disjoint in both cells.
- The manifest's historical seed collision audit is PASS: 61,000 new seed values checked and unique against 64,600 historical unique values across the declared schedules.
- All seven output files listed in `summary.json` match their recorded SHA-256 digests.
- B3 contains exactly 250 unique datasets per cell. The selected IDs exactly match the selection manifest; selection declares `selection_uses_c5_outcomes=false`. All 500 B3 rows match the original calibration dataset seed and row hash.
- F1 A2/A3, Tier B, comparative holdout and C10 scientific execution are all false in the execution manifest.
- F5 MCSE interval construction remains explicitly out of scope/abstained. No MCSE interval is promoted or adjudicated.

The execution/artifact integrity checks therefore PASS. This is separate from the scientific acceptance result.

## 3. Frozen component adjudication — C5

The frozen gate is applied separately to every cell × bank × target: conditional coverage in [0.93, 0.97], 95% Wilson interval containing 0.95, interval emission at least 0.95, exact denominator, and no unresolved numerical optimizer state. No pooling or averaging is permitted.

| Cell / bank | Target | Coverage | 95% Wilson interval | Emission | Gate |
|---|---|---:|---:|---:|---|
| M10/R5 calibration | within | 97.74% | [97.29%, 98.12%] | 98.22% | FAIL |
| M10/R5 calibration | raw-between | 98.33% | [97.93%, 98.65%] | 98.22% | FAIL |
| M10/R5 validation | within | 98.02% | [97.59%, 98.38%] | 98.10% | FAIL |
| M10/R5 validation | raw-between | 98.70% | [97.93%, 98.65%] | 98.10% | FAIL |
| M30/R20 calibration | within | 94.04% | [93.35%, 94.66%] | 100.00% | FAIL |
| M30/R20 calibration | raw-between | 93.08% | [92.34%, 93.75%] | 100.00% | FAIL |
| M30/R20 validation | within | 93.96% | [93.27%, 94.59%] | 100.00% | FAIL |
| M30/R20 validation | raw-between | 93.00% | [92.26%, 93.67%] | 100.00% | FAIL |

Interpretation:
- M10/R5 C5 materially overcovers both targets in calibration and independent development validation; point coverage exceeds the frozen 97% upper limit and Wilson intervals do not contain 95%.
- M30/R20 C5 point coverage is within the [93%,97%] band, but all four Wilson intervals (within/raw-between in both banks) lie below 95%; the Wilson requirement therefore fails. Raw-between is close to the lower point-coverage boundary (93.08% calibration; 93.00% validation).
- C5 emission itself meets the >=95% gate in every component, but this does not rescue coverage or optimizer failures.
- Result: **0/8 C5 components pass the complete frozen gate.** The summary disposition is `NO_VALIDATED_F5_COMPONENT_INTERVAL_METHOD`.

### 3.1 C5 fit and optimizer diagnostics

M10/R5:
- Calibration: 89 abstentions (15 concentration-at-upper-bound; 74 primary multi-start nonconvergence); 4,911 interior fits.
- Validation: 95 abstentions (20 concentration-at-upper-bound; 75 primary multi-start nonconvergence); 4,905 interior fits.
- Independent optimizer audit statuses: calibration 2,169 unresolved, 2,727 concordant, 103 no admissible primary fit, 1 discordant; validation 2,132 unresolved, 2,747 concordant, 121 no admissible primary fit.
- The unresolved independent optimizer termination message is `Desired error not necessarily achieved due to precision loss.`

M30/R20:
- All 5,000 fits are classified interior in each bank; no C5 intervals are abstained.
- Independent optimizer audit remains unresolved for 3,270/5,000 calibration fits and 3,259/5,000 validation fits; the remainder are concordant.
- The unresolved independent optimizer termination message is again precision loss.

Important diagnostic nuance:
- The unresolved label must not be waived after seeing the result: the frozen gate requires no unresolved numerical optimizer state.
- However, the raw diagnostics show near-identical objective values for many such fits. In M30/R20, median absolute log-likelihood difference is zero and the maximum is approximately 4.83e-13 (calibration) / 4.12e-13 (validation), despite the independent optimizer's precision-loss termination message. In M10/R5 the maximum difference is 4.53e-6 / 5.72e-6. These facts justify a targeted numerical investigation of the independent optimizer's precision-loss classification, gradients and terminal coordinates; they do not by themselves certify a global MLE or alter this run's gate.
- No binary weak-identification threshold is inferred from the raw curvature or optimizer status.

## 4. Matched C0 comparator

C0 emits all intervals (100%) but also fails the frozen coverage/Wilson criteria in both cells and banks:
- M10/R5 within coverage is 93.64% calibration and 93.82% validation; raw-between is 98.66% and 98.96%.
- M30/R20 within coverage is 93.40% and 93.86%; raw-between is 96.52% and 96.40%.
- The Wilson intervals for these C0 components do not contain 95%. M10/R5 raw-between also exceeds the 97% upper point-coverage limit.

C0 is a comparator, not a substitute acceptance route. The fact that both C0 and C5 fail does not validate either method.

## 5. B3 endpoint Monte Carlo sensitivity

B3 is diagnostic only and is not used for coverage adjudication.

Integrity:
- 250 pre-outcome-selected datasets per cell; all selected IDs, calibration seeds and row hashes match.
- M10/R5: 5 of 250 selected datasets have null C5 endpoints at both B values because the original calibration fit abstained for `MLE_NONCONVERGENCE`; 245 have paired endpoint values.
- M30/R20: all 250 have paired endpoint values.

Rank uncertainty:
- At B=1,000 the approximate 95% order-statistic rank uncertainty width is 20 ranks (2% of B).
- At B=4,000 it is 40 ranks (1% of B).
- Thus the relative rank uncertainty halves when B quadruples; absolute rank width increases as expected on the larger rank scale.

Endpoint changes (B=4,000 minus B=1,000):
- M10/R5 paired endpoint shifts have medians zero; central 90% ranges are approximately ±0.01 for within endpoints and roughly -0.0062 to +0.0073 for raw-between upper endpoints (lower endpoints roughly -0.0044 to +0.0038).
- M30/R20 endpoint shifts are smaller: central 90% ranges are approximately -0.0021 to +0.0022 for within lower endpoints and -0.00235 to +0.00183 for raw-between upper endpoints; medians are close to zero.

B3 therefore indicates modest finite-B endpoint variability on the selected development datasets, with five M10/R5 abstentions preserved. It does not show that increasing B corrects the observed M10/R5 overcoverage or M30/R20 undercoverage. B=4,000 is not substituted for the frozen B=1,000 primary analysis.

## 6. Scientific and operational disposition

**F5 B2/B3: EXECUTED AND PRIMARY ARTIFACT INTEGRITY AUDITED.**  
**C5 within/raw-between: NOT VALIDATED under frozen v1.0 gates.**  
**C0 comparator: NOT VALIDATED under the same coverage/Wilson criteria.**  
**MCSE: OUT OF SCOPE / EXPLICIT ABSTENTION.**  
**Confirmatory status: NONE.** Both banks are development data and cannot be reused as a future confirmatory holdout.

The main scientific signal is a design-dependent coverage pattern: C5 overcovers at M10/R5 and undercovers relative to the Wilson nominal criterion at M30/R20. Optimizer precision-loss diagnostics are frequent, especially at M30/R20, but the coverage failures are independently sufficient to prevent acceptance.

No threshold, interval rule, estimator, DGP, K/B value or frozen criterion was changed after observing results. No calibration bank was retuned and no result was pooled to rescue a family. No Tier B, F1 A2/A3, comparative holdout or C10 causal execution occurred.

## 7. Next work — diagnosis, not another calibration run

The next coordinated static/diagnostic work should:
1. Reconcile the exact independent-optimizer implementation, termination messages, gradients, terminal coordinates and objective differences against the per-dataset records, separating precision-loss termination from genuine optimizer disagreement.
2. Identify whether the optimizer-audit unresolved rate is a numerical-coordinate/gradient issue, a tolerance/termination issue, or substantive likelihood ambiguity. Any revised adjudication rule must be specified and tested independently before any new numerical bank; it cannot be retrofitted to relabel this run.
3. Diagnose the M10/R5 overcoverage and M30/R20 raw-between undercoverage against the frozen beta-binomial DGP/oracle and the estimator's finite-M/R behaviour, keeping within and raw-between distinct.
4. Treat B3 only as endpoint Monte Carlo sensitivity evidence; do not increase B or rerun K as a reflex.
5. If a revised C5 candidate or rule is genuinely necessary, create a new versioned design decision and fresh disjoint development banks. The current banks remain historical development evidence and are not confirmatory.

No further numerical execution is authorized by the one-use authorization used for run `44615173745`. The frozen specification v1.0 remains unchanged.
