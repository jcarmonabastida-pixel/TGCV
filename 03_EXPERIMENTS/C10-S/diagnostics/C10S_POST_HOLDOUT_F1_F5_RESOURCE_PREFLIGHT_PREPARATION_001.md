# C10-S — Post-holdout F1/F5 resource preflight preparation

**Record:** C10S-POST-HOLDOUT-F1-F5-RESOURCE-PREFLIGHT-PREPARATION-001  
**Date:** 2026-11-19  
**Status:** IMPLEMENTED / STATIC VALIDATION PENDING / RESOURCE EXECUTION NOT AUTHORIZED  
**Governing specification:** C10S-POST-HOLDOUT-F1-F5-DEVELOPMENT-CALIBRATION-SPEC-001 v1.0  
**Frozen specification blob:** `d1c8bae882dc2e4cd0e1caae29609561b9ebac68`  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Scope:** resource measurement only; no calibration, validation, holdout, Tier B or causal C10 execution.

## 1. Purpose and historical reuse

This package prepares the bounded resource preflight required by §7 of the frozen v1.0 specification. It does not reuse the old `C10S-NESTED-MR-COMPARATIVE-RESOURCE-PREFLIGHT-001` runner/result as the current preflight: that historical operation used 1,000 datasets per representative cell and predates the post-holdout F1 profile/F5 development package.

The implementation reuses, without copying or modifying:
- the frozen Tier A cell definitions in `c10s_nested_mr_fixtures.py`;
- the established independent dataset generator `generate_holdout_dataset`, called with a new preflight seed override;
- the matched C0/C1/C5 comparison engine;
- the F1 profile-likelihood implementation;
- the F5 fitted beta-binomial bootstrap and B1 optimizer audit;
- the existing hash-locked dependency set.

The frozen v1.0 specification and all Tier A source data/results remain unchanged.

## 2. Bounded sample and measured workload

Exactly two representative cells are used, retaining the earlier resource design's largest M/R design:

| Family | Cell | K | Workload |
|---|---|---:|---|
| F1 | `F1_balanced_M30_R20` | 100 | A2 profile LR at truth and constrained MLE; A3 C0 B=1,000 + C1 + full profile interval inversion |
| F5 | `F5_beta22_M30_R20` | 100 | B1 optimizer audit + C0 B=1,000 + C5 B=1,000; additional C5 B=4,000 on the same fixed sample to measure B3 incremental cost |

The B=4,000 operation is a resource-only sensitivity benchmark on the same 100 F5 preflight datasets. It is not a calibration replicate, does not enter any denominator, and does not replace the frozen B=1,000 primary. The future B3 workload remains 250 selected calibration-bank datasets per F5 cell (500 total).

The F1 profile inversion requires a numerical LR cutoff to exercise its complete computational path. The runner uses `3.841458820694124` strictly as a **non-calibrated computational benchmark**. It is not used to score coverage, choose a cutoff, tune a method, or make an inferential statement. A2's calibration-statistic work is timed separately using the known DGP truth only for the profile LR statistic and the data-derived constrained MLE.

## 3. Seed separation and provenance

New schedule and namespace:

- Schedule: `C10S_POST_HOLDOUT_F1_F5_DEV_PREFLIGHT_SEEDS_1.0`
- Namespace: `c10s_post_holdout_f1_f5_dev_preflight_v1`
- Streams: dataset, C0 bootstrap, C5 B=1,000, C5 B=4,000.

Before generating any sample, the runner checks the full 100-replicate seed inventory for the representative cells against:
- `C10S_NESTED_MR_SEED_SCHEDULE_1.0` (historical fixture/v002 namespace);
- `C10S_NESTED_MR_COMPARATIVE_HOLDOUT_SEEDS_1.0` (executed Tier A v1.0);
- `C10S-COMPARATIVE-RESOURCE-PREFLIGHT-1.0` (earlier resource-only sample).

