# N-R5.3 — Predictor Dataset Construction and Freeze Specification v0.1

**Status: PROPOSED FOR PROSPECTIVE FREEZE**  
**Date:** 2026-09-05  
**Scope:** Branch N controlled reconstruction of EMP-1.1  

## 1. Purpose

Define the reproducible construction of the predictor-side dataset from the already frozen N-R4B.4 controlled corpus, using the conforming N-R5.2 representation.

This is a prospective controlled reconstruction. It is **not** recovery of the historical MVE-1.0 executable dataset construction and does not claim reproduction of the historical EMP-1.1 result.

No learner fitting or confirmatory inference is authorized by this specification.

## 2. Frozen upstream inputs

The only scientific source for predictor records is the initial snapshot partition of N-R4B.4:

- train: 30,000 snapshots, dataset seed 3,100,000
- test: 10,000 snapshots, dataset seed 4,100,000

Frozen snapshot hashes:

- `train_snapshots.jsonl`: `b49c4da6187d015b9eb8a930a729ebbb874f17586f18c3ddddf65ed505145ef9`
- `test_snapshots.jsonl`: `18a67b22523f3d17183b14f7611ebc58451754bbfa104bc08ce26a512665ade1`

No trajectory, outcome, post-snapshot state, or external/network state may be used in predictor construction.

## 3. Predictor representation

For each initial snapshot S0:

### Baseline B

`B = [n_components, q1, q2, q3, one_hot(O01...O12)]`

Dimension: **16**.

### Structural representation R

`R = encode_r(S0)` according to N-R1.3 v0.2.

Dimension: **58**.

### Combined representation

`BR = B || R`

Dimension: **74**.

No additional variables, interactions, embeddings, scaling, dimensionality reduction, feature selection, or result-driven transformations are permitted.

## 4. Predictor record schema

Each predictor record MUST contain exactly:

- `episode_id`
- `initial_snapshot_sha256`
- `B`
- `R`
- `BR`

The canonical predictor record is serialized as UTF-8 JSON with deterministic key ordering and compact separators, consistent with the N-R5.2 implementation.

The `episode_id` is provenance only. Changing it must not change B/R/BR for the same underlying snapshot structure; the corresponding snapshot hash may change because episode identity is part of canonical snapshot serialization.

## 5. Construction boundary

The permitted computation is strictly:

`N-R4B.4 initial snapshot → State → B/R/BR → predictor record`

The following are prohibited inputs:

- trajectory records
- outcome Y
- terminal step/reason
- post-initial states
- transition selections
- future snapshots
- test-derived training information
- historical EMP-1.1 result values as tuning targets
- live registry/network state
- ambient external caches
- learner predictions or residuals

## 6. Train/test separation

Train and test predictor datasets are constructed independently from their respective frozen N-R4B.4 initial snapshot partitions.

No fitting, normalization, feature transformation, vocabulary construction, or parameter estimation may cross the train/test boundary during this gate.

The test partition is not inspected for model-selection decisions.

## 7. Traceability requirements

Every predictor record must be traceable to exactly one N-R4B.4 initial snapshot through:

`episode_id + initial_snapshot_sha256`

Integrity checks must establish:

1. one predictor record per snapshot;
2. no missing snapshot IDs;
3. no duplicate episode IDs within a partition;
4. snapshot hash recomputes exactly;
5. B/R/BR recompute exactly from the snapshot;
6. `BR == B + R` exactly;
7. dimensions 16/58/74 exactly;
8. train/test records cannot silently cross partitions.

## 8. Leakage controls

A predictor record must be computable without reading any trajectory or outcome information.

Static and runtime checks must establish absence of dependencies on learner execution, network access, and historical result literals.

The corpus generation itself remains upstream and frozen; this gate must not regenerate or alter N-R4B.4.

## 9. Determinism

Repeated construction from byte-identical N-R4B.4 inputs and identical implementation must produce byte-identical predictor datasets and identical SHA-256 hashes.

Canonical record ordering is by `episode_id` ascending within each partition.

The constructor must not depend on filesystem enumeration order, hash-table iteration order, ambient RNG state, locale, or wall-clock time.

## 10. Dataset artifacts

Prospective output directory:

`03_EXPERIMENTS/EMP-1.1/artifacts/N-R5.3_PREDICTOR_DATASET/`

Required artifacts:

- `train_predictors.jsonl`
- `test_predictors.jsonl`
- `PROVENANCE.json`
- `INTEGRITY_REPORT.json`

The large JSONL datasets are execution artifacts and are not required to be committed to GitHub. Their exact hashes must be recorded in the provenance/integrity artifacts and preserved locally as frozen scientific artifacts.

## 11. Provenance

`PROVENANCE.json` must record:

- specification identifier/version;
- N-R4B.4 input artifact hashes;
- N-R5 implementation hash;
- constructor implementation hash;
- Python/runtime/platform information;
- train/test counts and seeds inherited from N-R4B.4;
- output artifact hashes;
- generation timestamp as provenance metadata only, never as a scientific input;
- historical recovery = false;
- learner executed = false;
- confirmatory inference executed = false;
- historical result used as tuning target = false.

The provenance file must not contain a self-referential hash.

## 12. Required conformance checks

Before scientific freeze, the implementation/runner must verify at minimum:

1. registered train/test counts 30,000/10,000;
2. source snapshot hashes match N-R4B.4;
3. predictor schema;
4. B/R/BR dimensions;
5. B encoding;
6. R encoding delegation to N-R5.2/N-R1.3;
7. exact BR concatenation;
8. one-to-one snapshot/predictor mapping;
9. episode/hash traceability;
10. canonical ordering;
11. deterministic serialization;
12. same-input repeated-run byte identity;
13. train/test separation;
14. no trajectory/outcome dependency;
15. no learner/network dependency;
16. no historical-result literal/tuning path;
17. full-dataset counts;
18. output SHA-256 recording;
19. no modification of N-R4B.4 inputs.

Conformance must first be demonstrated at smoke scale. Full 30k/10k construction occurs only after conformance PASS.

## 13. Scientific boundary

Closing N-R5.3 freezes the predictor dataset representation and its provenance. It does **not** validate the hypothesis that R improves predictive utility.

The historical `ΔLogLoss = 0.07942359585000518` remains an archival acceptance/reference value only and must never be used to select, tune, or modify the representation.

## 14. Gate transition

N-R5.3 PASS/CLOSED authorizes the next phase: learner specification/conformance and only thereafter controlled model fitting and confirmatory inference.

Until N-R5.3 is closed, no learner execution is authorized.
