# N-R8.2.4 — C Residual-Structure Interpretability Qualification v0.1

**Status:** PROPOSED — NOT FROZEN  
**Date:** 2026-09-05  
**Parent:** N-R8.2 Operationalisation Specification v0.1  
**Predecessor:** N-R8.2.3 C Amended Operationalisation v0.1

## 1. Purpose

This qualification records the interpretive consequence of the N-R8-C matching-key amendment in N-R8.2.3.

The amendment removes equality of graph edge count from the matching key because the original key fixed the quantities determining the R4 successor-structure coordinates and therefore prevented the required full-R inequality.

The present document does not alter the N-R8-C construction rule. It establishes the exact claim boundary that may be assigned to a successful C experiment.

## 2. Normative amended key

N-R8-C uses:

`K_C*(S) = (B(S), R_family_availability(S), R_family_cardinality(S), R_component_incidence(S), |T_acc(S)|, family_count(S), n_components(S), resources(S), objective(S))`

A pair A,B is valid only if:

`K_C*(A) = K_C*(B)`

and:

`R(A) != R(B)`

where R is the complete authoritative 58-dimensional N-R1.3 v0.2 representation.

No outcome, trajectory, learner result, N-R7 result, p-value, or post-state information may enter pair construction.

## 3. What is controlled

The matching design controls exactly the following classes of information:

1. baseline state information B;
2. R family availability;
3. R family cardinality;
4. R3 component-incidence structure;
5. total accessible-transformation cardinality;
6. number of non-empty transformation families;
7. component count;
8. resources;
9. objective.

These controls prevent a successful C contrast from being explained solely by differences in those matched quantities.

## 4. What remains free

The amended key deliberately leaves graph-level edge organisation and edge count unconstrained, subject only to the requirement that the complete R vectors differ.

Consequently, a successful C pair may differ in R4 coordinates that are functions of edge structure, including successor-structure statistics derived from edge transformations.

This is not an implementation defect. It is the direct consequence of making full-R inequality identifiable after the original key was shown to overconstrain the representation.

## 5. Interpretive qualification

A successful N-R8-C result MUST NOT be described as proof that an abstract, representation-independent "higher-order structure" exists beyond every lower-order structural explanation.

The admissible interpretation is narrower:

> N-R8-C tests whether predictive/outcome-relevant information remains in the accessible-transformation structure after the specified low-order summaries are held exactly fixed.

Accordingly, if a systematic C difference is observed, the result supports the existence of **residual structural information beyond the matched summaries**, not isolation of a unique causal mechanism and not universal higher-order structure independent of representation.

If the C difference disappears, the evidence supports narrowing the N-R8 claim boundary: the information tested by C is adequately explained, for this design, by the matched summaries and/or by the structure represented by the remaining contrast.

## 6. Confounding boundary

The free edge-level structure is a designed contrast rather than an uncontrolled nuisance variable. Nevertheless, because edge organisation contributes to R4, C cannot by itself distinguish among all possible decompositions of the residual R difference.

Therefore:

- C establishes a residual-structure contrast under `K_C*`;
- C does not establish that any particular R4 coordinate is the causal or uniquely explanatory carrier of the effect;
- feature-level attribution remains exploratory;
- R2 in N-R8-D provides an independent representation check and must not be collapsed conceptually into C.

## 7. Relationship to N-R8-D

N-R8-D has a distinct methodological role: it evaluates an independently specified representation R2 of `T_acc`.

A consistent result across C and D would strengthen the interpretation that the observed information is not merely an artifact of the specific R representation. A discrepancy would require the claim to remain representation-qualified.

No C result may be used retrospectively to modify R2.

## 8. Decision rule for N-R8-C design

The N-R8-C amended operationalisation is classified:

**CONDITIONAL PASS — IDENTIFIABILITY ACCEPTED WITH INTERPRETIVE QUALIFICATION.**

The condition is that all reporting of C remains within the claim boundary defined in Sections 5–7.

This qualification does not constitute an experimental result and does not authorize corpus generation by itself.

## 9. Execution gate

Before N-R8.4 construction, implementation/conformance must demonstrate:

1. exact equality of `K_C*` for accepted pairs;
2. exact inequality of full 58-dimensional R;
3. deterministic candidate generation and pair ordering;
4. no outcome/trajectory/learner/N-R7 dependency;
5. fail-closed target and budget behaviour;
6. correct R2 empty-T_acc conformance test;
7. all inherited N-R8.2 controls remain unchanged.

Only after conformance PASS may N-R8.4 corpus construction proceed to integrity-freeze review.

## 10. Governance

This document is an interpretive qualification, not a result document.

It changes neither N-R7 nor any historical result. It does not authorize execution and does not freeze N-R8.2.3.

**Current gate state:**

- N-R8.2.3: PROPOSED
- N-R8.2.4: PROPOSED
- N-R8-C: CONDITIONAL PASS on design/identifiability, pending implementation conformance
- N-R8.3: implementation/conformance pending
- N-R8.4: BLOCKED
- Corpus: NOT GENERATED
- N-R7: INTACT
