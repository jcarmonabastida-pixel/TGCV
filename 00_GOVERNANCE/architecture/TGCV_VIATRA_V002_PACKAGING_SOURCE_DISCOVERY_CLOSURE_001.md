# TGCV VIATRA V002 Packaging Source Discovery Closure 001

## Status

SUPERSEDED — PRE-CANONICAL PACKAGING DISCOVERY

The later source recovery at `eb68158a...` established the materialized historical packaging used by the current V002 Observer Host.

## Scope

The discovery searched the canonical VIATRA source revision:

`eclipse-viatra/org.eclipse.viatra@ffa111dbb160c0bc55e89ea16430e97a38908662`

for the concrete tutorial dependency:

`com.incquerylabs.course.cps.viatra.batch`

including source, `MANIFEST.MF`, feature metadata, and implementation references.

## Finding

The bundle is referenced by the tutorial documentation as an example dependency, but its materializable bundle source and OSGi packaging metadata are not present in the pinned VIATRA repository revision.

Therefore TGCV does not currently possess source evidence sufficient to reconstruct that bundle's exact OSGi/Tycho packaging.

## Consequence

The bundle SHALL be treated as an external provenance dependency of the tutorial example, not as a locally reconstructable TGCV implementation dependency.

TGCV SHALL NOT:

- invent a `MANIFEST.MF`;
- infer `Require-Bundle` entries;
- substitute a different VIATRA generation;
- recreate the bundle under a new identity;
- claim source-equivalent packaging without the original artifact/source.

## V002 implementation boundary

The frozen V002 source binding remains valid at the documentation level:

`hostRule` → V002 semantic transition.

However, a runtime-equivalent host cannot yet be materialized solely from the canonical VIATRA repository.

## Scientific boundary

No build, runtime execution, runtime-equivalence claim, or scientific execution was performed.

## Next gate

Resolve the external provenance dependency for `com.incquerylabs.course.cps.viatra.batch` by identifying its original source/release artifact with immutable provenance.

Only after that resolution may the OSGi/Tycho host be materialized.
