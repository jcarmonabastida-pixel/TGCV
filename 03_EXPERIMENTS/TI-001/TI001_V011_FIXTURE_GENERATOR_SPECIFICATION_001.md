# TI-001 V011 Fixture Generator Specification 001

**Status:** GENERATOR SPECIFICATION — SEED FROZEN / FIXTURE NOT GENERATED

## 1. Generator identity

- Generator ID: `TI001-V011-FIXTURE-GENERATOR-001`
- Fixture ID: `TI001-V011-FIXTURE-001`
- Generator type: deterministic
- Scientific execution: NOT AUTHORIZED
- Fixture generation: not yet performed

## 2. Frozen seed

- Seed: `20260926`

The seed is part of the generator contract. The same generator source, specification, and seed must reproduce the same fixture byte-for-byte.

## 3. Population

The generated fixture must contain exactly:

- 210 unique pairs;
- 420 decision units;
- 70 pairs in control;
- 70 pairs in treatment;
- 70 pairs in null;
- 35 pairs per condition × presentation;
- 210 I1_FIRST decision units;
- 210 I2_FIRST decision units.

Each pair must contain exactly two decision units:
- one I1_FIRST;
- one I2_FIRST.

## 4. Assignment procedure

Pair IDs are assigned deterministically in canonical order.

For each condition, exactly 70 pair IDs are assigned.

Within each condition, exactly 35 pairs are assigned to the I1_FIRST/I2_FIRST orientation class through the deterministic seeded assignment procedure.

Each pair then emits exactly two decision units, one for each orientation.

No model output is involved in fixture generation.

## 5. Required decision-unit schema

Every decision unit must contain exactly these top-level fields:

- `decision_id`
- `pair_id`
- `condition`
- `presentation`
- `context`
- `available_actions`
- `future_structure`

The model-visible fields are:

- `context`
- `available_actions`
- `future_structure`

The following are hidden provenance fields:

- `decision_id`
- `pair_id`
- `condition`
- `presentation`

## 6. Action space

Every decision unit must expose exactly two selectable actions:

- `A`
- `B`

No additional action is permitted.

## 7. Presentation construction

The fixture must explicitly encode the presentation orientation.

For every pair:

- I1_FIRST unit presents the first decision item before the second according to the frozen presentation rule;
- I2_FIRST unit reverses that presentation order according to the same rule.

The underlying paired decision content must remain invariant except for the presentation transformation defined by the specification.

## 8. Condition construction

The generator must implement the frozen condition semantics from the V011 experiment specification.

The generator must not use model responses, external outcomes, reward, utility, performance, or task-success information.

## 9. Determinism requirements

The generator must:

1. initialize the pseudorandom generator exclusively from the frozen seed;
2. use a documented deterministic assignment order;
3. avoid time, process ID, filesystem order, network state, or nondeterministic iteration as generation inputs;
4. emit canonical JSON with stable ordering and encoding;
5. make no external API calls.

## 10. Integrity requirements

After generation, the fixture must be checked for:

- exactly 420 decision units;
- exactly 210 unique pairs;
- exactly two units per pair;
- exactly one I1_FIRST and one I2_FIRST per pair;
- exactly 70 pairs per condition;
- exactly 35 pairs per condition × presentation;
- exactly 210 units per presentation;
- exactly 140 decision units per condition;
- exactly A/B as the action set;
- exact visible/hidden field partition;
- no duplicate decision IDs;
- no duplicate pair IDs;
- deterministic reconstruction from the frozen seed.

The fixture SHA-256 must be computed and bound to the resulting manifest.

## 11. Independence boundary

The generator may depend only on this specification and its own source plus deterministic local standard-library functionality.

It must not import, execute, parse, or consume:
- Executor-1 outputs;
- Executor-2 outputs;
- V010 scientific results;
- model responses;
- post-hoc observations.

V010 findings motivate the design but are not inputs to fixture generation.

## 12. Pre-generation gate

Before implementation or execution of the generator, the following must be checked:

- specification is canonical;
- seed is fixed;
- population counts are fixed;
- schema is fixed;
- condition semantics are fixed;
- presentation construction is fixed;
- deterministic serialization is fixed;
- integrity criteria are fixed.

The pre-generation gate does not authorize scientific model execution.

## 13. Current disposition

**Generator specification: FROZEN.**

**Seed: FROZEN — `20260926`.**

**Fixture: NOT GENERATED.**

**Scientific execution: NOT AUTHORIZED.**

The next action is to implement the deterministic V011 fixture generator and run a generator-only identity/integrity preflight before generating the scientific fixture.
