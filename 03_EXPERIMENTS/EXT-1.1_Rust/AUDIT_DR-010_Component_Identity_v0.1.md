# EXT-1.1 Rust — DR-010 component identity audit v0.1

**Status:** COMPLETED / EVIDENCE RECORD

## Purpose

Record the structural audit executed against the frozen local Rust dataset for verification of the proposed DR-010 component identity/domain decision.

## Dataset

ZIP: `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

The audit streamed the relevant CSV members directly from the ZIP. No extraction was performed.

## Audit result

```text
TGCV EXT-1.1 — Rust component identity audit v0.1
================================================================
ZIP: C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip

[1] SOURCE DOMAIN
source_id=3 rows: 1
  id=3 name='crates' url_root=''
PASS_SOURCE_CRATES: True

[2] PACKAGE IDENTITY
package rows: 91437
unique package ids: 91437
crate packages: 91437
package id -> name/source conflicts: 0
duplicate (source_id=3, name) rows: 0
PASS_PACKAGE_ID_STABLE: True

[3] RELEASE OBSERVATION
package_version rows: 607498
unique version ids: 607498
crate release rows: 607498
non-crate release rows: 0
version rows with missing package_id: 0
duplicate (package_id, version_str) keys: 0
rows with version.created_at < package.created_at: 0
rows with missing package/version timestamp: 0
PASS_VERSION_KEY_UNIQUE: True
PASS_VERSION_PACKAGE_FK: True
PASS_VERSION_TEMPORAL_ORDER: True

[4] DEPENDENCY REFERENCE INTEGRITY
dependency rows: 3618523
depending_version ids missing from package_versions: 0
depending_on_package ids missing from packages: 0
distinct semver strings: 12672
literal '*' semver rows: 17597
PASS_DEP_VERSION_FK: True
PASS_DEP_PACKAGE_FK: True

AUDIT CONCLUSION
PASS_STRUCTURAL_COMPONENT_IDENTITY: True
NOTE: This audit does not define T, T_acc, B, R, resources, outcome, sampling, or the exact dependency-resolution semantics.
NOTE: No dataset extraction was performed; CSV members were streamed directly from the ZIP.
NOTE: No confirmatory experiment was executed.
```

## Verification assessment

All structural conditions required by the current DR-010 proposal passed:

1. The dataset contains exactly one `source_id=3` row identified as `crates`.
2. All 91,437 package IDs are unique; all are crate packages; no package ID maps to conflicting name/source values; and no duplicate `(source_id=3, name)` identity rows were observed.
3. All 607,498 release observations are crate releases with unique version IDs, valid package references, unique `(package_id, version_str)` keys, valid package/release temporal ordering, and non-missing timestamps.
4. All 3,618,523 dependency rows have valid references to both release and package entities.
5. The observed literal `*` dependency constraint is recorded as a dataset fact only. It does not alter the normative R* semantics governed separately by DR-017.

## Decision consequence

The audit verifies that the proposed component identity can be reconstructed from pre-outcome dataset metadata and that the representation `package@version` is structurally observable while package identity remains stable across releases.

This evidence is sufficient to move DR-010 from **PROPOSED** to **ACCEPTED — NEW EXPERIMENTAL DECISION**, subject to the scope exclusions already stated in DR-010.

The audit does **not** decide or authorize:

- concrete transformation universe `T`;
- accessibility predicate or `T_acc`;
- resource variables/thresholds;
- outcome or horizon;
- sampling/exclusion;
- baseline `B`;
- `R` serialization;
- exact dependency-resolution implementation parameters left open by DR-009;
- confirmatory execution.

## Reproducibility

Audit implementation: `03_EXPERIMENTS/EXT-1.1_Rust/src/audit_rust_component_identity_v01.py`

Execution environment: local Windows environment; dataset remained local and was not uploaded.

## Governance

This evidence record supports the closure of the component-identity/domain question only. Subsequent open decisions remain governed by the fail-closed rule and must be resolved sequentially.
