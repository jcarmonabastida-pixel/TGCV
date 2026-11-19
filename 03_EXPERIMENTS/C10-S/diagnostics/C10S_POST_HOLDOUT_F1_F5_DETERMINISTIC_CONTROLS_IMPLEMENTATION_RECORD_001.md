# C10-S — Post-holdout F1/F5 deterministic controls implementation record

**Record:** C10S-POST-HOLDOUT-F1-F5-DETERMINISTIC-CONTROLS-IMPLEMENTATION-001  
**Date:** 2026-11-19  
**Status:** PARTIAL IMPLEMENTATION / 119-TEST STATIC SUITE PASS / NUMERICAL DEVELOPMENT EXECUTION NOT AUTHORIZED  
**Frozen design:** `C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md` v1.0  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Initial implementation commit:** `e7920543e8c6fb19582c62446381df7cb1d95e1a`  
**Latest validated commit:** `b7127b29db6e2a2a6f6c2bfdc8f998a5014f694e`  
**Execution authorization:** NONE

---

## 1. Scope and disposition

This record documents the first implementation increment for deterministic controls A1 (F1 profile likelihood) and B1 (F5 beta-binomial likelihood/optimizer audit) under the frozen post-holdout development specification.

The increment is limited to software-level deterministic calculations and tests on fixed fixtures. It did **not** generate DGP datasets, run Monte Carlo calibration/validation banks, bootstrap comparison banks, endpoint sensitivity experiments, Tier A/B, or the causal C10 Generator/Analyzer/Evaluator experiment.

The latest static workflow passed. This establishes that the listed source compiles and the declared software-contract suite passes on the exact commit. It does not establish coverage, estimator calibration, empirical eligibility, or scientific acceptance.

## 2. F1 — profile-likelihood controls implemented

Source:
- `harness/c10s_f1_between_profile_likelihood.py`
- `harness/test_c10s_f1_between_profile_likelihood.py`

Implemented controls:

1. The confidence-set callable now requires an explicit `family="F1"`; non-F1 dispatch is rejected.
2. Each profile evaluation invokes the existing nuisance optimizer/root diagnostic and the exact-rational score-polynomial root isolator.
3. All isolated positive nuisance stationary roots are evaluated; the independent score sign is checked on the monotone polynomial partitions.
4. The bounded scalar optimizer is compared with the likelihood at the isolated stationary-root maximum. A discrepancy above the frozen numerical tolerance, unresolved root/tangency, optimizer boundary state, non-finite value or non-unique local nuisance maximum causes typed abstention.
5. The search span and diagnostic grid adapt to the ratio between the variance scale and within variance. Excessive required range fails closed.
6. The profile result records nuisance-certification and topology status.
7. The connectedness argument is documented in the callable: by the envelope derivative, an interior stationary point of the profiled likelihood requires (q^*=S^2_{\bar Y}); substituting into the nuisance score gives (s^*=MSW) and (\tau^*=S^2_{\bar Y}-MSW/R). Hence, conditional on the unique certified nuisance maximum and continuity, there is at most one interior stationary point in (\tau>0), and the LR acceptance set is connected.

Deterministic tests include explicit family rejection, root inversion, endpoint LR equations, zero-boundary inclusion, extreme-cutoff fail-closed behaviour, scale equivariance, polynomial roots, tangential/near-tangential score cases, and critical-point solver adversarial cases.

**F1 disposition:** deterministic control path implemented and tested for current fixtures. It is not yet eligible for calibration. The six frozen F1 cell regimes and additional adversarial nuisance/topology cases still require a systematic fixture matrix and independent review of the analytical connectedness argument.

## 3. F5 — analytic likelihood and optimizer audit implemented

Source:
- `harness/c10s_f5_beta_binomial_likelihood_diagnostics.py`
- `harness/test_c10s_f5_beta_binomial_likelihood_diagnostics.py`

Implemented controls:

