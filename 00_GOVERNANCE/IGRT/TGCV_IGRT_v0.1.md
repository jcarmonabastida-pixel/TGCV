# TGCV Integrated Governance Runtime — IGRT v0.1

**Status:** CURRENT / CONTROLLED — EXECUTABLE GOVERNANCE LAYER  
**Date:** 2026-09-11  
**Scope:** session continuity, proportional governance, material-change control and canonical-state validation

## 1. Purpose

IGRT is the executable integration layer for the TGCV governance system. It does not replace governance specifications, RMA, SIP, PMO/SMO, the scientific registry or the current-state validator. It connects them into a lightweight session lifecycle that can be invoked at the beginning and end of each ChatGPT working session.

The design principle is **governance by flow, not governance by document repetition**.

## 2. Non-authority principle

IGRT is a coordination/runtime layer. It must never:

- redefine the scientific Core;
- upgrade claims;
- infer scientific validity from governance PASS;
- reopen closed tests or operations;
- grant experimental or industrial authorization by itself;
- replace human/programme-owner decisions where explicit authorization is required.

## 3. Session lifecycle

### START

`SESSION_START`

1. Resolve repository root.
2. Load `CANONICAL_STATE.json`.
3. Resolve current RMA, matrix, traceability, governance principles, STATUS, CHANGELOG, registry and validator.
4. Run the existing `validate_current_state.py` as the canonical current-state gate.
5. Load the active programme context relevant to the session.
6. Return a compact `SESSION_READY` state.

### RUN

Normal work proceeds without repeatedly reloading all governance documents.

The runtime asks for escalation only when an action is potentially material:

- scientific Core / claim boundary;
- current canonical pointer/version;
- governed evidence or interpretation;
- new experiment or controlled execution;
- authorization boundary;
- provenance/integrity;
- material asset status/dependency.

Routine drafting, analysis, inspection and continuation remain low-friction operations.

### CLOSE

`SESSION_CLOSE`

1. Capture material decisions/results supplied by the session.
2. Classify whether canonical governance was materially affected.
3. If no material change: emit `SESSION_CLOSED_NO_MATERIAL_CHANGE`.
4. If material governance changed: require propagation through the applicable canonical surfaces.
5. Run the canonical validator after substantive canonical changes.
6. Emit a compact continuation record for the next session.

## 4. Proportional governance levels

| Level | Typical activity | Runtime behaviour |
|---|---|---|
| G0 | inspection / analysis / drafting | continue |
| G1 | controlled document maintenance | record provenance; no scientific gate unless material |
| G2 | material evidence / interpretation | require propagation decision |
| G3 | scientific claim/Core change | explicit architecture/claim gate |
| G4 | new governed experiment/execution | preflight + explicit authorization |
| G5 | canonical-state mutation | propagation + validator |

IGRT does not itself decide scientific truth. It decides only whether the **governance path** must escalate.

## 5. Canonical continuity contract

The runtime treats GitHub repository state as the continuity source. Local execution is operational data.

At START, the minimum authoritative chain is:

`CANONICAL_STATE → RMA → Evidence→Claim Matrix → traceability → STATUS → validator`

The Scientific Asset Registry is the mandatory reuse/discovery surface before new scientific gates, audits, experiments, domain selection, dataset search, operationalisation or cross-domain translation.

## 6. Closed-work protection

IGRT maintains a `closed_operations` context. A closed operation is not presented as pending merely because it is relevant to the current work.

Examples currently protected include TR-131, D-OPS-24/EXT-UPD-4.8, IT-NOSD-010 and other explicitly closed governed operations.

## 7. Session state

The runtime produces a machine-readable state containing at least:

- runtime version;
- timestamp;
- repository root;
- canonical-state status;
- current RMA/matrix/traceability versions;
- validator result;
- session phase;
- governance level;
- active work item, if supplied;
- material-change flag;
- required next action;
- continuation note.

The state is a continuity aid, not a scientific record unless explicitly promoted through normal governance.

## 8. Failure policy

Fail closed only when continuation would create a real integrity or governance risk, such as:

- missing/invalid canonical state;
- current-state validator failure before a material operation;
- unresolved canonical pointer required by the selected operation;
- attempt to silently alter a protected scientific boundary;
- execution requiring authorization that has not been granted.

Do not block ordinary analysis merely because an unrelated governance document is absent or an historical recovery item remains open.

## 9. Relationship to existing governance

- Project Zero: constitutional programme identity.
- Programme Contract: constitutional integrity rules.
- ACTI: scientific-technological architecture.
- MOI-Operativo: knowledge-transformation workflow.
- SIP: scientific integration and prioritisation.
- PMO/SMO: programme coordination/control.
- RMA/Matrix/Traceability: canonical scientific state.
- Scientific Asset Registry: reuse gate.
- Validator: canonical-state integrity gate.
- IGRT: executable session integration layer.

## 10. Current limitations

v0.1 is intentionally conservative. It integrates and checks existing governance; it does not yet perform automatic propagation, automatic Git commits, scientific decision-making or authorization issuance.

Those capabilities require separate explicit design and should not be smuggled into a session bootstrapper.

## 11. Acceptance target

A successful IGRT START should reduce the normal session bootstrap to one executable command and one compact machine-readable result. A successful CLOSE should produce a clear continuation state and invoke the canonical validator whenever required.

**IGRT v0.1 is therefore an executable integration layer, not another governance bureaucracy layer.**
