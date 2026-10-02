# TGCV VIATRA Minimal Fixture Specification v001

**Status:** SPECIFICATION COMPLETE — pending fixture canonicalization audit  
**Date:** 2026-10-02  
**Framework revision:** ffa111dbb160c0bc55e89ea16430e97a38908662  
**Fixture identifier:** TGCV_VIATRA_MINIMAL_FIXTURE_v001

## 1. Purpose

Define one deterministic, minimal CPS-to-Deployment event-driven transformation fixture for validating the TGCV runtime observation boundary.

This fixture is an instrumentation test object. It is **not** a scientific test of R* and does not authorize scientific execution.

VIATRA documentation establishes that a CPS HostInstance has a unique node IP address and that the documented HostRule CREATED action creates a DeploymentHost, sets its IP from the HostInstance node IP, and creates a CPS-to-Deployment trace linking source and target. citeturn0search0turn0search3

## 2. Frozen semantic fixture

### 2.1 CPS input

Exactly one semantic HostInstance:

- semantic_key = host:H001
- identifier = H001
- nodeIp = 10.0.0.1

No ApplicationType, ApplicationInstance, state machine, transition, trigger, requirement or additional HostInstance is included.

### 2.2 Deployment initial state

Exactly one Deployment root exists.

It contains zero DeploymentHost elements.

### 2.3 Traceability initial state

Exactly one CPSToDeployment root exists.

It contains zero CPS2DeploymentTrace elements.

### 2.4 Transformation

Exactly one rule is admitted:

- semantic rule identifier: HostRule
- precondition: HostInstance match
- activation state: CREATED
- action:
  1. read HostInstance.nodeIp;
  2. create one DeploymentHost;
  3. assign DeploymentHost.ip = HostInstance.nodeIp;
  4. create one CPS2DeploymentTrace;
  5. link HostInstance to the created DeploymentHost.

No ApplicationRule or other transformation rule is part of the fixture.

The rule semantics correspond to the documented VIATRA example. citeturn0search0turn0search1

## 3. Canonical semantic keys

Runtime EMF object identity is excluded.

The fixture assigns semantic keys before instrumentation:

| Element | Semantic key |
|---|---|
| HostInstance | host:H001 |
| DeploymentHost | deploymentHost:DH001 |
| CPS2DeploymentTrace | trace:T001 |
| Deployment root | deployment:ROOT |
| CPSToDeployment root | traceability:ROOT |

The target and trace keys are deterministic expected identities of this fixture, not Java object identities.

## 4. Canonical state records

The state projection uses the record grammar:

entity_type | entity_key | attribute_name | canonical_value

### 4.1 Initial state records

The canonical semantic records are:

    Deployment|deployment:ROOT|exists|TRUE
    HostInstance|host:H001|identifier|H001
    HostInstance|host:H001|nodeIp|10.0.0.1
    CPSToDeployment|traceability:ROOT|exists|TRUE
    DeploymentHost|deploymentHost:DH001|exists|FALSE
    CPS2DeploymentTrace|trace:T001|exists|FALSE

### 4.2 Expected post-state records

    Deployment|deployment:ROOT|exists|TRUE
    HostInstance|host:H001|identifier|H001
    HostInstance|host:H001|nodeIp|10.0.0.1
    CPSToDeployment|traceability:ROOT|exists|TRUE
    DeploymentHost|deploymentHost:DH001|exists|TRUE
    DeploymentHost|deploymentHost:DH001|ip|10.0.0.1
    CPS2DeploymentTrace|trace:T001|exists|TRUE
    CPS2DeploymentTrace|trace:T001|cpsElement|host:H001
    CPS2DeploymentTrace|trace:T001|deploymentElement|deploymentHost:DH001

The records are sorted lexicographically by (entity_type, entity_key, attribute_name) before encoding.

## 5. Byte-level canonical encoding

For v001, each field is encoded as UTF-8 preceded by its decimal byte length and a colon:

< byte_length >:<UTF8_bytes>

A record is:

field1#field2#field3#field4 followed by LF.

The state stream begins with:

TGCV_STATE_v001 followed by LF.

No platform-default charset, locale, line ending or object serialization is permitted.

The state digest is SHA-256 over the complete canonical UTF-8 byte stream.

## 6. Transformation identity

Canonical transformation identity input is:

    framework_revision=ffa111dbb160c0bc55e89ea16430e97a38908662
    fixture_revision=TGCV_VIATRA_MINIMAL_FIXTURE_v001
    rule_id=HostRule
    activation_state=CREATED
    binding_schema_version=TGCV_VIATRA_BINDING_v001

Fields are ordered exactly as shown, separated by LF, with a final LF.

The SHA-256 digest of this byte sequence is the fixture's canonical transformation_id.

This identity excludes event sequence, timestamps, Java object identity, outputs, outcomes, reward, utility and value.

## 7. Binding

The only semantic binding is:

    hostInstance = host:H001

The binding is serialized as:

binding_schema=TGCV_VIATRA_BINDING_v001 followed by LF
hostInstance=host:H001 followed by LF

Its digest is provenance metadata for the activation; it is not part of the transformation identity unless explicitly included by the identity tuple above.

## 8. Expected event sequence

The first implementation run is serial and must contain exactly:

1. TRANSFORMATION_BEGIN
2. TRANSFORMATION_END

The observer assigns:

- BEGIN: event_seq=1
- END: event_seq=2

The fixture therefore tests the mechanics of observer ordering, pre/post state capture and completeness, but cannot by itself establish an independent R*.

## 9. Expected state transition

The only permitted semantic transition is:

    initial_state
      -> HostRule(CREATED)
      -> post_state

Expected invariant:

post_state - initial_state contains exactly the DeploymentHost and trace records specified above.

No unrelated model mutation is permitted.

## 10. Fixture integrity checks

Before implementation is admitted, the fixture audit must verify:

- exactly one HostInstance;
- exactly one Deployment root;
- exactly one CPSToDeployment root;
- zero initial DeploymentHosts;
- zero initial CPS2DeploymentTraces;
- no ApplicationInstance or additional transformation rule;
- semantic keys are unique;
- initial canonical record set matches this specification;
- expected post-state record set matches this specification;
- transformation identity input matches this specification;
- no value/outcome/reward field exists.

## 11. Scientific firewall

The fixture contains no:

- U_t;
- T_acc;
- accessibility label;
- future assignment;
- outcome;
- utility;
- reward;
- value;
- performance metric.

It is solely a controlled runtime observation fixture.

## 12. Status and next gate

**SPECIFICATION COMPLETE — pending fixture canonicalization audit.**

This document freezes the semantic fixture specification, but does not yet claim that a concrete EMF/XMI artifact has been generated or hash-verified.

**Next gate:** perform the **Minimal Fixture Canonicalization Audit**, including byte-level reconstruction and verification against the actual VIATRA metamodel. Only after PASS may an immutable fixture artifact be generated and considered for instrumentation implementation.