1. Analytic beta-binomial log-likelihood, score and Hessian in mean-logit/log-concentration coordinates.
2. Deterministic central finite-difference comparisons for both score components and the full Hessian.
3. Explicit likelihood evaluations for the extended limits (\kappa\to\infty) (binomial) and (\kappa\to0) (two-point mixing), including the zero-probability state for interior counts under the latter.
4. A deterministic optimizer audit that retains every declared bounded L-BFGS-B start, including success/message, final coordinates, objective, gradient norm and distance to each numerical bound.
5. An independently parameterized BFGS audit in ((\log\alpha,\log\beta)), recording objective difference, parameter distance, score norm and observed-Hessian eigenvalues.
6. The audit reports likelihood-concordant parameter disagreement separately from objective discordance and optimizer non-convergence; it does not silently rewrite the existing C5 fit selection.

Deterministic tests cover derivative agreement, Hessian symmetry/finiteness, input guards, both extended likelihood limits, the high-concentration/binomial limit and retention of all optimizer starts plus the independent fit audit.

**F5 disposition:** deterministic likelihood and optimizer-audit primitives implemented and tested. The audit helper is not yet integrated into the per-dataset C5 result/provenance path. The exact finite-R oracle crosswalk, boundary-adjacent derivative fixtures, and diagnostic status propagation into C5 records remain open.

## 4. Static validation

Workflow:
`.github/workflows/c10-s-nested-mr-calibration-comparator-static.yml`

Run:
- ID: `44582807370`
- Commit: `e7920543e8c6fb19582c62446381df7cb1d95e1a`
- Conclusion: `SUCCESS`
- Compile step: PASS
- Test step: PASS
- Test modules: existing comparator/oracle/runner contracts plus F1 profile-likelihood and F5 likelihood-diagnostic modules
- Result: **110 tests passed**

The workflow used the repository's hash-locked dependencies. No DGP or bootstrap dataset bank was executed.

Other F1 numerical-stress workflows were triggered by branch pushes but their authorization conditions were false; their jobs concluded `SKIPPED`. No numerical-stress execution was performed.

## 5. Exact source identities at the validated commit

| Artifact | Git blob SHA |
|---|---|
| Frozen design v1.0 | `d1c8bae882dc2e4cd0e1caae29609561b9ebac68` |
| F1 profile source | `87de3f15468482327fa1170b050fdd54dac13ade5` |
| F1 profile tests | `81c42c6af743faca11df6aa4b8219e2ef6bb214a` |
| F5 likelihood/optimizer diagnostics | `7df6d4e679c909d79f4aa184918b75117f28f3c0` |
| F5 diagnostics tests | `3e54bc39cd36b4c24619354d031ef9e579f942a5` |
| Static workflow | `624370a438000809c7cc6b660fda126b77ced5de` |

The canonical branch head at validation was `e7920543e8c6fb19582c62446381df7cb1d95e1a`. `main` remained at `e22928eb79adb5bc74295967a45b9c440b78f849`.

## 6. Remaining implementation gates before resource preflight

### F1
- Build the frozen six-cell adversarial fixture matrix, including near-zero within sums, low/high between regimes and scale extremes.
- Add explicit multiple/tangential nuisance-root fixtures to the *interval-path* gate, not only the standalone polynomial diagnostic.
- Independently verify the score-polynomial and profile-likelihood identities against a separately coded likelihood/score oracle.
- Exercise boundary inclusion, endpoint bracketing/overflow and the connectedness argument over the full declared design roster.
- Preserve typed abstention for any mismatch.

### F5
- Integrate the optimizer audit into a separate diagnostic output for each fixed C5 fit without changing the existing interval calculation or C5 selection rule.
- Reconcile the fitted count likelihood and finite-R distribution with the existing exact beta-binomial PMF/moment oracle.
- Add boundary-adjacent score/Hessian tests and explicit weak-curvature/near-binomial cases.
- Ensure all starts and the independent optimizer result are serializable in the future per-dataset audit records.

