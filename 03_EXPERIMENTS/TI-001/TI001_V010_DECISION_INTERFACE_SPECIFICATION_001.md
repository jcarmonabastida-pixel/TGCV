# TI-001 V010 Decision-Interface Specification 001

**Status:** SPECIFICATION — NOT AUTHORIZED

## Purpose

Define the model-facing decision interface required to obtain protocol-valid atomic A/B observations in TI-001 V010 after the V009 execution produced zero valid A/B outputs.

This specification changes only the operational decision interface. It does not modify the frozen V008 fixture, the scientific object, the experimental conditions, or the analysis definition.

## Scientific decision task

For each decision unit, the agent must select exactly one of the two actions supplied in `available_actions`.

The decision is made using only the agent-visible fields:
- `context`
- `available_actions`
- `future_structure`

The agent must not receive:
- `decision_id`
- `pair_id`
- `condition`
- `presentation`

## Model-facing instruction

The model-facing instruction shall explicitly state:

> Select exactly one action from the available actions.
>
> Your response must contain exactly one token: `A` or `B`.
>
> Do not output JSON, explanations, reasoning, punctuation, additional text, or any other content.

The instruction must be presented as task protocol, not as a scientific interpretation or hypothesis about the expected answer.

## Input boundary

The decision payload supplied with the instruction contains only the existing agent-visible V008 fields:

`context`, `available_actions`, and `future_structure`.

No hidden provenance field may be transmitted to the model.

The fixture values themselves remain unchanged.

## Output contract

A response is protocol-valid if and only if its normalized output is exactly one of:

- `A`
- `B`

No other output is valid.

Examples that remain invalid:
- `{"action":"A"}`
- `A because...`
- `The answer is A`
- `["A"]`
- `A,B`
- any JSON structure
- any natural-language response
- empty output
- truncated output

No invalid response may be recoded into A/B.

## Output normalization

Normalization may remove only transport-level surrounding whitespace required to identify the response token.

Normalization MUST NOT:
- parse JSON;
- extract an A/B value from a larger response;
- interpret natural language;
- select one value from multiple actions;
- infer an answer from the supplied structure.

## Protocol validation

V010 preflight must independently demonstrate that the implementation:
1. sends only the permitted visible fields plus the explicit decision instruction;
2. excludes hidden provenance;
3. requires exactly one A/B token;
4. rejects every non-atomic output;
5. performs no retry or recoding;
6. preserves the frozen fixture;
7. preserves the scientific object and analysis definition.

## Scientific invariants

Unchanged from V008/V009:
- 420 decision units / 210 pairs.
- 70 control / 70 treatment / 70 null.
- 105 I1_FIRST / 105 I2_FIRST.
- Scientific object: Transformational Intelligence.
- No value, reward, utility, performance, task-success, or external-outcome variable.
- No causal `ΔT_acc → ΔV` claim or analysis.
- No successor realization.
- No scientific analysis during execution.
- No interpretation of invalid responses as decisions.

## V010 status

This specification establishes the required interface but does not authorize scientific execution.

The implementation and its compatibility preflight must be completed before the V010 final pre-authorization gate.

**Disposition: NOT AUTHORIZED**
