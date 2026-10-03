# TGCV VIATRA V002 Dependency / Bundle Binding v001

## Status

SOURCE-VERIFIED BINDING.

## Source revision

Repository: `eclipse-viatra/org.eclipse.viatra`

Revision: `ffa111dbb160c0bc55e89ea16430e97a38908662`

## Verified coordinates

The pinned tutorial source explicitly identifies these runtime/example bundles:

- `org.eclipse.viatra.examples.cps.traceability` — bundle-version `0.1.0`
- `org.eclipse.viatra.query.runtime` — bundle-version `1.2.0`

The VIATRA Maven documentation at the same revision explicitly identifies:

- groupId `org.eclipse.viatra.examples.cps`
- artifactId `org.eclipse.viatra.examples.cps.model`
- version `1.2.0`

## Important packaging boundary

The source evidence distinguishes Maven coordinates from Eclipse/OSGi bundle coordinates.

Therefore the current TGCV host `pom.xml` MUST NOT be treated as build-verified merely because these version strings are present.

In particular, `org.eclipse.viatra.query.runtime` and `org.eclipse.viatra.examples.cps.traceability` are source-verified as Eclipse/OSGi bundles in the tutorial, not thereby proven to be ordinary Maven JAR dependencies consumable by a plain Maven project.

## Consequence for host architecture

The host project requires an Eclipse/OSGi/Tycho-compatible dependency boundary, or another source-verified mechanism that consumes the exact bundles.

A plain Maven dependency declaration SHALL NOT be considered sufficient evidence of reproducibility.

## Evidence

The source tutorial at the pinned revision declares the traceability and query-runtime bundle versions as:

`org.eclipse.viatra.examples.cps.traceability;bundle-version="0.1.0"`

`org.eclipse.viatra.query.runtime;bundle-version="1.2.0"`

The source Maven documentation declares the CPS model dependency as version `1.2.0`.

## Boundary

This document is dependency/provenance reconciliation only.

It does not authorize a build or runtime execution.

The next gate is correction of the host project packaging model so that it matches the source-verified Eclipse/OSGi dependency boundary.
