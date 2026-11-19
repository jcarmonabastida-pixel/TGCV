# C10-S — Post-holdout integrated F1/F5 development and calibration specification

**Record:** C10S-POST-HOLDOUT-F1-F5-DEVELOPMENT-CALIBRATION-SPEC-001  
**Version:** 1.0  
**Status:** DESIGN FROZEN FOR IMPLEMENTATION / NUMERICAL EXECUTION NOT AUTHORIZED  
**Date:** 2026-11-19  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Input evidence:** `C10S_NESTED_MR_COMPARATIVE_HOLDOUT_AUDIT_001.md`  
**Prior design reused:** `C10S_NESTED_MR_CALIBRATION_COMPARISON_DESIGN_001.md`  
**Method reviews reused:** `C10S_F1_PROFILE_LIKELIHOOD_STATIC_REVIEW_001.md`; `C10S_F5_FITTED_BETA_BINOMIAL_STATIC_REVIEW_001.md`  
**Execution authorization:** NONE

---

## 1. Purpose and decision

This specification freezes one integrated **development/calibration work package** responding to the completed Tier A v1.0 result. It defines the numerical diagnostics and candidate calibration work required before a later, genuinely independent confirmatory holdout can be designed.

The work package has two distinct scientific-method tasks:

1. **F1 raw-between:** evaluate the already implemented F1 constrained profile-likelihood candidate as a less conservative alternative to C1's Bonferroni/joint-pivot raw-between interval; calibrate its likelihood-ratio cutoff prospectively on a development bank and assess it on a separate development-validation bank.
2. **F5 within/raw-between:** diagnose why the existing fitted beta-binomial C5 procedure changes from overcoverage at M10/R5 to undercoverage at M30/R20. Separate likelihood identification, optimizer failure, boundary behaviour and finite-bootstrap endpoint variability. C5 is not silently replaced; no new F5 interval method is selected in this work package.

This is **not** a rerun or amendment of the original Tier A, not a new confirmatory holdout, not Tier B, and not the C10 causal Generator/Analyzer/Evaluator experiment. The unblinded Tier A data are historical development evidence only and are excluded from all new denominators, tuning and calibration samples.

## 2. Historical reconciliation and reuse

The following existing assets are reused; no parallel estimator/oracle is to be recreated:

- Frozen C0/v002 two-stage cluster bootstrap adapter in `c10s_nested_mr_comparative_inference_engine.py`.
- F1 C1 exact within pivot and conservative joint-pivot raw-between interval in `c10s_f1_exact_pivotal_candidate.py`.
- F1 raw-between profile-likelihood candidate in `c10s_f1_between_profile_likelihood.py`, method ID `F1_BETWEEN_PROFILE_LIKELIHOOD_0.2`.
- F1 Gaussian reference/oracle in `c10s_gaussian_variance_oracles.py`.
- F5 fitted beta-binomial percentile candidate in `c10s_fitted_beta_binomial_bootstrap.py`.
- F5 exact finite-R count PMF and finite-M moment oracle in `c10s_beta_binomial_variance_oracles.py`.
- Common immutable input/result contract, matched-data adjudicator and fixture generator already referenced by the existing comparative engine contract.

The executed Tier A v1.0 protocol, its raw artifact, replay, adjudication, and authorization are immutable. The original v002 run is also immutable. No data from either execution may be reused as a simulation replicate, optimizer fixture for tuning, cutoff-calibration observation, or later confirmatory denominator. Fixed examples may be used only as labelled regression fixtures for deterministic software tests, not as empirical calibration data.

## 3. Frozen scientific invariants

All methods must preserve:

- F1 scope: balanced Gaussian random-intercept model only.
- F5 scope: independent world probabilities (p_m\sim\mathrm{Beta}(\alpha,\beta)), followed by (R) Bernoulli contributions conditional on each (p_m).
- The original cell parameters and designs listed in §4.
- The raw between-world estimand. Negative raw estimates and interval endpoints remain admissible and are never truncated, clipped, discarded or replaced by a positive-only conditional distribution.
- Identical datasets, truths and target design for all matched methods within a cell.
- Separate F1 and F5 adjudication. No cross-family pooling or cell averaging to rescue a failure.
- Truth is generated independently from candidate fitting and interval construction. Oracle parameters are never passed to a fitted candidate.
- Typed abstention for non-identification, boundary solution, optimizer failure, non-finite values or unresolved numerical topology. No silent fallback to C0/C1/C5.
- Separate reporting of conditional coverage, unconditional usable-and-covering rate, interval emission, lower/upper misses, width, bias/RMSE, convergence and computational cost.

For the primary component targets:
[
\widehat{\sigma_w^2}=MSW,\qquad
\widehat{\sigma_{b,raw}^2}=S^2_{\bar q}-MSW/R.
]
The raw between target remains (sigma_b^2), constrained to be nonnegative in the F1 likelihood parameter space but not truncated in the observed estimator or its scored interval target.

