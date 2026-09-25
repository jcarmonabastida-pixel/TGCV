# TI-001 V008 Runtime Compatibility Preflight Specification 001

**Status:** READY — SCIENTIFIC EXECUTION NOT AUTHORIZED

## Purpose

Verify that the bound V008 runtime configuration is technically compatible with the frozen provider contract before any scientific decision input is submitted.

## Canonical bindings

- Fixture: `TI001-V008-FIXTURE-001`
- Fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- Provider: `TI001-V008-DECISION-AGENT-PROVIDER-001`
- Provider blob SHA-1: `c7d066de3481143d878f06bb2c1d791cb7dc54e1`
- Schema: `TI001-V008-DU-SCHEMA-001`
- Schema blob SHA-1: `d9539790452b047bc845a19bdcf50b8713a42b2a`
- Contract: `TI001_V008_EXECUTION_CONTRACT_001`
- Model: `gpt-5.6-luna`
- API surface: Responses API
- Tools: none
- Temperature: omitted
- Top-p: 0.98
- Max output tokens: 16
- Reasoning: none
- Conversation state: none
- Previous response: none
- Store: false

## Required checks

1. Exact provider and schema identities are bound.
2. Exact frozen fixture identity is bound.
3. Runtime model/API identity is bound.
4. No unsupported `temperature` parameter is supplied.
5. Runtime request contains no external tools.
6. No conversation state or previous response is supplied.
7. Provider accepts only A/B responses.
8. Invalid responses are not retried or recoded.
9. Hidden V008 fields cannot enter the model-facing input.
10. No successor is realized before the decision.
11. No outcome, reward, value, utility or performance feedback is supplied.
12. Scientific fixture inputs are not consumed by the compatibility test.
13. A separate diagnostic/non-scientific request must demonstrate serving compatibility of the intended request surface, including `top_p=0.98`, without consuming any V008 decision unit.
14. The diagnostic response must complete normally and expose a valid response object; it is infrastructure evidence only.
15. `scientific_execution` remains `NOT_PERFORMED`.

## Scientific boundary

This preflight must not submit any of the 420 frozen decision units and must not produce scientific decisions, scores or evidence.

A diagnostic serving request, if required to establish runtime compatibility, is strictly non-scientific and must use no V008 fixture decision input.

## Decision rule

PASS only if every required check passes and the diagnostic runtime test, where required, demonstrates compatibility of the exact intended scientific request surface.

A PASS does not authorize scientific execution.

**Scientific execution: NOT_AUTHORIZED**
