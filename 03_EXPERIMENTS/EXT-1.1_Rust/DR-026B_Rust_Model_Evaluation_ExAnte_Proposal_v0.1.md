# DR-026B — EXT-1.1 Rust Model and Evaluation Ex-Ante Proposal v0.1

**Status:** PROPOSED — EX-ANTE DESIGN, NO ACCEPTANCE  
**Scope:** Concrete model/evaluation candidate under DR-026  
**Depends on:** DR-023, DR-024, DR-025A, DR-026A  

## 1. Purpose

Convert the open DR-026 questions into a single deterministic candidate protocol that can be audited and, if accepted, frozen before any confirmatory outcome computation or model fitting.

This document is a design proposal, not an empirical result. No outcome prevalence, association, effect size, significance result or predictive performance has been inspected in choosing the proposal.

## 2. Primary scientific comparison

For the same eligible origin population and frozen outcome `Y_180`, compare:

- **B-model:** frozen conventional baseline `B(v_o)` from DR-025A;
- **A-model:** frozen accessibility representation `TAcc_repr(v_o)` from accepted DR-026A.

The models use the same learner, partitioning, tuning protocol, scoring rule and test origins. Only the representation supplied to the learner differs.

The primary comparison quantity is:

`ΔLogLoss = LogLoss(B) - LogLoss(A)`

so positive values favor the accessibility representation. The primary metric is mean out-of-sample log loss on the common held-out test set. The sign convention is fixed before execution.

## 3. Primary model family

**Candidate primary learner: L2-regularized logistic regression.**

Rationale:

- binary outcome is compatible with logistic probability modeling;
- log loss is a proper probabilistic scoring rule aligned with the model's probability output;
- deterministic implementation is available;
- L2 regularization controls the very high dimensionality of relational/hash representations;
- the same linear learner can consume both sparse baseline and sparse accessibility representations;
- coefficient-level interpretability is secondary and is not required for the primary test.

No alternative learner will be selected using observed outcome performance.

## 4. Baseline representation for the learner

The accepted baseline object remains:

`B(v_o) = (V_o, H_o, A_o, D_o)`

with primary numerical form:

`B_num(v_o) = encode(V_o) || prior_release_count_o || package_age_days_o || D_o`.

For the proposed learner:

- `version_str` is represented as one categorical token;
- numeric features are retained as numeric values;
- no package identity feature is included;
- no SemVer ordering or arithmetic is applied;
- no target encoding is used.

## 5. Accessibility representation for the learner

The accepted DR-026A object is:

`TAcc_repr(v_o) = (A_rel(v_o), A_count(v_o))`

where `A_rel` contains canonical `(target_package_id,target_version_id)` pairs.

For the proposed sparse learner encoding, each resolved pair becomes a deterministic categorical token:

`TACC_PAIR::<target_package_id>::<target_version_id>`.

Each token receives value 1 for the origin release if present. `A_count` is added as one numeric feature.

No target package/version token is generated from unresolved declarations. No additional target statistics are added.

The origin package ID is not encoded as a feature.

## 6. Fixed sparse encoding

Because the accessibility vocabulary can be very large, the proposal uses a **fixed feature-hashing representation** rather than a vocabulary learned from the complete dataset.

Proposed hash space:

`m = 2^20` signed sparse dimensions.

The hashing algorithm, byte encoding, namespace prefixes and sign convention MUST be frozen exactly before confirmatory execution. Hashing is applied independently to the categorical token namespaces of B and T_acc so that representation provenance remains explicit.

No vocabulary is learned from test observations. No frequency filtering, rare-category removal, or post-hoc feature selection is permitted.

## 7. Numeric transformations

For the baseline numeric features `prior_release_count_o`, `package_age_days_o`, and `D_o`, the proposal uses:

`log1p(x)`

followed by standardization using statistics estimated from the training data only.

The accessibility `A_count` receives the same `log1p` transformation and training-only standardization.

The version categorical token is not numerically transformed.

If a training standard deviation is zero, the corresponding standardized value is deterministically set to zero.

No test-set statistics are used for transformations.

## 8. Missing and invalid values

Under the accepted DR-024/DR-025A structural audit, required origin timestamps, identity fields and version strings are complete. Therefore no primary missing-value imputation is expected for the frozen population.

If an implementation encounters a value that cannot be represented under the frozen schema, it MUST fail closed and report the observation rather than silently repairing it.

No outcome-dependent exclusion is permitted.

## 9. Partitioning proposal