No MCSE method is introduced or promoted here. F5 MCSE remains the existing explicit abstention. F1 MCSE is out of scope for this package.

## 4. Frozen development cells and truth

Use exactly the eight regular Tier A cell definitions, but with new independent seed namespaces:

| Cell family | DGP parameters | Input/target design |
|---|---|---|
| F1 balanced | (sigma_w^2=1, sigma_b^2=1) | M10/R5; M30/R20 |
| F1 low-between | (sigma_w^2=1, sigma_b^2=0.05) | M10/R5; M30/R20 |
| F1 high-between | (sigma_w^2=0.25, sigma_b^2=2) | M10/R5; M30/R20 |
| F5 beta22 | (alpha=2, beta=2) | M10/R5; M30/R20 |

For F5 beta22 the independent oracle truth is (sigma_w^2=0.20), (sigma_b^2=0.05), and observed world-mean variance (0.20/R+0.05), as already defined by the oracle. No new stress family, Tier B cell, sparse Bernoulli family or misspecified mixing family is added to this bounded package. Such extensions require a later design decision.

The target design is ((M^*,R^*)=(M,R)) for every cell. The primary estimands in this package are within and untruncated raw-between only.

## 5. Frozen work-package phases

### Phase A — F1 profile-likelihood numerical certification and cutoff calibration

**Candidate:** existing `F1_BETWEEN_PROFILE_LIKELIHOOD_0.2`. C0 and C1 remain matched comparators. C1 within remains unchanged and is not retuned.

A1. **Deterministic numerical certification (before Monte Carlo):**
- Enforce an explicit F1 balanced Gaussian model-scope guard at the adapter boundary.
- Integrate the existing nuisance score-polynomial/stationary-root diagnostic into the profile evaluation path as a fail-closed check; unresolved tangential roots, unresolved critical points, boundary-sensitive disagreement or optimizer/root discordance must abstain.
- Independently evaluate the nuisance score and profile log-likelihood, checking stationary-root classification and the selected global candidate against an independent score/likelihood calculation.
- Inspect the LR acceptance set over the full admissible nonnegative between-variance axis using adaptive bracketing and topology checks. If disconnected components cannot be excluded or reliably represented, return a typed topology abstention; do not return a single interval by assumption.
- Retain zero-boundary inclusion, one-sided/unbounded status, endpoint brackets, scale equivariance, root residuals and every failure reason.
- Add adversarial deterministic contracts: zero and near-zero raw between; near-zero within sum; low/high variance ratios; multiple and tangential nuisance roots; near-degenerate score polynomials; search-boundary contact; extreme scale equivariance; lower-bound inclusion; upper-bracket expansion/overflow; disconnected or unresolved LR sets; invalid/non-F1 scope.
- No numerical calibration or coverage claims arise from these deterministic contracts.

A2. **Calibration bank:**
- (K_{cal}=5,000) independent datasets per each of the six F1 cells.
- Evaluate the profile LR statistic at the known true (sigma_b^2) using only the observed data and the F1 likelihood; the true value is used only to calculate the calibration statistic, never in candidate fitting or interval inversion.
- Calibrate one cutoff for each input design (M10/R5 and M30/R20), taking the least-favourable upper tolerance limit across the three declared variance regimes for that design.
- Use the nonparametric one-sided 95%-confidence upper tolerance order statistic for the 95th percentile: choose the smallest rank (k) for which (P\{\mathrm{Binomial}(K_{cal},0.95)\leq k-1\}\geq0.95). The cutoff is the maximum of the three regime-specific (k)-th order statistics. Record exact ranks and values.
- This is explicitly a least-favourable calibration over the six declared F1 parameter/design cells only. It is not a continuous-parameter uniform-coverage theorem.

A3. **Independent development-validation bank:**
- (K_{val}=5,000) fresh datasets per each of the six F1 cells, generated from a disjoint seed namespace.
- Apply the two frozen design-specific cutoffs without retuning.
- Compare C0, unchanged C1 and profile-likelihood candidate on the same dataset IDs.
- Report conditional coverage, 95% Wilson interval, coverage MCSE, interval emission, unconditional usable-and-covering rate, lower/upper misses, mean/median/quantile width, raw negative point-estimate frequency, boundary inclusion, topology/optimizer abstention, endpoint residuals and runtime.
- The profile candidate is eligible for a later confirmatory protocol only if every one of the six raw-between cells satisfies the strict component gate in §8, all deterministic numerical contracts pass, and no unresolved topology/global-maximum state remains. No family-level averaging is permitted.

### Phase B — F5 likelihood identification, optimizer and C5 calibration diagnosis

