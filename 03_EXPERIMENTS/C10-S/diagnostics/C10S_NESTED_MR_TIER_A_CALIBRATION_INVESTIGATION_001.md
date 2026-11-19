# C10-S — Tier A nested M/R calibration investigation

**Record:** C10S-NESTED-MR-TIER-A-CALIBRATION-INVESTIGATION-001  
**Status:** RESEARCH DIAGNOSTIC — EXPLORATORY / NON-CANONICAL / NO METHOD CHANGE  
**Date:** 2026-11-19  
**Source run:** GitHub Actions `44449787220`  
**Artifact:** `14495695421` (`c10s-nested-mr-validation-6bcb5a2827d810896315f66042083a5be7dda308-A`)  
**Artifact digest:** `sha256:0bb83a1ab0fd8c22c2aa98bb1b7944d65b979b4ba8b44fec3be462d708e57b60`  
**Code commit:** `6bcb5a2827d810896315f66042083a5be7dda308`  
**Method:** `TGCV_NESTED_MR_BOOTSTRAP` 1.2  
**Protocol:** `C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001` v002  
**Protocol SHA-256:** `cf3fd80e474e58632f6a88d8afb092df8db31716ed962826f949f5750405bad1`

## 1. Purpose and governance boundary

This note investigates why Tier A did not validate the current 95% percentile-bootstrap intervals and projected-MCSE procedure. It is a secondary exploratory analysis of the already completed Tier A artifact.

It does **not** amend or reinterpret protocol v002, does not promote a method, does not authorize Tier B, and does not authorize C10 scientific execution. All reported alternative intervals are diagnostic benchmarks, not post-hoc replacements for the frozen acceptance procedure.

The original Tier A disposition remains **NOT_VALIDATED**.

## 2. Artifact integrity and scope

The downloaded artifact contains eight cell-level JSONL records, eight summaries, a run manifest, a checkpoint index and SHA256SUMS. All 19 listed files passed `sha256sum -c SHA256SUMS.txt`.

The run manifest binds the artifact to:
- authorization `TIER-A-RETRY-20261119-01`;
- code commit `6bcb5a2827d810896315f66042083a5be7dda308`;
- protocol v002 and its SHA-256 above;
- fixture generator 1.1 and seed schedule 1.0;
- K=1,000 datasets per cell and B=1,000 bootstrap draws per dataset;
- Python 3.12.10 and NumPy 2.3.5.

No C10 Generator, Analyzer, Evaluator, scientific DGP, calibration bank or confirmatory workflow was run.

## 3. Tier A percentile-bootstrap results

The table reports the original frozen percentile-bootstrap coverage. The target is 95%; protocol v002 requires coverage in [93%,97%] and a 95% Wilson interval containing 95%.

| Cell | Within coverage | Between-raw coverage | Projected-MCSE availability | MCSE conditional coverage |
|---|---:|---:|---:|---:|
| F1 balanced M10/R5 | 84.0% | 93.8% | 24.4% | 98.36% (244 cases) |
| F1 balanced M30/R20 | 94.9% | 90.7% | 100.0% | 90.4% |
| F1 high-between M10/R5 | 84.3% | 80.1% | 91.6% | 82.42% |
| F1 high-between M30/R20 | 93.8% | 86.5% | 100.0% | 86.5% |
| F1 low-between M10/R5 | 79.9% | 98.2% | 0.0% | Not emitted |
| F1 low-between M30/R20 | 95.5% | 87.8% | 57.8% | 83.39% |
| F5 beta22 M10/R5 | 94.2% | 98.7% | 1.7% | 100% (17 cases only) |
| F5 beta22 M30/R20 | 91.8% | 95.4% | 99.7% | 95.49% |

Cell adjudication:
- Within: 4/8 pass (F1 balanced M30/R20; F1 high-between M30/R20; F1 low-between M30/R20; F5 beta22 M10/R5).
- Between raw: 2/8 pass (F1 balanced M10/R5; F5 beta22 M30/R20).
- Projected MCSE: only F5 beta22 M30/R20 meets both availability >=95% and the coverage/Wilson rule.

The F5 beta22 M10/R5 MCSE conditional coverage of 100% is based on only 17 emitted intervals and is not calibrated evidence. Conditional coverage must not be read without availability.

## 4. Point-estimator diagnosis

The mean point estimates are generally close to their analytical truths. Examples:

| Cell | Within bias | Between-raw bias |
|---|---:|---:|
| F1 balanced M30/R20 | -0.000243 | +0.005699 |
| F1 high-between M30/R20 | -0.000866 | +0.013085 |
| F1 low-between M30/R20 | +0.002395 | -0.000572 |
| F5 beta22 M30/R20 | -0.000596 | +0.000475 |

This supports a provisional diagnosis that the principal defect is interval/projection calibration, not a gross point-estimator bias. It does not establish point-estimator validity outside these fixtures.

