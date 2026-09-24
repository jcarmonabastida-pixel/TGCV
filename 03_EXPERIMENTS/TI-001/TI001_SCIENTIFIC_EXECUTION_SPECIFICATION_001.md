# TI-001 Scientific Execution Specification 001

**Status:** FROZEN EXECUTION SPECIFICATION — SCIENTIFIC EXECUTION NOT AUTHORIZED

## 1. Scope

This specification defines the execution procedure for the first TI-001 scientific test after explicit authorization. It does not itself authorize execution.

## 2. Frozen inputs

- Canonical fixture: `03_EXPERIMENTS/TI-001/TI001_PREFLIGHT_FIXTURE_v004.json`
- Fixture SHA-256: `20ad94fcaca2e85228f1a266ae69d9d391a35182a64ab122fd5feed56b46a4dd`
- Randomisation seed: `582031`
- Environment seed base: `731407`
- Matched pairs: 32
- Records: 64
- Primary estimand: `matched_condition_difference_in_transformation_handling`
- Estimand type: `difference_in_subsequent_transformation_handling`

## 3. Execution conditions

Each matched pair is executed under its preassigned control/treatment slot. The assignment must be read from the frozen fixture and must not be regenerated or altered during execution.

For every record:

1. Present the current state and the currently executable transformations.
2. Present the condition-specific information.
3. Require the transformation choice before successor-state information is revealed.
4. Record the selected transformation.
5. Apply the frozen deterministic transition.
6. Reveal/record the successor state and successor accessible transformations.
7. Persist the resulting execution record without modifying the frozen input fields.

## 4. Control condition

Control receives only ordinary current transformation/task information specified by the fixture. It does not receive the structured future transformation-space signal.

## 5. Treatment condition

Treatment receives the same current transformation/task information plus the structured future transformation-space information specified by the fixture.

The treatment information must not contain:

- a recommended action;
- reward, utility, payoff, value, or outcome information;
- the identity of a preferred transformation;
- successor-state observations available before the decision.

## 6. Null condition

The null information structure remains non-scientific in this first test package and contains no future-space signal, recommendation, or outcome information.

## 7. Primary observation

The primary observation is subsequent transformation handling. The execution record must retain the selected transformation and the matched pair/condition identifiers required for the frozen estimand.

No composite intelligence score is to be constructed.

## 8. Prohibited changes during execution

The following are frozen and cannot be changed after authorization:

- fixture contents;
- fixture hash;
- assignment;
- seeds;
- information conditions;
- temporal order;
- primary estimand;
- exclusion rules.

Any such change is a deviation and invalidates the affected execution until formally resolved.

## 9. Required execution evidence

For each scientific run persist:

- exact canonical commit;
- fixture SHA-256;
- executor identifier and version;
- runtime/environment metadata;
- pair and slot identifiers;
- condition;
- selected transformation;
- successor state;
- successor accessibility;
- execution timestamp;
- deviations, if any.

## 10. Scientific interpretation boundary

Execution produces observations only. Any inference concerning Transformational Intelligence must be performed after execution against the frozen estimand and evidence package. Execution itself must not encode an interpretation or desired outcome.

## 11. Authorization boundary

This specification is frozen as the execution procedure, but:

**SCIENTIFIC EXECUTION = NOT_AUTHORIZED**

A separate authorization record is required before the first scientific run.
