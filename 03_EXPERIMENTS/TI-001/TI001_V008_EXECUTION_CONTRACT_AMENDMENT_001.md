# TI-001 V008 Execution Contract Amendment 001

**Status:** READY FOR FINAL PRE-AUTHORIZATION — SCIENTIFIC EXECUTION NOT AUTHORIZED

## Purpose

This amendment reconciles the canonical V008 Execution Contract with the scientific Executor-1 runner that has passed its dedicated identity preflight.

## Base contract

- Contract: `TI001_V008_EXECUTION_CONTRACT_001.json`
- Contract blob SHA-1: `64efcdad2aa0be52774588c90956087426d67d9d`
- Scientific execution remains: `NOT_AUTHORIZED`

## Scientific Executor-1 binding

- Executor ID: `TI001-V008-SCIENTIFIC-EXECUTOR-1-001`
- Runner path: `03_EXPERIMENTS/TI-001/TI001_V008_SCIENTIFIC_EXECUTOR_1_001.py`
- Runner Git blob SHA-1: `04a1b6cf37197499988579e5636c72a445a03a16`
- Identity preflight: `TI001-V008-SCIENTIFIC-EXECUTOR-1-IDENTITY-PREFLIGHT-001`
- Identity preflight status: `PASS`
- Identity preflight result: `TI001_V008_SCIENTIFIC_EXECUTOR_1_IDENTITY_PREFLIGHT_RESULT_001.json`
- Scientific execution during identity preflight: `NOT_PERFORMED`

## Bound runtime

- Model: `gpt-5.6-luna`
- API: `Responses API`
- temperature: omitted
- top_p: `0.98`
- max_output_tokens: `16`
- tools: `[]`
- conversation: `null`
- previous_response_id: `null`
- store: `false`

## Binding invariants

The scientific Executor-1 must consume only the agent-visible fields defined by the canonical decision-unit schema: `context`, `available_actions`, and `future_structure`.

The runner must not expose `decision_id`, `pair_id`, `condition`, or `presentation` to the model; must not realize a successor before the decision; must accept only A/B; and must not retry or recode invalid responses.

The runner performs no scientific analysis and does not authorize itself.

## Authorization boundary

This amendment does **not** authorize scientific execution.

Scientific execution remains blocked until the final pre-authorization gate passes all bound preconditions and a separate execution authorization record is created following explicit user authorization.

**scientific_execution:** `NOT_AUTHORIZED`
