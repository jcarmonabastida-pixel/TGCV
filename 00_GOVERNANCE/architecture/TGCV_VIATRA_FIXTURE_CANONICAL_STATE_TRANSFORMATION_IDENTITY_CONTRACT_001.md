# TGCV VIATRA Fixture Canonical State & Transformation Identity Contract

**Status:** CONTRACT DRAFT FOR PREFLIGHT — no implementation or scientific execution authorized  
**Date:** 2026-10-02  
**Framework revision:** ffa111dbb160c0bc55e89ea16430e97a38908662  
**Fixture family:** CPS-to-Deployment event-driven transformation

## 1. Scope

This contract freezes the semantic observation boundary for the minimal one-HostInstance / CREATED transformation fixture.

The fixture is deliberately smaller than the documented full CPS-to-Deployment transformation. It contains one controlled transformation event and exists first to validate observation integrity, not to test TGCV discrimination.

## 2. Canonical observed state

The state projection contains exactly these semantic records:

### CPS input
- HostInstance.identifier
- HostInstance.nodeIp

### Deployment output
- existence of the corresponding DeploymentHost;
- DeploymentHost.ip.

### Traceability
- existence of the corresponding CPS-to-Deployment trace;
- identity of the linked CPS element;
- identity of the linked deployment element.

No other model element or runtime structure is part of the initial state projection.

## 3. State serialization

Canonical state is encoded as an ordered UTF-8 record sequence.

Each record has:

entity_type | entity_key | attribute_name | canonical_value

Canonicalization rules:

1. records sorted lexicographically by the tuple (entity_type, entity_key, attribute_name);
2. UTF-8 encoding;
3. no Java object identity;
4. no memory address;
5. no hash-map iteration order;
6. absent optional values represented by an explicit NULL token;
7. strings encoded with length-prefixed UTF-8;
8. numeric values represented in a single frozen textual form;
9. schema version prepended to the canonical byte stream;
10. digest computed over the resulting bytes using SHA-256.

The exact escaping/length-prefix syntax must be implemented and tested before scientific use.

## 4. Pre-state

Before the CREATED transformation:

- HostInstance record exists;
- DeploymentHost record does not exist;
- corresponding trace does not exist.

The pre-state digest must encode absence of output/trace records explicitly rather than infer absence from missing serialization.

## 5. Post-state

After the CREATED transformation:

- the HostInstance remains present;
- DeploymentHost exists with the rule-derived IP;
- corresponding trace exists and links the source and target elements.

The post-state digest is computed over the same schema and state scope.

## 6. Transformation identity

Canonical transformation_id input tuple:

framework_revision | fixture_revision | rule_id | activation_state | binding_schema_version

For the minimal fixture:

- rule_id = HostInstance-CREATED;
- activation_state = CREATED;
- binding_schema_version = TGCV_VIATRA_BINDING_v001.

The transformation identity must not contain:
- event sequence;
- timestamp;
- Java object identity;
- output/result;
- reward/value;
- downstream performance.

The canonical byte representation of the tuple is hashed with SHA-256.

## 7. Activation instance identity

activation_instance_id is observer-assigned:

run_id + event_seq + local_activation_counter

It is an execution-instance identifier, not a semantic identity.

## 8. Information firewall

The fixture and its canonical state must exclude:

- U_t;
- T_acc;
- accessibility labels;
- future assignments;
- outcomes;
- utility;
- reward;
- value;
- performance metrics.

The transformation is observed only through model state and execution events.

## 9. Determinism requirements

The fixture passes its contract only if:

- identical initial fixture bytes produce identical initial state digest;
- identical post-transformation semantic state produces identical post-state digest;
- transformation identity is identical across repeated runs;
- activation instance identities differ between runs as execution identifiers;
- event ordering is supplied by the observer sequence, not reconstructed from state.

## 10. Preflight decision states

- PASS — contract is fully specified and implementation can proceed.
- UNDERDETERMINED — serialization or identity encoding still contains unresolved semantics.
- FAIL — observation boundary is contaminated or non-reproducible.

## Decision

**CONTRACT DRAFT FOR PREFLIGHT.**

The semantic scope is now explicit, but the concrete fixture artifacts and exact byte-level serialization implementation still require validation.

## Next gate

Perform a Fixture Canonicalization Preflight against the actual VIATRA CPS/Deployment metamodel and determine whether the proposed fields and identity tuple can be instantiated without ambiguity.
