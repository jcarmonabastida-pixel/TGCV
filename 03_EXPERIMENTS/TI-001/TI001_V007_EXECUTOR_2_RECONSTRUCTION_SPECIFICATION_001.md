# TI-001 V007 Executor-2 Reconstruction Specification 001

**Status:** BLOCKED — PRNG DEFINITION REQUIRED  
**Scientific execution:** NOT_PERFORMED

## Purpose

Define the independent reconstruction boundary for the frozen TI-001 V007 fixture.

Executor-2 is a structural equivalence activity only. It must not perform scientific execution or model/API calls.

## Independence boundary

Executor-2 MUST NOT import, call, execute, parse, or consume:

- the V007 scientific provider;
- the V007 scientific executor;
- Executor-1 outputs;
- model/API responses;
- any generated decision result.

Executor-2 MAY use only:

- this specification;
- the frozen V007 fixture parameters and canonical fixture;
- its own independent implementation.

## Frozen V007 parameters

- fixture_id: `TI001-v007-candidate-001`
- fixture_version: `v007-candidate-001`
- canonical fixture blob SHA: `663383b27b567d73757ac967986d0b9b949dc50e`
- pair_count: 210
- decision_count: 420
- conditions: control / treatment / null
- pair allocation: 70 / 70 / 70
- presentation order: 105 I1_FIRST / 105 I2_FIRST
- action space: A / B
- randomisation seed: 20260925
- declared randomisation algorithm: xorshift32 + Fisher-Yates

## Reconstruction identity requirements

Executor-2 must reproduce, independently:

1. the complete pair identity set;
2. condition assignment;
3. presentation-order assignment;
4. the complete observable instance structure;
5. treatment future-structure mapping;
6. control/null withholding;
7. hidden identity fields and leakage boundaries;
8. deterministic ordering;
9. canonical fixture hash.

The resulting reconstruction must be observationally identical to the frozen fixture for all fields that are part of the frozen fixture.

## Critical unresolved definition: xorshift32 + Fisher-Yates

The frozen fixture declares the algorithm as `xorshift32 + Fisher-Yates`, but the repository currently contains no V007 generator implementation or V007 reconstruction specification that defines the exact PRNG transition and Fisher-Yates index extraction.

Therefore Executor-2 MUST NOT infer or choose an implementation variant.

The following details MUST be fixed before Executor-2 implementation:

- xorshift32 word width and unsigned arithmetic semantics;
- initial state derivation from seed;
- exact xorshift shift constants;
- state update ordering;
- whether zero state is permitted and how it is handled;
- Fisher-Yates iteration direction;
- exact random-value-to-index mapping;
- modulo vs bounded/unbiased reduction;
- whether any warm-up draws are consumed;
- whether one or multiple PRNG draws are consumed per shuffle position;
- separate or shared PRNG streams for condition assignment and presentation-order assignment.

## Gate rule

**BLOCKED** until the exact V007 PRNG/Fisher-Yates definition is recovered from an authoritative V007 design/generator artifact or explicitly fixed as part of the experimental design.

Once resolved:

1. this specification is updated;
2. its hash/commit is frozen;
3. Executor-2 is implemented independently;
4. reconstruction preflight is executed;
5. PASS/FAIL is recorded;
6. no scientific execution is authorized by that PASS alone.

## Scientific execution boundary

This reconstruction specification and any resulting Executor-2 run must retain:

`scientific_execution = NOT_PERFORMED`

until a separate, explicit scientific authorization is granted after all applicable gates pass.
