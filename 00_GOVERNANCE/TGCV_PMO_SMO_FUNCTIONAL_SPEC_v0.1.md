# TGCV — PMO/SMO Functional Specification v0.1

**Date:** 2026-09-11  
**Status:** CURRENT / CONTROLLED — FUNCTIONAL DERIVATIVE  
**Nature:** Current programme-governance specification derived from recovered functional evidence; **not** a reconstruction of a historical original.

## 1. Purpose

Define the current functional role of PMO/SMO as the programme coordination and control layer across the TGCV operating cycle, while preserving the separation between scientific architecture, research execution, methodological assets, transfer and programme governance.

This specification does not modify the TGCV Core, scientific claims, current evidence status, SIP, RMA, or any closed experimental/gouvernance decision.

## 2. Provenance and derivation boundary

This specification is derived from:

- `TGCV_PROGRAMME_OPERATING_SYSTEM_v1.0.md` — canonical operational baseline, explicitly reconstructed rather than historical-original.
- `TGCV_INTERNAL_INTERFACES_v0.1.md` — recovered/working interface record.
- `TGCV_INTERNAL_ARCHITECTURE_RECOVERY_INDEX.md` — recovery status and prohibition against fabricating missing originals.
- Current SIP v0.1 and current RMA/governance state.

The exact historical PMO and SMO source artefacts remain unrecovered. If an original is later recovered, it becomes historical provenance and does not retroactively alter this derivative specification without explicit reconciliation.

## 3. Functional scope

PMO/SMO is the coordination/control function that:

1. maintains programme coherence across work items and assets;
2. coordinates dependencies, gates, decisions and versions;
3. routes selected work from SIP into controlled execution;
4. ensures evidence/results are returned to the appropriate governance layer;
5. coordinates architecture/governance review when a result may affect scientific or methodological state;
6. ensures canonical records are updated after substantive decisions;
7. maintains separation between research, methodology, transfer and governance;
8. supports continuity and provenance across sessions and execution contexts.

PMO/SMO does **not** constitute an additional scientific layer.

## 4. Programme control loop

The current controlled loop is:

`CURRENT PROGRAMME STATE`
`        ↓`
`RMA`
`        ↓`
`SIP / PRIORITISATION`
`        ↓`
`SELECTED WORK ITEM`
`        ↓`
`RESEARCH / SLR / EXPERIMENT / TRANSFER ACTIVITY`
`        ↓`
`EVIDENCE + RESULT + LIMITS`
`        ↓`
`DECISION / GATE`
`        ↓`
`ARCHITECTURE / GOVERNANCE REVIEW`
`        ↓`
`RMA + STATUS + RELEVANT ASSET UPDATES`
`        ↺`

PMO/SMO coordinates this loop; it does not replace the decision authority belonging to the relevant scientific or governance gate.

## 5. Interfaces

### 5.1 RMA ↔ PMO/SMO

RMA is the authoritative registry of programme assets, versions, states and dependencies.

PMO/SMO consumes RMA state to coordinate work and returns substantive governance decisions for canonical recording.

`PMO/SMO control decision → RMA state/version/dependency update`

### 5.2 SIP → PMO/SMO

SIP converts the current scientific/programme state into prioritised candidate work. PMO/SMO coordinates the selected work item through the applicable governance gates.

`RMA + current research state → SIP prioritisation → PMO/SMO coordination → controlled work`

SIP remains the planning/prioritisation layer; PMO/SMO is not a substitute for SIP.

### 5.3 PMO/SMO → execution

PMO/SMO may coordinate an authorised operation, its dependencies, preflight, evidence capture and closure. It does not itself create scientific evidence or silently authorise execution.

Execution authorization remains operation-specific and must be explicit where required.

### 5.4 Execution → PMO/SMO → governance

Results, hashes, limits and interpretation status return through the applicable gate. PMO/SMO ensures that substantive consequences are routed to RMA/STATUS and, where required, architecture review.

