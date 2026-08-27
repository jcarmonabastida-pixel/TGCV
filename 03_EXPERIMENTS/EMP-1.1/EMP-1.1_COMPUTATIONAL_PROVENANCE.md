# TGCV-EMP-1.1 — Computational Provenance Record

**Status:** CANONICAL PROVENANCE STATEMENT
**Date:** 2026-08-27

## Purpose

This record closes the provenance question concerning the executable implementation used for the completed EMP-1.1 empirical test.

## Provenance finding

The historical executable rules of MVE-1.0 could not be recovered. EMP-1.1 therefore used a newly specified, explicit and frozen operationalisation rather than a claimed reconstruction of the original MVE implementation.

Accordingly:

- MVE-1.0 remains the conceptual experimental architecture;
- EMP-1.1 is the canonical reproducible operationalisation for the completed computational test;
- no claim is made that EMP-1.1 is the recovered historical MVE-1.0 implementation.

## EMP-1.1 operational specification

The canonical specification records:

- potential components: A1, A2, B1, B2, C1, C2;
- initial component count: 3–5;
- six transformation families;
- three discrete resources;
- twelve objectives;
- horizon H=6;
- stochastic execution independent of objective;
- conventional baseline B versus TGCV representation R;
- primary outcome: paired out-of-sample Delta LogLoss;
- secondary outcomes: AUROC, AUPRC, Brier/calibration and descriptive accuracy;
- structural and null/permutation controls.

## Result boundary

The recorded EMP-1.1 result is evidence for the specified operationalisation. It is not evidence that the unrecovered historical MVE-1.0 implementation has been reproduced.

The result must not be used to retrospectively alter TGCV Core, R, or the operational definition.

## Reproducibility requirement

A future executable package claiming to reproduce EMP-1.1 must include the exact source code, configuration, seeds, data-generation procedure, dependency/environment specification and integrity hashes. Until those artifacts are assembled and verified, the historical result remains **documented and frozen as an empirical record, but not independently re-executable from this repository alone**.

## Relation to TR-181E

TR-181E must treat the frozen EMP-1.1 specification as its operational baseline. It must not infer missing historical MVE-1.0 code, and it must not tune R or TGCV against the EMP-1.1 result.

**Canonical conclusion:** MVE-1.0 executable provenance = NOT RECOVERABLE; EMP-1.1 = canonical explicit operationalisation of the completed computational falsification test.
