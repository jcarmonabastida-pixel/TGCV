# N-R5.3 DATASET FREEZE GATE RESULT v0.1

**Date:** 2026-09-05  
**Status:** PASS / CLOSED  
**Branch:** N — controlled prospective reconstruction  
**Historical recovery:** NO

## 1. Gate decision

The N-R5.3 predictor dataset freeze gate is **PASS / CLOSED**.

The complete prospective predictor dataset was constructed from the frozen N-R4B.4 initial snapshots and passed the registered full-dataset integrity checks. No learner fitting, confirmatory inference, historical-code recovery, or result-driven tuning was performed.

## 2. Frozen predictor dataset

| Partition | Count | Seed | Predictor SHA-256 |
|---|---:|---:|---|
| train | 30,000 | 3,100,000 | `d40e3d5f5bd8839d5c83efb1fa2a2d33f432c65c47f568516152dce578f991bd` |
| test | 10,000 | 4,100,000 | `8ae5d84ef0bd1dc50835b1b006e20f299437f2a49395b31e057c0f016d1d3b35` |

Frozen N-R4B.4 snapshot inputs:

- train: `b49c4da6187d015b9eb8a930a729ebbb874f17586f18c3ddddf65ed505145ef9`
- test: `18a67b22523f3d17183b14f7611ebc58451754bbfa104bc08ce26a512665ade1`

Integrity report:

- `INTEGRITY_REPORT.json` SHA-256: `67d423aabcb5f1774cbff0ef64169e65d5ff698ed37ef6dcb9e6e4855949d2c0`

## 3. Integrity result

The full-dataset checker reported **PASS** for all registered checks:

- frozen snapshot hashes
- predictor hashes
- train/test counts
- canonical episode IDs
- uniqueness
- predictor schema
- dimensions B=16, R=58, BR=74
- `BR = B || R`
- snapshot-hash consistency
- snapshot-to-predictor traceability
- train/test seed separation
- absence of learner/inference execution
- historical-recovery boundary

## 4. Implementation provenance

- Predictor implementation SHA-256: `c512367c3747f28a4d3960001228013015fd816d8af18f3f3552b19937113c39`
- Predictor-dataset constructor SHA-256: `2a220c3291d422a3d8b86ecaa812532d0b397417c87da9b285e726c41cff782e`
- Full-integrity checker correction commit: `53514f722cec82fb8d81fb8fb292b40071db489d`
- N-R5.3 conformance gate: PASS / CLOSED

The integrity-checker correction changed only the verification procedure so that snapshot hashing exactly matched the canonical N-R5.2 serialization. The predictor artifacts themselves were not regenerated or modified; their registered SHA-256 values remained unchanged.

## 5. Scientific boundary

This gate establishes the integrity and provenance of the **predictor dataset**. It does not establish predictive utility, causal validity, historical equivalence, or empirical validation of TGCV.

The historical EMP-1.1 result remains a documented historical empirical record and is **not** used as a tuning target or acceptance criterion for the present learner execution.

## 6. Freeze rule

From this gate onward, any modification to the frozen predictor dataset, its source snapshots, predictor representation, or registered construction procedure requires a new explicit decision and provenance record. Silent modification or regeneration is prohibited.

## 7. Next authorized gate

**N-R6.1 — Learner Specification.**

The next step is specification and conformance of the learner and analysis procedure before any learner is executed against the frozen 30,000/10,000 predictor dataset.

No scientific learner execution is authorized by this gate itself.
