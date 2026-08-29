# EXT-1.1 — Historical dependency source gate v0.1

**Date:** 2026-08-29
**Status:** PASS for historical-source availability; target cutoff revised pending exact 2022-09-07 state

## Finding

The official Rust crates.io index archive exists and preserves historical snapshot branches. The archive contains `snapshot-2022-08-31`, whose commit is `31a1d8c9b1f6851c9b248813b5bb883ba5297883`.

The snapshot exposes the normal crates.io index JSON records, including version identifiers and dependency requirements. Example verification: the `serde` index record is directly retrievable from the 2022-08-31 snapshot and contains `vers`, `deps`, dependency `req`, optional/default-feature flags, checksum, yanked state, and related metadata.

The official archive does not contain a 2022-09-07 snapshot; the next archived snapshot is 2022-12-19. Therefore an exact 2022-09-07 historical index state has not yet been demonstrated through the official archive.

## Methodological consequence

We must not silently combine the 2022-08-31 dependency state with a 2022-09-07 label and call it the 2022-09-07 state.

Two valid options remain:

1. recover an exact 2022-09-07 index commit/state from an independent verifiable Git history source; or
2. formally redefine the experimental cutoff to **2022-08-31**, and use download observations from that date onward under an explicitly specified observation window.

Option 2 is preferable to uncontrolled reconstruction if exact 2022-09-07 recovery cannot be demonstrated, because it gives us a fully auditable historical state.

## Current gate result

`HISTORICAL_DEPENDENCY_SOURCE = PASS`
`EXACT_2022-09-07_STATE = NOT_YET_PROVEN`
`2022-08-31_STATE = VERIFIED`
`DOWNLOAD_ARCHIVE = VERIFIED`
`FREEZE = BLOCKED`

## User action

**No download is required yet.** Do not download the large crates.io index or any database dump. We will only request a file once the minimum acquisition set is fixed and the exact filenames/URLs are known.
