# C10-S — F1 exact/pivotal candidate specification

**Record:** C10S-F1-EXACT-PIVOTAL-CANDIDATE-SPEC-001  
**Status:** RESEARCH DESIGN — NON-CANONICAL / FORMULAS SPECIFIED / ADDITIVE CANDIDATE IMPLEMENTED / TESTS NOT RUN  
**Date:** 2026-11-19  
**Applies to:** F1 balanced Gaussian nested random-intercept fixture only  
**Baseline preserved:** C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001 v002; TGCV_NESTED_MR_BOOTSTRAP 1.2  
**Research branch:** research/c10s-nested-mr-calibration-design-20261119

## 1. Purpose and boundary

Specify the first F1 exact/pivotal candidate against the common variance-comparison contract. This is a model-specific reference procedure, not a replacement for the frozen percentile-bootstrap baseline and not a general method for F5 or arbitrary C10-S contributions.

This specification authorizes no test execution, workflow dispatch, Monte Carlo calibration, holdout, Tier B, scientific C10-S execution, or promotion to main. The mission record's execution boundary remains controlling.

## 2. Sampling model and sufficient statistics

For a balanced design with M independent outer worlds and R observations per world:

`q_{mr}=\mu+U_m+\epsilon_{mr}`

where `U_m ~ N(0, sigma_b2)`, `epsilon_mr ~ N(0, sigma_w2)`, mutually independent, and `sigma_b2 >= 0`, `sigma_w2 >= 0`. The chi-square pivots below are regular when their denominator variance is positive. At an exact zero-variance boundary, the corresponding sufficient statistic is degenerate at zero and must be handled by an explicit boundary branch (returning the point interval `[0,0]` for that component); do not evaluate a stochastic pivot with a zero denominator.

Define:

- `MSW = sum_m sum_r (q_mr - qbar_m)^2 / [M(R-1)]`;
- `S2bar = sum_m (qbar_m - qbar)^2 / (M-1)`;
- `tau2 = sigma_b2 + sigma_w2/R`.

Under this exact Gaussian balanced model:

`nu_w * MSW / sigma_w2 ~ chi-square(nu_w)`, with `nu_w=M(R-1)`;

`nu_b * S2bar / tau2 ~ chi-square(nu_b)`, with `nu_b=M-1`.

The two pivots are independent. The raw unbiased component estimate remains:

`sigma_b2_hat_raw = S2bar - MSW/R`.

No truncation, positive-only conditioning, or substitution of a nonnegative convenience estimate is permitted for inference or scoring.

## 3. C1a — exact marginal interval for within variance

For nominal error `alpha`, return:

`Lw = nu_w * MSW / chi2_quantile(1-alpha/2, nu_w)`;

`Uw = nu_w * MSW / chi2_quantile(alpha/2, nu_w)`.

The interval is exact under the stated F1 model when `sigma_w2>0`; at `sigma_w2=0`, `MSW=0` almost surely and the explicit degenerate-boundary interval is `[0,0]`. The implementation must expose its model scope, boundary branch and degrees of freedom in provenance. Invalid degrees of freedom or non-finite/negative sufficient statistics produce typed failure, not a fallback.

## 4. C1b — conservative joint-pivot confidence set for between variance

Construct two-sided intervals for both `tau2` and `sigma_w2` at marginal confidence `1-alpha/2` (marginal error `alpha/2`):

`[Lt, Ut] = [nu_b*S2bar/chi2_quantile(1-alpha/4,nu_b), nu_b*S2bar/chi2_quantile(alpha/4,nu_b)]`;

`[LwJ, UwJ] = [nu_w*MSW/chi2_quantile(1-alpha/4,nu_w), nu_w*MSW/chi2_quantile(alpha/4,nu_w)]`.

Their intersection has coverage at least `1-alpha` by Bonferroni (and the pivots are independent under F1) when both denominator variances are positive. If `tau2=0`, then `S2bar=0` almost surely and the tau interval is handled as the degenerate point `[0,0]`; if `sigma_w2=0`, then `MSW=0` almost surely and its interval is `[0,0]`. The implementation must branch explicitly rather than divide by a zero variance. Project the rectangle through `sigma_b2 = tau2 - sigma_w2/R`:

`Lb_raw = Lt - UwJ/R`;

`Ub_raw = Ut - LwJ/R`.

Return these raw endpoints unchanged, including a negative lower endpoint. Do not intersect the reported scalar interval with zero: the scored estimator and interval are for the raw component estimator. Label the result **conservative F1 joint-pivot benchmark**, not efficient or general-purpose.

For parameter-space optimization only, define the joint confidence set:

`C = {(tau2,w2): Lt<=tau2<=Ut, LwJ<=w2<=UwJ, w2>=0, tau2>=w2/R}`.

This constraint represents `sigma_b2>=0`; it must not be used to silently clip the raw scalar interval above.

## 5. C1c — joint confidence-set projection for target MCSE

For a declared target design `(Mstar,Rstar)`, the target is:

