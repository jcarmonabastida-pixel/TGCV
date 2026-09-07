# RUST-DYN-EXEC-1A — Adapter Integrity Closure v0.1

## Status

**PASS — REAL-DATA ADAPTER STRUCTURE ACCEPTED / REAL EXECUTION NOT AUTHORIZED**

Date: 2026-09-08

## Evidence chain

1. Dataset/input-schema preflight: PASS and CLOSED.
2. Adapter synthetic conformance: PASS.
3. Adapter implementation: v0.2 committed in GitHub.
4. R* v0.2 dependency: frozen existing resolver.
5. DR-035 temporal population: preserved.
6. Real execution: fail-closed.

## Frozen components

Dataset SHA-256:

`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Adapter:

`03_EXPERIMENTS/EXT-1.1_Rust/src/rust_dyn_adapter_v01.py`

Adapter blob SHA:

`1fc03d48c5de6d04d72042208cc332570ec9b15a`

Adapter commit:

`cbd1d3e3374561952a08b4d18f47ba8f0ef978b6`

Resolver:

`03_EXPERIMENTS/EXT-1.1_Rust/src/rstar_v02.py`

Resolver blob SHA:

`669d4f01131af518f32b1b4b3da27f676ae4ae55`

Temporal rule:

`DR-035-v0.1-ADJACENT-CREATED-AT`

Horizon:

`H = 1`

## Structural implementation review

### Input contract

The adapter reads only the frozen structural members `package_versions.csv` and `package_dependencies.csv`, matching the schemas established by the local input/schema preflight.

### Origin construction

Origins are represented as `(version_id, package_id, version_str, created_at)` and `created_at` is parsed explicitly. Duplicate origin IDs fail closed.

### T_acc construction

For each origin, dependency edges are resolved through the frozen R* v0.2 resolver. Selected admissible target versions are represented as canonical transformations `(origin_version_id, target_package_id, target_version_id, target_version_str)`. Duplicate canonical transformations fail closed.

### Temporal population

The adapter preserves DR-035: package-local ordering by `created_at`, exact timestamp ties excluded, adjacent consecutive origins only, no arbitrary secondary ordering, no cross-package pairs.

### Firewall

The adapter contains no outcome, popularity, download, adoption, success, predictive-target, or future-activity computation. Reach and Trajectory are not used to construct `T_acc`.

### Determinism

Synthetic conformance verifies deterministic temporal-pair construction and fail-closed duplicate handling. Real-data invocation remains blocked by an explicit authorization constant and CLI fail-closed path.

## Synthetic conformance result

All seven adapter checks passed:

- adjacent_only = TRUE
- created_at_order_only = TRUE
- deterministic = TRUE
- no_cross_package_pairs = TRUE
- real_execution_blocked = TRUE
- tacc_duplicate_fail_closed = TRUE
- timestamp_ties_excluded = TRUE

## Boundary assessment

This closure establishes implementation integrity of the adapter structure only. It does not establish an empirical result from the Rust dataset and does not establish H-R1, H-R3, or H-R4.

It does not establish causality, predictive superiority, universal validity, positive value, or originality.

TR-131 and DR-032 remain closed and are not reopened.

## Decision

**RUST-DYN-EXEC-1A adapter integrity = PASS.**

The real-data adapter is technically ready for the next governance stage.

**REAL-DATASET EXECUTION AUTHORIZED: NO.**

## Next controlled operation

Prepare the **RUST-DYN-EXEC-1 execution authorization gate**, including exact executor composition, hashes, command, dataset hash, runtime, expected outputs, replay requirements, and explicit ex-ante authorization decision.
