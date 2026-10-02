# TGCV VIATRA Minimal Transformation Fixture Selection Review

**Status:** SELECTED CANDIDATE — fixture not yet frozen or executed  
**Date:** 2026-10-02  
**Candidate framework revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`

## Selection

The selected fixture family is the repository's documented **event-driven CPS-to-Deployment transformation**.

The VIATRA documentation explicitly provides:
- a CPS source model;
- a Deployment target model;
- a traceability model;
- event-driven transformation rules;
- explicit CREATED, UPDATED and DELETED activation actions;
- a fixed-priority conflict resolver;
- a concrete transformation construction sequence.

This is preferable to inventing an abstract fixture because the transformation semantics are already documented in the frozen VIATRA revision.

## Minimal TGCV fixture

For the first instrumentation prototype, use the smallest model instance containing:

1. one `HostInstance`;
2. one transformation rule that reacts to the host instance;
3. one corresponding `DeploymentHost`;
4. one traceability relation;
5. one controlled CREATED transformation event.

The first prototype should not include application rules, deletion events, downstream performance, value or other outcome variables.

## Canonical transformation identity

The fixture-level `transformation_id` is defined from:

- frozen VIATRA source revision;
- fixture specification revision;
- rule identifier;
- activation-state identifier (`CREATED`);
- canonical binding representation.

Runtime Java object identity is explicitly excluded.

## Canonical state projection

The initial observed state projection is restricted to the semantic model elements required by the one-host transformation:

- host-instance identifier;
- host-instance attributes used by the rule;
- deployment-host existence/attributes;
- traceability relation relevant to the transformation.

The projection excludes:
- Java object identity;
- memory/runtime addresses;
- query-engine internals;
- debugger state;
- timestamps;
- value/reward/outcome variables.

A canonical serializer for this projection must be specified and tested before implementation.

## Why this fixture is suitable

It provides a concrete transformation with explicit model mutation: the documented CREATED action creates a DeploymentHost and a trace entry. The documentation also demonstrates a fixed conflict resolver for the broader transformation, while the minimal one-rule fixture avoids unnecessary rule interactions.

This supports a clean first test of:
- activation identity;
- pre/post state capture;
- observer sequence ordering;
- deterministic state hashing;
- provenance and completeness.

## Limitations

This fixture does **not** establish that an independent R* exists. It only provides a controlled environment in which the observation boundary can be tested.

The minimal single-event fixture also cannot discriminate temporal organisation by itself. A later paired-run design must introduce multiple transformation events while holding the inherited representation A fixed, if and only if the instrumentation prototype passes.

## Decision

**SELECTED CANDIDATE — NOT YET FROZEN.**

No scientific execution is authorized.

## Next gate

Create the **Fixture Canonical State & Transformation Identity Contract**, freeze its exact semantic projection and identity encoding, and then run a fixture-level preflight.
