# TGCV VIATRA V002 Fixture-Level Preflight Construction Review

**Status:** CONSTRUCTION REVIEW PASS — PREFLIGHT NOT EXECUTED
**Date:** 2026-10-03
**Fixture:** `TGCV_VIATRA_MINIMAL_FIXTURE_v002`
**Purpose:** Close the deterministic construction of the fixture-level preflight before its first execution.

## 1. Gate boundary

This preflight is a deterministic fixture-contract audit. It must not invoke Maven, Tycho, Java runtime execution, VIATRA transformation execution, or scientific analysis.

It verifies repository bytes, XML structure, cross-file references, semantic fixture invariants that are directly encoded in the XMI, transformation identity metadata, and the scientific firewall.

A PASS does not freeze the fixture by itself. Fixture freeze remains a separate explicit gate.

## 2. Canonical inputs

The five authoritative fixture artefacts are:

- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_CPS.xmi`
- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_INITIAL.xmi`
- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_EXPECTED.xmi`
- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_INITIAL.xmi`
- `TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_EXPECTED.xmi`

Their SHA-256 values and exact byte counts are authoritative in `fixtures/TGCV_VIATRA_V002_FIXTURE_BYTE_HASH_MANIFEST_001.md`.

The source binding is pinned to historical examples revision `eb68158a3d74581f69ccb8bc4f47673b12abdf85`.

## 3. Static check construction

### F1 — byte identity

For every fixture artefact:

1. require the file to exist;
2. calculate SHA-256 over exact repository bytes;
3. compare byte count and SHA-256 with the canonical manifest;
4. fail on any mismatch;
5. never reconstruct or normalize the artefact before hashing.

### F2 — XML well-formedness

Parse each XMI as XML using a standard XML parser. No regular-expression parsing is used for XML structure.

### F3 — namespace/root identity

Require exactly these root namespace/local-name pairs:

- CPS: `http://org.eclipse.viatra/model/cps` / `CyberPhysicalSystem`
- Deployment: `http://org.eclipse.viatra/model/deployment` / `Deployment`
- Traceability: `http://org.eclipse.viatra/model/cps-traceability` / `CPSToDeployment`

Require `xmi:version="2.0"`.

### F4 — initial CPS semantic fixture

Require exactly:

- one `hostTypes` element;
- identifier `Rawsberry.PI`;
- one `instances` child;
- identifier `Aragorn`;
- nodeIp `152.66.102.6`.

No second relevant HostType or HostInstance may be present.

### F5 — initial Deployment semantic fixture

Require zero `hosts` elements.

### F6 — initial Traceability semantic fixture

Require:

- exactly one root `CPSToDeployment`;
- exactly one CPS root reference;
- exactly one Deployment root reference;
- no `traces` elements;
- CPS reference resolves to the canonical CPS filename and root fragment;
- Deployment reference resolves to the canonical INITIAL deployment filename and root fragment.

### F7 — expected Deployment semantic fixture

Require exactly one `hosts` element with:

- `ip="152.66.102.6"`.

### F8 — expected Traceability semantic fixture

Require:

- exactly one CPS root reference to the canonical CPS root;
- exactly one Deployment root reference to the canonical EXPECTED deployment root;
- exactly one `traces` element;
- exactly one `cpsElements` reference resolving to the canonical `Aragorn` instance fragment;
- exactly one `deploymentElements` reference resolving to the sole expected DeploymentHost fragment.

No additional trace mapping is admitted.

### F9 — direct expected-state correspondence

The preflight may verify only the direct structural correspondence encoded by the fixture:

- initial deployment hosts = 0 → expected deployment hosts = 1;
- expected host IP equals the CPS HostInstance nodeIp;
- initial traces = 0 → expected traces = 1;
- expected trace source resolves to `Aragorn`;
- expected trace target resolves to the created host.

It must not infer a scientific outcome or value.

### F10 — transformation identity

The preflight must validate the canonical metadata:

`(implementation_id, transformation_id, rule_id, fixture_contract_revision)`

with:

- implementation_id = `org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra`
- transformation_id = `CPS2DeploymentTransformationViatra`
- rule_id = `hostRule`
- fixture_contract_revision = `V002`

The implementation must reject identity encodings containing fixture-instance identifiers, IP addresses, activation IDs, URI fragments, Java object identity, timestamps, execution results, outcomes, value, or reward.

### F11 — P1–P8 contract surface

The preflight must establish deterministic inputs for P1–P8 without executing them:

- P1: identity metadata is fixed;
- P2: the fixture admits exactly one relevant activation;
- P3: canonical state fields are explicitly enumerated;
- P4: initial/expected boundaries are explicit;
- P5: serial event sequence is defined;
- P6: seriality is a declared contract;
- P7: source pin and byte hashes are fixed;
- P8: forbidden scientific fields are absent from the fixture schema.

Runtime properties that cannot be proven from static XMI must remain runtime gates.

### F12 — scientific firewall

Fail if the fixture introduces fields or metadata representing:

- value;
- utility;
- reward;
- performance score;
- downstream outcome;
- market/business variables;
- TGCV value-construction result.

The preflight itself must not calculate or emit any such quantity.

## 4. Implementation constraints

The preflight implementation must:

- be deterministic;
- use exact repository bytes for hashing;
- use an XML parser rather than grep/sed for XML semantics;
- avoid Maven/Tycho/Java/VIATRA execution;
- fail explicitly on every contract violation;
- print a final `VIATRA_V002_FIXTURE_PREFLIGHT=PASS` marker only after every check succeeds.

## 5. Checks deliberately excluded

The preflight must not claim to prove:

- actual VIATRA rule activation matching;
- actual rule firing;
- EMF runtime loading equivalence;
- runtime event ordering;
- observer serialization implementation;
- runtime seriality;
- Java object identity behavior.

Those belong to later gates.

## 6. Decision

**CONSTRUCTION REVIEW PASS — READY TO IMPLEMENT THE PREFLIGHT**

The fixture-level preflight contract is now closed sufficiently to implement without using workflow execution as a design/debugging loop.

The next operation is to create the deterministic preflight implementation, review it statically, and only then execute it once against `main`.
