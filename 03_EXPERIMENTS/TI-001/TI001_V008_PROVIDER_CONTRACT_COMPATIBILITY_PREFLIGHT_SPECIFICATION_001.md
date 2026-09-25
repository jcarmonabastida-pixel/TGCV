# TI-001 V008 Provider–Contract Compatibility Preflight Specification 001

**Status:** READY — EXECUTION NOT PERFORMED

## Canonical bindings

- Provider: `TI001_V008_DECISION_AGENT_PROVIDER_001.py`
- Provider commit: `283a25017d3fcad753c9919129c83aa8c1070667`
- Provider Git blob SHA-1: `c7d066de3481143d878f06bb2c1d791cb7dc54e1`
- Provider ID: `TI001-V008-DECISION-AGENT-PROVIDER-001`
- Schema ID: `TI001-V008-DU-SCHEMA-001`
- Schema Git blob SHA-1: `d9539790452b047bc845a19bdcf50b8713a42b2a`

## Required checks

1. Provider exists and identity matches.
2. Provider blob SHA matches the canonical binding.
3. Schema identity and blob SHA match.
4. The provider consumes exactly the V008 seven-field decision-unit boundary.
5. Hidden fields are excluded from model-facing input.
6. Context contains exactly `items` and `item_count`.
7. Context ordering is preserved.
8. Available actions are exactly `["A","B"]`.
9. Future structure contains exactly the two canonical fields.
10. `successor_realized` must be false.
11. No successor, outcome, reward, value, utility, or performance feedback is introduced.
12. No V007 fixture/contract identity is bound.
13. Invalid responses are rejected; no retry/recode is defined.
14. No external tools or conversation state are introduced.
15. Scientific execution remains `NOT_PERFORMED`.
16. No model/API call occurs during preflight.

## Boundary

This preflight validates runtime compatibility only. It does not generate the V008 fixture and does not authorize scientific execution.

**Fixture generated:** false

**Scientific execution:** NOT_PERFORMED
