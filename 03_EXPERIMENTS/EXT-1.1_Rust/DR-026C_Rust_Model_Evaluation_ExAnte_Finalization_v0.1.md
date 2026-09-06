# DR-026C — EXT-1.1 Rust Model and Evaluation Ex-Ante Finalization v0.1

**Status:** PROPOSED — EX-ANTE DESIGN, NO ACCEPTANCE  
**Scope:** Finalization of open DR-026B methodological choices  
**Depends on:** DR-023, DR-024, DR-025A, DR-026A, DR-026B  

## 1. Purpose

Freeze the remaining model/evaluation choices without inspecting the outcome, fitting models, estimating associations, or using predictive performance to choose any parameter.

This document is the candidate final protocol. Acceptance remains conditional on a structural implementation audit.

## 2. Primary learner

The primary learner is **L2-regularized logistic regression** with identical learner configuration for B and T_acc.

Primary regularization:

`C = 1.0`

No outcome-driven hyperparameter search is permitted.

## 3. Exact sparse representation

### 3.1 Accessibility tokens

For every element `(target_package_id,target_version_id)` in the accepted canonical `A_rel(v_o)`, construct exactly one token:

`TACC_PAIR::<target_package_id>::<target_version_id>`

The token is represented as binary presence (`1`). Multiple occurrences of the same canonical relation are impossible under DR-026A and are not counted repeatedly.

`A_count` is represented separately as a numeric feature.

### 3.2 Baseline categorical representation

`version_str` is represented as one categorical token:

`BASE_VERSION::<version_str>`

No SemVer parsing, ordering, distance or arithmetic is performed.

### 3.3 Hashing

The primary encoding uses a fixed signed feature hash with:

- algorithm: **BLAKE2b-256**;
- input: UTF-8 bytes of the complete token string;
- digest interpretation: first 8 digest bytes as unsigned big-endian integer;
- feature index: `integer mod 2^20`;
- sign: next digest byte, even → `+1`, odd → `-1`;
- dimension: `2^20`.

Baseline and T_acc use explicit namespace prefixes in the token strings. The hash space is therefore formally common while token namespaces remain provenance-distinct.

No vocabulary is learned from the dataset. No frequency filtering, collision removal, rare-category pruning or post-hoc feature selection is permitted.

### 3.4 Collision policy

Hash collisions are accepted as an intrinsic property of the pre-specified representation. They MUST NOT be detected and selectively corrected after inspecting outcome or model performance.

## 4. Numeric features

The baseline numeric features are:

- `prior_release_count_o`;
- `package_age_days_o`;
- `D_o`.

The accessibility numeric feature is:

- `A_count`.

Each numeric feature is transformed as:

`z = (log1p(x) - mean_train) / sd_train`.

`mean_train` and `sd_train` are estimated exclusively from the training origins.

If `sd_train = 0`, the transformed feature is deterministically set to `0` for all observations.

No test observation contributes to transformation statistics.

## 5. Logistic implementation

Primary implementation target:

**scikit-learn `LogisticRegression`**, with the exact package version recorded by the execution environment audit.

Primary solver: **`liblinear`**.

Configuration:

- `penalty = l2`
- `C = 1.0`
- `solver = liblinear`
- `fit_intercept = True`
- `max_iter = 1000`
- `tol = 1e-8`
- `class_weight = None`
- `random_state = None`

The implementation must fail if convergence is not achieved rather than silently changing solver, tolerance, iterations or regularization.

The same configuration is used for B and T_acc.

## 6. Temporal partition

A chronological hold-out is mandatory.

The exact boundary is defined **algorithmically and ex ante**, without outcome inspection:

1. construct the DR-024 eligible origin population using complete 180-day follow-up;
2. obtain the minimum and maximum `created_at` among eligible origins;
3. define the temporal span between those two timestamps;
4. set the primary boundary at **80% of that elapsed temporal span** from the minimum eligible timestamp;
5. training = eligible origins with `created_at <= boundary`;
6. test = eligible origins with `created_at > boundary`.

The resulting boundary timestamp MUST be computed and recorded by the structural implementation audit before any `Y_180` label is generated.

This rule gives the test set the final 20% of the eligible observation timeline and avoids selecting a calendar date after observing outcome behavior.

No random row-level split is permitted.

## 7. Temporal/package leakage rule

Every origin representation is reconstructed using only information available at that origin boundary.

For historical baseline features:

`created_at(previous_release) < created_at(origin)`.

