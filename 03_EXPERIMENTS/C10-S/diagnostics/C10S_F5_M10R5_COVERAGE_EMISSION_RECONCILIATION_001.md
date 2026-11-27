# C10-S — F5 M10/R5 coverage and emission reconciliation 001

**Status:** HISTORICAL DIAGNOSIS — NO NEW SIMULATION / NO METHOD SELECTION  
**Date:** 2026-11-27  
**Branch:** `research/c10s-coverage-first-focus-20261127`  
**Purpose:** distinguish the actual F5 M10/R5 coverage defect from method-specific emission failures, and prevent an invalid repair based on conflating different procedures.

## 1. Decision summary

**No minimum replacement interval method is currently supported by the evidence.** The current C5 plug-in percentile procedure emits adequately but overcovers. The M1-PCT refitted bootstrap has a severe emission failure under its strict all-refits-admissible contract. G7 v1.1 also fails emission under its separate global-MLE/certification contract. These are not one combined failure of one method.

Do not attempt to repair C5 coverage by weakening M1/G7 abstention, and do not treat a higher optimizer certification rate as a coverage correction.

## 2. Keep the methods and their results separate

| Procedure / evidence | M10/R5 within | M10/R5 raw-between | Emission | Meaning |
|---|---:|---:|---:|---|
| C5 B2 calibration | 97.74% | 98.33% | 98.22% | Coverage failure; emission passes |
| C5 B2 validation | 98.02% | 98.70% | 98.10% | Coverage failure; emission passes |
| G7 v1.1 | 98.644% | 99.661% | 88.5% | Separate method fails both coverage and emission |
| M1-PCT pilot | 100%* | 100%* | 4% | Not calibrated; only two intervals emitted |

*Descriptive coverage of only the two emitted M1-PCT intervals; it is not an estimate of calibrated coverage.

Sources:
- `C10S_F5_B2_B3_DEVELOPMENT_CALIBRATION_RESULT_AUDIT_001.md`
- `C10S_F5_M1_PCT_DEVELOPMENT_PILOT_RESULT_001.md`
- `C10S_F1_F5_INTEGRATED_SIMPLIFICATION_AUDIT_001.md` §3.4 and G7 v1.1 adjudication, consolidated in `C10S_TIER_A_COVERAGE_LEDGER_001.md`.

## 3. What the existing evidence establishes about C5

### 3.1 The aggregate overcoverage hides opposite conditional behaviours

The B2/B3 post-result diagnostic stratified the already exposed development data by fitted concentration. This is exploratory diagnosis only; it is not a new acceptance stratum or tuning rule.

For M10/R5, the top fitted-concentration decile is close to the binomial limit:
- median fitted concentration κ approximately 5,561 (calibration) and 5,468 (validation), versus DGP truth κ=4;
- profile curvature is nearly flat and likelihood advantage over the binomial limit is very small;
- C5 coverage in this decile falls to 93.1%/89.4% (within/raw-between) in calibration and 92.1%/91.0% in validation;
- C5 intervals are materially narrower than matched C0 intervals, with directional misses.

At the low-concentration end, C5 improves on C0's poor coverage. Thus the aggregate C5 overcoverage (97.74–98.70%) conceals sharply different conditional behaviour. This is not repaired by applying a single global width multiplier.

The stratification is post-fit and exploratory. It establishes heterogeneity in the observed development data, not a causal effect of κ and not a threshold for excluding datasets.

### 3.2 Production-versus-analytic optimizer differences are usually small on W/B

The later offline P/A functional reconciliation reconstructed the within and raw-between functionals from the stored production and analytic fit parameters:

- M10/R5 calibration: 4,897 paired records; 95th percentile of max(|ΔW|,|ΔB|) = 1.084e-9; maximum 1.537e-5.
- M10/R5 validation: 4,879 paired records; 95th percentile = 1.036e-9; maximum 2.922e-5.
- Only 18 calibration and 14 validation paired records exceeded 1e-6.
- Missing analytic parameters (103/121 records) are missing comparison values, not missing production fit records; production C5 fits were classified interior in the historical runner.

This does not certify a global MLE or remove the frozen unresolved-state gate. It does show that broad additional optimizer-coordinate certification is not the first coverage remedy: for the vast majority of paired M10/R5 records, parameter-coordinate differences do not materially change W/B functionals.

