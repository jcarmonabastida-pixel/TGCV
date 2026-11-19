# C10-S — Tier A post-holdout method diagnosis and development routing

**Record:** C10S-TIER-A-POST-HOLDOUT-METHOD-DIAGNOSIS-001  
**Date:** 2026-11-19  
**Status:** RESEARCH DIAGNOSIS / HYPOTHESES ONLY / NO METHOD CHANGE / NO EXECUTION AUTHORIZATION  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Input audit:** `C10S_NESTED_MR_COMPARATIVE_HOLDOUT_AUDIT_001.md`  
**Frozen comparison protocol:** C10S nested M/R comparative holdout v1.0

## 1. Purpose and boundary

This record translates the completed Tier A adjudication into a bounded development plan. It does not amend protocol v1.0, change C0/C1/C5, select a winner, authorize another numerical run, authorize Tier B, or authorize C10 causal scientific execution.

The primary/replay evidence from run 44572812481 remains immutable. The 8,000 holdout datasets are now unblinded and must be treated as development evidence for any subsequent method refinement; they cannot be reused as an independent confirmatory holdout after method selection.

## 2. Historical work recovered — reuse before recreation

The following prior work already exists and must be reused:

1. `C10S_NESTED_MR_TIER_A_CALIBRATION_INVESTIGATION_001.md`: documents the original v002 Tier A percentile-bootstrap undercoverage; an exact Gaussian within pivot; and the conservative joint-pivot raw-between benchmark, with coverage around 97.0–99.6% in the original development artifact. It explicitly recommends an efficient F1 between interval rather than a global width multiplier.
2. `C10S_F1_EXACT_PIVOTAL_CANDIDATE_SPEC_001.md` and `c10s_f1_exact_pivotal_candidate.py`: specify and implement C1's exact within pivot and conservative joint-pivot raw-between projection. Its scope is balanced Gaussian random-intercept F1 only.
3. `C10S_F1_BETWEEN_PROFILE_LIKELIHOOD_IMPLEMENTATION_NOTE_001.md` and `c10s_f1_between_profile_likelihood.py`: an existing F1 profile-likelihood alternative with caller-supplied LR cutoff, numerical inversion and explicit failure modes. It remains unexecuted and uncalibrated; its cutoff is not selected. This is the first existing alternative to review rather than creating another F1 interval implementation.
4. `C10S_F5_MCSE_PROFILE_IMPLEMENTATION_NOTE_001.md` and `c10s_f5_beta_binomial_mcse_profile.py`: this is an F5 MCSE-functional profile evaluator only. It does **not** solve the current F5 within/raw-between coverage failures, and its LR cutoff/topology are not calibrated.
5. `C10S_COMPARATIVE_CALIBRATION_READINESS_AUDIT_001.md` and `C10S_NESTED_MR_COMPARATIVE_ENGINE_CONTRACT_001.md`: establish the matched C0/C1/C5 comparison, truth pairing, denominators, Wilson reporting, C5 MCSE fail-closed abstention and no-pooling rules.

No new estimator family is needed before these existing candidates and diagnostics are reconciled against the holdout evidence.

## 3. Findings established by the independent holdout audit

### 3.1 F1 within

C1 within passes all six F1 cells (coverage 94.9–95.5%; each Wilson interval contains 95%; 100% interval emission). This reproduces the earlier exact-pivot benchmark and is bounded evidence for the declared balanced Gaussian random-intercept fixture family.

C0 within passes only the three M30/R20 cells and fails the three M10/R5 cells. C0 is the frozen baseline, not a validated full-family procedure.

### 3.2 F1 raw between

No C0 or C1 raw-between cell passes. C1 coverage is 96.7–99.4%, with Wilson intervals above 95% in all six cells. This is consistent with the earlier development investigation, which found the same joint-pivot construction deliberately conservative (97.0–99.6%).

**Established:** the current C1 raw-between projection overcovers relative to the protocol's [93%,97%] band and its width can be large. It emits all intervals and preserves negative raw estimates/endpoints.

**Not established:** that the formula is incorrect, that the Gaussian DGP/oracle is wrong, or that a specific alternative will achieve the acceptance criteria. The joint rectangle projection is intentionally conservative; coverage above the frozen upper bound is a method-performance failure for this protocol, not by itself a mathematical implementation defect.

### 3.3 F5 within and raw between