`g(tau2,w2) = sqrt((tau2-w2/R)/Mstar + w2/(Mstar*Rstar))`.

The MCSE interval is the image of the same joint confidence set `C`:

`Lmcse = min_{(tau2,w2) in C} g(tau2,w2)`;

`Umcse = max_{(tau2,w2) in C} g(tau2,w2)`.

This is a projection of a single joint confidence set, not a combination of independently selected marginal endpoints. Since the objective is continuous and C is compact when nonempty, extrema exist. A deterministic bounded two-dimensional optimizer or exact boundary/corner evaluation may be used, but the implementation must verify feasibility and compare all relevant boundary candidates. The optimizer must not use random simulation or a Wilks cutoff.

If C is empty, return typed abstention `EMPTY_FEASIBLE_JOINT_CONFIDENCE_SET` and retain the diagnostic endpoints and sufficient statistics. Do not fall back to a clipped, positive-only, or independently assembled interval. If numerical optimization fails its feasibility/tolerance checks, return `PROFILE_PROJECTION_NUMERICAL_FAILURE`.

Report the joint-set construction, alpha allocation, target `Mstar/Rstar`, optimizer/tolerance, and whether an endpoint is attained at a boundary. This procedure's availability is not a function of bootstrap B.

## 6. Required adversarial formula checks (design only; not run)

The future deterministic suite must cover:

1. Exact chi-square quantiles and interval ordering for several valid M/R values.
2. Agreement of `nu_w*MSW/sigma_w2` and `nu_b*S2bar/tau2` formulas with hand calculations.
3. Negative `Lb_raw` is preserved exactly.
4. Zero raw between estimate does not trigger clipping or an automatic failure; exact zero `sigma_w2` and exact zero `tau2` use their declared degenerate-boundary branches.
5. Joint-set feasibility with an interior point and with an active `sigma_b2=0` boundary.
6. MCSE projection for `Rstar=R`, `Rstar>R`, and `Rstar<R`; the objective must be evaluated from the original variance-component expression.
7. Empty feasible set and numerical non-convergence produce distinct typed abstentions.
8. Deterministic repeatability and no mutation of the immutable input dataset.
9. Explicit rejection of F5/non-Gaussian family labels by this F1-only method.

These are software/formula tests, not coverage validation.

## 7. Comparison contract and interpretation

The candidate returns the common observed-data point estimates unchanged, plus separate interval records for within, raw between and MCSE. It must not overwrite the common adapter's point estimates or the frozen Analyzer output. Provenance must identify:

- method `C1_F1_EXACT_PIVOTAL`;
- model scope `F1_BALANCED_GAUSSIAN_RANDOM_INTERCEPT`;
- `M`, `R`, `nu_w`, `nu_b`, `alpha`;
- sufficient statistics `MSW`, `S2bar`;
- raw component estimate;
- confidence-set endpoints and feasibility status;
- MCSE target `Mstar`, `Rstar`;
- typed abstention, if any.

The comparison must score coverage against the raw between truth and report interval width, lower/upper miss rates, and emission rate. Conservative overcoverage and width are explicit costs; coverage alone cannot select this method.

F1 exactness is conditional on the declared balanced Gaussian random-intercept DGP. It cannot be transferred to F5 beta-binomial data, skewed/heavy-tailed outer effects, unequal cluster sizes, dependence between worlds, or real C10-S contribution metrics without a separately justified model.

## 8. State and next operation

| Item | State |
|---|---|
| F1 sampling pivots | MATHEMATICALLY SPECIFIED |
| Exact within interval | SPECIFIED |
| Conservative raw-between interval | SPECIFIED |
| Joint MCSE confidence-set projection | SPECIFIED |
| Candidate implementation | IMPLEMENTED ADDITIVELY: `03_EXPERIMENTS/C10-S/harness/c10s_f1_exact_pivotal_candidate.py` |
| Deterministic tests | AUTHORED: `03_EXPERIMENTS/C10-S/harness/test_c10s_f1_exact_pivotal_candidate.py`; NOT RUN |
| Coverage calibration | NOT AUTHORIZED |
| Independent holdout | NOT AUTHORIZED |
| Tier B | NOT AUTHORIZED |
| C10 scientific execution | NOT AUTHORIZED |

**Implementation note (2026-11-19):** C1 was added as `c10s_f1_exact_pivotal_candidate.py` using the existing `c10s_variance_comparison_interface.py`; no duplicate adapter was created. Deterministic tests were authored in `test_c10s_f1_exact_pivotal_candidate.py` but have not been run. The implementation uses the existing interface's pooled within estimate and observed variance of world means, preserves raw between endpoints, and obtains the target-MCSE interval by evaluating the vertices of the Bonferroni rectangle intersected with the physical parameter space. This is a candidate implementation, not yet reviewed by an independent execution or test run. The next operation is static mathematical/code review and integration-contract reconciliation. Technical test execution, workflow dispatch, coverage calibration and scientific execution remain unauthorized.
