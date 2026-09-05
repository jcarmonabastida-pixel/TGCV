# N-R8.2.6 — N-R8-C Minimal-Relaxation Analysis v0.1

**Status:** PROPOSED — DESIGN DECISION NOTE
**Date:** 2026-09-05
**Parent:** N-R8.2 Operationalisation Specification v0.1
**Trigger:** N-R8.4 conformance failure recorded in N-R8.2.5

## 1. Decision question

Can N-R8-C be repaired by a minimal relaxation of the matching key while retaining the current authoritative 58-dimensional R representation and the intended interpretation of C as a structural-confounding attack?

## 2. Result

**No, not without weakening the scientific meaning of the control.**

The current R definition is constructed as R1 + R2 + R3 + R4. Under the frozen Branch N transformation universe, the R4 coordinates are deterministic functions of quantities already represented in R1/R2/R3 together with state-level quantities fixed by B and the existing C key.

Therefore, any C key that continues to fix all R1, all R2, and all R3 coordinates cannot simultaneously require `R(A) != R(B)`.

The failure is structural, not a shortage of candidate states.

## 3. Why removing explicit edge count is insufficient

N-R8.2.3 removed `n_edges` as an explicit key component. This did not create an independent degree of freedom because R2 contains the cardinality of `REMOVE_EDGE`, which equals the current number of directed edges under N-R1.2.

Thus:

`R2_REMOVE_EDGE(A) = R2_REMOVE_EDGE(B)` implies `|E_A| = |E_B|`.

Similarly, for a fixed component set, the accessible `ADD_EDGE` and `REWIRE_EDGE` cardinalities are determined by component and edge counts under the frozen transformation semantics.

The attempted relaxation therefore removed only a duplicated representation of an already-controlled quantity.

## 4. Screening of Option A: relax the matching key

### A1 — Remove explicit edge count only

Rejected. This is already the N-R8.2.3 amendment and remains non-identifiable because edge count is encoded in R2.

### A2 — Relax one or more edge-family R2 cardinalities

Technically capable of producing `R(A) != R(B)`, but the resulting contrast changes low-order transformation-family cardinality. The pair would no longer test residual structure conditional on the specified family cardinalities. Any observed difference could be explained by the deliberately unmatched family cardinality itself.

This would be a different scientific test, not a minimal implementation repair of C.

### A3 — Relax component-incidence R3 coordinates

Same problem. R3 is explicitly intended as a low-order structural control. Allowing R3 differences would make the contrast attributable to an unmatched component-level incidence feature and would change the claim boundary.

### A4 — Remove `|T_acc|` matching

Rejected for the intended C claim. This permits a direct accessibility-cardinality difference and therefore abandons one of the principal low-order controls.

### A5 — Relax resources or objective

Rejected. These are part of B / state context and would introduce ordinary baseline confounding rather than a residual structural contrast.

### A6 — Retain all R1/R2/R3 equality but seek a larger or different graph fixture

Rejected. No search expansion can create a pair if the full R vector is functionally determined by the matched quantities. The observed 64-subset failure is therefore not evidence that a larger fixture would solve the problem.

## 5. Scientific implication

Option A does not provide a clean repair of the intended C test. A relaxation can create pairs only by releasing information that C currently claims to control. Such a change is permissible only as a new scientific design, with a new hypothesis/claim boundary and new pre-execution power/identifiability analysis.

The current design should therefore **not** be patched by selectively dropping R2/R3 features merely to make the fixture pass.

## 6. Preferred next design direction

The next design should separate two questions that the current C construction conflates:

1. whether low-order summaries are matched;
2. whether the chosen representation of structural organisation contains information not determined by those summaries.

The cleanest candidate is a redesign around an **independent representation of T_acc** (the methodological role already assigned to N-R8-D), rather than requiring inequality in the current R vector as the definition of the residual contrast.

Such a redesign must be specified independently before any results are observed. It must define:

- the independent representation;
- its exact dimensionality and semantics;
- the matching controls;
- the contrast criterion;
- deterministic pair generation;
- leakage exclusions;
- conformance fixtures;
- interpretation limits;
- and its relationship to N-R8-D.

No existing N-R8 result or N-R7 result may be used to choose the representation or threshold.

## 7. Governance decision

**N-R8-C remains BLOCKED.**

Option A is rejected as a repair strategy because every technically effective relaxation changes a substantive control and therefore creates a different experiment.

The next authorized step is to formulate and audit a new C representation-level design, preferably using the independent-representation logic already specified for N-R8-D, before implementation or corpus construction.

No 5,000-pair corpus generation is authorized.

N-R7 remains untouched.
