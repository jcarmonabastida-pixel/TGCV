# RUST-DYN-EXEC-1A — Synthetic Conformance Result v0.1

## Status

**PASS — SYNTHETIC CONFORMANCE / REAL DATASET EXECUTION NOT YET RE-RUN**

Date: 2026-09-08

## Executor

Path: `03_EXPERIMENTS/EXT-1.1_Rust/src/rust_dyn_executor_v01.py`

Corrected executor commit: `aec3e72c1b266f000f44668f9d2599a90d2e7f06`

Corrected executor content SHA-256: `746b6d90ecf909244009a5e8ff8ff37add4e8a57`

## Synthetic result

Command executed locally:

`python .\03_EXPERIMENTS\EXT-1.1_Rust\src\rust_dyn_executor_v01.py --synthetic`

Result: `pass = true`

All seven tests passed:

- `canonical_four_field_identity = true`
- `delta_reconfiguration_equal_cardinality = true`
- `duplicate_fail_closed = true`
- `firewall_closed = true`
- `origin_difference_does_not_force_reach_difference = true`
- `reach_excludes_origin = true`
- `trajectory_excludes_origin = true`

`REAL_DATASET_EXECUTION = false`

`EXECUTION_AUTHORIZATION = false`

## Interpretation

The corrected executor conforms synthetically to the four-field canonical transformation identity and to the bounded H=1 Reach/Trajectory normalization required by the frozen RUST-DYN design. Duplicate transformations fail closed and the synthetic firewall checks remain closed.

This result is a technical conformance result only. It is not an empirical result and does not validate H-R1, H-R3 or H-R4.

## Execution boundary

The earlier real-data invocation that produced 516,061 temporal pairs is **not accepted as the scientific primary result**, because it used the preceding executor representation whose transformation identity omitted `target_package_id`.

The next real-data execution must use the corrected executor identified above. It constitutes the new controlled primary run under the existing scientific design, with the result subject to a fresh primary execution audit and mandatory deterministic replay.

No interpretation of the earlier classification counts is retained as scientific evidence.
