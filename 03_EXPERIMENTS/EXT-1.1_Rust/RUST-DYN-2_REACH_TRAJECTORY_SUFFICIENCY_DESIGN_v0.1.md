# RUST-DYN-2 — Reach/Trajectory Sufficiency and ΔT_acc Downstream Link Design v0.1

## Status

**DESIGN DRAFT — EXECUTION NOT AUTHORIZED**

Date: 2026-09-08

## 1. Purpose

Test whether the empirically observed change in accessible transformation space (`ΔT_acc`) preserves a non-degenerate analytical distinction from changes in bounded Reach and Trajectory.

This operation is not intended to prove causality, predictive superiority, universal validity, positive value, or originality.

## 2. Preconditions

RUST-DYN-EXEC-1 is scientifically closed. Its result may be used as methodological precedent but not as evidence for the new downstream hypotheses.

The following structures remain frozen:

- `Core_ontological = S`
- `T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`
- `ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`
- DR-035 adjacent temporal population rule
- four-field transformation identity
- Rust resolver `R* v0.2`
- bounded successor-state representation from RUST-DYN-STATE-1

## 3. Central question

Does a change in `T_acc` provide information about downstream reachable futures or trajectory structure that is not reducible to the mere fact of state transition?

Operationally, the test must distinguish at least:

1. `ΔT_acc ≠ 0` with `ΔReach = 0`;
2. `ΔT_acc ≠ 0` with `ΔReach ≠ 0`;
3. `ΔReach ≠ 0` without identical `ΔT_acc` classification;
4. equal Reach cardinality with different Reach membership;
5. equal Reach with different Trajectory structure;
6. same observed one-step successor but different accessible transformation alternatives.

## 4. Objects

For each temporal pair `(o_i,o_j)`:

`T_i = T_acc(o_i)`

`T_j = T_acc(o_j)`

`R_i,H = Reach_H(o_i)`

`R_j,H = Reach_H(o_j)`

`G_i,H = Trajectory_H(o_i)`

`G_j,H = Trajectory_H(o_j)`

Primary change indicators:

`D_T = 1[T_i ≠ T_j]`

`D_R = 1[R_i,H ≠ R_j,H]`

`D_G = 1[G_i,H ≠ G_j,H]`

Set comparison must be membership-based, never cardinality-only.

## 5. Reach definition

For a selected finite horizon `H`, Reach is the set of successor-state identifiers reachable through the independently constructed structural successor graph within `1..H` steps, excluding the initial origin.

The present bounded Rust representation uses `version_id` as the accepted successor-state identifier.

Reach construction MUST NOT use T_acc membership, outcome information, popularity, downloads, later release activity, or predictive targets.

## 6. Trajectory definition

Trajectory is an ordered finite-horizon sequence of successor states induced by the structural successor graph, excluding the initial origin while preserving path order.

Trajectory equality must be sequence equality, not merely set equality or scalar length equality.

## 7. Independence requirement

T_acc, Reach and Trajectory must be constructed through logically separate procedures.

In particular:

- Reach cannot be defined as a projection of T_acc;
- Trajectory cannot be defined as an ordering of T_acc;
- T_acc cannot be reconstructed from Reach or Trajectory;
- no downstream object may feed back into `Pτ`;
- execution and observed outcome remain outside accessibility classification.

## 8. Primary non-degeneracy test

The principal test is whether the joint contingency structure of `(D_T,D_R,D_G)` contains cells demonstrating that the distinctions are not deterministically identical.

Minimum required witness classes:

### ND-1 — ΔT_acc without Reach change

`D_T = 1, D_R = 0`.

This demonstrates that a change in accessible transformations need not imply an immediate change in bounded Reach.

### ND-2 — ΔT_acc with Reach change

`D_T = 1, D_R = 1`.

This demonstrates a case in which accessibility change coincides with a downstream reachable-future difference.

### ND-3 — Reach change not identical to ΔT_acc classification

`D_R = 1` with a pattern not reducible to a one-to-one mapping from `D_T`.