### Shared
- Add static schema/manifest tests for diagnostic records and provenance.
- Re-run the static workflow on the final implementation commit and record exact hashes.
- Only then perform the bounded 100-dataset-per-representative-cell resource preflight under its own authorization.
- Do not request the 80,000-dataset development/calibration authorization until these gates and the resource preflight pass.

## 7. Prohibitions preserved

No Tier A v1.0 protocol, raw result, replay, authorization or audit was changed. No C0/C1/C5 interval definition was changed. No calibration cutoff was selected. No new method was promoted. No data from the unblinded Tier A holdout were reused. No scientific C10 execution was performed. No write was made to `main`.

**Final disposition:** A1/B1 deterministic implementation has advanced, with 110/110 static tests passing. The integrated development/calibration package remains OPEN and numerical execution remains unauthorized.


## 8. F5 per-dataset optimizer-audit integration — 2026-11-19

The next implementation increment closes the previously open per-dataset diagnostic propagation path.

### 8.1 Candidate result integration

`c10s_fitted_beta_binomial_bootstrap.py` now attaches the deterministic `BetaBinomialOptimizerAudit` to each `FittedBetaBinomialBootstrapResult`, including the fit-abstention and boundary-abstention returns.

- The three diagnostic L-BFGS-B starts are retained independently of the existing C5 fit.
- The independently parameterized BFGS result, likelihood difference, parameter distance, score norm, Hessian eigenvalues and extended-limit likelihoods remain available in the attached audit.
- A diagnostic failure is recorded separately as `optimizer_audit_error`; it does not select a different C5 fit, change its interval, or replace its existing abstention.
- The original C5 fitting/selection code and bootstrap calculation remain unchanged.

### 8.2 Per-dataset comparison persistence

`c10s_nested_mr_comparative_inference_engine.py` now serializes the complete audit into the F5 candidate's per-dataset diagnostics as `likelihood_optimizer_audit_json`. Extended-real likelihood limits are encoded as explicit strings (`"-Infinity"`, `"Infinity"`, or `"NaN"`) so the output is valid strict JSON and does not silently emit non-standard JSON numeric tokens.

The engine test parses this record and verifies that all three starts and the optimizer status survive the per-dataset comparison boundary.

### 8.3 Additional deterministic cross-checks

- The finite-R beta-binomial count likelihood is checked against the existing independent exact PMF oracle for every count in the support (0,ldots,R), using the frozen beta22 parameterization.
- Analytic score components are checked against central finite differences in low-concentration and near-binomial/high-concentration, mean-boundary-adjacent fixtures.
- Existing tests verify audit retention on the ordinary interior path and on all-zero/all-one typed abstention paths.

A static failure exposed that the audit received NumPy integer scalars while the reused extended-limit evaluator deliberately requires built-in integers. The audit now normalizes validated count scalars before invoking that evaluator. A second numerical guard ensures the independently parameterized optimizer gradient respects the objective's finite representability guard. Both issues were corrected before the passing validation below.

### 8.4 Latest static validation

Workflow:
`.github/workflows/c10-s-nested-mr-calibration-comparator-static.yml`

- Run ID: `44584027037`
- Exact commit: `469dbe52c9a7075e68506f2c58d754b7ea45dc58`
- Conclusion: `SUCCESS`
- Compile: PASS
- Hash-locked dependency installation: PASS
- Test suite: **112 tests passed**
- No DGP, calibration, validation-bank or bootstrap-bank execution was performed.

### 8.5 Exact identities at latest validation

| Artifact | Git blob SHA |
|---|---|
| Frozen development/calibration specification v1.0 | `d1c8bae882dc2e4cd0e1caae29609561b9ebac68` |
| F5 likelihood diagnostics | `363f9be9ad8ea71b6dd09a9ecb0dddb4319b9967` |
| F5 likelihood diagnostic tests | `fa1c21f96d843662643879af56803be4195b6e3f` |
| F5 fitted bootstrap candidate | `1052ed986e4a551654b9d32928937e4e39df2c88` |
| F5 fitted bootstrap tests | `4b7e70b59b99ddb6ed6fdd767d38e31096d0cdaa` |
| Comparative inference engine | `5aa04ba4add1c7c6293e3d27bf0360b400e7eed4` |
| Comparative inference engine tests | `20481d051e4d6986991398c260cbb14fa2ef9118` |
| Static workflow | `624370a438000809c7cc6b660fda126b77ced5de` |

