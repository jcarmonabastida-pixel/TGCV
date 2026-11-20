# C10-S — F5 weak-identification audit plan 001

Date: 2026-11-19  
Branch: `research/c10s-f1-integrated-correction-20261119`

## Verified baseline

Static workflow run `44588467741` checked out commit `72f119b4be3b696fee95e5ad92c07376e5ba10c2` and completed successfully:
- hash-locked dependencies: PASS;
- compile: PASS;
- deterministic suite: 122 tests passed;
- `test_two_point_limit_is_the_low_concentration_limit`: PASS.

This validates deterministic likelihood-limit checks only.

## Weak-identification gap

The current `BetaBinomialOptimizerAudit` reports observed Hessian eigenvalues, score norm, multi-start outcomes, independent-optimizer agreement, and distances to optimizer bounds. Its status vocabulary adjudicates optimizer agreement, not statistical identification strength.

A small Hessian eigenvalue alone must not be equated with weak identification without a parameterization-aware scale and a defined diagnostic rule. Likewise, optimizer convergence, small score norm, or agreement in likelihood do not establish that concentration is identified.

## Required deterministic work before any classification rule

1. Construct data-level fixtures with analytically understood limiting behaviour:
   - endpoint-only counts approaching the `kappa -> 0` two-point mixture;
   - low-dispersion counts approaching the `kappa -> infinity` binomial limit;
   - interior-count fixtures for which the two-point boundary likelihood is `-inf`.
2. For each fixture retain:
   - observed log-likelihood and both boundary likelihoods;
   - score norm and full observed Hessian;
   - eigenvalues and eigenvectors in declared `(mean_logit, log_concentration)` coordinates;
   - every optimizer start, termination message, and boundary distance;
   - independent shape-parameter optimizer comparison.
3. Separate numerical optimizer convergence, likelihood preference over each boundary limit, and local information/curvature in concentration.
4. Do not create a binary weak-identification status until a scale-aware criterion and its operating characteristics are justified. Preserve raw diagnostics and permit indeterminate outcomes.
5. Add deterministic tests for invariance/known limits and diagnostic-schema completeness. Do not run Monte Carlo calibration or bootstrap simulations under this task.

## Guardrails

- No changes to C5 candidate selection, interval construction, or frozen scientific thresholds.
- No changes to frozen development/calibration specification v1.0.
- No calibration, resource preflight, holdout, or scientific C10 execution.
- Any future weak-identification threshold requires an explicit scientific rationale and must remain distinct from optimizer convergence status.

## Current disposition

The low-concentration two-point-limit and high-concentration binomial-limit likelihood tests exist. The remaining implementation gap is not to duplicate those identities, but to expose and verify a nuisance-profiled local concentration-curvature diagnostic while preserving raw optimizer and boundary comparisons. This plan is a research-branch design record only.


## Implementation increment — raw nuisance-profiled curvature

A new optional field, `profile_log_concentration_curvature`, is now calculated from the observed Hessian at the selected interior fit using the nuisance-adjusted Schur complement:

`H_xixi - H_etaxi^2 / H_etaeta`

where `eta = mean_logit` and `xi = log_concentration`. The field is left null when the nuisance-coordinate curvature is exactly zero or the resulting quantity is non-finite. No arbitrary numerical threshold is introduced.

This is a local, parameterization-specific observed profile-curvature diagnostic. It is not a normalized information measure, does not define weak identification, does not alter optimizer status, and does not affect C5 fit/interval selection. The existing dataclass-to-JSON serialization path carries the field into the per-dataset audit record.

Deterministic tests were added to:
- verify the field against the Hessian Schur-complement identity;
- verify that the per-dataset strict-JSON audit retains a finite value.

Implementation commits:
- diagnostic: `9d8f96cfe0100d30f017456b77b0da9ab6fe4d10`
- diagnostic unit test: `18f9293632348266a7dea872d587a2ff9c02a9bc`
- per-dataset serialization assertion: `09af6710a8954450ec85dbfae02c1a156432a73d`

Static workflow for the intermediate diagnostic and unit-test commits was triggered; the final serialization-test commit is the current validation target. **No passing result is claimed until its exact-commit run completes and logs are inspected.**


## Static validation of the profiled-curvature increment

The final static workflow validated the exact code commit:
- Run: `44589734031`
- Exact commit: `cb65659c82bb79183e2b81d13487ebb56d89f862`
- Conclusion: `SUCCESS`
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **123 tests passed**
- `test_profile_concentration_curvature_is_nuisance_adjusted_schur_complement`: PASS
- Per-dataset JSON serialization assertion for `profile_log_concentration_curvature`: PASS.

The raw curvature is emitted only when the selected mean-logit coordinate is strictly interior to its configured optimizer bounds, the nuisance Hessian diagonal is finite and nonzero, and the Schur-complement result is finite. Otherwise it remains null. This avoids treating a boundary-constrained mean estimate as an interior nuisance profile. No threshold was added.

The static workflow's three F1 numerical-stress workflows were `SKIPPED` by their authorization conditions. No numerical stress, calibration, bootstrap bank, resource preflight, holdout, or scientific C10 execution occurred.

## Exact source identities at the validated commit

| Artifact | Git blob SHA |
|---|---|
| F5 likelihood/optimizer diagnostics | `e57ea294c71de8810d7feded6a85110cee588929` |
| F5 diagnostic tests | `a7ef6b2da85b53a1d4ddf921aa8c28807a91565f` |
| Comparative engine per-dataset JSON test | `16534c1943092be8f569b75cdfe682c89830e47f` |
| Static workflow | `d47ac4cdde1f32c5c70cd9182a50d235cb630e5b` |

