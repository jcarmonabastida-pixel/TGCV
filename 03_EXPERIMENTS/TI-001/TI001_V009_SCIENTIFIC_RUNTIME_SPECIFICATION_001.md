# TI-001 V009 Scientific Runtime Specification 001

**Status:** SPECIFICATION ONLY — SCIENTIFIC EXECUTION NOT AUTHORIZED

## Purpose

Define the runtime correction required to repeat TI-001 after V008 produced 420/420 incomplete responses because the 16-token output budget was consumed by reasoning.

V008 remains immutable and is not reinterpreted.

## Runtime

- model: `gpt-5.6-luna`
- API: Responses API
- top_p: `0.98`
- max_output_tokens: `64`
- temperature: omitted
- reasoning: `{"effort":"none"}`
- tools: `[]`
- tool_choice: `auto`
- background: `false`
- store: `false`
- previous_response_id: `null`
- conversation: `null`

The explicit reasoning setting is the runtime mechanism recovered from TI-001 V006 and validated non-scientifically by V009 Runtime Diagnostic 002.

## Scientific invariants

Unchanged from the V008 frozen design:

- same frozen V008 fixture
- same 420 decision units / 210 pairs
- same 70 control / 70 treatment / 70 null units
- same A/B decision space
- same visible fields: context, available_actions, future_structure
- same hidden provenance fields
- no successor realization
- no value, reward, utility, performance or task-success variable
- no retry or recoding
- no scientific analysis during execution

## Interpretation boundary

V009 is a runtime-corrected repeat of the TI-001 experiment. It tests the same Transformational Intelligence observable under a runtime configuration that has passed non-scientific compatibility validation.

This specification does not authorize scientific execution.

**Next gate:** V009 scientific execution contract and runner binding.