The validated research branch head was `469dbe52c9a7075e68506f2c58d754b7ea45dc58`. The frozen specification remained byte-identical at the blob SHA above. `main` remained at `e22928eb79adb5bc74295967a45b9c440b78f849`.

**F5 disposition update:** the per-dataset optimizer audit is now implemented and propagated through the in-memory result and comparison diagnostic record. It remains a diagnostic, not an interval-selection rule or empirical finding. The development/calibration package remains OPEN because the six-cell F1 adversarial interval-path matrix and remaining F5 weak-identification/boundary fixture work are not yet complete.


## 9. F1 frozen six-cell deterministic interval-path matrix — 2026-11-19

A deterministic fixture matrix has now been added to `test_c10s_f1_between_profile_likelihood.py`.

It generates fresh Gaussian random-intercept fixtures using PCG64 for each of the six frozen combinations:
- balanced: ((\sigma_w^2,\sigma_b^2)=(1,1)), M10/R5 and M30/R20;
- low-between: ((1,0.05)), M10/R5 and M30/R20;
- high-between: ((0.25,2)), M10/R5 and M30/R20.

Each fixture is sent through the actual F1 profile confidence-set path with the same explicit diagnostic LR cutoff. The contract checks data shape/finiteness and then requires either a valid ordered nonnegative interval containing the profile MLE or a typed `F1ProfileError` abstention. Unexpected exceptions or malformed intervals fail the suite.

These are deterministic software fixtures only. They are not Monte Carlo replicates, calibration observations, coverage evidence, or a substitute for the six-cell A2/A3 banks. The matrix does not yet exhaust the separately frozen multiple/tangential-root, near-degenerate, extreme endpoint and independent-oracle cases at the interval-path boundary.

### Latest static validation after the F1 matrix

- Workflow run: `44584274490`
- Exact commit: `601610465e2374b700f58dd8d7acbcf7a7b0b837`
- Conclusion: `SUCCESS`
- Compile: PASS
- Hash-locked dependency installation: PASS
- Test suite: **113 tests passed**

The two numerical-stress workflows associated with this push were `SKIPPED` by their authorization conditions; no numerical-stress or scientific execution was performed.

### Additional exact identity

| Artifact | Git blob SHA |
|---|---|
| F1 six-cell interval-path fixture test module | `338e1fe193231260dd695f96c20077b87b58613b` |
| F1 profile-likelihood implementation | `87de3f15468482327fa117b050fdd54dac13ade5` |

The validated research branch head was `601610465e2374b700f58dd8d7acbcf7a7b0b837`; `main` remained at `e22928eb79adb5bc74295967a45b9c440b78f849`. The frozen specification remains unchanged at `d1c8bae882dc2e4cd0e1caae29609561b9ebac68`.

**Current disposition:** F5 per-dataset optimizer diagnostics are now propagated into the dataset comparison record. The six frozen F1 cell designs are exercised by deterministic interval-path fixtures. The integrated A1/B1 work package is still OPEN: further F1 adversarial interval-path and independent-oracle verification, plus F5 weak-identification/boundary classification and diagnostic schema/provenance checks, remain before the resource preflight gate. No numerical development execution is authorized.


## 10. F1 interval-path fail-closed propagation for unresolved roots — 2026-11-19

Two deterministic integration contracts were added to the actual F1 profile confidence-set entry point.

