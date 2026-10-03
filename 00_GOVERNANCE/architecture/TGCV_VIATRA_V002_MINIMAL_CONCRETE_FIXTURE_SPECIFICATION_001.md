# TGCV VIATRA V002 Minimal Concrete Fixture Specification

**Status:** DESIGN DRAFT — fixture not yet frozen; implementation and scientific execution not authorized  
**Date:** 2026-10-03  
**Branch:** `viatra-v002-provenance-canonical-closure`

## 1. Purpose

Define the smallest concrete VIATRA CPS transformation fixture that can support the runtime-observation prototype and the P1–P8 instrumentation contract.

This fixture is derived from the already validated V002 runtime-equivalence preflight. It does not introduce a new transformation semantics.

## 2. Concrete transformation

The fixture exercises the VIATRA CPS `CPS2DeploymentTransformation` and exactly one relevant activation:

`UnmappedHostInstance` for:

- HostType identifier: `Rawsberry.PI`
- HostInstance identifier: `Aragorn`

The transformation creates one `DeploymentHost` and one `CPS2DeploymentTrace` mapping the CPS HostInstance to the created deployment host.

## 3. Input state

The frozen semantic input projection contains:

### CPS
- exactly one relevant HostType;
- exactly one relevant HostInstance;
- HostType identifier = `Rawsberry.PI`;
- HostInstance identifier = `Aragorn`.

### Deployment
- exactly zero DeploymentHost instances before firing.

### Traceability
- exactly one root `CPSToDeployment`;
- root CPS reference resolves to the CPS model;
- root Deployment reference resolves to the deployment model;
- exactly zero trace mappings before firing.

### Activation set
Immediately before transformation execution:
- exactly one relevant `UnmappedHostInstance` match;
- no additional relevant activation is admitted by the fixture.

## 4. Expected transformation

One transformation activation is selected and executed serially.

Expected semantic post-state:

- deployment host count = 1;
- created DeploymentHost IP = `152.66.102.6`;
- trace count = 1;
- trace CPS element identifier = `Aragorn`;
- trace deployment element IP = `152.66.102.6`;
- unmapped-host activation count after firing = 0.

EMF URI fragments are **not** part of semantic equivalence. They may be used only to resolve fixture references when loading expected XMI.

## 5. Fixture artefacts

The intended frozen fixture package consists of:

- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_CPS.xmi`
- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_INITIAL.xmi`
- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_INITIAL.xmi`
- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_EXPECTED.xmi`
- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_EXPECTED.xmi`

The fixture artefacts are provenance-controlled repository assets. Their bytes must be treated as authoritative; they must not be reconstructed implicitly.

## 6. Canonical observed state

The runtime observer shall not serialize the Java heap.

The initial minimal semantic state projection is:

`S = (H, D, M)`

where:

- `H` = ordered semantic HostType/HostInstance projection;
- `D` = ordered semantic DeploymentHost projection;
- `M` = ordered semantic trace mapping projection.

Only fields necessary to establish the transformation and its direct structural effect are admitted.

For this fixture:

### Host projection
- HostType identifier
- HostInstance identifier

### DeploymentHost projection
- IP address

### Trace projection
- CPS element semantic identifier
- deployment element semantic IP

Collection ordering must be deterministic.

## 7. Transformation identity

The observer-level `transformation_id` shall be derived from:

- transformation implementation/rule identity;
- frozen binding schema;
- fixture contract revision.

It must not contain:
- runtime Java object identity;
- memory address;
- execution result;
- outcome/value/reward;
- wall-clock timestamp.

For the fixture, the semantic transformation is the single host-mapping operation represented by `CPS2DeploymentTransformation`.

The canonical semantic encoding for `transformation_id` is the ordered tuple:

`(implementation_id, transformation_id, rule_id, fixture_contract_revision)`

For V002:

- `implementation_id` = `org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra`
- `transformation_id` = `CPS2DeploymentTransformationViatra`
- `rule_id` = `hostRule`
- `fixture_contract_revision` = `V002`

The encoding is semantic metadata only. It must not include the concrete HostInstance identifier, generated IP, activation identity, EMF URI fragment, Java object identity, timestamp, execution result, outcome, value, or reward.

## 8. Activation identity

`activation_instance_id` is assigned by the observer at first selection for execution.

Requirements:

- unique within `run_id`;
- assigned exactly once;
- never reused;
- independent of EMF URI fragments;
- independent of Java object identity;
- excluded from canonical semantic state serialization.

## 9. Expected event stream

For one serial activation the minimum expected event sequence is:

1. `TRANSFORMATION_BEGIN`
2. `TRANSFORMATION_END`

with contiguous observer sequence numbers.

The expected semantic relation is:

`R*(BEGIN, END) iff seq(BEGIN) < seq(END)`

No additional transformation event may occur between BEGIN and END in the initial serial prototype.

## 10. P1–P8 fixture obligations

| Test | Fixture criterion |
|---|---|
| P1 identity stability | Same frozen transformation/binding metadata yields identical transformation identity |
| P2 execution uniqueness | One activation receives one observer execution identity |
| P3 state determinism | Same semantic fixture state serializes to identical bytes/digest |
| P4 boundary integrity | Pre-state is captured before mutation; post-state after mutation |
| P5 sequence integrity | Sequence is contiguous and strictly increasing |
| P6 seriality | No overlapping transformation execution |
| P7 provenance integrity | All revisions and fixture artefacts resolve to frozen digests |
| P8 firewall | No value/reward/outcome field appears in trace |

## 11. Scientific firewall

The fixture explicitly excludes:

- value;
- utility;
- reward;
- performance score;
- downstream outcome;
- market/business variable;
- TGCV value construction result.

The fixture is an observation/instrumentation test only.

## 12. Fixture freeze gate

Before implementation, a fixture-level preflight must verify:

1. all five XMI artefacts exist;
2. metamodel namespaces resolve;
3. root references resolve;
4. initial activation count is exactly one;
5. expected post-state is semantically consistent with the existing PF-09 result;
6. no hidden outcome/value variable enters the observed state;
7. all fixture bytes receive SHA-256 digests;
8. fixture revision is immutable for the subsequent instrumentation preflight.

## 13. Decision

**DESIGN SPECIFICATION READY FOR FIXTURE-LEVEL PREFLIGHT.**

This document does not freeze fixture bytes, authorize instrumentation implementation, or authorize scientific execution.

## Next gate

Perform the **VIATRA Minimal Fixture-Level Instrumentation Contract Preflight** against the actual XMI artefacts and source revision. If any referenced fixture artefact is absent or cannot be resolved deterministically, stop and report the missing dependency rather than reconstructing it implicitly.
