# TGCV — N-R8-C2 Bounded Identifiability Probe Specification v0.1

**Status:** GOVERNANCE SPECIFICATION / NOT EXECUTED
**Date:** 2026-10-01
**Parent:** N-R8.2.7 C Independent Transformation-Organisation Design
**Decision:** ARCH-DISC-002

## 1. Purpose

Specify the smallest reproducible technical gate capable of determining whether the proposed transformation-organisation object G_T / candidate vector O_T contains at least one independently identifiable coordinate under the frozen matching key K_C2.

This document authorizes specification only. It does not authorize scientific execution or corpus generation.

## 2. Question

Does there exist a bounded pair of valid states A,B such that K_C2(A) = K_C2(B) and at least one candidate O_T coordinate differs, while the complete inherited representation required by the current design remains equivalent where equivalence is expected?

A positive result establishes only identifiability within the bounded search domain. It does not establish architectural non-equivalence or any TGCV claim.

## 3. Frozen inputs

The probe shall use only N-R1.2 canonical transformation semantics; N-R1.2 canonical state semantics; the exact K_C2 definition in N-R8.2.7; the exact G_T relation in N-R8.2.7; the candidate O_T coordinates in N-R8.2.7; fixed resources and objective; and deterministic canonical serialization.

Forbidden inputs: outcomes, trajectories, learner predictions or losses, N-R7/N-R8 results, historical experimental results, and any statistic selected after inspecting probe outcomes.

## 4. Bounded search domain

The first probe shall use only a microscopic exhaustive fixture family: fixed 3-component directed-edge systems, fixed resources, fixed objective, all directed-edge subsets permitted by the N-R1.2 state constructor over the fixed 4-component fixture, and deterministic lexicographic enumeration.

The domain boundary must be encoded explicitly in the execution artifact. No expansion of the domain is permitted within the same version.

If the domain contains no valid pair satisfying the matching key, the result is BLOCKED — NO MATCHING PAIR IN BOUNDED DOMAIN, not a reason to enlarge the search.

## 5. Pair construction

For each valid state: construct canonical T_acc; construct complete R; construct G_T; construct candidate O_T; compute frozen K_C2; serialize all representations deterministically.

States are grouped by exact byte-level serialization of K_C2. Within each group, candidate pairs are examined deterministically.

## 6. Identifiability classification

IDENTIFIABLE: at least one pair exists with identical K_C2 and different coordinate value, while all required inherited-equivalence controls pass.

DERIVED: exhaustive enumeration of the bounded domain shows the coordinate is constant within every K_C2 equivalence class. This is a bounded-domain result, not a mathematical proof outside the domain.

UNRESOLVED: the implementation cannot establish either condition because the domain or inherited-equivalence test is insufficient.

## 7. Full-vector classification

O_T may be retained as a contrast vector only if at least one coordinate is IDENTIFIABLE. DERIVED coordinates must be excluded from the structural contrast. UNRESOLVED coordinates must not be used for a scientific contrast.

## 8. Required diagnostics

The execution artifact must record the exact fixture-family definition; enumeration count; valid-state count; number of K_C2 equivalence classes; class-size distribution; candidate-pair count examined; per-coordinate classification; first deterministic witness pair for each IDENTIFIABLE coordinate; canonical R hashes for witness pairs; G_T hashes; O_T values; deterministic serialization hashes; runtime; and memory diagnostics.

The witness is provenance only; it does not become a scientific result until later gates are satisfied.

## 9. PASS / BLOCKED / FAIL semantics

PASS — IDENTIFIABILITY ESTABLISHED: at least one O_T coordinate is IDENTIFIABLE.

BLOCKED — NO IDENTIFIABLE COORDINATE: no coordinate is identifiable in the bounded domain, with no evidence that the construction itself is invalid.

FAIL — SPECIFICATION/IMPLEMENTATION NON-CONFORMITY: any frozen semantic, deterministic serialization, leakage, or control requirement is violated.

PASS does not authorize a scientific experiment. It authorizes only the next conformance/A-reconstruction gate.

## 10. Determinism and fail-closed rules

The probe must be byte-reproducible for identical source semantics and fixture version. Any mismatch in canonical transformation semantics, canonical state semantics, K_C2, graph construction, serialization, resource/objective controls causes FAIL, not silent substitution.

No ambient RNG is permitted.

## 11. Architectural boundary

A PASS establishes only that an independently varying O_T coordinate exists relative to K_C2 within the bounded fixture domain.

It does not establish A-non-equivalence, a new Core, TSDI validity, causality, predictive utility, value, or generalisation beyond the bounded domain.

## 12. Gate status

**N-R8-C2 IDENTIFIABILITY PROBE: SPECIFIED — NOT EXECUTED.**

No scientific execution, corpus generation, statistical design, workflow dispatch, or authorization is implied.

## 13. Reconciliation with pre-existing canonical D1/N-R8-C2 records

The repository already contains a frozen N-R8-C2 vNext package and an immutable bounded identifiability result. Therefore this governance specification is not an authorization to rerun that probe. The canonical result records a PASS / IDENTIFIABLE outcome over the fixed 4-component, 4,096-state exhaustive fixture, with 1,194 collision pairs examined and `K_C2_vNext(A)=K_C2_vNext(B)` plus `O_T(A)≠O_T(B)` for a deterministic witness. That result is bounded and does not establish A-non-equivalence.

Accordingly, the existing result is treated as the evidence record for the identifiability gate. No duplicate execution is required merely to satisfy this transition layer.
