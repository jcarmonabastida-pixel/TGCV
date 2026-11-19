# C10-S — F5 MCSE profile implementation note

Status: PROFILE EVALUATOR AND NUMERICAL LR-SET INVERSION IMPLEMENTED /
NOT EXECUTED / NOT CALIBRATED
Branch: `research/c10s-nested-mr-calibration-design-20261119`
Scope: beta-binomial world-probability F5 only.

## Implemented

Module:
`03_EXPERIMENTS/C10-S/harness/c10s_f5_beta_binomial_mcse_profile.py`

The scalar MCSE profile evaluator uses the full vector of world-cluster
Bernoulli counts. It parameterizes the beta-binomial through mean μ and
concentration κ, derives both μ branches from the target constraint, and
maximizes each branch separately over concentration.

The evaluator includes:
- finite-count beta-binomial log likelihood using log-beta/log-gamma;
- separate μ+ and μ- profile branches;
- analytic κ→0 endpoint likelihood (two-point count support);
- analytic κ→∞ endpoint likelihood (binomial limit);
- admissible target-space upper bound (g\leq1/(2\sqrt{M^*}));
- finite feasible concentration cap when the target constraint ceases to be
  feasible at large κ;
- typed failures and diagnostics for unsupported numerical cases.

## Numerical LR-set inversion added

Function:
`f5_beta_binomial_mcse_profile_confidence_set(...)`

It:
1. scans the full admissible MCSE interval on a deterministic grid;
2. refines grid-detected local maxima to estimate the unrestricted profile
   maximum;
3. forms the caller-specified LR acceptance set;
4. retains each grid-detected connected component separately;
5. refines each detected finite endpoint using Brent root finding;
6. reports the interval hull, grid resolution, and a status distinguishing
   connected from disconnected detected sets.

The cutoff is mandatory and caller-supplied. No default, Wilks approximation,
or calibration choice is embedded in the code.

**Important qualification:** this is grid-detected topology, not a certified
proof that every connected component or narrow island has been found. It is
not yet acceptable as a final inferential interval without resolution
sensitivity, adversarial multimodality tests, and independent likelihood
checks. Root refinement cannot repair a component missed by the scan.

## Comparative engine

The common F1/F5 engine records a profile diagnostic at the observed
nonnegative point MCSE when available. It does not emit the new LR set or
replace C5's existing typed abstention. This separation is intentional:
there is no selected or calibrated cutoff.

## Tests defined, not executed

The test module now includes finite profile evaluation, retention of both
branches, permutation invariance, an independent asymmetric beta-binomial
likelihood lower-bound check, analytic beta-binomial scores compared with
finite differences of an independent math.lgamma likelihood, maximum-target
and zero-target boundaries, infeasible targets, invalid input, profile LR
inversion with component/hull consistency, invalid-cutoff rejection,
non-finite root refinement, explicit grid-resolution reporting, and the
nested-grid convergence diagnostic interface.

No tests have been executed. These are test definitions only.

## Remaining limitations

- Finite-κ maximization uses a deterministic log-concentration scan followed
  by local bounded optimization; it is not a certified global optimizer.
- Both MCSE and concentration grid resolutions are configurable and reported.
  A nested-grid convergence diagnostic now compares component counts, profile
  maxima, and LR-set endpoints. Stability across two grids is not proof that
  both grids did not miss the same narrow/disconnected component. Adversarial
  tests remain mandatory.
- The profile and LR set are restricted to this beta-binomial model and target
  mapping; no generality beyond that model is claimed.
- No LR cutoff is selected. No calibration or holdout has been run.
- No simulation or scientific C10 execution has run.

## Next required work

1. Expand independent score/likelihood checks to all boundary classes and
   compare gradients/scores against numerical differentiation.
2. Execute the nested-grid convergence diagnostic over a predeclared
   adversarial roster; supplement it with adversarial multimodality tests for
   both concentration and MCSE scans.
3. Extend robust root-bracketing tests for non-finite profile regions and
   endpoint cases.
4. Validate analytic score expressions against independent numerical
   derivatives over a wider asymmetric parameter roster.
4. Wire interval emission into C5 only after the cutoff and abstention policy
   have been prospectively specified and authorized.
5. Calibrate the cutoff on a calibration roster independent of the holdout
   roster, only after separate authorization.

This artifact changes no causal claim, estimand, frozen v002 baseline, main
branch, RMA, Evidence→Claim Matrix, or scientific execution authorization.
