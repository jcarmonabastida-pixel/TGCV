# EXT-1.1 Scientific Execution — Preparation Boundary v0.1

**Status:** PREPARED — NOT EXECUTED  
**Date:** 2026-09-05

## 1. Purpose

This record defines the execution boundary for the scientific EXT-1.1 run after the N-R8-C2 vNext corpus has been frozen. It is a preparation artifact only. It does not contain scientific results and must not be interpreted as execution evidence.

## 2. Frozen scientific input

The sole frozen N-R8-C2 vNext input is:

- Corpus: `N-R8-C2_vNEXT_CORPUS_v0.1.jsonl`
- Corpus SHA-256: `795bfb12b11be49dc08f4dbe568141cd0a2f7e776c7a10cc8aa9122befb408af`
- Manifest final SHA-256: `14ed0cdc3ec00690b06ea12d4e6cf6b97cd15037a506bfe202984f07f1614c07`
- Freeze record: `N-R8-C2_vNEXT_CORPUS_FREEZE_2026-09-05.md`
- Pair count: `5000`
- Distinct audited states: `7496`

The frozen corpus is immutable. Scientific execution must consume it as-is: no regeneration, normalization, reordering, filtering, repair, or substitution is permitted.

## 3. Scientific execution boundary

EXT-1.1 scientific execution begins only when an explicit execution command invokes the designated execution entrypoint. Merely importing preparation modules, running gates, or inspecting the corpus is not scientific execution.

The execution layer must be separated from:

1. frozen corpus generation;
2. corpus audit and deterministic reproducibility evidence;
3. external Rust dataset acquisition/consumption;
4. result analysis and reporting.

## 4. Rust dataset boundary

The Rust dataset is an external empirical input for EXT-1.1 and has not been consumed by the preparation pipeline. Before scientific execution, the dataset package must be acquired and independently frozen with its own identity, provenance, and SHA-256 evidence.

No dataset-derived observation may be used to construct, select, repair, pair, or alter the frozen N-R8-C2 vNext corpus.

## 5. Required execution gates before first scientific run

The first scientific run must refuse to proceed unless all of the following are satisfied:

- frozen corpus exists and SHA matches exactly;
- frozen manifest exists and identity matches exactly;
- freeze record is present;
- required frozen implementation SHA values match;
- Rust dataset is present, identified, and independently frozen;
- execution output directory is clean or uniquely versioned;
- no result artifact from a previous scientific run is being overwritten;
- execution explicitly records the corpus SHA and dataset SHA;
- execution explicitly records that corpus construction was completed before dataset consumption;
- preparation-stage gates remain PASS;
- scientific execution is explicitly marked `PERFORMED` only by the execution entrypoint itself.

## 6. Prohibited actions

Before and during EXT-1.1 execution, the execution layer must not:

- regenerate the N-R8-C2 vNext corpus;
- modify the frozen corpus or manifest;
- silently normalize corpus records;
- construct new pairs from the Rust dataset;
- use Rust observations to alter frozen pair selection;
- overwrite an existing scientific result;
- label preparation-stage PASS evidence as a scientific result.

## 7. Expected provenance chain

`FROZEN_CORPUS` → `FROZEN_RUST_DATASET` → `EXT-1.1_EXECUTION` → `RESULT_ARTIFACTS` → `ANALYSIS`

The causal/provenance direction must remain explicit. In particular, the frozen corpus precedes and is independent of empirical dataset consumption.

## 8. Current state

```text
N-R8-C2 vNext corpus: FROZEN SCIENTIFIC INPUT
Corpus audit: PASS
Deterministic rerun: PASS
Rust dataset: NOT_CONSUMED / NOT_YET_FROZEN
EXT-1.1 scientific execution: NOT_PERFORMED
Scientific result: NONE
```

## 9. Next implementation step

Create and audit the dedicated EXT-1.1 execution entrypoint and its pre-execution gate. That gate must bind the frozen corpus identity and the independently frozen Rust dataset identity before allowing any scientific run. Do not execute EXT-1.1 as part of this preparation step.
