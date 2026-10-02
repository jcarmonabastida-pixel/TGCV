# TGCV VIATRA Instrumentation Contract Preflight Audit

**Status:** UNDERDETERMINED — implementation not authorized  
**Date:** 2026-10-02  
**Contract:** `TGCV_VIATRA_INSTRUMENTATION_CONTRACT_IMMUTABLE_EVENT_SCHEMA_001.md`  
**Candidate revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`

## Audit scope

This preflight checks whether the immutable event contract is sufficiently specified to implement an independent runtime observation layer.

## Findings

| Gate | Result | Finding |
|---|---|---|
| Event identity | PASS | run/event identifiers and observer-assigned sequence are explicitly defined. |
| Primary temporal ordering | PASS | `event_seq` is explicitly external to transformation-space construction. |
| Source revision binding | PASS | candidate source revision is frozen. |
| Transformation/activation identity | UNDERDETERMINED | VIATRA exposes activation objects and activation coding, but the canonical observer identity and its stability across runs have not yet been specified. |
| Pre-state capture | UNDERDETERMINED | The contract requires a state digest immediately before execution, but the exact VIATRA callback boundary and canonical state serialization are not yet frozen. |
| Post-state capture | UNDERDETERMINED | The existing debugger exposes post-firing notification, but exact state-capture ordering relative to all relevant runtime mutations requires implementation-level verification. |
| Completeness | PASS AT SPECIFICATION LEVEL | Explicit terminal manifest and missingness states are defined. |
| Provenance | PASS AT SPECIFICATION LEVEL | Required immutable provenance fields are defined. |
| Information separation | PASS | The contract excludes `U_t`, accessibility, outcomes, value and reward from the primary event. |
| R* reconstruction | PASS AT SPECIFICATION LEVEL | R* is defined solely from observer sequence. |
| Concurrency | UNDERDETERMINED | The contract currently assumes a serial observer sequence; concurrent execution requires an explicit causal/concurrency policy. |
| Scientific firewall | PASS | No outcome/value channel is required for the primary observation. |

## Critical blockers before implementation

### B1 — Canonical activation identity

The observer must define whether activation identity is:
- a stable semantic identity of the transformation rule plus bound parameters; or
- an execution-instance identity assigned by the observer.

These must not be conflated. The execution-instance identity should be observer-assigned and unique within a run.

### B2 — Exact state boundary

The implementation must identify the precise callback/interception point at which:
- pre-state is captured before any transformation mutation;
- post-state is captured after the transformation mutation relevant to the event is complete.

This cannot be inferred from method names alone.

### B3 — Canonical state serialization

A deterministic state serialization/hash procedure is still missing. Object identity, iteration order, transient runtime objects and non-semantic metadata must not make equivalent observed states hash differently.

### B4 — Serial execution restriction

Until concurrency semantics are specified and tested, the experimental runtime must be constrained to a single transformation execution thread / serial event stream.

## Decision

**UNDERDETERMINED.**

The contract itself is structurally sound, but four implementation-critical details remain unresolved. No instrumentation implementation and no scientific execution are authorized.

## Next gate

Create a **VIATRA Serial Runtime Observation Prototype Specification** that resolves B1–B4 at the design level, including exact callback boundaries, activation identity, canonical state serialization, and an explicit single-thread execution constraint.
