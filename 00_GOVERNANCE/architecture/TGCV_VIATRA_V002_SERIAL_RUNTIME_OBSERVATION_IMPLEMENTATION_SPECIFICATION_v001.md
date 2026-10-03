# TGCV VIATRA V002 Serial Runtime Observation Implementation Specification v001

## Status
SPECIFICATION — implementation not yet authorized.

## Purpose
Define the minimum implementation contract for a serial runtime observer bound to the canonical TGCV VIATRA V002 fixture and its concrete HostMapping transformation.

This specification is an implementation boundary. It does not constitute runtime-equivalence evidence, scientific execution, or authorization to execute the transformation.

## Canonical inputs
The implementation SHALL bind to the canonical V002 fixture artifacts already reconciled and byte-verified in the repository:
- CPS
- Deployment INITIAL
- Deployment EXPECTED
- Traceability INITIAL
- Traceability EXPECTED

The implementation SHALL NOT substitute an earlier fixture revision or infer fixture bytes from Git blob identifiers.

## Observation unit
One concrete HostMapping activation constitutes one observation unit.
The observer SHALL capture a serial lifecycle:
1. TRANSFORMATION_BEGIN
2. transformation activation
3. TRANSFORMATION_END
No parallel activation, batching, pooling, or aggregation is permitted in the minimal implementation.

## Required identity
Each observation SHALL expose:
- transformation_id
- activation_instance_id
- event_seq
- source/run provenance
- instrumentation version
The transformation identity SHALL identify the concrete HostMapping rule/activation without encoding scientific outcome, value, utility, reward, accessibility, or performance.

## Required state evidence
The observer SHALL capture canonical digests for:
- pre_state_digest
- post_state_digest
The pre-state SHALL correspond to the canonical V002 INITIAL state and the post-state SHALL correspond to the canonical V002 EXPECTED state for the concrete activation.
The implementation SHALL retain sufficient deterministic state serialization to independently reproduce each digest.

## Semantic transition
The minimal expected semantic transition is:
- create one DeploymentHost;
- assign ip = 152.66.102.6;
- create one CPS2DeploymentTrace;
- establish one CPS source-element reference;
- establish one Deployment target-element reference.
The observer SHALL observe this transition without modifying the transformation semantics.

## Event ordering
event_seq SHALL provide a deterministic total order for the serial observation.
The minimal valid sequence is:
- BEGIN before activation evidence;
- activation evidence before END;
- END after post-state evidence.

## Provenance
The implementation SHALL record enough provenance to identify:
- fixture revision;
- fixture SHA-256 manifest revision;
- implementation revision;
- instrumentation revision;
- runtime/toolchain identity where available.
Git blob SHA values SHALL NOT replace SHA-256 digests of canonical fixture bytes.

## Scientific firewall
The implementation SHALL NOT introduce or compute:
- U_t;
- T_acc;
- accessibility labels;
- future assignment;
- utility;
- reward;
- value;
- scientific performance metrics.
The observer is purely operational and provenance-oriented.

## Determinism requirements
Repeated execution of the same isolated activation over identical canonical inputs SHALL produce byte-identical canonical observation records, apart from explicitly declared run metadata that is excluded from the canonical state digest.

## Acceptance conditions
Implementation is ready for its implementation preflight only when:
1. all required fields are emitted;
2. the concrete HostMapping activation is uniquely identifiable;
3. PRE and POST states are canonically serializable;
4. the expected V002 semantic delta is observable;
5. event ordering is deterministic;
6. provenance is complete;
7. the scientific firewall passes;
8. no mutation of canonical fixture artifacts occurs.

## Boundary
This specification does not:
- claim runtime equivalence;
- establish scientific validity;
- authorize scientific execution;
- authorize a production run;
- replace the already completed V002 provenance reconciliation;
- require a build merely to persist or review this specification.

The next gate after this specification is a dedicated implementation/preflight review of the concrete observer implementation.