# EXT-1.1 Rust — R7 Download Archive Bridge Audit v0.1

Date: 2026-09-06
Status: CLOSURE READY — C1 archive set verified locally; controlled repository retention pending
Scientific execution: NOT PERFORMED

## Purpose
Audit CHR-MICRO-3 R7: whether each historically reconstructed `package@version` can be linked reproducibly to the corresponding crate archive, using the historical index checksum as the identity bridge and without current-state or outcome leakage.

## C1 local archive verification
The six C1 crate archives were located in the historical reconstruction environment and their complete SHA-256 values were independently computed locally:

- `proc-macro2-0.4.19.crate` → `FFE022FB8C8BD254524B0B3305906C1921FA37A84A644E29079A9E62200C3901`
- `quote-0.6.8.crate` → `DD636425967C33AF890042C483632D33FA7A18F19AD1D7EA72E8998C6EF8DEA5`
- `serde-1.0.0.crate` → `369633CFE0F0BDE1DFC037FB6C5A329D46586A31F981BED14D87487A3439AE37`
- `serde_derive-1.0.79.crate` → `31569D901045AFBFF7A9479F793177FE9259819AFF10AB4F89EF69BBC5F567FE`
- `syn-0.15.6.crate` → `854B08A640FC8F54728FB95321E3EC485B365A97FE47609797C671ADDD1DDE69`
- `unicode-xid-0.1.0.crate` → `FC72304796D0818E357EAD4E000D19C9C174AB23DC11093AC919054D20A6A7FC`

These values match the independently established historical archive checksums for the C1 reconstructed graph.

## C2 and C3 repository evidence
C2 retains `tokio-1.0.0.crate` with SHA-256 `9F4BFDCBD00FA893AC0549B38AA27080636A0104B0D0C38475A99439405E1DF8` in `SHA256SUMS.txt`. C3 retains `rand-0.8.0.crate` with SHA-256 `A76330FB486679B4ACE3670F117BBC9E16204005C4BDE9C4BD372F45BED34F12`. fileciteturn24file0L2-L2

## R7 verdict

**R7 = CLOSURE READY.**

The historical package/version → archive bridge is now demonstrated for C1–C3, and the previously identified C1 retention gap is reduced to a controlled repository-retention action: the six verified C1 binaries must be added explicitly to the continuity repository, with no broad staging of the local environment.

This is a provenance/retention closure step, not scientific execution.

## Controlled closure action
The intended repository paths are:

`03_EXPERIMENTS/EXT-1.1_Rust/execution/C1/archives/`

Only these six files should be staged from the local historical reconstruction environment. No other files under `execution/environment/` should be staged by this action.

## Boundary conditions
No frozen N-R8-C2 corpus was read or modified. No empirical Rust dataset was consumed. No scientific execution was performed. No outcome information was used.

## Gate status
- R6: PASS for current confirmatory cases
- R7: CLOSURE READY — pending controlled binary retention
- R8: OPEN
- R9: OPEN / methodological rule fixed
- R10: OPEN
- CHR-MICRO-3: OPEN / NOT CLOSED
