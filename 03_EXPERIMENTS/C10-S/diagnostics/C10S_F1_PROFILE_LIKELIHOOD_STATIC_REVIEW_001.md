# C10-S — Static review of the existing F1 raw-between profile-likelihood candidate

**Record:** C10S-F1-PROFILE-LIKELIHOOD-STATIC-REVIEW-001  
**Date:** 2026-11-19  
**Status:** STATIC REVIEW COMPLETE / CANDIDATE NOT APPROVED FOR EXECUTION OR INFERENCE  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Reviewed source:** `harness/c10s_f1_between_profile_likelihood.py` (method `F1_BETWEEN_PROFILE_LIKELIHOOD_0.2`)  
**Related records:** `C10S_F1_BETWEEN_PROFILE_LIKELIHOOD_IMPLEMENTATION_NOTE_001.md`; `C10S_TIER_A_POST_HOLDOUT_METHOD_DIAGNOSIS_001.md`

## 1. Scope

This is a read-only mathematical/code review. No tests, simulations, workflows, calibration, or scientific execution were run. No source code or frozen protocol was changed.

The candidate is an existing F1-only alternative for the raw between-world variance component. Its LR cutoff is caller-supplied and uncalibrated. This review does not select a cutoff or claim coverage.

## 2. Mathematical structure — static assessment

For the balanced Gaussian random-intercept model, the implementation uses:
- within residual sum of squares (SS_W=M(R-1)MSW), with (df_W=M(R-1));
- variance of world means (S^2_{\bar Y}), with (df_B=M-1);
- (q=\sigma_b^2+\sigma_w^2/R).

The implemented log-likelihood, up to parameter-independent constants, is the sum of the within chi-square contribution and the world-mean chi-square contribution. The code profiles over positive within variance for each fixed nonnegative between variance. The constrained point estimate is \hat\sigma_b^2=max(0,S^2_{\bar Y}-MSW/R).

The parameterization is consistent with the raw between-component target used in the holdout. The candidate does not clamp the raw point estimate as the inferential target; the constrained MLE is used to locate the likelihood maximum, while the confidence set is defined over nonnegative parameter space.

**Static conclusion:** no immediate algebraic contradiction was identified in the core likelihood expression or target parameterization. This is not an independent numerical verification of the implementation.

## 3. Material review findings

### F1-PL-01 — Global nuisance maximum is not certified by the interval inversion path

The production path `f1_profile_between_confidence_set()` evaluates the profile likelihood through `_profile_at_tau()`. That function uses one bounded `minimize_scalar` call over log(within variance), compares the returned point with the two search endpoints, and fails if the selected result is a search endpoint.

The module also contains a separate, more elaborate diagnostic path:
- `f1_score_polynomial_diagnostic()` constructs the cubic numerator of the nuisance score from exact rational representations of the binary input values and attempts to isolate positive stationary roots;
- `f1_profile_nuisance_optimizer_diagnostic()` compares the bounded optimizer with the stationary-root route and a score scan;
- `f1_profile_nuisance_stability_diagnostic()` compares a finite grid-resolution/log-span cross-product.

However, the LR interval inversion does **not** call these diagnostics and does not require a concordant status at each evaluated σ²_between value. The diagnostics are therefore informative but not currently an enforced precondition of the returned confidence set.

**Required before candidate promotion:** either use the isolated stationary candidates to construct/certify the nuisance maximum in the interval path, or make a fail-closed diagnostic gate part of the confidence-set computation. The gate must account for unresolved/tangential roots and search-boundary sensitivity. A finite family of scans is still a numerical check, not a mathematical proof of globality.

### F1-PL-02 — Single-component LR inversion assumes a connected acceptance set

The return type allows a tuple of confidence components, but `f1_profile_between_confidence_set()` currently returns one interval. It brackets a lower endpoint between zero and the constrained MLE (unless zero is included) and a single upper endpoint by geometric expansion.

