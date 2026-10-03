# TGCV VIATRA V002 Minimal Fixture Instrumentation Contract Preflight 001

**Status:** DESIGN REVIEW PASS — implementation not authorized  
**Date:** 2026-10-03  
**Fixture:** `TGCV_VIATRA_MINIMAL_FIXTURE_v002`  
**Fixture freeze:** `eda3786ab1e4c6a44846f1fd5eb47898b1c2cff5`  
**Source binding:** `b39cf9402b532dd80fe962123377720f0251ed59`

## 1. Scope

This preflight checks whether the frozen V002 fixture, the pinned VIATRA source binding, and the serial observation specification jointly define an implementation-admissible instrumentation contract.

No Java code, Maven/Tycho build, VIATRA runtime, or scientific execution is performed or authorized by this document.

## 2. Boundary evidence

The historical VIATRA EVM API exposes `IEVMListener.beforeFiring(Activation)` and `afterFiring(Activation)`. These callbacks are the candidate observation boundaries.

For V002:

- BEGIN observation occurs immediately before invoking the effective `hostRule` mutation.
- END observation occurs immediately after the effective mutation returns.
- The observer owns `event_seq` and `activation_instance_id`.
- The transformation semantic identity is the frozen tuple:
  `(implementation_id, transformation_id, rule_id, fixture_contract_revision)`.

## 3. Frozen state scope

The state observation is restricted to the declared V002 semantic projection required to distinguish the frozen initial and expected fixtures:

- CPS HostInstance source identity/reference;
- Deployment hosts and the host IP relevant to `hostRule`;
- Traceability root references and the CPS-to-Deployment trace links relevant to the expected delta.

Runtime object identity, memory addresses, timestamps, activation object identity, and scientific outcome/value/reward fields are excluded.

The exact canonical serialization implementation remains an implementation concern and must be tested for determinism; it is not inferred from Java object traversal.

## 4. P1–P8 admission matrix

| Test | Design status | Admission condition |
|---|---|---|
| P1 identity stability | PASS at design level | derive `transformation_id` only from frozen semantic metadata |
| P2 execution uniqueness | PASS at design level | assign one observer-owned `activation_instance_id` per selected activation |
| P3 state determinism | IMPLEMENTATION TEST REQUIRED | identical semantic state must produce identical canonical bytes/digest |
| P4 boundary integrity | IMPLEMENTATION TEST REQUIRED | verify no relevant mutation occurs outside BEGIN/END boundaries |
| P5 sequence integrity | PASS at design level | single observer counter, contiguous sequence |
| P6 seriality | PASS at design level | single execution thread; reject overlap |
| P7 provenance integrity | PASS at design level | bind frozen fixture, source, instrumentation and run manifests by digest |
| P8 firewall | PASS at design level | primary trace contains no value/outcome/reward channel |

## 5. Non-admitted claims

This preflight does not claim:

- that the callbacks have already been executed successfully against V002;
- that the proposed serializer is already implemented or deterministic;
- that the runtime mutation scope has been empirically verified;
- that the observer can already reconstruct a complete runtime trace;
- that any TGCV scientific quantity has been measured.

## 6. Decision

**DESIGN REVIEW PASS — IMPLEMENTATION PRECONDITIONS DEFINED.**

The frozen fixture and pinned source binding are sufficient to define the implementation boundary without altering the transformation semantics. P3 and P4 remain empirical implementation-validation tests.

## 7. Next gate

Perform a separately gated **Prototype Implementation Construction** followed by its own static/build preflight. Runtime execution remains unauthorized until P1–P8 are empirically validated.