**Candidate:** existing `C5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0`. C0 remains the unchanged matched comparator. No alternative F5 interval is invented or selected in this package.

B1. **Per-dataset likelihood/optimizer audit:**
- For each F5 calibration/validation dataset, retain all existing three-start L-BFGS-B outcomes, not just the selected successful fit: start vector, convergence flag, message, objective, fitted coordinates, gradient norm and distance to each numerical bound.
- Implement an independent analytic score in mean-logit/log-concentration coordinates and an independently coded Hessian or observed-information calculation; cross-check scores/Hessian behaviour against central finite differences on interior and boundary-adjacent deterministic fixtures.
- Compare the accepted fit with a separately parameterized independent optimizer. Record objective differences, score norms and parameter disagreement; optimizer success flags alone do not establish an admissible global MLE.
- Evaluate the two extended concentration limits explicitly: (kappa\to\infty) (binomial limit) and (kappa\to0) (two-point mixing limit). Compare their limiting likelihoods with finite interior fits. A finite numerical cap is not itself a statistical boundary solution.
- Classify outcomes distinctly as interior identified fit, boundary-dominated/weakly identified fit, optimizer disagreement, numerical failure or non-identification. Do not label a high concentration fit a bug without likelihood evidence.
- Reconcile fitted likelihood and finite-R distribution against the independent beta-binomial count PMF/moment oracle; oracle parameters remain withheld from the fit.

B2. **Matched C5/C0 development comparison:**
- (K=5,000) fresh datasets in each of the two F5 beta22 cells.
- For C0 retain the frozen v002 bootstrap (B=1,000); for C5 retain the existing fitted parametric bootstrap (B=1,000). No B/K tuning on these banks.
- Report all metrics listed in §5 A3, including fit-status frequencies, (hat\mu), (hat\kappa), (hat\alpha), (hat\beta), log-likelihood, score/curvature, boundary distance, typed abstention, conditional/unconditional coverage, emission, tails, width and point-estimate bias/RMSE.
- Interpret M10/R5 and M30/R20 separately. The purpose is to identify whether the holdout pattern is associated with weak identification, optimizer selection, finite-B variability, or another measured mechanism. The design does not assume any one explanation.

B3. **Endpoint Monte Carlo error sub-study:**
- Select 250 datasets per F5 cell by a deterministic hash rule from the new Phase B calibration bank, before examining their C5 outcome.
- On those fixed datasets, compare independently seeded C5 bootstrap runs at (B=1,000) and (B=4,000), with separate recorded streams.
- This sub-study is diagnostic only. The B=4,000 intervals do not replace the B=1,000 primary comparison, do not enter coverage adjudication, and cannot be used to retroactively alter the frozen Tier A protocol or this package's primary B.
- Report endpoint rank uncertainty, endpoint-value variability and interval-width changes. Do not use positive-only bootstrap projections for any target.

## 6. Replication, RNG and data separation

All new simulations use the existing PCG64 generator/fixture contracts where compatible, with a new immutable seed schedule identifier:

`C10S_POST_HOLDOUT_F1_F5_DEV_CAL_SEEDS_1.0`

Required disjoint namespaces:

- `f1_profile_calibration_dataset`
- `f1_profile_validation_dataset`
- `f1_profile_calibration_auxiliary`
- `f5_optimizer_calibration_dataset`
- `f5_optimizer_validation_dataset`
- `f5_c0_bootstrap`
- `f5_c5_bootstrap`
- `f5_endpoint_sensitivity_b1000`
- `f5_endpoint_sensitivity_b4000`

Seed derivation must include schedule version, namespace, cell ID and replicate index. All generated dataset IDs, seeds, bootstrap seeds and source/code identities must be written to the run manifest. A collision check against the original Tier A and executed v1.0 comparative holdout seed namespaces is a hard precondition.

The calibration and validation banks are both **development data**. Validation here means independent assessment of the calibrated development candidate, not confirmatory evidence. Because both banks are inspected during method development, neither can serve as the later confirmatory holdout. A future holdout must use a new protocol, new seed namespace, fresh data and a separate one-use authorization.

## 7. Resource preflight and execution order

Before full K:
1. Complete static implementation and tests for A1 and B1.
2. Run the static-only suite under a research-branch workflow; verify exact tested commit and dependency lock.
3. Conduct a bounded resource preflight using 100 datasets per representative F1 and F5 cell, with the specified bootstrap counts. The preflight is not included in K, cannot be used for coverage adjudication and has a separate seed namespace.
4. Record runtime, peak memory, failure modes and projected full-run cost. If the projected run exceeds the predeclared available execution budget, STOP and return a revised design for review; do not reduce K/B or drop cells autonomously.
5. Only after the preflight passes may the one-use execution authorization cover the full development/calibration banks.

