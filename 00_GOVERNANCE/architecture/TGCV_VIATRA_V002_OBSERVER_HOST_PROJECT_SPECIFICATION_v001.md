# TGCV VIATRA V002 Observer Host Project Specification v001

## Status

SUPERSEDED — HOST PROJECT MATERIALIZED AND BUILD VERIFIED

This specification records the pre-materialization design state. The canonical host is now materialized and its packaging/build chain was verified by run `37123064623`.

## Purpose

Define the minimum reproducible host project required to materialize the V002 serial runtime observation implementation.

This is implementation infrastructure only. It is not a scientific experiment and does not authorize runtime execution.

## Source binding

The host project SHALL bind to:

- repository: `eclipse-viatra/org.eclipse.viatra`;
- source revision: `ffa111dbb160c0bc55e89ea16430e97a38908662`;
- concrete transformation: CPS-to-Deployment `hostRule`;
- rule precondition: `HostInstance.instance`;
- canonical V002 fixture set and its SHA-256 manifest.

## Project boundary

The host project SHALL contain four logically separated components:

1. source/example adapter;
2. V002 fixture loader;
3. serial observer;
4. deterministic observation serializer.

The observer SHALL remain separate from transformation semantics and SHALL NOT modify the transformation rule.

## Required dependencies

The project specification SHALL resolve the exact VIATRA/EMF dependencies required by the pinned source revision and the concrete example, including the CPS, Deployment and Traceability metamodel/runtime artifacts used by the source example.

Dependency versions SHALL be pinned rather than resolved from floating/latest ranges.

The project SHALL preserve the previously established VIATRA PF-09 dependency/runtime pins where those dependencies are reused.

## Fixture loading

The harness SHALL load exactly the canonical V002 INITIAL inputs for an observation run and SHALL make the EXPECTED artifacts available for independent post-observation comparison.

It SHALL NOT regenerate or rewrite canonical fixture files.

The five canonical artifacts remain external immutable inputs:

- CPS;
- Deployment INITIAL;
- Deployment EXPECTED;
- Traceability INITIAL;
- Traceability EXPECTED.

## Transformation entry

The harness SHALL expose one deterministic entry point for the selected `hostRule` activation.

The minimal observation SHALL be restricted to the V002 HostMapping activation corresponding to the canonical `HostInstance`.

The harness SHALL NOT execute unrelated transformation rules.

## Observer placement

The observer SHALL be attached at the transformation lifecycle boundary needed to capture:

- PRE state before the selected `hostRule` action;
- activation identity;
- POST state after the selected `hostRule` action.

The observer SHALL emit the lifecycle:

`TRANSFORMATION_BEGIN → hostRule activation → TRANSFORMATION_END`.

## Determinism

The host project SHALL operate serially.

No parallel execution, batching, pooling, random scheduling, or aggregation is permitted in the minimal harness.

The canonical observation record SHALL be reproducible for identical canonical inputs and pinned implementation/source revisions.

## Provenance

The harness SHALL expose provenance for:

- source repository and commit;
- fixture revision;
- fixture SHA-256 manifest;
- host-project revision;
- observer/instrumentation revision;
- runtime/toolchain identity.

Git blob identifiers SHALL NOT substitute for fixture-byte SHA-256 values.

## Scientific firewall

The host project SHALL contain no computation or storage of:

- U_t;
- T_acc;
- accessibility labels;
- future assignment;
- utility;
- reward;
- value;
- scientific performance metrics.

## Build and execution boundary

Creating or reviewing this specification does not require a build.

Materialization of the host project is an implementation step.

Any runtime execution requires a separate gate and explicit authorization.

Scientific execution SHALL remain blocked until all applicable implementation and equivalence gates pass.

## Acceptance conditions

The host project is ready for implementation materialization when:

1. all source/dependency revisions are pinned;
2. all required metamodel/runtime artifacts are identified;
3. fixture loading is immutable;
4. the selected `hostRule` activation is uniquely scoped;
5. PRE/POST observation boundaries are implementable;
6. serial determinism is enforceable;
7. provenance is complete;
8. the scientific firewall is preserved.

## Next gate

The next gate is implementation materialization and static review of this host project. It is not runtime execution and it does not require a scientific build/run.
