# N-R8.2.3 — C Amended Operationalisation v0.1

**Status:** PROPOSED — DESIGN AMENDMENT, NOT FROZEN
**Date:** 2026-09-05
**Parent:** N-R8.2 Operationalisation Specification v0.1
**Predecessor amendment:** N-R8.2.2 C Structural-Confounding Identifiability Analysis and Amendment v0.1

## 1. Purpose

This amendment incorporates the pre-execution identifiability finding recorded in N-R8.2.2 into the executable N-R8-C definition. It supersedes only the N-R8-C matching key; all other N-R8 semantics remain inherited from N-R8.2 v0.1 and N-R8.2.1.

No N-R7 artifact, result, learner output, outcome, p-value, or historical result has been used to select this amendment.

## 2. Normative N-R8-C matching key

A valid N-R8-C candidate pair A,B must satisfy exact equality for:

- B(S), all 16 baseline features;
- R family availability, six features;
- R family cardinality, six features;
- R3 component-incidence, 30 features;
- |T_acc|;
- number of non-empty accessible-transformation families;
- number of components;
- resources;
- objective.

The equality of **graph edge count is explicitly removed** from the matching constraints.

The pair must satisfy:

`R(A) != R(B)`

for the complete authoritative 58-dimensional N-R1.3 v0.2 representation.

The amended key is therefore:

`K_C(S) = (B(S), R_family_availability(S), R_family_cardinality(S), R_component_incidence(S), |T_acc(S)|, family_count(S), n_components(S), resources(S), objective(S))`.

The omission of edge count is intentional and minimal: the pre-execution analysis established that the original key fixed the quantities determining the R4 successor-structure coordinates, eliminating the required full-R degree of freedom.

## 3. Pair construction

The constructor shall use seed `5_300_000`, generate a deterministic candidate stream using the frozen G2-compatible state generator, and bucket candidates by the amended `K_C`.

Within each bucket, candidate pairs are evaluated in deterministic generation order and accepted only when their complete 58-dimensional R vectors differ.

Target: **5,000 valid pairs**.

Maximum candidate-pair evaluation budget: **5,000,000**.

Search stops immediately at the target. Failure to reach the target within the budget is fail-closed: no partial corpus may be promoted to frozen status.

The constructor must retain candidate-pool size, bucket counts, accepted/rejected counts, evaluation count, pair ordering, seed, implementation hash, and all relevant artifact hashes.

## 4. Required conformance

The N-R8-C conformance fixture must independently demonstrate all of the following:

1. exact equality of the amended matching key;
2. exact inequality of the full 58-dimensional R vector;
3. no outcome, trajectory, learner, or N-R7-result dependency;
4. deterministic construction semantics;
5. fail-closed target/budget behavior.

A failed fixture search is a conformance failure and must not be bypassed by weakening the assertion or fabricating a pair.

## 5. R2 test correction

The R2 empty-T_acc test shall temporarily replace the `tacc` symbol in the authoritative `branch_n_r8_operationalisation_v01` module namespace, because `r2()` resolves that module-global symbol. The original symbol must be restored in a `finally` block.

This is a test-harness correction only and does not alter R2 semantics.

## 6. Governance

This amendment remains PROPOSED until implementation and conformance demonstrate that the amended N-R8-C condition is executable and that all required controls remain intact.

No N-R8.4 full corpus generation is authorized by this amendment alone.

**Decision:** N-R8.2.3 AMENDMENT PROPOSED; N-R8.4 remains BLOCKED pending conformance PASS and subsequent integrity freeze.
