# RUST-DYN-EXEC-1 — Deterministic Replay Consistency Closure v0.1

## Status

**PASS — DETERMINISTIC REPLAY CONSISTENCY ESTABLISHED**

Date: 2026-09-08

## Compared artifacts

Primary:
`03_EXPERIMENTS/EXT-1.1_Rust/execution/RUST_DYN_EXEC_1_PRIMARY.json`

Replay:
`03_EXPERIMENTS/EXT-1.1_Rust/execution/RUST_DYN_EXEC_1_REPLAY.json`

## Byte-level result

Primary SHA-256:
`B1E87A1B20C9198D95895904F9E845DD01596CEAA8F4906850F34B4C3ABC18C9`

Replay SHA-256:
`B1E87A1B20C9198D95895904F9E845DD01596CEAA8F4906850F34B4C3ABC18C9`

**Hashes are identical.**

Therefore the replay JSON is byte-identical to the primary JSON.

## Execution consistency

Both executions report:

- MODE = `REAL_DATASET_EXECUTION`
- REAL_DATASET_EXECUTION = `true`
- EXECUTION_AUTHORIZATION = `true`
- HORIZON = `1`
- dataset SHA-256 = `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- temporal rule = `DR-035-v0.1-ADJACENT-CREATED-AT`
- temporal pair count = `516061`
- pass = `true`

Classification counts are identical:

- PERSISTENCE: 77,858
- EXPANSION: 8,295
- CONTRACTION: 3,786
- RECONFIGURATION: 426,122

## Gate conclusion

**REPLAY CONSISTENCY = PASS.**

The corrected RUST-DYN-EXEC-1 primary execution has been reproduced deterministically at the complete JSON artifact level.

The earlier three-field execution remains excluded from scientific evidence and is not part of this closure.

## Scientific boundary

This gate establishes execution reproducibility only. It does not establish causality, predictive superiority, universal validity, positive value, or originality. Scientific integration must use the frozen four-field transformation identity and the bounded H=1 Reach/Trajectory representation.

## Next controlled operation

**RUST-DYN-EXEC-1 Scientific Integration / Result Closure.**

The next step is to integrate the reproducible structural result into the experiment's scientific record, explicitly preserving the stated limitations and the distinction between observed ΔT_acc classifications and downstream Reach/Trajectory representations.
