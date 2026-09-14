# TGCV C09 — KGFS / D178F70 Source Inconsistency Audit 001

**Date:** 2026-09-14  
**Status:** `RECONCILED — DATAVERSE OBJECT VERIFIED; CATALOGUE SIZE DISCREPANCY RETAINED`  
**Scientific status:** `NO C09 UPGRADE`

## 1. Purpose

Record the reproducible technical reconciliation completed while finalizing the exact public-file reproducibility audit for Yale ISPS dataset D178 (*Rural Banks Can Reduce Poverty: Experimental Evidence from 870 Indian Villages*).

This record does **not** alter the C09 protocol, the KGFS D5-A closure record, the trajectory bridge, the Evidence→Claim Matrix, the RMA, or TGCV Core.

## 2. Initial catalogue assertion

The official Yale ISPS D178 archive lists **D178F70 — Data EL sec.20 — .dta — 5,661,173 bytes**.

This remains the historical/published catalogue assertion used by the original acquisition inventory.

## 3. Dataverse canonical file record

The D178F70 HDL resolves to Dataverse file ID **28730**.

The current Dataverse API record for file 28730 reports:

- `datasetVersionId`: **928**
- `version`: **1**
- `filename`: `EL_section20_health.tab`
- `originalFileName`: `EL_section20_health.dta`
- `originalFileFormat`: `application/x-stata-14`
- `originalFileSize`: **5,660,036 bytes**
- `md5`: **42b62693db82e8725ef0f40021e0b84e**
- `storageIdentifier`: `s3://yul-dv-prd:19b98919255-c46adf67a928`
- `lastUpdateTime`: `2026-04-08T21:01:02Z`

## 4. Independent object verification

A fresh direct acquisition was performed from the canonical Dataverse endpoint:

`https://dataverse.yale.edu/api/access/datafile/28730?format=original`

The resulting local object was independently checked:

- Size: **5,660,036 bytes**
- MD5: **42b62693db82e8725ef0f40021e0b84e**

The local object therefore matches the **Dataverse-declared original size and MD5 exactly**.

## 5. Reconciliation conclusion

The 1,137-byte discrepancy is now resolved as a **catalogue-versus-current-Dataverse-record discrepancy**, not a transport/download truncation.

`5,661,173 - 5,660,036 = 1,137 bytes`

The serving object is internally consistent with the current Dataverse metadata and checksum. There is no evidence that the current Dataverse object is locally truncated or corrupted.

The historical Yale catalogue value **5,661,173 bytes is retained and not overwritten**; the current Dataverse record establishes the reproducible canonical object currently available for `fileId=28730`.

## 6. Reproducibility boundary

Technical status after reconciliation:

- D178 inventory: `74 DTA files`
- Verified against current canonical object/metadata: **74/74**
- D178F70: **RECONCILED / VERIFIED**
- Current Dataverse original size: **5,660,036 bytes**
- Current Dataverse MD5: `42b62693db82e8725ef0f40021e0b84e`
- Historical catalogue size: **5,661,173 bytes**
- Retained catalogue discrepancy: **1,137 bytes**
- Exact variable-level reproducibility closure: `READY TO CLOSE SUBJECT TO FINAL MANIFEST/VARIABLE AUDIT UPDATE`
- C09 scientific claim: `NO UPGRADE`

## 7. Governance boundary

The acquisition algorithm must **not** be changed merely to force the historical 5,661,173-byte catalogue value.

The exact-file manifest should distinguish:

1. historical published catalogue expectation (`5,661,173`); and
2. current Dataverse canonical original object (`5,660,036`, MD5 `42b626...`).

No bytes are to be fabricated, padded, discarded, or silently substituted.

## 8. Next authorized action

Update the KGFS acquisition/reproducibility manifest so that D178F70 records both the historical catalogue assertion and the reconciled current Dataverse metadata/object identity. Then rerun the exact variable-level audit against the reconciled 74-file inventory.

Only the technical reproducibility status changes here. This record does not by itself upgrade C09, the Evidence→Claim Matrix, RMA, or TGCV Core.
