# TGCV — Rust Ω-Primary Dataset Identifiability and Privacy Admission Review v0.2

**Status:** CLOSED — EXISTING LOCAL SNAPSHOT CONDITIONALLY ADMITTED / IDENTIFIABILITY-PRIVACY REVIEW PASSED FOR GOVERNED PROCESSING
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_DATASET_IDENTIFIABILITY_AND_PRIVACY_ADMISSION_REVIEW
**Predecessor:** v0.1

## 1. Reconciliation

The v0.1 decision treated this gate as preceding acquisition. That is no longer the applicable operational state: the exact historical Rust snapshot is already retained locally and has passed the canonical real-data byte/schema preflight.

No new acquisition is required or permitted.

## 2. Dataset identity

Local candidate: `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`.

Recorded SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`.

The dataset is treated as a historical Rust corpus/snapshot, not as a fresh crates.io download.

## 3. Identifiability and privacy boundary

The retained structural classes for the Ω route are package/crate identity, release/version identity, release timestamp, dependency declaration, and dependency target identity/version.

These fields are structural software-ecosystem metadata. This review does not infer absence of every possible sensitive field in the entire archive merely from the two structural CSV schemas already inspected.

Accordingly, processing is limited to the explicitly admitted structural members and fields needed for the Ω construction. Any additional field requires separate semantic classification before use.

## 4. Minimisation

The Ω route shall not ingest or use downstream activity, accessibility, execution results, outcome, reward/value, future trajectory, or variables derived from them.

Only the minimum primitive structural fields required for U_t, canonicalisation, candidate relations and κ may enter the primary construction.

## 5. Repository handling

The dataset bytes remain outside GitHub. GitHub stores the governance record, hashes, manifests, protocols and derived artifacts, not the large source archive.

The local snapshot must not be silently replaced by a different publication, revision or newly downloaded corpus.

## 6. Decision

**IDENTIFIABILITY/PRIVACY GOVERNANCE:** PASS FOR THE DEFINED STRUCTURAL PROCESSING BOUNDARY.

**LOCAL SNAPSHOT:** RETAINED.

**NEW DOWNLOAD:** NOT REQUIRED / NOT PERMITTED AS A SUBSTITUTE.

**Ω-PRIMARY EMPIRICAL ADMISSION:** NOT YET GRANTED.

**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 7. Next gate

`RUST_OMEGA_PRIMARY_DATASET_ADMISSION_PACKAGE_REVIEW`