# TGCV — Internal Architecture Recovery Index

**Date:** 2026-09-11  
**Status:** RECOVERY IN PROGRESS  
**Purpose:** recover and canonicalize the internal architecture, governance and programme-control assets that accumulated across TGCV research conversations and ChatGPT Library artefacts.

## 1. Recovery principle

The objective is preservation before reinterpretation. Recovered material is not automatically current. Each item must retain provenance and an epistemic/status label.

Suggested status labels:

- `FOUNDATIONAL` — explicitly established and still compatible with the current canonical state.
- `CURRENT` — current operational programme state.
- `WORKING` — useful working material subject to revision.
- `HISTORICAL` — genuine TGCV material from an earlier stage.
- `SUPERSEDED` — replaced by a later explicit decision.
- `UNVERIFIED` — referenced or partially recovered but not yet sufficiently evidenced.
- `RECOVERED — CANONICAL CANDIDATE` — recovered specification adopted as a governance candidate, without claiming verbatim historical reproduction.

## 2. Recovery inventory — confirmed

### 2.1 RMA

- `TGCV_RMA_v0.1.md` — recovered from Library; contains asset registry, epistemic states, dependencies, traceability schema and update rules.
- `TGCV_RMA_traceability_v0.1.csv` — recovered traceability matrix.

The RMA explicitly defines the programme asset classes and the dependency order: external assets; methodological infrastructure (SIP, PMO/SMO, SDM); and SLR infrastructure.

### 2.2 Research continuity / transfer package

- `TGCV — Paquete maestro de transferencia y continuidad tras TR-140.md` — recovered and highly valuable as a continuity record.

It records the stabilized architecture, test sequence, epistemic boundaries and the rule that SLR-1 must attempt to falsify architectural originality rather than confirm it.

### 2.3 Core / conceptual history

- `TGCV Fundacional v0.1.pdf` — historical foundational formulation.
- `Conversación Investigación TGCV.pdf` — long-form research history containing conceptual derivations, counterexamples, formalization attempts and evolution of the system/generativity/value framing.

These are historical evidence, not a replacement for the later stabilized Core.

### 2.4 TCP

- `TGCV-EXT-TCP-001_v0.1.md`
- `TGCV-EXT-TCP-001_v0.2.md`

v0.2 records the critical distinction between conceptual `T_acc`, operational representation `R`, and empirical performance, and preserves the rule that prior-art equivalence remains an SLR question.

## 3. Recovered programme-control assets

The `00_GOVERNANCE/RECOVERY/RECOVERED_ASSETS/` directory contains four recovered specifications supplied by the programme owner. They are explicitly marked `RECOVERED — CANONICAL CANDIDATE`; their provenance notes state that they are not claimed to be verbatim historical transcripts.

| Asset | Recovery status | Current interpretation |
|---|---|---|
| `ACTIVO_001_PROYECTO_CERO_v0.1.md` | `RECOVERED — CANONICAL CANDIDATE` | Origin-level programme identity: purpose, scope and permanent principles |
| `ACTIVO_002_CONTRATO_DEL_PROGRAMA_v0.1.md` | `RECOVERED — CANONICAL CANDIDATE` | Constitutional governance contract: principles, commitments and behavioural rules |
| `ACTIVO_003_ACTI_v1.0.md` | `RECOVERED — CANONICAL CANDIDATE` | Integral scientific-technological programme architecture |
| `ACTIVO_004_MOI_OPERATIVO_v1.0.md` | `RECOVERED — CANONICAL CANDIDATE` | Operational research workflow / knowledge-transformation flow |

### 3.1 Project Zero

Project Zero is explicitly defined as the origin-level programme asset. It defines the Programme, not TGCV as a scientific theory. Its recovered specification establishes no dependency on another TGCV programme asset and states that it feeds downstream programme, methodological and scientific assets.

Existing reconciliation record `ACTIVO_001_RECONCILIATION.md` already corrected the earlier weaker interpretation of Project Zero as merely an inferred upstream dependency.

### 3.2 Programme Contract

The recovered Programme Contract is explicitly the second constitutional document of the Programme. It depends on Project Zero and defines how the Programme decides and works while protecting scientific, methodological and strategic integrity. It is explicitly **not a legal contract**.

### 3.3 ACTI

