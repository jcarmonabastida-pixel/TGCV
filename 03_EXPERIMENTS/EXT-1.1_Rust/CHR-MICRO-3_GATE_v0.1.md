# EXT-1.1 Rust — CHR-MICRO-3 Chrono-Resolution Gate v0.1

**Status:** OPEN — execution pending
**Date:** 2026-08-30
**Parent experiment:** EXT-1.1_Rust

## Purpose

Determine whether historical package/release and dependency resolution can be reconstructed reproducibly and non-circularly, using only information available at the relevant observation time, before any full EXT-1.1 dataset extraction.

## Continuity rule

This file is part of the canonical EXT-1.1 experiment record in GitHub. The chat may elaborate the protocol, but a gate decision is not considered canonical until recorded in the repository.

## Micro-slice

Three crates must be evaluated:

- C1 — simple historical dependency-resolution case.
- C2 — intermediate case with multiple compatible candidate releases.
- C3 — difficult case with potential temporal ambiguity or dependency-history evolution.

Selection must not be based on downstream outcome or later success.

## Required reconstruction chain

`package@version → release_time → dependency constraint → historical candidate universe → resolved package@version → registry version_id → historical observations`

All resolution inputs must be available no later than the relevant observation time.

## Gates

### A — Identity

`package@version` identifies one unambiguous release.

### B — Temporal availability

For every resolved dependency release:

`release_time <= resolution_time`

A release that did not yet exist cannot be selected retrospectively.

### C — Reproducibility

Running the same resolution against the historical state at time `t` must reproduce the same result.

### D — No outcome leakage

Resolution must not use downloads, popularity, adoption, survival, success, or any outcome-derived variable observed after `t`.

### E — Registry bridge

A reproducible identifier bridge must exist:

`package@version → registry version_id`

The bridge may use a modern lookup only as an identity mapping; it must not inject retrospective temporal or outcome information.

### F — Temporal T_acc construction

The historical graph must support construction of `T_acc,t` from information available at `t`, and where applicable comparison with `T_acc,t+1` to obtain `ΔT_acc`.

## Verdict rule

- **PASS:** A–F pass for all three cases.
- **CONDITIONAL PASS:** only an explicit, non-substantive convention is required and does not alter historical observability.
- **FAIL:** any substantive use of future information, retrospective resolution, irreproducibility, identity ambiguity, or inability to construct the required temporal object.

No full EXT-1.1 extraction or FREEZE is authorized solely by this protocol. Execution evidence and the final verdict must be recorded separately.

## Execution record

| Case | A | B | C | D | E | F | Notes |
|---|---|---|---|---|---|---|---|
| C1 | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | |
| C2 | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | |
| C3 | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | |

**Overall verdict:** PENDING

## Next authorized step

Execute CHR-MICRO-3 on the three selected cases, preserve the evidence needed to reproduce each gate, and record the verdict before proceeding to minimal extraction or EXT-1.1 freeze.