It also checks collisions within the new preflight streams. Any collision is a hard stop. The output manifest records each dataset ID, stream seeds and SHA-256 digest of the generated rows; raw datasets are not retained.

The runtime record binds the approved code commit, authorization commit/ID, spec hash, full source dependency closure, dependency-lock hash, Python/NumPy/platform identity and GitHub run metadata.

## 4. Resource projection

The runner records separate F1 timings for:
- A2 profile LR calibration statistic;
- A3 matched comparison plus full profile interval inversion.

It records F5 B=1,000 matched C0/C5 time separately from the incremental C5 B=4,000 sensitivity time. It then projects the frozen work-package sizes:
- F1 A2: 30,000 datasets (six cells × 5,000);
- F1 A3: 30,000 datasets (six cells × 5,000);
- F5 B2: 20,000 datasets (two cells × 5,000 calibration and 5,000 validation);
- F5 B3: 500 selected datasets for the B=4,000 incremental run.

Projection is linear per-dataset extrapolation from one representative M30/R20 cell per family. It is advisory, not a guarantee. Peak RSS is reported as a process-lifetime high-water mark; the value is explicitly labelled cumulative and must not be misread as an independent per-cell memory measurement.

No K, B, cell, method, acceptance criterion or frozen specification value is changed. If measured cost exceeds the available execution budget, the workflow must stop at resource review; it must not reduce the frozen workload.

## 5. Fail-closed execution boundary

The runner refuses to execute unless called with an explicit internal authorization flag; its CLI additionally requires the workflow-set environment sentinel, which is set only after the one-use validator passes.

The separate authorization validator binds:
- the exact frozen v1.0 spec;
- exact code commit as the sole parent of the authorization commit;
- representative cells and K/B values;
- benchmark-only F1 cutoff semantics;
- workflow, validator, runner, tests, dependency lock and full estimator/source dependency hashes;
- a dedicated one-use branch and unexpired explicit approval.

The dedicated workflow can run only on a branch named `research/c10s-post-holdout-resource-preflight-auth-<authorization_id>`, after a commit that changes only the authorization JSON and whose message contains the required approval phrase. It checks out and executes the exact approved parent code commit.

The authorization scope is only `C10S_POST_HOLDOUT_F1_F5_RESOURCE_PREFLIGHT_ONLY`. Calibration, validation, comparative holdout, Tier B and causal C10 execution must all be explicitly false.

## 6. Output and adjudication exclusions

The workflow uploads:
- `post_holdout_resource_preflight.json`;
- `post_holdout_resource_preflight_summary.json`.

The output contains runtime, peak RSS, typed abstentions, optimizer fit statuses, untyped failures, seed-collision audit, code/dependency identities and projected full-workload cost.

It deliberately does not call `adjudicate_matched_datasets`, emit coverage/width/bias metrics, select a cutoff, generate calibration or validation banks, or retain raw preflight datasets. All records are marked resource-only and excluded from calibration and validation.

## 7. Current gate status

| Gate | Status |
|---|---|
| Frozen spec v1.0 recovered and unchanged | PASS |
| Historical preflight distinguished and not reused | PASS |
| New 100-per-cell runner implemented | IMPLEMENTED |
| New seed namespace and historical collision guard | IMPLEMENTED |
| C0/C5 B=1,000 and C5 B=4,000 workload instrumentation | IMPLEMENTED |
| F1 A2/A3 workload instrumentation | IMPLEMENTED |
| One-use authorization validator/workflow | IMPLEMENTED |
| Static tests and exact-commit workflow | PENDING |
| Resource preflight execution | NOT AUTHORIZED / NOT RUN |
| Full calibration/validation execution | NOT AUTHORIZED / NOT RUN |

**No resource sample has been executed by this preparation.** The only permitted next technical validation is the deterministic static workflow. The resource workflow remains dormant until the user explicitly authorizes this exact one-use resource-only operation.
