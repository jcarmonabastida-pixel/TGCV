# N-R7 Run 01 ↔ Run 02 — Reproducibility Concordance Gate v0.1

**Date:** 2026-09-05  
**Status:** PASS / CLOSED

## Decision

The N-R7 Run 01 ↔ Run 02 concordance gate is **PASS/CLOSED**.

Run 02 reproduced the frozen N-R7 scientific execution exactly. The complete scientific result set and the test prediction artifact are byte-identical to Run 01; the execution-specific provenance record differs, as expected.

This establishes **computational reproducibility / deterministic repeatability under the frozen conditions**. It is not an independent-data statistical replication.

This distinction follows the National Academies' definition of computational reproducibility as consistent computational results from the same input data, computational steps, methods/code, and analysis conditions; replicability instead concerns studies answering the same question with newly obtained data. citeturn0search0turn0search3

## Concordance criteria

| Criterion | Result |
|---|---|
| Same frozen predictor dataset | PASS |
| Same frozen trajectory/outcome corpus | PASS |
| Same learner specification | PASS |
| Same controls and seeds | PASS |
| Same primary result values | PASS |
| Same control result values | PASS |
| Same test prediction artifact SHA | PASS |
| No result-driven tuning between runs | PASS |
| Run 02 artifact integrity sealed | PASS |
| Execution-specific provenance retained separately | PASS |

## Primary concordance

Run 01 and Run 02 both produced:

- base log loss: `0.36012118987132763`
- TGCV log loss: `0.2301141852417799`
- delta log loss: `0.13000700462954773`
- SD(delta): `0.47085270367973225`
- paired sign-flip p: `4.9999750001249995e-06`
- alpha criterion: PASS
- practical-delta criterion: PASS

## Controls concordance

**Count-only:**
- delta = `-0.00205673981071788`
- practical-delta criterion = FAIL
- p = `0.023114884425577874`

**Permuted marginals:**
- delta = `-0.0045819302273459326`
- practical-delta criterion = FAIL
- p = `4.9999750001249995e-06`

**Random forest:**
- delta = `0.42405530131964725`
- practical-delta criterion = PASS
- p = `4.9999750001249995e-06`

All control values are identical across Run 01 and Run 02.

## Artifact concordance

The following five artifacts are byte-identical across the two executions:

1. `control_count_only_results.json`
2. `control_permuted_marginals_results.json`
3. `control_random_forest_results.json`
4. `primary_results.json`
5. `primary_test_predictions.jsonl`

Prediction SHA-256 in both runs:

`3C576ED6304BAA2EF6ACF8FC21D10DB2E90D284CEBA72563BFC3DECF398E223F`

The execution-specific provenance hashes are intentionally different:

- Run 01: `50DE35232E3857A01392D0C24C53DEC356D6E3BE1F9B0509ECC2F7E9889A3ABC`
- Run 02: `3CA93DF2DE57EEFD9EBF7285D16FE9AA0621D4663FF3035E9AF56E90DD28F32F`

Run 01 and Run 02 therefore remain distinguishable as executions while sharing the same scientific outputs.

## Scientific interpretation authorized by this gate

The combined Run 01/Run 02 record supports the following limited statement:

> Under the frozen N-R5.3 predictor dataset, frozen N-R4B.4 outcome corpus, frozen N-R6 learner and controls, fixed seeds, fixed implementation and execution conditions, N-R7 produces exactly reproducible scientific outputs.

The primary result remains positive under the pre-registered alpha and practical-delta criteria, while the count-only and permuted-marginals controls do not meet the practical-delta criterion. The random-forest control also meets the practical-delta criterion and therefore limits attribution of the observed predictive gain to the specific HGB learner architecture alone.

## Claims explicitly not authorized

This gate does **not** establish:

- historical EMP-1.1 equivalence;
- replication on newly sampled data;
- generalization beyond Branch N's controlled synthetic domain;
- cross-domain validity;
- novelty of TGCV;
- universality of the mechanism;
- validation of TGCV as a general theory;
- causal identification of the observed predictive association.

In particular, exact Run 01 ↔ Run 02 agreement must not be presented as independent statistical replication because both executions use the same frozen inputs and deterministic seeds.

## Governance consequence

N-R7 Run 01 and Run 02 are jointly sealed as the reproducible execution record for this frozen Branch N experiment. No further execution is required for the reproducibility gate.

Any subsequent scientific work must be a separately specified and frozen extension, robustness analysis, new-data replication, or new-domain experiment; it must not alter this sealed record or retroactively tune the present result.
