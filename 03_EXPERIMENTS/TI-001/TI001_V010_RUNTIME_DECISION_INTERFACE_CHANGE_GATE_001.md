# TI-001 V010 Runtime / Decision-Interface Change Gate 001

**Status:** CHANGE REQUIRED — NOT AUTHORIZED

## Trigger

TI-001 V009 completed the authorized scientific execution boundary, but produced no valid atomic A/B decisions.

Observed V009 result:
- 420 decision units processed.
- 245 responses completed.
- 175 responses incomplete with reason `max_output_tokens`.
- 420/420 had `reasoning_tokens=0`.
- 0/420 outputs were protocol-valid atomic `A` or `B`.

The V009 primary execution audit is closed as **SCIENTIFIC DECISIONS NOT VALID**.

## Diagnosis

The V009 runtime correction successfully eliminated reasoning-token consumption. The remaining failure is at the model-facing decision interface.

The scientific runner transmitted the visible decision payload, but the operational protocol did not sufficiently constrain the model to return exactly one atomic decision `A` or `B`.

Completed responses therefore included transformed/reproduced JSON, multi-action structures, natural-language descriptions, and requests for further instructions.

The 175 incomplete responses remain invalid because they were truncated by the output-token limit.

## Required V010 change

V010 shall introduce and validate an explicit model-facing decision instruction that:

1. Defines the task as selecting exactly one action, `A` or `B`.
2. Makes clear that the response must contain only the single token `A` or `B`.
3. Defines the mapping between the supplied decision context and the required atomic response without exposing hidden provenance.
4. Does not expose `decision_id`, `pair_id`, `condition`, or `presentation`.
5. Does not introduce reward, utility, value, performance, task success, or external outcomes.
6. Does not alter the frozen fixture or its visible fields.
7. Does not realize the successor or provide information beyond the defined `future_structure`.
8. Does not permit retry, recoding, or post-hoc conversion of model outputs into A/B.
9. Preserves the existing V009 runtime configuration unless an independent compatibility finding requires another change.
10. Separately validates that the interface produces protocol-valid atomic A/B outputs before scientific execution.

## Scientific invariants

The following remain unchanged and frozen:

- Scientific object: Transformational Intelligence.
- Experimental question: whether the agent incorporates available future transformation structure into its present decision.
- Frozen V008 fixture: 420 decision units / 210 pairs.
- Conditions: 70 control / 70 treatment / 70 null.
- Pair orientation: 105 I1_FIRST / 105 I2_FIRST.
- Agent-visible fields: context, available_actions, future_structure.
- Hidden fields remain hidden.
- Valid output domain: exactly `A` or `B`.
- No value/reward/utility/performance/task-success variable.
- No causal `ΔT_acc → ΔV` analysis.
- No recoding of invalid outputs.
- No scientific execution during design or compatibility preflights.

## Required V010 artifacts

Before any scientific execution:

1. V010 decision-interface specification.
2. V010 model-facing prompt/interface implementation.
3. V010 interface compatibility preflight.
4. V010 runtime compatibility preflight, reusing V009 runtime only if unchanged.
5. V010 scientific execution contract.
6. V010 runner identity preflight.
7. V010 final pre-authorization gate.
8. Explicit user authorization.

## Authorization boundary

This change gate does **not** authorize scientific execution.

No V010 scientific run may occur until all required preconditions pass and explicit authorization is recorded.

## Disposition

**CHANGE REQUIRED — NOT AUTHORIZED**

The next action is to formalize the V010 decision-interface specification and its exact output contract.
