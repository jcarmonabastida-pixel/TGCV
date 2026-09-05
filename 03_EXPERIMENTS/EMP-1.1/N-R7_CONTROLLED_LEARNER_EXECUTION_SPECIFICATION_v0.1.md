# N-R7 — CONTROLLED LEARNER EXECUTION SPECIFICATION v0.1

**Status:** FROZEN FOR PROSPECTIVE EXECUTION  
**Date:** 2026-09-05

## 1. Purpose

N-R7 defines the first authorized scientific execution of the prospective Branch N learner against the frozen N-R5.3 predictor dataset, using the separately frozen N-R4B.4 outcome corpus solely as the source of supervised labels.

This is a controlled reconstruction, not recovery of the historical EMP-1.1 executable. The historical numerical result is not a tuning target and must not be used to select or modify any implementation choice.

## 2. Frozen inputs

### Predictor-side inputs

- N-R5.3 train predictors: 30,000 records
- N-R5.3 test predictors: 10,000 records
- train predictor SHA-256: `d40e3d5f5bd8839d5c83efb1fa2a2d33f432c65c47f568516152dce578f991bd`
- test predictor SHA-256: `8ae5d84ef0bd1dc50835b1b006e20f299437f2a49395b31e057c0f016d1d3b35`
- B = 16 dimensions
- R = 58 dimensions
- BR = 74 dimensions

### Outcome-label input

The binary supervised label `Y` is obtained **only** from the frozen N-R4B.4 controlled trajectory/outcome corpus, using the one-to-one key:

`episode_id + initial_snapshot_sha256`

The outcome corpus is a separate input channel from the predictor dataset. Its trajectory fields are never passed to the learner as predictor features.

For each predictor record, exactly one matching outcome record must exist. The join is valid only if:

1. `episode_id` matches;
2. `initial_snapshot_sha256` matches exactly;
3. the outcome record is unique;
4. `Y` is binary;
5. no predictor-side field is sourced from the trajectory or terminal state.

The resulting supervised datasets are conceptually:

`X_B, Y_train` and `X_BR, Y_train` for training, and

`X_B, Y_test` and `X_BR, Y_test` for evaluation.

`Y` is a **label**, not a predictor feature. The test label is inaccessible to fitting and model selection and is consumed only at the pre-registered evaluation stage.

N-R6.1 learner specification and N-R6.2 conformance gate are also frozen inputs.

## 3. Primary comparison

Two primary arms are fitted independently using the same frozen training partition and the same registered learner configuration:

- **B arm:** 16-dimensional baseline B
- **B+R arm:** 74-dimensional concatenation `[B || R]`

No additional features, transformations, feature selection, embeddings, interactions, dimensionality reduction, scaling, or result-driven preprocessing are permitted.

## 4. Learner

Primary learner: `sklearn.ensemble.HistGradientBoostingClassifier`.

The exact N-R6.1 fixed configuration is used in both arms. No parameter may be changed after execution begins.

The training random state is 3,100,000 for both arms.

## 5. Evaluation

The test partition is never used for model fitting or model selection.

For every test episode i:

`delta_i = logloss(B_i) - logloss(BR_i)`

Primary estimand:

`Delta LogLoss = mean(delta_i)`

Positive Δ favours B+R.

Report:

- mean test LogLoss for B;
- mean test LogLoss for B+R;
- paired ΔLogLoss;
- sample SD of paired deltas;
- two-sided Monte-Carlo sign-flip p-value;
- whether Δ >= 0.04;
- whether p < 0.05.

## 6. Sign-flip inference

- 200,000 sign-flip permutations
- seed = 13,579
- each paired delta receives an independently generated ±1 sign
- statistic = absolute mean signed delta
- two-sided exceedance uses `>=` observed absolute statistic
- finite Monte-Carlo p-value convention: `(exceedances + 1) / (200000 + 1)`

The observed statistic is not included as an additional generated permutation; the +1 correction is the registered finite-sample convention.

## 7. Controls

The following controls are secondary and are executed only under their registered configurations:

1. count-only R control;
2. permuted-marginals R control;
3. RandomForest alternative.

The permuted-marginals procedure is frozen as follows:

