# TGCV VIATRA Minimal Fixture Specification v002

**Status:** SPECIFICATION COMPLETE — concrete example-backed semantics
**Date:** 2026-10-02
**VIATRA core revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`
**VIATRA examples revision:** `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`
**Fixture identifier:** `TGCV_VIATRA_MINIMAL_FIXTURE_v002`

## 1. Purpose

Define the smallest concrete CPS-to-Deployment fixture that is directly backed by the VIATRA CPS example repository and can be used as a controlled runtime observation fixture.

This fixture is **not** a scientific test of R* and does not authorize scientific execution.

v002 supersedes v001 because v001 treated TGCV-derived semantic keys as if they were VIATRA model attributes and represented the concrete trace structure without direct artifact verification.

## 2. Evidence basis

The concrete example repository is:

`eclipse-viatra/org.eclipse.viatra.examples`

The examples repository has an independent Git history from the VIATRA core repository. No one-to-one commit identity is assumed.

The selected examples revision is the immutable commit:

`15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`

The relevant CPS transformation artifacts are unchanged between the immediately preceding CPS demonstrator update `e30943a5c6d42df5d1ee94cd01094773d9c66c9e` and `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`; the intervening commits modify build/CI/dependency metadata only.

### 2.1 Concrete metamodel artifacts

Traceability:

`cps/domains/org.eclipse.viatra.examples.cps.traceability/model/traceability.ecore`

It defines:

- `CPSToDeployment.cps : CyberPhysicalSystem`
- `CPSToDeployment.deployment : Deployment`
- `CPSToDeployment.traces : CPS2DeploymentTrace[*]`, containment
- `CPS2DeploymentTrace.cpsElements : Identifiable[*]`
- `CPS2DeploymentTrace.deploymentElements : DeploymentElement[*]`

Deployment:

`cps/domains/org.eclipse.viatra.examples.cps.deployment/model/deployment.ecore`

It defines:

- `Deployment.hosts : DeploymentHost[*]`, containment
- `DeploymentHost.applications : DeploymentApplication[*]`, containment
- `DeploymentHost.ip : EString`, ID
- `DeploymentHost` extends `DeploymentElement`

CPS:

`cps/domains/org.eclipse.viatra.examples.cps.model/model/model.ecore`

Relevant classes/features:

- `HostType.identifier : EString`, ID
- `HostType.instances : HostInstance[*]`, containment
- `HostInstance.identifier : EString`, ID
- `HostInstance.nodeIp : EString`
- `CyberPhysicalSystem.hostTypes : HostType[*]`, containment

### 2.2 Concrete transformation artifacts

Transformation entry point:

`cps/transformations/org.eclipse.viatra.examples.cps.xform.m2m.incr.expl/src/org/eclipse/viatra/examples/cps/xform/m2m/incr/expl/CPS2DeploymentTransformation.xtend`

The transformation registers rule groups for hosts, applications, state machines, states, transitions and triggers.

Host rules:

`cps/transformations/org.eclipse.viatra.examples.cps.xform.m2m.incr.expl/src/org/eclipse/viatra/examples/cps/xform/m2m/incr/expl/rules/HostRules.xtend`

The concrete host mapping rule is `HostMapping`.

Its CREATED action:

1. reads `match.hostInstance.nodeIp`;
2. creates a `DeploymentHost`;
3. assigns `host.ip = nodeIp`;
4. adds the host to `rootMapping.deployment.hosts`;
5. creates a `CPS2DeploymentTrace`;
6. adds the matched `HostInstance` to `trace.cpsElements`;
7. adds the created `DeploymentHost` to `trace.deploymentElements`.

The query definitions are in:

`cps/transformations/org.eclipse.viatra.examples.cps.xform.m2m.incr.expl/src/org/eclipse/viatra/examples/cps/xform/m2m/incr/expl/queries/cpsXformM2M.vql`

The relevant patterns are:

- `mappedCPS`
- `cps2depTrace`
- `hostInstances`
- `mappedHostInstance`
- `monitoredHostInstance`
- `unmappedHostInstance`
- `deletedDeploymentHost`

The `rootMapping` accessor requires exactly one `CPSToDeployment` mapping.

## 3. Minimal concrete CPS fixture

The source-side fixture contains exactly:

- one `CyberPhysicalSystem` root;
- one `HostType`;
- one `HostInstance` under that HostType.

No application types, application instances, requests, state machines, states, transitions, signals or additional hosts are included.

### 3.1 Source-side values

The fixture deliberately uses identifiers and values occurring in the concrete VIATRA example model:

- `HostType.identifier = Rawsberry.PI`
- `HostInstance.identifier = Aragorn`
- `HostInstance.nodeIp = 152.66.102.6`

These are real VIATRA example-model values, not invented fixture values.

The corresponding source fragment is represented by the following minimal EMF/XMI structure:

    <cps:CyberPhysicalSystem
        xmlns:cps="http://org.eclipse.viatra/model/cps">
      <hostTypes identifier="Rawsberry.PI">
        <instances
            identifier="Aragorn"
            nodeIp="152.66.102.6"/>
      </hostTypes>
    </cps:CyberPhysicalSystem>

The root `CyberPhysicalSystem` has no required identifier.

## 4. Initial target and mapping state

### 4.1 Deployment

Exactly one `Deployment` root exists.

Initial `Deployment.hosts` is empty.

No `DeploymentHost` exists before execution.

### 4.2 Traceability

Exactly one `CPSToDeployment` root exists.

Its required semantic bindings are:

- `cps ->` the fixture CPS root;
- `deployment ->` the fixture Deployment root.

Initial `CPSToDeployment.traces` is empty.

No `CPS2DeploymentTrace` exists before execution.

This structure is directly supported by the concrete `traceability.ecore` artifact and by the `mappedCPS` query.

## 5. Expected concrete transformation activation

The complete VIATRA transformation registers all rule groups, but this minimal fixture is constructed so that the only source-side mapping activation is:

- rule class: `HostMapping`
- semantic operation: CPS HostInstance -> DeploymentHost + trace
- activation state: `CREATED`
- query: `unmappedHostInstance`
- binding:
  - `hostType = Rawsberry.PI`
  - `hostInstance = Aragorn`

No application, state-machine, state, transition or trigger mapping should have a valid match.

The fixture therefore does **not** claim that the runtime contains only one registered rule specification. It claims that the controlled input exposes one relevant HostMapping CREATED activation.

## 6. Expected post-state

The concrete target object has the actual VIATRA identity attribute:

    DeploymentHost.ip = 152.66.102.6

Because `DeploymentHost.ip` is an EString ID, this value is the actual model-level identity of the created DeploymentHost.

The expected structural post-state is:

- one Deployment root;
- one DeploymentHost in `Deployment.hosts`;
- `DeploymentHost.ip = 152.66.102.6`;
- one CPS2DeploymentTrace in `CPSToDeployment.traces`;
- the trace contains the CPS HostInstance `Aragorn` in `cpsElements`;
- the same trace contains the created DeploymentHost in `deploymentElements`.

The concrete trace shape is therefore:

    CPS2DeploymentTrace
      cpsElements -> HostInstance(identifier=Aragorn)
      deploymentElements -> DeploymentHost(ip=152.66.102.6)

There is no trace ID attribute in the concrete metamodel.

## 7. TGCV semantic keys

TGCV may assign semantic observation keys, but these are explicitly **derived identifiers**, not VIATRA model attributes.

### 7.1 Source key

    host:HID-Aragorn

Derivation:

    HostInstance.identifier = Aragorn

### 7.2 Target key

    deploymentHost:IP-152.66.102.6

Derivation:

    DeploymentHost.ip = 152.66.102.6

This is admissible because `ip` is an actual EString ID in the concrete metamodel.

### 7.3 Trace observation key

The concrete `CPS2DeploymentTrace` has no identifier attribute.

TGCV therefore derives:

    trace:host:HID-Aragorn->deploymentHost:IP-152.66.102.6

This key is a TGCV observation identifier only. It must never be serialized back into the VIATRA model as a `CPS2DeploymentTrace.id` attribute.

## 8. Canonical observation records

The canonical observation projection is:

    entity_type | entity_key | attribute_name | canonical_value

### 8.1 Initial semantic records

    CPSToDeployment|traceability:ROOT|exists|TRUE
    CyberPhysicalSystem|cps:ROOT|exists|TRUE
    HostType|hostType:Rawsberry.PI|identifier|Rawsberry.PI
    HostInstance|host:HID-Aragorn|identifier|Aragorn
    HostInstance|host:HID-Aragorn|nodeIp|152.66.102.6
    Deployment|deployment:ROOT|exists|TRUE
    DeploymentHost|deploymentHost:IP-152.66.102.6|exists|FALSE
    CPS2DeploymentTrace|trace:host:HID-Aragorn->deploymentHost:IP-152.66.102.6|exists|FALSE

### 8.2 Expected post-state semantic records

    CPSToDeployment|traceability:ROOT|exists|TRUE
    CyberPhysicalSystem|cps:ROOT|exists|TRUE
    HostType|hostType:Rawsberry.PI|identifier|Rawsberry.PI
    HostInstance|host:HID-Aragorn|identifier|Aragorn
    HostInstance|host:HID-Aragorn|nodeIp|152.66.102.6
    Deployment|deployment:ROOT|exists|TRUE
    DeploymentHost|deploymentHost:IP-152.66.102.6|exists|TRUE
    DeploymentHost|deploymentHost:IP-152.66.102.6|ip|152.66.102.6
    CPS2DeploymentTrace|trace:host:HID-Aragorn->deploymentHost:IP-152.66.102.6|exists|TRUE
    CPS2DeploymentTrace|trace:host:HID-Aragorn->deploymentHost:IP-152.66.102.6|cpsElements|host:HID-Aragorn
    CPS2DeploymentTrace|trace:host:HID-Aragorn->deploymentHost:IP-152.66.102.6|deploymentElements|deploymentHost:IP-152.66.102.6

The records are sorted lexicographically by `(entity_type, entity_key, attribute_name)` before canonical encoding.

## 9. Runtime identity exclusion

The fixture explicitly excludes:

- Java object identity;
- EMF object memory identity;
- resource URI fragment as a TGCV identity key;
- generated Java class identity;
- execution timestamp;
- event ordering as an entity identity;
- any TGCV-derived trace key from the VIATRA model itself.

The XMI URI fragments used by the example repository are provenance references only.

## 10. Transformation identity

The canonical transformation identity input for v002 is:

    framework_revision=ffa111dbb160c0bc55e89ea16430e97a38908662
    fixture_revision=TGCV_VIATRA_MINIMAL_FIXTURE_v002
    examples_revision=15f269dbf74000eac7b97cf7f92e256b8fb1fc1c
    rule_id=HostMapping
    activation_state=CREATED
    binding_schema_version=TGCV_VIATRA_BINDING_v002

Fields are ordered exactly as shown, separated by LF, with a final LF.

The resulting SHA-256 is:

    23af6acbbeb9b641d3d4cced837c98cc4feee4b953c8a6866fa9a88f72af2f7f

This identity excludes event sequence, timestamps, Java object identity, outcomes, reward, utility and value.

## 11. Binding

The binding schema is:

    binding_schema=TGCV_VIATRA_BINDING_v002
    hostType=hostType:Rawsberry.PI
    hostInstance=host:HID-Aragorn
    hostInstance.identifier=Aragorn
    hostInstance.nodeIp=152.66.102.6

The binding values are provenance/observation metadata. They are not additional VIATRA model attributes.

## 12. Expected semantic transition

The controlled semantic transition is:

    initial CPS + empty Deployment + empty traces
        |
        | HostMapping(CREATED)
        v
    CPS + DeploymentHost(ip=152.66.102.6)
        + CPS2DeploymentTrace(Aragorn -> DeploymentHost)

The expected newly created semantic elements are exactly:

1. one DeploymentHost;
2. one CPS2DeploymentTrace.

The expected trace contains exactly one CPS element and exactly one Deployment element.

## 13. Concrete rule semantics relevant to the fixture

The actual `HostMapping` implementation performs:

    nodeIp = match.hostInstance.nodeIp
    host = createDeploymentHost
    host.ip = nodeIp
    rootMapping.deployment.hosts += host
    trace = createCPS2DeploymentTrace
    trace.cpsElements += match.hostInstance
    trace.deploymentElements += host

This is the authoritative rule-level basis for the fixture.

The generic VIATRA core traceability metamodel remains distinct from this application-specific traceability metamodel.

## 14. Integrity gates

Before an immutable fixture artifact is admitted, verify:

- the examples revision is exactly `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`;
- the core revision is exactly `ffa111dbb160c0bc55e89ea16430e97a38908662`;
- the CPS Ecore package URI is `http://org.eclipse.viatra/model/cps`;
- the deployment Ecore package URI is `http://org.eclipse.viatra/model/deployment`;
- the traceability Ecore package URI is `http://org.eclipse.viatra/model/cps-traceability`;
- exactly one HostType exists;
- exactly one HostInstance exists;
- HostType.identifier is `Rawsberry.PI`;
- HostInstance.identifier is `Aragorn`;
- HostInstance.nodeIp is `152.66.102.6`;
- exactly one Deployment root exists;
- Deployment.hosts is initially empty;
- exactly one CPSToDeployment root exists;
- its cps and deployment references are populated;
- CPSToDeployment.traces is initially empty;
- no TGCV trace ID is written into the VIATRA model;
- the only relevant mapping activation is HostMapping(CREATED);
- the created DeploymentHost has ip `152.66.102.6`;
- the created trace has one cpsElements entry and one deploymentElements entry;
- no application/state/transition/trigger artifact is introduced;
- canonical semantic records reproduce the expected initial and post-state projections;
- the transformation identity digest matches the specification;
- no value/outcome/reward field exists.

## 15. Scientific firewall

The fixture contains no:

- U_t;
- T_acc;
- accessibility label;
- future assignment;
- outcome;
- utility;
- reward;
- value;
- scientific performance metric.

It is solely a controlled runtime observation fixture.

## 16. Status and next gate

**SPECIFICATION COMPLETE — concrete example-backed semantics.**

v002 is the corrected specification candidate. It does not freeze a generated EMF/XMI artifact and does not authorize instrumentation or scientific execution.

**Next gate:** perform the **VIATRA v002 Concrete Fixture Materialization & Byte Audit**, generating the minimal concrete CPS/Deployment/CPSToDeployment artifacts from the verified metamodel and checking their exact canonical bytes and hashes against this specification.
