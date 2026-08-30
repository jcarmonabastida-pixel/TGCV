# EXT-1.1 Rust — CHR-MICRO-3 Amendment v0.2

**Date:** 2026-08-30
**Status:** APPROVED FOR EXECUTION
**Predecessor:** CHR-MICRO-3_GATE_v0.1
**Trigger:** HIAR partial pass; historical crates.io index snapshots recovered.

## Purpose

Replace the previously blocked release-time reconstruction with an explicitly snapshot-aligned observation protocol. This is a temporal redesign of the test window, not a retrospective claim that a later snapshot was the registry state at the original release timestamp.

## Temporal unit

For each case, the observation state is defined as a dated archived index snapshot `S_k`. All candidate-universe and dependency-resolution inputs must come exclusively from `S_k`.

`O_k := Snapshot(k)`

No current index state, later snapshot, downloads, adoption, popularity, survival, or outcome variable may enter resolution.

## Cases and snapshots

| Case | Target release | Observation snapshot | Rule |
|---|---|---|---|
| C1 | serde@1.0.0 | snapshot-2018-09-26 | target must exist by snapshot; candidate universe from snapshot only |
| C2 | tokio@1.0.0 | snapshot-2021-05-05 | target must exist by snapshot; candidate universe from snapshot only |
| C3 | rand@0.8.0 | snapshot-2021-05-05 | target must exist by snapshot; candidate universe from snapshot only |

## Interpretation constraint

The amended test does **not** establish resolver behavior at the exact original release timestamp. It establishes whether a reproducible historical registry state can support temporal resolution at a declared snapshot cutoff.

If exact release-time resolution is required later, a separate exact-date archival reconstruction will remain necessary.

## HRSV execution requirements

For each case:

1. Recover the crate record from the declared snapshot.
2. Identify the dependency constraints of the target release.
3. Recover each dependency's record from the same snapshot.
4. Enumerate candidate releases available in that snapshot.
5. Apply the declared Cargo/SemVer resolver rule.
6. Record the resulting `package@version` identities.
7. Establish the `package@version → version_id` bridge independently of outcome data.

## Verdict rule

PASS only if A-D of HRSV can be demonstrated for all three cases using the snapshot-only state.

A later publication or current metadata may be used only as an identity cross-check and must never determine the historical candidate universe or resolution.

**FREEZE remains BLOCKED until the amended HRSV/CHR execution passes.**