For the balanced Gaussian design, the estimators are the usual balanced one-way ANOVA mean-square estimators:
- `MSW` estimates `sigma2_within`;
- `between_raw = S2(world means) - MSW/R` estimates `sigma2_between` without truncation.

The raw between estimate must remain the inferential object. The nonnegative convenience field must not replace it in bias, coverage or interval scoring.

## 5. Independent Gaussian finite-sample benchmark

### 5.1 Within component

For F1, under the exact Gaussian random-intercept fixture, the within-world residual sum of squares has the exact pivot:

`M(R-1) MSW / sigma2_within ~ chi-square_df`, where `df=M(R-1)`.

Therefore an exact 95% interval is:

`[df*MSW / chi2(0.975,df), df*MSW / chi2(0.025,df)]`.

This interval was computed independently from each record's `estimate_within` and compared with the known fixture truth. Results:

| F1 cell | Percentile bootstrap coverage | Exact chi-square within coverage |
|---|---:|---:|
| Balanced M10/R5 | 84.0% | 95.6% |
| Balanced M30/R20 | 94.9% | 94.6% |
| High-between M10/R5 | 84.3% | 95.4% |
| High-between M30/R20 | 93.8% | 95.4% |
| Low-between M10/R5 | 79.9% | 94.6% |
| Low-between M30/R20 | 95.5% | 94.6% |

The benchmark restores nominal coverage across all six Gaussian cells. This is strong evidence that the percentile bootstrap is not adequately calibrated for the within variance component in the smaller designs, despite small point-estimator bias.

### 5.2 Between component: conservative joint-pivot benchmark

For the Gaussian random-intercept fixture, define `tau2 = sigma2_between + sigma2_within/R`, and let `S2bar` be the sample variance of the M world means. Then:

- `(M-1) S2bar / tau2 ~ chi-square_(M-1)`;
- `M(R-1) MSW / sigma2_within ~ chi-square_(M(R-1))`;
- these two quantities are independent under the Gaussian balanced model.

A conservative >=95% confidence set for `sigma2_between = tau2 - sigma2_within/R` was constructed by combining separate two-sided 97.5% chi-square intervals for `tau2` and `sigma2_within` with Bonferroni protection. The interval was not truncated to force nonnegative endpoints.

| F1 cell | Percentile bootstrap coverage | Conservative joint-pivot coverage |
|---|---:|---:|
| Balanced M10/R5 | 93.8% | 98.6% |
| Balanced M30/R20 | 90.7% | 96.8% |
| High-between M10/R5 | 80.1% | 97.6% |
| High-between M30/R20 | 86.5% | 97.0% |
| Low-between M10/R5 | 98.2% | 99.6% |
| Low-between M30/R20 | 87.8% | 97.9% |

This is a deliberately conservative Gaussian benchmark, not a proposed general-purpose production interval. It demonstrates that the between-component coverage failures can be addressed under a correctly specified Gaussian model, but its overcoverage and potentially large width require a more efficient interval construction (e.g. generalized pivotal, profile-score or carefully validated parametric methods).

### 5.3 What this benchmark does and does not establish

It establishes a model-specific reference for F1 and exposes the gap between percentile-bootstrap and finite-sample Gaussian inference. It does not validate Gaussian assumptions for real C10-S metrics, nor does it validate F5. The exact chi-square within pivot is not transferable to arbitrary discrete, skewed or heavy-tailed contributions.

## 6. Shape and width diagnostics

The percentile intervals are not uniformly too narrow. Their failure is component- and regime-dependent.

For between raw, mean interval width divided by `3.92 × empirical SD of the point estimator` was:
- balanced M10/R5: 0.887;
- balanced M30/R20: 0.899;
- high-between M10/R5: 0.740;
- high-between M30/R20: 0.864;
- low-between M10/R5: 1.452 (overcoverage);
- low-between M30/R20: 1.376 (yet undercoverage);
- F5 beta22 M10/R5: 1.134 (overcoverage);
- F5 beta22 M30/R20: 1.031 (yet undercoverage).

Thus a simple global widening factor is not justified. Skewness, finite-cluster resampling, proximity to the nonnegative boundary and discrete support affect coverage differently. Interval calibration must address the sampling distribution, not merely inflate all widths.

## 7. Projected-MCSE abstention diagnosis

The implementation retains all B bootstrap draws. For each target projection it counts a boundary draw whenever `b_between < 0`; if **any** of the B draws is negative, it returns `SENSITIVITY_REQUIRED` and emits no numeric interval.

Consequently, projected-MCSE availability is effectively the proportion of datasets with zero negative-between draws among B=1,000. If the per-draw probability of a negative draw is p, the probability of observing no negative draw is approximately `(1-p)^B`.

This makes availability intrinsically dependent on B. Increasing B can reduce reported availability even though the underlying dataset and statistical design are unchanged. The rule is intentionally conservative and consistent with the frozen v002 instruction not to condition on positive draws, but it is not a stable measure of estimability or calibration. It is a Monte Carlo detection rule for any negative support.

