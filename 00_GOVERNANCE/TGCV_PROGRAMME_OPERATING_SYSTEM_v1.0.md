# TGCV — Programme Operating System v1.0

**Date:** 2026-08-27  
**Status:** CANONICAL OPERATIONAL BASELINE — reconstructed, not historical-original

> This document is the first operational baseline of the TGCV Programme Operating System. It consolidates recovered evidence and explicitly marked functional reconstruction. It does not claim to reproduce missing historical artefacts verbatim.

## 1. Purpose

Provide a stable operating layer for continuing TGCV across conversations, documents, experiments and external work without depending on conversational memory.

The repository is the continuity point; the Programme OS defines how the repository is used and how programme state changes.

## 2. Governing principles

1. **Preserve before reinterpretation.** Historical artefacts are immutable provenance.
2. **Current state beats historical state for execution.** Historical material remains available but does not override later freezes.
3. **Scientific Core is protected.** Programme operations cannot silently alter the Core.
4. **Every substantive change has provenance.**
5. **Evidence precedes promotion.** Working constructs do not become foundational by repetition.
6. **Separate science, methodology and programme governance.**
7. **Repository state is the continuity reference.**

## 3. Programme layers

### L0 — Continuity / Governance

- Programme OS
- STATUS
- freezes
- decisions
- provenance
- recovery index

### L1 — Scientific architecture

- TGCV Core
- conceptual tests
- empirical operationalisation
- SLR / prior-art programme

Current scientific boundary:

`Core = S`

`T_acc = F(S,C,L)`

`ΔT_acc → ΔReach → ΔTrajectory`

`Trajectory → Outcome → Value`

`I` = explanatory mechanism, not Core primitive.

### L2 — Research execution

- research questions
- SLR dossiers
- evidence/fact management
- experiments
- analyses
- falsification tests

### L3 — Applied methodology

- ARM
- RII
- MOI
- value-construction methodology
- external application assets

Applied methodology may derive from or operationalise the scientific architecture but cannot redefine it without an explicit scientific decision.

### L4 — External transfer

- Vision Paper
- Research Prospectus
- academic candidature assets
- Orange / industrial research assets
- other external deliverables

## 4. Operating control loop

```text
CURRENT PROGRAMME STATE
        ↓
       RMA
        ↓
       SIP
        ↓
 SELECT NEXT WORK
        ↓
 RESEARCH / SLR / EXPERIMENT
        ↓
 EVIDENCE + RESULT
        ↓
 DECISION / GATE
        ↓
 ARCHITECTURE REVIEW
        ↓
 RMA + STATUS UPDATE
        ↺
```

PMO/SMO is the coordination/control function across this loop.

## 5. Asset-state discipline

Every significant asset should have:

- identifier;
- version;
- status;
- provenance;
- dependencies;
- current/canonical flag;
- supersession relationship where applicable;
- associated decision/gate where relevant.

Recommended statuses:

`DRAFT` → `WORKING` → `REVIEW` → `FROZEN` → `SUPERSEDED`

Historical recovered artefacts additionally use:

`HISTORICAL` / `RECOVERED` / `UNVERIFIED`

## 6. Change control

### Scientific change

Requires evidence, explicit test/argument and architecture review. A conversational proposal is not a Core change.

### Methodological change

Must identify the scientific dependency it uses and must not introduce circularity into the scientific Core.

### Governance change

Must update the relevant governance artefact and provenance record.

### External asset change

Must be traceable to the current scientific/methodological state and must not silently become evidence for the Core.

## 7. SLR operating interface

The current working chain is:

`claim/question → search/screen → source dossier → evidence → fact → structural comparison → absorption assessment → decision → RMA`

SLR-1 specifically addresses architectural originality and must distinguish terminology similarity, construct equivalence, structural equivalence and full architectural absorption.

## 8. Recovery interface

Missing historical assets are handled through:

`RECOVERY INDEX → source search → provenance → confidence classification → functional reconstruction (if necessary) → reconciliation → canonical derivative`

A reconstruction never replaces the original source if the latter is later found.

## 9. Session continuity protocol

At the beginning/end of substantial work, the working state should be recoverable from:

1. `STATUS.md`;
2. RMA;
3. current freezes;
4. current Programme OS;
5. active research/SLR records;
6. recovery index where historical context matters.

The chat is an execution interface, **not the canonical store**.

## 10. Current known historical gaps

The following remain recovery targets and are not fabricated here:

- Project Zero original;
- Work Contract original;
- exact historical SIP specification;
- exact PMO/SMO specification;
- ACTII original/specification;
- Flows/MOP original/specification;
- full historical SDM specification;
- full historical SLR SOP/matrices.

## 11. Relationship to historical value methodology

The recovered historical value-construction framework is retained as programme intellectual heritage and as a possible input to applied methodology. It is not part of the minimal scientific ontology merely because it predates the current Core.

## 12. Canonicality rule

This v1.0 is canonical **as an operating baseline**, not as a claim about what the historical programme document originally said.

Future versions may modify the operating baseline through explicit governance decisions while preserving this version as provenance.

## 13. Next controlled improvements

1. Recover Project Zero / Work Contract sources if possible.
2. Recover ACTII and Flows/MOP semantics.
3. Reconcile historical SIP/PMO procedures against current operation.
4. Consolidate SLR SOP and evidence lifecycle.
5. Add automated repository checks for status/provenance consistency.
6. Link Programme OS to STATUS/RMA and active freezes.