1. **Unresolved tangential nuisance-score candidate:** the test retains a real data fixture and its actual polynomial diagnostic, injects an optimizer/score-scan diagnostic carrying one unresolved tangential candidate, then calls `f1_profile_between_confidence_set`. The interval path must raise `F1ProfileError` with `PROFILE_NUISANCE_CERTIFICATION_FAILED` and preserve the unresolved count in the reason.
2. **Unresolved polynomial critical-point isolation:** the test retains the actual polynomial coefficients/roots from the fixture but changes the critical-point solver status to an unresolved state. The interval path must again abstain with `PROFILE_NUISANCE_CERTIFICATION_FAILED`, rather than returning a confidence interval.

These are deliberately *fault-injection integration tests*: they verify that the interval inversion boundary propagates adverse diagnostic states fail-closed. They do not claim that the fixture itself naturally generates a multiple/tangential root, nor do they establish coverage or empirical frequency of such cases. The separate algebraic root-isolation tests remain the evidence for the diagnostic primitive; construction of actual adversarial data whose score polynomial has a prescribed repeated root, and independent confirmation of that construction, remain OPEN.

### Static validation

- Workflow: `.github/workflows/c10-s-nested-mr-calibration-comparator-static.yml`
- Run ID: `44584915718`
- Exact commit: `1fa0a5831a8a4f89602d544ac6b4c69a5738106f`
- Conclusion: `SUCCESS`
- Hash-locked dependency installation: PASS
- Compile: PASS
- Test suite: **115 tests passed**
- F1 numerical-stress workflows on the same push: `SKIPPED` by authorization conditions; no numerical stress or simulation was run.

### Exact identities

| Artifact | Git blob SHA |
|---|---|
| F1 profile-likelihood implementation | `87de3f15468482327fa117b050fdd54dac13ade5` |
| F1 profile-likelihood tests | `288c80c540ab98d3569b1ea4f4db01e59f0d21f6` |
| Frozen development/calibration specification v1.0 | `d1c8bae882dc2e4cd0e1caae29609561b9ebac68` |

Validated research branch head: `1fa0a5831a8a4f89602d544ac6b4c69a5738106f`. Canonical `main` remained `e22928eb79adb5bc74295967a45b9c440b78f849`.

**Disposition:** the interval-path fail-closed propagation for unresolved tangency and unresolved polynomial critical-point isolation is now covered. The package remains OPEN: actual constructed repeated-root/near-degenerate interval fixtures, independent score/likelihood oracle cross-checks, remaining F5 weak-identification/boundary classifications, and shared diagnostic schema/provenance tests remain before resource preflight. Numerical development execution remains unauthorized.


## 11. F1 constructed repeated-root data fixture and interval-path integration — 2026-11-19

The previous unresolved item was not merely whether a synthetic polynomial could be made to have a repeated root; it was whether such a root could be realized by valid balanced-Gaussian nested data and observed by the existing F1 diagnostic path.

