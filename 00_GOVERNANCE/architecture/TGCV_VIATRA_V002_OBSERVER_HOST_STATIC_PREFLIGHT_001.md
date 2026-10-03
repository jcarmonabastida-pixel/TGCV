# TGCV VIATRA V002 Observer Host Static Preflight 001

## Status

SUPERSEDED — HISTORICAL PREFLIGHT; CURRENT BUILD CHAIN VERIFIED

This document records an earlier blocked state and is retained for provenance. Its source revision and dependency-coordinate conclusions are not the current canonical state.

## Scope

Static review of the materialized host skeleton under:

`05_IMPLEMENTATION/viatra-v002-observer-host/`

No build, dependency resolution, transformation execution, or scientific execution was performed.

## Checks

### Host structure

PASS.

The project contains:

- host `pom.xml`;
- host README;
- non-executing Java entry boundary.

### Source binding

PASS.

The host records the frozen VIATRA revision:

`ffa111dbb160c0bc55e89ea16430e97a38908662`

and the concrete `hostRule` binding.

### Execution firewall

PASS.

The entry point explicitly refuses runtime execution and no workflow was launched.

### Canonical fixture boundary

PASS.

The host documentation declares canonical fixtures immutable and does not regenerate them.

### Dependency binding

BLOCKED.

The current `pom.xml` contains dependency coordinates/version values that have not been verified against the pinned VIATRA source repository. The host README explicitly states that these values are not build-verified.

Therefore the project is not yet a reproducible implementation host.

## Decision

Do not build or execute this host project.

The dependency coordinates MUST first be derived directly from the pinned VIATRA source revision `ffa111db...` and its actual project metadata. No version may be retained merely because it appears plausible or was inferred from a prior environment.

## Next gate

Source-level dependency/bundle reconciliation against `ffa111db...`.

This is a provenance/configuration task, not scientific execution and does not itself require a build.
