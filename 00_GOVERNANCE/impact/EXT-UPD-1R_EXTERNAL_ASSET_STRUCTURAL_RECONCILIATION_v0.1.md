# EXT-UPD-1R — External Asset Structural Reconciliation v0.1

**Date:** 2026-09-08  
**Status:** CLOSED — STRUCTURAL RECONCILIATION COMPLETE / CONTENT UPDATE NOT YET STARTED  
**Parent operation:** `00_GOVERNANCE/impact/IMPACT-EXT-ASSETS-UPDATE_v0.1.md`  
**Scope:** identity, location and semantic role of external-facing assets only.

## 1. Objective

Establish a single canonical identity and location for each external deliverable family before drafting new versions.

This operation does **not** modify scientific content, empirical evidence, claims, gates or historical artefacts.

## 2. Structural rule established

> One external asset family = one canonical identity = one canonical location.

The asset identity is determined by the `TGCV-EXT-*` identifier and its semantic role, not by the historical filename or the directory in which an earlier version was created.

`05_ASSETS` is established as the canonical surface for external-facing deliverables.

Scientific source material remains in `01_SCIENTIFIC_CORE`; external-science preparation remains in `02_EXTERNAL_SCIENCE`; impact/transfer analysis remains in `04_IMPACT_TRANSFER`; governance/RMA remains in `00_GOVERNANCE`.

## 3. Reconciled asset families

| Asset ID | Family | Canonical location | Current finding |
|---|---|---|---|
| `TGCV-EXT-TCP-001` | TCP | `05_ASSETS/TCP/` | Canonical family exists; `TGCV-EXT-TCP-001_v0.2.md` is present. |
| `TGCV-EXT-VP-001` | Vision Paper | `05_ASSETS/Vision_Paper/` | Canonical family exists; `TGCV-EXT-VP-001_v0.1.md` is present. The older `02_EXTERNAL_SCIENCE/VISION_PAPER_POST_EMP11_v0.2.md` is treated as historical/preparatory, not a competing current identity. |
| `TGCV-EXT-RP-001` | Research Prospectus | `05_ASSETS/Research_Prospectus/` | Canonical family is established conceptually, but the current scientific generic RP file has not yet been created there. The IE PhD version is correctly separated as an adaptation. |
| `TGCV-EXT-ARM-001` | ARM | `05_ASSETS/ARM/` | No canonical ARM file was identified. The `01_SCIENTIFIC_CORE/TGCV_METHODOLOGY_POST_EMP11_v0.2.md` file is scientific methodology, not an ARM, and must not be relabelled as such. |
| `TGCV-EXT-RII-001` | RII | `05_ASSETS/RII/` | No canonical RII file was identified. `04_IMPACT_TRANSFER/INNOVATION_IMPACT_ROADMAP_POST_EMP11_v0.2.md` is the historical/preparatory candidate for reconciliation, not yet a current RII. |
| `TGCV-EXT-MOI-001` | MOI | `05_ASSETS/MOI/` | No asset to create now. Creation remains deferred under the parent operation. |

## 4. Research Prospectus distinction

The following distinction is now normative:

- Generic scientific Research Prospectus = `TGCV-EXT-RP-001`.
- Programme/application adaptations are derived artefacts and do not create new scientific asset identities.
- `05_ASSETS/Research_Prospectus/IE/Research_Prospectus_IE_PhD_v0.1.md` remains an IE application-stage adaptation/history artefact.

The existing README already preserves this distinction. No historical IE file is to be overwritten. fileciteturn374file0

## 5. ARM determination

The reconciliation explicitly rejects the assumption that `TGCV_METHODOLOGY_POST_EMP11_v0.2.md` is the ARM.

That document is located in `01_SCIENTIFIC_CORE` and declares itself provisional scientific methodology. It belongs to the scientific/methodological layer and must remain there. fileciteturn360file0

Therefore `TGCV-EXT-ARM-001` remains an identified dependent asset without a current canonical document.

## 6. RII determination

`04_IMPACT_TRANSFER/INNOVATION_IMPACT_ROADMAP_POST_EMP11_v0.2.md` is confirmed as the strongest historical/preparatory candidate for the RII family because its function is strategic impact/transfer planning.

It is **not** promoted automatically to current RII because its evidential starting point is tied to the older EMP-1.1 state and therefore requires controlled content reconciliation against the current RMA and claim matrix. fileciteturn378file0

## 7. Scientific documents that must not be reclassified

The following remain scientific-core documents and are not external assets merely because their titles resemble deliverables:

- `01_SCIENTIFIC_CORE/RESEARCH_PROSPECTUS_POST_EMP11_v0.2.md` — historical/internal canonical scientific draft from the pre-DYN2 state. It must remain immutable. fileciteturn380file0
- `01_SCIENTIFIC_CORE/TGCV_METHODOLOGY_POST_EMP11_v0.2.md` — provisional scientific methodology. fileciteturn360file0
- `01_SCIENTIFIC_CORE/TGCV_REFERENCE_ARCHITECTURE_POST_EMP11_v0.2.md` — scientific reference-architecture draft, explicitly not a transfer deliverable. fileciteturn379file0

## 8. Canonical external directory target

The target canonical structure is:

```text
05_ASSETS/
├── README.md
├── TCP/
│   └── TGCV-EXT-TCP-001_vX.Y.md
├── Vision_Paper/
│   └── TGCV-EXT-VP-001_vX.Y.md
├── Research_Prospectus/
│   ├── TGCV-EXT-RP-001_vX.Y.md
│   ├── README.md
│   └── adaptations/
│       └── IE_PhD/
│           └── Research_Prospectus_IE_PhD_vX.Y.md
├── ARM/
│   └── TGCV-EXT-ARM-001_vX.Y.md
├── RII/
│   └── TGCV-EXT-RII-001_vX.Y.md
└── MOI/
    └── [deferred]
```

The exact physical migration of historical files is a separate controlled maintenance action. This reconciliation does not move or delete files.

## 9. Current canonical inventory after reconciliation

### Canonical current families already physically represented

- TCP: present in `05_ASSETS/TCP/`. fileciteturn365file0
- Vision Paper: present in `05_ASSETS/Vision_Paper/`. fileciteturn366file0
- Research Prospectus container: present in `05_ASSETS/Research_Prospectus/`, with IE adaptation isolated. fileciteturn367file0

### Canonical families structurally reserved but not yet populated

- ARM: `05_ASSETS/ARM/`
- RII: `05_ASSETS/RII/`
- MOI: `05_ASSETS/MOI/` deferred.

The existing `05_ASSETS` README is therefore stale/incomplete and should be updated only during the subsequent controlled structural maintenance step. fileciteturn373file0

## 10. Governance consequences

The parent external-asset update operation remains open.

This reconciliation closes **EXT-UPD-1R.1 / EXT-UPD-1R.2 structural identity work** but does not close the overall external-update operation.

Next controlled steps:

1. structural maintenance of `05_ASSETS` and current pointers;
2. RMA/traceability propagation for the structural change;
3. EXT-UPD-2 current-state content delta analysis;
4. controlled drafting of new asset versions;
5. cross-asset consistency closure.

No D-OPS-24 execution is authorized by this record.

## 11. Non-effects

This reconciliation does not:

- change TGCV Core;
- change the Evidence-to-Claim Matrix;
- upgrade any evidence level;
- establish originality or superiority;
- establish causality, prediction, value creation or transversal empirical validity;
- create an industrial use case;
- promote the historical RII candidate to current status;
- create the MOI.

**Decision:** Structural identity is reconciled. The repository can now be cleaned and regularised without semantic ambiguity.
