# EXT-UPD-1R.4 — External Asset Structural Consistency Propagation v0.1

**Date:** 2026-09-08
**Status:** ACCEPTED — PROPAGATION REVIEW OPEN
**Parent:** `00_GOVERNANCE/impact/EXT-UPD-1R_EXTERNAL_ASSET_STRUCTURAL_RECONCILIATION_v0.1.md`

## 1. Change propagated

EXT-UPD-1R.3 regularised the physical canonical surface for external deliverables under `05_ASSETS/`.

Canonical families:
- `TGCV-EXT-TCP-001` → `05_ASSETS/TCP/`
- `TGCV-EXT-VP-001` → `05_ASSETS/Vision_Paper/`
- `TGCV-EXT-RP-001` → `05_ASSETS/Research_Prospectus/`
- `TGCV-EXT-ARM-001` → `05_ASSETS/ARM/`
- `TGCV-EXT-RII-001` → `05_ASSETS/RII/`
- `TGCV-EXT-MOI-001` → `05_ASSETS/MOI/` (reserved only)

The IE PhD adaptation is now under `05_ASSETS/Research_Prospectus/adaptations/IE_PhD/`.

## 2. Impact classification

**Class E — RMA/portfolio structure**, with dependent external-asset location updates.

No scientific proposition, empirical result, claim/evidence level, gate state, or experimental protocol is changed by this operation.

## 3. Propagation decisions

| Surface | Action |
|---|---|
| RMA current master | UPDATE to v0.4 with canonical external locations |
| RMA current pointer | UPDATE to v0.4 |
| RMA traceability | UPDATE to v0.4 with canonical locations and structural status |
| STATUS | UPDATE current RMA pointer and structural regularisation state |
| Evidence-to-Claim Matrix | EXPLICITLY UNAFFECTED; no evidence/claim change |
| TCP | EXEMPT from content revision in this structural operation; current file remains current family member |
| Vision Paper | EXEMPT from content revision in this structural operation |
| Research Prospectus | EXEMPT from content revision; IE adaptation location regularised |
| ARM | RESERVED; no substantive content yet |
| RII | RESERVED; historical candidate remains outside current family |
| MOI | RESERVED; substantive creation deferred |
| CHANGELOG | UPDATE |
| Machine validator | UPDATE to validate v0.4 and canonical external structure |

## 4. Historical integrity

No historical scientific or external document is overwritten. The old IE adaptation path is removed only after its content was reproduced at the canonical adaptation path. Historical/preparatory documents in `01_SCIENTIFIC_CORE`, `02_EXTERNAL_SCIENCE` and `04_IMPACT_TRANSFER` remain immutable.

## 5. Claim/evidence consequence

No claim is upgraded, downgraded or otherwise changed. The authoritative Evidence-to-Claim Matrix remains unchanged and is explicitly exempted from content modification.

## 6. Gate consequence

D-OPS-24 remains NEXT and unblocked from governance-consistency perspective, but this propagation operation does not authorize its execution.

## 7. Required closure

Closure requires:
1. RMA v0.4 current;
2. current pointer aligned;
3. traceability v0.4 aligned;
4. STATUS aligned;
5. CHANGELOG updated;
6. validator updated and passing;
7. human consistency closure recorded.
