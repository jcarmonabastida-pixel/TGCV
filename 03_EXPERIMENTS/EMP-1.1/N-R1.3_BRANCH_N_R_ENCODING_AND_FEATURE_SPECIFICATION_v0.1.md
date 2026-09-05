# N-R1.3 — Branch N R Encoding and Feature Specification v0.1

**Program:** TGCV  
**Experiment:** EMP-1.1  
**Branch:** N — Controlled New Reconstruction  
**Status:** PROSPECTIVE SPECIFICATION — CORRECTED  
**Gate:** N-R1.3  
**Date:** 2026-09-05

## 1. Purpose

This document freezes the prospective representation `R = Phi(T_acc)` for the controlled Branch N reconstruction of EMP-1.1.

It does not recover the historical `R` implementation. No historical result is used to select feature definitions, dimensionality, ordering, scaling, or encoding.

The representation must be deterministic, snapshot-local, structurally informative, finite-dimensional, and independently reproducible.

## 2. Source object

Input:

`T_acc(S) = {tau : P_tau(S)=1}`

as specified in N-R1.2.

The representation is a deterministic function:

`R(S) = Phi(T_acc(S), S)`.

The state `S` is supplied only for structural incidence summaries explicitly defined below. No future trajectory or outcome information is permitted.

## 3. Design principles

The representation must satisfy:

1. **Snapshot locality:** every feature is computable from the current snapshot and `T_acc`.
2. **Structurality:** representation must distinguish transformation types and their incidence where defined.
3. **No cardinality-only representation:** total `|T_acc|` is retained only as a diagnostic, not as the sole R representation.
4. **Fixed dimensionality:** every valid snapshot produces the same-length vector.
5. **Determinism:** identical snapshots produce byte-identical feature vectors after canonical serialization.
6. **Permutation invariance:** input row ordering cannot affect R.
7. **No target leakage:** objective outcome, future state, realized transformation, trajectory, success, or value cannot enter R.
8. **No result-driven tuning:** dimensions and definitions are fixed before confirmatory execution.

## 4. Canonical feature vector

The Branch N representation contains four blocks with a total of **58 numerical features**.

`R = [R1 || R2 || R3 || R4]`

### R1 — Family availability: 6 features

One binary feature per transformation family, in this exact order:

1. `ADD_COMPONENT_available`
2. `REMOVE_COMPONENT_available`
3. `ADD_EDGE_available`
4. `REMOVE_EDGE_available`
5. `REWIRE_EDGE_available`
6. `MODIFY_RESOURCE_available`

For family `f`,

`R1_f = 1` iff at least one accessible transformation instance of family `f` exists; otherwise `0`.

### R2 — Family cardinality: 6 features

One integer feature per family in the same fixed order:

`R2_f = |T_acc,f|`.

These counts are included as structural descriptors but are not the representation's only information.

No logarithmic transformation or post-hoc normalization is applied to these counts.

### R3 — Component-incidence structural summaries: 30 features

For each of the six components, in canonical order

`A1, A2, B1, B2, C1, C2`,

five features are recorded:

1. `add_component_incident(v)` — number of accessible `ADD_COMPONENT(v)` instances. Since the operation applies only to absent components, this is `0` when `v in V` and otherwise `0/1` under the current universe.
2. `remove_component_incident(v)` — number of accessible `REMOVE_COMPONENT(v)` instances.
3. `add_edge_incident(v)` — number of accessible `ADD_EDGE` instances having `v` as source or target.
4. `remove_edge_incident(v)` — number of accessible `REMOVE_EDGE` instances having `v` as source or target.
5. `rewire_incident(v)` — number of accessible `REWIRE_EDGE` instances in which `v` occurs in any of the three transformation endpoints.

For each component `v`, the five values are concatenated before moving to the next component.

The features are defined against the full six-component universe, including currently absent components, so dimensionality does not depend on `|V|`.

### R4 — Transition-result structural signature: 16 features

R4 summarizes the distinct structural changes induced by accessible transformations without using future realization.

The 16 features are:

1. `n_delta_components_add`
2. `n_delta_components_remove`
3. `n_delta_edges_add`
4. `n_delta_edges_remove`
5. `n_delta_edges_rewire`
6. `n_delta_resources_up`
7. `n_delta_resources_down`
8. `n_noop`
9. `n_distinct_next_component_counts`
10. `n_distinct_next_edge_counts`
11. `n_distinct_next_resource_vectors`
12. `n_distinct_next_states`
13. `max_next_component_count`
14. `min_next_component_count`
15. `max_next_edge_count`
16. `min_next_edge_count`

For each accessible transformation instance `tau`, apply the deterministic transition `S' = tau(S)` from N-R1.2 and compute the resulting structural quantities.

`n_distinct_next_states` counts distinct canonical successor states, not transformation instances. Multiple transformation instances that yield the same successor therefore remain distinct in R2 but are collapsed only in this R4 feature.

`n_noop` is expected to be zero under N-R1.2. It is retained as an integrity diagnostic so an implementation cannot silently introduce no-op transformations.

## 5. Empty and degenerate cases

The fixed-dimensional vector is always emitted.

If `T_acc = emptyset`, **all 58 scientific R features are exactly `0`**. This includes the four R4 min/max successor-state features. No current-state value is copied into R when there is no accessible transformation.

