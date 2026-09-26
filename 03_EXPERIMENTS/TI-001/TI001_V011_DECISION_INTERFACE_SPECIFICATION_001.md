# TI-001 V011 Decision-Interface Specification 001

**Status:** INTERFACE SPECIFICATION — NOT AUTHORIZED

## 1. Purpose

Define the frozen model-facing decision interface for TI-001 V011 so that the canonical V011 fixture can be bound to an execution implementation without exposing hidden provenance or changing the scientific object.

This specification does not authorize scientific execution.

## 2. Scientific decision task

For each decision unit, the agent must select exactly one action from the two actions supplied in `available_actions`.

The agent-visible fields are exactly:

- `context`
- `available_actions`
- `future_structure`

The following fixture fields are hidden provenance and must not be transmitted:

- `decision_id`
- `pair_id`
- `condition`
- `presentation`

## 3. Model-facing instruction

The model-facing instruction is exactly:

> Select exactly one action from the available actions.
>
> Your response must contain exactly one token: `A` or `B`.
>
> Do not output JSON, explanations, reasoning, punctuation, additional text, or any other content.

No scientific hypothesis, expected answer, condition label, or interpretation may be added to this instruction.

## 4. Input boundary

For each canonical V011 decision unit, the execution implementation may transmit only the authorized visible fields:

`context`, `available_actions`, and `future_structure`.

The implementation must preserve their values exactly as supplied by the canonical fixture.

No hidden provenance field, pair identity, condition identity, presentation identity, response history, or analysis result may be transmitted.

## 5. Output contract

A response is protocol-valid if and only if, after the predefined transport-level surrounding-whitespace normalization, it is exactly one token:

- `A`
- `B`

All other outputs are invalid.

The validator must not parse, extract, repair, infer, recode, retry, or otherwise transform an invalid response into A/B.

## 6. Normalization boundary

Normalization may remove only surrounding transport-level whitespace needed to identify the response token.

Normalization must not:

- parse JSON;
- extract A/B from natural language;
- extract A/B from multiple tokens;
- interpret explanations;
- choose among multiple actions;
- infer an answer from the future structure;
- retry an invalid response.

## 7. Fixture binding

The interface implementation must bind to:

- Fixture ID: `TI001-V011-FIXTURE-001`
- Schema ID: `TI001-V011-DU-SCHEMA-001`
- Generator ID: `TI001-V011-FIXTURE-GENERATOR-001`
- Fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`
- Generator Git blob SHA: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema Git blob SHA: `b2fef667f6eb33689ece5481957d3917a860dd3e`
- Seed: `20260926`

A mismatch in any binding identifier or hash blocks execution.

## 8. Scientific invariants

V011 remains a decision-level Transformational Intelligence experiment.

The interface must not introduce:

- value;
- reward;
- utility;
- performance;
- task success;
- external outcome;
- successor realization;
- scientific score;
- post-hoc analysis.

No causal `ΔT_acc → ΔV` analysis is permitted.

## 9. Required compatibility checks

Before any scientific execution, the implementation-specific compatibility preflight must demonstrate:

1. exact fixture identity and SHA-256;
2. exact schema and generator binding;
3. exact visible-field projection;
4. absence of hidden provenance from the model payload;
5. exact A/B action set;
6. exact model-facing instruction;
7. exact atomic-output validation;
8. no retry, repair, recoding, or interpretation;
9. no mutation of the canonical fixture;
10. scientific execution remains `NOT_PERFORMED`.

## 10. Authorization boundary

Passing this interface specification and its compatibility preflight does not itself authorize scientific execution.

Scientific execution requires a separate final preauthorization gate and explicit authorization.

**Disposition: NOT AUTHORIZED**
