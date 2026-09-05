# N-R8.4.1 — Amendment: N-R8-C Matching Key and Conformance v0.1

**Status:** PROPOSED — NOT FROZEN  
**Date:** 2026-09-05  
**Parent:** N-R8.4 Controlled Corpus Construction and Integrity Freeze Specification v0.1  
**Predecessors:** N-R8.2.3, N-R8.2.4  

## 1. Purpose

This amendment reconciles the N-R8.4 construction specification with the already-approved N-R8.2.3 amendment and N-R8.2.4 interpretive qualification.

It is an operational and conformance amendment only. It does not authorize scientific execution and does not alter N-R7.

## 2. Normative C matching key

For N-R8-C, the constructor and integrity checks MUST use the amended key:

`K_C* = (B, R_family_availability, R_family_cardinality, R_component_incidence, |T_acc|, family_count, n_components, resources, objective)`

The following equality constraints therefore remain fixed:

- B (16 dimensions);
- R1 family availability;
- R2 family cardinality;
- R3 component-incidence features;
- `|T_acc|`;
- number of accessible transformation families;
- component count;
- resource tuple;
- objective.

**Graph edge count is deliberately NOT a matching-key coordinate.**

After exact `K_C*` equality, the pair MUST satisfy full authoritative `R1(A) != R1(B)` over all 58 dimensions.

## 3. Interpretive boundary

The resulting N-R8-C contrast leaves edge-level organization, including edge count, unconstrained. Therefore a successful result MUST NOT be described as proof of an abstract representation-independent "higher-order structure".

The admissible claim is:

> N-R8-C tests whether predictive/outcome-relevant information remains in the accessible-transformation structure after the specified low-order summaries are held exactly fixed.

A successful result supports residual structural information beyond the matched summaries. It does not isolate a unique causal coordinate, prove universality, or establish representation-independent higher-order structure.

## 4. Constructor requirements

The canonical implementation `branch_n_r8b4_corpus_v01.py` MUST:

1. compute `_c_match_key` without `len(state.edges)`;
2. preserve the full 58-dimensional R inequality check;
3. retain seeds `5_300_000`, target `5,000`, and maximum candidate-pair evaluation budget `5,000,000`;
4. fail closed if the target is not reached within budget;
5. use only initial-state information for pair construction;
6. contain no learner, outcome, trajectory, N-R7-result, or N-R8-result dependency.

## 5. Conformance requirements

The N-R8 conformance runner MUST independently verify:

- amended `K_C*` equality;
- full 58-D R inequality;
- deterministic C fixture construction;
- deterministic G2 generation;
- frozen seed and budget constants;
- fail-closed behavior;
- absence of learner/result dependencies;
- R2 dimension and empty-`T_acc` zero behavior.

The empty-`T_acc` test MUST patch the authoritative `tacc` symbol in the `branch_n_r8_operationalisation_v01` module namespace and restore it in `finally`.

The runner MUST remain fixture-only and MUST NOT construct the 5,000-pair corpus.

## 6. Gate state

N-R8.3 implementation/conformance was previously closed PASS, but the amended N-R8-C rule requires this conformance amendment to be treated as a downstream implementation reconciliation.

Therefore:

- N-R8.2.3: PROPOSED — DESIGN AMENDMENT;
- N-R8.2.4: PROPOSED — INTERPRETIVE QUALIFICATION;
- N-R8.4.1: PROPOSED — AMENDMENT;
- N-R8.4: NOT FROZEN;
- scientific execution: BLOCKED.

The next action is to execute the amended fixture-only conformance runner and record its PASS/FAIL evidence before any full N-R8.4 corpus generation.