**Primary evaluation: chronological hold-out.**

Origins are ordered by `created_at` and divided using an ex-ante fixed temporal boundary. Training contains earlier eligible origins; test contains later eligible origins. No random row-level split is used.

The exact boundary must be frozen before confirmatory outcome computation. The boundary should be selected from the observation timeline on methodological grounds only and must leave complete 180-day follow-up for all test origins.

No package-specific future information is used to construct test representations.

A later release of the same package may therefore occur in both training and test only when the test representation uses information permitted at its own origin boundary. This is not treated as leakage because package identity is not a baseline predictor and all historical features are reconstructed strictly pre-origin.

## 10. Hyperparameter policy

The primary logistic-regression regularization strength `C` must be frozen ex ante.

Proposed primary value:

`C = 1.0`

No outcome-driven hyperparameter search is permitted for the primary analysis.

Solver, tolerance, maximum iterations and convergence policy must be fixed in the implementation audit.

## 11. Determinism

The primary pipeline must be deterministic:

- fixed Python/library implementation versions recorded;
- fixed hash algorithm and namespace encoding;
- fixed temporal split;
- fixed `C`;
- deterministic solver configuration;
- fixed random seed where the implementation exposes one;
- stable row ordering before fitting;
- identical eligible origins for B and A;
- reproducible replay producing identical predictions and metrics.

If the selected solver is deterministic without a random state, this fact is recorded rather than introducing an unnecessary random seed.

## 12. Primary and secondary metrics

**Primary metric:** mean test-set log loss.

Secondary descriptive metrics may include:

- Brier score;
- ROC AUC, provided both classes are present in the test set;
- positive-event prevalence in the test set, reported descriptively after the confirmatory outcome is frozen.

Secondary metrics cannot replace or redefine the primary metric after execution begins.

## 13. Comparison rule

Primary quantity:

`ΔLogLoss = LogLoss(B) - LogLoss(A)`.

Interpretation:

- `ΔLogLoss > 0`: A has lower log loss and therefore better predictive performance;
- `ΔLogLoss = 0`: equal mean log loss;
- `ΔLogLoss < 0`: B has lower log loss.

A positive result is not required for acceptance of the design.

A separate inferential/significance procedure is intentionally not specified by this proposal yet; if inferential testing is required, it must be frozen in a subsequent ex-ante gate before execution.

## 14. Class imbalance

No outcome-driven reweighting, oversampling, undersampling or threshold optimization is proposed for the primary analysis.

Log loss remains the primary metric because it evaluates probabilistic predictions without requiring a classification threshold.

Any class weighting would change the target probability model and therefore requires an explicit methodological decision before acceptance.

## 15. Symmetry and leakage controls

B and A MUST:

- use the same eligible origins;
- use the same `Y_180` definition;
- use the same 180-day completeness rule;
- use the same temporal partition;
- use the same primary learner;
- use the same regularization policy;
- use the same primary metric;
- be fitted without post-origin information;
- be evaluated on exactly the same test origins.

B MUST NOT receive T_acc, R*, outcome-derived features, package identity encoding, downloads/adoption, downstream activity or future information.

A MUST NOT receive B-selected features, outcomes, post-origin information or an alternate resolver.

## 16. Remaining acceptance questions

Before DR-026 acceptance, the following must be independently reviewed and frozen:

1. exact temporal split boundary;
2. exact hashing algorithm and byte encoding;
3. whether B and A use separate hash namespaces/dimensions or a formally common namespace;
4. exact logistic solver/configuration and implementation version policy;
5. whether a single fixed `C=1.0` is methodologically accepted;
6. exact handling of zero-variance numeric features;
7. whether secondary metrics are retained;
8. whether an inferential comparison is required and, if so, its exact ex-ante procedure;
9. exact unrepresentable-observation failure rule;
10. deterministic end-to-end replay audit.

## 17. Prohibited actions before acceptance

No confirmatory execution may:

- compute `Y_180` for the purpose of model selection;
- inspect outcome prevalence to choose the split, learner, C, encoding or metric;
- fit B or A models;
- compare predictions;
- tune hash dimensions;
- tune C;
- search temporal boundaries;
- perform significance testing;
- select secondary metrics based on results.

## 18. Decision boundary

This document is an ex-ante candidate protocol only. It does not constitute acceptance of DR-026 and does not authorize confirmatory execution.

The next step is a methodological review of the concrete choices above, followed by a structural implementation audit if the proposal is retained.
