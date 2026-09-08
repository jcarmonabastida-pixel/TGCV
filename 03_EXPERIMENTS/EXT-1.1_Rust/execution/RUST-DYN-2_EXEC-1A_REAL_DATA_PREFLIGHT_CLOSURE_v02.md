# RUST-DYN-2 EXEC-1A — Real-Data Preflight Closure v0.2

**Date:** 2026-09-08  
**Status:** CLOSED — REAL-DATA PREFLIGHT PASS / EXECUTION AUTHORIZATION PENDING

## Command executed

```text
python .\03_EXPERIMENTS\EXT-1.1_Rust\src\rust_dyn2_preflight_v01.py --dataset "C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip"
```

## Result

`pass = true`.

## Dataset integrity

- Dataset SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- Expected SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- ZIP opened: PASS
- Package versions rows: 607,498
- Horizon: H=1
- Temporal rule: `DR-035-v0.1-ADJACENT-CREATED-AT`

## Frozen members and schemas

### package_versions.csv

Member:
`rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv`

Header:
`id, package_id, version_str, created_at`

Schema: PASS; no missing or duplicate columns.

### package_dependencies.csv

Member:
`rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv`

Header:
`depending_version, depending_on_package, semver_str`

Schema: PASS; no missing or duplicate columns.

## Firewall verification

The preflight confirms that no real experimental computation or authorization occurred:

- `tacc_constructed = false`
- `delta_tacc_computed = false`
- `reach_computed = false`
- `trajectory_computed = false`
- `future_activity_read = false`
- `outcome_read = false`
- `predictive_metrics = false`
- `sampling = false`
- `real_dataset_execution = false`
- `execution_authorization = false`

## Governance interpretation

The frozen Rust dataset is structurally compatible with the RUST-DYN-2 execution design at the input/schema level. The dataset identity matches the previously frozen SHA-256 and the required members and schemas are present.

This closure does **not** authorize RUST-DYN-2 real-data execution. It only closes the preflight gate. Scientific computation remains blocked pending a separate explicit governance authorization decision.

## Next gate

Prepare and review the dedicated ex-ante execution authorization decision for RUST-DYN-2, including the exact executor, dataset SHA, semantic/reanchoring constraints, DR-035 temporal population, H=1 scope, firewall, primary/replay requirements, and scientific interpretation boundary.