No explicit theorem or test in the reviewed note establishes that the nuisance-profile LR acceptance set in the between variance is always connected for every admissible sufficient-statistic configuration. The score diagnostics concern nuisance stationary points at fixed between variance; they do not by themselves prove global shape/unimodality of the profiled likelihood as a function of between variance.

**Required before candidate promotion:** establish connectedness for this model/likelihood, or add a robust diagnostic over the between-variance profile that can detect multiple LR-set components and return them separately. Do not infer connectedness from the current test fixture.

### F1-PL-03 — Model-scope guard is weaker than the C1 candidate

The C1 exact-pivotal function requires an explicit `family == "F1"` label. The reviewed profile-likelihood API accepts only `rows` and a variance value; its F1 scope is expressed in module documentation/constants, not enforced by a family argument. The common engine does not currently dispatch this profile interval, so this is not an active holdout contamination.

**Required before integration:** enforce the F1 balanced Gaussian random-intercept scope at the dispatch/adapter boundary, with an explicit family/design contract. The profile candidate must not be callable as an F5 or generic nested M/R interval by accidental reuse.

### F1-PL-04 — Boundary and scale limitations are explicit but remain outside the demonstrated domain

The implementation explicitly abstains when within sum of squares is zero, and it checks finite statistics, positive scale, optimizer search-boundary hits, endpoint bracketing and representability. This is appropriate fail-closed behaviour for the currently declared unresolved boundary.

The existing tests cover scale equivariance, zero-between behaviour, invalid cutoff, one fixed interval inversion example, score-polynomial construction and selected near-degenerate numerical cases. They do not constitute coverage calibration and do not yet establish robustness across the six F1 holdout cells, adversarial near-zero within sums, profile topology changes, or all root-multiplicity configurations.

### F1-PL-05 — LR cutoff remains a separate inferential calibration problem

The function correctly requires a caller-supplied positive cutoff and embeds no default. The unit tests use a familiar numerical cutoff to check root inversion; that test value is not a calibrated acceptance rule for this composite/boundary variance-component problem.

A future cutoff must be prospectively calibrated under the exact declared F1 model and boundary regime, with a development/calibration namespace distinct from the future confirmatory holdout. No cutoff should be selected by inspecting the already unblinded Tier A holdout.

## 4. Reconciliation with the completed Tier A evidence

The completed holdout confirms that C1's raw-between interval is too conservative for the v1.0 acceptance band (96.7–99.4% empirical coverage across the six F1 cells). The earlier Tier A investigation had already shown a similar conservative joint-pivot pattern (97.0–99.6%).

This supports investigating a more efficient F1 interval. It does **not** establish that the profile-likelihood candidate will solve the overcoverage: its coverage, interval width, boundary behaviour, LR cutoff and numerical reliability remain untested.

The F1 exact within interval remains a separate bounded component result and must not be altered to address the raw-between problem.

## 5. Decision and minimum next work

**Disposition: EXISTING CANDIDATE RETAINED FOR DEVELOPMENT; NOT READY FOR NUMERICAL CALIBRATION.**

Before any numerical execution, the development work should:
1. close F1-PL-01 by integrating or enforcing nuisance-root/global-maximum diagnostics in the interval inversion path;
2. resolve F1-PL-02 by proving connectedness under the stated model or implementing detection/reporting of multiple LR-set components;
3. add an explicit F1 model-scope guard at the callable integration boundary;
4. add deterministic adversarial contracts for the six frozen F1 designs, low-between/high-between regimes, near-zero within sums, multiple/tangential nuisance roots, scale extremes, boundary inclusion, and upper/lower LR root bracketing;
5. define an independent score/likelihood oracle and verify the profile endpoints against it;
6. specify and calibrate an LR cutoff prospectively on a development namespace, with a separate fresh holdout protocol and authorization.

Do not add a default cutoff, change C1, alter v1.0, or run numerical calibration as part of this static review.

## 6. Non-claims

This review establishes no coverage result, no candidate superiority, no general variance-component method, no F5 applicability, no real-world M/R validity, and no C10 causal or Value claim.