A deterministic (M=4,R=4) nested dataset has now been constructed by solving the score-polynomial double-root conditions (P(s_0)=0) and (P'(s_0)=0) for the within sum of squares and world-mean sample variance. The fixture uses:
- target between variance (	au=1);
- repeated positive nuisance-score root (s_0=1);
- (SSW=4.425);
- sample variance of world means (S^2_{\bar Y}=17.03125);
- four world means ((-a,-a,a,a)), with (a=\sqrt{3S^2_{\bar Y}/4});
- balanced within-world deviations proportional to ((-1.5,-0.5,0.5,1.5)), scaled to reproduce the specified (SSW).

For these sufficient statistics the cubic score numerator is, up to floating-point representation,
[
P(s)=-0.9375(s-1)^2(s-4.72).
]
This produces one genuine positive double/tangential root and one distinct simple positive root in the actual data-derived polynomial, rather than injecting a mocked diagnostic state.

Two tests were added:

1. The constructed rows pass through `f1_score_polynomial_diagnostic` and the independent nuisance diagnostic. The test requires the repeated root to be isolated and classified as `TANGENTIAL_STATIONARY_NO_LOCAL_EXTREMUM`, with zero unresolved tangential candidates.
2. The same rows are passed through `f1_profile_between_confidence_set`. The endpoint bracketing callback is instrumented to evaluate the actual profile callback at the constructed `tau=1` point before continuing with the genuine Brent endpoint solve. Polynomial root-isolation calls themselves are left untouched. The test requires the interval path to complete with its single connected component and the declared nuisance-certification status.

This establishes deterministic numerical-path behaviour for one *constructed exact-statistic repeated-root fixture*. It does not establish Monte Carlo frequency, coverage, robustness across the full frozen six-cell roster, or the independent score/likelihood oracle requirement. The separate near-degenerate, boundary-contact and multiple-scale interval fixtures remain OPEN.

### Static validation

- Workflow: `.github/workflows/c10-s-nested-mr-calibration-comparator-static.yml`
- Run ID: `44585584703`
- Exact commit: `c8d9706c0b3424a9ae59922593356c58694834bd`
- Conclusion: `SUCCESS`
- Hash-locked dependency installation: PASS
- Compile: PASS
- Test suite: **117 tests passed**
- F1 numerical-stress workflows v1/v2/v3: `SKIPPED` by authorization conditions; no numerical stress, DGP bank, calibration, validation or bootstrap simulation was run.

### Exact identities

| Artifact | Git blob SHA |
|---|---|
| F1 profile-likelihood implementation | `87de3f15468482327fa117b050fdd54dac13ade5` |
| F1 profile-likelihood tests and constructed fixture | `4c76a1dea0a898c568eb57c9adea51c53891fed3` |
| Frozen development/calibration specification v1.0 | `d1c8bae882dc2e4cd0e1caae29609561b9ebac68` |

Validated research branch head: `c8d9706c0b3424a9ae59922593356c58694834bd`. Canonical `main` remained `e22928eb79adb5bc74295967a45b9c440b78f849`.

**Disposition:** one actual repeated-root data construction now traverses the F1 polynomial diagnostic, nuisance classification and interval profile callback. A1 remains OPEN pending independent score/likelihood verification and the remaining frozen adversarial cases. B1/F5 weak-identification/boundary classification and shared schema/provenance checks also remain open. No resource preflight or numerical development execution is authorized.


## 12. Independent finite-difference likelihood oracle for the F1 score polynomial — 2026-11-19

Two further deterministic tests were added to close part of the independent-oracle requirement without invoking any simulation or calibration bank.

1. **Independent likelihood derivative cross-check.** The test reconstructs the balanced-Gaussian sufficient statistics directly from the raw rows using a separate implementation in the test module. It then evaluates the explicit nuisance log-likelihood formula and obtains its derivative with a central finite difference in \\(\log s\\). That numerical derivative is compared with the score recovered from the production score-polynomial coefficients, \\(P(s)/(2s(\tau+s/R)^2)\\), at six positive within-variance values for both an ordinary fixture and the constructed repeated-root fixture.
2. **Repeated-root derivative check.** At the constructed double score root, an independent central finite difference of the explicit likelihood verifies a zero derivative within the declared numerical tolerance.

The oracle does not call the production nuisance score, coefficient constructor, or production likelihood function. It does share the statistical model formula, as it must, but uses a separately implemented raw-row statistic reconstruction and finite-difference derivative. This is a numerical cross-check, not a formal proof of the likelihood identity or an independent external review.

### Static validation

- Workflow: `.github/workflows/c10-s-nested-mr-calibration-comparator-static.yml`
- Run ID: `44586276957`
- Exact validated code commit: `b7127b29db6e2a2a6f6c2bfdc8f998a5014f694e`
- Conclusion: `SUCCESS`
- Hash-locked dependency installation: PASS
- Compile: PASS
- Test suite: **119 tests passed**
- The separate F1 numerical-stress job for this push concluded `SKIPPED` under its authorization condition. No stress bank, DGP bank, Monte Carlo calibration, bootstrap simulation, resource preflight or scientific C10 execution was performed.

### Exact identities

| Artifact | Git blob SHA |
|---|---|
| F1 profile-likelihood implementation | `87de3f15468482327fa117b050fdd54dac13ade5` |
| F1 profile-likelihood tests and independent oracle | `2c775e89130284b016f320875b60df4bb08d3f5a` |
| Frozen development/calibration specification v1.0 | `d1c8bae882dc2e4cd0e1caae29609561b9ebac68` |

Validated code branch head: `b7127b29db6e2a2a6f6c2bfdc8f998a5014f694e`. Canonical `main` remained `e22928eb79adb5bc74295967a45b9c440b78f849`.

**Disposition:** the score-polynomial/likelihood derivative correspondence now has an independent deterministic finite-difference cross-check over ordinary and repeated-root fixtures. The F1 work remains OPEN for near-degenerate and boundary-contact interval-path cases and broader adversarial roster checks. F5 weak-identification/boundary classifications and shared schema/provenance checks also remain before the separately authorized resource preflight. Numerical development execution remains unauthorized.


## 9. F5 concentration-profile and stability audit propagation — 2026-11-19

The B1 concentration-profile audit is now integrated into the matched-dataset F5 comparison record through an explicit opt-in interface. A caller must provide the log-concentration grid; the engine does not infer a grid or range from the observed data.

Each enabled F5 dataset record carries separate strict-JSON profile and numerical-stability audit objects. The former preserves optimizer status, finite-grid profile maximum, nuisance-profiled extended-boundary likelihood comparisons and local profile curvature. The latter preserves paired profile/mean-logit/curvature differences across reference, refined and expanded nuisance-search controls. Both retain `INDETERMINATE` identification semantics; the stability record is `NUMERICAL_STABILITY_NOT_ADJUDICATED`.

The opt-in is deliberate: the three-trace stability comparison is materially more expensive than the existing C5 fit audit and must not be silently imposed on all 80,000 frozen development/calibration datasets. The caller can enable it for a governed diagnostic subset while leaving the frozen calibration path unchanged.

The deterministic engine tests verify:
- both audit objects cross the per-dataset comparison boundary and serialize as strict JSON;
- an explicit concentration grid is required;
- F5-only routing is enforced;
- enabling the new diagnostics leaves C5 within, raw-between and MCSE interval outputs unchanged.

Exact-commit validation: Run `44593339897`, commit `898906f2b5ee94c599a478991688cbe2e9333551`, hash-locked dependencies PASS, compilation PASS, **137 deterministic tests PASS**. Numerical-stress workflows v1/v2/v3 were skipped by their authorization guards. No DGP, calibration, bootstrap bank, resource preflight, holdout or scientific C10 execution occurred.

This is implementation/static-validation evidence only. It does not establish concentration identification, repair the observed C5 coverage failures, select a replacement interval, or support a causal `Delta T_acc -> Value` claim. The frozen development/calibration specification v1.0 and all C5 interval/selection logic remain unchanged.


## 10. B1 adversarial per-dataset profile-audit propagation — 2026-11-19

Added deterministic tests at the comparison-engine boundary for three adversarial conditions:

- Missing optimizer audit: the concentration profile object is explicitly `null` with `F5LikelihoodDiagnosticError:OPTIMIZER_AUDIT_UNAVAILABLE`; the independent stability trace remains available and serializable.
- Finite two-point boundary: endpoint-only world counts preserve `FINITE_ENDPOINT_MIXTURE_PROFILE` and a finite boundary log-likelihood in the profile audit record.
- Unresolved nuisance optimizer: forced bounded scalar-optimizer failure is retained pointwise as `NUISANCE_PROFILE_OPTIMIZER_UNRESOLVED`; the combined profile record is marked `PROFILE_HAS_BOUNDARY_OR_UNRESOLVED_POINTS`, all affected curvature entries remain null, and the stability object retains unresolved statuses.

The first attempt at the boundary assertion used a nuisance-mean field not exposed by the audit-record schema. The exact failure was inspected and the test was corrected to assert only the record's declared fields. No production implementation or scientific contract was altered to accommodate the test.

Final exact-commit static validation:
- Commit: `ee676c7f85181e87196cee32b1c955ba5172e3e2`
- Run: `44594182486`
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **140 tests PASS**
- Three new adversarial tests: PASS.

The tests establish safe deterministic propagation and serialization for these fixtures. They do not establish optimizer reliability in general, global nuisance maximization, concentration identification, interval coverage or causal evidence. No numerical stress, calibration, bootstrap bank, resource preflight, holdout or scientific C10 execution occurred.


### End-to-end comparison-engine fault injection — optimizer-audit absence

A further deterministic test injects failure in `audit_beta_binomial_count_fit` through `fitted_beta_binomial_parametric_bootstrap` and exercises the actual `compare_dataset()` path with B1 diagnostics enabled. The resulting per-dataset record retains the original optimizer-audit error, leaves the concentration profile audit explicitly null with `OPTIMIZER_AUDIT_UNAVAILABLE`, and still emits the independent stability trace. Existing C5 within/between intervals remain present.

Exact-commit static validation:
- Commit: `9be6339947db2fd1b4554d6c808fccbdd30a28ca`
- Run: `44594508999`
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **141 tests PASS**
- End-to-end optimizer-audit fault-injection test: PASS.

This closes the full-engine propagation check for the optional optimizer-audit failure path. It remains a deterministic software test, not a statistical identification or coverage result. No calibration, bootstrap bank, resource preflight, holdout or scientific C10 execution was performed.


### End-to-end C5 boundary-abstention propagation

An all-zero F5 dataset now exercises the actual comparison engine with B1 profile diagnostics enabled. C5 retains its existing `ALL_ZERO_OR_ALL_ONE_BOUNDARY` abstention, while the independent B1 record preserves the optimizer audit, `MEAN_PROFILE_BOUNDARY` profile statuses and finite endpoint-mixture boundary likelihood. The concentration identification disposition remains `INDETERMINATE`.

An initial fixture used a non-dataclass stand-in and failed the existing strict dataclass serialization contract. The fixture was corrected to use the declared `BetaBinomialOptimizerAudit` record; production code and serialization requirements were left unchanged.

Exact-commit static validation:
- Commit: `3c389e123da11e4c6a0bc567cf36786ce418ee40`
- Run: `44594961717`
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **142 tests PASS**
- End-to-end C5 boundary-abstention/profile propagation test: PASS.

No numerical stress, calibration, bootstrap bank, resource preflight, holdout or scientific C10 execution occurred.


## 11. Integrated B1 endpoint / low-dispersion / interior-count fixture matrix — 2026-11-19

Historical reconstruction found that all three data-level fixtures already existed individually. Rather than duplicate them, an integrated test now runs each through the same numerical profile, separately profiled boundary likelihoods and audit-record builder.

The shared assertions preserve:
- finite binomial-limit nuisance profile for all three fixtures;
- finite two-point endpoint-mixture boundary only for endpoint-only counts;
- explicit `ZERO_PROBABILITY_INTERIOR_COUNTS` and null two-point likelihood for the low-dispersion and interior-count fixtures;
- raw maximum over the supplied finite profile grid and descriptive differences to each available boundary;
- profile curvature vector and profile-status propagation;
- optimizer convergence status separately from the always-`INDETERMINATE` identification disposition;
- strict JSON serialization.

Exact-commit static validation:
- Code/test commit: `62c5481f1a4cb5009ebdc9f32eaa928b28da7988`
- Run: `44595785248`
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **143 tests PASS**
- Integrated three-regime fixture-matrix test: PASS.

No production estimation, C5 interval, selection or abstention rule was changed. The finite-grid profile remains `NUMERICAL_PROFILE_UNCERTIFIED`; the boundary differences do not certify a global likelihood maximum or statistical identification. No calibration, bootstrap bank, resource preflight, holdout or scientific C10 execution occurred.
