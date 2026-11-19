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


## Implementation increment — raw nuisance-profiled curvature

A new optional field, `profile_log_concentration_curvature`, is now calculated from the observed Hessian at the selected interior fit using the nuisance-adjusted Schur complement:

`H_xixi - H_etaxi^2 / H_etaeta`

where `eta = mean_logit` and `xi = log_concentration`. The field is left null when the nuisance-coordinate curvature is exactly zero or the resulting quantity is non-finite. No arbitrary numerical threshold is introduced.

This is a local, parameterization-specific observed profile-curvature diagnostic. It is not a normalized information measure, does not define weak identification, does not alter optimizer status, and does not affect C5 fit/interval selection. The existing dataclass-to-JSON serialization path carries the field into the per-dataset audit record.

Deterministic tests were added to:
- verify the field against the Hessian Schur-complement identity;
- verify that the per-dataset strict-JSON audit retains a finite value.

Implementation commits:
- diagnostic: `9d8f96cfe0100d30f017456b77b0da9ab6fe4d10`
- diagnostic unit test: `18f9293632348266a7dea872d587a2ff9c02a9bc`
- per-dataset serialization assertion: `09af6710a8954450ec85dbfae02c1a156432a73d`

Static workflow for the intermediate diagnostic and unit-test commits was triggered; the final serialization-test commit is the current validation target. **No passing result is claimed until its exact-commit run completes and logs are inspected.**
