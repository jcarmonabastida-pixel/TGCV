# C10-S — F5 B2/B3 coordinated post-result diagnostic

**Record:** C10S-F5-B2-B3-COORDINATED-DIAGNOSTIC-001  
**Date:** 2026-11-20  
**Status:** STATIC RAW-ARTIFACT DIAGNOSIS / NO NEW SCIENTIFIC EXECUTION  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Frozen specification:** `C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md`, v1.0 — unchanged  
**Primary run:** GitHub Actions `44615173745`  
**Artifact:** `c10s-f5-b2-b3-F5-B2B3-20261119-2202-cdd8617f13296556fd5eb463834fb60c0f051f7c`  
**Artifact ID:** `14586221304`  
**Artifact ZIP SHA-256:** `b3ddcaab1c1028c934f37e3edebf9a176248b21150ab6c2212466b810085f02f`

## 1. Purpose and boundary

This record advances the next F5 operation directly from the completed B2/B3 raw artifact. It is an offline/static analysis of already executed records; it does not replay the workflow, regenerate datasets, rerun a bootstrap, change the estimator, or create a new scientific sample.

The nine-file artifact was downloaded and its ZIP SHA-256 independently recomputed; it matches the GitHub artifact identity recorded in the primary result audit. The existing per-dataset JSONL records are the source for all stratified calculations below. No raw result was edited.

The frozen v1.0 criteria remain binding. All stratified analyses below are exploratory diagnostics only; they are not new acceptance criteria, tuning targets, or confirmatory evidence.

## 2. Key implementation finding: three distinct optimizer paths are currently conflated

The source code establishes three different operations:

1. **C5 production fit:** `fit_beta_binomial_counts` in `c10s_fitted_beta_binomial_bootstrap.py` runs three L-BFGS-B starts in `(logit(mu), log(kappa))`, with the same bounds, but does not pass an analytic Jacobian. SciPy therefore estimates gradients numerically. The C5 bootstrap uses this fit.
2. **Analytic-gradient comparison fit:** `audit_beta_binomial_count_fit` in `c10s_f5_beta_binomial_likelihood_diagnostics.py` runs the same three starts and bounds, but supplies the analytic score as the L-BFGS-B Jacobian. It selects the best successful analytic-gradient start and records its Hessian, score, profile curvature and boundary likelihood differences.
3. **Independent-coordinate BFGS check:** the same audit then runs BFGS in `(log(alpha), log(beta))`, initialized from the analytic-gradient fit just selected. It is a different parameterization and optimizer, but **not an independently initialized global-search check**. Its current status is marked unresolved whenever SciPy's BFGS `success` flag is false, regardless of the recorded objective difference, terminal score or parameter distance.

The current audit's `optimizer_status` compares operations 2 and 3. It does not directly reconcile operation 1 (the accepted C5 production fit) against operation 2. The B2 records nevertheless contain both values: the production fit's `fit_alpha`, `fit_beta`, and `fit_log_likelihood` are in the candidate comparison provenance; the analytic-gradient fit and BFGS diagnostics are in `fit_diagnostics.optimizer_audit`.

This is a concrete B1 traceability/diagnostic gap, not a reason to discard the existing records. The result report must distinguish the production fit from the analytic-gradient audit fit; the top-level `fit_diagnostics.selected_alpha/beta/concentration` fields describe the analytic-gradient audit fit, not necessarily the production fit used to generate C5 bootstrap draws.

### 2.1 The current runner imposes an additional all-starts-success gate

The runner's `_optimizer_diagnostic_is_resolved` requires **all three** analytic-gradient L-BFGS-B starts to report success. The frozen B1 specification requires retaining and comparing all three outcomes; it does not state that every start must individually converge when one or more successful starts agree on the admissible fit. This implementation therefore adds a stricter condition that must be reconciled with the frozen wording before it is treated as a scientific acceptance requirement.

The raw outcomes show why a blanket Boolean rule is inadequate:
- M30/R20: 342/5,000 calibration and 355/5,000 validation records have one or more failed starts, but their successful starts have median negative-log-likelihood spread around (8.5\times10^{-14}) and (8.5\times10^{-14}), with maxima (4.55\times10^{-13}) and (2.27\times10^{-13}); successful-start parameter spreads have maxima (2.08\times10^{-7}) and (5.13\times10^{-8}). The failed starts are commonly far worse in objective value. This pattern is consistent with a noncompetitive start failing while the successful starts agree.
- M10/R5: 684/5,000 calibration and 655/5,000 validation records have at least one failed start while another succeeds; successful-start objective and parameter spreads have much heavier tails (q90 parameter spread approximately 1.32 and 1.35 log-coordinate units). Here a failed start may coexist with genuine concentration-ridge ambiguity and cannot be dismissed by the same rule.

The runner's stricter gate leaves only 2,565/5,000 and 2,591/5,000 M10/R5 records resolved, and 1,596/5,000 and 1,608/5,000 M30/R20 records resolved under its combined conditions. These are implementation-gate counts, not frozen scientific component outcomes. Removing the all-starts-success condition alone would not turn the run into a PASS: the BFGS termination state and, independently, the coverage/Wilson failures remain.

