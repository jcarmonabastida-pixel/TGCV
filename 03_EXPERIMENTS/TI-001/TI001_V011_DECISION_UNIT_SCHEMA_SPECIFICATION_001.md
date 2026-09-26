# TI-001 V011 Decision Unit Schema Specification 001

**Status:** SCHEMA FROZEN — NOT GENERATED

## 1. Identity

- Schema ID: `TI001-V011-DU-SCHEMA-001`
- Fixture ID: `TI001-V011-FIXTURE-001`
- Generator ID: `TI001-V011-FIXTURE-GENERATOR-001`
- Seed: `20260926`

## 2. Decision-unit record

Each decision unit is a JSON object with exactly these top-level fields, in this order:

1. `decision_id`
2. `pair_id`
3. `condition`
4. `presentation`
5. `context`
6. `available_actions`
7. `future_structure`

No additional top-level field is permitted.

## 3. Identity fields

### decision_id

String, exactly `D001` through `D420`, assigned in canonical pair order.

### pair_id

String, exactly `P001` through `P210`.

Each pair has exactly two decision units.

### condition

Exactly one of:

- `control`
- `treatment`
- `null`

The field is hidden provenance and must not be exposed to the model.

### presentation

Exactly one of:

- `I1_FIRST`
- `I2_FIRST`

The field is hidden provenance and must not be exposed to the model.

## 4. Context

`context` is an object with exactly two fields, in this order:

1. `items`
2. `item_count`

`item_count` is always integer `2`.

For `I1_FIRST`:

`items = [{"id":"I1","action":"A"},{"id":"I2","action":"B"}]`

For `I2_FIRST`:

`items = [{"id":"I2","action":"B"},{"id":"I1","action":"A"}]`

Presentation therefore changes only ordering, not the identity/action mapping.

No condition, pair identity, utility, reward, value, performance, successor state, future outcome, or response information may occur in context.

## 5. Available actions

Exactly:

`["A","B"]`

No additional action is permitted.

## 6. Future structure

`future_structure` is an object with exactly these fields, in this order:

1. `successor_realized`
2. `future_structure_available`

For `control` and `null`:

`{"successor_realized":false,"future_structure_available":false}`

For `treatment`:

`{"successor_realized":false,"future_structure_available":true}`

Thus treatment exposes future structural information without realizing a successor.

## 7. Agent-visible boundary

The model receives only:

- `context`
- `available_actions`
- `future_structure`

The model must not receive:

- `decision_id`
- `pair_id`
- `condition`
- `presentation`

The interface must preserve this exact visibility boundary.

## 8. Pair invariant

Every pair contains exactly:

- one `I1_FIRST` decision unit;
- one `I2_FIRST` decision unit;
- the same condition in both units.

The presentation order does not alter condition assignment.

## 9. Population invariants

The complete fixture must contain:

- 420 decision units;
- 210 unique pairs;
- 70 control pairs;
- 70 treatment pairs;
- 70 null pairs;
- 140 decision units per condition;
- 210 I1_FIRST units;
- 210 I2_FIRST units.

At pair level, exactly 35 pairs per condition have `I1_FIRST` as their first materialized unit and 35 have `I2_FIRST` as their first materialized unit.

## 10. Serialization

The containing fixture must be UTF-8 JSON.

Decision-unit objects must preserve the exact field order specified above. Nested objects and arrays must preserve the exact orders specified above.

Fixture serialization is compact JSON, without BOM, with exactly one final LF.

## 11. Prohibited content

The schema and generated fixture must not contain:

- value;
- reward;
- utility;
- performance;
- task success;
- external outcome;
- realized successor;
- model/API response;
- scientific score;
- post-hoc analysis.

## 12. Scientific boundary

This schema defines only the experimental input object.

It does not authorize:
- fixture generation;
- model execution;
- scientific analysis;
- interpretation.

## 13. Approval

**Schema status: FROZEN.**

Before fixture generation, the schema Git blob SHA must be bound into the generator identity/integrity preflight.

**Fixture: NOT GENERATED.**

**Scientific execution: NOT AUTHORIZED.**
