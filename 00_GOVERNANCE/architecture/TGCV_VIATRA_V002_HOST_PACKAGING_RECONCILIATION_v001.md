# TGCV VIATRA V002 Host Packaging Reconciliation v001

## Status

SUPERSEDED — REQUIRED PACKAGING CHANGES IMPLEMENTED AND BUILD VERIFIED

This document records the pre-materialization packaging gap. The required Tycho host structure was subsequently implemented and verified by build run `37123064623`.

## Historical implementation model

The recovered VIATRA example is an Eclipse/OSGi plug-in project.

Historical facts at revision `eb68158a3d74581f69ccb8bc4f47673b12abdf85`:

- project packaging: `eclipse-plugin`
- Bundle-SymbolicName: `org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra`
- Bundle-Version: `2.1.0.qualifier`
- required execution environment: JavaSE-1.8
- build system: Tycho
- target definition packaging: `eclipse-target-definition`
- parent Tycho version: `1.0.0`
- Xtend compiler: `2.13.0`
- VIATRA compiler: `2.0.0-SNAPSHOT`

The target definition is the dependency-resolution boundary for the historical Eclipse platform. Tycho uses target platforms to select concrete OSGi artifacts for compilation, testing and assembly.

## Current TGCV host model

The current TGCV host POM is an ordinary Maven project:

- packaging defaults to `jar`
- Maven compiler release: 11
- only ordinary Maven dependency retained: CPS model 1.2.0
- VIATRA/traceability/runtime dependencies are represented as metadata only.

This model is therefore NOT packaging-equivalent to the historical project.

## Reconciliation

### 1. Packaging

Current:
`jar` / ordinary Maven.

Required:
`eclipse-plugin` with Tycho.

Reason:
the historical MANIFEST.MF is the authoritative OSGi dependency declaration and the historical POM explicitly declares `eclipse-plugin`.

### 2. Java level

Current:
Java 11.

Historical:
JavaSE-1.8.

Decision:
do NOT retain Java 11 in the equivalence host. The historical implementation boundary is Java 8.

### 3. Target platform

Current:
no actual Tycho target-platform configuration.

Required:
materialize the historical `eclipse-target-definition` project and configure the host to consume its target definition.

The target definition pins Eclipse Oxygen/EMF/Xtext/GEF/e(fx)clipse and related installable units. It must not be replaced by a modern target.

### 4. VIATRA p2 source

The historical parent POM also declares the VIATRA integration repository and VIATRA compiler version. Therefore the target definition alone is not sufficient to claim a complete dependency-resolution environment for the host.

The host packaging must preserve the historical distinction between:
- OSGi bundle versions in MANIFEST.MF;
- Maven project/compiler versions;
- p2 target-platform contents.

### 5. Source identity

The host must not rename the historical implementation bundle if it is presented as the historical implementation package.

The TGCV observer/adapter may be a separate bundle, but that is a distinct TGCV component and must not be represented as the original VIATRA example bundle.

## Required materialization delta

Before any build:

1. convert the host from ordinary Maven packaging to a Tycho reactor/module structure;
2. materialize the historical target-definition project;
3. add the target-platform configuration referencing that target artifact;
4. preserve the historical Java 8 execution environment for the compatibility host;
5. represent OSGi dependencies through MANIFEST.MF, not ordinary Maven dependencies;
6. keep the TGCV observer as a separate component from the recovered historical transformation bundle;
7. preserve the frozen source revision and all provenance bindings.

## Explicit non-actions

No build was performed.

No dependency resolution was performed.

No runtime was launched.

No scientific execution or equivalence claim was made.

## Gate boundary

This reconciliation is architectural/package-level only. The next step is materialization of the Tycho host structure from the frozen historical packaging, followed by a static packaging audit. Build remains a separate authorized action.
