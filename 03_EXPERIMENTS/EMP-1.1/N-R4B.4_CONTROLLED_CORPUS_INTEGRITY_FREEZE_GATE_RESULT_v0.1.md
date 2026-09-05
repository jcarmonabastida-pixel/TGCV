# N-R4B.4 — Controlled Corpus Integrity / Freeze Gate Result v0.1

**Date:** 2026-09-05
**Status:** PASS / CLOSED
**Corpus:** `N-R4B.3_CONTROLLED_TRAJECTORY_OUTCOME_CORPUS`
**Specification:** `N-R4B.3 v0.1`

## Decision

N-R4B.4 controlled corpus integrity gate **PASS / CLOSED**.

The full prospective controlled corpus has been generated and its primary filesystem-level integrity checks pass.

## Corpus

- train: 30,000 episodes
- test: 10,000 episodes
- train seed: `3,100,000`
- test seed: `4,100,000`
- historical recovery: `False`
- learner executed: `False`
- confirmatory inference executed: `False`
- historical result used as tuning target: `False`

## Artifact hashes

- `train_snapshots.jsonl`: `b49c4da6187d015b9eb8a930a729ebbb874f17586f18c3ddddf65ed505145ef9`
- `train_trajectories.jsonl`: `08ed37b6b13a033eb47bb52e559b7a11db3c8917b68bff19aad73f98ab836514`
- `test_snapshots.jsonl`: `18a67b22523f3d17183b14f7611ebc58451754bbfa104bc08ce26a512665ade1`
- `test_trajectories.jsonl`: `1a5e9a21fa1f0f2ad756e7743045dc40835a7c3d5203c321f6b0427b32c2eae8`

## Integrity evidence

The executed integrity check confirmed:

- all required artifacts exist;
- registered partition counts are exactly 30,000 train and 10,000 test;
- the four corpus artifact hashes exactly match the hashes recorded in `PROVENANCE.json`;
- provenance records the intended implementation hashes and runtime (`CPython 3.14.7`, Windows 11);
- historical recovery remains false;
- learner and confirmatory inference remain false;
- historical result was not used as a tuning target.

## Freeze boundary

The corpus is now treated as a **prospective controlled reconstruction artifact**. It is not historical EMP-1.1/MVE-1.0 data and does not establish historical Cargo or historical experimental reproducibility.

No modification, regeneration, filtering, rebalancing, or tuning of the frozen corpus is permitted for the confirmatory analysis path without a new explicitly registered decision and corresponding provenance record.

## Scientific-execution boundary

This gate does **not** authorize or constitute learner fitting or confirmatory inference. Those remain subsequent gates.

## Next authorized step

Construct and freeze the predictor-side representations `B` and `R` from the frozen initial snapshots, with explicit leakage and traceability checks, before any learner fitting.
