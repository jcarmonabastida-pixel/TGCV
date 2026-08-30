# EXT-1.1 Rust — HIAR Gate v0.1

**HIAR:** Historical Index Archive Recovery Gate
**Date:** 2026-08-30
**Status:** EXECUTED — PARTIAL PASS / ROUTE OPEN
**Parent:** EXT-1.1_Rust
**Predecessor:** HRSV v0.1 (FAIL/BLOCKED)

## Purpose
Determine whether an independently auditable historical archive exists that can recover registry states required by CHR/HRSV without using retrospective outcome information.

## Finding
The official `rust-lang/crates.io-index-archive` repository exists specifically to preserve historical crates.io index snapshots after index-history squashes. The Rust crates.io team documented that historical snapshot branches were moved from the main index repository into this archive repository. The archive currently exposes protected snapshot branches including:

- `snapshot-2018-09-26`
- `snapshot-2020-03-25`
- `snapshot-2020-08-04`
- `snapshot-2020-11-20`
- `snapshot-2021-05-05`
- later snapshots through 2026.

This directly resolves the acquisition assumption that caused HRSV-A to fail: historical registry states are not necessarily lost; they are preserved as dated snapshot branches.

## Case alignment

The original CHR cases used release-time cutoffs (serde 2017-04-20, tokio 2020-12-23, rand 2020-12-18). No archive snapshot exists exactly at those dates. Therefore a snapshot must not be treated as if it represented the release-time state.

A valid reconstruction can instead use an explicitly declared **snapshot-aligned observation cutoff**, provided the experimental event being represented is defined at that cutoff and all inputs are restricted to that snapshot. Candidate cutoffs are:

- C1 `serde@1.0.0`: snapshot `2018-09-26` (release predates snapshot).
- C2 `tokio@1.0.0`: snapshot `2021-05-05` (release predates snapshot).
- C3 `rand@0.8.0`: snapshot `2021-05-05` (release predates snapshot).

This is a methodological redesign of the micro-slice timing, not a retrospective substitution of data. It requires an explicit CHR amendment before execution.

## Evidence

The archive branch listing demonstrates the dated snapshots. Direct access to the `serde` file on `snapshot-2018-09-26` and the `tokio` file on `snapshot-2021-05-05` confirms that the archived branches contain crate-index records with release/version metadata and dependency declarations.

## Verdict

**HIAR = PARTIAL PASS / ROUTE OPEN.**

The archive-recovery problem is no longer a dead end. A historical registry-state source exists. However, HIAR does not by itself pass HRSV or CHR because the existing micro-slice cutoffs were release-time cutoffs and no exact-date snapshot exists for them.

## Next authorized step

Amend CHR-MICRO-3 to a snapshot-aligned protocol with explicit observation times, then execute HRSV against the corresponding archive branches. The amendment must preserve the temporal rule: no information after the declared snapshot cutoff may enter candidate-universe or resolution reconstruction.

**EXT-1.1 FREEZE remains BLOCKED.**