Source: `C10S_F5_B2_PA_FUNCTIONAL_RECONCILIATION_001.md`.

## 4. Why M1-PCT is not a simple fix

M1-PCT's strict refitted bootstrap required every bootstrap refit to be admissible. In M10/R5:
- 45 original fits were admissible and five abstained;
- among 4,500 bootstrap refits, 846 (18.8%) were non-admissible;
- the contract consequently abstained on 43 of the 45 otherwise admissible original datasets;
- only 2/50 intervals were emitted (4%).

Failures included finite numerical bound hits, no admissible primary fit, boundary limits not excluded, and failure of strict local-maximum/Hessian conditions. They are not all interchangeable optimizer warning flags.

Dropping failed refits, taking a complete-case bootstrap, or loosening the contract after seeing these results would change the inferential procedure and can induce selection bias. It is not an admissible repair.

The result therefore rejects the current M1-PCT contract for Tier-A M10/R5. It does not prove that every possible boundary-aware refitted bootstrap must fail.

## 5. What is and is not the next minimum task

### Established
1. C5's M10/R5 emission passes in B2/B3; its coverage does not.
2. C5's aggregate overcoverage masks high-κ undercoverage and low-κ overcoverage behaviour.
3. B=1,000 versus B=4,000 endpoint sensitivity was modest on selected B3 datasets; increasing B is not supported as the remedy.
4. Production/analytic parameter discrepancies usually map to negligible W/B functional differences.
5. Current M1-PCT and G7 emission failures are method-specific and cannot be transferred to C5 as if they were the same defect.

### Not established
1. That omitting α/β estimation uncertainty is the sole cause of C5 miscoverage.
2. That a refitted parametric bootstrap will achieve both coverage and >=95% emission.
3. That profile likelihood for W/B will be computationally feasible and calibrated under the near-binomial weak-identification regime.
4. That any candidate currently meets Tier-A.

### Minimum admissible next step

Do **not** run another simulation yet. Write a short method decision comparing only two statistically meaningful routes:

**Route A — boundary-aware refitted parametric bootstrap.** Determine whether the bootstrap can represent the extended concentration boundary and weak-identification states without conditioning on successful interior fits, dropping replicates, or turning genuine non-identification into numeric intervals. Reuse the existing likelihood and finite-R oracle. The output must specify exactly what happens to every refit state and why the resulting interval has a defensible repeated-sampling interpretation.

**Route B — direct likelihood/profile intervals for W and B.** Consider only if Route A cannot provide a defensible treatment of the observed boundary/weak-identification states. The target is coverage/emission, not complete topology certification for its own sake. The previous profile/Sturm work is not a mandate to continue; no new numerical machinery is authorized by this diagnostic.

Choose neither route based on the exposed B2/B3/G7 results. If neither has a clear defensible interval and emission contract, record **NO_SUPPORTED_F5_M10R5_CANDIDATE** and stop rather than inventing another instrument.

## 6. Anti-drift / explicit non-actions

- No further global-MLE, optimizer-coordinate or Sturm certification work unless a concrete W/B coverage failure is shown to depend on it.
- No relaxation of M1-PCT refit admissibility and no dropping failed bootstrap replicates.
- No complete-case bootstrap.
- No post-hoc concentration cutoff or stratum-specific eligibility.
- No global interval-width multiplier.
- No increase in B as a reflex.
- No replay or rerun of C5, B2/B3, G7 or M1-PCT.
- No reuse of exposed banks as a fresh validation/holdout.
- No changes to the frozen estimands, DGP, acceptance thresholds or historical adjudications.
- No Tier-A confirmatory, Tier-B or causal C10-S execution.

## 7. Next coverage priority after M10/R5

F5 M30/R20 raw-between remains a separate deficit. Its high-κ tail has severe directional undercoverage despite a materially identified profile, so it must not be folded into the M10/R5 weak-identification solution. Its diagnosis should be a separate bounded task after the M10/R5 method decision.

**Controlling question:** Which specific coverage or emission deficit does the proposed action address, and what observable result would show improvement? If this cannot be answered, do not implement or execute it.
