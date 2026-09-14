# TGCV C09 — KGFS / D178F70 Source Inconsistency Audit 001

**Date:** 2026-09-14  
**Status:** `BLOCKED — SOURCE/CATALOGUE SIZE INCONSISTENCY`  
**Scientific status:** `NO C09 UPGRADE`

## 1. Purpose

Record the reproducible technical inconsistency encountered while completing the exact public-file reproducibility audit for Yale ISPS dataset D178 (*Rural Banks Can Reduce Poverty: Experimental Evidence from 870 Indian Villages*).

This record does **not** alter the C09 protocol, the KGFS D5-A closure record, the trajectory bridge, the Evidence→Claim Matrix, the RMA, or TGCV Core.

## 2. Canonical catalogue assertion

The official Yale ISPS D178 archive lists **D178F70 — Data EL sec.20 — .dta — 5,661,173 bytes**. The archive page is the canonical published inventory used by the acquisition audit.

Source: Yale ISPS D178 household-data archive.

## 3. Observed serving-object assertion

The resumable acquisition repeatedly obtained **5,660,036 bytes** for D178F70. The strict HTTP Range audit subsequently requested bytes `0-262143` and the server returned:

`Content-Range: bytes 0-262143/5660036`

The server therefore identifies the currently served object as having total length **5,660,036 bytes**.

Difference from the Yale catalogue size:

`5,661,173 - 5,660,036 = 1,137 bytes`

The same discrepancy is observed across the full-download and Range paths; it is therefore not explained by the local downloader's chunk assembly.

## 4. Interpretation

The evidence establishes a **source/catalogue inconsistency**, not a scientific failure of KGFS and not evidence against the TGCV representation.

The audit must not:

- pad or fabricate the missing 1,137 bytes;
- silently replace the published Yale size with the smaller served size;
- treat the truncated object as an exact reproduction of D178F70;
- upgrade technical reproducibility to PASS while the discrepancy remains unresolved.

The 73 other D178 DTA files have passed the published-size verification and remain reusable. D178F70 remains the sole blocked file.

## 5. Reproducibility boundary

Current technical status:

- D178 inventory: `74 DTA files`
- Verified: `73/74`
- Blocked: `D178F70`
- Published size: `5,661,173 bytes`
- Served-object size: `5,660,036 bytes`
- Unresolved discrepancy: `1,137 bytes`
- Exact variable-level reproducibility closure: `OPEN`
- C09 scientific claim: `NO UPGRADE`

## 6. Next authorized action

Do **not** continue changing the acquisition algorithm merely to accommodate the smaller object.

The next action is source reconciliation: determine whether Yale/Dataverse exposes an alternate canonical representation, revision, metadata record, or archival copy for D178F70 that reconciles the 1,137-byte discrepancy.

Only after reconciliation should D178F70 be admitted to the exact-file manifest and the canonical metadata/trajectory audit be allowed to close.

## 7. External source support

Yale's current D178 archive explicitly lists D178F70 as Data EL sec.20 with size 5,661,173 bytes and identifies the study as a randomized field experiment involving expansion of banking services. The Yale archive describes its role as providing curated replication materials for reproducibility.

The source therefore supports retaining the published size as the canonical expectation while the serving-object discrepancy remains unresolved.