## 3. Independent-coordinate BFGS: distinguish termination failure from likelihood disagreement

### M30/R20

BFGS is marked `INDEPENDENT_OPTIMIZER_UNRESOLVED` for 3,270/5,000 calibration and 3,259/5,000 validation datasets. Every such case reports `Desired error not necessarily achieved due to precision loss.`

Despite the false success flag:
- calibration absolute log-likelihood difference from the analytic-gradient fit: median 0; maximum (4.83\times10^{-13});
- validation maximum: (4.12\times10^{-13});
- log-shape parameter distance: median 0; maximum (2.14\times10^{-7}) calibration and (1.93\times10^{-7}) validation;
- independent score norm: median (1.04\times10^{-7}) / (9.71\times10^{-8}), with maxima (3.48\times10^{-6}) / (4.00\times10^{-6}).

The primary finite-difference fit and analytic-gradient fit also agree extremely closely in M30/R20: maximum absolute log-likelihood differences are (6.06\times10^{-11}) calibration and (8.07\times10^{-11}) validation; maximum absolute log-concentration differences are approximately (6.8\times10^{-6}) and (6.7\times10^{-6}).

**Interpretation:** the M30/R20 unresolved count is overwhelmingly a BFGS termination-flag/tolerance problem rather than evidence of a materially different likelihood optimum in the recorded data. It still fails the frozen no-unresolved-state gate. It must not be retrospectively relabelled PASS. A new deterministic diagnostic may report the termination flag separately from numerical concordance, but any future acceptance rule must be specified and tested before new banks.

### M10/R5

BFGS is marked unresolved for 2,169/5,000 calibration and 2,132/5,000 validation datasets. Again, every such case reports precision loss, but the tail diagnostics are materially less benign:
- BFGS-versus-analytic-fit log-likelihood difference has median (3.55\times10^{-15}), q95 (1.67\times10^{-6}) / (1.79\times10^{-6}), and maximum (4.53\times10^{-6}) / (5.72\times10^{-6});
- log-shape distance has median 0, q95 approximately (1.96\times10^{-7}), and maximum (1.45\times10^{-4}) / (2.64\times10^{-4});
- score norms have a much heavier tail than M30/R20.

More importantly, the **production finite-difference fit and analytic-gradient audit fit diverge** on M10/R5:
- calibration: 499/4,822 interior C5 fits differ in log likelihood by more than (10^{-6}), including 177/4,822 above (10^{-3}); log-shape distance has median (3.42\times10^{-7}), q90 3.15, q99 14.20, maximum 16.26;
- validation: 480/4,798 exceed (10^{-6}), including 165/4,798 above (10^{-3}); log-shape distance has median (3.28\times10^{-7}), q90 0.279, q99 14.16, maximum 16.86.

This is not evidence that every such fit is a different global optimum: the likelihood can be nearly flat in concentration. It does establish that the existing B1 record did not directly reconcile the production fit with the analytic-gradient audit fit, and that M10/R5 has a substantial parameter/likelihood ridge requiring explicit treatment.

## 4. M10/R5: direct evidence of a near-binomial concentration ridge

Stratifying the existing M10/R5 records by the production C5 fitted concentration (sum of the candidate-provenance `fit_alpha` and `fit_beta`) shows:

- In the top fitted-concentration decile, the median production κ is approximately 5,561 (calibration) and 5,468 (validation), far above the DGP truth κ=4.
- In the corresponding analytic-gradient audit, the top-decile median profile curvature is approximately (1.4\times10^{-7}) / (9.3\times10^{-8}), and the median profile log-likelihood advantage over the binomial limit is approximately (1.4\times10^{-6}) / (9.3\times10^{-7}).
- The analytic-gradient audit reaches its upper numerical concentration bound in 210/4,822 and 189/4,798 interior production-fit records, respectively.

This is a near-flat concentration profile adjacent to the binomial limit. The data do not meaningfully distinguish a broad range of large concentrations in this stratum. The profile curvature and boundary likelihood comparison provide the likelihood evidence; the high point estimate alone would not be enough.

The same top production-κ decile has C5 coverage:
- calibration: within 93.1%, raw-between 89.4%;
- validation: within 92.1%, raw-between 91.0%.

Matched C0 coverage on exactly those datasets is 100% for both targets in both banks. C5 median interval widths are materially narrower in this stratum (about 0.100 within and 0.097 raw-between) than C0 (about 0.140 and 0.137). The C5 miss direction is predominantly lower-end misses for within and upper-end misses for raw-between.

At the other end of the fitted-κ distribution, C5 substantially improves on C0's poor low-κ coverage. The aggregate M10/R5 C5 overcoverage therefore masks sharply heterogeneous conditional behaviour: some fitted-parameter strata overcover, while the near-binomial/high-κ tail undercovers. A single aggregate coverage percentage conceals this structure.

