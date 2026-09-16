# TGCV — Governance Lessons Learned 001

**Status:** PERSISTENT GOVERNANCE LESSON / OPERATIVE PROCEDURAL GUIDANCE  
**Date:** 2026-09-16  
**Origin:** MT4 governance-closure episode  
**Location:** `00_GOVERNANCE/` by deliberate design so that a future working session can discover this rule directly from the repository rather than relying on conversational memory.

## GL-001 — Repository-discoverable governance continuity

A governance rule that is intended to survive a ChatGPT conversation MUST be persisted in `00_GOVERNANCE/`. Conversational context is not a source of truth for governance continuity.

At the start of a future working session, governance continuity MUST be recoverable from the repository itself. In particular, the working process MUST inspect the governance material under `00_GOVERNANCE/` before reconstructing or proposing any cumulative governance update from conversational context.

## GL-002 — Never reconstruct a cumulative Evidence-to-Claim Matrix from conversation

The Evidence-to-Claim Matrix MUST NOT be reconstructed, rewritten, summarized, or regenerated from remembered conversation context.

A new matrix version MUST be derived mechanically from the exact canonical predecessor, preserving its complete material content, and then applying only explicitly authorized additive or corrective changes.

## GL-003 — No iterative repair loop for governance propagation

When canonical governance propagation is required, the process MUST NOT enter a sequence of speculative repair scripts, temporary workflows, residual versions, or repeated corrective commits.

If a propagation attempt fails, the process MUST return to the last verified canonical state and make one deterministic correction rather than layering another repair state on top of the failed state.

## GL-004 — Governance maintenance remains subordinate to scientific progress

Governance maintenance restores integrity and records scientific state; it is not itself scientific progress. Once the canonical governance gate is closed, work MUST return to the next pending scientific or methodological operation without creating additional governance work merely to refine the maintenance process.

## GL-005 — Canonical source hierarchy

For governance continuity, the repository is authoritative over conversational memory. The relevant hierarchy is:

`CANONICAL_STATE → canonical pointers/current artifacts → versioned historical artifacts → governance lessons/principles → conversation context`

Conversation context may explain why a change was made, but it MUST NOT be used as the authoritative reconstruction source when the repository contains the relevant artifact.

## GL-006 — MT4 incident recorded as a process warning

The MT4 governance episode demonstrated a concrete failure mode: a residual v1.12 artifact was followed by a v1.12 reconstruction that compressed/lost material from v1.11, followed by additional automation attempts. The result was disproportionate governance effort without corresponding scientific progress.

This incident is therefore recorded as a procedural warning against conversational reconstruction, cumulative rewriting, and iterative governance repair.

## GL-007 — Explicit X-update traceability for material evidence additions

The cumulative matrix rule is:

**Each version = complete predecessor + explicitly authorized additive/corrective changes.**

After the new version has been created as an exact byte-for-byte copy of the canonical predecessor, any material evidence result that is incorporated into the new version and materially changes, qualifies, bounds, or otherwise modifies the evidentiary basis or interpretation of one or more claims MUST be identified explicitly in the new version's header as an `X update` (for example, `MT4 update`, `C10C-004 update`).

The criterion for an `X update` is **material evidence propagation**, not claim-level upgrade. Therefore an `X update` is required even when the affected claim status remains unchanged, provided the evidence is material enough to be propagated into the matrix as a new evidentiary contribution or qualification.

The `X update` MUST be part of the matrix version content itself. It MUST NOT exist only as a workflow-generated note, temporary workflow, commit message, or external trace. A temporary workflow MAY perform an authorized mechanical edit during an exceptional recovery operation, but the resulting `X update` is valid only when persisted in the canonical matrix content and covered by the cumulative-version integrity checks.

Conversely, an evidence result that is not materially propagated into the new matrix version does not require an `X update`. Historical evidence already present in the predecessor is not repeated merely because it remains relevant.

### Required order for future cumulative matrix updates

1. Freeze/identify the exact canonical predecessor.
2. Create the new version as a byte-for-byte copy of that predecessor.
3. Identify material evidence additions/qualifications and determine which require an `X update`.
4. Add the `X update` entry or entries to the new version header together with the corresponding explicit claim-table/material-evidence additions.
5. Verify that predecessor content is preserved in order except for the explicitly authorized additive/corrective changes.
6. Only after content integrity passes, propagate the new version to `CURRENT` and update canonical pointers/state as required.
7. Run the canonical validator as the final gate.

This rule prevents a systematic omission in which the evidence is propagated into claim rows or material sections but the new version's top-level traceability fails to identify the evidence as a material novelty of that version.

## Future-session discovery instruction

**Before any future TGCV governance update, inspect `00_GOVERNANCE/` and locate this document (`GOVERNANCE_LESSONS_LEARNED_001.md`) and the active `GOVERNANCE_OPERATING_PRINCIPLES` artifact. Do not assume that either rule set is remembered from prior ChatGPT sessions.**