### 5.5 SLR / evidence subsystem

PMO/SMO coordinates the lifecycle but does not adjudicate scientific truth. The governed chain remains:

`question/claim → search/screen → source dossier → evidence → fact → structural comparison → absorption assessment → decision → RMA`

### 5.6 External transfer / value delivery

PMO/SMO may coordinate transfer work through MOI/RII and external assets. External actors, pilots or applications are not automatically evidence for TGCV claims. Their evidentiary status must be explicitly assessed.

## 6. Separation of functions

| Function | Primary layer | PMO/SMO role |
|---|---|---|
| Scientific architecture | Core / scientific governance | Coordinate review; cannot redefine Core |
| Research prioritisation | SIP | Route and coordinate; does not replace SIP |
| Asset registry | RMA | Maintain/update through governed changes |
| Research execution | L2 | Coordinate authorised work |
| Evidence/claims | Scientific governance | Ensure routing and provenance |
| Methodology | ARM/RII/MOI | Coordinate dependencies; no silent scientific upgrade |
| External transfer | L4 | Coordinate controlled opportunities/work items |
| Execution authorization | Operation-specific governance | Enforce explicit authorization boundary |
| Canonical state | Governance | Ensure propagation and validation |

## 7. Gate discipline

A PMO/SMO work item must identify, where applicable:

- objective;
- source/canonical dependency;
- scientific or methodological boundary;
- evidence required;
- preflight condition;
- execution authorization condition;
- stop/hard-stop criteria;
- result and limitation record;
- propagation requirement;
- validation requirement.

A work item is not considered closed merely because execution completed. Closure requires the applicable result, interpretation, provenance and propagation records.

## 8. Scientific protection rules

PMO/SMO shall not:

- change `Core_ontological = S` by programme decision;
- convert `T_acc` into an ontological primitive;
- promote explanatory `I` to a Core primitive;
- upgrade a claim without governed evidence;
- infer industrial utility, superiority, causality or value from coordination status;
- reopen a closed scientific test merely to resolve programme-management uncertainty;
- treat an external partner or pilot as prior validation.

Current methodological boundary remains that complete ex-ante enumeration of `T_acc` is not a universal experimental prerequisite.

## 9. Current scientific boundary

The governing architecture remains:

`Core = S`

`T_acc = F(S,C,L)`

`ΔT_acc → ΔReach → ΔTrajectory`

`Trajectory → Outcome → Value`

`I` is an explanatory mechanism/event, not a Core primitive.

## 10. Status model

PMO/SMO uses the programme asset-state discipline:

`DRAFT → WORKING → REVIEW → FROZEN → SUPERSEDED`

Historical/recovered artefacts additionally retain provenance labels such as `HISTORICAL`, `RECOVERED` and `UNVERIFIED`.

This specification is `CURRENT / CONTROLLED` and may be revised through explicit governance while this version remains immutable provenance.

## 11. Non-goals

This specification does not:

- reconstruct missing historical PMO/SMO documents;
- define a corporate project-management methodology;
- create new scientific claims;
- authorize a specific experiment;
- replace SIP, RMA, STATUS, scientific gates or operation-specific protocols;
- establish industrial validation, utility, superiority, causality or financial value.

## 12. Open historical recovery

The following remain historical recovery targets:

- exact PMO source artefact;
- exact SMO source artefact;
- Project Zero → PMO/SMO rules;
- Work Contract → PMO/SMO rules.

Recovery of these sources is not a blocker for use of this current functional derivative, but any recovered original must be reconciled explicitly before changing the current specification.

## 13. Controlled relationship to Programme OS and SIP

This document operationalises the PMO/SMO function already identified by the Programme Operating System and recovered interface record. It does not supersede either document.

SIP remains the programme planning/prioritisation instrument. PMO/SMO remains the coordination/control function. RMA remains the canonical asset/state registry.

**No scientific state change is introduced by this document.**
