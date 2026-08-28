# TGCV — G1 Independent Replication Protocol v0.1

**Status:** Pre-registration-ready protocol draft
**Purpose:** Test whether the empirical signal observed in EMP-1.1 survives an independently specified operationalisation, without modifying or re-running the historical experiment.

## 1. Governance status

EMP-1.1 remains sealed historical evidence. This protocol is a new empirical study and must not alter, reinterpret, or retroactively optimise EMP-1.1.

The replication is governed by the Evidence-to-Claim Matrix and by the Programme Contract.

## 2. Replication question

Does a relational representation of a system's accessible transformations provide reproducible predictive information beyond a conventional baseline and beyond accessibility cardinality alone?

## 3. Primary hypothesis

**H1:** Under an independently specified operationalisation, a relational accessibility representation yields lower out-of-sample predictive loss than the pre-specified baseline.

**H0:** The relational accessibility representation does not yield a reproducible improvement over the baseline under the pre-specified evaluation protocol.

## 4. Secondary hypotheses

**H2:** Any improvement is not explained solely by the number of accessible transformations.

**H3:** Destroying relational structure while preserving appropriate lower-order summaries removes or substantially reduces the observed advantage.

Trajectory and value hypotheses are explicitly outside G1 unless separately registered. G1 is a replication of the accessibility signal, not a test of the entire TGCV chain.

## 5. Independence requirements

The replication must independently specify, before outcome inspection:

- dataset/domain;
- transformation universe;
- accessibility predicate;
- relational representation;
- baseline representation;
- control representations;
- train/validation/test partitioning;
- primary metric;
- statistical test;
- decision threshold;
- exclusion rules;
- random seeds or reproducibility procedure;
- computational environment.

Reusing conceptual semantics is permitted and necessary. Reusing the exact empirical implementation is not the objective.

## 6. Design principles

### 6.1 No outcome leakage
Accessibility features must be computable without information from the future outcome being predicted.

### 6.2 Pre-specification
Primary hypotheses and analysis decisions must be fixed before the test set is used for confirmatory inference.

### 6.3 Matched comparison
The baseline and TGCV representations must be evaluated on the same prediction tasks, splits and outcome observations.

### 6.4 Cardinality control
A count-only control must preserve the relevant accessibility cardinality information without preserving the relational structure being tested.

### 6.5 Structure-destruction control
A valid null transformation must disrupt the relational accessibility structure while preserving the declared lower-order properties required by the design.

## 7. Primary outcome

Primary metric: **out-of-sample LogLoss**, unless a domain-independent justification for another proper scoring rule is registered before execution.

Primary effect:

`ΔLL = LL_baseline − LL_TGCV`

Positive values favour the TGCV representation.

The numerical threshold used in EMP-1.1 must not automatically be imported as a universal replication threshold. G1 must justify its own minimum practically/scientifically meaningful effect before outcome inspection.

## 8. Statistical inference

The primary comparison should use paired evaluation across matched test observations. The inferential procedure, number of resamples/permutations, and multiplicity treatment must be frozen before test-set inspection.

The analysis must report effect size, uncertainty, exact sample counts and the full distribution relevant to the paired comparison, not only a p-value.

## 9. Negative-result policy

A failure to reproduce the effect is a legitimate scientific result. It must not trigger post-hoc changes to the operationalisation in the same confirmatory run.

If an implementation defect is independently demonstrated, the correction must be documented as a new protocol/version rather than silently applied to G1.

## 10. Success and failure gates

### G1-PASS
The independently specified representation reproduces a statistically and substantively meaningful advantage over baseline, while controls support the interpretation that the advantage is relational rather than cardinality-only.

### G1-PARTIAL
The primary effect is reproduced but one or more control conditions are inconclusive.

### G1-FAIL
The primary effect is absent or the evidence is incompatible with the pre-specified hypothesis.

### G1-INDETERMINATE
The protocol cannot support a valid inference because of a documented methodological failure.

## 11. What G1 would justify

A PASS would strengthen C03 in the Evidence-to-Claim Matrix and permit progression toward G2 (generalisation), while still not establishing trajectory or value effects.

A FAIL would require revising the evidential status of C03 and examining boundary conditions.

## 12. What G1 would not justify

Regardless of outcome, G1 alone cannot establish:

- universal domain independence;
- causality of accessibility changes;
- effects on future trajectories;
- practical value creation;
- a final TGCV ontology;
- a universally valid methodology.

## 13. Reproducibility package

Before execution, the replication should produce a versioned package containing:

- protocol;
- dataset provenance;
- transformation specification;
- accessibility specification;
- analysis code;
- environment/dependency lock;
- configuration and seeds;
- pre-test checks;
- machine-readable results;
- final report.

## 14. Freeze gate before execution

G1 may enter confirmatory execution only when the following are frozen:

`Protocol → Data → Transformations → Accessibility → Controls → Splits → Metric → Analysis → Decision Rule`.

After that point, changes require a new version and cannot be presented as part of the original confirmatory G1.

## 15. Current status

**Protocol:** drafted.

**Scientific objective:** defined.

**Historical EMP-1.1:** preserved and untouched.

**Execution:** not yet authorised by this document alone; the remaining pre-registration/freeze fields must be completed before confirmatory execution.
