# TI-001 V011 Fixture Generator Specification 001

**Status:** GENERATOR SPECIFICATION — SEMANTICS FROZEN / FIXTURE NOT GENERATED**

## 1. Generator identity

- Generator ID: `TI001-V011-FIXTURE-GENERATOR-001`
- Fixture ID: `TI001-V011-FIXTURE-001`
- Generator type: deterministic
- Scientific execution: NOT AUTHORIZED
- Fixture generation: not yet performed

## 2. Frozen seed

- Seed: `20260926`
- PRNG: xorshift32
- State width: exactly 32 bits
- Arithmetic: unsigned 32-bit modulo 2^32
- zero state: invalid and terminates generation
- mask: `0xFFFFFFFF`
- presentation stream XOR constant: `0x9E3779B9`

The seed is part of the generator contract. The same generator source, specification, and seed must reproduce the same fixture byte-for-byte.

## 3. Deterministic PRNG semantics

Transition, in order:

1. `state ^= (state << 13) & 0xFFFFFFFF`
2. `state ^= state >> 17`
3. `state ^= (state << 5) & 0xFFFFFFFF`
4. mask the resulting state with `0xFFFFFFFF`.

No warm-up draws are used.

Condition stream initial state: `20260926`.

Presentation stream initial state: `20260926 XOR 0x9E3779B9`, reduced to 32 bits.

The streams are independent and never share consumed state.

## 4. Fisher-Yates semantics

Input sequences are indexed from zero.

Iteration is descending:

`i = n-1, n-2, ..., 1`

At each iteration exactly one PRNG state is consumed and:

`j = state % (i+1)`

The elements at positions `i` and `j` are swapped.

No rejection sampling, floating-point conversion, or additional random draw is permitted.

Condition labels before shuffle:

`70 control, 70 treatment, 70 null`

Presentation-orientation labels before shuffle:

`105 I1_FIRST, 105 I2_FIRST`

Pair IDs are assigned in fixed lexical order `P001` through `P210`. The shuffled condition assignment is applied by pair position.

The shuffled presentation assignment determines which orientation appears first within each pair. Every pair still contains exactly one `I1_FIRST` unit and one `I2_FIRST` unit.

Thus, at pair level, exactly 35 control pairs, 35 treatment pairs, and 35 null pairs have `I1_FIRST` as their first materialized unit; the remaining 35 pairs in each condition have `I2_FIRST` as their first materialized unit. This is an ordering balance, not a reduction of the two-presentation-per-pair structure.

## 5. Population

The generated fixture must contain exactly:

- 210 unique pairs;
- 420 decision units;
- 70 pairs in control;
- 70 pairs in treatment;
- 70 pairs in null;
- 210 I1_FIRST decision units;
- 210 I2_FIRST decision units.

Each pair contains exactly two decision units:
- one I1_FIRST;
- one I2_FIRST.

The resulting decision-unit counts are exactly 140 control, 140 treatment, and 140 null.

## 6. Decision-unit schema

Every decision unit must contain exactly these top-level fields, in this order:

1. `decision_id`
2. `pair_id`
3. `condition`
4. `presentation`
5. `context`
6. `available_actions`
7. `future_structure`

The model-visible fields are only:

- `context`
- `available_actions`
- `future_structure`

Hidden provenance fields are:

- `decision_id`
- `pair_id`
- `condition`
- `presentation`

## 7. Exact field semantics

`decision_id`: `D001` through `D420`, assigned in canonical pair order.

`pair_id`: `P001` through `P210`.

`context` contains exactly `items` and `item_count`.

For I1_FIRST:

`{"items":[{"id":"I1","action":"A"},{"id":"I2","action":"B"}],"item_count":2}`

For I2_FIRST:

`{"items":[{"id":"I2","action":"B"},{"id":"I1","action":"A"}],"item_count":2}`

`available_actions` is exactly:

`["A","B"]`

`future_structure` contains exactly:

- `successor_realized`
- `future_structure_available`

For control and null:

`{"successor_realized":false,"future_structure_available":false}`

For treatment:

`{"successor_realized":false,"future_structure_available":true}`

No utility, reward, value, performance, task-success, successor state, outcome, model response, or scientific score may occur in the fixture.

## 8. Canonical serialization

The fixture is UTF-8 JSON with:

- exact top-level field order: `fixture_id`, `schema_id`, `generator_id`, `seed`, `decision_units`;
- exact decision-unit field order defined above;
- exact nested field order defined above;
- compact separators equivalent to `,` and `:`;
- preserved array ordering;
- no BOM;
- exactly one final LF.

Fixture JSON metadata:

- `fixture_id = TI001-V011-FIXTURE-001`
- `schema_id = TI001-V011-DU-SCHEMA-001`
- `generator_id = TI001-V011-FIXTURE-GENERATOR-001`
- `seed = 20260926`

## 9. Integrity requirements

After generation, verify:

- exactly 420 decision units;
- exactly 210 unique pairs;
- exactly two units per pair;
- exactly one I1_FIRST and one I2_FIRST per pair;
- exactly 70 pairs per condition;
- exactly 140 decision units per condition;
- exactly 210 units per presentation;
- exactly 35 pairs per condition in each pair-level first-presentation orientation class;
- exact A/B action set;
- exact visible/hidden field partition;
- no duplicate decision IDs;
- no duplicate pair IDs;
- deterministic reconstruction from the frozen seed.

The fixture SHA-256 is calculated over the exact UTF-8 bytes including the single final LF and bound in an external integrity manifest.

## 10. Independence boundary

The generator may depend only on this specification, its own source, and deterministic local standard-library functionality.

It must not import, execute, parse, or consume:

- Executor-1 outputs;
- Executor-2 outputs;
- V010 scientific results;
- model responses;
- post-hoc observations.

V010 findings motivate V011 but are not generator inputs.

## 11. Required generator self-tests

Before fixture generation, the implementation must verify:

1. xorshift32 seed-1 first five outputs:
   `270369, 67634689, 2647435461, 307599695, 2398689233`;
2. zero-state rejection;
3. deterministic condition-stream reconstruction for seed `20260926`;
4. deterministic presentation-stream reconstruction from the frozen XOR seed;
5. Fisher-Yates descending iteration and modulo mapping;
6. canonical serialization;
7. population/integrity invariants.

The V011 stream vectors must be computed and recorded by the generator preflight rather than copied from an external execution.

## 12. Pre-generation gate

Before generation:

- this specification must be canonical;
- seed and PRNG semantics must be frozen;
- schema identity must be canonical;
- generator source must be committed and hash-bound;
- self-tests must pass;
- integrity preflight must pass.

The gate does not authorize scientific model execution.

## 13. Current disposition

**Generator specification: FROZEN.**

**Seed: FROZEN — `20260926`.**

**Fixture: NOT GENERATED.**

**Scientific execution: NOT AUTHORIZED.**

The next action is to create the V011 decision-unit schema specification and then implement the deterministic generator against the exact frozen schema.
