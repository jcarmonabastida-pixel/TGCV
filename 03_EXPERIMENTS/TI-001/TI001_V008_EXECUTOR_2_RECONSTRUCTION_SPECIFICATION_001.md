# TI-001 V008 Executor-2 Reconstruction Specification 001

**Status:** READY FOR IMPLEMENTATION — SCIENTIFIC EXECUTION NOT_PERFORMED  
**Scope:** independent deterministic reconstruction of the frozen V008 fixture.

## Purpose

Define the independent reconstruction boundary for the frozen TI-001 V008 fixture.

Executor-2 is a structural/deterministic equivalence activity only. It MUST NOT perform scientific execution, call the model/API, consume model responses, or consume any scientific execution result.

## Independence boundary

Executor-2 MUST NOT import, call, execute, parse, or consume:

- the V008 scientific provider;
- the V008 scientific executor;
- Executor-1 implementation or outputs;
- model/API responses;
- generated decision results;
- the canonical generated fixture as reconstruction input.

Executor-2 MAY use only:

- this specification;
- the canonical V008 generator specification;
- the frozen V008 generator source;
- the V008 Decision Unit Schema Specification;
- the declared seed/constants and deterministic rules fixed by those artifacts;
- its own independent implementation.

The expected fixture hash stated below is an integrity target only; it is not permission to read or parse the generated fixture.

## Frozen V008 identities

- fixture_id: `TI001-V008-FIXTURE-001`
- schema_id: `TI001-V008-DU-SCHEMA-001`
- generator_id: `TI001-V008-FIXTURE-GENERATOR-001`
- seed: `20260925`
- canonical fixture Git blob SHA-1: `3ff971544f98c8d810173493cd49d54c46070952`
- canonical fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- generator specification Git blob SHA-1: `8964cb1cee4e5017d8512873fcb7934c21d5d18c`
- generator source Git blob SHA-1: `f345c41371a189c43b69b707b49b7eb17d140f55`
- decision-unit schema Git blob SHA-1: `d9539790452b047bc845a19bdcf50b8713a42b2a`

## Reconstruction requirements

Executor-2 MUST independently reproduce:

1. the complete pair identity set P001 through P210;
2. the exact condition allocation: 70 control, 70 treatment, 70 null;
3. the exact presentation allocation: 105 I1_FIRST, 105 I2_FIRST;
4. the complete observable instance structure;
5. treatment future-structure mapping;
6. control/null future-structure withholding;
7. hidden identity fields and agent-visibility boundaries;
8. canonical decision-unit ordering;
9. canonical compact UTF-8 JSON serialization;
10. the canonical fixture SHA-256.

The reconstructed fixture MUST be observationally identical to the frozen V008 fixture for every field and byte that belongs to the canonical fixture representation.

## Authoritative deterministic semantics

Executor-2 MUST use the exact deterministic semantics already fixed by the V008 generator specification.

### PRNG

- xorshift32;
- state width exactly 32 bits;
- unsigned 32-bit arithmetic;
- transition:
  1. `state ^= (state << 13) & 0xFFFFFFFF`;
  2. `state ^= state >> 17`;
  3. `state ^= (state << 5) & 0xFFFFFFFF`;
  4. final state masked with `0xFFFFFFFF`;
- zero state is invalid and MUST terminate reconstruction;
- condition stream initial state: seed `20260925`;
- presentation stream initial state: `20260925 XOR 0x9E3779B9 = 2667729284`;
- streams are independent;
- no warm-up draws.

### Fisher-Yates

- zero-based indexing;
- descending iteration `i = n-1 ... 1`;
- one PRNG draw per iteration;
- `j = state % (i+1)`;
- swap `i,j`;
- no rejection sampling or additional draw;
- condition labels before shuffle: 70 control, 70 treatment, 70 null;
- presentation labels before shuffle: 105 I1_FIRST, 105 I2_FIRST;
- pair IDs assigned lexically P001 through P210;
- shuffled assignments are applied by pair position.

### Decision-unit materialization

For every pair:

- exactly two decision units;
- both share the pair condition;
- exactly one is I1_FIRST and one is I2_FIRST;
- the pair-level orientation determines which presentation is materialized first;
- I1 maps to action A;
- I2 maps to action B;
- treatment has `future_structure_available=true`;
- control and null have `future_structure_available=false`;
- `successor_realized=false` in all conditions;
- no utility, reward, value, performance, outcome, successor state, or model response is present.

The agent-facing fields are exactly:

- `context`;
- `available_actions`;
- `future_structure`.

Hidden fields are never consumed by the provider boundary.

## Canonical serialization

Executor-2 MUST reproduce the schema-defined canonical serialization:

- UTF-8;
- compact JSON;
- no insignificant whitespace;
- exact top-level field order;
- exact decision-unit field order;
- exact nested-object field order;
- exact array ordering;
- exactly one final LF;
- no BOM.

The reconstructed byte sequence MUST hash to:

`dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`

A hash mismatch is FAIL. Executor-2 MUST NOT repair, normalize, reorder, or otherwise modify the reconstruction to obtain a match.

## Required reconstruction checks

The independent reconstruction run MUST report at least:

- fixture_id identity;
- schema_id identity;
- generator_id identity;
- seed identity;
- pair count = 210;
- decision count = 420;
- condition counts = 70/70/70 pairs;
- presentation counts = 105/105;
- exactly two decisions per pair;
- complementary presentation within every pair;
- treatment/control/null future-structure mapping;
- no successor realization;
- hidden-field isolation;
- action representation A/B;
- canonical ordering;
- canonical serialization;
- reconstructed SHA-256;
- equality against the expected canonical SHA-256.

The run MUST explicitly report:

`scientific_execution = NOT_PERFORMED`

and MUST not perform any model/API call.

## Gate sequence

1. Freeze this specification and its Git blob identity.
2. Implement Executor-2 independently from the permitted sources only.
3. Bind the Executor-2 source identity.
4. Execute a reconstruction preflight/run with no scientific inputs.
5. Record PASS/FAIL and all required checks.
6. Only a PASS may satisfy the Executor-2 reconstruction precondition in the V008 execution contract.
7. PASS does not authorize scientific execution.

## Scientific execution boundary

This specification and any Executor-2 reconstruction run MUST retain:

`scientific_execution = NOT_PERFORMED`

Scientific execution requires a separate execution authorization gate after all contractual preconditions are satisfied and explicit user authorization is obtained.
