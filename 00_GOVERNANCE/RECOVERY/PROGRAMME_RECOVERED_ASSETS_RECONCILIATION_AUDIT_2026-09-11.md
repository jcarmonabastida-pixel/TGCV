# TGCV — Reconciliation Audit of Recovered Programme Assets

**Date:** 2026-09-11  
**Status:** CLOSED — RECONCILIATION AUDIT  
**Scope:** Project Zero · Programme Contract · ACTI · MOI-Operativo · PMO/SMO · SIP · RMA/current governance

## 1. Purpose

Reconcile the recovered programme-control assets against the current controlled governance and scientific state without silently promoting recovered candidates, rewriting historical provenance, or modifying the scientific Core.

The audit confirms that `RECOVERED_ASSETS` contains four explicit recovered specifications. The directory is therefore a primary recovery surface that must be inspected before declaring a programme asset unrecovered.

## 2. Constitutional layer

### Project Zero

Project Zero defines programme identity, purpose, scope and permanent principles. It explicitly states that it defines the Programme, not the TGCV theory, and has no other programme asset as a conceptual prerequisite.

**Reconciliation:** compatible with current governance. Treat as upstream programme identity reference. No scientific authority is transferred to it.

### Programme Contract

The Programme Contract is the second constitutional asset. It defines behavioural/governance principles protecting scientific, methodological and strategic integrity and explicitly is not a legal contract.

**Reconciliation:** compatible with PMO/SMO and current governance. Its invariants should constrain programme coordination but must not determine scientific truth.

## 3. ACTI reconciliation

ACTI defines the integral scientific-technological architecture and explicitly places TGCV Reference Architecture & Methodology inside the scientific-technological core.

This creates a **material taxonomy reconciliation point** with the current external-asset registry, where ARM is maintained as `TGCV-EXT-ARM-001` in `05_ASSETS/ARM/`.

**Finding:** no automatic promotion or relocation is authorized.

The distinction to preserve is:

- ACTI: architectural role of reference architecture/methodology inside the programme's scientific-technological architecture.
- Current ARM asset registry: controlled artefact identity/location and current versioning.

These are not necessarily contradictory, but the architectural role and asset classification need one explicit reconciliation decision before a future governance integration treats them as identical.

## 4. MOI-Operativo reconciliation

MOI-Operativo defines the research workflow and establishes the Principle of Flow Primacy: the Programme is organised around knowledge transformation, not documents.

It proposes the ordering:

`Project Zero → Contract → Vision Paper → Research Prospectus → MOI-Operativo → SIP`

and distinguishes workflow description (MOI-Operativo) from governance/control (SIP).

**Reconciliation:** compatible with the desired integrated-governance direction, but the ordering is a recovered proposed sequence rather than a current canonical dependency graph. SIP v0.1 is already a current controlled planning asset and PMO/SMO v0.1 is already a current controlled functional derivative.

Therefore the sequence must be interpreted as **functional dependency**, not as a requirement that SIP or PMO/SMO cannot exist before a workflow document is present.

## 5. SIP / PMO-SMO interface reconciliation

A semantic asymmetry exists between current controlled documents:

- SIP v0.1 describes itself as a scientific planning/integration instrument and states that it logically precedes operational management instruments such as PMO/SMO.
- PMO/SMO v0.1 coordinates the programme operating loop and explicitly receives prioritisation from SIP while returning evidence/results to governance.

**Finding:** this is an interface-ordering ambiguity, not a scientific contradiction.

The safe integrated interpretation is:

`SIP = scientific prioritisation / integration authority within its scope`

`PMO/SMO = programme coordination / control function that operationalises selected work`

with a bidirectional controlled interface:

`RMA/current state → SIP prioritisation → PMO/SMO coordination → controlled work → evidence/results → governance → RMA/current state`

PMO/SMO does not override SIP scientific priorities; SIP does not itself grant execution authorization.

## 6. RMA reconciliation

RMA v3.32 remains the current scientific/programme asset registry and dependency reference. No recovered asset justifies modification of the scientific Core, claim matrix or closed experimental decisions.

The current governance chain remains:

`CANONICAL_STATE → RMA → Evidence→Claim Matrix → RMA traceability → STATUS → validator`

Recovered programme assets should be integrated as governance context and interfaces, not substituted for this chain.

## 7. Integrated programme model resulting from reconciliation

The reconciled functional architecture is:

```text
PROJECT ZERO
Programme identity / purpose / scope / principles
        ↓
PROGRAMME CONTRACT
Constitutional integrity / behavioural rules
        ↓
ACTI
Scientific-technological architecture
        ↕
MOI-OPERATIVO
Knowledge-transformation workflow
        ↕
SIP
Scientific prioritisation / integration
        ↓
PMO / SMO
Programme coordination / control / continuity
        ↓
RMA + evidence + experiments + SLR + methodology + transfer
        ↓
Decision / gate / propagation
        ↓
CANONICAL STATE + STATUS + validator
```

The arrows are functional interfaces, not an assertion that every activity is strictly linear.

## 8. Governance integration principle

The recovered assets support a governance model that is **flow-oriented rather than document-oriented**.

The minimum effective governance cycle should be:

`START → LOAD CANONICAL STATE → CHECK ACTIVE GOVERNANCE → SELECT/RESUME WORK → EXECUTE → RECORD MATERIAL DECISION/RESULT → PROPAGATE → VALIDATE → CLOSE`

The governance layer should intervene only when a gate, boundary, dependency, material decision, provenance issue or canonical-state change requires it.

Routine scientific work should not require repeated manual restatement of all governance documents.

## 9. Session lifecycle implication

The reconciliation supports creation of a future executable integration layer with three lightweight session operations:

### Session START

Resolve canonical pointers, current governance state, active programme constraints and the relevant work-item context. Fail closed only for conditions that genuinely invalidate safe continuation.

### Session RUN

Apply the minimum applicable governance gates to the selected operation; maintain provenance and decision boundaries; avoid reopening closed work.

### Session CLOSE

Record material outputs/decisions, propagate only material changes, run the current-state validator when canonical governance was affected, and emit a compact continuation state for the next session.

This is a functional governance design direction, not yet an implemented executable asset.

## 10. Decisions / boundaries

1. Project Zero and Programme Contract remain `RECOVERED — CANONICAL CANDIDATE`.
2. ACTI and MOI-Operativo remain `RECOVERED — CANONICAL CANDIDATE`.
3. No recovered asset is automatically promoted to `CURRENT` by this audit.
4. No scientific Core change.
5. No claim-matrix change.
6. No closed test reopened.
7. No execution authorization created.
8. ARM taxonomy/role requires explicit future reconciliation; no relocation now.
9. SIP/PMO ordering is resolved as a functional interface, not a rigid sequence.
10. An executable integrated governance layer is justified as the next architecture/governance operation.

## 11. Closure

**RECONCILIATION:** PASS WITH TWO CONTROLLED FOLLOW-UPS.  
**FOLLOW-UP A:** reconcile ACTI architectural role of ARM with current ARM asset classification.  
**FOLLOW-UP B:** implement the lightweight executable governance session layer around existing canonical-state validation and material-change propagation.

No scientific state change occurred.
