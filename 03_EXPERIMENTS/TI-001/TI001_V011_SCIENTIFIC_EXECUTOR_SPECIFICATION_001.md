# TI-001 V011 Scientific Executor Specification 001

**Status:** SPECIFICATION — AUTHORIZED, EXECUTION NOT STARTED

## 1. Purpose

Define the canonical Executor-1 execution harness for TI-001 V011 after explicit scientific authorization.

The executor must consume the frozen V011 fixture, construct only the V011 decision-interface payload, obtain one decision per decision unit from the authorized decision provider, validate the atomic A/B response, and persist traceable execution evidence.

## 2. Frozen bindings

- Fixture ID: `TI001-V011-FIXTURE-001`
- Fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`
- Generator Git blob SHA: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema Git blob SHA: `b2fef667f6eb33689ece5481957d3917a860dd3e`
- Decision-interface Git blob SHA: `8667b0ff70f58283c688f24c76f10db142655d14`
- Seed: `20260926`
- Population: 420 decision units / 210 pairs.

## 3. Execution boundary

For each decision unit, the provider receives exactly:

- `instruction`
- `decision.context`
- `decision.available_actions`
- `decision.future_structure`

The executor/provider must not transmit:

- decision_id
- pair_id
- condition
- presentation
- fixture metadata
- seed
- expected condition
- expected answer
- scientific estimands
- value, reward, utility, performance, task-success or successor information.

## 4. Decision protocol

Exactly one provider call is made per decision unit.

The response is accepted only after the V011 interface validator normalizes surrounding whitespace and obtains exactly `A` or `B`.

No extraction, repair, inference, retry, recoding, imputation, or replacement is permitted.

An invalid response is recorded as invalid evidence; it is not repaired or retried.

## 5. Assignment and ordering

The executor consumes the canonical fixture in its serialized order. It must not reorder, rebalance, filter, duplicate, or regenerate decision units.

All 420 decision units must be attempted exactly once in Executor-1.

## 6. Traceability

For every attempted decision the evidence package must persist, at minimum:

- decision_id
- pair_id
- condition
- presentation
- provider request/response identifiers when exposed
- response status
- raw output representation sufficient for audit
- validated decision, or explicit invalid status
- request and response timestamps when available
- executor/provider version
- fixture SHA-256
- interface Git blob SHA
- runtime metadata.

Hidden provenance fields are persisted only in the evidence package and are never sent to the decision mechanism.

## 7. Runtime controls

The executor must bind the exact frozen interface implementation and fixture before the first scientific call.

Before execution it must verify:

1. fixture SHA-256;
2. interface Git blob SHA;
3. generator Git blob SHA;
4. schema Git blob SHA;
5. authorization record status;
6. execution-contract bindings;
7. decision-unit count equals 420.

Failure of any binding check blocks scientific calls.

## 8. Separation of concerns

The executor does not compute TI-001 estimands and does not interpret decisions.

It only acquires and persists decision evidence.

Scientific analysis is a later, separate stage.

## 9. Execution status

This specification does not itself perform scientific execution.

**Scientific execution remains NOT_STARTED until the Executor-1 implementation passes its dedicated identity/compatibility preflight.**
