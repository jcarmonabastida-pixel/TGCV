# TGCV — Rust Ω-Primary Dataset Source and Snapshot Specification Review v0.2

**Status:** CLOSED — HISTORICAL FIGSHARE SNAPSHOT SPECIFIED / EXACT LOCAL SNAPSHOT BOUND / Ω-PRIMARY EMPIRICAL ADMISSION STILL PENDING
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_DATASET_SOURCE_AND_SNAPSHOT_SPECIFICATION_REVIEW
**Predecessor:** v0.1

## 1. Correction to v0.1

Version v0.1 incorrectly reframed the empirical route as requiring a new crates.io source/snapshot. That is superseded.

The Ω-primary Rust route uses the **already retained historical Rust dataset**, previously identified with the Figshare collection DOI `10.6084/m9.figshare.c.5983534.v1` and the 2022-09-07 snapshot.

No new crates.io acquisition is part of this route.

## 2. Exact retained candidate

Local artifact:

`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

Recorded SHA-256:

`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Archive root:

`rust_repos_2022_09_07/`

Canonical preflight: ZIP hash match PASS; archive opened PASS; required structural CSV schemas PASS.

## 3. Historical source boundary

The source boundary is the retained historical Figshare Rust corpus associated with the 2022-09-07 snapshot, not a current live registry reconstruction.

This distinction is essential for reproducibility: the scientific object is the frozen historical snapshot already retained locally, not whatever the live registry contains now.

## 4. Required provenance binding

The remaining provenance requirement is to bind, in one canonical manifest:

1. Figshare collection/item/version identity;
2. exact source archive/file identity;
3. local ZIP SHA-256;
4. archive member manifest;
5. acquisition/provenance record;
6. license/usage basis;
7. structural field inventory;
8. temporal snapshot boundary;
9. coverage and missingness semantics.

The absence of one consolidated publication-chain manifest does not justify reacquisition. It remains a documentation/verification task against the existing artifact.

## 5. Ω source boundary

Admitted primitive structural classes remain limited to package/crate identity, release/version identity, release timestamp, dependency declaration and dependency target identity/version.

No accessibility, execution, outcome, reward/value or future-trajectory variable may enter the primary construction.

## 6. Decision

**SOURCE CLASS:** HISTORICAL FIGSHARE SNAPSHOT — FROZEN CANDIDATE.

**EXACT LOCAL SNAPSHOT:** BOUND TO THE RECORDED ZIP HASH AND PRIOR PREFLIGHT.

**NEW CRATES.IO DOWNLOAD:** NOT REQUIRED / NOT PART OF THIS ROUTE.

**PROVENANCE MANIFEST:** STILL REQUIRES FINAL CONSOLIDATED VERIFICATION.

**Ω-PRIMARY EMPIRICAL ADMISSION:** NOT YET GRANTED.

**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 7. Next gate

`RUST_OMEGA_PRIMARY_DATASET_SNAPSHOT_MANIFEST_AND_PROVENANCE_REVIEW`