ACTI is recovered as the integral scientific-technological architecture. It explicitly places the TGCV Reference Architecture & Methodology inside the scientific-technological core rather than treating it as a transfer-only deliverable. This must be reconciled with current asset taxonomy before any promotion is made.

### 3.4 MOI-Operativo

MOI-Operativo is recovered as the operational process specification for how the Programme conducts research. It distinguishes itself explicitly from the Modelo Ontológico Inicial (MOI). Its recovered sequence places it before SIP and defines a four-cycle discovery/explanation/transformation/programme-learning model.

## 4. Internal assets specifically requested — current recovery status

| Asset | Recovery status | Action |
|---|---|---|
| Proyecto Cero | Recovered specification; canonical candidate | Reconcile against current Programme OS / PMO / SIP |
| Contrato del Programa | Recovered specification; canonical candidate | Reconcile against current Programme OS / PMO / PMO-SMO |
| PMO | Current functional derivative exists; exact historical source unrecovered | Preserve derivative; continue historical recovery separately |
| SMO | Current functional derivative exists; exact historical source unrecovered | Preserve derivative; continue historical recovery separately |
| SIP | Current controlled asset v0.1 | Reconcile recovered operational sequence before any further certification/change |
| ACTI | Recovered specification; canonical candidate | Reconcile with current scientific/asset taxonomy |
| ACTII | Historical distinction remains unresolved | Targeted recovery only |
| Flujos / MOP | MOI-Operativo recovered; exact historical Flows/MOP semantics remain unresolved | Reconcile terminology and recover exact source if available |
| SLR architecture | Partially recovered | Consolidate after targeted retrieval |
| Evidence Bank | Explicitly referenced by RMA/ACTI | Recover source artefact |
| Fact Bank | Explicitly referenced by RMA/ACTI | Recover source artefact |
| SLR-1 Prior-Art Absorption Matrix | Explicitly established as scientific gate in recovered continuity package | Recover working matrix and preserve versions |
| SDM / discovery methodology | Referenced as proposed methodological asset | Recover and classify before formalizing |

## 5. Correction to 2026-09-11 source-recovery audit

The targeted search operation recorded in `PROJECT_ZERO_WORK_CONTRACT_SOURCE_RECOVERY_AUDIT_2026-09-11.md` was incomplete because it searched textual/indexed repository surfaces but did not inspect the `RECOVERED_ASSETS` directory directly.

That audit must therefore be treated as **superseded for the recovery classification of Project Zero and Work Contract**.

The correct current classification is:

- Project Zero: `RECOVERED — CANONICAL CANDIDATE`.
- Programme Contract / Work Contract: `RECOVERED — CANONICAL CANDIDATE`.

The recovered provenance notes do not claim verbatim historical reproduction. This distinction is retained.

## 6. What must NOT be done during recovery

1. Do not recreate missing documents as if they were recovered originals.
2. Do not merge early conceptual formulations into the current Core without an explicit transition record.
3. Do not overwrite historical versions.
4. Do not promote a recovered candidate automatically to `CURRENT` without reconciliation against current canonical governance.
5. Do not use recovery to reopen stabilized scientific decisions.
6. Do not infer exact historical PMO/SMO/ACTII/Flows semantics where the recovered candidate does not establish them.
7. Do not allow recovered programme architecture to silently redefine the scientific Core.

## 7. Current canonical scientific boundary

The recovered programme assets do not supersede the current scientific boundary:

`Core_ontological = S`

`T_acc = F(S,C,L)`

`ΔT_acc → ΔReach → ΔTrajectory`

`Trajectory → Outcome → Value`

with `I` as explanatory mechanism rather than Core primitive.

## 8. Next recovery/reconciliation operation

Do **not** construct Project Zero or Work Contract derivatives: recovered candidates already exist.

The next operation is a **reconciliation audit** across:

`Project Zero → Programme Contract → ACTI / MOI-Operativo → PMO/SMO → SIP → RMA → current scientific/transfer assets`

The purpose is to identify only material contradictions, terminology collisions, stale dependencies or required provenance updates. No automatic promotion and no scientific change is implied.

## 9. Canonical continuity rule

GitHub remains the canonical continuity point for the whole TGCV programme. This recovery index is itself versioned evidence of what has and has not yet been recovered.
