# EXT-1.1 Rust — CHR-MICRO-3 Chrono-Resolution Gate v0.1

**Status:** EXECUTED — FAIL / BLOCKED ON AVAILABLE EVIDENCE
**Date:** 2026-08-30
**Parent experiment:** EXT-1.1_Rust

## Purpose

Determine whether historical package/release and dependency resolution can be reconstructed reproducibly and non-circularly, using only information available at the relevant observation time, before any full EXT-1.1 dataset extraction.

## Continuity rule

This file is part of the canonical EXT-1.1 experiment record in GitHub. The chat may elaborate the protocol, but a gate decision is not considered canonical until recorded in the repository.

## Micro-slice

- C1 — `serde@1.0.0`.
- C2 — `tokio@1.0.0`.
- C3 — `rand@0.8.0`.

Selection was made to span increasing resolution complexity and was not based on downstream outcome.

## Required reconstruction chain

`package@version → release_time → dependency constraint → historical candidate universe → resolved package@version → registry version_id → historical observations`

All resolution inputs must be available no later than the relevant observation time.

## Gate results

| Case | A Identity | B Temporal availability | C Reproducibility | D No outcome leakage | E Registry bridge | F Temporal T_acc construction |
|---|---|---|---|---|---|---|
| C1 `serde@1.0.0` | PASS | PASS for release identity; historical candidate resolution not demonstrated | OPEN | PASS | OPEN | OPEN |
| C2 `tokio@1.0.0` | PASS | PASS for release identity; historical candidate resolution not demonstrated | OPEN | PASS | OPEN | OPEN |
| C3 `rand@0.8.0` | PASS | PASS for release identity; historical candidate resolution not demonstrated | OPEN | PASS | OPEN | OPEN |

## Verdict rule

**FAIL / BLOCKED:** the currently recoverable evidence establishes release identity, chronology and dependency constraints, but does not establish reproducible historical dependency resolution from a time-indexed registry state for the three cases. The `package@version → registry version_id` bridge has also not yet been independently demonstrated for all three cases.

This is a substantive evidentiary gap, not a merely conventional choice.

## Consequence

The failure is a failure of the **current acquisition/evidence path**, not proof that the Cargo-native route is impossible.

- Full EXT-1.1 extraction remains blocked.
- EXT-1.1 FREEZE remains blocked.
- No outcome variable may be used to infer or repair the missing historical resolution.
- A new acquisition/reconstruction sub-gate is required for historical registry/index state and the version_id bridge.

## Execution evidence

Detailed execution record: `CHR-MICRO-3_EXECUTION_v0.1.md`.