1. use the training R matrix only;
2. leave B unchanged;
3. independently permute each of the 58 R columns across the 30,000 training rows;
4. use `numpy.random.default_rng(24681357)`;
5. preserve the exact empirical marginal of each R column;
6. preserve the original R column order;
7. construct `B || R_permuted`;
8. use the exact registered HGB configuration;
9. do not use test outcomes, trajectory data, model performance, or historical results to determine the permutation.

This is a prospective structural-disruption control, not historical implementation recovery.

## 8. Execution boundary and label firewall

The complete controlled data flow is:

`N-R5.3 predictors + N-R4B.4 labels → registered learner → test predictions → paired loss → registered inference`

The predictor path is strictly:

`initial snapshot S0 → B/R → learner features`

The label path is strictly:

`frozen N-R4B.4 trajectory/outcome corpus → Y → supervised-label interface`

The following are forbidden as predictor inputs:

- trajectory records;
- transformation IDs;
- terminal reason;
- terminal step;
- post-transition states;
- future states;
- outcome Y encoded into B or R;
- any test-derived statistic;
- historical EMP-1.1 result values as configuration targets;
- live network or registry access;
- ambient caches or undeclared files;
- post-result parameter changes.

`Y` is permitted to the learner **only as the supervised target vector**. Training labels may be consumed by `.fit()`; they must never be concatenated into X or used to construct B/R. Test labels may be consumed only after fitting is complete, to calculate test LogLoss and paired deltas.

## 9. Determinism and provenance

The execution record must contain:

- implementation SHA-256;
- learner configuration;
- Python version and implementation;
- NumPy and scikit-learn versions;
- platform;
- N-R5.3 predictor input hashes;
- N-R4B.4 outcome artifact hashes;
- output prediction/loss hashes;
- row counts and episode-ID ranges;
- model random states;
- sign-flip seed and count;
- permuted-marginals seed and procedure;
- execution timestamp;
- control statuses;
- join integrity checks;
- any exception or blocked control.

A second identical execution must reproduce the primary output byte-for-byte where serialized outputs are deterministic, or otherwise reproduce all registered numerical outputs within an explicitly pre-registered tolerance.

## 10. Historical-result firewall

The historical EMP-1.1 value is not a tuning target, acceptance target for parameter selection, or stopping criterion.

Comparison with historical results is permitted only after the new execution has been completely sealed and its provenance frozen.

## 11. Failure conditions

Execution is invalid if any of the following occurs:

- frozen input hash mismatch;
- train/test contamination;
- predictor schema or dimensionality mismatch;
- label join missing, duplicate, or hash-inconsistent;
- learner configuration drift;
- undeclared dependency;
- network access;
- historical-result-driven tuning;
- nondeterministic unaccounted output;
- test data used during fitting/model selection;
- control procedure invented after observing primary results;
- inability to pair B and B+R predictions by episode ID;
- sign-flip procedure drift;
- silent fallback to unsupported parameters;
- any trajectory/outcome field entering predictor features.

## 12. Claims permitted after successful execution

A successful N-R7 execution can support claims about the specified prospective Branch N operationalization and its out-of-sample predictive performance on the frozen synthetic corpus.

It cannot by itself establish:

- historical EMP-1.1 equivalence;
- causal universality of R;
- universal predictive superiority;
- cross-domain validity;
- literature novelty;
- validation of TGCV in general.

## 13. Gate sequence

Before execution:

1. N-R7 specification reconciliation and freeze;
2. N-R7 execution-runner preflight/conformance;
3. freeze all secondary-control procedures;
4. execute primary learner once under the frozen runner;
5. seal outputs and provenance;
6. perform independent repeat;
7. only then interpret confirmatory statistics.

**Scientific execution is authorized only after the reconciled N-R7 specification, N-R7 preflight gate, and N-R6.2 conformance gate are PASS/CLOSED.**

## 14. Reconciliation decision

The prior ambiguity concerning the source of `Y` is resolved without changing any predictor representation, learner parameter, seed, dataset partition, or control procedure.

`Y` is explicitly sourced from the already frozen N-R4B.4 trajectory/outcome corpus and joined to N-R5.3 predictor records by `episode_id + initial_snapshot_sha256`.

This reconciliation introduces no new scientific degree of freedom and does not use any observed learner result.

**N-R7 specification: FROZEN FOR PROSPECTIVE EXECUTION.**
