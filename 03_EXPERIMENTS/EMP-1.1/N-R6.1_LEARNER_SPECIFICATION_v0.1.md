# N-R6.1 LEARNER SPECIFICATION v0.1

**Date:** 2026-09-05  
**Status:** PROPOSED FOR PROSPECTIVE FREEZE  
**Branch:** N — controlled prospective reconstruction  
**Historical recovery:** NO

## 1. Purpose and boundary

N-R6.1 defines the learner and statistical-analysis procedure to be applied to the already frozen N-R5.3 predictor dataset.

This is a **prospective controlled learner specification**, not recovery of the historical EMP-1.1 executable implementation. The historical record specifies the learner family and major confirmatory parameters but does not recover the exact historical hyperparameter dictionary. Missing historical executable details are therefore not silently reconstructed.

No learner execution, model fitting, test-set scoring, permutation test, or confirmatory inference is authorized by this specification alone. Execution requires N-R6.2 conformance PASS/CLOSED.

## 2. Frozen inputs

The learner consumes only the frozen N-R5.3 predictor dataset:

- train: 30,000 records;
- test: 10,000 records;
- train seed: 3,100,000;
- test seed: 4,100,000;
- B dimension: 16;
- R dimension: 58;
- BR dimension: 74;
- train predictor SHA-256: `d40e3d5f5bd8839d5c83efb1fa2a2d33f432c65c47f568516152dce578f991bd`;
- test predictor SHA-256: `8ae5d84ef0bd1dc50835b1b006e20f299437f2a49395b31e057c0f016d1d3b35`.

The predictor dataset is frozen by N-R5.3.

## 3. Primary hypothesis and estimand

Primary hypothesis:

> `R` adds reproducible out-of-sample predictive utility beyond conventional snapshot representation `B`.

Null hypothesis:

> `R` adds no incremental out-of-sample predictive utility beyond `B`.

Primary estimand, per test episode `i`:

`delta_i = logloss(B_i) - logloss(BR_i)`

and aggregate paired improvement:

`Delta LogLoss = mean(delta_i)`.

Positive values favour `B+R`.

Historical confirmatory parameters recovered from the frozen protocol:

- alpha = 0.05;
- historical practical threshold delta = 0.04;
- paired Monte-Carlo sign-flip permutations = 200,000;
- permutation seed = 13,579.

These are protocol parameters, not parameters to be tuned against the present data.

## 4. Predictor arms

Two primary arms are evaluated on exactly the same train/test episode identities and outcomes:

### Arm B

Input = the frozen 16-dimensional baseline vector:

`B = [n_components, q1, q2, q3, one_hot(O01...O12)]`

### Arm B+R

Input = direct concatenation:

`BR = B || R`

with 74 dimensions.

No additional variables, interactions, embeddings, dimensionality reduction, feature selection, scaling, or post-hoc feature engineering are permitted.

## 5. Primary learner

The primary learner family is:

`sklearn.ensemble.HistGradientBoostingClassifier`

The same learner configuration must be used for Arm B and Arm B+R. The only allowed difference between the two primary fits is the predictor matrix supplied to the learner.

### 5.1 Prospective fixed configuration

Because the exact historical hyperparameter dictionary was not recovered, N-R6.1 adopts the estimator's documented standard configuration as an explicit **prospective reconstruction choice**, with all relevant parameters made explicit rather than relying on library defaults implicitly.

Configuration:

```text
loss = "log_loss"
learning_rate = 0.1
max_iter = 100
max_leaf_nodes = 31
max_depth = None
min_samples_leaf = 20
l2_regularization = 0.0
max_features = 1.0
max_bins = 255
categorical_features = None
early_stopping = "auto"
scoring = "loss"
validation_fraction = 0.1
n_iter_no_change = 10
tol = 1e-7
random_state = 3100000
class_weight = None
```

The configuration is fixed before any scientific execution. It is not selected, altered, or tuned using the historical result or any test-set outcome.

If the installed scikit-learn version does not support one of these explicit parameters, execution must fail closed and N-R6.1 must be revised; the parameter must not simply be dropped or silently substituted.

## 6. Randomness and fitting determinism

- `random_state = 3100000` is fixed for the primary learner in both arms.
- Training data ordering is the canonical N-R5.3 ordering.
- Test data are never used for fitting or early-stopping selection beyond the learner's explicitly configured internal training validation mechanism.
- No external random state, global RNG, network state, or ambient cache may influence execution.
- B and B+R must be fitted independently but under identical learner configuration and training observations.

