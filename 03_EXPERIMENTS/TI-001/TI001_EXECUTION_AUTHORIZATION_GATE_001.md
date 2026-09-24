# TI-001 Scientific Execution Authorization Gate 001

**Status:** GATE DEFINED — SCIENTIFIC EXECUTION NOT AUTHORIZED

## Purpose

This gate separates structural preflight closure from authorization to perform the scientific TI-001 experiment.

Passing this gate specification does not itself authorize execution. Authorization requires an explicit, separately persisted decision after all gate conditions are verified.

## Required conditions

1. **Preflight closure:** TRGCV_TI-001_PREFLIGHT_AUDIT_002.json reports PREFLIGHT_PASS.
2. **P1–P10:** all preflight checks are PASS.
3. **Assignment controls:** A1–A9 are PASS.
4. **Independent reconstruction:** P9 is independently reconstructed by Executor-2, with exact observable equivalence and matching fixture SHA-256.
5. **Primary estimand freeze:** P10 is frozen before scientific execution:
   - name: matched_condition_difference_in_transformation_handling
   - type: difference_in_subsequent_transformation_handling
6. **Fixture immutability:** the frozen TI-001 fixture and its defining generator are not modified after gate closure.
7. **No scientific execution:** no treatment/control scientific run is performed as part of this gate.
8. **Execution traceability:** any authorized execution must persist the exact package commit, fixture hash, assignment seed, environment seeds, executor identity, runtime metadata, outputs, and deviations.
9. **Deviation rule:** any deviation from the frozen package, assignment protocol, estimand, or execution order invalidates authorization for the affected run until formally resolved.
10. **No retrospective estimand change:** the primary estimand cannot be changed after observing scientific outcomes.

## Authorization record requirements

A separate authorization record must state:

- authorization status (AUTHORIZED or NOT_AUTHORIZED);
- exact canonical commit;
- exact fixture SHA-256;
- preflight audit reference;
- P9 reconstruction record reference;
- frozen primary estimand;
- authorized executor/version;
- authorization timestamp;
- explicit confirmation that no scientific execution has occurred before authorization.

## Current state

The current state satisfies the documented preflight requirements, but **scientific execution remains NOT_AUTHORIZED** until an explicit authorization record is created.

## Governance boundary

This gate is a governance artifact, not a scientific result and not evidence for the TI-001 hypothesis.