Do not fix this by silently dropping negative draws, clipping the raw estimator, or conditioning the interval on positive draws. A new method must instead define a boundary-aware joint inference procedure for `(sigma2_within, sigma2_between)` and the functional:

`MCSE(M*,R*) = sqrt(sigma2_between/M* + sigma2_within/(M*R*))`.

Candidate approaches include a constrained/generalized pivotal construction, profile-score inversion on the nonnegative variance parameter space, or a pre-specified boundary-mixture procedure. The boundary mass/probability and the resulting MCSE interval should be reported separately. The rule must be invariant to increasing B apart from ordinary Monte Carlo error.

## 8. Literature and method candidates

Relevant methodological evidence supports comparing several interval families rather than tuning a single percentile interval:

1. Austin & Leckie (2020), multilevel bootstrap inference, compare parametric, residual and nonparametric procedures and report that parametric and residual bootstrap procedures generally performed better than the nonparametric procedure for the variance/heterogeneity quantities they studied. This is adjacent evidence, not direct validation of the present scalar estimator.
2. Jiratampradab, Supapakorn & Suntornchost (2022), unbalanced one-way random effects, compare classical exact, generalized pivotal and fiducial intervals; their simulation favours generalized pivotal/fiducial approaches on coverage and average length in the studied designs.
3. Ekvall & collaborators' score-based variance-component work and the `reconf` implementation use profile-score inversion for variance parameters, with near-nominal coverage in studied linear mixed models, including near-boundary cases. This is a promising model-based comparator, not an automatic solution for arbitrary q distributions.
4. Carpenter & Bithell (2000) and later bootstrap guidance distinguish percentile, BCa and studentized intervals; BCa/studentized methods are candidates when their assumptions and nested resampling implementation are justified. Studentization requires a valid standard-error estimate inside each bootstrap replicate and may be computationally expensive.

External references:
- Austin & Leckie (2020), DOI: 10.1080/00949655.2020.1797738.
- Jiratampradab et al. (2022), DOI: 10.2478/stattrans-2022-0047.
- `reconf` score-based variance-component intervals: https://github.com/koekvall/reconf.
- Carpenter & Bithell (2000), *Statistical Methods in Medical Research*, 19, 1141–1164.

## 9. Recommended integrated calibration programme

### Stage A — preserve and freeze the diagnosis

- Keep protocol v002 and the original Tier A result immutable.
- Keep the current percentile implementation as a baseline comparator.
- Do not reinterpret the failed coverage as failure of the point estimators or of C10-S.

### Stage B — create a method-comparison development suite

Use the existing Tier A artifact as development evidence only. Compare, at minimum:
- current two-stage nonparametric percentile bootstrap;
- BCa or studentized nested bootstrap, with cluster-level acceleration/studentization derived correctly;
- Gaussian exact chi-square within interval and Gaussian joint-pivot/profile-score between interval as F1 reference methods;
- parametric bootstrap under the declared Gaussian F1 generator;
- a discrete beta-binomial-aware comparator for F5.

Report point-estimator bias/RMSE, coverage with Wilson intervals, average length, lower/upper miss rates, boundary frequency, computational cost and abstention. Never select a method solely because it fits the current eight cells.

### Stage C — independent holdout validation

After selecting a candidate and freezing a new protocol version:
- use a new seed namespace/version and independently generated holdout datasets;
- predeclare K, B, cell grid, interval methods, coverage tolerances and boundary rules;
- retain all original eight cells, with explicit extension for additional M/R support only if justified before outcomes;
- test sensitivity to distributional departures, especially skewed/heavy-tailed outer worlds and discrete conditional outcomes;
- evaluate projected MCSE as a joint functional, not as two separately calibrated marginal intervals.

The existing K=1,000 outcomes must not serve as the final unbiased acceptance set after method selection.

### Stage D — application gate

Even a successful synthetic calibration does not establish that the real C10-S M/R sampling contracts are valid. Before applying projections to C10-S, independently establish the actual outer-world and within-world assignment mechanisms, independence/coupling, complete contribution definition and support.

## 10. Current conclusion

**The current method remains NOT_VALIDATED under protocol v002.**

The investigation identifies:
1. a clear finite-sample percentile-bootstrap undercoverage problem for Gaussian within and between components;
2. an exact Gaussian within-component benchmark that restores nominal coverage;
3. a conservative Gaussian joint-pivot between benchmark that restores at-least-nominal coverage but may overcover;
4. an MCSE abstention rule whose availability is mechanically dependent on B and therefore needs a new boundary-aware inferential design;
5. no basis yet to generalize a Gaussian correction to the discrete beta-binomial family or to arbitrary C10-S metrics.

The next scientific/software operation should be a pre-registered interval-method comparison and boundary-aware MCSE design, not Tier B execution and not a change to the frozen v002 implementation.

**No Tier B authorization. No C10 scientific execution. No change to main, RMA, Evidence→Claim Matrix, STATUS or canonical TGCV claims.**
