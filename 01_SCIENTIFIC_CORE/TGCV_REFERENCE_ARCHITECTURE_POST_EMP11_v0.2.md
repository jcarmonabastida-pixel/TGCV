# TGCV — Reference Architecture Post-EMP-1.1 v0.2

**Status:** Scientific architecture draft — NOT FROZEN

## 1. Purpose

Define the reusable scientific architecture implied by the current TGCV programme while separating validated evidence from assumptions that remain subject to replication.

## 2. Architecture

```text
System / Environment
        │
        ▼
 State S + Context C + Constraints/Resources L
        │
        ▼
 Accessibility function F(S,C,L)
        │
        ▼
 Accessible transformations T_acc
        │
        ▼
 Change in accessibility ΔT_acc
        │
        ▼
 Subsequent trajectory ΔTrajectory
        │
        ▼
 Value / practical consequence
```

The architecture is a research architecture, not a claim that every arrow has already been empirically established.

## 3. Evidence boundary

EMP-1.1 provides positive evidence for the predictive usefulness of the tested accessibility representation. The architecture therefore treats `T_acc` as the currently strongest empirically supported layer.

The links from `ΔT_acc` to trajectory and from trajectory to value remain research hypotheses.

## 4. Independence from EMP-1.1 implementation

The reference architecture is intentionally implementation-neutral. It must not encode the particular classifier, dataset, candidate construction, feature encoding or intervention procedure used in EMP-1.1 as if those were constitutive elements of TGCV.

Those details belong to the experimental record, not to the theory's reference architecture.

## 5. Replication interface

A future replication must instantiate at least:

- a system/state representation;
- contextual conditions;
- constraints/resources;
- a declared transformation universe;
- an independently specified accessibility function;
- an outcome or trajectory measure appropriate to the research question.

The replication may use different algorithms, domains and candidate representations provided that the tested hypothesis remains semantically identifiable.

## 6. Architectural invariants

The following are retained as current design invariants:

1. Accessibility is distinct from current state.
2. Accessibility is a set/structure of possible transformations, not an outcome.
3. Accessibility must be evaluable from information available before the tested outcome.
4. Changes in accessibility and changes in outcome must remain analytically distinguishable.
5. Value is downstream and must not be assumed from accessibility alone.
6. Empirical operationalisations are instances of the architecture, not definitions of the architecture itself.

## 7. What is not frozen

The following remain open to empirical and theoretical revision:

- universal decomposition of `S`, `C`, and `L`;
- universal transformation taxonomy;
- necessary and sufficient accessibility predicates;
- causal interpretation of accessibility changes;
- trajectory linkage;
- value linkage;
- domain-independent implementation details.

## 8. Role in the Programme

The Reference Architecture sits in the TGCV scientific core. It is not a transfer deliverable. Transfer mechanisms and industrial applications consume validated architectural principles; they do not redefine them.

## 9. Next maturation step

The architecture should be frozen only after the independent replication design has demonstrated that its key semantics can be instantiated without relying on the original EMP-1.1 implementation.