The authorized numerical operation, if later approved, is limited to Phases A2–A3 and B2–B3 plus their required preflight. It does not include Tier B, any new stress family, F5 MCSE, or C10 scientific execution. Phase A1/B1 implementation and deterministic tests must already be complete before authorization is requested.

## 8. Frozen development acceptance and interpretation rules

For the F1 profile candidate raw-between and the F5 C5 within/raw-between comparisons, retain the strict criteria used by the completed Tier A adjudication:

- Conditional coverage in ([0.93,0.97]).
- Two-sided 95% Wilson interval contains 0.95.
- Interval emission at least 0.95 of K.
- No unresolved truth/denominator/method-roster mismatch, non-finite interval, untyped abstention or raw-between truncation.
- All cells pass separately; no pooling or averaging.

These are **development eligibility gates**, not a confirmatory scientific acceptance claim. The F1 profile calibration bank is used to determine its LR cutoff; only the disjoint development-validation bank is used to assess the selected cutoff. C0/C1/C5 results remain comparators and are not reselected or modified.

For the F1 profile method, overcoverage above 97% is a failure under this strict efficiency/calibration gate; do not relabel it as acceptable merely because it is conservative. Width is reported as a secondary efficiency diagnostic and cannot compensate for a coverage failure.

For F5, a successful optimizer fit is not itself a coverage pass. C5 can be eligible only if both M/R cells pass both components and the optimizer/identifiability diagnostics have no unresolved numerical state. If it fails, record `NO_VALIDATED_F5_COMPONENT_INTERVAL_METHOD`; do not improvise a replacement in this execution.

## 9. Required output artifacts

The implementation/execution package must produce:

1. This frozen specification, unchanged after authorization.
2. A static implementation and adversarial-test record for A1/B1.
3. A resource-preflight record and JSON with exact code/dependency identities.
4. A one-use authorization manifest bound to exact protocol/code/workflow/dependency hashes.
5. Immutable calibration and validation dataset manifests with complete seed inventories.
6. Per-cell raw records and checkpoints, separately for calibration and validation.
7. F1 profile cutoff calibration record, including all cell quantiles, selected order-statistic ranks, least-favourable cutoff per M/R and calibration-bank digests.
8. F1 topology/nuisance optimizer diagnostics and profile interval outputs.
9. F5 per-fit likelihood/score/Hessian/optimizer/boundary diagnostics, with all starts retained.
10. F5 C0/C5 comparison records and B=1,000/B=4,000 endpoint sensitivity records.
11. Independent adjudication JSON and human-readable report, including every denominator, Wilson interval, emission rate, tail miss, width, abstention and runtime.
12. Exact replay of the full development execution under the same frozen code/inputs/definitions, with deterministic digest equality. Replay is a computational-integrity check, not a new independent statistical sample.
13. A final audit record separating execution integrity, development eligibility and remaining confirmatory work.

No original Tier A artifact, manifest, result or protocol may be edited in place.

## 10. Stop conditions

Stop the affected phase and do not silently continue if any of the following occurs:

- seed collision with any previous Tier A/v1.0 execution;
- source/code/dependency/protocol hash mismatch;
- F1 unresolved nuisance stationary root, score-polynomial ambiguity, boundary-sensitive optimizer disagreement, unbracketed endpoint, unresolved LR topology or inability to represent disconnected components;
- F5 independent score/Hessian disagreement, optimizer disagreement without an admissible likelihood comparison, unexplained boundary dominance, non-finite likelihood or oracle mismatch;
- missing/duplicate dataset IDs, method roster mismatch, truth mismatch, denominator drift or non-deterministic replay;
- untyped abstention, hidden deletion, positive-only conditioning or raw-between clipping;
- resource preflight indicates the frozen K/B cannot be completed within the available execution budget.

A stopped phase is reported as BLOCKED/INDETERMINATE with raw diagnostics preserved. No K/B reduction, threshold change, cell deletion or method substitution is allowed without a new versioned design and explicit approval.

## 11. Explicit exclusions and non-claims

This specification does not authorize or define:
- Tier B;
- C10-S Generator, Analyzer or Evaluator execution;
- causal estimation of (Delta T_{acc}\to\Delta V) or Value;
- F5 MCSE interval construction;
- Gaussian inference applied to F5;
- C2, C3 or C4 implementation/evaluation;
- new DGP families, misspecification generalization or external/real datasets;
- modification of protocol v002, the completed comparative holdout v1.0, production Analyzer, canonical `main`, RMA, Evidence→Claim Matrix or scientific claim status.

**Final design disposition:** the scope, cells, methods, replication counts, seed namespaces, numerical controls, acceptance gates, stop rules and required artifacts above are frozen for implementation. Numerical execution remains unauthorized. A separate one-use authorization may be requested only after A1/B1 implementation, deterministic tests, static workflow validation and resource preflight are complete and their exact identities are verified.
