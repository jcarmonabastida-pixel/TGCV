# TI-001 V008 Decision Unit Schema Specification 001

**Status:** DESIGN — NOT APPROVED FOR GENERATION**  
**Design identity:** TI001-V008-DU-SCHEMA-001  
**Scientific execution:** NOT_PERFORMED  
**Fixture generated:** false

## 1. Scope

This document defines the exact materialized Decision Unit schema for the new V008 design.

It is a new V008 schema. It is not represented as a recovered V007 schema.

## 2. Decision Unit record

Each materialized decision unit is a JSON object with exactly these fields, in the stated canonical order:

1. `decision_id`
2. `pair_id`
3. `condition`
4. `presentation`
5. `context`
6. `available_actions`
7. `future_structure`

### 2.1 decision_id

String.

Canonical value:

`D001` through `D420`, assigned in canonical pair/decision order.

### 2.2 pair_id

String.

Canonical value:

`P001` through `P210`.

Each pair has exactly two decision units.

### 2.3 condition

One of:

- `control`
- `treatment`
- `null`

The condition is part of the experimental assignment metadata but MUST NOT be exposed to the scientific agent.

For fixture materialization, the field exists in the canonical record for auditability; the agent-facing context excludes it.

### 2.4 presentation

One of:

- `I1_FIRST`
- `I2_FIRST`

Presentation is assignment metadata and MUST NOT be exposed to the scientific agent.

### 2.5 context

Object containing exactly:

- `items`
- `item_count`

`items` is an ordered array of the two decision alternatives, represented as:

`[{"id":"I1","action":"A"}, {"id":"I2","action":"B"}]`

or, when `presentation = I2_FIRST`:

`[{"id":"I2","action":"B"}, {"id":"I1","action":"A"}]`

Thus the presentation manipulation changes only the order in which the two alternatives are presented.

`item_count` is always `2`.

No condition, pair identity, variant label, utility, reward, value, performance, successor state, or future outcome is included in `context`.

### 2.6 available_actions

Ordered array:

`["A","B"]`

This is the complete action set available at decision time.

### 2.7 future_structure

Object with exactly:

- `successor_realized`
- `future_structure_available`

For control and null:

`{"successor_realized":false,"future_structure_available":false}`

For treatment:

`{"successor_realized":false,"future_structure_available":true}`

The treatment condition therefore provides future structural information without realizing a successor before the decision.

## 3. Agent-facing boundary

The scientific agent receives only:

- `context`
- `available_actions`
- `future_structure`

It does not receive:

- `decision_id`
- `pair_id`
- `condition`
- `presentation`

No field may encode condition, pair identity, or presentation indirectly.

## 4. Pair structure

There are exactly 210 pairs and 420 decision units.

Each pair contains exactly two decision units.

For each pair:

- one decision unit is assigned `I1_FIRST`;
- the other is assigned `I2_FIRST`;
- both share the same condition.

The two decisions therefore provide complementary presentation orders while preserving the pair-level condition.

## 5. Condition allocation

The generator assigns exactly:

- 70 control pairs;
- 70 treatment pairs;
- 70 null pairs.

Thus:

- 140 control decision units;
- 140 treatment decision units;
- 140 null decision units.

## 6. Action representation

The two alternatives have stable semantic identities:

- I1 → action A
- I2 → action B

The presentation field changes only their ordering in `context.items`.

## 7. Prohibited information

The schema MUST NOT include:

- utility;
- reward;
- value;
- performance feedback;
- observed successor;
- realized future state;
- outcome-dependent information;
- model/API response;
- scientific score.

## 8. Canonical serialization

The complete fixture MUST be serialized as UTF-8 JSON.

Rules:

- UTF-8 encoding;
- one JSON object per decision unit in canonical array order;
- object fields emitted in the exact order defined in §2;
- nested object fields emitted in the exact order defined above;
- arrays preserve their stated order;
- no insignificant whitespace;
- separators equivalent to JSON compact serialization: `,` and `:`;
- no ASCII-only escaping requirement;
- final newline: exactly one LF byte;
- no BOM.

The fixture top-level structure is:

`{"fixture_id":...,"schema_id":...,"generator_id":...,"seed":...,"decision_units":[...]}`

Top-level field order:

1. `fixture_id`
2. `schema_id`
3. `generator_id`
4. `seed`
5. `decision_units`

## 9. Provenance

The fixture metadata MUST contain:

- `fixture_id = "TI001-V008-FIXTURE-001"`
- `schema_id = "TI001-V008-DU-SCHEMA-001"`
- `generator_id = "TI001-V008-FIXTURE-GENERATOR-001"`
- `seed = 20260925`

The final fixture provenance record must additionally bind the exact generator source blob SHA and schema specification blob SHA.

## 10. Canonical decision-unit ordering

Decision units are ordered by:

1. pair_id lexical order P001 → P210;
2. within each pair, `I1_FIRST` then `I2_FIRST`.

Therefore:

- D001 = P001 / I1_FIRST;
- D002 = P001 / I2_FIRST;
- D003 = P002 / I1_FIRST;
- D004 = P002 / I2_FIRST;
- ...
- D419 = P210 / I1_FIRST;
- D420 = P210 / I2_FIRST.

## 11. Deterministic assignment boundary

Condition assignment and presentation assignment are generated according to the already approved V008 generator specification.

This schema does not redefine the PRNG, seed, or Fisher-Yates semantics.

## 12. Independent reconstruction

Executor-2 must be able to reconstruct the fixture using only:

- this schema specification;
- the approved V008 generator specification;
- the frozen generator source;
- the declared seed and constants.

Executor-2 MUST NOT read:

- the generated fixture;
- Executor-1 output;
- model/API responses;
- scientific results.

## 13. Scientific boundary

Schema specification and validation are pre-execution activities.

`scientific_execution = NOT_PERFORMED`

No model/API call is authorized by this artifact.

## 14. Approval state

This specification is **DESIGN — NOT APPROVED FOR GENERATION**.

Before generation:

1. compute and record the canonical schema specification blob SHA;
2. create and execute a schema integrity preflight;
3. verify exact field/order/visibility/serialization rules;
4. update the generator only if the approved schema requires it;
5. bind the generator source SHA;
6. obtain a generation gate PASS.

No fixture may be generated before these conditions are satisfied.
