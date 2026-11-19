# C10-S — Static review of the F5 fitted beta-binomial component-interval candidate

**Record:** C10S-F5-FITTED-BETA-BINOMIAL-STATIC-REVIEW-001  
**Date:** 2026-11-19  
**Status:** STATIC REVIEW COMPLETE / CANDIDATE NOT VALIDATED / NO EXECUTION AUTHORIZATION  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Reviewed source:** `harness/c10s_fitted_beta_binomial_bootstrap.py`  
**Related records:** `C10S_NESTED_MR_COMPARATIVE_ENGINE_CONTRACT_001.md`; `C10S_NESTED_MR_TIER_A_CALIBRATION_INVESTIGATION_001.md`; `C10S_F5_MCSE_PROFILE_LIKELIHOOD_DESIGN_001.md`; `C10S_TIER_A_POST_HOLDOUT_METHOD_DIAGNOSIS_001.md`

## 1. Scope

Read-only mathematical/code review of the existing F5 candidate for within and untruncated raw-between component intervals. No tests, simulations, optimizer benchmarks, calibration, workflows or scientific execution were run. No source code or frozen protocol was changed.

The separate F5 MCSE profile design is not the subject of this review: it concerns the MCSE functional, not the current C5 within/raw-between coverage failures.

## 2. Model and implementation — static assessment

The implementation fits a beta-binomial model to the M integer world-cluster counts:
`X_m ~ BetaBinomial(R, alpha, beta)`, using mean-logit and log-concentration coordinates. It then generates parametric bootstrap worlds from the fitted beta distribution and binomial conditional sampling, recomputes the common nested M/R estimators, and takes percentile limits for within and raw-between.

The likelihood includes the binomial coefficient and beta-function ratio. The bootstrap generator uses PCG64 with an explicit seed. Raw between estimates are not truncated. The C5 MCSE interval remains a typed abstention rather than conditioning on positive/projectable bootstrap draws.

The independent `c10s_beta_binomial_variance_oracles.py` already supplies the exact finite-R beta-binomial count PMF and finite-M moments/covariance of the within and raw-between estimators. It is a useful existing oracle and should be reused; no new oracle is needed before the candidate is audited against it.

**Static conclusion:** the broad model/likelihood and parametric-bootstrap construction are coherent with the declared F5 fixture. This review does not establish numerical optimizer reliability or confidence-interval coverage.

## 3. Material review findings

### F5-BB-01 — Finite multi-start optimizer does not establish global MLE or distinguish weak identification

The fit uses three fixed initial values for concentration (2, 0.5 and 20), L-BFGS-B, finite bounds on logit mean and log concentration, and accepts the lowest objective among starts whose optimizer reports success. It does not calculate an independent analytic score/Hessian check, compare the accepted fit with an independent optimizer/parameterization, or characterize a flat likelihood ridge.

The holdout contains 15 M10/R5 optimizer non-convergences and one concentration-at-upper-bound abstention. Among the 984 M10/R5 interior fits, the fitted alpha and beta distributions have very long upper tails (90th percentiles about 619 and 572; maxima about 759,203 and 963,975). By contrast, the M30/R20 fitted values are much more concentrated (90th percentiles about 3.39 for both parameters).

**Established:** small-M/R fits sometimes fail or produce extremely high fitted concentration; this is a real numerical/identifiability diagnostic that must be retained.

**Not established:** whether those high-concentration fits are wrong local optima, genuine near-binomial likelihood maxima, or weakly identified estimates caused by the observed finite sample. Do not label them optimizer bugs without likelihood-surface and independent-score evidence.

### F5-BB-02 — Finite parameter bounds need a statistical boundary interpretation

The optimizer works over finite logit/log-concentration bounds. It flags a fit only when the selected parameter is within a fixed tolerance of a bound. A large but interior concentration can still approximate the binomial limit and be weakly identified without triggering the boundary abstention.

The F5 MCSE profile design already recognizes that κ→∞ (binomial limit) and κ→0 (two-point mixing limit) are meaningful extended parameter-space boundaries, and that a numerical cap is not itself a statistical boundary solution. That design is for MCSE, but its boundary lesson also applies to interpreting C5's fitted component intervals.

