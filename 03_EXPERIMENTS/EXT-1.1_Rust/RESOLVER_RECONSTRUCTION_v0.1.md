# EXT-1.1 Rust — Minimal Snapshot-Only Resolver Reconstruction v0.1

**Date:** 2026-08-30
**Protocol:** CHR-MICRO-3_AMENDMENT_v0.2 / HRSV v0.2
**Status:** PARTIAL EXECUTION — RESOLUTION NOT YET PROVEN

## Objective

Materialize, for C1-C3, the candidate universe from the declared historical crates.io snapshot and demonstrate a deterministic Cargo/SemVer resolution without current-state or outcome leakage.

## Historical inputs confirmed

- C1: `serde@1.0.0` against `snapshot-2018-09-26`.
- C2: `tokio@1.0.0` against `snapshot-2021-05-05`.
- C3: `rand@0.8.0` against `snapshot-2021-05-05`.

The official index archive exposes the crate records as newline-delimited JSON containing version, dependency declarations, checksum, features and `yanked` state. These snapshot records are the authoritative input for the amended test.

## Resolver rule

Cargo uses SemVer-compatible requirements and attempts to unify compatible dependency versions; incompatible requirements may resolve to distinct versions. Default/caret requirements are defined by Cargo's compatibility rules. No current registry metadata or download/outcome information is allowed as a resolver input.

## Execution result

The historical target/dependency records can be inspected, and external documentation corroborates the target release dependency declarations. However, the available execution environment cannot currently materialize the complete archived snapshot index as a local registry and run an actual Cargo resolver against it. Therefore an executable full transitive resolution has **not** been demonstrated.

This is an execution-capability limitation, not evidence that the historical resolution is impossible. Consequently C remains **BLOCKED**, not PASS or FAIL.

## C1-C3 status

| Case | Snapshot state | Candidate universe | Resolver execution | Verdict |
|---|---|---|---|---|
| C1 serde@1.0.0 | PASS | PARTIAL | BLOCKED | PENDING |
| C2 tokio@1.0.0 | PASS | PARTIAL | BLOCKED | PENDING |
| C3 rand@0.8.0 | PASS | PARTIAL | BLOCKED | PENDING |

## Version-ID bridge

The crates.io API model defines `Version.id` as the opaque version identifier and the official daily download archive uses that identifier. The independent mapping for all three cases has not yet been demonstrated, so D remains BLOCKED.

## Conclusion

No PASS is declared. The historical-state route is validated, but the two decisive empirical operations remain:

1. materialize the snapshot-only candidate universe and run Cargo resolution reproducibly;
2. independently establish `package@version → version_id` for the resolved releases.

**EXT-1.1 FREEZE remains BLOCKED.**
