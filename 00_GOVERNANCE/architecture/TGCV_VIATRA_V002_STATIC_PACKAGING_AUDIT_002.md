# TGCV VIATRA V002 Static Packaging Audit 002

## Status

STATIC PACKAGING COHERENCE PASS.

## Verified

The canonical `main` branch contains a coherent Tycho reactor:

- root reactor: `org.tgcv:viatra-v002-observer-host:0.1.0-SNAPSHOT`
- target definition: `org.tgcv:tgcv-viatra-v002-target:0.1.0-SNAPSHOT`
- observer: `org.tgcv:org.tgcv.viatra.v002.observer:0.1.0-SNAPSHOT`
- root packaging: `pom`
- target packaging: `eclipse-target-definition`
- observer packaging: `eclipse-plugin`
- Tycho version: `1.0.0`
- Java boundary: `1.8`

The root reactor explicitly references the target-definition artifact through Tycho `target-platform-configuration`.

The observer retains its independent OSGi identity:

`org.tgcv.viatra.v002.observer`

The historical VIATRA bundle identity is not reused.

## Provenance check

The historical target definition remains unchanged at source SHA:

`7481dee30f1ae07d7dd9212d7891dc336f1e96ae`

Observer MANIFEST SHA on TGCV main:

`987166dcc10193c81fa5f3536231531351df3318`

## Decision

The static packaging layer is now internally coherent and ready for a separate build gate.

This audit does NOT establish:
- dependency resolution;
- successful Tycho build;
- runtime equivalence;
- transformation execution;
- observer correctness;
- scientific execution.

Those remain separate gates.

## Next gate

Before any build, perform a source/package dependency reconciliation of the observer MANIFEST against the recovered historical implementation and observer specification. Add only dependencies that are explicitly required by the observer implementation; do not add broad historical dependencies merely to make the build pass.
