# TGCV — Source Candidate S3: Controlled Runtime Traces — Source Card 001

**Status:** CANDIDATE / NOT YET ADMITTED / NO SCIENTIFIC EXECUTION AUTHORIZED
**Date:** 2026-10-02
**Parent:** TGCV_SOURCE_MEASUREMENT_BOUNDARY_IDENTIFICATION_001.md

## 1. Candidate identity

**Source class:** S3 — Controlled experimental runtime/event traces.

**Candidate:** a purpose-built transformation-capable software system instrumented to emit immutable, timestamped runtime transformation events under a frozen observation protocol.

This is a source class candidate, not a claim that such a dataset already exists in the TGCV repository.

## 2. Why this candidate is considered

Unlike the frozen Rust ecosystem snapshot, runtime traces can potentially observe actual transformation events and their temporal ordering rather than only declaring possible dependency relations.

The candidate is therefore capable in principle of supplying an observation boundary distinct from static U_t construction.

## 3. Required transformation identity

Each runtime transformation event must carry a stable event-level transformation identity and a reproducible mapping to the system state before and after the event.

The identity protocol must be frozen before collecting or analysing the downstream observable.

An event identifier generated only for logging convenience is insufficient unless its mapping to the transformation semantics is independently specified.

## 4. Required event schema

At minimum, each event should contain:

- event identifier;
- transformation identity;
- pre-event state identifier or canonical state representation;
- post-event state identifier or canonical state representation;
- event timestamp or monotonic sequence position;
- execution context identifier;
- provenance/version of the instrumented runtime;
- event status;
- explicit missing/unknown semantics.

No outcome, reward, value or future-state field may be required to construct the candidate R_t.

## 5. Candidate R_t observation

R_t would be derived from timestamped runtime events according to a pre-registered relation rule, for example a typed temporal relation between transformation events satisfying a specified temporal and causal-observation criterion.

The exact relation rule is **not yet frozen**.

Therefore this source card does not yet establish an admissible R_t.

## 6. Independence boundary

The critical test is whether the runtime event record contains empirical information that is not deterministically recoverable from the inherited A representation.

The mere fact that events are recorded at runtime does not establish independence.

A-reconstruction must receive the strongest legitimate information available under the inherited architecture. Any residual R_t information must come from the independently observed runtime event stream, not from withholding A inputs.

## 7. Temporal boundary

At time t, R_t may use only runtime events whose observation timestamp/sequence position is at or before t.

Later events may be used for separate audit of the frozen trace but may not define historical R_t.

## 8. Completeness and missingness

The trace protocol must distinguish:

- observed event;
- observed absence only where completeness is certified;
- unknown/missing trace;
- out-of-scope execution.

No complete-absence inference is permitted without an explicit completeness certificate.

## 9. Provenance and reproducibility

Before admission, the candidate requires:

1. instrumented system identity;
2. immutable source/runtime version;
3. trace schema version;
4. deterministic or reproducible instrumentation configuration;
5. frozen trace-generation protocol;
6. byte-level or equivalent artifact integrity identifier;
7. documented execution environment.

These items are not yet available in this source card and must not be invented.

## 10. A-reconstruction gate

The candidate may proceed only if a separate preflight can demonstrate one of:

- **A-EQUIVALENT:** runtime R_t is fully determined by A;
- **A-NON-EQUIVALENT:** an independently observed runtime component remains unexplained by A;
- **UNDERDETERMINED:** the trace or information boundary is insufficient.

No predictive experiment is permitted before this classification.

## 11. Current disposition

**SOURCE STATUS: CANDIDATE — NOT ADMITTED.**

The controlled-runtime-trace class is the first source class selected for detailed review because it can, in principle, provide actual longitudinal observations rather than another static transformation of U_t.

However, no specific runtime dataset is asserted to exist, and no scientific execution is authorized.

## 12. Next gate

**Runtime Trace Instrumentation & Provenance Preflight.**

The next package must specify the concrete system, event instrumentation, trace schema, frozen runtime version, observation protocol and artifact-integrity procedure before any trace is generated or analysed.