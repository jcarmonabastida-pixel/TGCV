# TI-001 Decision Agent Runtime Freeze Record 001

**Status:** FROZEN RUNTIME — SCIENTIFIC EXECUTION AUTHORIZED, NOT STARTED

## 1. Model

- Provider: OpenAI
- Model ID: `gpt-5.6-luna`
- Reasoning effort: `none`
- Tools: disabled
- External information access: disabled
- Output modality: text
- Decision output constraint: exactly one executable transformation identifier

The model identifier is fixed rather than using a generic model alias.

## 2. Runtime

- API interface: Responses API
- Runtime configuration: no tools, no external retrieval, single decision request per instance
- Conversation state: isolated per instance
- Cross-instance state: disabled
- Temperature/sampling parameters: not set unless supported by the frozen model/API contract
- Maximum output: constrained by the decision output contract to the minimum response required for one transformation identifier

## 3. Prompt

- Base prompt: `03_EXPERIMENTS/TI-001/TI001_DECISION_AGENT_BASE_PROMPT_001.md`
- Prompt version: `TI001_DECISION_AGENT_BASE_PROMPT_001`
- Prompt content must be supplied exactly as frozen.
- Prompt hash must be recorded in the execution package before scientific observations are accepted.

## 4. Isolation

The runtime must not expose web search, file search, computer use, functions, prior conversation state, or any other external tool to the decision agent.

The only variable experimental information is the condition-specific input defined by the frozen fixture.

## 5. Reproducibility boundary

The following values must be recorded for every scientific run:

- model ID;
- API/runtime identifier and version where available;
- generation configuration actually applied;
- base-prompt SHA-256;
- fixture SHA-256;
- canonical package commit;
- execution timestamp.

If the provider exposes a more specific immutable model snapshot/version at execution time, that identifier must be recorded and used for the run.

## 6. Governance

This record freezes the runtime choice. It does not itself generate scientific observations and does not modify the fixture or estimand.

**Scientific execution remains AUTHORIZED but NOT STARTED.**
