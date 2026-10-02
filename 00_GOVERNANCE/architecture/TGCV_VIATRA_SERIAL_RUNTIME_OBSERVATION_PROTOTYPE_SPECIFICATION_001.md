# TGCV VIATRA Serial Runtime Observation Prototype Specification

**Status:** DESIGN COMPLETE — implementation still not authorized  
**Date:** 2026-10-02  
**Candidate revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`

## 1. Prototype objective

Resolve the four blockers identified by the instrumentation-contract preflight:

- B1 activation identity;
- B2 exact pre/post state boundaries;
- B3 canonical state serialization;
- B4 concurrency.

The prototype is an instrumentation feasibility artifact. It is not a scientific execution.

## 2. Execution constraint

The prototype MUST execute transformations serially:

- one transformation execution thread;
- one observer sequence counter;
- no parallel transformation firing;
- no asynchronous state mutation admitted to the observed state.

Any violation invalidates the prototype trace.

## 3. Activation identity

Two identities are retained separately:

### Transformation identity

`transformation_id` identifies the semantic transformation rule/specification plus its frozen binding schema.

It is derived only from declared transformation metadata and does not include outcomes.

### Execution identity

`activation_instance_id` is assigned by the observer when the activation is first selected for execution.

It is unique within `run_id` and is never reused.

This avoids treating runtime object identity as a reproducible scientific identity.

## 4. Event boundaries

For each selected activation:

### BEGIN boundary

Immediately before invoking the transformation's effective mutation operation:

1. observer increments `event_seq`;
2. observer records activation/transformation identity;
3. observer canonicalizes the declared observed state;
4. observer computes `pre_state_digest`;
5. observer emits `TRANSFORMATION_BEGIN`.

### END boundary

Immediately after the effective mutation operation returns and before any subsequent transformation activation is selected:

1. observer canonicalizes the same declared observed state;
2. observer computes `post_state_digest`;
3. observer emits `TRANSFORMATION_END`.

The prototype must verify empirically that no relevant state mutation occurs outside these boundaries.

## 5. Temporal relation

The observer-generated sequence defines:

[
R^*(e_i,e_j) iff event_seq(e_i) < event_seq(e_j)
]

For a transformation instance, its BEGIN and END events must be adjacent in the serial event stream unless an explicit nested-event mechanism is later admitted.

## 6. Canonical state serialization

The observed state must be declared as a finite semantic projection, not the complete Java runtime heap.

Serialization requirements:

- stable field ordering;
- stable collection ordering;
- exclusion of runtime object identity;
- exclusion of memory addresses;
- exclusion of nondeterministic metadata;
- explicit treatment of null/absent values;
- UTF-8 canonical encoding;
- explicit numeric representation;
- versioned serialization schema.

The digest is computed over the canonical byte representation.

The prototype must include a determinism test: serializing the same semantic state twice must produce byte-identical output and identical digest.

## 7. State scope

The initial prototype MUST use a deliberately small, explicitly enumerated model state.

The scope must be frozen before execution and must contain only state whose transformation is directly observable.

No value, reward, performance or downstream outcome variable may be included.

## 8. Completeness certificate

A successful prototype run must produce:

- run manifest;
- event stream;
- source revision;
- instrumentation revision;
- state schema revision;
- expected event count;
- observed event count;
- sequence continuity check;
- artifact digests.

## 9. Prototype validation tests

Before any scientific run:

**P1 — identity stability:** same declared transformation produces the same `transformation_id`.

**P2 — execution uniqueness:** each selected activation receives one unique `activation_instance_id`.

**P3 — state determinism:** repeated serialization of an unchanged state is byte-identical.

**P4 — boundary integrity:** controlled test verifies pre-state precedes mutation and post-state follows mutation.

**P5 — sequence integrity:** event sequence is contiguous and strictly increasing.

**P6 — seriality:** no overlapping transformation execution is observed.

**P7 — provenance integrity:** all artifacts resolve to frozen revisions and digests.

**P8 — firewall:** trace contains no outcome/value/reward field.

## 10. Admission criterion

The prototype may advance to implementation preflight only if P1–P8 pass.

Even then, **scientific execution remains separately unauthorized** until the experimental design and A-reconstruction protocol pass their respective gates.

## Decision

**DESIGN COMPLETE.**

The four previously unresolved design blockers have explicit operational resolutions. Empirical validation is still required; therefore this document does not authorize execution.

## Next gate

Run a **Prototype Implementation Preflight** against the actual VIATRA APIs and repository revision, checking whether the specified boundaries and serialization can be implemented without altering the transformation semantics.
