# DR-041 — RUST-DYN-2 Historical Reconciliation and Semantic Re-Anchoring v0.1

## Status

**ACCEPTED — HISTORICAL RECONCILIATION / DR-040 SUPERSEDED IN SCOPE / REAL-DATA EXECUTION NOT AUTHORIZED**

Date: 2026-09-08

## Purpose

Apply the mandatory Historical Reconstruction Before New Work Rule to RUST-DYN-2 and determine whether the Reach definition problem identified in DR-040 is genuinely unresolved or had already been solved and accepted in the historical EXT-1.1 Rust work.

## Historical reconstruction

The following historical line is recovered as canonical prior work:

1. `TGCV_RUST_POTENTIAL_REACH_SUCCESSOR_SEMANTICS_GATE_v0.1` — PASS; froze configuration-level potential successor semantics.
2. `TGCV_RUST_POTENTIAL_REACH_SEMANTIC_MEMBERSHIP_GATE_v0.1` — PASS; froze depth-1 potential Reach membership semantics.
3. `TGCV_RUST_POTENTIAL_REACH_STRUCTURAL_v0.2` result review — CONDITIONAL PASS; accepted structural reconstruction while explicitly qualifying it as a validation shadow rather than reachability evidence.
4. `TGCV_RUST_REACH_NON_REDUNDANCY_DELTA_REACH_DISTINCTION_GATE_v0.1` — PASS; froze the non-redundancy test contract.
5. `AUDIT_REACH_Non_Redundancy_v0.1` — PASS; produced structural evidence under the frozen depth-1 configuration-successor representation.
6. `DR-018-reach-non-redundancy-ext-1.1-rust.md` — ACCEPTED; formally accepted Reach informational non-redundancy relative to tested `T_acc`.

## Accepted historical semantic object

The historical Reach object is not an independently observed runtime graph. It is a **potential Reach** object generated from configuration-level potential successors under frozen structural semantics.

The successor is a complete canonical configuration resulting from a single admissible transformation under the frozen potential-successor contract. It is therefore analytically downstream from the transformation space while remaining distinct from transformation identity.

This semantic object was deliberately designed to avoid Cargo execution, observed resolver outcomes, outcome/value information, later activity, and predictive information.

## Historical empirical evidence

The accepted Reach non-redundancy audit reported:

- 516,061 paired focal version transitions;
- `T_acc` additions: 2,490,426;
- additions with redundant successor: 0;
- additions with non-redundant successor: 2,490,426;
- 69,890 pairs with equal local `T_acc` cardinality but different Reach structure;
- no execution, outcome, value, future activity, or trajectory computation.

DR-018 accepted this as **structural/informational non-redundancy**, not as ontological primitivity.

## Reconciliation with DR-038 / DR-040

DR-038 and DR-040 introduced a stronger requirement: Reach and Trajectory were required to be constructed through an independently constructed structural successor graph, with Reach prohibited from being a projection of `T_acc`.

Historical reconstruction establishes that this requirement is **not part of the previously frozen Rust Potential Reach semantics** and is not necessary to preserve the already accepted informational non-redundancy result.

Therefore:

- DR-040 remains historically valid as a record of the blocker it identified under the then-current RUST-DYN-2 design.
- DR-040 is **superseded in scope** by this reconciliation decision for the purpose of defining the Rust Reach object used by RUST-DYN-2.
- The independent-successor-graph requirement must not be implemented merely to satisfy DR-040.
- No historical semantic gate or accepted Reach result is invalidated.
- No historical artifact is rewritten to conceal the divergence.

## Re-anchored RUST-DYN-2 semantics

RUST-DYN-2 shall use the already frozen Rust Potential Reach semantics:

`T_acc,t = {tau in U_tau | P_tau(S_t,C_t,L)=1}`

`Reach^1_pot,t = {C' | C' is a canonical depth-1 potential successor generated under the frozen successor semantics from an admissible transformation at t}`

The following distinctions remain mandatory:

- transformation identity is not successor-configuration identity;
- Reach is not reduced to scalar cardinality;
- Reach membership is compared by canonical configuration identity;
- Reach is not an observed execution result;
- Reach construction must not use outcome/value/future activity/predictive information;
- the historical potential-successor contract is reused rather than recreated.

## What is genuinely new in RUST-DYN-2

The unresolved scientific question is no longer the definition of Reach itself.

The genuinely new question is the **dynamic relation** between the already defined objects:

`Delta T_acc(t,t+1)`

and

`Delta Reach^1_pot(t,t+1)`

with trajectory structure as a subsequent distinct dimension.

The dynamic operation must determine whether temporal changes in the already accepted potential Reach object exhibit non-degenerate relations to changes in `T_acc`, using the frozen temporal population and without importing the historical result as new evidence.

## Reuse requirements

RUST-DYN-2 must reuse, where compatible:

- historical Potential Reach successor semantics;
- historical semantic membership contract;
- historical configuration-level successor identity;
- historical non-redundancy distinctions NR-1 through NR-4;
- frozen D-OPS-1 transformation identity;
- DR-035 adjacent temporal-pair rule;
- current firewall and deterministic execution requirements.

A new implementation is justified only to operationalize the genuinely new temporal comparison and trajectory dimension, not to redefine Reach.

## Remaining open questions

1. Verify exact compatibility between the historical temporal population and current DR-035, including timestamp-tie handling.
2. Define the dynamic `Delta Reach^1_pot` comparison using the historical canonical successor-configuration representation.
3. Determine which historical NR cases can be reused as methodological precedents and which must be regenerated under the current frozen temporal contract.
4. Define Trajectory as a genuinely additional ordered object; historical Reach work did not compute Trajectory.
5. Establish whether H=1 is sufficient for the dynamic question. Any H>1 extension requires a separate controlled gate.

## Scientific boundary

This reconciliation does not create new empirical evidence.

It does not establish causality, predictive superiority, universal validity, positive value, originality, or ontological primitivity of Reach or Trajectory.

The accepted EXT-1.1 Reach result remains bounded structural/informational evidence. The closed RUST-DYN-EXEC-1 result remains separate and is not imported as evidence for RUST-DYN-2.

## Execution status

**REAL-DATASET EXECUTION AUTHORIZED: NO.**

No executor modification, real-data execution, replay, or H>1 expansion is authorized by this Decision Record.

## Decision

**DR-041 = ACCEPTED — HISTORICAL RECONCILIATION COMPLETE; RUST-DYN-2 RE-ANCHORED TO FROZEN POTENTIAL REACH SEMANTICS.**

The prior Reach-definition work is reused. The independent-successor-graph construction proposed by DR-040 is not pursued. The next controlled operation is a minimal design amendment/gate for the dynamic `Delta Reach^1_pot` comparison and the genuinely new trajectory dimension, followed by implementation only after explicit review.
