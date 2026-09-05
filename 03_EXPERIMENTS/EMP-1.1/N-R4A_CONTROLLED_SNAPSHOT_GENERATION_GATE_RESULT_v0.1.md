# N-R4A — Controlled Snapshot Generation Gate Result v0.1

**Status:** PASS / CLOSED  
**Date:** 2026-09-05  
**Branch:** N — Controlled New Reconstruction  
**Scope:** prospective snapshot-generation conformance only

## Decision

N-R4A is **PASS / CLOSED**. The controlled Branch N snapshot generator conforms to the registered N-R4A specification at the conformance level tested.

This closes the snapshot-generation/reconstruction input boundary for the next gate. It does **not** constitute scientific execution, historical generator recovery, validation of EMP-1.1 historical code, or confirmation of the predictive result.

## Runner

`N_R4A_CONFORMANCE_RUNNER_v0.1`

## Implementation

Path:

`03_EXPERIMENTS/EMP-1.1/src/branch_n_r4a_generator_v01.py`

Implementation SHA-256:

`18ca6dbe1916267078a2e401e71c073d6656c2e92eafc671031e714c09ba792d`

## Conformance checks

- `train_schema_and_domain` — PASS
- `test_schema_and_domain` — PASS
- `episode_id_canonical` — PASS
- `same_seed_byte_identity` — PASS
- `train_test_seed_separation` — PASS
- `rerun_sha256_identity` — PASS
- `snapshot_future_outcome_boundary` — PASS
- `scientific_execution` — NOT_PERFORMED

Smoke corpus sizes:

- train: 100 snapshots
- test: 100 snapshots

Smoke corpus SHA-256:

- train: `0356e96df645b52559b9c3a49b6aa7fba9b5d26677d112369f6387fb1c52b174`
- test: `678afe0aded74b78e39b8fd6919a3f11628d2dbec58954aa4858c293c8bd115d`

## Scientific boundary

The gate verifies only the deterministic and provenance-controlled generation of prospective Branch N input snapshots. No learner fitting, outcome generation, trajectory simulation, confirmatory statistic, or comparison with the historical EMP-1.1 result was performed.

The historical 20,000-episode pilot procedure remains OPEN and is not silently substituted by this smoke conformance corpus.

## Consequence

The N-R4A blocker is closed. The next authorized gate is **N-R4B — Controlled Outcome/Trajectory Generation Specification**.

N-R4B must independently specify the post-snapshot outcome/trajectory process, including its boundary with the frozen snapshot input, without using the historical recorded result as a tuning target.
