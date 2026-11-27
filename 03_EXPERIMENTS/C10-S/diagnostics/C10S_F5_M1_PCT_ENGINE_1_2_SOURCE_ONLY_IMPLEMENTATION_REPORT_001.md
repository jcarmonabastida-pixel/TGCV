# C10-S — M1-PCT engine 1.2 source-only implementation report 001

**Date:** 2026-11-27  
**Status:** SOURCE IMPLEMENTED — NOT EXECUTED — REVIEW REQUIRED  
**Branch:** `research/c10s-m1-engine12-source-only-20261127`  
**Execution authorization:** NONE  
**Scientific execution:** NOT AUTHORIZED

## 1. Purpose and scientific boundary

This implementation is limited to making the existing M1-PCT interval candidate representable beside frozen C0 and unchanged C5. It is not a new scientific workstream, does not select M1, and does not authorize calibration or validation.

The only reason to retain this adapter is to support transparent interval-emission and coverage comparison where that comparison is still scientifically useful. It must not delay the primary C10-S mission: establish reasonable statistical operating characteristics for the selected estimator/inference path, then use that evidence in the causal attribution experiment.

The historical M1 development pilot already reported 4% interval emission in M10/R5 and 100% in M30/R20. Its decision was **M1-PCT NOT SELECTED for Tier-A**. This implementation does not reverse that decision. Unless a later source review identifies a specific scientific reason, no further M1 tuning or M1-specific simulation should be scheduled merely because this adapter now exists.

## 2. Source changes

Added:

- `harness/c10s_nested_mr_comparative_inference_engine_1_2_m1.py`
- `harness/test_c10s_nested_mr_comparative_inference_engine_1_2_m1.py`

The versioned path:

1. Calls the existing engine 1.1 F5 path to obtain its C0 and C5 records.
2. Retains the complete legacy record without mutating C0, C5, their method IDs, or their fit/interval provenance.
3. Runs M1 only on the binary per-world count vector, under its existing fit contract.
4. Copies M1 intervals as M1 interval outputs; it does not recenter or transform them.
5. Uses the common `observed_nested_mr_result` point fields for all three methods' shared point comparisons.
6. Retains M1 beta-binomial point estimates only in the original M1 result as auxiliary model diagnostics.
7. Preserves original-fit/bootstrap abstentions and counts all datasets in the interval-emission denominator.
8. Requires distinct unsigned 64-bit C0, C5 and M1 bootstrap seeds for each call.
9. Keeps unrelated F5 profile diagnostics disabled in the legacy call, avoiding additional optimizer work unrelated to the interval challenger.
10. Uses a separately versioned adjudicator for the exact three-method roster and paired independent truth.

M1 MCSE point and interval estimates are explicitly unavailable; the adapter reports `M1_MCSE_INTERVAL_NOT_IMPLEMENTED`. It does not reuse the common projected MCSE point estimate as an M1 estimate.

## 3. Test source

Seventeen source-level contract tests were added, covering:

- exact three-method roster;
- preservation of C0/C5 legacy records;
- unchanged M1 interval values;
- common raw point fields;
- separation of M1 model points;
- original-fit and bootstrap-failure abstentions, with model point diagnostics suppressed when the original fit is inadmissible;
- truth-ID integrity, including duplicate IDs;
- all-dataset emission denominator;
- conditional and unconditional coverage;
- design stratification;
- distinct per-call seed routing;
- no overwrite of C5 identity;
- explicit M1 MCSE non-implementation and interval-provenance consistency.

**Tests have not been executed.** No Python compilation, local test, GitHub Actions workflow, benchmark, simulation, calibration, holdout or scientific run has been launched.

## 4. Remaining pre-execution requirement

The adapter requires three distinct caller-supplied C0/C5/M1 seeds per dataset and preserves the seed values in the underlying method results. The source tests cover seed routing and collision rejection within a dataset, not cross-bank namespace disjointness. It does **not** establish or validate a development-versus-validation namespace manifest. That manifest, its disjointness audit, and the prospective K/B/runtime/precision justification remain mandatory before any future numerical operation. No seed namespace is authorized or created by this source-only implementation.

## 5. Explicit non-actions

- No changes to engine 1.1, C0, C5 or their historical records.
- No changes to frozen Tier-A protocols or holdout data.
- No changes to causal architecture, Analyzer/Evaluator, `V_cont` or `theta_A`.
- No workflow or CI changes.
- No writes to `main`.
- No method-selection or calibration claim.

## 6. Next scientific decision

The next decision is **not** to expand instrumentation. First review this source-only adapter. If it is retained, separately authorize its deterministic contract tests. After those tests, the work must return to the shortest statistically defensible route for coverage/emission, bias/RMSE and precision assessment of the methods that remain viable.

M1 is not presumed viable: its recorded M10/R5 emission failure remains binding. Do not spend another simulation batch on M1 without a written, scientifically justified reason that does not relax its frozen abstention rule or the inherited emission requirement.

Only after statistical operating characteristics are adequately established should the programme proceed to the causal attribution estimand `theta_A(q_X*, r_common; V_cont)` and the target relation `Delta T_acc -> Delta V`.

**Disposition:** implementation source is present for review; execution remains prohibited pending a separate explicit authorization.
