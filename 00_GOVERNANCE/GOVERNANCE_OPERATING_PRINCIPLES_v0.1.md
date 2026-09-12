# TGCV — Governance Operating Principles v0.1

**Status:** CURRENT / OPERATIVE  
**Date:** 2026-09-12  
**Purpose:** prevent governance maintenance from creating artificial scientific stages and keep governance effort subordinate to research progression.

## GPO-01 — Scientific-state primacy
Governance work must be driven by substantive scientific or methodological state changes: claim status, gate status, evidence status, decision status, falsification status, or an explicitly authorized experimental state transition.

## GPO-02 — No artificial scientific states
A documentation-only change that does not alter a substantive scientific or methodological state must not be represented as a new scientific phase, claim transition, promotion, experiment, or research decision.

## GPO-03 — Maintenance is subordinate
Pointer repair, formatting, metadata alignment, synchronization, changelog maintenance and similar integrity operations are governance maintenance. They may restore consistency, but do not by themselves constitute scientific progress.

## GPO-04 — Atomic propagation of substantive changes
When a substantive state does change, the minimum necessary current-state artifacts must be propagated as one coherent governance update. Unrelated intermediate governance states should not be created.

## GPO-05 — Validator scope
The current-state validator verifies structural and semantic integrity of the canonical governance chain. It must not require a new scientific state merely because maintenance has occurred.

## GPO-06 — Routing rule
After a governance maintenance closure with no substantive state change, the workflow must return directly to the next pending scientific or methodological operation.

## GPO-07 — Historical immutability
Governance maintenance must not rewrite historical evidence or historical closure records merely to make current-state pointers consistent.

## GPO-08 — Cumulative evidence-matrix preservation
The Evidence-to-Claim Matrix is a cumulative evidence-control artifact, not a summary dashboard. Every current version must preserve the predecessor's claim schema, material evidence descriptions, evidence basis, interpretation boundaries and next requirements, while adding or explicitly qualifying new material evidence. Columns or substantive evidence content must not be silently removed or compressed into a summary-only representation.

## GPO-09 — Current/versioned matrix identity
The stable `EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` alias and the versioned current matrix artifact must contain the same complete matrix content. The stable alias must never become a reduced or simplified derivative of the versioned artifact.

## GPO-10 — Matrix schema integrity is a validator invariant
The current-state validator must detect loss of the required Evidence-to-Claim Matrix columns and divergence between the stable current alias and its versioned current artifact. A governance-current-state PASS is not sufficient if matrix evidence richness has been silently degraded.
