# C10-S — F5 B2/B3 optimizer-start and P/A concordance diagnostic 001

**Date:** 2026-11-20  
**Status:** STATIC RAW-ARTIFACT DIAGNOSTIC — NO ADJUDICATION RULE  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Historical run:** GitHub Actions `44615173745`  
**Historical code commit:** `cdd8617f13296556fd5eb463834fb60c0f051f7c`  
**Artifact ID:** `14586221304`  
**Artifact ZIP SHA-256:** `b3ddcaab1c1028c934f37e3edebf9a176248b21150ab6c2212466b810085f02f`

## 1. Scope and method

This is a read-only analysis of the four existing B2 JSONL banks (5,000 records each). No replay, regeneration, simulation, bootstrap, calibration or scientific execution was performed.

The historical artifact predates the additive P/A reconciliation schema. The direct comparison was therefore reconstructed from values already present in each record:
- **P:** production C5 `fit_alpha`, `fit_beta`, `fit_log_likelihood` in the candidate comparison provenance;
- **A:** analytic-gradient diagnostic `selected_alpha`, `selected_beta`, `selected_log_likelihood` and its three start outcomes in `fit_diagnostics.optimizer_audit`.

The reported shape distance is Euclidean distance in `(log(alpha), log(beta))). Objective gaps for failed analytic starts are measured against the best successful analytic start in the same dataset. These are descriptive raw summaries, not new acceptance criteria. No numerical threshold is proposed or applied.

The downloaded ZIP digest matches the GitHub artifact digest. Bank identities:
- M10/R5 calibration: `cd1d3e4c409b79e28831bcbd8cb9ebd33ff72197e317577578a14c0237a05564`
- M10/R5 validation: `c02e000e6f36fbe1c3ab4f7ed6db2356fe6c4061acc344a4805254c47468bbd2`
- M30/R20 calibration: `6e52d82a18319877a6c1dcde321a219f6ab78f586263e641b74539a54cb7aac5`
- M30/R20 validation: `abb786cd81b1fcd54fa864c539db3916e9d7cf21c8980d6b1cd57feade34c891`

## 2. Direct production P versus analytic A

All differences below are absolute unless explicitly stated. M10/R5 denominators exclude the records where production C5 abstained before an interior P/A pair existed.

| Cell / bank | Interior P/A pairs | |Δ log L| median | q90 | q95 | q99 | max | |log-shape distance| median | q90 | q95 | q99 | max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M10/R5 calibration | 4,822 | 7.46e-14 | 3.46e-6 | 5.47e-4 | 2.49e-3 | 6.25e-3 | 3.42e-7 | 3.146 | 11.828 | 14.201 | 16.260 |
| M10/R5 validation | 4,798 | 7.11e-14 | 7.93e-7 | 4.04e-4 | 2.36e-3 | 4.38e-3 | 3.28e-7 | 0.290 | 11.686 | 14.164 | 16.856 |
| M30/R20 calibration | 5,000 | 5.26e-13 | 2.46e-12 | 3.55e-12 | 6.57e-12 | 6.06e-11 | 2.74e-7 | 7.64e-7 | 1.00e-6 | 1.52e-6 | 6.76e-6 |
| M30/R20 validation | 5,000 | 5.26e-13 | 2.36e-12 | 3.51e-12 | 6.47e-12 | 8.07e-11 | 2.76e-7 | 7.79e-7 | 9.82e-7 | 1.47e-6 | 6.62e-6 |

Additional M10/R5 counts:
- Calibration: 499/4,822 P/A pairs have absolute log-likelihood difference above 1e-6; 177/4,822 above 1e-3.
- Validation: 480/4,798 above 1e-6; 165/4,798 above 1e-3.

Interpretation:
- **M30/R20:** P and A are numerically concordant across the full banks. The maximum absolute likelihood difference is below 8.1e-11 and maximum log-shape distance below 6.8e-6. This is strong evidence of P/A numerical agreement in the observed records, not proof of global optimality or statistical identification.
- **M10/R5:** the median P/A pair is close, but the upper tail contains large parameter divergence with comparatively small likelihood differences. This is consistent with the already observed near-binomial concentration ridge. Likelihood similarity alone is insufficient to adjudicate the concentration estimate.
- The M10/R5 production-versus-analytic discrepancies are not explained by the independent BFGS precision-loss flag alone. They are a distinct fit-path/weak-identification issue.

## 3. Three analytic L-BFGS-B starts: raw outcome structure

| Cell / bank | Records with ≥1 failed start | Failed start outcomes | All 3 report success | Failed-start objective gap: median / q90 | Failed-start terminal distance to best successful start: median / q90 |
|---|---:|---:|---:|---:|---:|
| M10/R5 calibration | 787 | 931 | 4,213 | 1.58e-8 / 2.50e-6 | 0.546 / 1.854 |
| M10/R5 validation | 776 | 895 | 4,224 | 8.08e-8 / 2.50e-6 | 0.633 / 1.784 |
| M30/R20 calibration | 342 | 349 | 4,658 | 1.42e-14 / 21.61 | 4.63e-8 / 16.13 |
| M30/R20 validation | 355 | 363 | 4,645 | 0 / 19.84 | 4.43e-8 / 16.06 |

The failed-start objective gap is the failed start's negative log-likelihood minus the best successful start's negative log-likelihood. The terminal distance uses the two fitted coordinates `(mean_logit, log_concentration)`. Large q90 values alongside near-zero medians indicate heterogeneous outcomes rather than one uniform failure mode.

Two additional observations matter:
- In M30/R20, many failed starts terminate extremely close to a successful solution with essentially the same objective, while a minority terminate far away with much worse objectives. A single Boolean “all starts succeeded” collapses these different states.
- Conversely, all-success is not sufficient evidence of start concordance: the successful-start objective spread exceeds 1e-6 in 35/5,000 M30/R20 calibration records and 29/5,000 validation records; maxima are 25.17 and 26.56. Success flags alone therefore do not establish that all starts found the same admissible optimum.
- In M10/R5, failed starts have materially broader terminal-coordinate distances even when objective gaps are small. This is compatible with a flat concentration direction; a failed start cannot be declared harmless from its objective alone.

## 4. Reconciliation with frozen B1 and §8

Frozen B1 requires retaining and comparing all three start outcomes, and explicitly states that optimizer success flags alone do not establish an admissible global MLE. It does **not** state that every start must individually report success.

Frozen §8 separately requires that C5 eligibility have no unresolved numerical state. Therefore:
1. The runner's all-three-starts-success condition is an implementation-level stricter condition, not a verbatim frozen B1 rule.
2. Removing that condition without a replacement diagnostic would not satisfy §8.
3. Replacing it with “at least one start succeeded” would be scientifically unjustified and contradicted by the all-success-but-discordant records.
4. A failed start near the best successful solution and a failed start far from it are different raw states; M10/R5 and M30/R20 also have different patterns.
5. No retrospective B2/B3 status change is permissible. The historical component gates remain failed, and the historical optimizer states remain as originally adjudicated.

**Disposition:** the current all-starts-success Boolean should not be treated as the final scientific interpretation of B1. However, no alternative threshold or pass rule is justified by this analysis. Preserve the frozen no-unresolved-state gate and keep optimizer/start adjudication unresolved until an independently justified rule is specified and tested prospectively.

## 5. What this closes and what remains open

Closed by this static diagnostic:
- direct P/A comparisons reconstructed across all 20,000 historical dataset records where the P/A pair exists;
- confirmation of strong P/A agreement in M30/R20;
- confirmation of a broad P/A parameter ridge in M10/R5 despite near-equal median likelihoods;
- demonstration that “all three success” is neither necessary as a literal B1 condition nor sufficient to establish concordance;
- evidence that failed-start outcomes are heterogeneous and design-dependent.

Still open:
- a scale-aware, scientifically justified way to adjudicate successful-start spread and failed-start competitiveness without using arbitrary post-hoc thresholds;
- independent global-optimum evidence where likelihood profiles are flat or multiple starts disagree;
- the separate M30/R20 C5 high-concentration plug-in interval undercoverage mechanism.

No C5 gate, optimizer acceptance threshold, interval method, DGP, seed, B/K, frozen specification or historical result was changed. No new numerical execution was performed.
