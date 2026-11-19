# C10-S — F5 boundary-aware MCSE profile-likelihood design 001

**Record:** C10S-F5-MCSE-PROFILE-LIKELIHOOD-DESIGN-001  
**Status:** RESEARCH METHOD DESIGN — FORMULA SPECIFIED / NOT IMPLEMENTED / CUTOFF NOT CALIBRATED / NO EXECUTION  
**Date:** 2026-11-19  
**Applies to:** F5 beta-binomial world-probability fixture only  
**Baseline:** C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001 v002 remains frozen; C5's current MCSE output remains typed abstention.

## 1. Purpose and boundary

Define a candidate F5 confidence procedure for the target nested-M/R MCSE without selecting only bootstrap draws whose raw between estimate happens to be nonnegative.

The current C5 fitted parametric bootstrap may continue to report within and untruncated raw-between percentile intervals. It must not emit an MCSE interval from the positive/projectable subset. This design is a separate candidate for that target only.

No implementation, simulation, coverage calibration, cutoff selection, Tier B, scientific C10 execution or promotion to main is authorized by this design.

## 2. F5 sampling model and exact population targets

For each independent outer world:

\(p_m \sim Beta(\alpha,\beta)\), and conditional on it \(X_m \mid p_m \sim Binomial(R,p_m)\); the observed world contribution is \(q_m=X_m/R\).

Parameterize with mean and concentration:

\(\mu=\alpha/(\alpha+\beta)\in(0,1)\), \(\kappa=\alpha+\beta>0\),
so \(\alpha=\mu\kappa\) and \(\beta=(1-\mu)\kappa\).

Let \(s=\alpha+\beta=\kappa\). The exact population components are:

\(\sigma^2_{between}=\mu(1-\mu)/(\kappa+1)\)

\(\sigma^2_{within}=\kappa\mu(1-\mu)/(\kappa+1)\)

For target design \((M^*,R^*)\), the target is:

\(g(\mu,\kappa)=MCSE(M^*,R^*)=\sqrt{\frac{\mu(1-\mu)}{M^*}\frac{1+\kappa/R^*}{1+\kappa}}\).

This target is derived from the generating parameters, not from a truncated sample estimate. Its parameter-space range is:

\(0\leq g\leq 1/(2\sqrt{M^*})\).

The formula is an exact F5 oracle identity; it is not a Gaussian approximation.

## 3. Full count likelihood

The observed sufficient data are the M world counts \(x_1,\ldots,x_M\in\{0,\ldots,R\}\). The beta-binomial likelihood is:

\(L(\mu,\kappa)=\prod_{m=1}^{M}{R\choose x_m}\frac{B(x_m+\mu\kappa,R-x_m+(1-\mu)\kappa)}{B(\mu\kappa,(1-\mu)\kappa)}\).

Use the complete count vector. Do not filter worlds, discard counts, condition on nonnegative raw-between estimates, or substitute a positive-only bootstrap distribution.

The likelihood is independent of the ordering of worlds. The implementation must preserve the exact integer count support and use stable log-beta/log-gamma evaluation.

## 4. Profile likelihood for the scalar MCSE target

For a proposed scalar \(g\), define:

\(\ell_p(g)=\sup_{(\mu,\kappa)\in\Theta:g(\mu,\kappa)=g}\ell(\mu,\kappa)\)

and the likelihood-ratio statistic:

\(\Lambda(g)=2[\ell(\hat\mu,\hat\kappa)-\ell_p(g)]\).

A useful reduction avoids a generic two-dimensional constrained optimizer for every g. Rearranging the target equation gives:

\(h(g,\kappa)=g^2M^*\frac{1+\kappa}{1+\kappa/R^*}=\mu(1-\mu)\).

For a feasible \((g,\kappa)\), \(0\leq h\leq1/4\), and the only possible means are:

\(\mu_{\pm}(g,\kappa)=\frac{1\pm\sqrt{1-4h(g,\kappa)}}{2}\).

Therefore:

\(\ell_p(g)=\sup_{\kappa\in[0,\infty],\;h\leq1/4}\max\{\ell(\mu_+,\kappa),\ell(\mu_-,\kappa)\}\).

The implementation must evaluate both branches. It must not assume the likelihood is symmetric in the observed counts merely because the target is symmetric under \(\mu\leftrightarrow1-\mu\).

## 5. Boundary closure — mandatory

The parameter space must be treated as an extended closure, not merely as finite optimizer bounds:

