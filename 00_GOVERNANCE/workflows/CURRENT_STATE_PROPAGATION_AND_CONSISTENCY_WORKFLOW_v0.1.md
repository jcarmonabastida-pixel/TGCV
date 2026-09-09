# TGCV — Current-State Propagation and Consistency Workflow v0.2

**Status:** FROZEN GOVERNANCE WORKFLOW  
**Date:** 2026-09-09  
**Owner:** TGCV Governance  
**Canonical state register:** `00_GOVERNANCE/rma/TGCV_RMA_current.md`

## Purpose

Prevent governance-chain breaks and transient invalid canonical states after any substantive accepted change.

## Trigger

This workflow is mandatory after any substantive:

- Decision Record;
- Gate result;
- experimental execution/audit/replay/closure;
- scientific integration;
- claim/evidence change;
- architecture change;
- methodological/governance change.

## Mandatory propagation rule

### Atomicity rule

When a propagation affects two or more canonical/current-state assets, the complete affected state MUST be assembled and published to the canonical branch as **one Git commit**.

The canonical publication pattern is:

`inspect current HEAD → impact analysis → prepare all dependent changes → create blobs/tree → create ONE commit → update canonical ref → CI validation → human consistency closure → next gate`

For multi-file canonical propagation, the Git Data API (`create_blob` → `create_tree` → `create_commit` → `update_ref`) is the required publication mechanism.

The GitHub Contents API one-file-per-commit route MUST NOT be used to advance a multi-asset canonical state on `main`.

### Protected canonical assets

The following must be included in the same atomic commit whenever they are affected by the same propagation event:

- RMA master/version;
- current RMA pointer;
- current traceability;
- STATUS;
- current Evidence→Claim Matrix pointer;
- other declared canonical-state pointers;
- CHANGELOG entry for the same propagation.

A non-canonical supporting artifact may be committed independently only when its publication cannot make the current canonical state inconsistent.

## Mandatory sequence

`historical reconstruction → impact analysis → prepare complete dependent state → atomic canonical publication → machine consistency validation → human consistency closure → next gate`

No next controlled operation may be opened while the current-state consistency check is unresolved.

## CI behaviour

The machine validator MUST continue to validate every governance-relevant push/PR. A failing validator blocks progression.

However, CI validation is a **post-publication safety gate**. It does not replace atomic propagation. The objective is to prevent intermediate invalid canonical states from being published to `main`, rather than merely detecting them after publication.

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
- next gate opened before consistency closure;
- multi-asset canonical propagation published through sequential commits.

## Recovery rule

If a canonical propagation accidentally produces an intermediate failing commit, do not continue with additional sequential pointer commits. Stop propagation, reconstruct the intended final state from the last valid HEAD, and publish the complete correction atomically in one commit. Record the incident as a governance-integrity audit; do not rewrite historical commits or claim that the warning never occurred.

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

## Closure

The workflow is satisfied only when:

- all affected current assets are propagated or explicitly marked unaffected;
- the canonical propagation was atomic when multiple current assets were affected;
- RMA and STATUS agree;
- claim/evidence control agrees;
- next gate agrees;
- validator passes;
- a human consistency closure is recorded.
