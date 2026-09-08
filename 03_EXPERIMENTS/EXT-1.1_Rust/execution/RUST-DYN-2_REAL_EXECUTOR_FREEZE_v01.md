# RUST-DYN-2 — Final Real-Data Executor Freeze v0.1

**Status:** CLOSED — EXECUTOR FROZEN / AUTHORIZED PRIMARY RUN READY
**Date:** 2026-09-08
**Decision:** DR-043

## 1. Canonical executor

File:

`03_EXPERIMENTS/EXT-1.1_Rust/src/rust_dyn2_real_executor_v01.py`

Content SHA-256:

`073e09477df78920a10fff620eca4541068fd409`

Git commit:

`66c7b086ac1083941fc7637b97cce65b958807f8`

The executor is now the only authorized implementation for the RUST-DYN-2 primary real-data run.

## 2. Frozen dependencies

Dataset SHA-256:

`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

R* v0.2 SHA-256:

`669d4f01131af518f32b1b4b3da27f676ae4ae55`

Temporal rule:

`DR-035-v0.1-ADJACENT-CREATED-AT`

Temporal population SHA-256:

`1c7a29434675d5e7bbe5a1cfc3a44a809d8eae222d3467374177d8bd20048d8e`

Horizon:

`H=1`

## 3. Semantic freeze

The executor constructs the initial configuration from the structural dependency declarations `(target_package_id, semver_requirement)`.

It constructs `T_acc` using the frozen R* v0.2 admissibility/selection semantics and the four-field transformation identity:

`τ = (origin_version_id, target_package_id, target_version_id, target_version_str)`

Potential successor:

`Succ(C,τ) = C \ {(p_d,*)} ∪ {(p_d,v_d)}`

Reach is the exact canonical set of successor configurations, not the set of transformation tuples.

At H=1, trajectory is represented as the canonical unordered collection of singleton successor steps. No semantic ordering among alternative successors is invented.

## 4. Mandatory fail-closed checks

Before structural computation the executor verifies:

- dataset SHA;
- R* SHA;
- exact archive member paths;
- required structural fields;
- duplicate origin IDs;
- missing origin references;
- configuration multiplicity invariant;
- exact DR-035 temporal population hash;
- H=1 fixed horizon.

Any mismatch raises a blocking error.

## 5. Firewall

No code path reads or computes:

- downloads;
- adoption/popularity/success;
- future activity;
- outcomes;
- value;
- predictive metrics;
- Cargo/runtime execution;
- lockfile results;
- sampling.

## 6. Exact authorized command

```powershell
python .\03_EXPERIMENTS\EXT-1.1_Rust\src\rust_dyn2_real_executor_v01.py --dataset "C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip"
```

This is the exact primary-run command authorized by DR-043.

## 7. Primary/replay protocol

Run the exact command once for the primary execution.

Do not modify the executor, dataset, command, horizon or parameters after the primary run.

After the primary technical audit, the same frozen command must be executed once as deterministic replay.

Scientific closure is blocked until primary and replay canonical outputs agree exactly.

## 8. Expected execution boundary

The command must access only the frozen ZIP structural members and the frozen local R* module. It must not invoke Cargo or any runtime package installation/resolution process.

The console output is the primary machine-readable result. The user must preserve the complete stdout/stderr capture for the subsequent audit and closure artifacts.

## 9. Governance consequence

DR-043 authorization is now operationally bound to this frozen executor and exact command.

**REAL-DATASET EXECUTION: READY — DO NOT CHANGE THE COMMAND.**

Next operation: execute the exact primary command locally and return the complete console output unchanged for technical audit. Do not perform the replay yet.
