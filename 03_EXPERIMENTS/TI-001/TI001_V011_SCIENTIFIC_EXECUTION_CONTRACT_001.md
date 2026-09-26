# TI-001 V011 Scientific Execution Contract 001

**Status:** CONTRACT — NOT AUTHORIZED

## 1. Purpose

This contract defines the execution boundary for the frozen TI-001 V011 experiment. It does not authorize scientific execution.

## 2. Canonical bindings

- Fixture ID: `TI001-V011-FIXTURE-001`
- Fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`
- Generator Git blob SHA: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema Git blob SHA: `b2fef667f6eb33689ece5481957d3917a860dd3e`
- Decision-interface implementation Git blob SHA: `8667b0ff70f58283c688f24c76f10db142655d14`
- Decision-interface implementation SHA-256: `7fd513eaff8b0acdcfee5412aa2589767e2cd186b24297a1e32b632508b9b29b`
- Seed: `20260926`

## 3. Execution population

The execution input must be exactly the canonical V011 fixture:
- 420 decision units;
- 210 unique pairs;
- 70 pairs per condition;
- 140 decision units per condition;
- 210 I1_FIRST and 210 I2_FIRST decision units.

No unit may be added, removed, reordered for scientific analysis, modified, or regenerated after authorization.

## 4. Model-facing boundary

For each decision unit, the model-facing payload shall contain only:
- `context`;
- `available_actions`;
- `future_structure`;
- the frozen decision instruction.

The following fields remain hidden:
- `decision_id`;
- `pair_id`;
- `condition`;
- `presentation`.

The response validator accepts exactly `A` or `B` after the frozen surrounding-whitespace normalization rule.

No extraction, repair, retry, recoding, inference, or imputation is permitted.

## 5. Scientific execution boundary

The execution must not introduce value, reward, utility, performance, task-success, successor-realization, or external-outcome variables.

The execution itself must not calculate or condition subsequent model inputs on scientific scores or observed responses.

## 6. Independent executions

Executor-1 and Executor-2 are separate executions.

Their outputs must remain separately identifiable. No pooling, averaging, majority vote, recoding, retry, or imputation is permitted.

## 7. Runtime traceability

Each execution record must preserve sufficient metadata to bind the execution to the frozen fixture, interface, runtime, executor identity, and execution status.

A scientific execution is invalid for evidentiary purposes if its input cannot be bound to the canonical fixture and interface.

## 8. Authorization boundary

Passing this contract's structural checks does not authorize scientific execution.

Scientific execution requires a separate final preauthorization gate and explicit authorization.

Until that authorization is recorded:
- scientific execution status = `NOT_PERFORMED`;
- authorization status = `NOT_AUTHORIZED`.

## 9. Interpretation boundary

Execution results are decision-level observations within the frozen configuration. They do not by themselves establish causal effects, value effects, general capability, or a pooled effect across independent executions.

## 10. Required next gate

The next gate is the **TI-001 V011 Final Preauthorization Gate**, which must verify this contract together with the canonical fixture and decision-interface compatibility result before any scientific execution.
