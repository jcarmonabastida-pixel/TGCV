# RUST-DYN-2 — Scientific Integration Closure v0.1

**Status:** CLOSED — BOUNDED STRUCTURAL EMPIRICAL PASS
**Date:** 2026-09-08
**Scope:** EXT-1.1 Rust / RUST-DYN-2 / EXEC-1A
**Authorization:** DR-043

## 1. Execution closure basis

The authorized primary and mandatory replay were completed with the same reported dataset, R*, temporal rule, horizon and result fields. Replay consistency is recorded in `RUST-DYN-2_EXEC-1A_REPLAY_CONSISTENCY_CLOSURE_v01.md`.

The received primary and replay structured outputs are field-identical. No byte-level file comparison is claimed because independent raw JSON result files were not supplied as artifacts in this coordination step.

## 2. Frozen population and integrity

- Dataset SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- R* Git blob SHA: `669d4f01131af518f32b1b4b3da27f676ae4ae55`
- Temporal rule: `DR-035-v0.1-ADJACENT-CREATED-AT`
- H=1
- Eligible origins: `607498`
- Timestamp-tie exclusions: `0`
- Temporal pairs: `516061`
- Zero-pair packages: `30713`
- Pair evidence SHA-256: `fdab99039990d0e0a5ab221e6b98e857349048e8a26bf3f6a7ffe6fcd179bad8`

## 3. Empirical structural findings

Across 516,061 adjacent temporal package-version pairs:

- PERSISTENCE: `77858`
- EXPANSION: `8295`
- CONTRACTION: `3786`
- RECONFIGURATION: `426122`
- Non-persistence: `438203` pairs (`84.91%` approximately)

For the downstream distinction between accessible transformation-space change and potential one-step Reach:

- ND-1 — `ΔT_acc ≠ 0` and `ΔReach = 0`: `159921` pairs.
- ND-2 — `ΔT_acc ≠ 0` and `ΔReach ≠ 0`: `278282` pairs.
- ND-4 — equal Reach cardinality but different Reach membership: `266201` pairs.

ND-1 + ND-2 = `438203`, matching the complete non-persistence population reported by the executor.

## 4. Scientific interpretation

The result supports, **within the frozen Rust operationalization and H=1**, the following bounded empirical statements:

1. Changes in the analytically constructed accessible transformation set (`ΔT_acc`) occur frequently in the observed adjacent temporal population.
2. `ΔT_acc` and `ΔReach¹_pot` are empirically distinguishable: there are many pairs with `ΔT_acc ≠ 0` but `ΔReach = 0` (ND-1), and many with both changing (ND-2).
3. Reach cardinality alone is insufficient to characterize Reach identity: ND-4 provides pairs with equal Reach cardinality but different canonical Reach membership.
4. The distinction is reproducible at the structured-result level across the mandatory primary/replay pair.

## 5. What is NOT established

This experiment does not establish:

- causality from mechanism to `ΔT_acc` or `ΔReach`;
- predictive superiority;
- universal validity across domains;
- positive value or outcome implications;
- empirical proof that TGCV is original;
- superiority over existing reachability, adaptation, capability, opportunity or transformation-space theories;
- H>1 trajectory sufficiency;
- observed execution reachability in Cargo/runtime;
- downstream outcomes or adoption/success.

`Reach¹_pot` remains a bounded potential structural successor construct, not observed runtime reachability.

## 6. Hypothesis status

- H-R1: supported in the frozen Rust operationalization: substantial non-persistence and explicit structural change in `T_acc` are observed.
- H-R2: supported in the bounded sense of distinguishability between `ΔT_acc` and `ΔReach¹_pot` through ND-1/ND-2.
- H-R3/H-R4: remain open where they require stronger dynamic/trajectory or cross-domain evidence.
- Causal, predictive, value and originality claims remain open.

## 7. Firewall closure

The primary/replay outputs report all forbidden-access flags as false: no sampling, outcome read, future activity, predictive metrics, Cargo execution, runtime outcomes, lockfile read or value read.

## 8. Final decision

**RUST-DYN-2 / EXEC-1A is scientifically CLOSED as a bounded structural empirical test.**

The experiment provides evidence for the analytical distinction between `ΔT_acc` and bounded potential one-step Reach in the frozen Rust representation. It does not elevate Reach to an ontological primitive and does not alter the stabilized TGCV Core architecture (`Core_ontological = S`).

## 9. Next controlled operation

No rerun of RUST-DYN-2 is required. The next work should be a historical-state reconstruction and gate definition for the remaining open TGCV claims, rather than an exploratory extension of this execution.
