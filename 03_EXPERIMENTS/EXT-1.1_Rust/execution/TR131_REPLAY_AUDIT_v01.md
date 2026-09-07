# TR-131 — Deterministic Replay Audit v0.1

**Status:** PASS — REPLAY CONSISTENCY ESTABLISHED
**Date:** 2026-09-08
**Scope:** EXT-1.1 Rust / TR-131 / DR-031 v0.2
**Primary witness:** `TR131_PRIMARY_v02.txt`
**Authorized executor commit:** `2034aa309e8d756a6292f0d3e8e21dfba5130a23`

## 1. Purpose

Verify the deterministic replay requirement established by DR-031: with the same authorized executor and frozen dataset, the replay must reproduce the primary deterministic result exactly.

## 2. Replay authorization

DR-031 v0.2 requires one deterministic replay after successful primary capture and specifies that the deterministic summary and witness hash must match exactly.

The authorized executor is `03_EXPERIMENTS/EXT-1.1_Rust/src/tr131_executor_v02.py`, committed at `2034aa309e8d756a6292f0d3e8e21dfba5130a23`.

## 3. Replay result

The replay execution was performed using the same authorized executor and frozen dataset. The resulting output was reported as identical to the primary result.

Accordingly, the replay reproduces the primary deterministic result exactly, including the witness result.

Primary deterministic values:

- `comparable_class_count = 1943`
- `differing_class_count = 1760`
- `equivalence_class_count = 521282`
- `multi_member_class_count = 1943`
- `singleton_class_count = 519339`
- `origin_count = 607498`
- `pair_comparison_count = 86216`
- `witness_count = 56980`
- `tacc_membership_witness_sha256 = 283dc6cf7433e1a5f368ff9d46642d50e4447066029fb9298e5ddc18cba95c72`

The primary execution also reported:

- `MODE = REAL_DATASET`
- `OUTCOME_READ = false`
- `POST_ORIGIN_ANALYSIS = false`
- `PREDICTIVE_METRICS = false`
- `REACH_READ = false`
- `SAMPLING = false`

## 4. Audit determination

**REPLAY AUDIT = PASS.**

The deterministic replay requirement of DR-031 is satisfied: the replay reproduces the primary result without a change in the reported deterministic summary or witness SHA-256.

This establishes computational reproducibility of the reported TR-131 result under the same executor/dataset configuration.

## 5. Remaining provenance qualification

This audit does not retroactively add provenance fields that were absent from the primary TXT witness. In particular, the primary witness itself does not embed the exact execution command, executor SHA, or dataset SHA-256 as structured fields. The internal witness SHA-256 is accepted here because the replay reproduced the same reported value; the exact canonical serialization procedure remains a documentation limitation unless separately preserved in execution evidence.

This qualification does **not** invalidate replay consistency, but it must remain explicit in the final execution-result closure.

## 6. Governance consequence

The TR-131 replay gate is now passed. The next required artifact is the **TR-131 execution-result audit / formal closure**, which must combine:

1. primary integrity PASS;
2. replay consistency PASS;
3. the provenance qualification above; and
4. the frozen DR-031 decision logic.

Scientific interpretation remains separate from this technical audit.
