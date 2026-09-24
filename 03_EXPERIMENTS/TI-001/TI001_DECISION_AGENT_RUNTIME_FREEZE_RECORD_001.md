# TI-001 Decision Agent Runtime Freeze Record 001

**Status:** RUNTIME IDENTIFICATION PENDING — SCIENTIFIC EXECUTION AUTHORIZED, NOT STARTED

## Verified frozen component

- Prompt version: `TI001_DECISION_AGENT_BASE_PROMPT_001`
- Base prompt SHA-256: `e451d2d89a353aa58030b3e59510837f5a664b186eb077662ae93376764f7006`
- External tools: disabled
- Web access: disabled
- File access: disabled
- Required output: single transformation identifier

## Model/runtime identification

The exact production model ID and serving-runtime identifier have **not yet been verified** from an authoritative runtime/API source.

The conversational label **GPT-5.6 Luna** must not be converted into an assumed API model ID. No unverified model identifier is frozen by this record.

The following fields remain unresolved and must be populated from the actual executable runtime before scientific execution:

- `model_id`
- `model_version`
- `runtime_id`
- `runtime_version`
- `API surface/version`
- generation configuration actually supported by that runtime

## Generation constraints

The decision runtime must:

- expose no external tools;
- receive only the frozen pre-decision input;
- produce exactly one executable transformation;
- preserve the frozen base prompt;
- record the actual runtime metadata returned by the serving system.

## Governance

The previously issued scientific authorization remains in force, but **no scientific execution may start until the unresolved runtime fields are verified and frozen**.

This record supersedes any earlier unverified runtime identification.

**Scientific execution: AUTHORIZED / NOT STARTED**
