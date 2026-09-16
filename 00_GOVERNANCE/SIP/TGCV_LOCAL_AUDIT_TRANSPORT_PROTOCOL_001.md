# TGCV — Local Audit / Chat Transport Protocol — 001

**Status:** OPERATING PROCEDURE — ANALYSIS INFRASTRUCTURE, NOT GOVERNANCE-NORMATIVE  
**Date:** 2026-09-16  
**Purpose:** Establish the standard transport pattern for large local scientific audits so that PowerShell/local execution remains the computational layer, while ChatGPT receives only compact, decision-relevant summaries and explicitly selected exceptions.

## 1. Rationale

Large TGCV datasets, frozen source packages, CSV inventories and audit dumps must not be transported wholesale through the conversation interface. Doing so creates unnecessary quota consumption, excessive copy/paste burden, and avoidable risk of truncation or loss of context.

The canonical pattern is therefore:

`frozen local source → local audit → complete local artifact → compact summary → ChatGPT decision → persisted scientific/governance artifact`

The conversation is an analytical control channel, not the primary storage or transport layer for raw experimental data.

## 2. Separation of responsibilities

### Local environment

The local environment is responsible for:

- accessing frozen source packages;
- executing scripts and computations;
- calculating hashes and integrity checks;
- scanning complete datasets;
- producing complete audit artifacts;
- preserving detailed exceptions and record-level evidence;
- generating compact deterministic summaries.

### GitHub

GitHub is the canonical repository for:

- protocols;
- executable audit scripts when they are sufficiently stable;
- frozen-source manifests;
- scientific execution records;
- audit summaries and exception artifacts when appropriate;
- governance and evidence records.

GitHub is not required to contain every transient local dump.

### ChatGPT

The conversation should normally receive only:

- hashes;
- counts;
- grouped classifications;
- gate-relevant statuses;
- small exception tables;
- selected record-level examples when required to resolve ambiguity;
- methodological decisions and their rationale.

Raw datasets and multi-thousand-line command outputs should remain local unless a specific record-level inspection is necessary.

## 3. Two-level audit output

Every large audit should produce at least two outputs:

### A. Complete audit artifact

A local, deterministic artifact containing the full scan and sufficient detail for later inspection or reproduction.

Naming convention:

`<CASE>_<AUDIT>_AUDIT_<NNN>.txt`

This artifact need not be pasted into the conversation.

### B. Compact summary artifact

A small machine-generated summary containing only decision-relevant aggregates.

Naming convention:

`<CASE>_<AUDIT>_SUMMARY_<NNN>.txt`

The summary should normally contain:

- total records scanned;
- records classified by status/pattern;
- minimum and maximum years where relevant;
- counts of explicit temporal-risk patterns;
- unresolved/ambiguous counts;
- candidate clean-subset status;
- preliminary gate-relevant status, clearly marked as analytical rather than governance-final.

## 4. Exception funnel

Record-level inspection follows an exception funnel rather than full-output transfer:

`complete dataset → automated classification → aggregate summary → exceptional patterns → small targeted sample → methodological decision`

The audit should first identify patterns and counts. Only ambiguous or decision-critical cases should be promoted to record-level inspection.

A large class of records must not be copied into the conversation merely because it exists.

## 5. Temporal-audit rule

For temporal non-leakage audits, automated classification should distinguish at minimum:

- `CLEAN / NOT FLAGGED`;
- `RETROSPECTIVE / HISTORICAL DEPENDENCY`;
- `FUTURE INFORMATION / EXPLICIT LEAKAGE`;
- `PLANNING_OR_LEGAL_REQUIRES_DATE_CHECK`;
- `UNKNOWN / REQUIRES_REVIEW`.

These classifications are audit flags, not semantic conclusions. A record may be reclassified after inspection of its provenance and temporal availability.

## 6. Non-substitution rule

Automated summaries must not silently translate empirical variables into TGCV constructs.

In particular, an audit may report that a variable appears to describe:

- observed realization;
- potential;
- technical constraint;
- economic parameter;
- planning/legal condition;
- historical reconstruction;

but it must not automatically label that variable as `T_acc`, `ΔT_acc`, or `Pτ`.

Semantic assignment remains an analytical decision governed by the relevant TGCV protocol.

## 7. Reproducibility requirements

A reusable audit script should:

1. identify its frozen input path or package identity;
2. report the source hash when available;
3. avoid modifying the frozen source;
4. write complete and summary outputs separately;
5. use deterministic classification rules;
6. report unresolved cases rather than silently discarding them;
7. preserve enough metadata to reproduce the audit;
8. distinguish analytical preliminary status from final gate closure.

## 8. Communication rule

When an audit produces a very large output, the operator should **not** paste the complete output into ChatGPT by default.

Instead:

1. run the complete audit locally;
2. inspect the compact summary;
3. paste the summary into the conversation;
4. if required, run a second targeted command against only the exceptional class;
5. paste only that compact exception summary;
6. make the methodological decision;
7. persist the resulting decision and evidence in the appropriate TGCV repository artifact.

## 9. Relation to scientific validity

This transport protocol is an infrastructure/control procedure. It does not increase evidential strength merely by existing.

A compact summary is valid for decision-making only insofar as the underlying complete local audit is deterministic, preserved, and reproducible.

Where a scientific claim depends on individual records, the summary must not substitute for the underlying evidence. The protocol instead determines how that evidence is surfaced efficiently.

## 10. Current application to MT-4 / MT4-5

For the current historical electricity-system transfer test, the next local audit should inspect `Buildrates`, `Potential_annual`, and `Potential_installed` together and produce:

- one complete temporal audit;
- one compact summary;
- one exception artifact containing only ambiguous or decision-critical patterns.

The MT4-5 decision must be based on the complete local audit, while the conversation should receive the compact summary and only the minimum exception evidence required to resolve the gate.

The protocol does **not** predetermine whether MT4-5 will PASS, BOUNDED PASS, FAIL, or INVALID/REJECTED.

## 11. Governance boundary

This procedure does not modify:

- TGCV Core;
- RMA;
- Evidence-to-Claim Matrix;
- C09 status;
- C10 status;
- C11 transversal-validity status;
- C12 superiority status;
- C16 methodological/originality status;
- the open `ΔT_acc → Value` layer.

Any scientific or governance consequence must be recorded separately after the relevant audit is closed.

**Current status:** PROTOCOL PERSISTED — INFRASTRUCTURE PROCEDURE ACTIVE — NO SCIENTIFIC GATE MODIFIED.
