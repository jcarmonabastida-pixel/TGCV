# DR-042 — RUST-DYN-2 Re-Anchoring Design Review v0.1

**Date:** 2026-09-08  
**Status:** ACCEPTED — DESIGN FREEZE / EXECUTION NOT AUTHORIZED

## Decision

The RUST-DYN-2 design re-anchoring is accepted, subject to two implementation freezes: (1) canonical successor-configuration identity and (2) a non-arbitrary trajectory representation.

## Evidence reconstructed

1. Historical Rust Potential Reach semantics are frozen and reusable:
   `Succ(C,τ) = C \ {(p_d,*)} ∪ {(p_d,v_d)}`.
2. Historical Reach non-redundancy was accepted by DR-018.
3. DR-041 reconciled the historical Reach semantics and superseded the stronger independent-graph requirement of DR-040 in scope.
4. Temporal population reconciliation is EXACT: historical and DR-035 populations are identical at 516,061 pairs, with identical pair-set SHA-256 `1c7a29434675d5e7bbe5a1cfc3a44a809d8eae222d3467374177d8bd20048d8e` and zero timestamp ties.
5. Current RUST-DYN-2 transformation identity remains the frozen four-field tuple.

## Design findings

### A. Successor identity — ACCEPTED WITH IMPLEMENTATION FREEZE

Reach¹_pot must be represented as canonical successor **configuration identities**, not as transformation tuples. The successor is generated structurally from the focal configuration by replacing the relevant dependency target assignment with the target-version assignment implied by τ.

The canonical serialization must be deterministic, complete for the represented structural configuration, and independent of execution/runtime outcomes.

### B. Trajectory at H=1 — BOUNDED / NON-ARBITRARY ONLY

At H=1, each admissible transformation yields a potential successor configuration. A one-step trajectory can therefore be represented as the ordered transformation-to-successor construction associated with the canonical input ordering, but no arbitrary ordering may be introduced merely to manufacture trajectory differences.

For scientific sufficiency, trajectory ordering must have an explicit source of order. If multiple one-step successors have no semantically justified order, the executor must represent the trajectory as an unordered singleton-step successor object rather than invent an ordering.

Consequently, no H>1 trajectory claim is authorized by this DR.

### C. Dynamic distinction — ACCEPTED AS TEST TARGET

The primary new comparison remains:

`ΔT = 1[T_i ≠ T_j]`

versus

`ΔR = 1[R_i ≠ R_j]`.

Reach equality is exact set membership equality. Cardinality-only comparisons are insufficient.

ND-1 through ND-4 remain valid H=1 structural targets. ND-5 is conditional on a non-arbitrary trajectory representation and is not required to authorize the H=1 Reach comparison.

## Required implementation constraints

- reuse the historical successor semantics;
- use DR-035 temporal population;
- use four-field τ identity;
- canonicalize successor configurations deterministically;
- fail closed on duplicate/ambiguous structural identities;
- do not introduce a hidden resolver;
- do not use execution, lockfiles, outcomes, future activity, adoption, downloads, value or predictive metrics;
- no sampling;
- produce deterministic hashes and provenance;
- synthetic conformance before real-data execution;
- real-data execution requires a separate authorization decision.

## Governance consequence

The previous design blocker concerning an independent successor graph is closed in scope by DR-041. The current blocker is reduced to implementation-level canonical serialization and bounded trajectory representation.

**REAL-DATASET RUST-DYN-2 EXECUTION AUTHORIZED: NO.**

## Next gate

Construct the dedicated RUST-DYN-2 executor using the accepted historical Potential Reach semantics, first with synthetic conformance. Then run a new real-data preflight against the frozen dataset and require an explicit execution authorization gate.
