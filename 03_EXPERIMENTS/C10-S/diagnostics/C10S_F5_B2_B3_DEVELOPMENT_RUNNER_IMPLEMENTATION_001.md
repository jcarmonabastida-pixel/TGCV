# C10-S — F5 B2/B3 development runner implementation

**Record:** C10S-F5-B2-B3-DEVELOPMENT-RUNNER-IMPLEMENTATION-001  
**Date:** 2026-11-19  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Code commit statically validated:** `1ceca1550606407099df9bc1f2df45ddcd6e2ebb`  
**Status:** IMPLEMENTED / STATIC VALIDATION PASS / NUMERICAL EXECUTION NOT AUTHORIZED

## 1. Scope fixed by the frozen specification

The runner implements F5 only, within the existing C5 beta-binomial candidate. It does not change the estimator, bootstrap law, DGP, estimands, K/B values, coverage criteria, or the frozen specification v1.0.

| Phase | Per F5 cell | Two-cell total |
|---|---:|---:|
| B2 calibration bank | K=5,000; C0 B=1,000; C5 B=1,000 | 10,000 datasets |
| B2 disjoint development-validation bank | K=5,000; C0 B=1,000; C5 B=1,000 | 10,000 datasets |
| B3 endpoint sensitivity | 250 selected calibration datasets; C5 B=1,000 and B=4,000 | 500 datasets, each run at both B values |

Cells are exactly `F5_beta22_M10_R5` and `F5_beta22_M30_R20`. The F5 DGP remains beta-binomial with alpha=2 and beta=2. The validation bank is development validation, not a confirmatory holdout.

## 2. Seed and dataset integrity

Seed schedule ID: `C10S_POST_HOLDOUT_F1_F5_DEV_CAL_SEEDS_1.0`; namespace: `c10s_post_holdout_f1_f5_dev_cal_v1`.

Distinct streams are implemented for:
- `f5_optimizer_calibration_dataset`
- `f5_optimizer_validation_dataset`
- `f5_c0_bootstrap`
- `f5_c5_bootstrap`
- `f5_endpoint_sensitivity_b1000`
- `f5_endpoint_sensitivity_b4000`

Before generation, the hard collision guard reconstructs the original Tier A v002, executed comparative holdout v1.0, earlier comparative resource-preflight, and the separately authorized post-holdout resource-preflight seed inventories. It checks all new calibration, validation, C0/C5, and selected B3 stream seeds for historical and internal collisions.

B3 selection is precomputed from calibration dataset IDs alone, before any B2 C5 result is examined. Rule: SHA-256 of `schedule_id|B3_SELECTION|cell_id|dataset_id`, ascending digest, first 250 per cell. B3 regenerates each selected dataset from its original calibration seed and requires an exact row-hash match. Calibration and validation dataset IDs and dataset seeds are checked disjoint.

## 3. B2 records and frozen component adjudication

The runner writes per-dataset JSONL for each cell and bank. Each record retains dataset ID/seed/row hash, C0 and C5 bootstrap seeds and B, full comparison output, truth, fit status, typed failure reason, and the complete per-dataset F5 optimizer-audit JSON (three primary starts, independent optimizer, scores, Hessians, curvature, boundary distances and likelihood-limit contrasts).

Per-cell/bank summaries report:
- C0 and C5 separately for within and raw-between only;
- point and interval emission, conditional and unconditional coverage, Wilson intervals, lower/upper misses, interval width, point bias and RMSE;
- F5 fit and optimizer-status frequencies;
- summaries of fitted mean probability, concentration, alpha, beta, log-likelihood, score norm, profile curvature and minimum start-to-bound distance;
- typed abstentions and denominator counts.

No pooling is allowed across cells, banks, methods or components. C5 component gates are applied separately to each cell × bank × target:
1. exact denominator K=5,000;
2. conditional coverage in [0.93, 0.97];
3. 95% Wilson interval contains 0.95;
4. interval emission rate at least 0.95;
5. no unresolved numerical optimizer state.

The numerical diagnostic gate requires an interior fit, `OPTIMIZER_CONCORDANT`, independent optimizer success, all three primary starts successful with finite terminal coordinates/gradient/bound distances, finite selected and independent Hessians, and finite score/curvature/likelihood-disagreement diagnostics. Raw concentration/identification diagnostics are retained; no binary weak-identification threshold is invented. A passing result is labelled only `ELIGIBLE_FOR_LATER_CONFIRMATORY_PROTOCOL_NOT_CONFIRMATORY`. Any failure yields `NO_VALIDATED_F5_COMPONENT_INTERVAL_METHOD`.

## 4. B3 endpoint-sensitivity diagnostics

B3 uses the same selected calibration rows, with independent bootstrap streams at B=1,000 and B=4,000. It reports:
- endpoint rank position and binomial rank standard deviation `sqrt(B p (1-p))`;
- discrete 95% binomial order-statistic rank bounds from `scipy.stats.binom.ppf`;
- lower/upper endpoint changes B=4,000 minus B=1,000;
- interval-width changes B=4,000 minus B=1,000.

These are Monte Carlo sensitivity diagnostics only. B3 is not used for coverage adjudication and creates no new acceptance threshold. F5 MCSE interval construction remains an explicit abstention and is guarded against being emitted; MCSE is not adjudicated.

## 5. Authorization and execution guard

The production workflow is push-triggered only on a dedicated branch matching `research/c10s-f1-f5-dev-cal-auth-<authorization_id>`, and only when the one-use authorization JSON is added. The validator requires:
- explicit APPROVED authorization and unexpired UTC window;
- exact F5-only scope, exact K/B/cell roster and B3 selection rule;
- F1 A2/A3, Tier B, comparative holdout, C10 scientific execution and MCSE interval construction all explicitly false;
- the authorization commit's sole parent to equal the approved code commit;
- the authorization commit to change only the authorization JSON;
- exact hashes for spec, runner, DGP/fixture generator, comparison engine, C5 bootstrap/diagnostics, oracle, dependency lock, workflow and validator.

The only committed authorization artefact is a DRAFT template. No approved authorization file or authorization branch exists. The execution workflow has not been triggered. No B2/B3 datasets have been generated.

## 6. Static validation

- Workflow: `44608692364`
- Exact commit: `1ceca1550606407099df9bc1f2df45ddcd6e2ebb`
- Hash-locked dependencies: PASS
- Compilation: PASS
- Deterministic comparator/oracle suite: **168 tests PASS**
- New runner tests cover deterministic/disjoint seeds, B3 outcome-independent selection, frozen component gates, denominator checks, strict optimizer diagnostic gate, B3 row regeneration/hash equality, independent B streams, rank uncertainty and explicit MCSE exclusion.
- Authorization tests cover DRAFT rejection, exact-parent/hash-bound approval, scope expansion rejection and frozen K/B rejection.

A transient test-fixture scope error in an earlier static run was corrected. The exact final commit above passed the complete suite. No numerical calibration or validation run was launched.

## 7. Resource estimate and next gate

Using the measured F5 preflight runtime, the F5-only B2+B3 workload is projected at approximately **2.74 hours**. This is a linear estimate from the M30/R20 resource sample; actual runtime may vary by cell. The workflow timeout is six hours.

**Next gate:** obtain explicit one-use authorization for this exact F5-only B2/B3 scope. After execution, inspect all raw records, denominators, diagnostics, interval emission, coverage/Wilson gates, B3 sensitivity and artifact hashes. This development result cannot by itself establish confirmatory validity or a TGCV causal claim.