An explicit accessibility-status/validity diagnostic may be emitted outside R for execution auditing; it is not part of the scientific 58-feature vector.

If a valid state produces only one transformation family, all other family blocks remain zero. No imputation is performed.

## 6. Numeric representation

All 58 R features are numeric.

- binary availability features: integer `0/1`;
- cardinality/incidence/count features: non-negative integers;
- min/max structural features: integers.

No categorical one-hot encoding is needed inside R because transformation families are represented by fixed-position blocks.

## 7. Normalization

**No normalization is applied to R before serialization.**

The raw integer/binary representation is the canonical scientific representation.

Any learner-specific scaling or preprocessing must be applied downstream by a separately frozen learner pipeline and identically to all experimental arms. Such preprocessing is not part of the definition of R.

This avoids making R depend on training-sample statistics.

## 8. Canonical ordering and serialization

Feature order is fixed as follows:

1. all six R1 features in family order;
2. all six R2 features in family order;
3. R3 component blocks in component order `A1,A2,B1,B2,C1,C2`, each with its five features in the order defined in Section 4;
4. all sixteen R4 features in the order defined in Section 4.

Canonical component order:

`A1 < A2 < B1 < B2 < C1 < C2`.

Canonical family order:

`ADD_COMPONENT < REMOVE_COMPONENT < ADD_EDGE < REMOVE_EDGE < REWIRE_EDGE < MODIFY_RESOURCE`.

The serialized representation must preserve this exact order. Dictionary/hash-map iteration order is prohibited as a source of feature ordering.

## 9. Feature traceability

Every R feature must be traceable to one of:

- family membership of an element of `T_acc`;
- cardinality of a family subset of `T_acc`;
- incidence of a transformation instance on a named component;
- deterministic structural property of the successor state generated by an element of `T_acc`.

No R feature may be computed from the observed future trajectory or outcome.

## 10. Bounds and overflow

Because the transformation universe is finite, all R features have finite deterministic bounds for a valid state.

The implementation must use integer arithmetic sufficient for the maximum possible counts. Silent integer overflow is a failure condition.

For diagnostic purposes, the implementation should calculate and record the maximum observed feature value during validation, but this diagnostic is not part of R.

## 11. Required invariance properties

The following tests are mandatory before any scientific execution:

1. **Same-state determinism:** same S twice -> identical R.
2. **Input-order invariance:** permuting component/edge input rows -> identical R.
3. **Family completeness:** every accessible transformation contributes to exactly one family count.
4. **Traceability:** every non-zero R2/R3/R4 count can be traced to one or more concrete T_acc instances.
5. **Transition consistency:** every R4 successor signature agrees with the N-R1.2 transition equations.
6. **No leakage:** changing future/outcome data while holding S fixed cannot change R.
7. **Empty-set handling:** `T_acc=emptyset` yields the specified fixed vector of 58 zeros.
8. **Serialization determinism:** repeated canonical serialization yields identical bytes.
9. **Dimensionality:** every valid state produces exactly 58 features.
10. **Family-order invariance:** internal iteration order cannot change the vector.

## 12. Provenance classification

### RECOVERED

- baseline B fields remain those frozen in EMP-1.1 protocol;
- the historical domain contains six components and three resources;
- R is intended to encode accessible-transformation information rather than replace the baseline.

### DERIVED

- the requirement that R be a deterministic function of snapshot-local `T_acc`;
- structural feature traceability to accessible transformations and their immediate deterministic successors;
- fixed-dimensional encoding as necessary for reproducible learner input.

### RECONSTRUCTED

- 58-feature dimensionality;
- four-block architecture R1–R4;
- exact family availability and cardinality features;
- exact component-incidence summaries;
- exact successor-state structural signature;
- empty-set encoding as the all-zero 58-feature vector;
- raw integer representation and no pre-R normalization;
- canonical serialization order.

### OPEN / NOT CLAIMED

- historical EMP-1.1 R dimensionality;
- historical R feature ordering;
- historical R aggregation;
- historical learner preprocessing;
- historical implementation identity.

## 13. Anti-retrofitting rule

The historical result `Delta LogLoss = 0.07942359585000518` and any other archived outcome are **not** inputs to this specification and must not be used to modify:

- the 58-feature dimensionality;
- feature definitions;
- family selection;
- ordering;
- normalization;
- empty-case handling;
- implementation details.

Any change after this document is frozen requires a new version and a new prospective gate.

## 14. Gate decision — N-R1.3

**N-R1.3 STATUS: PASS / CLOSED — CORRECTED**

The Branch N R representation is now sufficiently explicit to permit implementation-level construction and deterministic unit testing.

**N-R1 GLOBAL STATUS: BLOCKED pending implementation conformance and validation.**

### Next gates

1. **N-R2 — Transformation/R implementation conformance** against N-R1.2 and this corrected N-R1.3 specification.
2. **N-R3 — Deterministic unit and invariance tests.**
3. **N-R4 — Controlled smoke execution and artifact integrity.**
4. Only after those gates pass may the reconstruction proceed toward the controlled full EMP-1.1 execution boundary.

No confirmatory result is authorized by N-R1.3 alone.
