# TGCV — Ω_T Representation Boundary Candidate Specification v0.1

**Status:** GOVERNANCE SPECIFICATION — CANDIDATE, NOT FROZEN, NOT EXECUTED
**Date:** 2026-10-01
**Scope:** formal-to-empirical bridge for TSDI hypothesis B

## 1. Purpose

Define the minimum representation boundary that a candidate empirical instantiation of Ω_T must satisfy before any source can be admitted to a discrimination-design gate.

This document does not select a dataset, experiment, model, result, or Core revision.

## 2. Candidate object

The candidate B object is:

`Ω_T,t = (U_t, ≡_t, R_t)`

where:
- `U_t` is the universe of transformation instances observable at time `t`;
- `≡_t` is an identity/equivalence relation over transformation instances;
- `R_t` is a typed structural relation over the resulting transformation identities.

The object is intended to describe organisation and temporal change of transformation possibilities, not outcomes or value.

## 3. Primitive-observation boundary

A valid empirical instantiation must start from primitive observations `P_t` that are available independently of Ω_T and A/B comparison.

Candidate primitive classes include identifiable system components/entities; versioned or timestamped configurations; declared operations/actions/changes; dependency or compatibility declarations; and provenance linking an operation to its pre/post configuration.

These are admissible examples, not a commitment to a specific source.

## 4. U_t — transformation identity

A transformation instance `u` must be defined by an ex-ante function `u = φ(P_t, P_{t+1})`, or directly from an independently recorded transformation event where event-level observations exist.

The identity must specify source configuration/state, transformation operation, target configuration/state, domain/type, and provenance/time.

`U_t` must not be defined by success, value, outcome, improvement, or target trajectory.

## 5. ≡_t — transformation equivalence

A frozen equivalence predicate `u_i ≡_t u_j` must be defined from identity fields only.

The rule must be deterministic, symmetric, transitive, fixed before the discrimination outcome, and invariant to irrelevant serialization differences.

No equivalence class may use downstream outcomes, value, reward, future success or post-hoc clustering.

## 6. R_t — typed structural relation

`R_t` must be a typed relation over transformation identities, with a finite frozen vocabulary of relation types.

A relation edge must be computable from primitive observations and frozen rules, without outcomes or target predictions.

Each relation type must specify source and target identity types, semantic condition, temporal scope, directionality if applicable, evidence/provenance fields, and missing-data treatment.

A graph statistic computed after the fact from `T_acc` is not sufficient. The relation itself must have an independent observational/semantic basis.

## 7. Temporal identity

A longitudinal bridge requires a provenance mapping `π_t : U_t → I`, where `I` is a stable identity space permitting transformation identities to be followed, replaced, split or merged under a frozen rule.

Changes in `U_t`, `≡_t` or `R_t` must be distinguishable from identifier renaming or serialization changes.

## 8. Matched A representation

From the same primitive observations `P_t`, construct `A_t = (S_t, T_acc,t)` using the currently governed A semantics.

The B construction may not receive primitive observations unavailable to A.

The comparison must therefore use a common observation boundary: `P_t → A_t` and `P_t → Ω_T,t`.

## 9. A-reconstruction test

Before any discrimination claim: test direct encoding in A; test deterministic derivation from `A_Core`; test reconstruction through currently admissible auxiliary mechanisms; only if all fail may the candidate be classified as potentially A-non-equivalent.

If `Ω_T` is fully reconstructible from `T_acc` under the frozen A boundary, it is **A-EQUIVALENT** and cannot serve as the independent B object.

## 10. Minimal longitudinal condition

At least two time points are required, with common provenance, unchanged identity/equivalence semantics, unchanged relation semantics, and at least one observable change in `U_t` or `R_t`.

Cross-sectional graph structure alone does not qualify as evidence for transformational dynamics.

## 11. Independence and anti-circularity

The representation boundary must be frozen before examining the result used for architectural discrimination.

Prohibited definitions include outcome/value/reward, target or future success, post-hoc relation discovery, relabelling `T_acc` as `U_t`, and graph statistics of `T_acc` presented as an independent relation object.

## 12. Candidate admission statuses

**BOUNDARY-PASS:** specification complete enough for source-specific audit.

**BOUNDARY-BLOCKED:** at least one identity, equivalence, relation, temporal or parity rule remains unspecified.

**BOUNDARY-FAIL:** proposed object is necessarily a deterministic representation of A or uses excluded downstream information.

A BOUNDARY-PASS is not scientific evidence and does not authorize execution.

## 13. Current status

**Ω_T REPRESENTATION BOUNDARY: CANDIDATE SPECIFICATION — NOT FROZEN.**

No source is selected.
No experiment is designed.
No execution is authorized.
No Core, Matrix or RMA revision follows from this specification.


## 14. Boundary-review finding — NOT YET FROZEN

The review identified three issues requiring correction before freeze:

1. **Temporal indexing:** defining `u = φ(P_t,P_{t+1})` while calling `U_t` observable at time `t` conflates a time state with an interval transition. The canonical candidate must use an explicit transition interval index (for example `U_[t,t+1]`) or an event-time convention.
2. **Identity versus equivalence:** the specification must distinguish transformation instance identity, transformation-type equivalence, and longitudinal persistence. Otherwise `≡_t` risks becoming a second name for exact identity rather than an independently useful relation.
3. **Relation domain:** `R_t` over instances and `π_t : U_t → I` are not yet sufficient to specify how relations persist/change across time. The temporal relation semantics must be frozen explicitly.

Until these are resolved, the boundary remains **BOUNDARY-BLOCKED**. No source admission or experiment design is permitted.

These are specification defects, not empirical findings, and do not alter the current Core, Matrix or RMA.


## 15. Corrected boundary formulation — candidate v0.2

To resolve the review defects, the candidate boundary is reformulated with explicit interval and identity layers.

### 15.1 Transformation instances
`U_[t,t+1]` is the set of transformation instances evidenced over interval `[t,t+1]`. An instance `u` has a frozen event/provenance identity and records source configuration, operation/change, target configuration, type/domain and interval provenance.

`U_t` is reserved for transformations already evidenced at or attributable to an observation instant `t`; it is not used as shorthand for an interval transition.

### 15.2 Three distinct identity relations
`id(u)` is the exact provenance identity of an observed transformation instance.

`u ≡_T v` is a frozen transformation-type equivalence relation derived only from pre-specified identity/type fields; it does not assert that the two events are the same instance.

`π(u)` is the longitudinal persistence/provenance mapping used to determine whether instances at different intervals represent continuation, replacement, split or merge under a frozen rule.

These three relations must not be collapsed.

### 15.3 Structural relation
`R_[t,t+1]` is a typed relation over the transformation instances in `U_[t,t+1]`, with each edge carrying a frozen relation type, semantic predicate, temporal scope and provenance.

Longitudinal change is represented by the transition between `R_[t,t+1]` and `R_[t+1,t+2]`, after applying the frozen persistence mapping `π`.

The candidate B object is therefore treated as the longitudinal structure:

`Ω_T = { (U_[t,t+1], ≡_T, R_[t,t+1], π_[t,t+1]) }_t`

rather than a single graph at an isolated time point.

### 15.4 Remaining freeze condition
This correction resolves the three identified specification defects at the conceptual level. Before freeze, the exact admissible relation vocabulary, persistence cases and serialization schema must be reviewed for circularity, A-reconstructibility and observation parity.

**Status: CORRECTED CANDIDATE — NOT YET FROZEN.**
