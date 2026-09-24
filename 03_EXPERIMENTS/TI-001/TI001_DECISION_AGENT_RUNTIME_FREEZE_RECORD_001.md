# TI-001 Decision Agent Runtime Freeze Record 001

**Status:** RUNTIME IDENTIFICATION PRESERVED — SCIENTIFIC EXECUTION NOT STARTED

## Verified frozen component

- Prompt version: `TI001_DECISION_AGENT_BASE_PROMPT_001`
- Base prompt SHA-256: `e451d2d89a353aa58030b3e59510837f5a664b186eb077662ae93376764f7006`
- External tools: disabled
- Web access: disabled
- File access: disabled
- Required output: single transformation identifier

## Model/runtime identification

A technical runtime verification was performed against the executable decision runtime without executing TI-001 scientific inputs.

Verified runtime metadata:

- `model_id`: `gpt-5.6-luna`
- `API surface/version`: Responses API; API version not exposed by the serving response
- `model_version`: not exposed by the serving response
- `runtime_id`: not exposed by the serving response
- `runtime_version`: not exposed by the serving response

The OpenAI model catalogue identifies GPT-5.6 Luna by model ID `gpt-5.6-luna` and states that GPT-5.6 models are available through the Responses API. citeturn0search0

## Historical technical verification configuration

The earlier technical verification recorded the following request configuration:

- `temperature`: 0.0
- `top_p`: 0.98
- `max_output_tokens`: 16
- `tools`: []
- `tool_choice`: auto
- `background`: false
- `previous_response_id`: none
- `conversation`: none
- `reasoning`: none
- `store`: false
- runtime status: completed
- web search requests: 0

This historical configuration is preserved as observed evidence. It is **not** silently rewritten as the current scientific request configuration.

## Scientific request reconciliation

The first attempted TI-001 scientific request was rejected by the serving runtime before any scientific decision was generated because `temperature=0` was unsupported for the selected model.

Consequently:

- no scientific decision was generated;
- no scientific observation was produced;
- no scientific evidence package was created by that failed request;
- the historical `temperature=0.0` observation remains preserved;
- the current Provider 002 scientific request configuration omits `temperature`;
- `top_p=0.98` remains recorded as the current intended configuration, but its serving compatibility has **not** yet been independently demonstrated by a successful TI-001 scientific request;
- `max_output_tokens=16` remains the current intended configuration;
- unsupported parameters must not be added to the scientific request merely to reproduce the historical technical probe.

## Current scientific runtime configuration

For the reconciled Provider 002:

- `model_id`: `gpt-5.6-luna`
- `API surface`: Responses API
- `temperature`: omitted
- `top_p`: 0.98
- `max_output_tokens`: 16
- `tools`: []
- `tool_choice`: auto
- `background`: false
- `previous_response_id`: none
- `conversation`: none
- `reasoning`: none
- `store`: false

The current configuration is **identified and reconciled but not yet scientifically runtime-validated**.

## Generation constraints

The decision runtime must:

- expose no external tools;
- receive only the frozen pre-decision input;
- produce exactly one executable transformation;
- preserve the frozen base prompt;
- record the actual runtime metadata returned by the serving system;
- use the reconciled Provider 002 request configuration;
- not include `temperature`.

## Runtime identification disposition

The executable runtime has provided a concrete `model_id` and the historical technical verification provided a concrete generation configuration. The serving response does not expose `model_version`, `runtime_id`, or `runtime_version`, and therefore these fields remain recorded explicitly as **not exposed by the serving response**, rather than inferred or fabricated.

The rejected scientific request establishes a serving incompatibility for `temperature=0` in the selected model. It does not establish successful serving compatibility for the remaining request parameters.

## Governance

This record supersedes the prior disposition of the runtime freeze record.

The historical technical verification remains immutable in substance and is distinguished from the current scientific request configuration.

The Provider 002 preflight is the current static/canonical preflight. Scientific execution remains blocked pending explicit reauthorization.

**Scientific execution: NOT AUTHORIZED / BLOCKED PENDING REAUTHORIZATION**

No TI-001 scientific decision input has been used in the reconciled runtime freeze record.