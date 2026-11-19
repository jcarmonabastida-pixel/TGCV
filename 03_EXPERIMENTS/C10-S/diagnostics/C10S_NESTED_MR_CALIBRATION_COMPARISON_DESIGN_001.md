# C10-S — Nested M/R calibration comparison design

**Record:** C10S-NESTED-MR-CALIBRATION-COMPARISON-DESIGN-001  
**Status:** RESEARCH DESIGN — NON-CANONICAL / NOT IMPLEMENTED / NOT EXECUTED  
**Date:** 2026-11-19  
**Predecessor diagnosis:** `C10S_NESTED_MR_TIER_A_CALIBRATION_INVESTIGATION_001`  
**Frozen baseline:** protocol `C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001` v002; method `TGCV_NESTED_MR_BOOTSTRAP` 1.2  
**Source Tier A run:** `44449787220`; artifact `14495695421`; code commit `6bcb5a2827d810896315f66042083a5be7dda308`

## 1. Decision and boundary

The next operation is a controlled comparison of interval procedures on common synthetic datasets, not another Tier A/Tier B run and not a change to the frozen estimator. The purpose is to identify which inferential procedure, if any, has defensible finite-sample coverage for the two variance components and their MCSE functional across the declared fixture families.

Protocol v002 and its Tier A result remain immutable. Current percentile intervals remain the baseline. This document neither selects a winner nor authorizes implementation execution, Tier B, or C10 scientific execution.

## 2. Statistical target and invariants

For balanced nested observations:
`q_{mr}=\mu+U_m+\epsilon_{mr}`, with independent outer effects and conditional inner errors in F1.

The unbiased ANOVA component estimators remain:
`MSW = SSW/[M(R-1)]`,
`MSB = R S^u_{\bar q}`,
`\hat\sigma^2_w=MSW`,
`\hat\sigma^2_{b,raw}=(MSB-MSW)/R=S^u_{\bar q}-MSW/R`.

The raw between estimate is the scored inferential object. A nonnegative convenience estimate may be reported separately but must never replace or truncate `between_raw` in bias, RMSE, coverage, likelihood, or bootstrap records.

The target projection is:
`g(\sigma_b^2,\sigma_w^2)=\operatorname{MCSE}(M^*,R^*)=\sqrt{\sigma_b^2/M^*+\sigma_w^2/(M^*R^*)}`.

Every candidate must preserve the same dataset, truth, M/R structure, target projection and coverage denominator. No method-specific deletion of negative raw draws is allowed without an explicitly defined constrained inferential construction.

## 3. Candidate method families

### C0 — Frozen baseline: two-stage nonparametric percentile bootstrap

- Exact protocol-v002 resampling law: resample M complete clusters, then R contributions within each selected cluster copy.
- Retain all B draws, including all-same-source cluster samples and negative raw-between values.
- Report percentile intervals for raw within, raw between and any declared regular projection.
- This is the comparison baseline, not a presumed acceptable procedure.

### C1 — Gaussian exact / finite-sample pivot benchmark (F1 only)

Under the balanced Gaussian random-intercept fixture:

`\nu_w=M(R-1)`,
`\nu_b=M-1`,
`\nu_w MSW/\sigma_w^2\sim\chi^2_{\nu_w}`,
`\nu_b S^2_{\bar q}/\tau^2\sim\chi^2_{\nu_b}`,
where `\tau^2=\sigma_b^2+\sigma_w^2/R`. The two pivots are independent.

Within interval at level 1−α:
`[\nu_w MSW/\chi^2_{1-\alpha/2,\nu_w},\ \nu_w MSW/\chi^2_{\alpha/2,\nu_w}]`.

Between raw inference must retain the constraint `\sigma_b^2=\tau^2-\sigma_w^2/R\geq0`. Include:
1. a conservative Bonferroni interval formed from independent `\tau^2` and `\sigma_w^2` intervals, explicitly labelled conservative;
2. a constrained profile-likelihood interval for `\sigma_b^2`, with nuisance `\sigma_w^2` profiled over the admissible parameter space.

Do not label the conservative interval efficient. C1 is an oracle/reference for F1 only and is not a general-purpose solution for F5 or real C10 metrics.

### C2 — Parametric bootstrap under the declared DGP

- F1: generate parametric bootstrap datasets from the fitted Gaussian random-intercept model; refit both variance components on each dataset; retain negative raw between estimates.
- F5: fit a declared beta-binomial random-effects model to world-level Bernoulli contributions; use the exact fixture parameterization as a separate oracle-known upper-bound diagnostic, not as the deployable fitted procedure.
- Refit the complete estimator in each parametric replicate. Do not bootstrap only a derived formula while holding nuisance estimates fixed.
- Report sensitivity to boundary estimates, optimizer failures, convergence, parameter constraints and fit misspecification.

