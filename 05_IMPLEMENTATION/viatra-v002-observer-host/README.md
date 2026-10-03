# TGCV VIATRA V002 Observer Host

Implementation host skeleton for the canonical V002 serial runtime observation path.

## Frozen bindings

- VIATRA source repository: `eclipse-viatra/org.eclipse.viatra`
- VIATRA source revision: `ffa111dbb160c0bc55e89ea16430e97a38908662`
- concrete rule: `hostRule`
- TGCV source binding: `TGCV_VIATRA_V002_IMPLEMENTATION_SOURCE_BINDING_v001.md`
- TGCV observer specification: `TGCV_VIATRA_V002_SERIAL_RUNTIME_OBSERVATION_IMPLEMENTATION_SPECIFICATION_v001.md`
- TGCV host-project specification: `TGCV_VIATRA_V002_OBSERVER_HOST_PROJECT_SPECIFICATION_v001.md`

## Scope

This project is intentionally a host skeleton. It provides pinned dependency declarations and the package boundary for:

1. source/example adapter;
2. immutable V002 fixture loader;
3. serial observer;
4. deterministic observation serializer.

The observer implementation itself is not yet authorized.

## Execution boundary

No transformation execution is performed by this project at materialization time.

Canonical fixtures are inputs only and MUST NOT be regenerated or modified.

Scientific variables and metrics are outside this project boundary.

## Dependency note

The dependency coordinates and versions are derived from the pinned VIATRA batch-transformation tutorial at `ffa111db`. They have not been claimed as build-verified by this materialization step.
