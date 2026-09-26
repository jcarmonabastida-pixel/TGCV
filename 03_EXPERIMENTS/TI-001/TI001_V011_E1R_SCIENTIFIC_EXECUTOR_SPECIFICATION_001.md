# TI-001 V011 E1-R Scientific Executor Specification 001

**Status:** SPECIFICATION — NOT AUTHORIZED

## Purpose

Define the replacement Executor-1 for TI-001 V011 after E1 was found non-conformant because the runtime observed non-zero reasoning tokens while no explicit no-reasoning request was transmitted.

E1-R preserves the scientific fixture, interface, ordering and estimands. Its sole controlled runtime configuration change is an explicit provider parameter:

`reasoning={"effort":"none"}`

## Frozen bindings

- Fixture ID: `TI001-V011-FIXTURE-001`
- Fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`
- Generator Git blob SHA: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema Git blob SHA: `b2fef667f6eb33689ece5481957d3917a860dd3e`
- Decision-interface Git blob SHA: `8667b0ff70f58283c688f24c76f10db142655d14`
- Seed: `20260926`
- Model: `gpt-5.6-luna`
- Population: 420 decision units / 210 pairs.

## Controlled configuration

The Responses API request must include exactly:

`reasoning={"effort":"none"}`

The persisted generation configuration must contain the same semantic setting:

`"reasoning": {"effort": "none"}`

Current OpenAI model documentation lists GPT-5.6 Luna as supporting reasoning value `none`. citeturn241560search0

## Execution boundary

For each decision unit the provider receives only:
- the frozen decision instruction;
- `context`;
- `available_actions`;
- `future_structure`.

Exactly one provider call per unit. No retry, repair, inference, recode, imputation or replacement.

All 420 units are attempted once in canonical serialized order.

## Evidence boundary

The result is a new E1-R execution package and must remain separate from E1.

The package must preserve:
- decision identity/provenance;
- response ID/status;
- raw output representation;
- validated A/B decision or invalid status;
- timestamps;
- model and executor version;
- fixture/interface/generator/schema bindings;
- runtime metadata;
- observed reasoning-token usage.

## Authorization

This specification does not authorize execution. E1-R requires:
1. identity/compatibility preflight;
2. final preauthorization gate;
3. explicit user authorization;
4. scientific execution;
5. primary execution audit.

## Interpretation

E1 remains immutable and excluded from confirmatory analysis. E1-R is eligible for analysis only after its own primary execution audit confirms conformity.

No pooling of E1 and E1-R is permitted.
