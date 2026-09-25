# TI-001 V008 Provider–Contract Compatibility Gate 001

**Status:** BLOCKED — V007 RUNTIME CONTRACT NOT COMPATIBLE WITH V008 SCHEMA

## Evidence reviewed

### V007 Provider

Path:
`03_EXPERIMENTS/TI-001/TI001_V007_DECISION_AGENT_PROVIDER_001.py`

Provider identity:
`TI001_DECISION_AGENT_PROVIDER_V007_001`

The V007 provider expects:
- a V007 fixture with `fixture_id = TI001-v007-candidate-001`;
- V007 fixture version `v007-candidate-001`;
- V007 fixture structure containing `pairs`, `instances`, `agent_view`, `state`, `available_transformations`, and `task`;
- a separate decision-units package whose units are zipped with V007 fixture instances;
- V007-specific fixture hash validation.

Its preflight record is:
`TI001_V007_DECISION_AGENT_PROVIDER_PREFLIGHT_004.json`

That record binds the provider to the V007 fixture identity and records `scientific_execution = NOT_PERFORMED`.

### V007 Execution Contract

Path:
`03_EXPERIMENTS/TI-001/TI001_V007_EXECUTION_CONTRACT_001.json`

Contract identity:
`TI001_V007_EXECUTION_CONTRACT_001`

The contract binds runtime execution to the V007 fixture identity:
`TI001-v007-candidate-001`

and to the V007 fixture blob:
`663383b27b567d73757ac967986d0b9b949dc50e`.

### V008 Decision Unit Schema

V008 schema identity:
`TI001-V008-DU-SCHEMA-001`

Current schema blob:
`d9539790452b047bc845a19bdcf50b8713a42b2a`

V008 materialized decision units have the exact seven fields:
`decision_id`, `pair_id`, `condition`, `presentation`, `context`, `available_actions`, `future_structure`.

The V008 agent-facing representation is structurally different from the V007 provider input contract.

## Compatibility finding

V007 Provider and V007 Execution Contract cannot be treated as implicitly reusable by V008.

Concrete incompatibilities:

1. **Fixture identity mismatch**
   V007 requires `TI001-v007-candidate-001`; V008 has a distinct fixture/schema identity.

2. **Schema mismatch**
   V007 expects `pairs/instances/agent_view`; V008 specifies top-level `decision_units` with the seven canonical fields.

3. **Field contract mismatch**
   V007 provider constructs its input from `state`, `available_transformations`, and `task`; V008 specifies `context.items`, `context.item_count`, `available_actions`, and `future_structure`.

4. **Presentation semantics**
   V008 explicitly binds presentation order to the reconciled pair-level presentation stream. The V007 runtime contract does not establish this V008 schema binding.

5. **Binding identity**
   The V007 provider preflight is explicitly bound to V007 fixture identity and therefore does not constitute a V008 compatibility preflight.

## Consequence

The existing V007 Provider and Contract may be used as **source material for a compatibility assessment**, but they are not currently authorized as the V008 runtime binding.

No V008 fixture generation is blocked by the provider itself; however, **V008 runtime readiness cannot be declared until the Provider–Contract interface is explicitly designed/bound to the V008 schema**.

## Required next gate

Create a V008 Provider–Contract compatibility/design specification that explicitly determines whether:

- a V008 adapter/provider revision can consume the V008 decision-unit schema without changing the scientific semantics; or
- a distinct V008 provider and/or execution contract must be created.

Any resulting implementation must receive its own integrity/binding preflight before scientific execution.

**Scientific execution:** NOT_PERFORMED

**Fixture generated:** false
