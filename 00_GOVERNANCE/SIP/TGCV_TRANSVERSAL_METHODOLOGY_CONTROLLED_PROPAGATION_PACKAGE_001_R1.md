# TGCV — Transversal Methodology Controlled Propagation Package 001-R1

**Package ID:** `TGCV-TM-CPP-001-R1`  
**Predecessor:** `TGCV-TM-CPP-001`  
**Date:** 2026-09-17  
**Status:** **FROZEN — EXECUTION NOT PERFORMED**  
**Purpose:** controlled reconciliation of the frozen propagation package after pre-execution target-identity verification.

## 1. Reconciliation trigger

`TGCV-TM-CPP-001` was correctly blocked before execution because its frozen target list contained two non-canonical path identities:

- RMA target frozen as `00_GOVERNANCE/RMA/TGCV_RESEARCH_MASTER_ARCHITECTURE_v3.35.md`; canonical repository artifact is `00_GOVERNANCE/rma/TGCV_RMA_v3.35.md`.
- RMA traceability target frozen as `00_GOVERNANCE/RMA_TRACEABILITY_CURRENT.md`; canonical repository artifact is `00_GOVERNANCE/rma/TGCV_RMA_traceability_current.csv`.

The first inconsistency has now been independently confirmed against `CANONICAL_STATE` and current RMA traceability. The second was already established during the same pre-execution inspection. The predecessor package is preserved immutable; this R1 package supersedes it for execution.

## 2. Frozen canonical targets

Only the following five targets are authorized:

**T1 — RMA current operative artifact**  
`00_GOVERNANCE/rma/TGCV_RMA_v3.35.md`

**T2 — Evidence→Claim Matrix current alias**  
`00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md`

**T3 — RMA traceability current artifact**  
`00_GOVERNANCE/rma/TGCV_RMA_traceability_current.csv`

**T4 — STATUS**  
`00_GOVERNANCE/STATUS.md`

**T5 — CANONICAL_STATE**  
`00_GOVERNANCE/CANONICAL_STATE.json`

No other governance file is a propagation target.

## 3. Scientific scope — unchanged from CPP-001

The package permits only controlled propagation of the candidate methodology extraction:

- M0–M4: propagable as candidate methodological rules;
- M5–M6: propagable as bounded methodological rules;
- M7: propagable as candidate methodological rule;
- M8: propagable as boundary rule;
- M9 `ΔT_acc → ΔV`: remains OPEN and is not propagated as an established rule.

No TGCV Core primitive, relation, threshold or falsification criterion may be changed.

No claim-level status may be upgraded by this package. Existing claim statuses, including C09 `PASS — BOUNDED EMPIRICAL CAUSAL SUPPORT`, must remain unchanged.

The seven non-substitution controls from CPP-001 remain mandatory:

1. observed transformation ≠ accessible transformation;
2. eligibility/administrative condition ≠ `Pτ` unless ex-ante admissibility is established;
3. structural/treatment/take-up/adoption change ≠ `ΔT_acc` without explicit accessibility reconstruction;
4. longitudinal variable match ≠ TGCV trajectory definition;
5. outcome ≠ TGCV Value automatically;
6. temporal association ≠ causal effect;
7. domain-specific semantic variables ≠ TGCV primitives.

## 4. Version and pointer policy

- Historical artifacts remain immutable.
- T1 is the current operative RMA v3.35 artifact already reconciled internally to Matrix v1.12; no new RMA version is created solely for this propagation.
- T2 must remain the complete current Matrix alias resolving to v1.12; it must not become a simplified derivative.
- T3 must preserve the canonical current traceability structure and record any resulting current-state changes consistently.
- T4 and T5 may be changed only as required to maintain the canonical current-state chain.
- No silent path substitution is permitted outside the frozen targets above.

## 5. Required execution order

1. Verify T1–T5 exist at the exact frozen paths and match the canonical current-state versions before writing.
2. Inspect current contents and preserve all cumulative evidence and existing claim statuses.
3. Apply only the controlled methodology propagation required by M0–M8.
4. Update traceability/pointers only where directly required by the propagation.
5. Validate the canonical chain:
   `CANONICAL_STATE → RMA → Evidence→Claim Matrix → RMA traceability → STATUS → validator`.
6. Verify that M9 remains open and that no Core or claim-level status has changed.
7. Record the final execution commit and resulting versions.

## 6. Abort conditions

Execution must abort before any write if:

- any exact frozen target is absent;
- current version identity differs from the canonical state unexpectedly;
- Matrix v1.12 cumulative content cannot be preserved;
- a proposed change would alter Core ontology or claim status;
- M9 would be represented as established methodology;
- a target outside T1–T5 would need modification;
- pointer or traceability validation fails.

## 7. Freeze decision

`TGCV-TM-CPP-001-R1` is **FROZEN — EXECUTION NOT PERFORMED**.

It is the sole authorized successor package for the execution of this controlled propagation. `TGCV-TM-CPP-001` remains immutable as the historical predecessor and is not to be executed.

**Execution authorization:** pending separate explicit execution instruction.
