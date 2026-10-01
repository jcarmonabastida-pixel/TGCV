# TGCV — Rust Ω-Primary Dataset Source and Snapshot Specification Review v0.1

**Status:** CLOSED — SOURCE CLASS SPECIFIED / EXACT SNAPSHOT NOT FROZEN
**Date:** 2026-10-01
**Gate:** RUST_OMEGA_PRIMARY_DATASET_SOURCE_AND_SNAPSHOT_SPECIFICATION_REVIEW
**Predecessor:** RUST_OMEGA_PRIMARY_DATASET_ADMISSION_PACKAGE_REVIEW_v0.1

## 1. Purpose

Specify the authoritative Rust source class and the exact requirements for freezing a reproducible observational snapshot, without acquiring or processing dataset bytes at this gate.

## 2. Source class

The retained candidate source class is the public crates.io registry/index ecosystem. The official crates.io documentation states that the package index contains metadata required for Cargo dependency resolution, including published versions and dependencies, and that the index is available through both the sparse HTTP protocol and the Git index. citeturn0search0turn0search5

The official crates.io architecture documentation also states that crate files are immutable once published and that the registry maintains index metadata including versions, dependencies and checksums. citeturn0search2

These facts support source suitability at the **source-class** level. They do not constitute admission of a particular dataset snapshot.

## 3. Required snapshot identity

A future admitted snapshot must identify, at minimum:

- authoritative source endpoint(s);
- protocol used (sparse or Git index, or another explicitly justified official source);
- snapshot date/time and temporal cutoff policy;
- exact source revision or equivalent immutable snapshot identifier;
- complete coverage scope;
- field/schema version where applicable;
- cryptographic manifest of all retained inputs or of the exact immutable source objects used;
- provenance record linking every derived observation to its source;
- licensing/terms and processing basis;
- completeness and missingness assessment.

## 4. Preferred source boundary for Ω construction

For the candidate Ω route, the primary observational source should be registry/index metadata containing package identity, version identity, dependency declarations and associated temporal metadata where retained.

Crate source archives may be used only if a separately frozen rule establishes that they are necessary for a primitive Ω field. They must not be introduced merely because they make a downstream relation easier to reconstruct.

## 5. Snapshot rule

The future snapshot must be frozen before outcome-linked analysis. A temporal cutoff must be defined independently of accessibility, execution, success/failure, downstream outcome, reward/value/utility and future trajectory.

The same snapshot construction protocol must be applied to adjacent snapshots t and t+1.

## 6. Integrity rule

Git commit identity alone is not a substitute for the required byte-level manifest when the scientific object depends on exact bytes. The admission package must retain cryptographic hashes for the actual source objects used by the pipeline.

Where the source exposes immutable version checksums, those checksums may be retained as source metadata, but they do not replace the manifest of the exact admitted input set.

## 7. Current decision

**SOURCE CLASS: CONDITIONALLY ACCEPTABLE FOR FURTHER ADMISSION WORK.**

**EXACT DATASET SNAPSHOT: NOT FROZEN.**

No dataset bytes are downloaded or processed by this gate.

## 8. Architectural status

This specification does not establish Ω-primary empirically. It only fixes the source/snapshot requirements needed before data admission.

Ω_T,t = (U_t, ≡_T, R_t) remains a candidate architectural object.
T_acc remains derived from Ω and current conditions.
Reach and ΔReach remain derived quantities.

Core remains unchanged. Evidence→Claim Matrix remains v1.44. RMA remains v3.37.

## 9. Next gate

`RUST_OMEGA_PRIMARY_DATASET_SNAPSHOT_MANIFEST_AND_PROVENANCE_REVIEW`