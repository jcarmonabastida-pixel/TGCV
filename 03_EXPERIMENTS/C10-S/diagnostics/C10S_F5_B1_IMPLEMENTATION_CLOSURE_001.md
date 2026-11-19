# C10-S — F5 B1 implementation closure and preflight scope reconciliation

**Record:** C10S-F5-B1-IMPLEMENTATION-CLOSURE-001  
**Date:** 2026-11-19  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Status:** B1 IMPLEMENTATION AND DETERMINISTIC TESTS COMPLETE / B2-B3 NOT EXECUTED / C5 VALIDATION NOT ESTABLISHED

## 1. Governing scope

Frozen specification: `C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md`, v1.0, blob `d1c8bae882dc2e4cd0e1caae29609561b9ebac68` (unchanged).

Phase B targets the existing `C5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0` candidate for **within and raw-between components**, against unchanged C0. It does not introduce or select a new interval method.

The specification explicitly excludes F5 MCSE interval construction (§§6, 7, 10 and 11). C5 MCSE therefore remains an explicit abstention. The preflight's `F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED` is expected scope behaviour, not a defect in the two Phase B target components. It must not be fixed by adding a new MCSE method under this package.

## 2. B1 requirement closure

| Requirement | Implemented evidence | Static test evidence | Status |
|---|---|---|---|
| Retain all three primary L-BFGS-B starts | `BetaBinomialStartOutcome` records initial/final coordinates, success/message, objective, gradient norm and distances to all four bounds | `test_optimizer_audit_retains_all_starts_and_independent_fit`; engine JSON test parses all three | PASS |
| Independent analytic score and Hessian in mean-logit/log-concentration coordinates | `beta_binomial_loglik_score_hessian` | Score and full Hessian central finite-difference tests | PASS |
| Independently parameterized Hessian cross-check near boundary | `beta_binomial_log_shape_score_hessian` in `(log(alpha),log(beta))` | `test_independent_log_shape_hessian_matches_score_differences_interior_and_near_boundary`, including `alpha=0.025,beta=0.04`; both diagonals and cross terms checked | PASS |
| Independent optimizer comparison | BFGS in log-shape coordinates; objective difference, parameter distance, terminal coordinates, scores and observed Hessian retained | Optimizer audit test and per-dataset JSON test | PASS |
| Compare finite fit to both concentration limits | Explicit `kappa→infinity` binomial and `kappa→0` two-point mixture likelihoods; separately profiled boundary nuisance means | Low/high concentration, endpoint-only and interior-count fixtures | PASS |
| Reconcile finite-R likelihood/oracle | Exact finite-R count likelihood and independent beta-binomial PMF/moment oracle | Every count in support; exhaustive finite-sample moment test | PASS |
| Preserve boundary and unresolved states | Typed fit abstention, optimizer status, profile status and identification disposition remain separate | All-zero/all-one, finite two-point boundary, optimizer-audit failure and unresolved nuisance-refinement fault-injection tests | PASS — fail-closed diagnostic implementation |

No threshold was introduced to convert raw curvature or optimizer convergence into a binary weak-identification verdict. Where concentration identification is not established by a justified scale-aware criterion, the diagnostic remains `INDETERMINATE`. This is a deliberate restraint, not an implementation omission.

## 3. Per-dataset propagation

The actual comparison engine persists `likelihood_optimizer_audit_json` for each F5 candidate. The JSON retains:
- all three primary starts and their terminal records;
- independent optimizer terminal `log(alpha)` and `log(beta)`;
- independent score components/norm and observed Hessian;
- selected fit score components, observed Hessian/eigenstructure and profile Schur curvature;
- likelihood contrasts against the two extended concentration limits;
- explicit optimizer-audit error if the optional diagnostic cannot be built.

The concentration-profile/stability audit is separately opt-in and requires an explicit caller-supplied concentration grid. It does not alter the C5 fit, within/raw-between intervals, selection, or abstention. It preserves `identification_status=INDETERMINATE` and does not claim global profile certification.

## 4. Exact source identities at the tested code commit

All blobs below were fetched directly at code commit `b44489341e4ee99aa279b15d6cb635e744a1665e`; they are the exact source identities consumed by run `44602425187`.