C5 fails both components at both M/R designs, but in different directions:
- M10/R5: 98.37% within and 98.88% raw-between conditional coverage; emission 98.4%.
- M30/R20: 93.5% within and 92.7% raw-between; emission 100%.

At M10/R5, the 16 non-emissions comprise 15 MLE non-convergences and one upper-bound concentration fit. At M30/R20, all 1,000 datasets emit intervals. The M10/R5 fitted alpha/beta values show a very long upper tail (empirical 90th percentiles approximately 619 and 572; maxima approximately 759,203 and 963,975), whereas the M30/R20 fit values are much more concentrated (90th percentiles approximately 3.39 for both parameters). These are diagnostics from this unblinded holdout, not proof of the cause of the coverage pattern.

**Established:** the current fitted beta-binomial percentile procedure is not calibrated across the two frozen designs; optimizer/boundary non-emission is present at M10/R5 but does not alone explain the conditional coverage failures.

**Not established:** whether the dominant cause is finite-M estimation of concentration, optimizer instability, percentile-bootstrap approximation, finite B endpoint noise, or a combination. Do not attribute causality without targeted development experiments.

## 4. Development workstream F1 — efficient raw-between interval

Reuse the existing profile-likelihood candidate and its implementation note. The immediate review should establish:

1. whether the profile likelihood is parameterized against the exact raw-between estimand σ²_between = τ² - σ²_within/R and retains the zero boundary correctly;
2. whether its nuisance optimization, bracket expansion and root inversion are stable over the six already specified F1 design cells and adversarial near-boundary sufficient statistics;
3. whether an independent score-equation/likelihood calculation agrees with the implemented profile objective;
4. how LR cutoff calibration would be performed prospectively on a separate development/calibration namespace, with no reuse of the holdout for final acceptance;
5. coverage, Wilson uncertainty, width, lower/upper misses, boundary behaviour and failure/emission rate compared with C0 and C1.

The profile LR cutoff remains caller-supplied and unselected. Do not insert a default Wilks cutoff or declare the interval validated from pointwise likelihood tests. The existing C1 method remains unchanged as a conservative benchmark.

## 5. Development workstream F5 — fitted beta-binomial component intervals

The next review should focus on the actual F5 within/raw-between outputs, not the separate MCSE profile work:

1. inspect the beta-binomial likelihood surface and identifiability of mean/concentration for M=10 versus M=30, especially the near-binomial/high-concentration region;
2. audit multi-start optimizer convergence, boundary classification, parameter bounds and sensitivity to starting values; distinguish true boundary/weak identification from numerical failure;
3. compare fitted alpha/beta with the independent fixture truth and the independent finite-R beta-binomial oracle, retaining the full distribution rather than only medians;
4. inspect parametric-bootstrap bias and endpoint Monte Carlo variability at B=1,000; any B-sensitivity must be a separate development exercise and cannot change v1.0;
5. compare alternative F5 component intervals only after specifying their estimand, boundary treatment, typed abstention and independent validation oracle.

The existing F5 MCSE profile evaluator is out of scope for these component failures. It must not be represented as a fix for C5 within/raw-between coverage.

## 6. Integrated next-operation sequence

1. Static mathematical/code review of the existing F1 profile-likelihood candidate; do not execute it yet.
2. Static likelihood/optimizer audit of the existing F5 fitted candidate and its independent oracle.
3. Produce one integrated candidate comparison design with explicit development versus fresh-confirmatory data separation, metrics, boundary rules and method-specific failure semantics.
4. Only after the design is frozen, seek a separately scoped authorization for any numerical development/calibration execution.
5. Select and freeze candidate procedures prospectively; then specify a new independent holdout protocol, fresh seed namespace and new one-use authorization.
6. Keep Tier B and C10 causal scientific execution separately gated.

## 7. Stop conditions and non-claims

Stop if a proposed change alters the raw-between estimand, truncates negative estimates, conditions on positive draws, imports oracle truth into candidate fitting, pools F1/F5, changes the frozen v1.0 result, or reuses the unblinded holdout as confirmatory evidence.

This diagnosis establishes no general-purpose variance-component estimator, no real-system M/R validity, no C10 causal effect, no ΔT_acc → Value result, and no TGCV Core or claim-level change.

**Recommended immediate next task:** static review of the existing F1 profile-likelihood candidate against the observed C1 overcoverage, followed by the F5 MLE identifiability audit. No code change or numerical execution is authorized by this record.
