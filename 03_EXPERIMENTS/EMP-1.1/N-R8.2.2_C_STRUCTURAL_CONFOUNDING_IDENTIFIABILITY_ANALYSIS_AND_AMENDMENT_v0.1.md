# N-R8.2.2 — C Structural-Confounding Identifiability Analysis and Amendment v0.1

**Status:** PROPOSED — DESIGN AMENDMENT, NOT FROZEN
**Date:** 2026-09-05
**Parent:** N-R8.2 Operationalisation Specification v0.1
**Purpose:** Resolve the failed N-R8-C conformance fixture without weakening the fail-closed rule or fabricating a qualifying pair.

## 1. Finding

The original N-R8-C matching key fixed:

- B;
- R1 family availability;
- R2 family cardinality;
- R3 component-incidence;
- |T_acc|;
- family count;
- component count;
- **edge count**;
- resources;
- objective.

The full authoritative R vector is R1 + R2 + R3 + R4, with R4 consisting of 16 successor-structure statistics.

Under the frozen Branch N transformation semantics, the original key fixes the quantities that determine all R4 coordinates:

1. R4 coordinates 1–7 are exactly the R2 family counts and resource-direction counts.
2. R4 coordinate 8 (`n_noop`) is identically zero because every valid transformation changes S under N-R1.2.
3. R4 coordinates 9 and 13–14 depend on component count and the component-transform family counts, all fixed by B/R2.
4. R4 coordinates 10 and 15–16 depend on edge count and edge-transform family counts, all fixed by the original key.
5. R4 coordinate 11 is determined by the fixed resource tuple and accessible resource transformations.
6. R4 coordinate 12 (`len(set(next_states))`) is fixed by the injective transformation-to-successor mapping of the frozen transformation universe; with canonical transformations, distinct valid transformations yield distinct successor states.

Therefore the original N-R8-C key leaves no intended degree of freedom for a full-R inequality. The observed conformance failure

`NO_C_FIXTURE_FOUND_WITHIN_64_EDGE_SUBSETS`

is therefore treated as a specification-identifiability failure, not as evidence against H1-N and not as a reason to weaken the conformance runner.

## 2. Corrective amendment

The explicit **edge-count equality condition is removed** from the N-R8-C matching key.

The amended key is:

`K_C(S) = (B(S), R_family_availability(S), R_family_cardinality(S), R_component_incidence(S), |T_acc(S)|, family_count(S), n_components(S), resources(S), objective(S))`.

All other conditions remain unchanged, including the requirement:

`R(A) != R(B)` for the full 58-dimensional authoritative R vector.

The purpose is precise: preserve baseline state, transformation-family availability/cardinality, component-level incidence, accessibility-set cardinality, component cardinality, resources and objective while leaving graph-level edge organization/count as a controlled residual degree of freedom. The attack therefore tests whether higher-order structural information survives after these lower-order summaries are matched.

This is an operationalisation amendment, not a result-driven adjustment: no N-R8 result, learner output, outcome, p-value, or historical result motivated the choice. The amendment is derived solely from the pre-execution identifiability analysis of the frozen representation and transformation semantics.

## 3. Remaining fail-closed condition

The amendment does **not** guarantee that 5,000 valid C pairs exist. The constructor must still search deterministically and fail closed if the frozen target cannot be reached within the frozen 5,000,000 candidate-pair evaluation budget.

If no qualifying pair exists after implementation of this amended key, N-R8-C remains blocked and requires a new scientific design decision. No synthetic exception or fabricated fixture is permitted.

## 4. Runner correction

The separate `r2_empty_zero` conformance failure is classified as an implementation-test defect: the runner patched the local module namespace rather than the `tacc` function actually referenced by the R2 implementation. The corrected test must patch the authoritative operationalisation module namespace and restore it after the assertion.

This runner correction does not alter R2 semantics.

## 5. Governance decision

Until this amendment is incorporated into the parent N-R8.2 specification, N-R8.4 remains **PROPOSED / NOT FROZEN** and scientific execution remains blocked.

Required next action:

1. incorporate the amended C key into N-R8.2;
2. update the N-R8.4 constructor to the amended key;
3. strengthen the N-R8.3 rewire conformance assertion if still outstanding;
4. correct the R2 empty-T_acc test;
5. rerun N-R8.3/N-R8.4 conformance;
6. only after PASS, perform the N-R8.4 integrity freeze.
