# RUST-DYN-2-EXEC-1A — Real-Data Preflight Closure v0.1

## Status

**PASS — REAL-DATA INPUT PREFLIGHT CLOSED / EXECUTION AUTHORIZATION PENDING**

Date: 2026-09-08

## Preflight execution

Executor:
`03_EXPERIMENTS/EXT-1.1_Rust/src/rust_dyn2_preflight_v01.py`

Mode:
`RUST_DYN_2_REAL_DATA_PREFLIGHT_ONLY`

Dataset:
`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

Dataset SHA-256:
`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Expected SHA-256 matched: **YES**

## Frozen structural inputs

Temporal rule: `DR-035-v0.1-ADJACENT-CREATED-AT`

Horizon: `H=1`

Exact archive members:
- `rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv`
- `rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv`

`package_versions.csv` schema: **PASS**

Columns:
`id, package_id, version_str, created_at`

`package_dependencies.csv` schema: **PASS**

Columns:
`depending_version, depending_on_package, semver_str`

ZIP opened successfully: **YES**

## Information firewall

The preflight confirms that no analytical experiment object was constructed:

- `T_acc_constructed = false`
- `delta_tacc_computed = false`
- `Reach_computed = false`
- `Trajectory_computed = false`
- `future_activity_read = false`
- `outcome_read = false`
- `predictive_metrics = false`
- `sampling = false`
- `real_dataset_execution = false`
- `execution_authorization = false`

## Environment

Python:
`3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)]`

Platform:
`Windows-11-10.0.26200-SP0`

## Decision

**RUST-DYN-2-EXEC-1A REAL-DATA PREFLIGHT = PASS.**

The frozen dataset is present, its SHA-256 matches the previously frozen dataset, the required structural members and schemas are present, and the preflight has not executed the experiment or accessed downstream outcome/predictive information.

This closure does **not** authorize execution by itself.

The next controlled operation is the explicit **RUST-DYN-2 real-dataset execution authorization gate**, which must freeze the executable version/content hash, resolver version/hash, exact command, output contract, one-primary-plus-one-replay scope, and stop conditions.

**REAL-DATASET EXECUTION AUTHORIZED: NO.**