## 7. Evaluation

After both fitted models are sealed, compute per-episode test LogLoss for B and B+R using the same locked test outcomes.

The paired difference vector `delta_i` is constructed by episode identity. No reordering may alter the pairing.

Primary reported quantities:

- mean LogLoss for B;
- mean LogLoss for B+R;
- `Delta LogLoss`;
- standard deviation of paired deltas;
- paired Monte-Carlo sign-flip p-value;
- whether `Delta LogLoss >= 0.04`;
- whether `p < 0.05`.

The practical threshold and statistical alpha are both reported; neither is used to tune the learner.

## 8. Paired Monte-Carlo sign-flip test

The confirmatory test uses the frozen paired differences `delta_i`.

For each of 200,000 permutations, independently assign a sign of +1 or -1 to every paired difference and calculate the resulting mean signed difference. The permutation RNG is independently seeded with `13,579`.

The two-sided empirical p-value must use one fixed, explicitly implemented finite-sample convention and that convention must be frozen in N-R6.2 before execution. No alternative p-value convention may be selected after observing the result.

The observed mean difference is never included or excluded selectively after inspection.

## 9. Controls

The following controls remain registered from the EMP-1.1 protocol:

### 9.1 Count-only R control

Replace the full 58-dimensional R representation by its registered accessibility-count information only. The exact control encoding must be derived from the frozen N-R1.3/N-R5 specifications without introducing additional variables.

### 9.2 Permuted-marginals R control

Construct a control in which R feature marginals are preserved while cross-feature structural association is disrupted. The permutation procedure, seed, and exact implementation must be frozen before execution. It must not inspect outcomes or model performance.

### 9.3 RandomForest alternative

A RandomForestClassifier is retained as an alternative learner control. It is not the primary confirmatory learner and cannot replace the primary HGB analysis.

Prospective fixed configuration:

```text
n_estimators = 100
criterion = "gini"
max_depth = None
min_samples_split = 2
min_samples_leaf = 1
max_features = "sqrt"
bootstrap = True
class_weight = None
random_state = 3100000
n_jobs = 1
```

This control configuration is fixed prospectively and is not tuned to the historical result.

## 10. Leakage and separation requirements

The following are prohibited:

- use of trajectory steps as predictor variables;
- use of terminal reason as a predictor;
- use of outcome Y as a predictor;
- use of test outcomes during fitting or model selection;
- use of future state information;
- use of historical result values as tuning targets;
- live registry/network access;
- ambient external data;
- post-hoc feature selection based on test performance;
- changing learner configuration after seeing confirmatory results.

The predictor boundary remains:

`N-R4B.4 initial snapshot -> N-R5.2 B/R -> learner`

The outcome boundary remains separate:

`N-R4B.4 initial snapshot -> trajectory -> Y`

## 11. Historical-result firewall

The historical result

`Delta LogLoss = 0.07942359585000518`

must not be read by the learner implementation, conformance runner, or execution configuration. It may be referenced only in provenance/audit documentation as a historical empirical record.

In particular, it must not be used to choose:

- hyperparameters;
- seeds;
- feature subsets;
- control procedures;
- stopping criteria;
- statistical conventions;
- data exclusions;
- preprocessing.

## 12. Reproducibility requirements

Before scientific execution, N-R6.2 must verify:

1. exact learner class and supported parameters;
2. exact parameter dictionary;
3. exact library/runtime versions;
4. deterministic training behavior;
5. canonical train/test ordering;
6. locked predictor hashes;
7. outcome join by episode identity;
8. no predictor/outcome leakage;
9. fixed permutation procedure and seed;
10. fixed control definitions;
11. no network dependency;
12. independent rerun byte/result identity to the registered tolerance.

## 13. Claims permitted after successful execution

If the learner execution and confirmatory analysis pass all registered gates, the resulting evidence may support a claim about the specified Branch N operationalization and its out-of-sample predictive performance.

It will not, by itself, establish:

- historical equivalence to the unrecovered EMP-1.1 executable;
- causal universality of TGCV;
- universal superiority of R;
- literature novelty;
- cross-domain validity.

## 14. Gate status and next step

**N-R6.1 status: PROPOSED FOR PROSPECTIVE FREEZE.**

The exact historical HGB hyperparameters remain unrecovered. The explicit prospective configuration above resolves that missing executable detail without claiming historical recovery and without using the historical result as a tuning target.

**Next gate:** N-R6.2 — Learner Conformance.

No learner execution is authorized until N-R6.1 is frozen and N-R6.2 passes.
