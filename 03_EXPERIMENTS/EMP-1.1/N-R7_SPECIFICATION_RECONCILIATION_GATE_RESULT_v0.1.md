# N-R7 — SPECIFICATION RECONCILIATION GATE RESULT v0.1

**Date:** 2026-09-05  
**Status:** **PASS / CLOSED**  
**Branch:** N — controlled prospective reconstruction

## Decision

The pre-execution ambiguity concerning the supervised label `Y` has been resolved without changing the predictor representation, learner configuration, seeds, frozen predictor dataset, or registered secondary controls.

The reconciled N-R7 specification is now **FROZEN FOR PROSPECTIVE EXECUTION**.

## Reconciled data boundary

Predictor path:

`N-R5.3 initial-snapshot-derived predictors → B / R / B+R`

Label path:

`N-R4B.4 controlled trajectory/outcome corpus → Y`

Join key:

`episode_id + initial_snapshot_sha256`

The join must be one-to-one, exact, and hash-consistent. `Y` is a supervised target only; trajectory fields, terminal fields, post-transition states, and outcome information cannot enter B/R/BR.

Training labels may be passed to `.fit()` as the target vector. Test labels may be consumed only after fitting, for the pre-registered evaluation metrics.

## No new scientific degree of freedom

The reconciliation does not alter:

- N-R5.3 predictor artifacts or hashes;
- B=16, R=58, BR=74;
- HGB configuration;
- RandomForest configuration;
- sign-flip count/seed;
- permuted-marginals procedure/seed;
- train/test partitions;
- historical-result firewall.

No observed scientific result was used in making this decision.

## Supporting frozen evidence

- N-R4B.4 corpus: PASS/CLOSED, 30,000 train + 10,000 test, learner/inference not executed.
- N-R6.2 current conformance: PASS/CLOSED on learner SHA `e9d2f61da49de0fa76f47efea31f8e8dcd4d4411afcd5ec99bbc744ab937bc0e`.
- N-R7 preflight v0.2: PASS/CLOSED.

## Scientific execution status

No scientific learner execution has been performed by this reconciliation gate.

`scientific_execution = NOT_PERFORMED`

`learner_execution = NOT_PERFORMED`

`confirmatory_inference = NOT_PERFORMED`

## Authorization

The reconciled N-R7 specification, together with the already closed N-R7 preflight and current N-R6.2 conformance, now authorizes the **first controlled scientific learner execution**.

Execution must occur exactly under the frozen specification. Any join failure, hash mismatch, leakage indication, configuration drift, or undeclared dependency is a blocking failure.