| Artifact | Git blob SHA |
|---|---|
| Frozen specification v1.0 | `d1c8bae882dc2e4cd0e1caae29609561b9ebac68` |
| F5 likelihood diagnostics | `d11d5b8d914d0b27cfed98163ca5da7ed45d3aea` |
| F5 likelihood diagnostic tests | `f1c820882e2d6c1c815a8c505d2dc45c90b3c692` |
| F5 fitted bootstrap candidate | `1052ed986e4a551654b9d32928937e4e39df2c88` |
| F5 fitted bootstrap tests | `4b7e70b59b99ddb6ed6fdd767d38e31096d0cdaa` |
| Comparative inference engine | `358794e1fcffe729546338ae7a7749bdaaa6aa2c` |
| Comparative inference engine tests | `faea099809b306b1e6891dc972dd68df28614b45` |
| Beta-binomial oracle | `2b4412311abd7c6fb19a9174b39e7eab8b317bc4` |
| Beta-binomial oracle tests | `68071f633b8750084071274a1740abc4bb85d5dc` |

## 5. Exact-commit static validation

Workflow run: `44602425187`  
Exact code commit: `b44489341e4ee99aa279b15d6cb635e744a1665e`  
Result: **153/153 deterministic tests PASS**  
Hash-locked dependencies: PASS  
Compilation: PASS

The inspected log explicitly shows passing F5 tests for:
- independent log-shape Hessian finite differences in interior and near-boundary fixtures;
- boundary-adjacent score finite-difference behaviour;
- optimizer audit retaining all starts and the independent fit;
- finite-R count likelihood against the independent exact PMF oracle;
- comparison-engine persistence of the three starts and independent optimizer outputs;
- opt-in profile/boundary/stability diagnostics and fail-closed propagation.

This is implementation/static evidence only. It is not calibration, validation, coverage evidence, or scientific execution.

## 6. Resource preflight evidence and limitation

Run: `44603264310` — SUCCESS.  
Artifact SHA-256: `79d1fce857aeee9fde993dd2ba690d6a623feaacee486cc835f8e15a8dbab56a`.

The raw artifact was downloaded and inspected:
- F5 representative cell: 100 datasets, M30/R20;
- fitted-model status: `INTERIOR` for 100/100;
- untyped execution failures: 0;
- C0 bootstrap B=1,000 and C5 bootstrap B=1,000 were run; C5 B=4,000 sensitivity was also measured on the same fixed preflight datasets;
- F5 elapsed time: 165.226 s total; 1.65226 s/dataset;
- process lifetime peak RSS: 119 MiB (cumulative high-water mark);
- full-workload linear projection: 3.210 h.

**Artifact limitation:** the preflight JSON records fit status, MCSE abstention reason, seeds and row hashes, but does not persist the complete per-dataset optimizer-audit JSON or within/raw-between interval-emission flags. Those details are covered by the deterministic engine serialization tests and must be retained in the actual B2/B3 calibration outputs. The resource preflight is not a substitute for that calibration audit.

The MCSE reason is present for 100/100 primary records and 100/100 B=4,000 sensitivity records because the candidate explicitly abstains on MCSE. It is not evidence that C5 within/raw-between intervals failed.

## 7. Remaining gates — not part of B1 closure

1. Execute B2 calibration and disjoint development validation only under a separate one-use authorization, preserving the frozen K/B and seed schedules.
2. Execute B3 endpoint sensitivity on the preselected 250 datasets per F5 cell at B=1,000 and B=4,000, without using B=4,000 for coverage adjudication.
3. Inspect full per-dataset optimizer/likelihood/boundary diagnostics, all denominators, typed abstentions, interval emission, conditional and unconditional coverage, Wilson intervals, tails, widths and replay/provenance.
4. Apply the frozen §8 gates separately to both M/R cells and both components. If any gate fails or diagnostics contain an unresolved numerical state, report `NO_VALIDATED_F5_COMPONENT_INTERVAL_METHOD`; do not substitute another method.

**Final disposition:** `F5_B1_IMPLEMENTATION_AND_DETERMINISTIC_TESTS_COMPLETE`. F5 component coverage/eligibility remains OPEN pending the separately authorized B2/B3 calibration and validation. No MCSE method, new threshold, new DGP, or scientific C10 claim is introduced.
