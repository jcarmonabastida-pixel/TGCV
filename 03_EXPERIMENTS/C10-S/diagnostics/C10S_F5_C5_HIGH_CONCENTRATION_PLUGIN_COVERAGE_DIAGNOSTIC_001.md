# C10-S — F5 C5 high-concentration plug-in coverage diagnostic 001

**Date:** 2026-11-20  
**Status:** STATIC HISTORICAL-ARTIFACT DIAGNOSIS — MECHANISM NOT CAUSALLY ESTABLISHED  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Historical run:** `44615173745`  
**Artifact ID:** `14586221304`  
**Artifact ZIP SHA-256:** `b3ddcaab1c1028c934f37e3edebf9a176248b21150ab6c2212466b810085f02f`  
**Historical C5 implementation blob:** `1052ed986e4a551654b9d32928937e4e39df2c88` at approved code commit `cdd8617f13296556fd5eb463834fb60c0f051f7c`

## 1. Question and evidence boundary

This diagnostic investigates why C5's high-fitted-concentration tail in M30/R20 has severe within/raw-between undercoverage while matched C0 remains near nominal on the same selected datasets.

Only the existing B2 calibration and disjoint development-validation artifact was analyzed. No replay, new bootstrap, refit, simulation, calibration, seed change, or scientific execution was performed. The top decile is a post-fit exploratory stratum and is not an acceptance gate or causal comparison.

## 2. What C5 actually bootstraps

The exact historical C5 implementation:
1. fits the beta-binomial model once to the observed world counts, obtaining `fit.alpha` and `fit.beta`;
2. generates bootstrap world probabilities from `Beta(fit.alpha, fit.beta)`;
3. generates each world's Bernoulli count from `Binomial(R, p_world)`;
4. reconstructs rows and computes the raw within and untruncated raw-between estimators;
5. takes percentile quantiles of those bootstrap statistics.

It does **not** refit alpha/beta within each bootstrap replicate. The generated bootstrap distribution is therefore conditional on the single fitted parameter pair from the original dataset. It propagates sampling variation of the nested estimators under that fitted law, but it does not reproduce the repeated-sampling distribution of the beta-binomial parameter estimator itself.

This is a concrete structural property of C5. Whether it is the sole cause of the observed undercoverage is not established by the existing artifact.

## 3. High-κ tail: fitted model and observed estimator align, but not with DGP truth

For the beta22 DGP, the true parameters are alpha=beta=2, so:
- mu = alpha/(alpha+beta) = 0.5;
- kappa = alpha+beta = 4;
- within variance = E[p(1-p)] = mu(1-mu) kappa/(kappa+1) = 0.20;
- between variance = Var(p) = mu(1-mu)/(kappa+1) = 0.05.

The same identities applied to the median fitted parameters in the M30/R20 top decile give:

| M30/R20 bank | Top-decile κ cutoff | Median fitted α | Median fitted β | Median fitted κ | Implied within | Implied between | Observed median within | Observed median raw-between |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Calibration | 6.5771 | 3.8266 | 3.8413 | 7.6679 | 0.22116 | 0.02884 | 0.21952 | 0.03013 |
| Validation | 6.6158 | 3.8112 | 3.9239 | 7.7351 | 0.22133 | 0.02861 | 0.21965 | 0.02974 |
| DGP truth | — | 2 | 2 | 4 | 0.20000 | 0.05000 | — | — |

The fitted model's implied within/between variance allocation closely matches the observed median estimators in this selected tail. Relative to truth, it shifts approximately 0.021 of variance from between to within. This is consistent with the high-κ estimates, not an independent demonstration that the model is correct.

## 4. Matched interval evidence in M30/R20

Each top-decile stratum contains 500 datasets.

| Bank / target | C5 coverage | C5 miss direction | C5 median width | C0 coverage | C0 median width |
|---|---:|---|---:|---:|---:|
| Calibration — within | 50.0% | 50.0% truth below lower endpoint | 0.03633 | 97.8% | 0.04344 |
| Calibration — raw-between | 35.6% | 64.4% truth above upper endpoint | 0.03607 | 96.8% | 0.04324 |
| Validation — within | 50.8% | 49.2% truth below lower endpoint | 0.03628 | 97.6% | 0.04369 |
| Validation — raw-between | 35.0% | 65.0% truth above upper endpoint | 0.03577 | 95.8% | 0.04365 |

In this tail C5's median interval widths are approximately 16–18% narrower than C0's, with strongly directional misses. The two methods use the same observed point estimates; the divergence is in the interval construction, not in the raw point estimator.

The median C5 endpoints further show the displacement:
- Calibration within: median lower 0.20004, upper 0.23658; true 0.20.
- Calibration raw-between: median lower 0.01208, upper 0.04798; true 0.05.
- Validation within: median lower 0.19991, upper 0.23649; true 0.20.
- Validation raw-between: median lower 0.01187, upper 0.04786; true 0.05.

Outside the top decile, C5 coverage is instead 98.7–99.5% in these M30/R20 banks, while C0 within coverage is approximately 92.9–93.4%. This reversal confirms that aggregate coverage masks sharply heterogeneous conditional behaviour. It does not validate C0 overall; C0 also fails the frozen aggregate component gates.

## 5. Interpretation: what is supported and what is not

Supported by the source and historical records:
- C5's bootstrap law conditions on one fitted alpha/beta pair and does not refit those parameters in bootstrap replicates.
- The M30/R20 top-decile fitted concentration is about 7.7 versus the DGP truth 4.
- The fitted model's implied variance allocation closely tracks the observed point-estimate medians in that tail: higher within and lower between than truth.
- C5 intervals are narrower than matched C0 intervals there and miss in the corresponding directions.
- The same pattern appears in the independent development-validation bank.

Not established:
- That omitted parameter-estimation uncertainty is the only cause.
- That high κ itself causally produces undercoverage; the stratum is selected post-fit.
- That a refitted parametric bootstrap, profile interval, likelihood interval, or any other alternative will repair coverage.
- That C0 is a validated replacement; its overall frozen gates fail.
- That the top-decile pattern can be converted into a post-hoc threshold or eligibility rule.

The most defensible diagnosis is therefore: **C5's fixed-parameter plug-in bootstrap is conditionally miscalibrated in the observed high-κ M30/R20 stratum, in association with upward concentration estimates and a shifted within/between variance allocation. Omitted uncertainty in alpha/beta is a plausible mechanism requiring a separately designed test, not a proven causal explanation.**

## 6. Methodological implications and next admissible design work

Do not alter C5 or select a replacement from these same development banks. A later method-design proposal should compare, prospectively and on fresh disjoint development data, at least the following conceptual distinctions:
- fixed-parameter plug-in bootstrap (current C5);
- bootstrap that refits alpha/beta in every replicate, with explicit boundary/non-identification handling;
- profile/likelihood-based uncertainty for the concentration and target functionals;
- an appropriate matched nonparametric reference, without assuming C0 is valid.

Before any new bank, the design must specify the estimand, refitting/failure semantics, boundary treatment, interval construction, Monte Carlo error, computational budget, and component-wise acceptance rules. The current B2/B3 data may motivate and inform the design but may not select or tune the alternative.

No changes were made to C5, C0, frozen specification v1.0, historical B2/B3 results, DGP, thresholds, seeds, B/K, or authorization.
