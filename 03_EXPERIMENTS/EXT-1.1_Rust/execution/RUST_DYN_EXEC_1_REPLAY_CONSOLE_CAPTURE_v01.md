# RUST-DYN-EXEC-1 — Replay Console Capture v0.1

## Status

**TECHNICAL REPLAY EXECUTION PASS — EXACT REPLAY CONSISTENCY PENDING HASH COMPARISON**

Date: 2026-09-08

## Replay result reported locally

Mode: `REAL_DATASET_EXECUTION`

Execution authorization: `true`

Real dataset execution: `true`

Horizon: `1`

Dataset SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Temporal pair count: `516061`

`pass`: `true`

Classification counts:

- PERSISTENCE: 77,858
- EXPANSION: 8,295
- CONTRACTION: 3,786
- RECONFIGURATION: 426,122

The replay console aggregates are identical to the audited primary execution.

## Reproducibility boundary

This console result establishes matching execution-level aggregates, but exact deterministic replay consistency is not yet formally closed because the replay JSON hash has not yet been compared with the primary JSON hash.

Required next check:

Compare SHA-256 of:

- `03_EXPERIMENTS/EXT-1.1_Rust/execution/RUST_DYN_EXEC_1_PRIMARY.json`
- `03_EXPERIMENTS/EXT-1.1_Rust/execution/RUST_DYN_EXEC_1_REPLAY.json`

If the hashes are identical, the replay can be closed as byte-identical deterministic reproduction. If not, the JSONs must be compared structurally before any scientific closure.

No new execution is authorized or required at this point.
