# TGCV VIATRA V002 Example Environment Binding v001

## Status

FROZEN — SOURCE-VERIFIED EXAMPLE ENVIRONMENT.

## Purpose

Freeze the dependency environment of the concrete VIATRA tutorial artifact containing the canonical `hostRule` binding.

## Source

Repository: `eclipse-viatra/org.eclipse.viatra`

Revision: `ffa111dbb160c0bc55e89ea16430e97a38908662`

Source artifact:

`documentation/org.eclipse.viatra.documentation.help/src/main/asciidoc/tutorial/batch-transformations.adoc`

## Example bundles

The tutorial source declares the example environment with:

- `com.incquerylabs.course.cps.viatra.batch;bundle-version="0.1.0"`
- `org.eclipse.viatra.examples.cps.traceability;bundle-version="0.1.0"`
- `org.eclipse.viatra.query.runtime;bundle-version="1.2.0"`

These declarations are part of the concrete example context and are therefore binding evidence for the V002 implementation host.

## Version namespace rule

OSGi `bundle-version` values SHALL NOT be substituted with Maven project versions.

Where the source repository exposes a Maven project version separately from the OSGi bundle version, both SHALL be recorded independently.

## Host consequence

The V002 observer host SHALL reproduce the tutorial/example environment sufficiently to load and execute the concrete `hostRule` source binding.

The host SHALL NOT silently replace these example bundles with a different VIATRA generation merely because newer runtime artifacts are available.

## Packaging consequence

Because the source environment is Eclipse/OSGi based, the implementation host SHALL use a source-compatible Eclipse/OSGi/Tycho packaging model or another explicitly source-verified equivalent.

A plain Maven dependency-only host is insufficient evidence of source-equivalent packaging.

## Scientific boundary

This binding establishes implementation provenance only.

It does not establish runtime equivalence, scientific execution, or any scientific result.

## Next gate

Materialize the OSGi/Tycho host skeleton using this frozen example environment binding. Do not build or execute as part of materialization.
