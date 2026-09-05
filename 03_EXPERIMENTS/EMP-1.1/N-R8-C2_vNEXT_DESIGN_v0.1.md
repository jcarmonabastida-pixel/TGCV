# N-R8-C2 vNext — Design Specification v0.1

## Status

**DRAFT FOR REVIEW — NOT FROZEN**

This document defines the next candidate operationalisation after the N-R8-C2 derivability block. It is intentionally a design document only. No new corpus, dataset processing, or scientific execution is authorised by this document.

## 1. Problem to solve

The previous C2 matching key fixed `B + R1 + R2 + R3` and additional redundant cardinalities. Under the frozen Branch N semantics, this makes the full `R` representation derivable from the matching key. Therefore the previous equal-key / unequal-`R` test could not establish the intended non-redundancy claim.

C2 vNext must remove the information that directly encodes the target representation while retaining a meaningful state-level constraint.

## 2. Design principle

The new matching key must constrain the **local state class** without encoding the transformation-universe summaries whose independent information is being tested.

Accordingly, C2 vNext will not include:

- R1;
- R2;
- R3;
- R4;
- `|T_acc|`;
- any direct count of transformation families;
- any statistic explicitly computed from `T_acc`.

## 3. Candidate matching key

The candidate key is:

`K_C2_vNext = B + K_S^local`

where:

- `B = (|V|, q1, q2, q3, objective)`;
- `K_S^local` is a structural state signature derived only from the current snapshot `(V,E)` and resource/objective context, and is fixed independently of `T_acc`.

The preferred first candidate is a deliberately low-order graph signature:

`K_S^local = (|E|, degree-multiset(V))`

with degree-multiset represented canonically as the sorted multiset of total directed incidences per component (`in_degree + out_degree`).

This retains coarse state organisation while avoiding direct transformation-family counts.

## 4. Target observable

The target remains the transformation-organisation observable `O_T` constructed from the one-step transformation universe:

- nodes = valid transformations in `T_acc`;
- an edge joins two transformations when their sequential application commutes on the current state;
- `O_T` is represented by graph-level structural coordinates (node count, component structure, degree classes, triangles and canonical graph hash).

The target is therefore explicitly downstream of `T_acc`, while the proposed key is computed directly from the current state.

## 5. Intended independent degree of freedom

The intended independent degree of freedom is **transformation organisation at fixed coarse state signature**.

Two states may share:

- the same number of components;
- the same resource vector;
- the same objective;
- the same number of directed edges;
- the same multiset of total component incidences;

while differing in the arrangement of those edges. That arrangement can alter the admissible transformation set and, potentially, the commutation structure among transformations.

This is the specific structural variation that the vNext probe must test.

## 6. Non-circularity requirement

The candidate key is constructed without inspecting transformation enumeration, transformation application, `R`, or `O_T`.

The probe must compute `K_C2_vNext` directly from `State` before any target observable is evaluated.

No feature may be added to the key because it improves the rate of collisions or produces a desired result.

## 7. Falsification / fail-closed rule

The bounded vNext probe must search for at least one pair `(A,B)` such that:

`K_C2_vNext(A) = K_C2_vNext(B)`

and

`O_T(A) != O_T(B)`.

Decision rule:

- if such a pair is found: `IDENTIFIABLE` for the tested bounded fixture family;
- if no such pair is found: `UNRESOLVED_OR_DERIVED`; do not infer global derivability from the bounded search alone;
- if implementation invariants fail: `BLOCKED_INFRASTRUCTURE` and no scientific interpretation.

## 8. Fixture requirement

The previous fixed-edge-subset fixture is not sufficient as the primary design because the vNext question specifically requires rearrangements at fixed coarse graph statistics.

The new bounded fixture must therefore contain non-isomorphic directed graphs with equal:

- `|V|`;
- `|E|`;
- degree-multiset;

while allowing different edge arrangements.

The fixture should remain small enough for exhaustive enumeration before any stochastic corpus is considered.

## 9. Required pre-execution audit

Before implementing or running the probe, verify formally that:

1. `K_C2_vNext` contains no `R` coordinate directly or indirectly through a transformation-derived statistic;
2. the fixture actually contains collisions under the candidate key;
3. the intended edge rearrangement degree of freedom is non-empty;
4. the target observable is computed independently of key construction;
5. the probe remains result-blind.

## 10. Scope boundary

This design does **not** authorize:

- generation of the 5,000-pair corpus;
- processing of the Rust dataset;
- scientific execution of EXT-1.1;
- modification of N-R1.3;
- acceptance of C2 vNext as established.

Those actions require a subsequent frozen specification and a passing bounded identifiability probe.

## 11. Next gate

The immediate next task is a **pure derivability/non-circularity audit of `K_C2_vNext`**, followed by construction of the smallest exhaustive fixture capable of producing the required key collisions.

Only after that audit passes should the vNext probe be implemented.