Oracle-known F5 parameters are not a fair estimate of real-world calibration and must be labelled as an oracle benchmark.

### C3 — BCa hierarchical cluster bootstrap

- Preserve M as the outer resampling unit and R as the conditional inner unit.
- Bias correction must be computed from the same target statistic and same raw (untruncated) estimand.
- Acceleration must use a delete-one-outer-cluster jackknife as the primary cluster-level influence calculation. Inner-level jackknife is not interchangeable with outer-level acceleration.
- If a stable acceleration cannot be computed (ties, degenerate jackknife, insufficient outer support), return a typed abstention, not a percentile fallback.
- Report acceleration, bias-correction constant, adjusted quantiles and failure rate.

BCa is a candidate only; it may not be presumed to fix a non-smooth/boundary variance estimator.

### C4 — Studentized nested bootstrap

- Define the studentized statistic for each component before implementation.
- The standard error inside each bootstrap replicate must be computed from a valid nested variance-estimator approximation, not borrowed from the original sample.
- Outer-cluster jackknife or a predeclared analytic standard error may be evaluated as studentizer candidates.
- Report studentizer stability, tail quantiles, failures and computational multiplier.
- No studentized interval is admissible if the replicate-level standard error is zero, undefined or based on an unsupported M/R contract.

C4 is likely expensive; benchmark a small development subset before considering confirmatory K.

### C5 — Boundary-aware joint inference for the MCSE functional

This is a separate inferential target, not a side-effect of separately calibrated marginal component intervals.

For F1, use the independent sufficient statistics:
- `X=MSW`, with `\nu_w X/\sigma_w^2\sim\chi^2_{\nu_w}`;
- `Y=S^2_{\bar q}`, with `\nu_b Y/(\sigma_b^2+\sigma_w^2/R)\sim\chi^2_{\nu_b}`.

Define the constrained parameter space:
`\Theta=\{(\sigma_b^2,\sigma_w^2):\sigma_b^2\geq0,\sigma_w^2\geq0\}`.

Construct a profile likelihood for the scalar target `g(\sigma_b^2,\sigma_w^2)` by maximizing the likelihood over all nuisance combinations satisfying a fixed g, then invert a predeclared likelihood-ratio cutoff. Calibrate the cutoff by exact/simulation-based finite-sample coverage over the F1 grid; do not assume Wilks' chi-square cutoff is valid at a boundary. A generalized-pivotal alternative may be compared on the same joint target.

The procedure must:
- include boundary mass rather than discard negative raw bootstrap estimates;
- return a numeric MCSE interval whenever the inversion is defined, including when the MLE is on the boundary;
- distinguish a legitimate unbounded/one-sided interval from computational failure;
- report boundary estimate frequency, likelihood-ratio calibration, interval width and coverage;
- be invariant to B because B is not part of this analytic inferential procedure.

For F5, no Gaussian pivot may be reused. Candidate MCSE inference must be calibrated against the beta-binomial oracle and the fitted beta-binomial parametric procedure separately.

## 4. Matched comparison protocol

All candidate procedures are evaluated on identical datasets and identical target parameters. The comparison must not use the original Tier A datasets as final acceptance evidence after method selection.

### Development stage

Use existing Tier A records only to debug and understand failure modes. New development simulations use a separate seed namespace and are labelled exploratory. Method selection criteria and code are recorded before inspecting any holdout result.

### Independent holdout stage

After freezing the candidate list, implementation, tuning rules and protocol:
- create a new seed namespace/version and fresh K datasets per cell;
- retain the eight Tier A cells and add predeclared F2 near/exact boundary cells and F5 sparse/constant controls as appropriate;
- use enough K for the Monte Carlo uncertainty of coverage to discriminate the [93%,97%] gate; K must be justified prospectively;
- use B sufficient for stable bootstrap quantiles, with Monte Carlo error of interval endpoints assessed separately from sampling coverage;
- do not increase B/K or change acceptance limits after seeing coverage outcomes.

Use independent seed namespaces for dataset generation, each bootstrap method, parametric simulation and any inner numerical calibration. Common datasets provide paired method comparison; independent random streams prevent method-specific RNG coupling.

## 5. Required outcomes and diagnostics