Validated research commit: `cb65659c82bb79183e2b81d13487ebb56d89f862`. The frozen development/calibration specification v1.0 was not modified.


## Implementation increment — numerical concentration profile and nuisance-profiled limits

Research commit sequence:
- profile and separately nuisance-profiled boundary diagnostics: `dfca143ffdd24bfffe6477ecbbf45afd1ea21b7b`
- first deterministic profile/boundary tests: `24306d06f7b4428ebb9ad3ac49cf7c519fde5bfd`
- endpoint-only, low-dispersion and permutation fixtures: `066ce9b989ba936f80127ff3391e6668251c350f`

The new `beta_binomial_profile_log_concentration` traces the log-likelihood over a caller-supplied strictly increasing log-concentration grid. At each point it searches the nuisance mean-logit coordinate on a deterministic grid, refines the best interior bracket with bounded scalar optimization, and retains nuisance/concentration scores plus the Schur-complement local curvature where defined. Its status is deliberately `NUMERICAL_PROFILE_UNCERTIFIED`; a finite grid plus local scalar refinement is not a certificate of a global nuisance maximum and does not classify identification.

The new `beta_binomial_profiled_boundary_likelihoods` separately maximizes the nuisance mean for:
- the binomial `kappa -> infinity` boundary, using the pooled Bernoulli MLE;
- the two-point `kappa -> 0` boundary, using the endpoint-mixture MLE when all observations are endpoints, and returning negative infinity when any interior count makes that limit impossible.

Deterministic tests now cover:
- profile curvature versus a finite difference of the nuisance-profiled log-likelihood on a local three-point grid;
- rejection of unordered/duplicate concentration grids;
- independent nuisance optimization at each extended boundary;
- endpoint-only and low-dispersion limiting fixtures;
- permutation invariance of the numerical profile under reordering independent world counts;
- interior-count exclusion from the two-point boundary.

Static workflow validation of commit `24306d06f7b4428ebb9ad3ac49cf7c519fde5bfd` completed successfully:
- Run `44590757616`
- dependency installation: PASS
- compile: PASS
- deterministic suite: PASS
- no calibration, bootstrap, resource preflight, holdout, or scientific execution.

The later fixture-test commit `066ce9b989ba936f80127ff3391e6668251c350f` is a new validation target; its result is not yet claimed.

### Interpretation and remaining limitations

The profile is a diagnostic trace, not a confidence set and not a proof of global nuisance maximization. The boundary likelihoods are model limits, not finite optimizer-bound substitutes. No weak-identification threshold, binary identification label, or C5 decision rule has been introduced. In particular, the endpoint-only and low-dispersion fixtures expose limiting behaviours but do not by themselves establish the sampling frequency or operating characteristics of any future diagnostic.

The next deterministic increment should add an explicit profile audit record that keeps optimizer convergence, boundary likelihood preference, and concentration-profile shape as separate fields, with an explicit `INDETERMINATE` identification disposition until a scale-aware criterion is scientifically justified. The frozen development/calibration specification v1.0 remains unchanged.


## Implementation increment — separated profile audit record and permutation-test correction

