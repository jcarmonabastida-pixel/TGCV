# TGCV — ChatGPT Bootstrap / Session Continuity

**Schema:** `TGCV-CHATGPT-BOOTSTRAP-1`
**Purpose:** provide a minimal, canonical entry point for resuming TGCV work in a new ChatGPT session.
**Source of truth:** GitHub repository `jcarmonabastida-pixel/TGCV`, branch `main`.

## Session-start protocol

When a new ChatGPT session starts with **`Carga TGCV`**:

1. Read this file from `main`.
2. Resolve and read `00_GOVERNANCE/CANONICAL_STATE.json`.
3. Resolve and read `STATUS.md`.
4. Resolve the current RMA, Evidence→Claim Matrix, RMA traceability and governance operating principles through the pointers in `CANONICAL_STATE.json`; also resolve `STATUS.md`, the scientific asset registry and the canonical validators.
5. Run or otherwise apply the read-only validators `00_GOVERNANCE/tools/validate_current_state.py` and `00_GOVERNANCE/tools/validate_chatgpt_bootstrap.py` when local execution is available.
6. Check that the declared versions, stable aliases, versioned artifacts and pointers are mutually consistent.
7. IGRT (Integrated Governance Readiness Tracker) is **not an established canonical TGCV artifact or required governance layer**. No IGRT pointer, status file or validation gate is expected. Its absence is not a bootstrap failure. If IGRT is proposed in the future, it must first be established through an explicit governance decision and added to the canonical schema and validators; do not infer or fabricate an IGRT state.
8. If the actual canonical pointers and versions are consistent, report the current state and continue from **Next operation** without reconstructing historical context.
9. If they are inconsistent, report `BOOTSTRAP_BLOCKED_CANONICAL_INCONSISTENCY`, identify the exact conflicting artifacts/versions, and do not silently choose one.

## Canonical repository

- Repository: `jcarmonabastida-pixel/TGCV`
- Branch: `main`
- Canonical rule: GitHub `main` is the authoritative continuity source.

## Authoritative state graph

`CANONICAL_STATE.json → STATUS.md → current RMA pointer/master → current Evidence→Claim Matrix pointer/artifact → RMA traceability → current-state validator → bootstrap validator`

This bootstrap is an index and session-entry protocol. It does **not** replace any authoritative governance artifact and must not be treated as an independent scientific source of truth.

## Current operational routing

The bootstrap must obtain the live values below from the authoritative artifacts at session start; they are recorded here only as routing labels and must not override those artifacts.

- Current scientific priority: `C10 — causal ΔT_acc → ΔV`
- Current next operation: recover and consolidate the canonical C10 methodological state before any new empirical execution or dataset search.
- Execution authorization for that operation: design/recovery only; no execution authorization.

## Continuity rules

- Do not reconstruct project state from ChatGPT memory when canonical GitHub state is available.
- Do not repeat closed tests, experiments or governance operations merely because the previous chat is unavailable.
- Do not infer that an operation is authorized from its description; use the authoritative governance state.
- Do not modify governance artifacts unless the current workflow explicitly authorizes the modification.
- Local execution is for validation or explicitly authorized operations; GitHub `main` remains canonical.
- On any canonical contradiction, stop at the contradiction and diagnose it before continuing.

## Bootstrap integrity

This file is intentionally small. It should remain stable and operational. Dynamic state should be generated or verified from the authoritative artifacts rather than manually duplicated here.

**Validators:** `00_GOVERNANCE/tools/validate_current_state.py` and `00_GOVERNANCE/tools/validate_chatgpt_bootstrap.py` (read-only; do not modify governance).  
**IGRT status:** `NOT_ESTABLISHED / NOT_REQUIRED_BY_CURRENT_CANONICAL_SCHEMA`.

**Bootstrap command:** `Carga TGCV`
