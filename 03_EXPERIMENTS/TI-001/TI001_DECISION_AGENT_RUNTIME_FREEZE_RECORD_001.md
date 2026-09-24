# TI-001 Decision Agent Runtime Freeze Record 001

**Status:** RUNTIME IDENTIFICATION VERIFIED WHERE EXPOSED — SCIENTIFIC EXECUTION NOT STARTED

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

Generation configuration actually observed:

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

Local execution environment observed during the technical verification:

- Python: 3.14.7
- Windows: 11, build 10.0.26200
- OpenAI SDK: 3.19.2

The conversational label **GPT-5.6 Luna** is not used as a substitute for the runtime metadata above.

## Generation constraints

The decision runtime must:

- expose no external tools;
- receive only the frozen pre-decision input;
- produce exactly one executable transformation;
- preserve the frozen base prompt;
- record the actual runtime metadata returned by the serving system.

The technical verification observed `tools=[]`, completed execution, and zero web-search requests.

## Runtime identification disposition

The executable runtime has provided a concrete `model_id` and generation configuration. The serving response does not expose `model_version`, `runtime_id`, or `runtime_version`, and therefore these fields are recorded explicitly as **not exposed by the serving response**, rather than inferred or fabricated.

This record therefore distinguishes verified runtime metadata from metadata unavailable through the serving interface.

## Governance

This record supersedes the earlier pending runtime-identification wording.

The previously issued scientific authorization remains in force, but **scientific execution must not start until governance accepts the disposition of the runtime fields that are not exposed by the serving response and, if required, freezes that disposition explicitly**.

No TI-001 scientific decision input was used in the technical runtime verification.

**Scientific execution: AUTHORIZED / NOT STARTED**