The objective is distinction, not causal attribution.

### ND-4 — Equal Reach cardinality, different Reach membership

`|R_i| = |R_j|` but `R_i ≠ R_j`.

This prevents scalar reach cardinality from replacing reachable-state identity.

### ND-5 — Same Reach, different Trajectory

`R_i = R_j` but `G_i ≠ G_j`.

This tests whether path/order information adds a distinct downstream layer.

## 9. Stronger extension condition

If H=1 cannot produce the required non-degenerate cases, no conclusion of redundancy is permitted.

Instead, the design must evaluate a pre-registered H>1 extension, with explicit horizon selection and a separate governance authorization.

H>1 must not be introduced merely because it generates a desired witness.

## 10. Hypotheses

**H2-R1 — Downstream distinction:** ΔT_acc and ΔReach are not universally identical under the frozen structural representation.

**H2-R2 — Trajectory distinction:** Trajectory contains order/path information not losslessly represented by Reach as a set.

**H2-R3 — Counterfactual preservation:** T_acc can differ while observed immediate successor structure remains equal, preserving accessible alternatives not represented by the observed successor alone.

These are falsifiable structural hypotheses, not causal hypotheses.

## 11. Falsifiers

The operation must fail or remain unresolved if any of the following is established:

- every observed `ΔT_acc` is deterministically equivalent to the same `ΔReach` change;
- Reach is shown to contain all information carried by Trajectory under the frozen representation;
- T_acc can be reconstructed losslessly from Reach/Trajectory in the tested population;
- no valid ND-1 witness exists where the design requires one and the population is demonstrably capable of testing it;
- the only distinctions arise from scalar cardinality artifacts;
- downstream objects leak outcome or future information into accessibility classification;
- temporal population or structural graph construction deviates from the frozen rules;
- sampling or retrospective case selection is introduced;
- the result depends on arbitrary ordering or nondeterministic traversal.

## 12. Information firewall

The following remain prohibited during classification and witness construction:

- downloads;
- adoption/popularity/success measures;
- later release activity beyond the frozen structural representation;
- future outcomes;
- predictive targets or metrics;
- value labels;
- post-origin metadata;
- retrospective selection of pairs because they exhibit a desired result;
- sampling unless separately authorized;
- outcome-based filtering.

## 13. Proposed execution population

Primary population remains the frozen DR-035 adjacent temporal pair population unless a separate design amendment establishes a different population.

No pair may be selected because it satisfies an expected witness class.

## 14. Horizon decision rule

The first conformance implementation should test the already frozen `H=1` semantics.

Real execution at H=1 requires a fresh executor/preflight because RUST-DYN-EXEC-1 is closed.

If H=1 is structurally insufficient for the pre-registered non-degeneracy tests, a separate H>1 design gate is required before execution.

## 15. Required outputs

A future authorized execution must produce:

- dataset SHA-256;
- executor and resolver hashes;
- temporal rule identifier;
- horizon;
- population counts;
- counts for `(D_T,D_R,D_G)` cells;
- witness identifiers for each accepted non-degenerate class;
- exact set-difference summaries;
- Reach membership hashes;
- Trajectory sequence hashes;
- firewall state;
- deterministic machine-readable result;
- primary SHA-256;
- mandatory replay and byte-identity comparison.

## 16. Evidence boundary

A PASS would support a bounded statement that the tested representations preserve distinct analytical information between accessible-transformation change, reachable-state change and trajectory change.

It would not establish:

- causal direction;
- causal sufficiency;
- predictive utility;
- universal validity;
- positive value;
- originality.

## 17. Governance boundary

This document freezes a candidate design only.

**REAL-DATASET EXECUTION AUTHORIZED: NO.**

No code modification, real-data execution, or H>1 expansion is authorized by this document.

The next controlled governance operation is a formal design review of RUST-DYN-2, followed by an explicit execution-authorization decision only if the design passes.

## 18. Decision

**RUST-DYN-2 DESIGN = PROVISIONALLY SPECIFIED / EXECUTION NOT AUTHORIZED.**
