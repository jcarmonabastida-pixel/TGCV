# C10-S — F5 MCSE profile implementation note

Status: PROFILE EVALUATOR IMPLEMENTED / ROOT INVERSION NOT IMPLEMENTED /
NOT EXECUTED / NOT CALIBRATED
Branch: `research/c10s-nested-mr-calibration-design-20261119`
Scope: beta-binomial world-probability F5 only.

## Implemented

New module:
`03_EXPERIMENTS/C10-S/harness/c10s_f5_beta_binomial_mcse_profile.py`

It evaluates the scalar MCSE profile log-likelihood using the full vector of
world-cluster Bernoulli counts. It parameterizes the beta-binomial through
mean μ and concentration κ, derives both μ branches from the target
constraint, and maximizes each branch separately over concentration.

The evaluator includes:
- exact finite-count beta-binomial log likelihood using log-beta/log-gamma;
- both μ+ and μ- profile branches, retaining separate log likelihoods;
- analytic κ→0 endpoint likelihood (two-point count support);
- analytic κ→∞ endpoint likelihood (binomial limit);
- explicit target-space upper bound (gleq1/(2sqrt{M^*}));
- finite feasible concentration cap when the target constraint ceases to be
  feasible at large κ;
- typed failures and diagnostics for unsupported numerical cases.

The shared comparative engine now records a diagnostic evaluation at the
observed nonnegative point MCSE when one exists. This does not create a
confidence interval and does not replace C5's current typed abstention.

## Tests defined, not executed

New test module:
`03_EXPERIMENTS/C10-S/harness/test_c10s_f5_beta_binomial_mcse_profile.py`

Cases cover finite interior evaluation, retention of both branches, permutation
invariance, the maximum-target concentration boundary, target values outside
the parameter space, all-zero/zero-target boundary likelihood, and rejection
of non-Bernoulli input.

No tests have been executed. These are test definitions only.

## Important limitations

- Finite-κ maximization uses a deterministic log-concentration scan followed
  by local bounded optimization around detected maxima. It is not yet a
  certified global optimizer.
- The profile evaluator is implemented; LR confidence-set inversion,
  connected-component/hull reporting, and root refinement are not yet
  implemented.
- The κ limits are evaluated analytically, but the finite numerical search
  still requires independent convergence and boundary diagnostics.
- No LR cutoff is selected. No Wilks cutoff is assumed.
- No calibration, holdout, simulation, or scientific C10 execution has run.

## Next required work

1. Add independent score/likelihood checks and adversarial tests for asymmetric
   beta parameters and all boundary classes.
2. Implement LR confidence-set scanning with explicit connected components,
   then refine every endpoint by bracketed roots.
3. Preserve the full confidence-set components and hull; abstain on unresolved
   optimizer or root failures.
4. Calibrate the cutoff prospectively on a calibration roster independent of
   the holdout roster, only after separate authorization.

This artifact changes no causal claim, estimand, frozen v002 baseline, main
branch, RMA, Evidence→Claim Matrix, or scientific execution authorization.
