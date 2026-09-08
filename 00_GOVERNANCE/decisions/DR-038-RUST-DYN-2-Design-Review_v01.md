# DR-038 — RUST-DYN-2 Design Review v0.1

## Status

**ACCEPTED — DESIGN FREEZE / EXECUTION NOT YET AUTHORIZED**

Date: 2026-09-08

## Reviewed artifact

`03_EXPERIMENTS/EXT-1.1_Rust/RUST-DYN-2_REACH_TRAJECTORY_SUFFICIENCY_DESIGN_v0.1.md`

Design artifact SHA-1: `08a6f2dd8629c10426b36a1121a2d45a32c648e8`

## Review decision

The RUST-DYN-2 design is accepted as a controlled experimental design subject to the execution boundaries below.

The design correctly separates:

- accessible transformation space (`T_acc`);
- change in accessible transformation space (`ΔT_acc`);
- bounded Reach;
- ordered Trajectory;
- execution/outcome/value.

The design also pre-registers non-degenerate witness classes rather than selecting cases retrospectively.

## Frozen hypotheses

**H2-R1 — Downstream distinction:** `ΔT_acc` and `ΔReach` are not universally identical under the frozen structural representation.

**H2-R2 — Trajectory distinction:** Trajectory contains order/path information not losslessly represented by Reach as a set.

**H2-R3 — Counterfactual preservation:** `T_acc` can differ while observed immediate successor structure remains equal, preserving accessible alternatives not represented by the observed successor alone.

These are structural hypotheses. They are not causal hypotheses.

## Frozen witness classes

- ND-1: `ΔT_acc ≠ 0`, `ΔReach = 0`.
- ND-2: `ΔT_acc ≠ 0`, `ΔReach ≠ 0`.
- ND-3: `ΔReach ≠ 0` without a one-to-one identity with `ΔT_acc`.
- ND-4: equal Reach cardinality but different Reach membership.
- ND-5: equal Reach but different Trajectory sequence.

## Frozen methodological constraints

1. T_acc, Reach and Trajectory must be constructed independently.
2. Reach must not be defined as a projection of T_acc.
3. Trajectory must not be defined as an ordering of T_acc.
4. No downstream object may feed back into `Pτ`.
5. Set comparisons must use membership identity, not cardinality alone.
6. No outcome/value/predictive information may enter accessibility classification.
7. No retrospective pair selection.
8. No sampling unless separately authorized.
9. No arbitrary timestamp ordering.
10. Deterministic traversal and canonical serialization are mandatory.

## Horizon rule

The first implementation target is the already frozen **H=1** representation.

If H=1 cannot discriminate the pre-registered cases, that result is recorded as an operational limitation, not as evidence of theoretical redundancy. Any H>1 extension requires a separate design amendment and governance authorization.

## Population rule

The primary population remains the DR-035 adjacent temporal pair population. No new population may be substituted without a governance amendment.

## Required execution evidence

Before authorization, the executor must pass synthetic conformance equivalent to the frozen design and a local preflight must record:

- dataset SHA-256;
- executor SHA;
- resolver SHA;
- temporal rule;
- horizon;
- population construction;
- firewall status;
- no-sampling status;
- no-outcome/predictive access;
- deterministic output contract.

After authorization, one primary execution and one mandatory deterministic replay are required.

## Scientific boundary

A PASS can establish only bounded structural evidence that the representations retain distinct information in the tested population.

It cannot establish causality, causal sufficiency, predictive superiority, universal validity, positive value, or originality.

## Authorization boundary

**REAL-DATASET EXECUTION AUTHORIZED: NO.**

This decision freezes the design but does not authorize execution.

The next controlled operation is:

**RUST-DYN-2-EXEC-1A — Synthetic Conformance + Real-Data Preflight + Execution Authorization Gate.**

## Decision

**DR-038 = ACCEPTED — RUST-DYN-2 DESIGN FROZEN.**
