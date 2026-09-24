# TGCV — Governance and Operating Model

**Status:** ACCEPTED WORKING GOVERNANCE GUIDE  
**Purpose:** Provide a single, stable entry point to the canonical TGCV operating model, reduce operational drift, and make continuation from a new ChatGPT session fast and reproducible.

## 1. Canonical source and execution boundary

**GitHub is the canonical source of truth and governance layer for TGCV.** The canonical repository is `jcarmonabastida-pixel/TGCV`, branch `main`.

GitHub contains, as applicable:

- scientific and methodological specifications;
- governance rules and workflows;
- Decision Records and authorizations;
- frozen definitions and execution contracts;
- canonical executable code and version/commit identity;
- manifests, hashes and provenance records;
- audits, execution records and scientific-closure records;
- canonical continuity state.

**The local environment is the technical execution layer.** It is used for:

- loading the canonical state from GitHub;
- compiling or preparing authorized software;
- executing authorized technical operations;
- datasets, runtime environments and generated execution data;
- stdout/stderr captures and other local raw outputs;
- local integrity checks and diagnostics.

Local state is not an independent source of governance truth. Chat context is not a source of truth.

## 2. Normal direction of synchronization

The normal operational direction is:

**GitHub `main` → local environment → technical execution/data → canonical recording in GitHub when required by governance.**

The local repository should normally be brought into conformity with the relevant canonical GitHub state before technical work begins.

Do not treat local modifications as canonical merely because they exist or because they make an execution work.

A local code modification is an **exceptional technical intervention**, justified only when execution or diagnosis demonstrates that it is necessary or materially more effective. Such an intervention must be distinguished from the canonical implementation and handled according to the applicable governance workflow before it is relied upon as evidence.

## 3. Mandatory historical reconstruction

Before starting new work, recover the relevant historical state from GitHub.

Apply:

`00_GOVERNANCE/workflows/HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1.md`

The minimum question is:

> Has this problem, requirement, implementation, audit or experiment already been solved, partially solved, frozen, executed, accepted, blocked or superseded?

Reuse compatible prior work before recreating it.

Do not restart an experiment, redefine a semantic object, rewrite a frozen contract or implement a new version merely because the previous chat context is unavailable.

## 4. Technical execution workflow

For governed technical executions, apply:

`00_GOVERNANCE/workflows/TECHNICAL_EXECUTION_WORKFLOW_v0.1.md`

The canonical sequence is:

`recover canonical design → integrity preflight → authorized execution → primary execution audit → replay gate → final execution-result audit → scientific closure`

The workflow requires that disagreements between GitHub and local state be resolved before proceeding, and that substantive deviations from frozen execution require a new or amended governance decision.

## 5. New ChatGPT session — Carga TGCV

When a new chat is opened, the first operational command is:

**Carga TGCV**

This is a continuity operation, not a new research operation.

Apply:

`00_GOVERNANCE/CHATGPT_BOOTSTRAP.md`

The bootstrap protocol is:

1. Read `CHATGPT_BOOTSTRAP.md` from GitHub `main`.
2. Resolve and read `CANONICAL_STATE.json`.
3. Resolve and read `STATUS.md`.
4. Resolve the current RMA, Evidence→Claim Matrix, RMA traceability and IGRT status through the canonical pointers.
5. Apply the read-only bootstrap consistency validator when local execution is available.
6. Verify that canonical versions and pointers are mutually consistent.
7. If consistent, report the current state and continue directly from **Next operation**.
8. If inconsistent, stop and report `BOOTSTRAP_BLOCKED_CANONICAL_INCONSISTENCY` with the conflicting artifacts/versions.

The chat must not reconstruct project state from memory when the canonical GitHub state is available.

## 6. Operational rule for local changes

When a technical problem appears locally:

1. **First recover the canonical GitHub artifact and its governing workflow.**
2. **Then determine whether the local discrepancy is real.**
3. **Check historical GitHub work before writing or changing code.**
4. If the canonical implementation should work, diagnose the local environment rather than silently changing the implementation.
5. If a code adjustment is demonstrated to be necessary or materially more effective, make the smallest technically justified local adjustment required for the authorized operation.
6. Record the deviation and its provenance as required by the applicable governance.
7. Do not allow the local patch to redefine the canonical scientific contract.
8. Before any scientific execution, ensure the executable, inputs, configuration and relevant definitions correspond to the authorized canonical state.

## 7. Stop conditions

Stop and resolve the discrepancy when:

- GitHub and local state disagree on a governing artifact;
- an executable, dataset, configuration or hash does not match the authorized identity;
- a frozen semantic contract appears to require modification;
- historical work may already satisfy the requirement;
- execution authorization is unclear;
- a local workaround changes the scientific or methodological meaning of the operation;
- provenance cannot be established.

Never resolve a canonical contradiction by choosing whichever local state happens to work.

## 8. Separation of evidence states

Maintain the distinction between:

- **DEFINED / FROZEN**
- **IMPLEMENTED**
- **EXECUTED**
- **AUDITED**
- **ACCEPTED**
- **CONDITIONAL**
- **OPEN**
- **BLOCKED**
- **SUPERSEDED BY EXPLICIT DECISION**

A design or preflight PASS does not imply empirical execution. An execution PASS does not by itself establish a scientific, causal, predictive, universal, value or originality claim.

## 9. Relationship to detailed governance

This README is an operational index and orientation layer. It does **not** replace detailed governance artifacts.

When this README and a detailed governance artifact appear to conflict, the detailed authoritative artifact governs, and the contradiction must be investigated rather than silently resolved.

Primary references:

- `00_GOVERNANCE/CHATGPT_BOOTSTRAP.md`
- `00_GOVERNANCE/workflows/HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1.md`
- `00_GOVERNANCE/workflows/TECHNICAL_EXECUTION_WORKFLOW_v0.1.md`
- `00_GOVERNANCE/CANONICAL_STATE.json`
- `STATUS.md`

**Core operational principle:**

> **Recover from GitHub, execute locally under canonical authorization, preserve provenance, and return to GitHub for canonical continuity and governance.**