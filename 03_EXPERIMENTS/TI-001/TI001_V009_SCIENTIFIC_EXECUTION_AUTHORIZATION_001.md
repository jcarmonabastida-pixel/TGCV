# TI-001 V009 Scientific Execution Authorization 001

**Status:** AUTHORIZATION RECORD — AWAITING EXPLICIT USER AUTHORIZATION

## Bound gate

- Final Pre-Authorization Gate: `TI001-V009-FINAL-PREAUTHORIZATION-GATE-001`
- Final gate status: `PASS`
- Gate result commit: `ae78348c6f73f32d82a91a0a29f6d963dc032fcb`
- Scientific execution: `NOT_PERFORMED`

## Bound runtime

- Scientific Executor-1: `TI001-V009-SCIENTIFIC-EXECUTOR-1-001`
- Runner commit: `2618c1ca6191bb616c9c3b064234b062b98ae68b`
- Model: `gpt-5.6-luna`
- API: `Responses API`
- top_p: `0.98`
- max_output_tokens: `64`
- reasoning: `{"effort":"none"}`
- temperature: omitted
- tools: none
- conversation: none
- previous_response_id: none
- store: false

## Bound scientific fixture

- Fixture: V008 frozen canonical fixture
- Fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- Decision units: 420
- Pairs: 210
- Conditions: 70 control / 70 treatment / 70 null
- Valid decision outputs: A / B

## Scientific object

**Transformational Intelligence.**

The experiment asks whether an agent, when provided information about a future transformation structure, modifies its present decision systematically in orientation to that future structure.

This is **not** a causal value experiment. No value, reward, utility, performance, task-success, or external-outcome measure is introduced.

## Execution boundary

If explicitly authorized, the bound scientific runner may execute the frozen fixture under the V009 runtime correction.

The runner must:
- expose only `context`, `available_actions`, and `future_structure`;
- keep `decision_id`, `pair_id`, `condition`, and `presentation` hidden;
- realize no successor before the decision;
- accept only A/B;
- perform no retry or recoding;
- perform no scientific analysis during execution;
- persist the raw response/provenance required by the contract.

## Explicit authorization

**No scientific execution is authorized by this record yet.**

The user must explicitly authorize execution in the conversation before the runner is executed.

Suggested authorization text:

> «Autorizo la ejecución científica de TI-001 V009.»

