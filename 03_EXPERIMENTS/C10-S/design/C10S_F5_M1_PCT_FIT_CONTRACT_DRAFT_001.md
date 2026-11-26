# C10-S — F5 M1-PCT fit contract draft 001

**Date:** 2026-11-26  
**Status:** D1 IMPLEMENTATION CANDIDATE — NOT FROZEN / NO DEVELOPMENT BANK RUN  
**Branch:** `research/c10s-instrumental-autonomous-workpackage-20261126`  
**Method ID:** `F5_M1_FUNCTIONAL_REFIT_PARAMETRIC_BOOTSTRAP_PCT_1.0`  
**Fit contract ID:** `F5_M1_ANALYTIC_LBFGSB_BEST_SUCCESSFUL_START_1.0`  
**Implementation:** `harness/c10s_f5_functional_refit_bootstrap.py`  
**Deterministic tests:** `harness/test_c10s_f5_functional_refit_bootstrap.py`

## 1. Decision scope

This draft defines the smallest executable M1-PCT candidate: a parametric bootstrap of the fitted beta-binomial population functionals (W) and (B), with a deterministic analytic-gradient fit repeated in every bootstrap replicate.

It does not amend frozen C10-S v1.0, change C5, select or validate an F5 interval method, or authorize Tier-A/Tier-B. M1-BASIC is deferred. M2 remains a contingency only if M1 cannot handle the frozen cells or fails the inherited component gates.

## 2. Estimator definition

For counts (x_1,\ldots,x_Min\{0,\ldots,R\}), the primary estimator is the best successful finite fit returned by the existing three-start analytic-gradient L-BFGS-B routine in ((\eta,\xi)=(\operatorname{logit}\mu,\log\kappa)) coordinates.

Fixed numerical contract inherited from `audit_beta_binomial_count_fit`:
- concentration starts: ((2.0,0.5,20.0));
- mean-logit bounds: ([-18,18]);
- log-concentration bounds: ([-12,18]);
- maximum iterations: 4,000;
- `ftol=1e-12`, `gtol=1e-8`;
- select the highest finite log-likelihood among successful starts.

The resulting estimator is an **algorithmically selected interior likelihood fit**. It is not described as a certified global MLE. The bootstrap repeats the same deterministic fit algorithm; its finite-sample behaviour is evaluated prospectively. No globality claim is made from multi-start optimization alone.

## 3. Primary fit-state contract

A fit is assigned `PRIMARY_ANALYTIC_INTERIOR_FIT` only if all of the following hold:

1. At least one successful finite analytic-gradient L-BFGS-B start exists and the selected mean-logit, log-concentration, log-likelihood and score norm are finite.
2. The selected solution is not within (2\times10^{-4}) of any finite numerical parameter bound.
3. The observed Hessian is finite and negative definite at the selected point.
4. The selected interior log-likelihood exceeds the finite binomial limit. If a finite two-point-mixture limit is available, it must also exceed that limit.
5. The boundary comparisons exceed a scale-aware floating-point guard of 64 binary64 machine epsilons times the maximum absolute log-likelihood scale. This is a numerical tie guard, not a statistical acceptance threshold.

Otherwise the fit receives a typed state, including `NO_ADMISSIBLE_PRIMARY_FIT`, `FINITE_NUMERICAL_BOUND_HIT`, `PRIMARY_FIT_NOT_STRICT_LOCAL_MAXIMUM`, or `BOUNDARY_LIMIT_NOT_EXCLUDED`. A typed non-interior state is not converted into a finite parameter estimate.

The exact (kappa\to\infty) and (kappa\to0) limits are evaluated by the existing boundary-likelihood diagnostic. This M1 draft does not accept boundary estimates as fitted functional values; if a boundary is tied with or dominates the selected interior fit, the fit abstains. A later extension would require its own versioned boundary-functional contract.

## 4. Secondary optimizer diagnostics

The existing analytic audit also runs a BFGS check in ((\log\alpha,\log\beta)) coordinates initialized from the selected analytic-gradient fit. Its success flag, message, likelihood, terminal parameters and score norm are retained for every fit.

