# TGCV VIATRA v002 Runtime Equivalence Preflight Specification v001

**Status:** READY FOR CONTROLLED PREFLIGHT — execution not yet performed
**Date:** 2026-10-02
**Core revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`
**Examples revision:** `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`
**Fixture:** `TGCV_VIATRA_MINIMAL_FIXTURE_v002`

## 1. Purpose

Establish the minimum executable gate required to demonstrate that the materialized v002 fixture is semantically equivalent to the concrete VIATRA CPS-to-Deployment transformation before any runtime observation is admitted.

This gate is a runtime-equivalence preflight, not a scientific experiment.

## 2. Operational constraint

The canonical TGCV README requires reproducibility through repository-controlled protocols, manifests, provenance and code. The preflight must therefore execute from pinned GitHub revisions and must not depend on an untracked local reconstruction.

## 3. Immutable inputs

### VIATRA core

`eclipse-viatra/org.eclipse.viatra`

Revision:

`ffa111dbb160c0bc55e89ea16430e97a38908662`

### VIATRA examples

`eclipse-viatra/org.eclipse.viatra.examples`

Revision:

`15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`

### TGCV

The fixture specification and materialized artifacts must be taken from the TGCV commit containing:

`TGCV_VIATRA_MINIMAL_FIXTURE_v002`

and

`TGCV_VIATRA_V002_CONCRETE_FIXTURE_MATERIALIZATION_BYTE_AUDIT_001`.

## 4. Preflight checks

The execution must PASS all of the following.

### PF-01 — revision pinning

The checked-out VIATRA core and examples repositories must report exactly the two revisions above.

**Failure:** any other commit, floating branch, tag without resolved SHA, or dirty source tree.

### PF-02 — metamodel loading

Load the CPS, Deployment and CPS traceability Ecore packages used by the concrete examples transformation.

Required classes:

- `CyberPhysicalSystem`
- `HostType`
- `HostInstance`
- `Deployment`
- `DeploymentHost`
- `CPSToDeployment`
- `CPS2DeploymentTrace`

Required features:

- `HostType.identifier`
- `HostInstance.identifier`
- `HostInstance.nodeIp`
- `Deployment.hosts`
- `DeploymentHost.ip`
- `CPSToDeployment.cps`
- `CPSToDeployment.deployment`
- `CPSToDeployment.traces`
- `CPS2DeploymentTrace.cpsElements`
- `CPS2DeploymentTrace.deploymentElements`

### PF-03 — initial fixture loading

Load:

- v002 CPS XMI;
- v002 Deployment INITIAL XMI;
- v002 Traceability INITIAL XMI.

Required cardinalities:

- CPS root = 1;
- HostType = 1;
- HostInstance = 1;
- Deployment root = 1;
- DeploymentHost = 0;
- CPSToDeployment = 1;
- CPS2DeploymentTrace = 0.

Required source values:

- HostType.identifier = `Rawsberry.PI`;
- HostInstance.identifier = `Aragorn`;
- HostInstance.nodeIp = `152.66.102.6`.

### PF-04 — root mapping

Resolve the concrete `rootMapping` used by the transformation.

Required result:

- exactly one `CPSToDeployment`;
- its `cps` reference resolves to the loaded CPS root;
- its `deployment` reference resolves to the loaded Deployment root.

### PF-05 — query cardinality

Evaluate the concrete query `unmappedHostInstance` before transformation.

Required result:

- exactly one match;
- `hostType.identifier = Rawsberry.PI`;
- `hostInstance.identifier = Aragorn`;
- `hostInstance.nodeIp = 152.66.102.6`.

Evaluate the other host-side predicates relevant to this transition.

Required result:

- no pre-existing mapped host for Aragorn;
- no deleted deployment host match.

The preflight must also verify that no application/state/transition/trigger mapping introduces a relevant activation for this minimal fixture.

### PF-06 — HostMapping activation

Instantiate the concrete `HostMapping` rule specification from `HostRules.xtend`.

Required lifecycle:

`CREATED`

Required activation cardinality:

**exactly 1**

Required binding:

`UnmappedHostInstance.Match(hostInstance=Aragorn, hostType=Rawsberry.PI)`

### PF-07 — controlled runtime application

Apply only the concrete transformation mechanism to the initial fixture.

The preflight is not authorized to collect scientific metrics.

It may observe model mutation only for equivalence verification.

### PF-08 — actual post-state

Required structural delta:

1. one new `DeploymentHost`;
2. `DeploymentHost.ip = 152.66.102.6`;
3. one new `CPS2DeploymentTrace`;
4. trace.cpsElements contains exactly the Aragorn HostInstance;
5. trace.deploymentElements contains exactly the newly created DeploymentHost.

Required final cardinalities:

- DeploymentHost = 1;
- CPS2DeploymentTrace = 1.

### PF-09 — semantic equivalence

Project the actual post-state to the canonical semantic records defined by v002.

The projection must equal the expected v002 semantic projection.

Comparison must be semantic, not Java-object-identity based.

### PF-10 — no contamination

The runtime result must not introduce:

- `CPS2DeploymentTrace.id`;
- TGCV-derived trace IDs into the VIATRA model;
- timestamps as model attributes;
- Java object identity;
- value/reward/utility/outcome fields;
- accessibility labels;
- scientific scores.

## 5. Runtime observation boundary

The preflight may record:

- pinned revisions;
- loaded-model cardinalities;
- query match cardinalities;
- activation identity;
- pre/post structural projections;
- exact runtime errors;
- exact toolchain versions.

It must not record a scientific observation as a result of this gate.

## 6. Required output artifact

The execution must produce:

`TGCV_VIATRA_V002_RUNTIME_EQUIVALENCE_PREFLIGHT_RESULT_001.json`

with at minimum:

- status;
- core_revision;
- examples_revision;
- tgcv_fixture_revision;
- java_version;
- build_tool_version;
- metamodel_load_status;
- root_mapping_count;
- unmapped_host_instance_count;
- host_mapping_created_activation_count;
- unexpected_relevant_activation_count;
- actual_post_state_projection;
- expected_post_state_projection;
- semantic_equivalence;
- contamination_check;
- failure_details.

The JSON must contain no scientific outcome/value/reward metric.

## 7. PASS criterion

The gate is PASS iff:

`PF-01 ... PF-10 = PASS`

and:

`semantic_equivalence = TRUE`

and:

`contamination_check = PASS`.

## 8. Current state

The static materialization/byte audit is already PASS.

The runtime-equivalence state is currently:

**NOT EXECUTED**

No claim of runtime equivalence is made until a pinned execution produces the result artifact.

## 9. Next operational action

Create and run a dedicated GitHub Actions **manual preflight workflow** using the pinned revisions above.

The workflow must be separate from any scientific execution workflow and must require explicit manual dispatch.

No `--execute` scientific authorization is implied by this preflight.
