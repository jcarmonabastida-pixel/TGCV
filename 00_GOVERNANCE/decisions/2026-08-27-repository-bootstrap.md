# Decision — TGCV repository bootstrap

**Date:** 2026-08-27

## Decision

Use GitHub as the canonical continuity layer for TGCV research artefacts and computational reproducibility.

## Scope

The repository separates:
- governance and immutable state records;
- conceptual/ontological core;
- literature and evidence;
- empirical experiments, including EXT-1.0 and EXT-1.1;
- RMA and external research assets;
- applications and institutional/industrial variants;
- source code and tests;
- dataset manifests, hashes and provenance.

## EXT-1.1 constraint

The Rust dataset is not to be downloaded or processed until an identifiability/privacy audit has passed. A freeze is created only after that gate and exact-dataset verification.

## Rationale

This preserves continuity across research sessions and prevents conversational context from being the sole source of truth.
