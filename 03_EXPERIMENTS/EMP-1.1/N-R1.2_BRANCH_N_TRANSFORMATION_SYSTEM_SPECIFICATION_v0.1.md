# N-R1.2 — Branch N Transformation-System Specification v0.1

**Program:** TGCV  
**Experiment:** EMP-1.1  
**Branch:** N — Controlled New Reconstruction  
**Status:** PROSPECTIVE SPECIFICATION — NOT HISTORICAL RECOVERY  
**Gate:** N-R1.2  
**Date:** 2026-09-05

## 1. Purpose and boundary

This document specifies the transformation universe for the controlled new reconstruction of EMP-1.1. It does **not** recover or claim the exact historical transformation semantics of MVE-1.0/EMP-1.1.

All choices not directly recovered from prior artifacts are explicitly marked **RECONSTRUCTED** or **DERIVED**. The historical recorded result is not used as a selection, tuning, or acceptance target for any transformation family.

This specification is upstream of implementation. No confirmatory execution is authorized by this document alone.

## 2. Recovered domain constraints

The following constraints were recovered from historical-domain artifacts and are therefore treated as domain constraints for Branch N:

| Element | Specification | Provenance |
|---|---|---|
| Component universe | `A1, A2, B1, B2, C1, C2` | RECOVERED |
| Initial component count | `3 <= |V| <= 5` | RECOVERED |
| Resources | exactly 3 discrete resource variables | RECOVERED |
| Objectives | 12 objective identities | RECOVERED |
| Outcome horizon | `H = 6` | RECOVERED |
| Relation representation | directed edge structure | RECOVERED |

The exact historical value domains, update equations, objective-goal predicates, and generator distributions remain unresolved unless explicitly specified below as new Branch N choices.

## 3. Branch N state space

A snapshot is represented as:

`S = (V, E, q, o)`

where:

- `V` is the active component set;
- `E` is the directed relational structure over active components;
- `q = (q1,q2,q3)` is the three-resource vector;
- `o` is the objective identity.

The objective is retained as an exogenous snapshot attribute. It is **not** used to define whether a transformation is accessible.

### 3.1 Components

`U_V = {A1, A2, B1, B2, C1, C2}`.

For every valid state, `V subseteq U_V`.

Branch N retains the recovered initial constraint `3 <= |V| <= 5`. Subsequent transformations may move the component count within the global state-space bounds defined below.

### 3.2 Directed relations

For Branch N, `E` is a simple directed graph over `V`:

`E subseteq {(u,v) in V x V : u != v}`.

No self-loop and no duplicate edge are permitted. This graph convention is a **RECONSTRUCTED** formalization of the recovered directed-edge representation; it is not claimed as recovered historical implementation semantics.

### 3.3 Resources

There are exactly three resource variables `q1,q2,q3`.

For the controlled new reconstruction, each resource is assigned the finite ordered domain:

`D_q = {0,1,2,3}`.

This finite domain is a **RECONSTRUCTED** Branch N choice. It must not be described as the historical resource domain.

### 3.4 Objectives

The 12 objective identities are represented as opaque categorical labels:

`O = {O01,...,O12}`.

Their historical goal predicates are not reconstructed in N-R1.2. Therefore objective identity may be used as a baseline feature exactly as specified by the frozen EMP-1.1 protocol, but no new claim about historical objective semantics is made here.

### 3.5 Global state validity

A state is valid iff:

1. `1 <= |V| <= 6`;
2. `V subseteq U_V`;
3. `E` is a simple directed edge set over `V` with no self-loops;
4. each `qi in D_q`;
5. `o in O`.

The lower bound `|V| >= 1` is a **RECONSTRUCTED** guard against degenerate empty states. It is not a historical claim.

## 4. Transformation universe

Branch N defines exactly six transformation families:

1. `ADD_COMPONENT`
2. `REMOVE_COMPONENT`
3. `ADD_EDGE`
4. `REMOVE_EDGE`
5. `REWIRE_EDGE`
6. `MODIFY_RESOURCE`

These six identities are **RECONSTRUCTED**, not historically recovered. They are selected because they span component-set change, relational addition/removal/rewiring, and explicit resource-state change while remaining finite, observable, and mechanically testable.

`MODIFY_ATTRIBUTE`, proposed in the earlier N-R1 draft, is **REJECTED** from the Branch N default universe because recovered artifacts do not justify a generic attribute state variable or its semantics.

## 5. Canonical transformation instances

Every transformation is an explicit typed instance. A family alone is not an element of `T_acc`.

### 5.1 ADD_COMPONENT

Instance:

`ADD_COMPONENT(v)` where `v in U_V \ V`.

Precondition:

`v notin V` and `|V| < 6`.

Transition:

`V' = V union {v}`  
`E' = E`  
`q' = q`  
`o' = o`

No edges incident to the newly added component are created by this transformation.

The latter convention is **RECONSTRUCTED**.

### 5.2 REMOVE_COMPONENT

Instance:

`REMOVE_COMPONENT(v)` where `v in V`.

Precondition:

`v in V` and `|V| > 1`.

Transition:

`V' = V \ {v}`  
`E' = {(u,w) in E : u != v and w != v}`  
`q' = q`  
`o' = o`

Incident edges are removed as a deterministic consequence of removing the component. This is **DERIVED** from graph validity plus the reconstructed component-removal operation.

### 5.3 ADD_EDGE

Instance:

`ADD_EDGE(u,v)`.

Precondition:

`u,v in V`, `u != v`, and `(u,v) notin E`.

Transition:

`V' = V`  
`E' = E union {(u,v)}`  
`q' = q`  
`o' = o`

### 5.4 REMOVE_EDGE

Instance:

