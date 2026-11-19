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
