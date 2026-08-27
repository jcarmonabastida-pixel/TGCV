# TGCV-EMP-1.1 — Reproducibility Reconstruction Plan

**Status:** CONTROLLED RECONSTRUCTION — NOT A HISTORICAL CODE RECOVERY
**Date:** 2026-08-27

## 1. Objective

Reconstruct the minimum executable package required to reproduce the frozen EMP-1.1 operationalisation and independently verify the recorded empirical result, without claiming recovery of the unavailable historical MVE-1.0 implementation.

## 2. Non-negotiable boundary

This is a reproducibility reconstruction of EMP-1.1, not a reconstruction of MVE-1.0.

No reconstruction step may modify:

- TGCV Core;
- the frozen EMP-1.1 operational specification;
- the recorded EMP-1.1 result;
- the historical interpretation of the result.

## 3. Required package

The reconstruction package must contain:

1. executable source code;
2. complete experiment configuration;
3. deterministic/random seeds;
4. data-generation procedure and parameters;
5. model/training specification;
6. train/validation/test split logic;
7. primary and secondary metric implementation;
8. control implementations;
9. dependency/environment specification;
10. execution instructions;
11. generated-output schema;
12. integrity hashes for all frozen inputs and source artifacts.

## 4. Reconstruction order

The work must proceed in this order:

`specification → implementation → unit checks → deterministic smoke test → full reproduction → result comparison → provenance freeze`

The recorded result is not used to tune the implementation. It is used only as an external acceptance criterion after the implementation has been independently constructed from the frozen specification.

## 5. Acceptance criteria

A reconstruction can be marked reproducible only if:

- all required inputs are identified;
- the implementation executes from a clean environment;
- the same primary estimand is produced;
- the resulting effect is consistent with the recorded EMP-1.1 result within a pre-specified reproducibility tolerance;
- all controls execute;
- source, configuration, environment and outputs can be hashed;
- no implementation choice was selected by inspecting the final test result.

Exact numerical identity is not assumed unless the original source and environment are recovered. Any tolerance must be specified before comparing results.

## 6. Current status

**BLOCKED — SOURCE IMPLEMENTATION NOT YET RECONSTRUCTED.**

The repository currently contains the scientific/protocol specification and empirical record but not yet a verified end-to-end executable package.

## 7. Relationship to TR-181E

TR-181E must not begin as though EMP-1.1 were fully re-executable. First establish the reconstruction boundary and determine which elements can be reused directly.

If the reconstructed package is verified, it becomes the canonical executable baseline for subsequent work. If exact reproduction cannot be achieved, the discrepancy must be documented rather than silently corrected.

## 8. Provenance labels

Every artifact produced during reconstruction must carry one of:

- `HISTORICAL`: recovered from the original record;
- `SPECIFIED`: directly determined by the frozen EMP-1.1 specification;
- `RECONSTRUCTED`: newly implemented to satisfy the specification;
- `DERIVED`: generated from specified/reconstructed inputs;
- `VERIFIED`: independently tested against the acceptance criteria.

**Current canonical statement:** EMP-1.1 is scientifically frozen; computational reproducibility reconstruction is pending.