`REMOVE_EDGE(u,v)`.

Precondition:

`(u,v) in E`.

Transition:

`V' = V`  
`E' = E \ {(u,v)}`  
`q' = q`  
`o' = o`

### 5.5 REWIRE_EDGE

Instance:

`REWIRE_EDGE(u,v,w)`.

Precondition:

`(u,v) in E`, `u,w in V`, `v != w`, `u != w`, and `(u,w) notin E`.

Transition:

`V' = V`  
`E' = (E \ {(u,v)}) union {(u,w)}`  
`q' = q`  
`o' = o`

The source endpoint is preserved and the target endpoint changes. This asymmetric definition is **RECONSTRUCTED** and is fixed prospectively for deterministic implementation.

### 5.6 MODIFY_RESOURCE

Instance:

`MODIFY_RESOURCE(i,d)` where `i in {1,2,3}` and `d in {-1,+1}`.

Precondition:

`qi + d in D_q`.

Transition:

`q'_i = qi + d`; all other resource values and all structural/objective fields remain unchanged.

This family is a **RECONSTRUCTED** use of the recovered existence of three discrete resources. It is not claimed to reproduce historical resource dynamics.

## 6. Accessibility

Let `U(S)` be the finite set of all valid typed transformation instances under the six families above.

For every `tau in U(S)`, define the deterministic predicate:

`P_tau(S) = 1` iff the family-specific precondition in Section 5 is satisfied.

Then:

`T_acc(S) = { tau in U(S) : P_tau(S) = 1 }`.

This is the Branch N operationalization of accessibility. It is **DERIVED** from the already frozen TGCV accessibility formulation and the reconstructed transformation predicates above.

No future state, future outcome, future trajectory, or post-snapshot information may be used in evaluating `P_tau(S)`.

## 7. Structural representation of T_acc

`T_acc` is represented as a typed structure, not merely as a scalar count.

The canonical ordering key for transformation instances is:

1. family rank in the six-family order in Section 4;
2. lexicographic component/resource parameters within family;
3. canonical component order `A1 < A2 < B1 < B2 < C1 < C2`;
4. numerical resource index;
5. numerical direction `-1 < +1`.

This deterministic ordering is **RECONSTRUCTED**.

The implementation must preserve both:

- the transformation identity/type;
- the source-state incidence needed to reconstruct structural summaries.

No feature may depend on database row order, hash iteration order, or incidental serialization order.

## 8. Boundary between T_acc and T_real

`T_acc(S)` is the set of transformations admissible from the current snapshot under the frozen Branch N rules.

`T_real` denotes transformations actually realized in a subsequent trajectory.

They must remain separate. A transformation is not removed from `T_acc` merely because it is not subsequently observed as realized, and future realization must never be used to define snapshot accessibility.

## 9. Interaction with baseline B

The frozen EMP-1.1 baseline remains unchanged:

- component count;
- three resource values;
- objective identity.

The Branch N R representation is intended to add structural information derived from `T_acc` rather than replacing B.

This document does **not** yet freeze the exact numerical feature vector `R`, its dimensionality, normalization, or learner encoding. Those belong to the next reconstruction specification.

## 10. Determinism and invariants

The implementation must satisfy at minimum:

1. identical valid `S` produces identical `T_acc`;
2. permutation of input component/edge row order does not alter `T_acc`;
3. no transformation instance violates global state validity;
4. every transformation has exactly one family identity and canonical parameterization;
5. `ADD_COMPONENT` changes only `V`;
6. `REMOVE_COMPONENT` changes `V` and removes only incident edges;
7. `ADD_EDGE` changes exactly one edge by addition;
8. `REMOVE_EDGE` changes exactly one edge by deletion;
9. `REWIRE_EDGE` preserves edge count and changes exactly one source-target relation;
10. `MODIFY_RESOURCE` changes exactly one resource by one unit;
11. objective identity is unchanged by all six transformations;
12. no future/outcome variable enters accessibility evaluation.

## 11. Provenance classification

### RECOVERED

- six component identifiers;
- initial 3–5 component range;
- existence of three resources;
- existence of 12 objectives;
- directed edge representation;
- horizon `H=6` as outcome-horizon information.

### DERIVED

- generic accessibility construction from valid transformation predicates;
- removal of incident edges as necessary to maintain graph validity after component removal.

### RECONSTRUCTED

- exact six transformation identities;
- simple directed graph formalization;
- resource domain `{0,1,2,3}`;
- global lower component bound;
- exact family preconditions and transition equations;
- canonical instance ordering;
- no incident edges on component addition;
- asymmetric source-preserving rewire.

### OPEN / NOT CLAIMED

- exact historical six-family identity;
- exact historical resource domain and dynamics;
- exact historical objective-goal predicates;
- historical generator distribution;
- historical implementation identity;
- exact R aggregation/encoding.

## 12. Gate decision — N-R1.2

**N-R1.2 STATUS: PASS / CLOSED**

The Branch N transformation system is now sufficiently explicit to permit implementation-level unit-test design without consulting the historical recorded result.

**Important:** N-R1 as a broader gate remains **BLOCKED** because exact R aggregation, dimensionality, encoding, and related reconstruction choices are not yet frozen.

### Next gate

**N-R1.3 — Branch N R Encoding and Feature Specification**

N-R1.3 must specify, prospectively and without result-driven tuning:

- exact R feature blocks;
- dimensionality;
- structural summaries;
- transformation-instance aggregation;
- empty/degenerate encodings;
- categorical/numerical representation;
- normalization;
- feature ordering and serialization;
- traceability from each R feature to `T_acc`.

No confirmatory EMP-1.1 execution is authorized until the relevant reconstruction gates are closed.
