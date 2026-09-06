# DR-026 — EXT-1.1 Rust Model and Evaluation Ex-Ante Design v0.1

**Status:** PROPOSED — EX-ANTE DESIGN, NO ACCEPTANCE  
**Scope:** Statistical comparison of conventional baseline `B` against `T_acc^(R*)` for the frozen EXT-1.1 Rust outcome `Y_180`  
**Depends on:** DR-019, DR-020, DR-021, DR-022, DR-023, DR-024, DR-025, DR-025A

## 1. Governing question

Can the comparison between `B` and `T_acc^(R*)` be specified before confirmatory outcome computation and model fitting so that any observed difference in predictive information is attributable to the representations rather than outcome-driven model selection?

## 2. Confirmatory objects

For each eligible origin release `v_o` with complete 180-day follow-up:

- outcome: `Y_180(v_o)` as frozen by DR-023;
- baseline representation: `B(v_o)` as frozen by accepted DR-025A;
- accessibility representation: `T_acc^(R*)(v_o)` as defined by DR-020/DR-021/DR-022.

The primary scientific comparison is between a model using `B` and a model using the accessibility representation. The comparison must not redefine either representation after observing outcomes.

## 3. Design principle

The model family and evaluation protocol must be chosen for methodological suitability, interpretability and deterministic reproducibility, not by inspecting outcome prevalence, associations, effect sizes, significance, or comparative predictive performance.

No pilot fitting is permitted for the purpose of choosing among candidate model families, hyperparameters, metrics, encodings, horizons, samples, or representations.

## 4. Required model-design decisions

Before acceptance, DR-026 must freeze:

1. primary model family;
2. exact input representation for `B`;
3. exact input representation for `T_acc^(R*)`;
4. categorical encoding rules, including handling of unseen categories;
5. numeric transformations, if any;
6. treatment of missing values;
7. train/test or cross-validation protocol;
8. grouping/blocking rules needed to prevent temporal or package leakage;
9. hyperparameter policy;
10. random seed and deterministic execution requirements;
11. primary predictive metric;
12. secondary/descriptive metrics, if any;
13. comparison statistic or decision rule;
14. treatment of class imbalance, if applicable;
15. handling of observations that cannot be represented under the frozen schema.

## 5. Fairness of comparison

The B and `T_acc^(R*)` models must be evaluated on the same eligible origin population and under the same outcome definition, horizon, partitioning protocol, and primary metric.

No model may receive post-origin information.

No package identity may enter B through supervised encoding, learned package-specific embeddings, or equivalent target-derived transformations.

The accessibility representation may use only the frozen `T_acc^(R*)` construction and may not receive additional outcome-derived features.

## 6. Temporal and dependency leakage controls

The confirmatory design must preserve the origin boundary:

`B(v_o)` uses only permitted pre-origin information.

`T_acc^(R*)(v_o)` is reconstructed according to DR-020/DR-021/DR-022 and its frozen temporal cutoff.

`Y_180(v_o)` uses only the later 180-day observation window specified by DR-023.

Train/test or validation splitting must be defined so that information from later releases cannot leak into training representations for earlier test origins. The exact strategy remains an open design point until methodological review.

## 7. Primary comparison target

The primary estimand is not yet fixed by this proposal. Candidate forms include:

- difference in out-of-sample log loss;
- difference in a proper probabilistic scoring rule;
- another pre-specified predictive-information comparison appropriate to the selected model family.

The final primary metric must be selected ex ante on methodological grounds and frozen before outcome-driven fitting.

## 8. Falsification requirements

The accepted design must remain capable of producing any of the following outcomes:

- `T_acc^(R*)` improves predictive performance relative to `B`;
- no material predictive difference is observed;
- `B` performs better;
- the comparison is inconclusive because the representation or evaluation is not estimable under the frozen rules.

No positive result is required for acceptance.

## 9. Prohibited adaptive decisions

After confirmatory outcome computation begins, the following may not be changed in response to observed results:

- outcome definition or horizon;
- eligible population;
- B representation;
- `T_acc^(R*)` construction;
- model family;
- categorical encoding;
- feature transformations;
- train/test/CV protocol;
- hyperparameters, except where a fully pre-specified tuning procedure exists;
- primary metric;
- decision threshold;
- exclusion rules.

## 10. Acceptance gate

DR-026 may be accepted only after an audit demonstrates that the complete model/evaluation specification is deterministic, ex ante, outcome-independent, temporally valid, and symmetric between B and `T_acc^(R*)` wherever comparison symmetry is required.

Acceptance of DR-026 will not itself authorize execution unless all preceding experimental decisions are accepted and the final execution gate is satisfied.

## 11. Current open questions

The following are deliberately unresolved in v0.1:

- model family;
- exact encoding of nominal version strings;
- representation of `T_acc^(R*)` suitable for the selected model;
- temporal split versus grouped cross-validation;
- primary proper scoring rule;
- class-imbalance treatment;
- deterministic hyperparameter policy;
- final confirmatory execution gate.

These questions must be resolved without inspecting confirmatory outcome-performance results.