For T_acc, the accepted DR-020/DR-021/DR-022 resolver semantics remain normative.

The model never receives package identity as a predictive baseline feature.

No post-origin release, dependency, adoption, download, downstream or outcome information is permitted in either representation.

## 8. Outcome handling

The primary outcome remains the accepted DR-023 definition:

`Y_180(v_o)=1` iff a later release of the same package exists with

`created_at(v_o) < created_at(v') <= created_at(v_o)+180 days`.

Only complete-follow-up origins are eligible.

The outcome MUST NOT be computed until the model/evaluation specification and its structural audit have been accepted.

## 9. Primary metric

The sole primary predictive metric is mean **log loss** on the common chronological test set.

The primary comparison is:

`ΔLogLoss = LogLoss(B) - LogLoss(T_acc)`.

Positive values favor T_acc.

No threshold is applied to probabilities.

## 10. Secondary metrics

Secondary metrics are retained only as descriptive diagnostics and cannot alter the primary conclusion:

- Brier score;
- ROC AUC, only if both outcome classes occur in the test set.

Test-set outcome prevalence may be reported descriptively after confirmatory outcome construction but cannot be used to modify the protocol.

## 11. Class imbalance

Primary analysis uses:

`class_weight = None`.

No oversampling, undersampling, synthetic outcome generation, class-weight tuning or threshold optimization is permitted.

This keeps the comparison focused on probabilistic out-of-sample scoring under the same learner specification.

## 12. Inferential comparison

The primary estimand is the paired test-origin difference in log loss:

`d_i = logloss_i(B) - logloss_i(T_acc)`.

The primary reported effect remains the arithmetic mean:

`mean(d_i) = ΔLogLoss`.

Because observations from the same package are temporally related, an inferential procedure MUST NOT assume independent package-version observations without justification.

Therefore, **no inferential p-value or confidence interval is authorized in the primary result until a separate ex-ante inference gate specifies a package-aware procedure**. The predictive comparison can be reported descriptively as the pre-specified ΔLogLoss.

## 13. Deterministic ordering and replay

Before fitting, origins MUST be sorted by:

1. `created_at` ascending;
2. `version_id` ascending as deterministic tie-breaker.

B and T_acc receive exactly the same ordered origin set and partition.

A complete replay of the structural/model-construction pipeline MUST reproduce:

- eligible-origin set;
- temporal boundary;
- feature hashes;
- transformed numeric features;
- model configuration;
- predictions;
- primary metric.

Any mismatch is a protocol failure, not an invitation to alter the implementation.

## 14. Unrepresentable observations

The primary population is the complete DR-024 eligible population.

If an eligible observation cannot be represented under the frozen schema or hash encoder, the implementation MUST fail closed and identify the observation. It MUST NOT be manually repaired or silently excluded.

Any systematic technical exclusion discovered during implementation requires a new ex-ante decision before confirmatory execution.

## 15. Symmetry requirement

B and T_acc MUST differ only in the representation supplied to the common learner.

They MUST share:

- eligible population;
- outcome;
- horizon;
- temporal split;
- feature preprocessing policy where applicable;
- learner;
- regularization;
- convergence configuration;
- primary metric;
- test observations.

## 16. Structural audit required before acceptance

The implementation audit must verify, without constructing outcome labels or fitting models:

1. exact reconstruction of the eligible population;
2. deterministic calculation of the 80%-timeline boundary;
3. no incomplete-follow-up origins in the eligible frame;
4. exact token serialization;
5. exact BLAKE2b-256 hashing and signed-index rule;
6. namespace separation;
7. deterministic numeric-transform specification;
8. exact logistic configuration recorded in code;
9. same partition frame for B and T_acc;
10. absence of outcome/post-origin inputs;
11. fail-closed handling for unrepresentable observations;
12. deterministic replay of all pre-outcome construction steps.

The audit MUST NOT compute `Y_180`, outcome prevalence, predictions, log loss, associations, effect sizes or significance.

## 17. Acceptance boundary

Acceptance of DR-026C would freeze the complete primary predictive protocol except for any separately required inferential procedure.

After acceptance, no outcome-driven change to learner, hash dimension, tokenization, split, preprocessing, C, solver, metric or eligibility is permitted.

A successful DR-026C audit would permit a subsequent execution gate to construct `Y_180` and fit the two pre-specified models.

**NO CONFIRMATORY EXECUTION IS AUTHORIZED BY DR-026C ALONE.**
