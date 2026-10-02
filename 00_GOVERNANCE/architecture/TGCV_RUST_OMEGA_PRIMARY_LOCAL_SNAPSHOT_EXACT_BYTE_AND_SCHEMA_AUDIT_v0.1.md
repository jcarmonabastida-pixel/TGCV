# TGCV — Rust Ω-Primary Local Snapshot Exact Byte and Schema Audit v0.1

**Status:** CLOSED — EXISTING SNAPSHOT BYTE/S CHEMA PREFLIGHT PASS / PROVENANCE AND Ω ADMISSION STILL OPEN  
**Date:** 2026-10-02  
**Gate:** RUST_OMEGA_PRIMARY_LOCAL_SNAPSHOT_EXACT_BYTE_AND_SCHEMA_AUDIT  
**Predecessor:** TGCV_RUST_OMEGA_PRIMARY_DATASET_SNAPSHOT_AND_PROVENANCE_RECONCILIATION_v0.1

## 1. Objective

Determine whether the already-retained local Rust ZIP has sufficient canonical evidence for exact byte identity and structural schema admission under the Ω-primary route, without downloading, replacing, or executing the dataset.

## 2. Existing byte identity

The prior canonical real-data preflight records:

- Local artifact: `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`
- SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- Expected SHA-256 matched: **YES**
- ZIP opened successfully: **YES**

This gate does not recompute the hash against the user's current local filesystem. It reuses the previously executed and canonically recorded byte-level preflight result.

## 3. Exact structural members verified by preflight

The prior preflight records the following exact archive members:

- `rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv`
- `rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv`

Schemas:

### package_versions.csv

`id, package_id, version_str, created_at`

**Schema result: PASS.**

### package_dependencies.csv

`depending_version, depending_on_package, semver_str`

**Schema result: PASS.**

These two structures provide candidate primitive sources for:

- transformation/version identity observations;
- release temporal ordering;
- dependency relations.

They do not, by themselves, establish the complete Ω tuple or its empirical irreducibility.

## 4. Ω information-firewall compatibility

The prior preflight explicitly recorded:

- `T_acc_constructed = false`
- `delta_tacc_computed = false`
- `Reach_computed = false`
- `Trajectory_computed = false`
- `future_activity_read = false`
- `outcome_read = false`
- `predictive_metrics = false`
- `sampling = false`
- `real_dataset_execution = false`

Therefore the existing preflight provides positive evidence that these prohibited downstream quantities were not used in establishing the retained structural input package.

## 5. Decision

**EXACT BYTE IDENTITY:** PASS — based on the previously executed canonical preflight.

**REQUIRED STRUCTURAL MEMBERS:** PASS.

**CSV SCHEMAS:** PASS.

**Ω INFORMATION-FIREWALL PRECONDITION:** PASS at preflight level.

**CURRENT Ω EMPIRICAL ADMISSION:** NOT GRANTED.

The audit establishes that the existing local artifact is not a missing dataset and does not require reacquisition. It also establishes a bounded primitive structural basis for the Ω route.

It does **not** yet establish:

- complete source/snapshot provenance;
- complete coverage/completeness;
- a frozen transformation canonicalisation implementation;
- a frozen relation vocabulary/completeness rule;
- longitudinal correspondence `κ`;
- state-reducibility discrimination;
- empirical Ω-primary admission.

## 6. Operational prohibition

No new Rust download is permitted for this gate.

No scientific execution is authorized by this gate.

No Core, Evidence→Claim Matrix v1.44, or RMA v3.37 change is justified.

## 7. Next gate

`RUST_OMEGA_PRIMARY_SNAPSHOT_PROVENANCE_AND_COVERAGE_ADMISSION_REVIEW`
