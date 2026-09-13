# TGCV — C09 Pre-Execution Integrity Capture 001

**Status:** `PREFLIGHT REQUIRED — SCIENTIFIC EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Bundle:** `C09_OPERATIONAL_BUNDLE_001`
**Purpose:** define the local integrity capture required before corrected execution authorization.

## 1. Preconditions

The C09 operational bundle has been constructed and its design remains controlled. The controlled-domain audit establishes design admissibility, but not scientific causal success.

The frozen bundle components are:

- `03_EXPERIMENTS/C09_OPERATIONAL_BUNDLE_001/fixture.json`
- `03_EXPERIMENTS/C09_OPERATIONAL_BUNDLE_001/EXECUTION_SPEC.md`
- `03_EXPERIMENTS/C09_OPERATIONAL_BUNDLE_001/execute_c09_bundle_001.py`
- `03_EXPERIMENTS/C09_OPERATIONAL_BUNDLE_001/HASH_MANIFEST.md`

## 2. Mandatory local capture

Before Executor-1 is authorized, the local environment must independently establish:

1. exact checkout commit containing the frozen bundle;
2. SHA-256 of every bundle component;
3. comparison of local SHA-256 values with the frozen manifest;
4. Python interpreter version and platform/runtime fingerprint;
5. exact executor source hash;
6. fixture/spec/hash-manifest source hashes;
7. working-tree cleanliness for all bundle components;
8. confirmation that no execution result is being used as an input;
9. confirmation that no external dataset or later TGCV interpretation is required;
10. confirmation that Executor-2 will receive only the frozen bundle and its own reconstruction instructions.

## 3. Hard blockers

The capture must return `BLOCKED` if:

- any bundle hash differs;
- the expected frozen commit cannot be identified;
- an executor component differs from the frozen source;
- runtime identity cannot be recorded;
- prior outcome data enter the execution inputs;
- the bundle is modified after capture;
- an unapproved dependency is required;
- the local checkout is not demonstrably the intended canonical revision.

## 4. Authorization boundary

This artifact authorizes **no scientific execution**. It only defines the integrity evidence required to issue a subsequent corrected authorization.

No C09 claim upgrade, Core change, RMA change, Evidence→Claim Matrix change, SWIM rerun or RUST-DYN-2 rerun is authorized.

## 5. Required output

The local operator shall persist a machine-readable integrity record containing:

`commit_sha, component_sha256, runtime_fingerprint, executor_sha256, working_tree_status, dependency_status, input_isolation_status, capture_timestamp, disposition`.

Only `PASS` on all mandatory fields may proceed to corrected authorization.

**Decision:** `PRE-EXECUTION INTEGRITY CAPTURE = REQUIRED / NOT YET EXECUTED`.
