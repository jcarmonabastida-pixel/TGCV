# TGCV VIATRA V002 Observer Host Build Construction Review 001

Status: CONSTRUCTION REVIEW PASS — BUILD NOT EXECUTED

Date: 2026-10-03

## Purpose

This review closes the construction contract for the VIATRA V002 observer-host package before another Tycho build is launched. The objective is to prevent reactive build/fix iteration by validating the complete package architecture statically first.

## Canonical inputs

- TGCV repository: `jcarmonabastida-pixel/TGCV`
- Branch: `main`
- Tycho: `1.0.0`
- Java execution environment: `JavaSE-1.8`
- Historical VIATRA examples source revision: `eb68158a3d74581f69ccb8bc4f47673b12abdf85`
- Historical target-definition byte/blob SHA: `7481dee30f1ae07d7dd9212d7891dc336f1e96ae`
- Target file: `target-definition/tgcv-viatra-v002-target.target`

## Construction graph

```
viatra-v002-observer-host
├── target-definition
│   └── tgcv-viatra-v002-target.target
├── cps-models
│   ├── org.eclipse.viatra.examples.cps.model
│   ├── org.eclipse.viatra.examples.cps.deployment
│   └── org.eclipse.viatra.examples.cps.traceability
└── observer
    └── org.tgcv.viatra.v002.observer
```

The historical CPS bundles are materialized at workflow time from the pinned external revision. Their TGCV Maven POMs remain canonical in the reactor.

## Construction contracts

| Layer | Contract | Status |
|---|---|---|
| Maven root | POM reactor only; no target-platform self-resolution | PASS |
| Tycho extension | Root provides Tycho 1.0.0 extension | PASS |
| Target definition | Dedicated `eclipse-target-definition` module | PASS |
| Target filename | `<artifactId>.target` for Tycho 1.x | PASS |
| Target immutability | Historical target content unchanged | PASS |
| Target consumption | CPS model and observer modules explicitly consume target GAV | PASS |
| Target-module isolation | Target-definition module does not inherit target-platform configuration | PASS |
| CPS reactor | Three historical bundles have explicit reactor POMs | PASS |
| CPS source | Workflow materializes exact pinned revision | PASS |
| OSGi observer | Observer MANIFEST declares concrete model dependencies | PASS |
| OSGi CPS closure | Historical manifests provide required EMF/runtime dependencies | PASS |
| Java | JavaSE-1.8 and workflow Java 8 | PASS |
| Static preflight | Checks structure, provenance, dependency closure and target immutability | PASS |
| Runtime/build execution | Not part of this review | NOT EXECUTED |

## Key architectural correction

The target-platform configuration was removed from the root reactor POM and placed explicitly in the two consuming build branches:

- `cps-models/pom.xml`
- `observer/pom.xml`

The target-definition module therefore provides the target artifact but does not inherit configuration that asks the reactor to consume that same target artifact.

The target reference uses the complete GAV:

```
org.tgcv:tgcv-viatra-v002-target:${project.version}
```

and no `relativePath` is used in the target-platform artifact reference.

This separation follows the Tycho target-platform model in which a target definition is consumed by downstream projects as a target artifact. The Tycho documentation explicitly supports target definitions referenced by GAV and distinguishes them from local-file target configuration.

## Build lifecycle gates

The next controlled workflow, once explicitly authorized, must execute in this order:

1. Checkout canonical `main`.
2. Provision Java 8.
3. Materialize the three pinned historical CPS bundles.
4. Run `build-readiness-preflight.sh`.
5. Run `mvn -B -ntp -DskipTests validate` as the dependency-resolution/build-model gate.
6. Only if gate 5 passes, run `mvn -B -ntp clean verify`.

A failure at gate 5 is classified as a construction/dependency-resolution failure. It must be diagnosed from that run before any rerun. The full reactor must not be repeatedly rebuilt merely to discover the next structural defect.

## Scientific firewall

This construction review contains no runtime execution, transformation outcome, accessibility result, value/utility/reward variable, or scientific performance measure. A successful build is a packaging/reproducibility result only.

## Decision

The package construction contract is now closed for the current configuration. No build has been launched as part of this review.

The next action is one controlled build workflow run. If it fails, the failure must be classified against the construction matrix above before any correction or rerun.
