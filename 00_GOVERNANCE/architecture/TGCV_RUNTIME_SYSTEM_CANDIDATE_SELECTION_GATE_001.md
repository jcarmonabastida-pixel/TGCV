# TGCV — Runtime System Candidate Selection Gate 001

**Status:** OPEN — SYSTEM SELECTION / NO EXECUTION AUTHORIZED
**Date:** 2026-10-02
**Parent:** TGCV_RUNTIME_TRACE_INSTRUMENTATION_PROVENANCE_PREFLIGHT_001.md

## 1. Purpose

Define the admission criteria for selecting a concrete runtime system that could later provide an independent longitudinal observation source for R*_t.

Selection of a system is not evidence for the architectural hypothesis and does not authorize instrumentation or scientific execution.

## 2. Mandatory criteria

A candidate system must satisfy all criteria:

### S1 — Real transformation activity

The system must execute actual state-changing or state-organising transformations rather than only declare possible transformations.

### S2 — Observable state boundary

Pre-transformation and post-transformation states must have reproducible identities or canonical representations.

### S3 — Transformation identity

Individual transformation events must have a reproducible identity that is independent of any downstream target.

### S4 — Temporal ordering

Events must have reliable event-time semantics or a monotonic execution ordering.

### S5 — Instrumentability

The system must permit deterministic instrumentation of the transformation events without changing the semantic identity of those transformations.

### S6 — Immutable source revision

The candidate must be pinned to an immutable source/runtime revision before instrumentation.

### S7 — Reproducible execution

The execution environment and configuration must be sufficiently controllable to reproduce the trace-generation procedure.

### S8 — Provenance

Source, revision, build/configuration and execution provenance must be capturable.

### S9 — Information separation

The runtime trace must permit explicit separation between information legitimately available to A and any information claimed as additional observation for B/R*.

### S10 — Scientific firewall

The system must permit trace generation without requiring outcome, value, reward or utility as inputs to event identity or R* construction.

## 3. Preferred candidate characteristics

Preference may be given to systems with:

- explicit state-transition APIs;
- deterministic or controlled execution modes;
- open source and immutable revision history;
- existing test suites;
- structured event/logging interfaces;
- reproducible builds;
- simple enough state semantics to permit independent auditing.

These are selection aids, not evidence or rankings.

## 4. Exclusion criteria

Reject or defer a candidate if:

- transformation identity depends on the downstream hypothesis;
- state transitions cannot be observed reliably;
- event order cannot be established;
- instrumentation materially changes transformation semantics;
- the source revision cannot be frozen;
- provenance cannot be reproduced;
- missing trace records cannot be distinguished from genuine absence;
- R* would be reconstructed from static metadata rather than observed runtime events.

## 5. Required system card

Before admission, the repository must contain a system card specifying:

1. system name and purpose;
2. source repository;
3. immutable revision;
4. licence/provenance;
5. state model;
6. transformation model;
7. event model;
8. instrumentation boundary;
9. build/execution procedure;
10. expected trace schema;
11. integrity procedure;
12. A information boundary.

No field may be populated by assumption. Unknown fields remain UNKNOWN.

## 6. Decision states

**ADMITTED:** all mandatory criteria satisfied and system card frozen.

**DEFERRED:** plausible candidate but one or more mandatory criteria cannot yet be demonstrated.

**REJECTED:** candidate violates an exclusion criterion.

## 7. Current status

No concrete runtime system is currently admitted by this gate.

**SYSTEM SELECTION: OPEN.**

## 8. Next governed action

Identify a concrete candidate system and populate the system card using repository/source evidence. Do not instrument, execute, or generate traces until the system card is admitted.

## 9. Scientific firewall

This gate authorizes no scientific execution, no trace generation, no predictive test, and no inference concerning TSDI, accessibility, outcome or value.