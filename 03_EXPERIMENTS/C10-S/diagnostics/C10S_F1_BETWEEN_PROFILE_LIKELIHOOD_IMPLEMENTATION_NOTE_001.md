# C10-S — F1 between-variance profile likelihood implementation note

Status: IMPLEMENTED IN RESEARCH BRANCH; NOT EXECUTED; NOT CALIBRATED
Branch: `research/c10s-nested-mr-calibration-design-20261119`
Scope: balanced Gaussian random-intercept F1 only.

## Purpose

Provide a profile-likelihood alternative for the raw between-world variance
component. This is an inferential candidate, not evidence for the TGCV causal
claim. It does not replace C0, C1, or the frozen v002 baseline.

## Likelihood

Let (M) be the number of independent outer worlds and (R) the balanced
number of inner replicates. Let (S_W^2) be the pooled within-world sample
variance and (S_{ar Y}^2) the sample variance of outer-world means. Under
the balanced Gaussian random-intercept model,

- (SS_W = M(R-1)S_W^2), with (M(R-1)) degrees of freedom;
- ((M-1)S_{ar Y}^2) is the between-world sum of squares, with (M-1)
  degrees of freedom;
- the variance of an outer-world mean is (	au + sigma_W^2/R).

The log-likelihood, up to parameter-independent constants, is profiled over
(sigma_W^2>0) for each fixed (	augeq0). The constrained MLE for the
between component is (hat	au=max(0,S_{ar Y}^2-S_W^2/R)).

## Numerical inversion

Version 0.2 replaces the finite-grid set approximation with:
1. a scale-adaptive bounded optimization in log within-variance;
2. explicit comparison of the optimizer result with search-boundary values;
3. a lower endpoint of zero when the boundary satisfies the supplied LR rule,
   otherwise a bracketed root between zero and the constrained MLE;
4. geometric expansion to bracket the upper endpoint, followed by Brent root
   solving.

The LR cutoff is mandatory and caller-supplied. No default cutoff, Wilks
approximation, or calibration choice is embedded in the implementation.
An unbracketed upper endpoint or nuisance optimum at a search boundary causes
an explicit failure rather than an invented finite endpoint.

## Verification contract

Regression tests are defined for finite profile evaluation, ordered interval
endpoints, LR endpoint equations, caller-cutoff preservation, inclusion and
exclusion of the zero boundary, invalid inputs, and zero within sum of squares.

Tests have NOT been executed. No workflow, simulation, calibration, or
scientific execution has been initiated. Therefore numerical correctness and
coverage remain unverified.

## Known limitations / next checks

- The current nuisance optimization is numerical; an independent score-equation
  solver or closed-form oracle should be added before treating it as stable.
- The interval is restricted to the balanced Gaussian random-intercept model.
- Zero within sum of squares is explicitly abstained pending a separate
  boundary likelihood treatment.
- The profile LR cutoff remains unselected and uncalibrated.
- The engine currently records the profile log-likelihood diagnostic at the
  nonnegative raw estimate; it does not yet emit this profile interval as a
  competing MCSE interval.

No causal claim is updated by this artifact.
