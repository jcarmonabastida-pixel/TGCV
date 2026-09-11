# ACTI ↔ ARM Taxonomy / Architectural-Role Reconciliation Audit

**Date:** 2026-09-11  
**Status:** `CLOSED — CONTROLLED RECONCILIATION`  
**Scope:** recovered ACTI architectural role of TGCV Reference Architecture & Methodology (ARM) versus current controlled ARM asset classification.

## 1. Objective

Resolve the controlled follow-up identified by the programme recovered-assets reconciliation audit: ACTI describes the TGCV Reference Architecture & Methodology as part of the scientific-technological core, while the current asset registry contains `TGCV-EXT-ARM-001` under `05_ASSETS/ARM/` as a controlled external asset.

The purpose is to reconcile **architectural role** and **asset identity/location** without silently changing scientific state.

## 2. Admitted canonical inputs

- `00_GOVERNANCE/RECOVERY/RECOVERED_ASSETS/ACTIVO_003_ACTI_v1.0.md` — recovered canonical candidate.
- `05_ASSETS/ARM/TGCV-EXT-ARM-001_v0.2.md` — current controlled ARM asset.
- `05_ASSETS/README.md` — current external-asset registry classification.
- `00_GOVERNANCE/CANONICAL_STATE.json` — current canonical scientific/programme state.
- `00_GOVERNANCE/rma/TGCV_RMA_current.md` — current RMA.

## 3. Reconciliation finding

ACTI assigns ARM a **scientific-technological architectural role**: it is a central pillar of the TGCV scientific-technological architecture and methodology.

The current registry assigns ARM the asset identity `TGCV-EXT-ARM-001` and stores it under `05_ASSETS/ARM/` as a controlled reusable asset.

These statements operate at different levels:

1. **Architectural role:** what function ARM performs in the programme's scientific-technological architecture.
2. **Asset classification/location:** how the current repository manages the concrete controlled artifact for continuity, reuse and external-facing work.

Therefore, the evidence does **not** require relocation of the current ARM file, nor does it justify automatic promotion of the asset into the ontological Core.

## 4. Reconciled interpretation

The controlled interpretation adopted is:

> **ARM is scientifically architectural in role, while its current controlled artifact remains a separately identified governed asset.**

Consequences:

- `ARM` may contribute to the scientific-technological architecture and methodology.
- `ARM` is not thereby an ontological primitive.
- `ARM` does not redefine `Core_ontological = S`.
- `ARM` does not become equivalent to the scientific Core merely because ACTI places its architectural role at the core level.
- The current asset location under `05_ASSETS/ARM/` remains valid for programme control unless a separate asset-taxonomy decision changes it.
- No scientific claim is upgraded by this reconciliation.

## 5. Architectural distinction

The following distinction is now explicit:

```text
SCIENTIFIC ONTOLOGICAL CORE
    Core_ontological = S

        ↓

SCIENTIFIC-TECHNOLOGICAL ARCHITECTURE / METHODOLOGY
    ARM = architectural + methodological pillar

        ↓

CONTROLLED PROGRAMME ASSET
    TGCV-EXT-ARM-001_v0.2
    05_ASSETS/ARM/
```

The layers are related but not interchangeable.

## 6. Governance decision

`ACTI ↔ ARM RECONCILIATION = PASS`

No relocation, promotion, demotion, Core modification, claim-matrix modification, or scientific re-execution is required by this audit.

The reconciliation closes Follow-up A from the recovered-assets reconciliation audit.

## 7. Propagation boundary

Because the result resolves taxonomy/architectural semantics but does not alter scientific state, no RMA, Evidence→Claim Matrix, or traceability version change is required solely by this audit.

The current canonical versions therefore remain:

- RMA `v3.32`
- Evidence→Claim Matrix `v1.1`
- Traceability `v3.32`
- ARM `TGCV-EXT-ARM-001_v0.2`

Any future change to ARM's asset identity, location, version, or scientific authority must be handled as a separate controlled change.

## 8. Closure

`FOLLOW-UP A = CLOSED.`

The remaining follow-up from the reconciliation audit is the executable IGRT/session integration layer; IGRT v0.1 has already been functionally validated through START and both CLOSE paths.
