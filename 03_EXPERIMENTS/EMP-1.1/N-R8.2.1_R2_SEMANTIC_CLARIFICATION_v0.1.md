# N-R8.2.1 — R2 Semantic Clarification v0.1

**Status:** PROPOSED — NOT FROZEN
**Date:** 2026-09-05
**Parent:** N-R8.2 Operationalisation Specification v0.1

## 1. Purpose

This clarification resolves the only material semantic ambiguity identified during N-R8.3 implementation: the meaning of transformation `src(τ)` and `dst(τ)` used by R2 features 5–6 and the exact interpretation of resource transformations.

It is intentionally prospective and result-blind. It does not alter N-R7 or any sealed artifact.

## 2. Principle

`src(τ)` and `dst(τ)` are **transformation-instance incidence sets**, not causal source/target states.

They identify the component endpoints explicitly implicated by the transformation instance itself. They do not attempt to infer a semantic actor, causal agent, or realized future transition.

This keeps R2 a representation of the accessible transformation structure and avoids importing trajectory information.

## 3. Exact incidence mapping

For every accessible transformation instance `τ`:

| Family | Canonical instance | `src(τ)` | `dst(τ)` |
|---|---|---|---|
| ADD_COMPONENT | `ADD_COMPONENT(v)` | `∅` | `{v}` |
| REMOVE_COMPONENT | `REMOVE_COMPONENT(v)` | `{v}` | `∅` |
| ADD_EDGE | `ADD_EDGE(u,v)` | `{u}` | `{v}` |
| REMOVE_EDGE | `REMOVE_EDGE(u,v)` | `{u}` | `{v}` |
| REWIRE_EDGE | `REWIRE_EDGE(u,v,w)` | `{u}` | `{w}` |
| MODIFY_RESOURCE | `MODIFY_RESOURCE(i,d)` | `∅` | `∅` |

For `REWIRE_EDGE`, the removed target `v` is not included in `dst(τ)` because the transformation's resulting relational incidence is with `w`; the old endpoint is represented by the explicit transformation parameters and the successor-state delta, not by `dst`.

The incidence sets are sets, so each component can occur at most once within `src(τ)` or `dst(τ)`.

## 4. Exact R2 feature semantics

The 24-dimensional R2 vector is ordered exactly as follows:

1. `total_tacc = |T_acc|`;
2. `nonempty_family_count`;
3. Shannon entropy of family proportions;
4. Herfindahl concentration of family proportions;
5. mean `|src(τ)|`;
6. mean `|dst(τ)|`;
7. mean absolute resource delta across successor states;
8. mean component-count delta `|V'|-|V|`;
9. mean edge-count delta `|E'|-|E|`;
10. mean positive edge-count change `max(ΔE,0)`;
11. mean edge-count decrease `-min(ΔE,0)`;
12. fraction of accessible transformations in `ADD_COMPONENT`;
13. fraction in `REMOVE_COMPONENT`;
14. fraction in `MODIFY_RESOURCE`;
15. fraction in edge-transform families `{ADD_EDGE, REMOVE_EDGE, REWIRE_EDGE}`;
16. fraction in component-transform families `{ADD_COMPONENT, REMOVE_COMPONENT}`;
17. fraction preserving component count (`ΔV=0`);
18. fraction preserving edge count (`ΔE=0`);
19. fraction modifying resources (`MODIFY_RESOURCE`);
20. fraction modifying edges (`ADD_EDGE`, `REMOVE_EDGE`, `REWIRE_EDGE`);
21. mean Jaccard similarity between `V` and `V'`;
22. mean Jaccard similarity between `E` and `E'`;
23. population standard deviation of `ΔE`;
24. population standard deviation of `ΔV`.

The existing N-R8.2 wording “mean absolute resource delta” is therefore retained, while feature 8 and feature 9 remain signed means.

## 5. Resource transformation semantics

N-R1.2 defines `MODIFY_RESOURCE(i,d)` with `d ∈ {-1,+1}` and precondition `qi+d ∈ {0,1,2,3}`.

Therefore N-R8 implementation **must not** enumerate arbitrary jumps such as `0→2` or `1→3` in one transformation instance.

For each resource index `i`, exactly those one-unit modifications satisfying the boundary condition are accessible.

This clarification supersedes the implementation shortcut that treated a resource transformation as direct assignment to every alternative value.

## 6. Empty T_acc rule

If `T_acc = ∅`, all 24 R2 values are exactly `0.0`.

This is a representation convention, not a claim that entropy or Jaccard has a naturally defined value at an empty domain.

## 7. R2 non-circularity

R2 may inspect only:

- the frozen initial state S;
- the finite accessible transformation instances `T_acc(S)`;
- the deterministic successor `S' = τ(S)` for each accessible τ.

R2 may not inspect:

- trajectory realizations;
- terminal states;
- Y;
- terminal reason;
- number of executed steps;
- learner predictions;
- N-R7 results;
- future snapshots;
- post-snapshot corpus fields.

## 8. Deterministic numerical rules

All R2 values use IEEE-754 double precision.

For standard deviation, the population definition is required:

`sqrt(mean((x - mean(x))^2))`.

For Jaccard similarity:

`J(A,B)=|A∩B|/|A∪B|` when the union is non-empty. If both sets are empty, Jaccard is defined as `1.0`.

Family proportions are computed over the complete accessible transformation set.

Entropy uses natural logarithms. Zero-proportion terms contribute zero.

## 9. Consequence for N-R8.3

The implementation created during N-R8.3 must be corrected before conformance to:

1. use the exact incidence mapping in Section 3;
2. implement `MODIFY_RESOURCE(i,±1)` exactly as N-R1.2 specifies;
3. expose all 24 features in the order of Section 4;
4. ensure feature names and implementation comments correspond exactly to these semantics;
5. add dedicated fixtures covering every transformation family and at least one resource boundary case.

No corpus generation or scientific execution is permitted until these conditions pass conformance.

## 10. Gate status

**N-R8.2.1: PROPOSED / CLARIFICATION COMPLETE**

This clarification removes the identified semantic ambiguity and authorizes a corrected implementation/conformance cycle. It does not itself freeze N-R8.2 and does not authorize execution.
