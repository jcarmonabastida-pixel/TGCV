# TGCV VSL Execution Authorization Gate 002

## Status

**READY — TECHNICAL FREEZE PASS; EXECUTION AUTHORIZATION PENDING FINAL PRE-RUN CHECK**

Date: 2026-09-18

## Purpose

This gate follows the valid byte-exact technical freeze established in `TGCV_VSL_FINAL_FREEZE_AUDIT_003.md`.

It does not itself generate experimental evidence and does not authorize Executor-2 to see Executor-1 outputs.

## Frozen package

Canonical package commit:

`a1e5005d4d924e0c725671bfca05506a4616e5ff`

Technical freeze: **PASS**.

Six executable-package components have been verified byte-identically between Git-stored bytes and the working tree.

## Required pre-run conditions

1. HEAD remains the frozen package commit or an explicitly governed equivalent containing identical frozen package bytes.
2. Working-tree bytes for all six package components remain SHA-256 identical to the frozen hashes.
3. Python remains 3.8.10.
4. Network access remains prohibited.
5. A and B are executed as paired within-fixture synthetic methodological executions exactly as specified.
6. No Executor-1 output, interpretation, expected direction, or result is supplied to Executor-2.
7. Executor-2 reconstruction is performed only after the independent boundary is preserved.
8. Existing invalidated execution results are not overwritten or treated as evidence.
9. New execution outputs use new result filenames and are explicitly tied to this freeze.
10. Any mismatch is a STOP condition; no reconciliation by editing the frozen package is permitted.

## Execution order

**Phase 1 — Pre-run integrity check**

Reconfirm HEAD, six SHA-256 values, Python version, network prohibition, and clean status for the six frozen components.

**Phase 2 — Executor-1 A/B execution**

Run the frozen A and B executors locally under the frozen environment. Preserve raw JSON outputs without interpretation.

**Phase 3 — Independent Executor-2 reconstruction**

Run reconstruction separately from the frozen package and specification, without access to Executor-1 outputs or interpretations.

**Phase 4 — Reconciliation audit**

Compare the independently reconstructed outputs against Executor-1 outputs. Any discrepancy is recorded as a failure/inconclusive condition according to the frozen reconstruction specification; no post-hoc editing is allowed.

## Result naming

Use new outputs, not the invalidated `_001` outputs. Recommended paths:

- `03_EXPERIMENTS/VSL/A_EXECUTION_RESULT_002.json`
- `03_EXPERIMENTS/VSL/B_EXECUTION_RESULT_002.json`

Executor-2 outputs must be separately identified and must not be mixed with Executor-1 outputs.

## Governance boundaries

This gate does not alter TGCV Core, RMA, Evidence-to-Claim Matrix, C09, VSL-SPEC-01, VSL-EXP-01, or the historical invalidation record.

## Authorization state

Current state: **NOT YET AUTHORIZED FOR EXECUTION**.

Authorization is granted only after the Phase 1 pre-run integrity check passes on the actual execution machine.
