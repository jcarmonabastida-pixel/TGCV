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

## GL-007 — Per-version X-update traceability for material evidence additions

The cumulative matrix rule is:

**Each version = complete predecessor evidentiary content + explicitly authorized additive/corrective changes.**

The `X update` entries in the matrix header are **version-local traceability metadata**, not cumulative evidentiary content. They identify the material evidence novelties introduced or materially qualified by that specific version and MUST NOT be carried forward into the header of later versions merely because the underlying evidence remains part of the cumulative matrix.

Therefore, after creating the new version from the canonical predecessor, the header's `X update` block MUST be reset/replaced for the new version so that it contains **only** the `X update` entries corresponding to material evidence propagation performed in that update cycle. For example:

- v1.11: `C10C-003 update` and `C10C-004 update`.
- v1.12: `MT4 update` only.
- v1.13: only the material `X update` entries belonging to the v1.13 cycle.

The underlying evidentiary content, claim-row qualifications and material evidence sections remain cumulative unless explicitly corrected, superseded or retired under the governance rules. Historical `X update` metadata remains preserved in the historical version in which it was recorded; it is not deleted from historical artifacts and is not propagated into later headers.

An `X update` is required when a new version incorporates a material evidence result that changes, qualifies, bounds or otherwise modifies the evidentiary basis or interpretation of one or more claims, even when no claim-level status/level is upgraded. An evidence result that is not materially propagated into the new matrix version does not require an `X update`.

The `X update` MUST be persisted in the matrix version content itself. It MUST NOT exist only as a workflow-generated note, temporary workflow, commit message or external trace. Temporary automation must not be treated as the authoritative traceability mechanism.

### Required order for future cumulative matrix updates

1. Freeze/identify the exact canonical predecessor.
2. Create the new version as a byte-for-byte copy of that predecessor.
3. Identify the material evidence additions/qualifications belonging to the new cycle.
4. Replace/reset the **version-local header `X update` block** so that it contains only the `X update` entries for the new cycle; do not carry forward prior-version header updates.
5. Add the corresponding explicit claim-table and/or material-evidence changes.
6. Verify that cumulative predecessor evidentiary content is preserved in order except for explicitly authorized additive/corrective changes and the intentionally renewed version-local header traceability block.
7. Only after content integrity passes, propagate the new version to `CURRENT` and update canonical pointers/state as required.
8. Run the canonical validator as the final gate.

This rule prevents two distinct systematic failures: omission of a material novelty from the new version's top-level traceability, and uncontrolled accumulation of historical `X update` entries in later version headers.

## Future-session discovery instruction

**Before any future TGCV governance update, inspect `00_GOVERNANCE/` and locate this document (`GOVERNANCE_LESSONS_LEARNED_001.md`) and the active `GOVERNANCE_OPERATING_PRINCIPLES` artifact. Do not assume that either rule set is remembered from prior ChatGPT sessions.**
