# DR-023 — EXT-1.1 Rust Outcome Definition and Horizon v0.1

**Status:** PROPOSED NEW EXPERIMENTAL DECISION  
**Scope:** Outcome definition and observation horizon for the Rust dependency-target transformation family defined by DR-020/DR-021/DR-022

## 1. Decision status

This record is a **proposal only**. It does not accept or freeze an outcome variable, outcome horizon, threshold, sampling rule, or confirmatory execution parameter.

## 2. Governing question

The question is:

> What observable post-transformation outcome can be measured at a pre-specified horizon to test whether the accessibility structure `T_acc^(R*)` contains information relevant to subsequent system trajectories, without defining the outcome from the predictor itself or introducing leakage from future information into the pre-outcome state?

## 3. Scope boundary

DR-023 applies only to the current EXT-1.1 Rust dependency-target transformation family. It does not redefine `T`, `R*`, `T_acc`, Resource, baseline `B`, representation `R`, sampling, or pilot N.

## 4. Outcome requirements

A candidate outcome must satisfy all of the following:

1. **Post-outcome status:** it occurs strictly after the origin release observation boundary.
2. **Observable reconstruction:** it can be reconstructed reproducibly from the frozen Rust dataset or an explicitly frozen outcome source.
3. **Temporal ordering:** the outcome horizon is specified before confirmatory execution.
4. **Non-circularity:** the outcome is not a restatement of `T_acc`, R*, dependency constraints, or any predictor representation.
5. **Incremental relevance:** the outcome must be capable of distinguishing subsequent trajectories associated with different pre-outcome accessibility states.
6. **Ex-ante definition:** its event rule, measurement window, censoring/exclusion treatment, and horizon are frozen before confirmatory execution.
7. **Reproducibility:** identical frozen inputs produce identical outcome labels.
8. **No future leakage:** information occurring after the specified outcome horizon cannot affect the outcome label.

## 5. Candidate outcome families

Candidate families may include subsequent package-level ecosystem events such as:

- release activity after the origin release;
- subsequent dependency-network trajectory;
- later package state transitions observable in the dataset.

These are candidate classes only. No candidate is accepted by this proposal merely because it is available.

## 6. Critical methodological constraint

The outcome must not be selected because it produces a desired association with `T_acc`, `B`, or `R`. The choice must be justified independently from the confirmatory result and frozen before analysis of the outcome relationship.

Likewise, the horizon must not be chosen by searching across multiple post-outcome windows for the strongest result. If more than one horizon is scientifically defensible, the primary horizon must be specified ex ante and alternatives, if retained, must be explicitly labelled secondary/exploratory.

## 7. Dataset-boundary constraint

Before accepting an outcome, the audit must establish exactly which post-release observations are available in the frozen Rust dataset and whether their timestamps support an unambiguous horizon. If the dataset does not contain a suitable post-outcome signal, no outcome should be manufactured from pre-outcome fields merely to complete the experimental architecture.

## 8. Audit gate

The DR-023 audit must test:

- O1 — post-outcome observability;
- O2 — temporal ordering;
- O3 — non-circularity with `T_acc`;
- O4 — no predictor-derived outcome definition;
- O5 — deterministic reconstruction;
- O6 — explicit horizon feasibility;
- O7 — no future leakage;
- O8 — incremental trajectory relevance;
- O9 — minimality of the selected outcome representation.

## 9. Acceptance rule

DR-023 may be accepted only when one outcome and one primary horizon have been independently justified, deterministically reconstructable, non-circular, and frozen ex ante.

If the current frozen dataset cannot support a suitable outcome/horizon, the decision remains OPEN; no proxy outcome may be introduced merely because it is convenient or statistically available.

## 10. Explicit non-claims

This proposal does not claim that any candidate outcome is predictive, that `T_acc` has empirical explanatory power, or that a particular horizon will produce a significant result. Those are empirical questions reserved for the experiment.

## 11. Next action

Perform a **DR-023 outcome/horizon audit** against the actual frozen Rust dataset schema and the accepted pre-outcome definitions. The audit must remain pre-confirmatory and must not inspect or optimize against any experimental result.
