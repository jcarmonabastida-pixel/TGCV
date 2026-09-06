# AUDIT — DR-020 Rust transformation candidate universe T v0.1

**Status:** COMPLETED — STRUCTURAL AUDIT EVIDENCE
**Date:** 2026-09-06
**Decision under audit:** `DR-020_Rust_Transformation_Candidate_Universe_v0.1.md`
**Audit implementation:** `src/audit_rust_candidate_universe_t_v01.py`
**Dataset:** `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

## Purpose

Verify the structural conditions required by DR-020 for construction of the candidate universe `T`, without executing `R*`, `T_acc`, resources, baseline `B`, sampling, or outcomes.

## Local execution results

The corrected audit implementation was executed twice, independently rerun without modification, against the same frozen local dataset. Both runs produced the same complete result:

```text
PACKAGE_COUNT: 91437
VERSION_COUNT: 607498
DEPENDENCY_EDGE_COUNT: 3618523
UNIQUE_DEPENDENCY_EDGE_KEYS: 3618523
DUPLICATE_DEPENDENCY_EDGE_ROWS: 0
UNIQUE_ORIGIN_TARGET_PAIRS: 3618523
CANDIDATE_COUNT: 194371905
UNIQUE_CANDIDATE_KEYS: 194371905
DUPLICATE_CANDIDATE_KEYS: 0
FUTURE_TARGET_RELEASES_EXCLUDED: 62706824
FUTURE_TIMESTAMP_VIOLATIONS_IN_T: 0
MISSING_ORIGIN_VERSION: 0
MISSING_TARGET_PACKAGE: 0
TARGET_PACKAGE_ID_MISMATCH: 0
Q_USED_FOR_MEMBERSHIP_DECISION: False
PASS_CANDIDATE_KEY_UNIQUE: True
PASS_TEMPORAL_CUTOFF: True
PASS_ORIGIN_FK: True
PASS_TARGET_PACKAGE_FK: True
PASS_TARGET_PACKAGE_CONSISTENCY: True
PASS_Q_INDEPENDENCE_BY_CONSTRUCTION: True
PASS_DETERMINISTIC_TARGET_ORDER: True
PASS_T_STRUCTURAL: True
```

## Assessment

### 1. Candidate-key uniqueness — PASS

The canonical candidate identity `(origin_version_id, target_package_id, target_version_id)` is unique in the audit result. No duplicate candidate keys were reported.

### 2. Temporal cutoff — PASS

`FUTURE_TIMESTAMP_VIOLATIONS_IN_T = 0`. The `62,706,824` future target releases are explicitly counted as excluded records rather than violations. Therefore no target release with `created_at(target_version) > created_at(origin_version)` enters `T`.

### 3. Referential integrity — PASS

No missing origin versions or target packages were found. Target package consistency also passed.

### 4. Independence from `q` / `R*` — PASS

`Q_USED_FOR_MEMBERSHIP_DECISION = False` and the audit construction does not execute the normative resolver. Candidate membership is therefore separated from accessibility selection.

### 5. Deterministic construction — PASS BY CONSTRUCTION

Target releases are indexed in deterministic timestamp/version-id order and candidate counting is performed from canonical origin-target pairs. The implementation does not depend on input row order for candidate membership.

### 6. Separation of `T` from `T_acc` — PASS

The audit constructs candidate target releases subject only to observed dependency relations and the temporal boundary. Accessibility, `R*`, resources and outcomes are explicitly excluded.

### 7. Reproducibility — PASS

A second execution of the unchanged auditor against the same frozen dataset reproduced the complete output exactly, including all counts and PASS flags. This closes the empirical repeatability criterion for DR-020.

### 8. Empty/excluded structural accounting — PASS FOR THE DEFINED AUDIT SCOPE

The audit explicitly accounts for future target releases excluded by the temporal cutoff and reports missing-origin/missing-target structural records. The candidate construction is defined over observed origin-target relation pairs; empty candidate families therefore contribute zero candidates and do not require materialization. No confirmatory experiment was executed.

## Scientific conclusion

The corrected implementation passes the structural and reproducibility gate for DR-020. The earlier `62,706,824` value was correctly reinterpreted as future target releases excluded by the temporal cutoff, not violations within `T`.

**DR-020 acceptance is now justified**, subject to recording the acceptance in the append-only Decision Log.

No confirmatory experiment is authorised by this audit. Acceptance of `T` does not accept or freeze `T_acc`, `B`, `R`, resources, sampling, or outcome.

## Provenance

This is evidence for a **NEW DECISION for EXT-1.1** and is not asserted as historical MVE/EMP-1.1 methodology.