**Role:** secondary numerical diagnostic only; it is not the estimator and is not a global search. Its status does not replace the primary fit-state contract. The primary estimator is fully defined by the fixed three-start analytic-gradient L-BFGS-B procedure. This separation is explicit so that an independent local BFGS termination flag is not silently treated as a second estimator or globality certificate.

This is a D1 methodological choice, not a claim that the secondary check is always concordant. Its frequency and functional implications must be reported in the development pilot. If the primary optimizer itself has no admissible fit, or fails the interior/Hessian/boundary checks above, the fit is unresolved and the dataset abstains.

## 5. M1-PCT interval construction

For an admissible original fit ((\hat\mu,\hat\kappa)), compute:

[
\hat W=\hat\mu(1-\hat\mu)\frac{\hat\kappa}{\hat\kappa+1},
\qquad
\hat B=\hat\mu(1-\hat\mu)\frac{1}{\hat\kappa+1}.
]

For each of (B_{boot}) bootstrap replicates:
1. Draw (p_m^*\stackrel{iid}{\sim}\operatorname{Beta}(\hat\alpha,\hat\beta)), (m=1,\ldots,M).
2. Draw (X_m^*\mid p_m^*\sim\operatorname{Binomial}(R,p_m^*)).
3. Refit with the exact same analytic-gradient fit contract.
4. Retain the complete replicate fit state, all starts, the secondary BFGS diagnostic, seed, and a digest of the simulated count vector.
5. If admissible, retain (hat W_m^*,\hat B_m^*).

The M1-PCT intervals are the empirical ((\alpha/2,1-\alpha/2)) quantiles of the replicate (hat W_m^*) and (hat B_m^*), using the recorded NumPy linear quantile convention. No clipping, truncation, centering correction or raw-sample-statistic substitution is allowed.

**Fail-closed replicate rule:** if any requested replicate does not produce an admissible primary fit, the complete dataset abstains. All requested replicate states remain in the output; no replicate is silently dropped, redrawn or replaced. No complete-case bootstrap distribution is formed.

## 6. Randomness and provenance

- Each dataset receives a fresh development-only dataset seed from a new namespace, disjoint from all historical Tier-A/B2/B3 and G7 namespaces.
- Each bootstrap replicate seed is derived deterministically from the dataset's bootstrap seed, fit-contract ID and replicate index using SHA-256; PCG64 is used for Beta/Binomial generation.
- The pilot must run a seed-collision audit against the persisted historical schedules before generating data.
- The exact requested bootstrap count, valid count, failed count by typed state, all replicate records, raw input digest and method/fit-contract IDs are persisted.

No bootstrap replicate count is frozen here. It must be selected using endpoint Monte Carlo precision analysis, not by reflexively increasing (B).

## 7. Known limitations

1. The selected multi-start optimizer is not a global MLE certificate. The method is an algorithmic estimator whose coverage must be demonstrated under the frozen beta22 DGP.
2. Boundary fits are not yet represented as valid W/B point estimates. Boundary-dominated or numerically tied datasets abstain.
3. The secondary BFGS diagnostic is local and initialized from the primary fit; it is not an independent global search.
4. No M1-PCT bootstrap bank has been run. No coverage, emission, width, or MCSE claim is available.
5. The method's estimator differs from frozen C5 raw sample statistics. Any comparison must describe the full estimator/interval package, not call it an interval-only change.

## 8. Next validation step

Run a bounded implementation pilot on a fresh development-only seed namespace, initially limited to a small number of datasets per frozen cell and a fixed modest (B_{boot}). Its purpose is only to test fit emission, typed failure behaviour, reproducibility, endpoint computation and runtime. It is not a coverage acceptance bank and cannot establish Tier-A readiness.

If the pilot is stable, define a separate prospective development/validation design with sample size and bootstrap (B) justified by MCSE and resource evidence. Apply the unchanged frozen component gates. If M1-PCT fails, do not relax thresholds; consider the already drafted M2 profile route or report the limitation.

No Tier-A/Tier-B execution is requested or authorized by this draft.
