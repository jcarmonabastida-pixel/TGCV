# RUST-DYN-EXEC-1 — Primary Execution Audit Closure v0.1

## Status

**PASS — PRIMARY EXECUTION AUDIT CLOSED**

Date: 2026-09-08

## Primary result audited

Input: `03_EXPERIMENTS/EXT-1.1_Rust/execution/RUST_DYN_EXEC_1_PRIMARY.json`

Input SHA-256: `b1e87a1b20c9198d95895904f9e845dd01596ceaa8f4906850f34b4c3abc18c9`

Dataset SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Temporal rule: `DR-035-v0.1-ADJACENT-CREATED-AT`

Horizon: `1`

## Audit result

Primary execution audit: **PASS**.

All 15 audit assertions passed:

- mode
- pass flag
- dataset SHA-256
- temporal rule
- horizon
- pair count
- classification counts
- unique pairs
- directional pairs
- class semantics
- exact delta counts
- T_acc hashes present and structurally valid
- firewall
- Reach/Trajectory exclusion of origin
- deterministic trajectory ordering

Audited row count: **516,061**.

Classification counts:

- PERSISTENCE: 77,858
- EXPANSION: 8,295
- CONTRACTION: 3,786
- RECONFIGURATION: 426,122

The classification counts sum exactly to the audited temporal population of 516,061 pairs.

## Scientific interpretation boundary

The corrected primary run is now technically and structurally admissible for the next reproducibility gate. The result supports proceeding to deterministic replay of the same frozen execution.

This closure does **not** by itself establish causality, predictive superiority, universal validity, positive value, or originality. It also does not use the earlier invalid three-field execution as evidence.

## Next controlled operation

**RUST-DYN-EXEC-1 — Mandatory Deterministic Replay.**

Replay must use the same frozen dataset, corrected executor, temporal rule, horizon, and output semantics. Replay consistency must be established before scientific integration/closure.
