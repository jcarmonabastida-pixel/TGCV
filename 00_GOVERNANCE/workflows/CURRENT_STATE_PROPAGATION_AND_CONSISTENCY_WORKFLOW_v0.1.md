# TGCV — Current-State Propagation and Consistency Workflow v0.1

**Status:** FROZEN GOVERNANCE WORKFLOW  
**Date:** 2026-09-08  
**Owner:** TGCV Governance  
**Canonical state register:** `00_GOVERNANCE/rma/TGCV_RMA_current.md`

## Purpose

Prevent governance-chain breaks after any substantive accepted change.

## Trigger

This workflow is mandatory after any substantive:

- Decision Record;
- Gate result;
- experimental execution/audit/replay/closure;
- scientific integration;
- claim/evidence change;
- architecture change;
- methodological/governance change.

## Mandatory sequence

`historical reconstruction → impact analysis → RMA version/update → dependent current assets → STATUS → claim/evidence control → CHANGELOG → machine consistency validation → human consistency closure → next gate`

No next controlled operation may be opened while the current-state consistency check is unresolved.

## Impact classes

### A — Scientific architecture
Check Core, analytical objects, definitions, invariants, formal specifications and architecture documents.

### B — Evidence / claims
Check Evidence-to-Claim Matrix, evidence level, falsified/open claims, claim boundaries and evidence references.

### C — Experiments
Check Decision Records, operational specifications, executor identity, dataset identity, execution/audit/replay/closure records and experiment status.

### D — Gates / programme sequence
Check open/closed/blocked/superseded gates and next controlled operation.

### E — RMA / portfolio
Check asset registry, dependency graph, current pointers and orphan/stale assets.

### F — External deliverables
Check Vision Paper, Research Prospectus, ARM, RII, MOI and methodological assets when they depend on changed scientific state.

## Required impact record

Every substantive change must record:

1. source change;
2. source commit;
3. affected assets;
4. unaffected assets and reason;
5. required version changes;
6. evidence/claim consequences;
7. gate consequences;
8. next operation;
9. validator result;
10. consistency-closure reference.

## Immutability

Historical artifacts are never rewritten to reflect current state. Current pointers and current versions may advance. Corrections to current versions create new versions.

## Epistemic protection

Document status and evidence level are separate. A document update cannot upgrade a scientific claim. Evidence level changes require evidence/gate support.

## Failure modes that MUST BLOCK progression

- stale RMA/current pointer;
- STATUS inconsistent with RMA;
- claim matrix inconsistent with accepted evidence;
- closed gate represented as open or vice versa;
- current architecture contradicts accepted Core;
- missing dependency propagation;
- orphan current asset without declared status;
- historical artifact overwritten;
- undocumented semantic replacement;
- next gate opened before consistency closure.

## Enforcement

The machine validator checks structural invariants and declared current-state pointers. Human review remains mandatory for semantic impact and scientific interpretation.

CI should execute the validator on every governance-relevant pull request/commit. A failing validator blocks the governance workflow until reconciled.

## Closure

The workflow is satisfied only when:

- all affected current assets are propagated or explicitly marked unaffected;
- RMA and STATUS agree;
- claim/evidence control agrees;
- next gate agrees;
- validator passes;
- a human consistency closure is recorded.
