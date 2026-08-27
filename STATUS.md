# TGCV — Status

**Repository bootstrap:** 2026-08-27

## Canonical state

The repository has been initialized from the currently recoverable TGCV research state. The central object is the set of interactions that modify the transformations accessible to a system.

## EXT-1.1 gate

Status: **NOT FROZEN**.

Required order:
1. Complete identifiability/privacy audit for the candidate Rust dataset.
2. If the audit passes, identify and verify the exact dataset.
3. Run/finalize EXT-1.1 using the frozen protocol and record provenance, hashes and configuration.
4. Create the immutable EXT-1.1 freeze.

No dataset is committed to this repository. Dataset identity and integrity belong in `08_DATA_MANIFESTS/`.

## Continuity rule

This file is a state pointer, not a substitute for frozen evidence. Any change to canonical research state must be versioned and recorded in `00_GOVERNANCE/decisions/` and, where appropriate, a new freeze must be created.
