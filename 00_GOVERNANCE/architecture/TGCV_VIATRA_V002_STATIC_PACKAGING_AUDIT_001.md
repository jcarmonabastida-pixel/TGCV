# TGCV VIATRA V002 Static Packaging Audit 001

## Status

SUPERSEDED — PRE-BUILD STATIC PACKAGING AUDIT

This audit records the earlier blocked state before target consumption was materialized. The current host packaging was subsequently reconciled and verified by build run `37123064623`.

## Findings

### PASS — Reactor structure

The host is a Maven reactor with:
- target-definition module;
- observer module.

The observer is declared with `eclipse-plugin` packaging.

### PASS — Target definition artifact

The target-definition module uses `eclipse-target-definition` packaging and contains the frozen historical target definition.

The target definition is the correct mechanism for supplying a controlled Tycho target platform; Tycho documentation explicitly describes target-definition modules and their use through target-platform-configuration. citeturn0search0turn0search1

### PASS — Historical target preservation

The materialized target file retains the historical source SHA:

`7481dee30f1ae07d7dd9212d7891dc336f1e96ae`

No target-platform substitution was introduced.

### PASS — Observer identity separation

Observer Bundle-SymbolicName:

`org.tgcv.viatra.v002.observer`

It does not reuse:

`org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra`

### PASS — Java boundary

Observer MANIFEST declares JavaSE-1.8, consistent with the historical compatibility boundary.

### BLOCK — Target consumption not yet configured

The reactor currently contains the target-definition artifact, but the parent POM does not yet configure `target-platform-configuration` to consume that artifact.

Therefore the current structure must NOT be built or described as dependency-resolvable.

Tycho's documented target-definition model requires the target artifact to be referenced through target-platform-configuration before it becomes the project's target platform. citeturn0search0

### BLOCK — Historical target environment is not yet fully reconciled

The recovered historical parent also declared the VIATRA integration p2 repository and compiler properties. These have not yet been transferred into the TGCV reactor because doing so would be a dependency-resolution change, not a static packaging operation.

## Decision

Do not build.

Do not run dependency resolution.

Do not add broad p2 repositories as a shortcut.

The next materialization step is narrowly defined: add the target-platform-configuration reference to the frozen target-definition artifact, then perform a static re-audit. Runtime and scientific execution remain outside this gate.
