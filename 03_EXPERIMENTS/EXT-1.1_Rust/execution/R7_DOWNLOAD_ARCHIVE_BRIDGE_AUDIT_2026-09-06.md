# EXT-1.1 Rust — R7 Download Archive Bridge Audit v0.1

Date: 2026-09-06
Status: PARTIAL PASS — bridge demonstrated, archive retention incomplete for C1
Scientific execution: NOT PERFORMED

## Purpose
Audit CHR-MICRO-3 R7: whether each historically reconstructed `package@version` can be linked reproducibly to the corresponding crate archive, using the historical index checksum as the identity bridge and without current-state or outcome leakage.

## Evidence reviewed
- C1 historical resolution evidence
- C2 historical resolution evidence
- C3 Cargo resolution/check evidence
- `SHA256SUMS.txt`
- `VERSION_IDS.md`

## Case assessment

### C1 — serde 1.0.0
PASS at acquisition/verification level. C1 evidence states that the selected crate archives were independently downloaded and verified against historical index checksums, including `serde 1.0.0` checksum `369633cfe0f0bde1dfc037fb6c5a329d46586a31f981bed14d87487a3439ae37` and the complete resolved dependency archive set.

However, the GitHub evidence tree currently retains the C1 resolution logs/lock/configuration and checksum manifest but does not retain the binary `.crate` archives themselves. Therefore the bridge is evidenced, but archival retention in the continuity repository is incomplete.

### C2 — tokio 1.0.0
PASS for the demonstrated target archive. The historical resolution evidence records the exact historical checksum `9f4bfdcbd00fa893ac0549b38aa27080636a0104b0d0c38475a99439405e1df8`, and `SHA256SUMS.txt` records the same checksum for `C2/tokio-1.0.0.crate`. The C2 historical evidence also states that the archive was independently verified against historical index metadata. fileciteturn23file0L2-L2

### C3 — rand 0.8.0
PASS for the demonstrated target archive. GitHub retains `C3/rand-0.8.0.crate`; `SHA256SUMS.txt` records SHA-256 `A76330FB486679B4ACE3670F117BBC9E16204005C4BDE9C4BD372F45BED34F12`, which is also the checksum associated with `rand 0.8.0` in the version-ID bridge. The C3 resolution evidence records Cargo selecting `rand 0.8.0` while `0.8.3` was available, consistent with the exact requirement. fileciteturn18file0L2-L10

## R7 verdict

**R7 = PARTIAL PASS.**

The download-archive identity bridge is demonstrated for C1–C3, but the continuity repository does not currently retain the C1 binary crate archives. Consequently R7 should not yet be promoted to a full PASS for the reconstruction package.

This is a provenance/retention gap, not evidence that C1 acquisition failed.

## Required closure action
Before declaring R7 globally PASS, retain or otherwise immutably reference the C1 verified `.crate` archive set in the reconstruction evidence package, with exact SHA-256 values tied to the historical index records. Do not reacquire from current registry semantics and do not substitute versions.

## Boundary conditions
No frozen N-R8-C2 corpus was read or modified. No empirical Rust dataset was consumed. No scientific execution was performed. No outcome information was used.

## Gate status after audit
- R6: PASS for current confirmatory cases
- R7: PARTIAL PASS — C1 archive retention gap
- R8: OPEN
- R9: OPEN / methodological rule fixed
- R10: OPEN
- CHR-MICRO-3: OPEN / NOT CLOSED
