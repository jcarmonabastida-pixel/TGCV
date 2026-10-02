# TGCV VIATRA Instrumentation Contract & Immutable Event Schema

**Status:** DRAFT FOR PREFLIGHT — no scientific execution authorized  
**Date:** 2026-10-02  
**Candidate:** Eclipse VIATRA  
**Source revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`

## 1. Contract purpose

Define the minimum immutable event contract required to observe executed transformations independently of the transformation-space representation.

The contract is an observation specification, not a scientific result and not an admission of VIATRA as an experimental system.

## 2. Event identity

Every emitted event receives:

- `run_id`: immutable identifier of one controlled execution;
- `event_seq`: strictly increasing observer-assigned integer starting at 1;
- `event_id`: deterministic identifier derived from `run_id + event_seq`;
- `event_type`: one of `TRANSFORMATION_BEGIN`, `TRANSFORMATION_END`;
- `transformation_id`: observer-level identity of the executed transformation;
- `activation_id`: identity of the concrete activation, when available.

The observer, not the transformation-space constructor, assigns `event_seq`.

## 3. Temporal contract

`event_seq` is the primary execution-order field.

For events (e_i,e_j):

[
R^*_r(e_i,e_j) iff event_seq(e_i) < event_seq(e_j)
]

A monotonic clock value may be recorded as secondary metadata. Wall-clock time is not the ordering authority.

If concurrent execution is introduced later, the contract must be extended with an explicit concurrency/causal-order specification before such executions are admitted.

## 4. State observation contract

Transformation events must provide explicit observation boundaries:

- `pre_state_digest`: digest of canonicalized relevant state immediately before the transformation;
- `post_state_digest`: digest of canonicalized relevant state immediately after the transformation;
- `state_schema_id`: frozen identifier of the canonical state representation;
- `state_scope`: explicit declaration of which state is observed.

The contract must never encode a value, utility, reward, downstream outcome, or future trajectory as part of the primary observation.

## 5. Provenance contract

Each event is bound to:

- source repository;
- source revision;
- instrumentation revision;
- runtime/build manifest digest;
- execution environment digest;
- run configuration digest;
- parent artifact/provenance identifier.

All referenced provenance artifacts must be immutable or content-addressed.

## 6. Completeness and missingness

A run must terminate with a separate immutable run manifest containing:

- expected event count;
- observed event count;
- first and last sequence numbers;
- missing sequence numbers, if any;
- terminal status;
- artifact digest.

Absence of an event must not silently be interpreted as evidence that no transformation occurred.

Allowed states:

- `OBSERVED`
- `MISSING_UNCERTAIN`
- `RUN_INCOMPLETE`
- `OUT_OF_SCOPE`

A scientific run is eligible for analysis only when completeness criteria are explicitly satisfied.

## 7. Canonical event record

Conceptual canonical record:

```json
{
  "schema_version": "TGCV_VIATRA_EVENT_v001",
  "run_id": "...",
  "event_seq": 1,
  "event_id": "...",
  "event_type": "TRANSFORMATION_BEGIN",
  "transformation_id": "...",
  "activation_id": "...",
  "pre_state_digest": "...",
  "post_state_digest": null,
  "state_schema_id": "...",
  "state_scope": "...",
  "observer_monotonic_time": "...",
  "source_revision": "ffa111dbb160c0bc55e89ea16430e97a38908662",
  "instrumentation_revision": "...",
  "runtime_manifest_digest": "...",
  "run_config_digest": "...",
  "provenance_id": "..."
}
```

The concrete serialization, field encoding and hash algorithms remain subject to preflight.

## 8. Information-separation rule

The event schema must not import:

- `U_t`;
- `T_acc`;
- accessibility labels;
- future assignments;
- outcomes;
- utility/reward;
- value;
- downstream performance metrics.

Those variables, if used in later analyses, must enter through separate declared channels.

## 9. Required invariants

Before implementation is admitted:

1. sequence numbers are unique and contiguous for a complete run;
2. event identity is deterministic from immutable identifiers;
3. source revision is frozen;
4. instrumentation revision is frozen;
5. state serialization is deterministic;
6. pre/post capture boundaries are explicit;
7. provenance is complete;
8. incomplete traces cannot silently pass as complete;
9. R* can be reconstructed solely from observer sequence data;
10. no outcome/value signal enters the primary trace.

## 10. Preflight decision criteria

Possible states:

- **PASS** — contract is sufficiently specified for implementation;
- **UNDERDETERMINED** — one or more fields require empirical/runtime clarification;
- **FAIL** — contract would contaminate the independent observation boundary.

No implementation or scientific execution is authorized until this contract receives a PASS preflight.
