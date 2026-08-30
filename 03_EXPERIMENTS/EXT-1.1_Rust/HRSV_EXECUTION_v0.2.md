# EXT-1.1 Rust — HRSV Execution v0.2

**Date:** 2026-08-30
**Protocol:** CHR-MICRO-3_AMENDMENT_v0.2
**Status:** EXECUTED — PARTIAL PASS / C-D BLOCKED

## Evidence reviewed

The official crates.io index archive exposes dated historical snapshot branches. The following crate records were retrieved directly from the archived snapshots:

- `serde` from `snapshot-2018-09-26`.
- `tokio` from `snapshot-2021-05-05`.
- `rand` from `snapshot-2021-05-05`.

The records are newline-delimited historical index entries containing version, dependency declarations, checksum, features and `yanked` state.

## Gate assessment

| Gate | Result | Reason |
|---|---|---|
| A Historical registry state | PASS | Dated archive snapshots are directly recoverable. |
| B Candidate-universe reconstruction | PARTIAL | Target crate records and dependency declarations are recoverable, but the full transitive candidate universe has not yet been reconstructed for all cases. |
| C Deterministic historical resolution | BLOCKED | No executable Cargo resolver run has yet been performed against reconstructed snapshot-only candidate universes; declaring a resolution from the visible records alone would be inferential. |
| D Version-ID bridge | BLOCKED | The `package@version → version_id` identity join has not yet been independently demonstrated for all three cases. |

## Important correction

The archive evidence repairs the HRSV-A failure from v0.1, but it does not by itself establish HRSV PASS. In particular, the existence of a snapshot and visibility of target/dependency records are insufficient to claim exact historical resolver output.

## Verdict

**HRSV v0.2 = PARTIAL PASS / BLOCKED.**

The historical-state acquisition route is validated. The resolver and version-ID bridge remain empirical subtests.

## Next authorized step

Execute the minimal snapshot-only resolver reconstruction for C1-C3, with the candidate universe materialized from the declared snapshot and the resolver run recorded reproducibly. Then perform the independent version-ID bridge check.

**EXT-1.1 FREEZE remains BLOCKED.**
