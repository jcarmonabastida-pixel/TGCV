# EXT-UPD-1R — External Asset Structural Reconciliation v0.1

**Date:** 2026-09-08  
**Status:** CLOSED — STRUCTURAL RECONCILIATION + PHYSICAL REGULARISATION COMPLETE / CONTENT UPDATE NOT YET STARTED  
**Parent operation:** `00_GOVERNANCE/impact/IMPACT-EXT-ASSETS-UPDATE_v0.1.md`  
**Scope:** identity, location and semantic role of external-facing assets only.

## Closure update — EXT-UPD-1R.3

The agreed physical regularisation has now been executed on `main`.

Completed:

- `05_ASSETS/README.md` updated as the canonical external-asset map.
- `05_ASSETS/ARM/README.md` created for `TGCV-EXT-ARM-001`.
- `05_ASSETS/RII/README.md` created for `TGCV-EXT-RII-001`.
- `05_ASSETS/MOI/README.md` created as a reserved location only; no substantive MOI created.
- IE PhD adaptation normalised from `05_ASSETS/Research_Prospectus/IE/` to `05_ASSETS/Research_Prospectus/adaptations/IE_PhD/`.
- The original IE path was removed only after the new canonical path had been created; the document content was preserved.

Resulting structural rule:

> One external asset family = one canonical identity = one canonical location.

No scientific claim, evidence level, gate state or historical scientific artefact was changed by this maintenance operation.

## Git commits for the maintenance operation

- ARM reservation: `91d2a2f46af4635a66db5286d33f98dbf6f86814`
- RII reservation: `800ee276cf4e71a6b041a44975ab0a11e70d0b5d`
- MOI reservation: `ce9110845a4d5c5094e44b7f11bafc651f8e64df`
- IE adaptation normalisation: create `931e953ee8a6ec9595bccf2292decb7cd0b97c27`, followed by removal of obsolete path `80d8d12df35c85b75e8a72be28f831331ea7b3c6`
- canonical `05_ASSETS/README.md`: `673363a6ac7556250f22bba70a18347a3d396fdd`

These are maintenance commits only; they do not constitute substantive scientific revisions.

## Governance consequences

The structural maintenance closes EXT-UPD-1R.3. The parent external-asset update operation remains open.

Next controlled step: propagate this structural change through the current-state governance chain, then open EXT-UPD-2 for current-state content delta analysis.

No D-OPS-24 execution is authorized by this record.
