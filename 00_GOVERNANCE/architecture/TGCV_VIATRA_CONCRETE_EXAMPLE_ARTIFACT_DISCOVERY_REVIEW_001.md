# TGCV VIATRA Concrete Example Artifact Discovery Review

**Status:** DISCOVERY COMPLETE — fixture v001 requires revision before freeze  
**Date:** 2026-10-02  
**VIATRA revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`

## 1. Evidence located

The frozen VIATRA repository contains a concrete CPS model instance:

`query/tests/org.eclipse.viatra.query.runtime.cps.tests/models/instances/demo.cyberphysicalsystem`

Its root is `cps:CyberPhysicalSystem`, with concrete `hostTypes` and `instances`. For example, the model contains HostInstance identifiers and nodeIp attributes such as:

`simple.cps.host.FirstHostClass0.inst0`

and

`simple.cps.host.FirstHostClass0.inst0`

respectively.

This establishes that semantic identifiers and node IP values are real CPS model attributes in the frozen repository; they need not be invented as TGCV metadata.

## 2. Transformation specification evidence

The frozen documentation states that the CPS-to-Deployment transformation:

- maps all host instances to deployment hosts;
- copies the host instance IP address to the deployment model;
- creates a 1-to-1 trace between host instance and deployment host.

The repository also documents multiple concrete transformation implementations, including event-driven/incremental variants and explicit traceability variants.

## 3. Consequence for fixture v001

The previous fixture specification introduced `deploymentHost:DH001` and `trace:T001` as if these were concrete metamodel identifiers. That was too strong.

The corrected policy is:

- `host:H001` is a TGCV semantic key derived from the actual CPS `identifier`;
- the deployment-host and trace semantic keys must be derived from actual post-state model structure or explicitly assigned by the fixture builder;
- they must not be represented as pre-existing VIATRA model attributes unless the concrete target metamodel proves such attributes exist.

## 4. Important discovery: existing model is not minimal

The discovered `demo.cyberphysicalsystem` contains many hosts, applications, state machines and requirements. It is therefore unsuitable as the first minimal observation fixture without reduction.

It is nevertheless valuable as a source artifact proving the real CPS syntax and attribute conventions.

## 5. Concrete source boundary

The source artifact is therefore:

- repository: `eclipse-viatra/org.eclipse.viatra`;
- revision: `ffa111dbb160c0bc55e89ea16430e97a38908662`;
- source model: `query/tests/org.eclipse.viatra.query.runtime.cps.tests/models/instances/demo.cyberphysicalsystem`.

A future minimal fixture should be derived from the repository's actual CPS metamodel and transformation implementation, not from documentation-only assumptions.

## 6. What remains unresolved

The discovery review did not yet establish, from a concrete target-model artifact:

1. the exact DeploymentHost identifier/key semantics;
2. the exact traceability EClass/attribute names and serialization;
3. the exact event-driven HostRule implementation path at the frozen revision;
4. whether the minimal one-host fixture can be represented without additional containment/model-root requirements.

These are implementation-level facts and must be established before fixture freeze.

## 7. Decision

**DISCOVERY COMPLETE — FIXTURE REVISION REQUIRED.**

The review successfully located a concrete CPS instance and confirmed the real source-side fields, but the target-side canonical representation remains insufficiently evidenced.

No fixture artifact is frozen. No instrumentation or scientific execution is authorized.

## Next gate

Locate the concrete CPS metamodel and target Deployment/Traceability metamodel definitions plus the exact HostRule implementation at the frozen revision. Then issue **Minimal Fixture Specification v002**, removing any field that is not directly supported by the actual metamodel/code.
