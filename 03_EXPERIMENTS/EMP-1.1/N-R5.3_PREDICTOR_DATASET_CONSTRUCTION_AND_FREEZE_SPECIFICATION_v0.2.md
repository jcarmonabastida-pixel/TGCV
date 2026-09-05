# N-R5.3 — PREDICTOR DATASET CONSTRUCTION AND FREEZE SPECIFICATION v0.2

**Status:** FROZEN FOR CORRECTED PROSPECTIVE USE  
**Date:** 2026-09-05  
**Supersedes:** N-R5.3 v0.1 for prospective scientific execution

## Purpose

Construct the Branch N predictor datasets from the unchanged frozen N-R4B.4 initial-snapshot corpus using the corrected N-R5.2 predictor representation.

## Frozen inputs

- N-R4B.4 train snapshots: SHA-256 `b49c4da6187d015b9eb8a930a729ebbb874f17586f18c3ddddf65ed505145ef9`
- N-R4B.4 test snapshots: SHA-256 `18a67b22523f3d17183b14f7611ebc58451754bbfa104bc08ce26a512665ade1`
- train count: 30,000; seed: 3,100,000
- test count: 10,000; seed: 4,100,000
- predictor dimensions: B=16, R=58, B+R=74

## Corrected initial-state hash

For each snapshot, `initial_snapshot_sha256` MUST equal SHA-256 of the UTF-8 bytes of exactly this semantic object:

```json
{"components":<components>,"edges":<edges>,"objective":<objective>,"resources":<resources>}
```

with JSON keys sorted lexicographically, compact separators `(',', ':')`, `ensure_ascii=True`, UTF-8 encoding, and **no terminal newline**.

The object MUST exclude `episode_id`, trajectory fields, outcome fields, and all post-snapshot metadata. This convention is identical to the N-R4B.4 semantic initial-state hash convention.

## Construction

The constructor reads only the frozen N-R4B.4 snapshot files and the corrected N-R5.2 representation implementation. It produces canonical JSONL records sorted by `episode_id` with fields:

`episode_id`, `initial_snapshot_sha256`, `B`, `R`, `BR`.

`BR` MUST equal `B + R` exactly.

## Integrity

The full-dataset integrity gate MUST independently reconstruct the semantic initial-state hash from each source snapshot and compare it with the predictor record. It MUST also verify frozen source hashes, counts, episode IDs, schema, dimensions, concatenation, train/test separation, and absence of learner/inference execution.

## Historical boundary

The v0.1 predictor dataset and its hashes are retained as superseded historical development artifacts. They MUST NOT be supplied to N-R7 scientific execution. The correction changes representation traceability only; N-R4B.4 snapshots, B/R semantics, learner specification, seeds, and outcome labels remain unchanged.

No learner execution, outcome-based feature construction, historical-result tuning, or confirmatory inference is part of N-R5.3 construction.
