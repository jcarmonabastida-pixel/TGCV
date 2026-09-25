# TI-001 V008 Provider–Contract Compatibility Specification 001

**Status:** DESIGN — IMPLEMENTATION NOT AUTHORIZED

## 1. Purpose

Define the runtime interface required to consume the canonical V008 decision-unit schema without silently reusing the V007 runtime contract and without changing the scientific design.

This specification is a compatibility/design gate. It authorizes neither fixture generation nor scientific execution.

## 2. Canonical V008 inputs

Schema ID:
`TI001-V008-DU-SCHEMA-001`

Schema blob:
`d9539790452b047bc845a19bdcf50b8713a42b2a`

Generator ID:
`TI001-V008-FIXTURE-GENERATOR-001`

Seed:
`20260925`

The provider consumes one V008 decision unit at a time.

## 3. Provider-consumed fields

The provider may consume only:

- `context`
  - `items`
  - `item_count`
- `available_actions`
- `future_structure`

The provider must not consume:

- `decision_id`
- `pair_id`
- `condition`
- `presentation`

The hidden fields remain available to the execution/audit layer but must never enter the model-facing request.

## 4. Model-facing semantic mapping

V008:

`context.items` represents the ordered decision context.

`available_actions = ["A","B"]` is the complete action space.

`future_structure` is the only future-structure information available to the agent and is determined by the V008 condition assignment:

- control: `successor_realized=false`, `future_structure_available=false`
- null: `successor_realized=false`, `future_structure_available=false`
- treatment: `successor_realized=false`, `future_structure_available=true`

The provider must not expose a realized successor, outcome, reward, value, performance feedback, or utility.

## 5. Presentation semantics

The provider must preserve the exact order of `context.items` supplied by the V008 decision unit.

It must not infer or reconstruct presentation from hidden `presentation`, `pair_id`, or `condition`.

The reconciled V008 generator/schema binding remains authoritative for pair-level presentation orientation.

## 6. Response contract

The provider must accept exactly one observable decision response:

- `A`
- `B`

Any other response is invalid.

Invalid responses must not be silently recoded or retried.

## 7. Runtime configuration boundary

The V008 runtime contract must explicitly bind:

- model identity;
- API surface;
- generation configuration;
- tools = none;
- conversation state = none;
- previous response = none;
- external tool use = none;
- explicit execution switch;
- scientific execution state.

The provider may contain an execution path, but import/preflight/design operations must never invoke a scientific API call.

## 8. V007 reuse rule

The V007 Provider and V007 Execution Contract are not V008 bindings.

The V007 implementation may be used as implementation reference only.

No V007 fixture identity, V007 schema structure, V007 fixture hash, or V007 contract identity may be silently inherited.

## 9. Required implementation form

A V008 provider implementation shall either:

1. be a new V008 provider; or
2. be an explicitly versioned adapter whose interface is independently bound to this specification.

In either case, its Git blob identity must be recorded and verified before scientific execution.

## 10. Required preflight checks

Before runtime authorization, a V008 Provider–Contract Compatibility Preflight must verify at minimum:

- provider identity;
- provider Git blob SHA;
- schema ID and schema Git blob SHA;
- exact seven-field schema consumption;
- hidden-field isolation;
- exact A/B action space;
- context item ordering preservation;
- future-structure isolation;
- no successor/outcome/value/reward/performance leakage;
- no external tools;
- no conversation state;
- no retry/recode;
- explicit execution gate;
- scientific execution remains NOT_PERFORMED;
- V007 identities are not silently bound;
- response validation accepts only A/B.

## 11. Authorization boundary

This specification does not authorize:

- generation of the V008 fixture;
- model/API calls;
- scientific execution;
- scientific result production.

Those require separate gates and explicit authorization.

## 12. Decision

**V008 Provider–Contract design is defined.**

The next gate is implementation of the V008 provider/adapter followed by a dedicated compatibility preflight.

**Fixture generated:** false

**Scientific execution:** NOT_PERFORMED
