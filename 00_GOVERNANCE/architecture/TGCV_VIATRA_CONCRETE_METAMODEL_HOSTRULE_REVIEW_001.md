# TGCV VIATRA Concrete Metamodel & HostRule Review

**Status:** PARTIAL EVIDENCE — target fixture semantics still not admissible  
**Date:** 2026-10-02  
**VIATRA revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`

## Findings

### 1. CPS instance evidence

The frozen repository contains concrete CPS instance files under:

`query/tests/org.eclipse.viatra.query.runtime.cps.tests/models/instances/`

including `demo.cyberphysicalsystem`.

The CPS model therefore provides a real source-side artifact rather than a synthetic schema.

### 2. Generic traceability metamodel

The frozen repository contains:

`transformation/plugins/org.eclipse.viatra.transformation.views/model/traceability.ecore`

with:

- `Traceability`, containing `traces` and `id`;
- `Trace`, containing `targets`, `id`, `params`, and `objects`.

This is important: the actual traceability metamodel is **not** the previously assumed `CPSToDeploymentTrace(cpsElement,deploymentElement)` schema.

Therefore the v001 trace record specification is invalid as a direct representation of this metamodel.

### 3. HostRule evidence

The frozen core repository's direct code search identifies `HostRule` in documentation, while the concrete transformation implementations are described as residing in the separate `org.eclipse.viatra.examples` repository. The core repository therefore does not, by itself, establish a concrete Java/Xtend HostRule implementation at the candidate revision.

### 4. Consequence

The current candidate fixture cannot yet be frozen from the core repository alone.

The following must not be asserted without the examples repository artifact:

- exact DeploymentHost EClass/attributes;
- exact trace object structure for the CPS transformation;
- exact HostRule implementation and activation semantics;
- exact target-model containment.

## Decision

**PARTIAL EVIDENCE — DEFERRED.**

This is a deliberate stop: the available evidence has exposed that the earlier fixture specification mixed the documented CPS-to-Deployment semantics with a different generic traceability metamodel.

No implementation or scientific execution is authorized.

## Next gate

Use the concrete **VIATRA examples repository** referenced by the frozen documentation to retrieve the CPS transformation artifacts at the corresponding immutable revision. Then rebuild the fixture specification from those artifacts, rather than continuing to infer target-side structure from documentation.
