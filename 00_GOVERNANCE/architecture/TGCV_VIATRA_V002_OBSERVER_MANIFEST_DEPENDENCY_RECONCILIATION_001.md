# TGCV VIATRA V002 Observer MANIFEST Dependency Reconciliation 001

## Status

SUPERSEDED — PRE-BUILD MANIFEST RECONCILIATION.

The observer manifest was subsequently materialized and the complete Tycho host build was verified by run `37123064623`. This document records the earlier dependency-design state and is not the current manifest contract.

## Evidence boundaries

The observer specification requires:
- CPS, Deployment and Traceability metamodel/runtime artifacts;
- fixture loading;
- serial lifecycle observation;
- deterministic serialization;
- provenance.

The frozen implementation source is the `hostRule` tutorial binding at:

`eclipse-viatra/org.eclipse.viatra` revision `ffa111dbb160c0bc55e89ea16430e97a38908662`.

The recovered historical implementation is an Eclipse/OSGi bundle whose MANIFEST declares the concrete VIATRA, CPS, Deployment and Traceability dependencies.

## Current observer MANIFEST

Current required bundle:

`org.eclipse.emf.ecore`

This is not sufficient to implement the specified observer host.

## Decision

Do NOT bulk-copy the historical implementation MANIFEST into the observer.

The observer is a distinct TGCV component and should declare only dependencies actually used by its implementation.

The following dependency families are therefore required for the next implementation phase, but their exact bundle coordinates must be bound before insertion:

1. EMF/Ecore/XMI infrastructure for fixture loading and deterministic serialization;
2. CPS model bundle;
3. Deployment model bundle;
4. Traceability model bundle;
5. VIATRA query/runtime APIs needed to identify and observe the selected transformation activation;
6. VIATRA transformation/EVM APIs only if the observer implementation directly consumes lifecycle events from those APIs.

## Important distinction

Historical implementation dependencies establish what the original transformation project could access. They do not, by themselves, prove that every dependency belongs in the observer.

The observer MANIFEST therefore remains intentionally minimal until the observer classes are materialized and their imports can be reconciled against pinned bundles.

## Build boundary

No dependency resolution was performed.

No build was performed.

No runtime execution was performed.

## Next gate

Materialize the observer implementation skeleton and its fixture/serialization interfaces without adding speculative runtime dependencies. Then derive the exact MANIFEST imports from the concrete implementation and bind each dependency to a pinned historical bundle/source coordinate.