The first static validation of the expanded fixture set exposed one failure:
- Run `44591073605`, exact commit `066ce9b989ba936f80127ff3391e6668251c350f`;
- dependency installation and compilation passed;
- 129 of 130 deterministic tests passed;
- the permutation-invariance assertion on the profiled nuisance mean was too strict (`1e-10)); bounded scalar optimization produced a maximum observed difference of approximately `1.24e-8`, while the profile log-likelihood comparison itself remained within its tighter tolerance.

This is treated as a test-tolerance defect, not as evidence of a statistical discrepancy. The mean-logit comparison tolerance was widened to `5e-8`, still below the scale at which the optimizer's output would materially affect this diagnostic. The implementation and likelihood tolerances were not relaxed. The correction is in commit `ada00f87c482b5f9baa09e9e1bff674d005603a1`; its exact-commit static validation is being checked separately.

A new `BetaBinomialProfileAuditRecord` and builder now keep distinct:
- optimizer convergence status (copied from the existing optimizer audit);
- numerical profile status and point count;
- maximum value on the supplied, uncertified profile grid;
- raw log-likelihood differences against the separately nuisance-profiled binomial and two-point limits;
- the vector and finite range of local profile-curvature values;
- identification disposition, fixed at `INDETERMINATE`.

The record deliberately does not translate profile-vs-boundary differences into a boundary-preference verdict or weak-identification label. The profile is not globally certified, and no scale-aware identification criterion has been justified. Empty, non-finite, or unordered profile inputs fail closed.

Implementation commits:
- separated audit record: `fc28018236b75b4c11ca9c7dfc7f7551d0b54ded`
- audit-record tests: `23dd5dd24f210907d2c702307553b9caebc45ed0`

Static validation for these exact commits is in progress. No PASS is claimed until the relevant run completes and logs are inspected. The frozen development/calibration specification v1.0 and all C5 candidate/interval logic remain unchanged.


### Static validation — separated nuisance-refinement failure

The semantic correction and its explicit fault-injection test passed on the exact code/test commit:
- Run: `44591616425`
- Exact commit: `3f84f52d22a7e60dcf34dc99819f601b63a22599`
- Dependency installation: PASS
- Compile: PASS
- Deterministic suite: **133 tests passed**
- Fault-injection test `test_failed_nuisance_refinement_is_not_misreported_as_boundary`: PASS.

The profile-point record now distinguishes a genuine mean-logit grid boundary from an unsuccessful scalar nuisance refinement. An unsuccessful refinement is reported as `NUISANCE_PROFILE_OPTIMIZER_UNRESOLVED`, its mean-boundary flag remains false, and its local profile curvature is null. This avoids falsely describing a numerical optimizer failure as a statistical boundary condition.

The static workflow validated deterministic tests only. Numerical-stress workflows were skipped by authorization guards. No calibration, bootstrap, resource preflight, holdout or scientific C10 execution occurred.

The previous 132/132 result on commit `23dd5dd24f210907d2c702307553b9caebc45ed0` remains valid for that exact commit; the 133/133 result above supersedes it for the latest code/test increment.


## Implementation increment — strict-JSON boundary representation

The extended profile audit initially used negative infinity to represent a zero-probability two-point boundary when any count was interior. Although mathematically correct, non-finite JSON numbers are not valid under the project's strict JSON serialization contract. The diagnostic record now represents that case with:
- `two_point_profile_log_likelihood: null`;
- `two_point_boundary_status: ZERO_PROBABILITY_INTERIOR_COUNTS`;
- no profile-minus-boundary difference (`null`), because the boundary likelihood is structurally zero rather than a finite comparator.

Finite endpoint-only two-point limits retain their finite log-likelihood and endpoint-mixture MLE. Tests assert `json.dumps(..., allow_nan=False)` succeeds for the profile audit and boundary records.

The first static run on commit `1cdb9ea9b173f81cc3bc7c96e1e665b2d2d46032` exposed a conversion bug while constructing the new null value (four affected tests; 133 tests discovered). The return path was corrected to preserve `None` rather than coercing it to float. The correction is commit `9a4b6798a621505919356f5fa657a3667bf27cdb`; exact-commit static validation is pending.


### Static validation — strict-JSON boundary correction

The corrected exact-commit static workflow completed successfully:
- Run: `44591980405`
- Exact commit: `9a4b6798a621505919356f5fa657a3667bf27cdb`
- Dependency installation: PASS
- Compile: PASS
- Deterministic suite: **133 tests passed**
- Strict JSON serialization assertions for the profile audit and boundary objects: PASS
- Null representation for the structurally zero two-point boundary with interior counts: PASS.

The failure on predecessor commit `1cdb9ea9b173f81cc3bc7c96e1e665b2d2d46032` is retained as a historical failed validation, not overwritten. The corrected commit is the validated source identity for this increment.


## Implementation increment — F5 profile numerical-control stability

The next deterministic diagnostic compares the same fixed log-concentration grid under three nuisance-search configurations:
1. reference eta bounds and reference eta-grid resolution;
2. identical bounds with a denser eta grid;
3. expanded eta bounds with the denser grid.

For every concentration point it retains the raw differences in profiled log-likelihood, profiled mean-logit and (when both are available) Schur-complement profile curvature. It also retains each profile point's optimizer/boundary status and maximum absolute deltas by metric. No numerical tolerance, pass/fail threshold, confidence-set rule or identification classification is introduced: the audit is explicitly `NUMERICAL_STABILITY_NOT_ADJUDICATED` and `INDETERMINATE`.

Implementation:
- diagnostic: `4f93ae4524a8cc51aec66c38640349c533bdb9e0`
- deterministic tests: `36f931cbc19c91318d2969ec9fc80e187be5550e`

The tests exercise all three paired traces, verify finite raw differences and strict-JSON serialization, and reject invalid grid-size relationships or expanded bounds that do not strictly contain the reference bounds.

Exact-commit static workflow:
- Run: `44592485904`
- Commit: `36f931cbc19c91318d2969ec9fc80e187be5550e`
- Status at record creation: dependency installation in progress; compile and deterministic suite not yet run.
- The companion F1 numerical-stress-v3 workflow is skipped by its authorization guard (`44592485986`); no numerical stress, calibration, bootstrap, resource preflight, holdout or scientific execution is authorized or performed by this increment.

The frozen development/calibration specification v1.0 remains unchanged. This stability comparison is a deterministic method diagnostic only; it is not a simulation bank or empirical identification result.


### Static validation — F5 profile numerical-control stability

The exact code/test commit completed the research-branch static workflow successfully:
- Run: `44592485904`
- Exact tested commit: `36f931cbc19c91318d2969ec9fc80e187be5550e`
- Hash-locked dependency installation: PASS
- Compile: PASS
- Deterministic suite: **135 tests passed**
- Both new numerical-stability tests: PASS
- No calibration, bootstrap, resource preflight, holdout or scientific execution.

The audit remains descriptive. The 135/135 result establishes deterministic software behaviour for the fixtures; it does not establish that any particular profile is numerically stable over a scientifically relevant range, nor that concentration is identified.


## Implementation increment — per-dataset F5 concentration-profile propagation

The concentration profile and its numerical-control stability audit are now available through the actual matched-dataset comparison path, as opt-in F5 diagnostics.

When `include_f5_concentration_profile_audit=True`, the caller must supply an explicit, finite, strictly increasing `f5_profile_log_concentration_grid`. No data-dependent grid or implicit concentration range is selected. The engine then stores two strict-JSON fields in that dataset's F5 candidate diagnostics:

- `concentration_profile_audit_json`: optimizer convergence status, profile status/point count, maximum on the supplied numerical grid, separately nuisance-profiled binomial and two-point boundary likelihoods and raw differences, and the vector/range of local Schur-complement profile curvatures. Identification remains `INDETERMINATE`.
- `concentration_profile_stability_json`: paired differences at the same concentration points under reference/refined/expanded nuisance searches (eta bounds -18..18 vs -24..24; grid sizes 65 and 257), preserving per-point statuses and raw maximum absolute deltas. Status remains `NUMERICAL_STABILITY_NOT_ADJUDICATED`.

Errors are retained separately for profile construction and stability construction. The diagnostic is explicitly opt-in so the expensive three-trace sensitivity audit is not silently added to every dataset in the frozen development/calibration banks. The new tests prove that enabling it leaves C5 within/between/MCSE interval outputs unchanged, and that strict JSON serialization succeeds. No C5 estimator, bootstrap, selection or abstention rule was changed.

Implementation:
- comparison-engine integration commit: `1890f19040f627eaef2069b1188f33ebf71d2118`
- per-dataset integration tests commit: `898906f2b5ee94c599a478991688cbe2e9333551`
- final engine blob: `358794e1fcffe729546338ae7a7749bdaaa6aa2c`
- final test blob: `d592e3feef1b621a3051098f453ca482abc04939`

Exact-commit static validation:
- Run: `44593339897`
- Commit: `898906f2b5ee94c599a478991688cbe2e9333551`
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **137 tests passed**
- New per-dataset audit, strict-JSON and interval-invariance tests: PASS
- F1 numerical-stress workflows v1/v2/v3: SKIPPED by authorization guards.

No DGP bank, calibration, bootstrap comparison bank, resource preflight, holdout, or scientific C10 execution was performed. This closes the static per-dataset propagation gap for B1 only; it does not validate the statistical identification of concentration or C5 coverage. The frozen development/calibration specification v1.0 remains unchanged.


## Adversarial B1 propagation controls — 2026-11-19

The per-dataset B1 propagation now has deterministic adversarial coverage for three distinct conditions:

1. **Optimizer audit unavailable:** the profile audit is recorded as JSON `null` with the explicit `OPTIMIZER_AUDIT_UNAVAILABLE` error, while the independent numerical-stability trace is still retained. One diagnostic failure does not erase the other.
2. **Finite two-point boundary:** an endpoint-only count fixture retains the separately profiled finite two-point mixture boundary and its status; identification remains `INDETERMINATE`.
3. **Unresolved nuisance refinement:** forced scalar-optimizer failure is propagated as `NUISANCE_PROFILE_OPTIMIZER_UNRESOLVED` at every point; profile status becomes `PROFILE_HAS_BOUNDARY_OR_UNRESOLVED_POINTS`, curvature remains null, and the stability trace preserves unresolved statuses without claiming numerical stability or identification.

Exact-commit static validation:
- An intermediate test commit `f7e2450bfe39a20372a21c88549df1dcd0f6bd49` failed one assertion because the test expected a nuisance-mean field not exposed by the audit record. The failure was inspected; no production-code change was needed. The test was corrected to assert only fields actually included in the record.
- Final tested commit: `ee676c7f85181e87196cee32b1c955ba5172e3e2`.
- Run: `44594182486`.
- Hash-locked dependency installation: PASS.
- Compile: PASS.
- Deterministic suite: **140 tests passed**.
- All three new adversarial propagation tests: PASS.
- F1 numerical-stress workflows remain outside this operation and were skipped by authorization guards.

This closes the identified deterministic propagation cases for optimizer-audit absence, finite two-point boundary handling and unresolved nuisance-profile refinement. It does not certify global nuisance maxima, profile topology, concentration identification, C5 coverage or any causal TGCV claim. No Monte Carlo, bootstrap bank, calibration, resource preflight, holdout or scientific execution occurred.


### Full comparison-engine fault injection — optimizer-audit absence

A further adversarial test now injects failure in the optional F5 optimizer audit through the real `compare_dataset()` path, rather than calling only the diagnostic serializer helper. The fitted C5 comparison still completes; the per-dataset record preserves:
- `likelihood_optimizer_audit_json = null` and the original optimizer-audit error;
- `concentration_profile_audit_json = null` with `OPTIMIZER_AUDIT_UNAVAILABLE`;
- the independently computed numerical-stability trace;
- the existing C5 within/between intervals.

Exact-commit static validation:
- Commit: `9be6339947db2fd1b4554d6c808fccbdd30a28ca`
- Run: `44594508999`
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **141 tests passed**
- Full comparison-engine optimizer-audit fault-injection test: PASS.

This confirms the optional audit failure remains diagnostic-only at the actual per-dataset engine boundary; it does not silently suppress C5 outputs or erase the independent stability record. No calibration, bootstrap bank, resource preflight, holdout or scientific execution was performed.


### Full comparison-engine boundary-fit abstention fixture

Added an end-to-end all-zero F5 dataset fixture. The existing C5 estimator correctly abstains with `ALL_ZERO_OR_ALL_ONE_BOUNDARY`; independently, the B1 profile audit records the optimizer status, the nuisance profile's boundary status, and the finite endpoint-mixture likelihood limit. The stability trace preserves `MEAN_PROFILE_BOUNDARY` at every concentration point. Identification remains `INDETERMINATE`.

The first test attempt used a `SimpleNamespace` in place of the optimizer-audit dataclass and correctly failed the engine's strict dataclass serialization contract. The fixture was corrected to use a schema-conformant `BetaBinomialOptimizerAudit`; no production code or contract was weakened.

Exact-commit static validation:
- Final tested commit: `3c389e123da11e4c6a0bc567cf36786ce418ee40`.
- Run: `44594961717`.
- Hash-locked dependencies: PASS.
- Compile: PASS.
- Deterministic suite: **142 tests passed**.
- All-zero C5 fit-abstention/profile-boundary propagation test: PASS.
- Companion F1 numerical-stress workflows v1/v3 were skipped by authorization guards; v2 also skipped. No numerical stress was executed.

This closes deterministic propagation coverage for a C5 fit boundary abstention in addition to optimizer-audit absence, finite endpoint mixture, and unresolved nuisance refinement. It remains software-level evidence only.


## Integrated deterministic B1 fixture-matrix validation — 2026-11-19

Historical reconstruction confirmed that endpoint-only, low-dispersion and interior-count fixtures were already present as separate deterministic unit tests. The new increment does not recreate those fixtures or alter their generating values. It adds one shared audit-record test that sends all three through the same sequence:

`profile_log_concentration → profiled_boundary_likelihoods → build_profile_audit_record`.

For each fixture the test verifies:
- the separately nuisance-profiled binomial boundary;
- whether the two-point mixture boundary is finite or impossible because interior counts occur;
- the maximum over the supplied finite numerical profile grid;
- the raw profile-minus-boundary likelihood differences, with null retained when the two-point limit is impossible;
- profile-curvature vector length and profile status propagation;
- optimizer convergence status kept as a separate field;
- `identification_status=INDETERMINATE`;
- strict JSON serialization without NaN/Infinity.

Exact-commit static validation:
- Code/test commit: `62c5481f1a4cb5009ebdc9f32eaa928b28da7988`
- Run: `44595785248`
- Hash-locked dependencies: PASS
- Compile: PASS
- Deterministic suite: **143 tests passed**
- `test_profile_audit_fixture_matrix_keeps_three_likelihood_regimes_separate`: PASS.

The numerical profile remains explicitly uncertified as a global nuisance maximum. Differences are descriptive comparisons over the supplied finite grid, not a likelihood-ratio test, confidence set, identification threshold or selection rule. No calibration, bootstrap bank, resource preflight, holdout or scientific C10 execution occurred.
 

## B1 local-information record completeness — 2026-11-19

The per-fit `BetaBinomialOptimizerAudit` now retains the complete observed Hessian matrix in declared `(mean_logit, log_concentration)` coordinates, its eigenvectors alongside the existing eigenvalues, the two selected score components, and raw fitted-log-likelihood differences against each finite extended concentration boundary. The two-point contrast remains null when interior counts make that limiting likelihood structurally zero; no non-finite JSON sentinel is introduced.

This is an additive diagnostic record only. It does not alter C5 fit selection, interval construction, optimizer status, or identification disposition. The curvature remains local and parameterization-specific.

Exact-commit static validation:
- Code/test commit: `654be3b90668374de2572611926a2a3c080c411b`.
- Run: `44596631663`.
- Hash-locked dependencies: PASS.
- Compile: PASS.
- Deterministic suite: **143 tests passed**.
- Full Hessian/eigenvector and boundary-contrast assertions: PASS.

Still open within B1: independently coded Hessian cross-checks at boundary-adjacent fixtures, explicit retention of the independent optimizer's terminal coordinates/gradient/bound distances, and a final audit that all three-start outcomes remain complete in the comparison-engine record. A1 F1 deterministic certification is also still open. No resource preflight or numerical calibration was run.


## 12. Final B1 implementation reconciliation — 2026-11-19

This section supersedes the provisional open-item list in §11. The listed implementation gaps are now present in the current research-branch code and covered by the exact-commit static workflow recorded below.

### 12.1 Three items previously listed as open — now closed

1. **Independent Hessian cross-check at a boundary-adjacent fixture — CLOSED.** The independent `(log(alpha), log(beta))` score/Hessian implementation is checked against central finite differences of both score components in an interior fixture and a low-shape boundary-adjacent fixture (`alpha=0.025, beta=0.04`). The test checks both diagonal entries and both cross-derivative directions: `test_independent_log_shape_hessian_matches_score_differences_interior_and_near_boundary`.
2. **Independent optimizer terminal state — CLOSED.** `BetaBinomialOptimizerAudit` retains independent terminal `log(alpha)`/`log(beta)`, both independent score components and norm, and the independent observed Hessian. The per-dataset serialization test asserts these fields are present and finite.
3. **All three primary starts through the comparison-engine record — CLOSED.** The per-dataset `likelihood_optimizer_audit_json` retains all three starts, their messages, final mean-logit/log-concentration coordinates, gradient norms and four distances to the configured numerical bounds. The engine-level test parses and asserts the full three-start record.

### 12.2 B1 requirements reconciled against the frozen specification

| Frozen §7 B1 requirement | Current evidence | Disposition |
|---|---|---|
| Three-start L-BFGS-B outcomes retained | `BetaBinomialStartOutcome`, `BetaBinomialOptimizerAudit`; comparison-engine JSON test | PASS |
| Independent mean-logit/log-concentration score and Hessian behaviour | Analytic score/Hessian plus central finite-difference tests | PASS |
| Independent Hessian/observed-information cross-check near a parameter boundary | Independent log-shape Hessian finite-difference fixture at small positive alpha/beta | PASS — bounded numerical fixture, not boundary-limit inference |
| Separately parameterized optimizer and disagreement diagnostics | Independent BFGS in log-shape coordinates; objective difference, parameter distance, scores, terminal coordinates and Hessian retained | PASS |
| Explicit kappa→infinity and kappa→0 likelihood limits | Binomial and two-point mixture limits, separately profiled nuisance means; endpoint-only and interior-count tests | PASS |
| Finite-R likelihood against independent count oracle | Every count in support reconciled to exact beta-binomial PMF; finite-sample moment oracle tests retained | PASS |
| Typed boundary/non-identification and unresolved numerical states | Fit-boundary abstentions, optimizer/profile status separation, unresolved nuisance failures preserved | PASS as fail-closed diagnostics; no binary weak-identification threshold claimed |

### 12.3 Identification interpretation retained

The diagnostic does **not** invent a binary weak-identification threshold. The profile audit's `identification_status=INDETERMINATE` is intentional where no scale-aware criterion with justified operating characteristics exists. It must not be rewritten as “identified” merely because an optimizer converged, the fit is interior, or independent likelihood values agree. Raw curvature, boundary likelihood contrasts, score norms, optimizer status and profile stability remain separate observations. The later B2 calibration/validation gate must inspect these diagnostics and apply the frozen §8 acceptance/stop rules; this B1 closure is not a C5 coverage pass.

### 12.4 Exact static validation

- Workflow run: `44602425187`
- Exact code commit: `b44489341e4ee99aa279b15d6cb635e744a1665e`
- Hash-locked dependencies: PASS
- Compilation: PASS
- Deterministic comparator/oracle suite: **153 tests PASS**
- The executed suite explicitly includes `test_c10s_f5_beta_binomial_likelihood_diagnostics`, `test_c10s_fitted_beta_binomial_bootstrap`, `test_c10s_nested_mr_comparative_inference_engine`, and `test_c10s_beta_binomial_variance_oracles`.
- The exact log includes passing checks for independent log-shape Hessian finite differences, boundary-adjacent score behaviour, optimizer audit retaining all starts and independent fit, finite-R PMF reconciliation, and the engine's three-start JSON persistence.

The current source blobs are recorded in `C10S_F5_B1_IMPLEMENTATION_CLOSURE_001.md`. The frozen development/calibration specification v1.0 remains unchanged.

### 12.5 MCSE scope correction

The preflight's `F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED` is **not** an open B1 defect. Frozen specification §§6, 7, 10 and 11 explicitly exclude F5 MCSE interval construction and preserve its abstention. The C5 candidate's within/raw-between intervals are the Phase B target. The MCSE abstention must remain explicit; no MCSE method is to be added or promoted under this work package.

**B1 disposition:** IMPLEMENTATION_AND_DETERMINISTIC_TESTS_COMPLETE. Statistical concentration identification and C5 component eligibility remain to be evaluated on the separately authorized B2/B3 calibration and disjoint validation banks. No coverage/calibration result is inferred from the static suite or resource preflight.


## 13. F5 B2/B3 execution package — implementation complete, execution gated

The F5-only B2/B3 development runner and its one-use authorization path are now implemented. Full specification mapping, seed schedules, per-dataset outputs, component gates, B3 rank/endpoint diagnostics, source hashes and static validation are recorded in `C10S_F5_B2_B3_DEVELOPMENT_RUNNER_IMPLEMENTATION_001.md`.

- B2: 5,000 calibration + 5,000 disjoint development-validation datasets per F5 cell; C0/C5 B=1,000.
- B3: 250 calibration-bank datasets per cell, selected by a pre-outcome SHA-256 rule; C5 B=1,000 and B=4,000 on independent streams.
- Historical seed collision guard and exact dataset regeneration/hash check are hard preconditions.
- Component gates are applied separately by cell, bank and target; no pooling. B3 is diagnostic only.
- MCSE remains explicitly excluded/abstained.
- Exact-commit static workflow `44609322947`: 168/168 PASS at `cdd8617f13296556fd5eb463834fb60c0f051f7c`.
- Dedicated workflow is dormant; only a DRAFT authorization template exists. No B2/B3 numerical execution has occurred.

**Disposition:** F5 B1 implementation and B2/B3 execution package are complete. F5 numerical development calibration/validation and C5 component eligibility remain OPEN until explicit one-use authorization and execution. No confirmatory or causal conclusion is implied.


## 14. F5 B2/B3 numerical development result — executed and audited

The one-use F5-only B2/B3 execution completed in GitHub Actions run `44615173745` (SUCCESS), under authorization `F5-B2B3-20261119-2202`, approved code commit `cdd8617f13296556fd5eb463834fb60c0f051f7c`. The primary artifact and all output-file hashes were audited. Full record: `C10S_F5_B2_B3_DEVELOPMENT_CALIBRATION_RESULT_AUDIT_001.md`.

- Both cells have 5,000 calibration and 5,000 disjoint development-validation datasets; B3 has 250 pre-outcome-selected datasets per cell.
- Dataset IDs/seeds are unique and disjoint between calibration and validation; historical seed collision audit PASS; all 500 B3 rows match selected calibration IDs, dataset seeds and row hashes.
- C5 complete frozen component gates: **0/8 pass**. M10/R5 overcovers both targets in both banks. M30/R20 point coverage lies within the broad band, but all four Wilson intervals lie below 95%, failing the nominal-coverage requirement.
- C5 optimizer audit unresolved states are frequent: M10/R5 2,169/2,132 independent-optimizer unresolved in calibration/validation; M30/R20 3,270/3,259. Many independent optimizer runs terminate with precision-loss messages despite very small likelihood differences, which warrants targeted diagnosis but cannot be relabelled post hoc.
- B3 shows modest endpoint changes as B increases from 1,000 to 4,000; it does not correct or explain the coverage pattern and is not used for coverage adjudication.
- Matched C0 also fails the complete coverage/Wilson criteria; it does not provide an acceptance fallback.
- F1 A2/A3, Tier B, comparative holdout, C10 causal execution and MCSE interval construction remained excluded.

**B2/B3 disposition:** EXECUTED / PRIMARY ARTIFACT INTEGRITY AUDITED / C5 NOT VALIDATED / C0 NOT VALIDATED / NON-CONFIRMATORY DEVELOPMENT EVIDENCE ONLY. No frozen rule, estimator or threshold was changed. The one-use authorization is consumed; no further numerical execution is authorized by it.

**Next operation:** static diagnosis of independent-optimizer precision-loss outcomes and the M10/R5 vs M30/R20 coverage divergence. Any new optimizer adjudication rule or revised candidate must be designed and independently tested before fresh development banks; current banks cannot become confirmatory data.


## 15. F5 B2/B3 coordinated static diagnosis — 2026-11-20

The post-result diagnosis is recorded in `C10S_F5_B2_B3_COORDINATED_DIAGNOSTIC_001.md`. It uses the existing raw artifact from run `44615173745`; no replay, new K/B sample, or scientific execution was performed.

New findings:
- The C5 production fit uses three L-BFGS-B starts without an analytic Jacobian; the diagnostic fit uses the same starts with an analytic Jacobian. The BFGS check then starts from the analytic-gradient fit. The existing audit therefore does not directly reconcile the production fit against the analytic-gradient fit and is not an independently initialized global optimizer.
- M30/R20's large BFGS unresolved count is predominantly a termination-flag issue: despite precision-loss messages, BFGS and analytic-gradient solutions have virtually identical likelihood and parameters. This remains a failed frozen optimizer gate; no retrospective PASS.
- M10/R5 shows substantial production-versus-analytic fit-path parameter divergence on a near-flat concentration ridge adjacent to the binomial limit. The upper fitted-concentration decile has near-zero profile curvature and near-zero likelihood advantage over the binomial limit.
- M30/R20's high-fitted-concentration upper decile is different: profile curvature remains materially negative and the likelihood remains separated from the binomial limit, yet C5 coverage falls to 50.0%/35.6% (within/raw-between) in calibration and 50.8%/35.0% in validation. Matched C0 coverage in the same post-fit strata remains approximately 96–98%. C5 intervals are narrower and misses are directional.
- These are exploratory post-fit strata, not acceptance gates or causal proof. They indicate that M10/R5 weak identification and M30/R20 high-κ plug-in interval undercoverage must be diagnosed separately.

**Next operation:** implement a static per-dataset production-fit vs analytic-fit reconciliation record; separate optimizer termination from numerical agreement without relaxing the frozen gate; add deterministic fixtures for precision-loss/local concordance, weak concentration ridge, true disagreement and upper-bound contact; and diagnose the plug-in C5 interval failure. Do not replay run `44615173745`, increase B/K, or launch another numerical bank at this stage. Any alternative interval method requires a separate versioned design decision and fresh disjoint development data.


Additional adjudication-control finding: the runner currently requires all three analytic-gradient starts to succeed, whereas frozen B1 requires their complete outcomes to be retained and compared, not necessarily all to succeed. M30/R20's failed starts are often clearly noncompetitive while successful starts agree to near machine precision; M10/R5 has much wider successful-start parameter spread. The next static change must reconcile this stricter Boolean gate with the frozen specification and replace it with raw multi-start concordance diagnostics, without relaxing the no-unresolved-state rule or retrospectively changing B2/B3.


## Implementation increment — direct production/analytic reconciliation (2026-11-20)

The per-dataset F5 traceability gap is now implemented additively. The production fit P (finite-difference L-BFGS-B) retains all three start outcomes and selected-start identity. The analytic fit A (analytic-gradient L-BFGS-B) and independent-coordinate BFGS check I remain distinct; I is explicitly labelled as a local check initialized from A, not a global search.

A strict-JSON reconciliation object records raw P-minus-A likelihood, mean-logit, log-concentration, alpha, beta, mean-probability and concentration differences, together with all P/A starts and typed missing-path states. The object propagates through the comparative inference engine into each calibration-runner dataset record.

No tolerance, binary weak-identification threshold, optimizer replacement, or automatic PASS is introduced. The runner's existing all-starts-success gate remains unchanged pending a separate interpretation against frozen B1 and §8; a failed start is neither presumed harmless nor presumed to imply materially different solutions.

Static validation:
- exact tested code/test commit: `18e1c6372af1c191b640e0d1f8d3318b889b28b9`;
- workflow run: `44645072630`;
- hash-locked dependency installation: PASS;
- compile: PASS;
- deterministic suite: **171 tests passed in 24.023 s**;
- direct P/A reconciliation, missing-audit and all-failed-production-start tests: PASS.

Implementation record: `C10S_F5_B1_PRODUCTION_ANALYTIC_RECONCILIATION_IMPLEMENTATION_001.md`. Current branch head after documentation updates: `10b2d16d0a97737c2b1859291a02239af650efc5`.

The historical B2/B3 results, frozen development specification v1.0, C0 and C5 interval construction remain unchanged. No replay, calibration, bootstrap bank, resource preflight, holdout, or scientific C10 execution occurred.


## Static historical-bank optimizer/start concordance diagnostic — 2026-11-20

The original B2/B3 artifact was downloaded and its ZIP SHA-256 independently matched the GitHub artifact metadata. All four 5,000-row calibration/validation JSONL banks were read without replay or regeneration. The direct production P versus analytic A comparison was reconstructed from the original candidate provenance and optimizer-audit fields; no new scientific execution was performed.

The analysis is recorded in `C10S_F5_B2_B3_OPTIMIZER_START_CONCORDANCE_DIAGNOSTIC_001.md`.

Main results:
- M30/R20 P/A agreement is extremely close across all 10,000 records: maximum absolute log-likelihood difference 8.07e-11 and maximum log-shape distance 6.76e-6.
- M10/R5 P/A agreement has a close median but a very broad upper tail: calibration 499/4,822 and validation 480/4,798 have absolute log-likelihood difference >1e-6; log-shape-distance q90 is 3.146 and 0.290, respectively, with q99 14.201 and 14.164. This supports a design-specific weak concentration ridge, not a generic optimizer-termination explanation.
- Analytic multi-start outcomes are heterogeneous. M30/R20 failed starts often lie essentially on the best successful solution, while a minority are far away and materially worse. M10/R5 failed starts show broader coordinate displacement even when objective gaps are small.
- All-three-success is not sufficient for start concordance: 35/5,000 M30/R20 calibration and 29/5,000 validation records have successful-start objective spread >1e-6, with maxima 25.17 and 26.56.
- Frozen B1 requires retaining and comparing all three starts; it does not require every start's success flag to be true. Frozen §8 nevertheless requires no unresolved numerical state. Thus the runner's Boolean is stricter than B1 wording, but it cannot simply be removed or replaced with an “at least one successful start” rule. No alternative threshold is justified here.

Disposition: historical B2/B3 gates remain unchanged and failed. No retrospective PASS, no optimizer tolerance change, no new numerical bank, and no change to frozen specification v1.0.

**Next operation:** diagnose the M30/R20 high-concentration C5 plug-in interval undercoverage separately from M10/R5 weak identification. Use only the existing raw artifact and deterministic/static calculations to trace what the bootstrap conditions on, which parameter uncertainty is omitted, and which interval endpoints/miss directions are implicated. Do not select or tune a replacement interval method from these development banks; any alternative requires a separately versioned design decision and fresh disjoint development data.


## Static C5 high-concentration plug-in interval diagnosis — 2026-11-20

The existing B2 artifact and the exact historical C5 source were examined. The detailed record is `C10S_F5_C5_HIGH_CONCENTRATION_PLUGIN_COVERAGE_DIAGNOSTIC_001.md`.

The source confirms that C5 fits alpha/beta once, generates beta-distributed world probabilities from that fixed pair, samples binomial counts, and computes nested estimators. It does not refit alpha/beta inside bootstrap replicates. Thus the bootstrap is conditional on one fitted parameter pair and does not reproduce the repeated-sampling distribution of the concentration estimator.

For M30/R20's top fitted-κ decile, median fitted κ is 7.668 (calibration) and 7.735 (validation), against DGP κ=4. The beta-binomial moment identities at the median fitted parameters imply within variance about 0.2212 and between variance about 0.0287–0.0288, close to observed point-estimate medians (within 0.2195–0.2196; raw-between 0.0297–0.0301) but shifted from true (0.20, 0.05).

In that same stratum, C5 coverage is 50.0%/35.6% within/raw-between in calibration and 50.8%/35.0% in validation, with directional misses and median intervals 16–18% narrower than matched C0. C0 is not validated overall; it is only a matched diagnostic comparator here.

**Interpretation:** the evidence supports conditional plug-in miscalibration associated with upward fitted concentration and shifted variance allocation. The omission of alpha/beta re-estimation within bootstrap replicates is a concrete mechanism and plausible contributor, but the artifact does not prove it is the sole cause. No alternative interval method is selected or tuned.

**Next operation:** prepare a separately versioned, static method-design comparison for fixed plug-in C5 versus a refitted parametric bootstrap and a profile/likelihood-based uncertainty approach. Define estimands, refit/boundary/failure semantics, interval construction, computational budget and prospective acceptance rules before any new development bank. The B2/B3 banks remain historical development evidence and cannot be used to select or tune the replacement.


## Coordinated comparative interval-method design — 2026-11-20

A single integrated design draft has been persisted at `03_EXPERIMENTS/C10-S/design/C10S_F5_INTERVAL_METHOD_COMPARISON_DESIGN_DRAFT_001.md`.

It defines:
- M0: incumbent fixed-parameter plug-in C5, retained as baseline and not validated;
- M1: refitted parametric bootstrap, including full per-replicate fit-state retention, boundary/failure semantics and explicit abstention obligations;
- M2a: asymptotic profile-likelihood reference, and M2b: bootstrap-calibrated profile likelihood, with nonregular/boundary caveats;
- shared W/B target functionals, parameterization and boundary geometry;
- paired per-dataset comparison, coverage/width/directional-miss/abstention/MCSE/cost outcomes;
- deterministic validation requirements and shared implementation interfaces;
- prospective disjoint development and confirmatory banks, selection/freeze gates, and explicit non-use of B2/B3 for tuning.

C0 is restricted to a historical diagnostic comparator; MCSE interval construction remains excluded. No method has been selected, no acceptance criterion changed, and no implementation, calibration, bootstrap, replay or scientific execution was performed.

**D0 remains OPEN.** The exact frozen v1.0 target/estimand mapping and interval semantics must be recovered and reconciled before D1 can be frozen. The draft explicitly leaves this unresolved rather than guessing whether the primary targets are population W/B functionals, finite-sample raw estimators, or both. It also leaves the M1 interval rule, failed-refit policy, M2b calibration precision and compute budget open.

**Next operation:** locate the authoritative frozen v1.0 specification and original C5 target mapping in the repository history/tree; reconcile the eight D1 questions in one integrated revision. No code or numerical execution until D1 is frozen and separately authorized.
