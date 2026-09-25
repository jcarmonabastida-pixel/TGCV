# TI-001 V009 Scientific Execution Authorization 001

**Status:** AUTHORIZED — SCIENTIFIC EXECUTION MAY PROCEED

## Explicit user authorization

The user explicitly authorized scientific execution of TI-001 V009 on 2026-09-25.

Authorization text:
> «Autorizo la ejecución científica de TI-001 V009.»

## Bound preconditions

- Final Pre-Authorization Gate: `TI001-V009-FINAL-PREAUTHORIZATION-GATE-001`
- Final gate status: `PASS`
- Gate result commit: `ae78348c6f73f32d82a91a0a29f6d963dc032fcb`
- Scientific Executor-1: `TI001-V009-SCIENTIFIC-EXECUTOR-1-001`
- Runner commit: `2618c1ca6191bb616c9c3b064234b062b98ae68b`
- Fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- Decision units: 420
- Valid outputs: A / B
- Scientific object: Transformational Intelligence

## Bound runtime

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

## Execution boundary

Authorization permits the bound scientific Executor-1 to execute the frozen V008 fixture under the V009 runtime contract.

The executor must:
- expose only `context`, `available_actions`, and `future_structure`;
- keep `decision_id`, `pair_id`, `condition`, and `presentation` hidden;
- realize no successor before the decision;
- accept only A/B as valid decision outputs;
- perform no retry or recoding;
- perform no scientific analysis during execution;
- persist raw response/provenance required by the execution contract.

## Interpretation boundary

This is an experiment of **Transformational Intelligence**. It is not a causal `ΔT_acc → ΔV` experiment. No value, reward, utility, performance, task-success, or external-outcome measure is introduced.

## Authorization status

**scientific_execution:** `AUTHORIZED`

This record authorizes execution but does not itself constitute execution evidence. Execution evidence must be produced by the scientific runner and audited separately.
