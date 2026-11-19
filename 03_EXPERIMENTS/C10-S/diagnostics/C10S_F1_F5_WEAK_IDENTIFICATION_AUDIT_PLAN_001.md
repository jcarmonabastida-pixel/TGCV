# C10-S — F5 weak-identification audit plan 001

Date: 2026-11-19  
Branch: `research/c10s-f1-integrated-correction-20261119`

## Verified baseline

Static workflow run `44588467741` checked out commit `72f119b4be3b696fee95e5ad92c07376e5ba10c2` and completed successfully:
- hash-locked dependencies: PASS;
- compile: PASS;
- deterministic suite: 122 tests passed;
- `test_two_point_limit_is_the_low_concentration_limit`: PASS.

This validates deterministic likelihood-limit checks only.

## Weak-identification gap

The current `BetaBinomialOptimizerAudit` reports observed Hessian eigenvalues, score norm, multi-start outcomes, independent-optimizer agreement, and distances to optimizer bounds. Its status vocabulary adjudicates optimizer agreement, not statistical identification strength.

A small Hessian eigenvalue alone must not be equated with weak identification without a parameterization-aware scale and a defined diagnostic rule. Likewise, optimizer convergence, small score norm, or agreement in likelihood do not establish that concentration is identified.

## Required deterministic work before any classification rule

1. Construct data-level fixtures with analytically understood limiting behaviour:
   - endpoint-only counts approaching the `kappa -> 0` two-point mixture;
   - low-dispersion counts approaching the `kappa -> infinity` binomial limit;
   - interior-count fixtures for which the two-point boundary likelihood is `-inf`.
2. For each fixture retain:
   - observed log-likelihood and both boundary likelihoods;
   - score norm and full observed Hessian;
   - eigenvalues and eigenvectors in declared `(mean_logit, log_concentration)` coordinates;
   - every optimizer start, termination message, and boundary distance;
   - independent shape-parameter optimizer comparison.
3. Separate numerical optimizer convergence, likelihood preference over each boundary limit, and local information/curvature in concentration.
4. Do not create a binary weak-identification status until a scale-aware criterion and its operating characteristics are justified. Preserve raw diagnostics and permit indeterminate outcomes.
5. Add deterministic tests for invariance/known limits and diagnostic-schema completeness. Do not run Monte Carlo calibration or bootstrap simulations under this task.

## Guardrails

- No changes to C5 candidate selection, interval construction, or frozen scientific thresholds.
- No changes to frozen development/calibration specification v1.0.
- No calibration, resource preflight, holdout, or scientific C10 execution.
- Any future weak-identification threshold requires an explicit scientific rationale and must remain distinct from optimizer convergence status.

## Current disposition

The low-concentration two-point-limit and high-concentration binomial-limit likelihood tests exist. The remaining implementation gap is not to duplicate those identities, but to expose and verify a nuisance-profiled local concentration-curvature diagnostic while preserving raw optimizer and boundary comparisons. This plan is a research-branch design record only.
