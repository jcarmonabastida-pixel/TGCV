# C2 Historical Resolution Diagnostic — 2026-09-05

## Scope
- Target release: `tokio 1.0.0`
- Historical snapshot: `2021-05-05`
- Snapshot commit: `a5dcd8438da2d8f99e3661a1956afbfb8f026fa0`
- Historical toolchain: Rust/Cargo `1.51.0`
- Dependency requirement tested: `tokio = "=1.0.0"`
- Resolution source: local historical registry only

## Integrity prerequisites
- `tokio-1.0.0.crate` SHA-256: `9f4bfdcbd00fa893ac0549b38aa27080636a0104b0d0c38475a99439405e1df8`
- `pin-project-lite-0.2.5.crate` SHA-256: `0cf491442e4b033ed1c722cb9f0df5fcfcf4de682466c46469c36bc47dc5548a`
- `pin-project-lite-0.2.6.crate` SHA-256: `dc0e1f259c92177c30a4c9d177246edd0a3568b25756a977d0632cf8fa37e905`

## Diagnostic execution
Cargo 1.51.0 was run against the local registry with the exact requirement `=1.0.0`.

Observed result: resolution failed because `tokio 1.0.0` is marked `yanked=true` in the historical snapshot. Cargo reported available non-matching candidates including `1.5.0`, `1.4.0`, `1.3.0`, etc.

## Interpretation
This is not evidence of a corrupted snapshot, archive mismatch, or incorrect local-registry construction. It demonstrates a boundary between historical release existence/metadata and fresh dependency selection by Cargo.

Therefore:
- C2 R1 — release identity: OPEN / prior evidence available
- C2 R2 — historical registry state: PASS for the observed target record
- C2 R3 — dependency metadata: PASS for the observed target record
- C2 R4 — candidate-universe reconstruction: PASS for demonstrated target/dependency records; fresh selection of the yanked target is not expected
- C2 R5 — deterministic resolution of the exact yanked target: BLOCKED BY YANKED TARGET, not passed and not substituted
- C2 R6 — version_id bridge: OPEN pending independent protocol closure
- C2 R7 — archive bridge: PASS for the three verified archives
- C2 R8 — temporal censoring: OPEN
- C2 R9 — no outcome leakage: PASS by protocol
- C2 R10 — T_acc operationalisation: OPEN

## Methodological boundary
Do not replace `tokio 1.0.0` with `1.0.1` and label that as exact C2 resolution. Any alternative confirmatory resolution must receive distinct scope and provenance. A lockfile manually seeded with a yanked release would not constitute fresh resolver selection evidence unless the protocol explicitly defines that procedure.

## Current status
`CHR-MICRO-3 RECONSTRUCTION GATE = BLOCKED / NOT EXECUTED`
`EXT-1.1 SCIENTIFIC EXECUTION = NOT PERFORMED`