**Required:** report profile/likelihood curvature and distance-to-bound diagnostics; distinguish a finite interior estimate, a practically boundary-sensitive estimate, and an optimizer failure. A finite upper cap must not be treated as evidence that the likelihood is well identified.

### F5-BB-03 — The current deterministic tests do not cover the holdout failure modes

The existing unit tests cover one interior overdispersed fit, deterministic bootstrap repeatability, all-zero/all-one abstention, non-Bernoulli input, equal-count boundary rejection and basic invalid supports. They do not test:
- M=10 versus M=30 concentration identifiability under the exact Beta(2,2) generator;
- near-binomial/high-concentration and near-two-point/low-concentration likelihood limits;
- multi-start disagreement, flat likelihood ridges or a false-success local optimum;
- gradient/score agreement with an independent derivative;
- coverage, interval width, point bias or tail misses;
- finite-B endpoint variability;
- raw-between boundary behaviour across the two frozen M/R designs.

These omissions are material because the holdout exposes both coverage over-shoot and undercoverage, plus small-design optimizer abstentions.

### F5-BB-04 — The fitted percentile intervals remain uncalibrated even when the fit converges

The holdout shows:
- M10/R5: 98.37% within and 98.88% raw-between conditional coverage, 98.4% emission;
- M30/R20: 93.5% within and 92.7% raw-between conditional coverage, 100% emission.

Thus optimizer non-emission alone cannot explain the method failure: the larger M/R cell emits every interval and still undercovers. Conversely, the small cell overcovers among emitted intervals. This is a finite-sample calibration problem across the declared designs, not merely an availability problem.

The implementation's bootstrap percentile method is a candidate procedure, not a coverage guarantee. B=1,000 is frozen in v1.0; endpoint Monte Carlo variability remains a declared protocol limitation and cannot be tuned after viewing this holdout.

### F5-BB-05 — MCSE abstention is correctly separated and must stay separate

The implementation retains projectable MCSE draw counts as diagnostics but does not emit an MCSE percentile interval from the positive-projectable subset. This respects the frozen no-positive-only-conditioning rule. The independent MCSE profile design is not yet implemented or calibrated.

Do not relax this abstention to improve the candidate's overall emission statistics, and do not confuse its MCSE status with within/raw-between interval emission.

## 4. Minimum development audit before proposing a replacement

Reuse the existing code, oracle and holdout diagnostics to perform the following static/design work before any authorized numerical development run:

1. Derive and independently implement the beta-binomial score in mean/concentration coordinates; compare analytic score and Hessian behaviour with independent finite differences over interior and boundary-adjacent fixtures.
2. Compare the three-start L-BFGS-B fit with a broader deterministic start design and an independent parameterization/optimizer. Record all starts, convergence flags, objective values and gradient norms; never select by optimizer success alone.
3. Characterize the likelihood as κ approaches both extended boundaries. Distinguish true weak identification from finite-bound truncation and numerical failure.
4. Reconcile fitted alpha/beta and their implied variance components against the exact finite-R oracle and independent count likelihood on fixed datasets.
5. Assess the percentile interval construction and finite-B endpoint noise as separate issues. Do not increase B or alter v1.0 after holdout unblinding.
6. If an alternative F5 interval is proposed, define its target, nuisance treatment, boundary behaviour, abstention policy and independent validation oracle before simulation.

## 5. Decision

**Disposition: EXISTING C5 RETAINED AS AN UNVALIDATED DEVELOPMENT CANDIDATE; NO METHOD CHANGE APPROVED.**

The current holdout fails C5 in both components and both M/R designs. The immediate unresolved question is whether the M10/R5 fit instability is an optimizer issue or a weak-identification/boundary feature, while M30/R20 demonstrates that successful fitting alone does not deliver calibrated percentile intervals.

The next valid step is a deterministic mathematical/optimizer audit and a prospectively specified development comparison using the existing beta-binomial oracle. Any numerical development/calibration execution requires a separate, explicit authorization. A new confirmatory holdout must use fresh independent datasets, a new seed namespace and a new protocol; the unblinded v1.0 holdout cannot be reused for acceptance.

## 6. Non-claims

This review establishes no F5 interval coverage guarantee, no general beta-binomial estimator, no transfer to non-beta-binomial C10-S contributions, no C10 causal effect, no ΔT_acc → Value result, and no TGCV Core or claim-level change.
