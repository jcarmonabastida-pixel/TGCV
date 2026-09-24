# TI-001 Decision Agent Runtime Freeze Record 001

**Status:** FROZEN — SCIENTIFIC EXECUTION AUTHORIZED, NOT STARTED

## Frozen runtime

- Model ID: `gpt-5.6-luna`
- Model family: GPT-5.6 Luna
- API: OpenAI Responses API
- Runtime capture date: 2026-09-24
- Reasoning configuration: `none`
- External tools: disabled
- Prompt version: `TI001_DECISION_AGENT_BASE_PROMPT_001`
- Base prompt SHA-256: `e451d2d89a353aa58030b3e59510837f5a664b186eb077662ae93376764f7006`

The OpenAI model catalogue identifies GPT-5.6 Luna with model ID `gpt-5.6-luna` and lists it as available through the Responses API. The catalogue also lists reasoning levels including `none`. The exact model ID above, rather than the conversational model label, is the experimental runtime identifier.

## Generation configuration

- output format: single transformation identifier
- temperature: not set
- tools: none
- web access: none
- file access: none
- external context: none
- reasoning: `none`

## Reproducibility boundary

The runtime identifier, prompt hash, API surface, reasoning configuration, tool restrictions, and output contract are frozen for the first TI-001 run.

If the serving platform reports an additional runtime/model revision identifier at execution time, that identifier must be persisted in the execution record. A change in model ID, prompt, reasoning configuration, tool access, or output contract after the first scientific observation constitutes a protocol deviation.

## Authorization state

This runtime freeze does not modify the already issued scientific authorization.

**Scientific execution: AUTHORIZED / NOT STARTED**
