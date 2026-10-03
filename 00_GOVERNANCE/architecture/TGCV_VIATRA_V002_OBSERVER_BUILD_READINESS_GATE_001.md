# TGCV VIATRA V002 Observer Host Build Readiness Gate 001

Status: READY FOR RE-RUN

## Scope

This gate was introduced after build run `37120128598` stopped before Maven/Tycho because the materialization verification step failed.

The failure was traced to the TGCV materializer itself, not to the historical VIATRA CPS bundle structure.

## Root cause of run 37120128598

`materialize-historical-cps-models.sh` computed its destination root one directory too high:

- script location: `05_IMPLEMENTATION/viatra-v002-observer-host/`
- previous `HOST_ROOT=dirname/..`: `05_IMPLEMENTATION/`
- expected destination: `05_IMPLEMENTATION/viatra-v002-observer-host/cps-models/`

Therefore the materializer populated a different `cps-models/` location while the verification step inspected the reactor location.

The historical source at revision `eb68158a3d74581f69ccb8bc4f47673b12abdf85` was independently checked and does contain `model/` and `src/` directories for all three bundles.

## Current safeguards

Before the full build, the workflow now performs:

1. Java 8 environment selection.
2. Exact checkout of the TGCV `main` revision.
3. Exact historical VIATRA examples revision check in the materializer.
4. Materialization of all three required bundles.
5. Per-bundle checks for `pom.xml`, `META-INF/MANIFEST.MF`, `build.properties`, `plugin.xml`, `plugin.properties`, non-empty `model/`, non-empty `src/`, expected bundle symbolic name, historical bundle version `2.1.0.qualifier`, JavaSE-1.8, model/source build properties, and TGCV reactor parent.
6. Reactor module wiring checks.
7. Observer MANIFEST dependency closure checks.
8. Exact Git blob SHA check for the preserved historical target definition: `7481dee30f1ae07d7dd9212d7891dc336f1e96ae`.
9. Maven/Tycho `validate` as a dependency-resolution gate.
10. Only if all preceding gates pass, `mvn clean verify`.

Tycho's effective target platform includes other artifacts from the same reactor, so the three CPS bundles can satisfy the observer's OSGi dependencies without being inserted into the preserved historical target definition. citeturn0search0

## Build boundary

This gate does not execute the V002 runtime observer or any scientific execution. It only establishes build/readiness and dependency resolution.

The full build remains the next gate after this preflight passes.