## 5. M30/R20: high-κ tail undercoverage is not the same weak-identification signature

Stratifying by the production C5 fitted concentration:

- The top decile has median κ approximately 7.625 (calibration) and 7.709 (validation), versus DGP truth κ=4.
- Its analytic-gradient profile curvature remains materially negative (median approximately -7.9 / -7.8), and its median profile log-likelihood advantage over the binomial limit is approximately 17.6 / 17.2. This is not the near-flat binomial-limit ridge seen in M10/R5.
- In that top decile, C5 coverage collapses:
  - calibration: within 50.0%, raw-between 35.6%;
  - validation: within 50.8%, raw-between 35.0%.
- Matched C0 coverage in the same datasets remains 97.8%/96.8% calibration and 97.6%/95.8% validation.
- C5 intervals are narrower: median widths approximately 0.0363 within and 0.0361 raw-between, versus C0 approximately 0.0434 and 0.0432.
- Misses are directional: within misses are almost entirely below the lower endpoint (50.0% / 49.2%); raw-between misses are predominantly above the upper endpoint (64.4% / 65.0%).

This is a strong diagnostic association between high fitted concentration and plug-in C5 undercoverage, but it does **not** prove that high concentration itself causes the failure. The strata are selected post-fit and are exploratory. The profile is not nearly flat in the same way as the M10/R5 upper tail. The next diagnosis must therefore separate (a) M10/R5 weak concentration identification and optimizer ridge behaviour from (b) M30/R20 high-κ conditional bootstrap miscalibration.

## 6. What B3 does and does not establish

B3's B=1,000 versus B=4,000 endpoint changes remain modest on the selected datasets. This is consistent with the observed coverage failures not being a simple finite-B Monte Carlo-noise problem. B3 does not evaluate uncertainty in the fitted α/β parameters, does not resolve concentration identification, and does not repair the plug-in distributional approximation. Increasing B again is not the next operation.

## 7. Coordinated next work — static implementation and deterministic tests

The next operation is **not** replay and not another K/B run. It is a bounded static B1 reconciliation and diagnostic-control package:

1. Add a per-dataset reconciliation record that explicitly compares the C5 production fit (finite-difference L-BFGS-B) with the analytic-gradient L-BFGS-B fit: log-likelihood difference, log-μ difference, log-κ difference, α/β differences, both score vectors, Hessian/profile curvature, all three start outcomes, and distances to bounds. Keep raw values; do not invent an acceptance tolerance.
2. Separate optimizer termination status from numerical fit agreement. Preserve the original status for historical traceability; add a descriptive diagnostic status that cannot itself turn an unresolved BFGS run into a PASS or change C5 interval emission.
3. Add deterministic fixtures for: (i) M30-like near-identical solutions with BFGS precision-loss termination; (ii) M10-like concentration ridge approaching the binomial limit; (iii) genuine optimizer disagreement; and (iv) upper concentration boundary contact. Cross-check the analytic score/Hessian against central finite differences and the exact beta-binomial likelihood/oracle on those fixtures.
4. Reconcile whether the independent BFGS check needs a genuinely distinct initialization or a bounded/multistart alternative. The current same-solution initialization is only a local coordinate/termination check; do not describe it as a global independent optimizer.
5. Separately investigate the C5 interval construction in the high-κ tail. The existing C5 bootstrap is conditional on the fitted α/β pair; do not assume B=4,000 addresses uncertainty in those fitted parameters. Compare candidate interval behaviour to the matched C0 on the same existing data, but do not select or tune a replacement from these banks.
6. Only after the deterministic/static package is complete should a new versioned method-design decision consider a different interval construction (e.g. a likelihood/profile-based method or a method that explicitly propagates concentration-estimation uncertainty). Any future development bank must use fresh disjoint seeds and a new authorization. These B2/B3 banks remain development evidence only.

### Explicit non-actions

- No replay of run `44615173745` now.
- No rerun of B2/B3, no increase in K or B, no new simulation.
- No modification of the frozen v1.0 specification or original Tier A data.
- No retroactive change to the failed C5 adjudication.
- No promotion of C0 as a validated replacement.
- No Tier B, F1 A2/A3, comparative holdout or C10 causal execution.

## 8. Current disposition

**B2/B3 execution and primary artifact integrity:** PASS / AUDITED.  
**C5 frozen component gates:** FAIL (0/8).  
**C0 comparator frozen component gates:** FAIL.  
**F5 concentration identification:** M10/R5 contains a demonstrable near-binomial weak-identification ridge in the high-κ tail; M30/R20 shows a distinct high-κ conditional coverage failure.  
**Independent optimizer audit:** current unresolved status mixes BFGS termination failure with substantive M10/R5 fit-path divergence; B1 reconciliation is incomplete.  
**Replay:** deferred because it does not address these scientific/methodological failures and would consume approximately 2.6 hours.  
**Next gate:** static B1 reconciliation + deterministic adversarial controls + C5 interval-method diagnosis; no numerical execution authorized.