For each cell × method × target:
- empirical coverage and 95% Wilson interval;
- Monte Carlo standard error of coverage;
- lower-tail and upper-tail miss rates separately;
- bias, RMSE and median absolute error of component point estimates;
- mean, median and quantiles of interval width;
- interval endpoint Monte Carlo error for bootstrap methods;
- raw negative-between frequency and bootstrap boundary fraction;
- abstention / non-convergence / non-finite rates with typed reasons;
- BCa acceleration and bias correction, or studentizer diagnostics where relevant;
- computational cost and peak-memory estimate;
- coverage conditional on emission **and** unconditional usable-interval rate.

A conditional coverage result cannot pass if the method abstains too often. Report the joint operational performance: probability of emitting a valid interval and probability that the emitted interval covers, with a prespecified minimum emission rate. Do not conceal abstentions by reporting conditional coverage alone.

For a family-level disposition, every required cell must pass its predeclared criterion. No averaging across cells, components or methods can rescue a failed cell.

## 6. F5-specific caution

F5's current beta22 generator has `p_m~Beta(2,2)`, then `q_{mr}|p_m~Bernoulli(p_m)`. Its marginal moments are:
`E[p_m]=1/2`,
`E[p_m(1-p_m)]=1/5`,
`Var(p_m)=1/20`.

The conditional within and between variance targets are therefore not the same as a Gaussian variance-components likelihood. The fitted beta-binomial procedure must estimate the hyperparameters from the M world clusters and preserve finite R information. The oracle-known parameter procedure is only a best-case reference. Include sensitivity to sparse p, overdispersion and misspecified mixing distributions before generalizing.

## 7. Implementation sequence — one integrated work package

1. **Independent formula/oracle module:** implement F1 exact chi-square pivots, constrained Gaussian likelihood and F5 moment/likelihood oracles in a module separate from the production analyzer.
2. **Common comparison interface:** each candidate accepts one immutable dataset and returns typed estimates, intervals, boundary diagnostics, abstention reason and provenance. No candidate may mutate or filter input rows.
3. **Candidate implementations:** C1 first; then C2; then C3/C4 only if the required acceleration/studentizer is mathematically and computationally defensible; C5 built as a joint functional procedure.
4. **Adversarial unit tests:** negative raw between values, exact zero components, M=2, M=3, tied data, all-same-cluster bootstrap draws, BCa undefined acceleration, studentizer zero, boundary MLE, unbounded profile interval, F5 all-zero/all-one and sparse outcomes.
5. **Deterministic micro-simulation:** verify formula correctness and method determinism on small K/B only. These tests are software/oracle tests, not coverage validation.
6. **Resource benchmark:** estimate full holdout runtime/memory before fixing K/B.
7. **New protocol version and authorization:** only after design review and successful static/micro tests. The new version must explicitly supersede neither protocol v002 nor its historical result; it defines a new method-comparison validation.

## 8. Acceptance and selection rule

A candidate is eligible for selection only if:
- all algebraic/oracle invariants pass;
- no silent truncation, positive-only conditioning or untyped abstention occurs;
- each regular holdout cell meets the predeclared coverage and Wilson criterion;
- boundary cells meet their separately predeclared coverage/abstention/interval-existence requirements;
- operational emission rate is adequate and declared in advance;
- interval width is not unacceptably conservative relative to the Gaussian reference;
- the procedure is robust to the declared F5 discrete model and specified misspecification tests;
- reproducibility and runtime requirements pass.

If no candidate meets all conditions, the correct outcome is no validated general-purpose method. A model-specific Gaussian procedure may be reported as bounded F1-only evidence but cannot be generalized to arbitrary C10-S metrics.

## 9. Current state and next operation

| Item | State |
|---|---|
| Protocol v002 baseline | FROZEN; historical result NOT_VALIDATED |
| Tier A artifact | EXECUTED; integrity checked; not a holdout |
| F1 exact within pivot | EXPLORATORY BENCHMARK |
| F1 conservative between pivot | EXPLORATORY BENCHMARK |
| Gaussian profile/joint MCSE | DEFINED HERE; NOT IMPLEMENTED |
| Parametric / BCa / studentized comparison | DEFINED HERE; NOT IMPLEMENTED |
| F5 fitted beta-binomial inference | OPEN |
| New holdout protocol | OPEN |
| Tier B | NOT AUTHORIZED |
| C10 scientific execution | NOT AUTHORIZED |

**Next operation:** implement the independent F1 oracle/profile-likelihood comparator and the common result interface, with adversarial tests. Keep all work on a research branch. Do not alter the production Analyzer, protocol v002, canonical main, RMA, Evidence→Claim Matrix or scientific authorization state.
