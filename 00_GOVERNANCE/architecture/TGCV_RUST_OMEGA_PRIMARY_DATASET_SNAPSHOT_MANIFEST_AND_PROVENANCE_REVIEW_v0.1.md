# TGCV — Rust Ω-Primary Dataset Snapshot Manifest and Provenance Review v0.1

**Status:** CLOSED — SNAPSHOT MANIFEST CONDITIONALLY FROZEN / PROVENANCE BOUND TO EXISTING ARTIFACT / Ω-PRIMARY ADMISSION STILL PENDING
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_DATASET_SNAPSHOT_MANIFEST_AND_PROVENANCE_REVIEW

## 1. Canonical snapshot identity

Historical source: Figshare Rust corpus associated with collection DOI `10.6084/m9.figshare.c.5983534.v1`.

Snapshot: 2022-09-07.

Local archive: `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`.

Recorded SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`.

Archive root: `rust_repos_2022_09_07/`.

These identifiers are inherited from the previously executed canonical real-data preflight. This gate does not recompute the local hash.

## 2. Structural manifest

Previously verified structural members include:

- `dumps/postgresql/data/package_versions.csv`
- `dumps/postgresql/data/package_dependencies.csv`

Verified schemas:

`package_versions(id, package_id, version_str, created_at)`

`package_dependencies(depending_version, depending_on_package, semver_str)`

These members provide the primitive structural basis currently admitted for the Ω candidate.

## 3. Temporal boundary

The retained real-data route uses `DR-035-v0.1-ADJACENT-CREATED-AT` with `H=1` as recorded by the prior preflight.

Temporal construction must remain independent of accessibility, execution, downstream outcome, reward/value and future trajectory.

## 4. Provenance chain

The current canonical chain is:

`Figshare historical Rust corpus → 2022-09-07 snapshot → retained ZIP → verified SHA-256 → verified archive members/schema → governed Ω structural processing boundary`.

The external publication-chain metadata are not independently re-fetched in this gate. Therefore the provenance is **bound conditionally to the existing retained artifact**, rather than represented as a newly audited external publication record.

## 5. Coverage and missingness

The frozen semantics remain:

- `OBSERVED_PRESENT`
- `OBSERVED_ABSENT_COMPLETE`
- `UNKNOWN_MISSING`
- `OUT_OF_SCOPE`

Presence of the structural members does not by itself establish complete row-level coverage of every historical transformation. Absence cannot be interpreted as removal unless completeness is independently demonstrated.

## 6. Information firewall

The manifest permits only the frozen structural classes required for Ω construction.

Prohibited inputs remain:

`T_acc`, Reach, `ΔReach`, execution/accessibility status, downstream outcome, reward/utility/value, future trajectory, and variables derived from them.

The prior preflight recorded these prohibited quantities as not constructed/read.

## 7. Decision

**SNAPSHOT MANIFEST:** CONDITIONALLY FROZEN.

**LOCAL BYTE IDENTITY:** PREVIOUS PREFLIGHT PASS.

**STRUCTURAL SCHEMA:** PASS.

**PROVENANCE BINDING:** CONDITIONAL TO EXISTING RETAINED ARTIFACT.

**Ω-PRIMARY DATASET ADMISSION:** NOT YET GRANTED.

**NEW DOWNLOAD:** NOT REQUIRED / NOT PERMITTED AS SUBSTITUTE.

**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 8. Next gate

`RUST_OMEGA_PRIMARY_OBSERVATIONAL_UNIVERSE_U_CONSTRUCTION_REVIEW`