- \(\mu\to0\) or \(\mu\to1\): degenerate all-zero/all-one world probabilities; both variance components and target MCSE tend to zero.
- \(\kappa\to\infty\): binomial limit with \(\sigma^2_{between}\to0\) and positive within variance when \(0<\mu<1\).
- \(\kappa\to0\): two-point mixing limit with \(\sigma^2_{within}\to0\) and positive between variance when \(0<\mu<1\).
- Interior: finite positive \(\mu\) and \(\kappa\).

A numerical cap on \(\kappa\) is not itself a statistical boundary solution. The optimizer must either evaluate the analytic limiting likelihoods or demonstrate a controlled limit approximation with an error bound.

All-zero/all-one and equal-intermediate-count samples must not automatically be treated as computational failures. Their MLE may lie on a limiting boundary. The confidence set may legitimately be one-sided or include a broad range of MCSE values. Do not replace it with \([0,0]\) merely because the observed point estimate is zero.

## 6. Confidence-set inversion and calibration

For a calibrated cutoff \(c_{.95}\), define the confidence set:

\(C_{.95}=\{g\in[0,1/(2\sqrt{M^*})]:\Lambda(g)\leq c_{.95}\}\).

The reported interval is the hull \([\inf(C_{.95}),\sup(C_{.95})]\). If the set is disconnected, retain and report its connected components as well as the hull; do not conceal disconnectedness.

**No Wilks chi-square cutoff is assumed.** The beta-binomial count likelihood is discrete and nuisance/boundary dependent. The cutoff must be calibrated prospectively by finite-sample simulation using the independent beta-binomial count generator and a separately implemented likelihood/profile evaluator.

A conservative calibration candidate is a least-favourable cutoff over a predeclared nuisance grid:

\(c_{.95}(M,R)=\sup_{(\mu,\kappa)\in\mathcal G}Q_{.95}\{\Lambda(g(\mu,\kappa));X^*\mid\mu,\kappa\}\).

The grid \(\mathcal G\), boundary limits, number of calibration replicates, Monte Carlo uncertainty of the cutoff, interpolation/guard-band rule and whether the resulting guarantee is grid-bounded or continuous-parameter-bounded must be fixed before execution. A finite grid alone does not prove uniform coverage over the continuous parameter space.

The cutoff calibration simulation must use independent RNG namespaces from the holdout datasets and from any fitted-C5 bootstrap. If a valid least-favourable cutoff cannot be established, the method remains exploratory and cannot be called calibrated.

## 7. Numerical and statistical diagnostics

For every fit and candidate interval, retain:

- \(M,R,M^*,R^*\), count vector fingerprint and target identity;
- \(\hat\mu,\hat\kappa\), boundary branch, log-likelihood and optimizer diagnostics;
- both \(\mu_+\) and \(\mu_-\) profile branches and the maximizing concentration;
- profile-LR curve, cutoff, root brackets, connected confidence-set components and hull;
- status distinguishing finite interval, one-sided/boundary interval, disconnected set, unbounded/numerical failure and non-identification;
- independent beta-binomial oracle truth for within, between and target MCSE;
- coverage, Wilson interval, interval emission, unconditional cover rate, width and runtime in the later holdout.

No method may return a regular finite interval after an optimizer failure by silently falling back to C5 percentile or C0.

## 8. Adversarial tests required before calibration

1. Interior beta22 datasets with both profile branches evaluated.
2. Asymmetric beta parameters where the two profile branches have different likelihood.
3. \(\kappa\to\infty\) binomial limit and \(\kappa\to0\) two-point limit.
4. All-zero, all-one and equal-intermediate-count samples.
5. Near-boundary \(\mu\) and near-boundary concentration.
6. Target at lower and upper attainable limits.
7. Disconnected profile confidence set and hull reporting.
8. Optimizer non-convergence, non-finite likelihood and root-bracketing failure.
9. Agreement of \(g(\mu,\kappa)\) with the independent F5 moment oracle.
10. Permutation invariance of world-count order.
11. Reproducibility of the cutoff calibration under fixed seeds.
12. Explicit proof that no subset of positive raw-between/projectable bootstrap draws is used.

## 9. Comparative position and disposition

If implemented and calibrated, this procedure would be the F5 joint MCSE candidate, compared on matched F5 datasets against the frozen C0 v002 MCSE projection. C5's current fitted percentile intervals remain candidates only for the within and raw-between components.

The current C5 MCSE output remains:

- mcse_interval = None
- reason = F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED.

This design does not alter the v002 Tier A/B protocol, the original Tier A NOT_VALIDATED result, the C10 causal estimand, the production Analyzer, RMA, Evidence→Claim Matrix or scientific authorization state.

**Disposition:** FORMULA/DESIGN CANDIDATE / NOT IMPLEMENTED / NOT CALIBRATED / NO EXECUTION AUTHORIZED.
