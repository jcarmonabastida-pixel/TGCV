# TGCV VIATRA V002 Build Installation Path Review 001

## Status

**Review complete. Workflow modification not yet applied.**

## Scope

This review reconstructs the build path required by the exact pinned revisions used by the TGCV VIATRA V002 runtime-equivalence preflight:

- VIATRA core: `6f7d2d7860ed901c33029700387d3535bd2553f1`
- VIATRA examples: `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`

The purpose is to replace iterative dependency patching with the repository-defined Maven/Tycho reactor path.

## Evidence

### 1. VIATRA core CONTRIBUTING.md

At the pinned core revision, the official build instructions define two Maven/Tycho passes:

1. Core pass:
   `mvn clean install -f releng/org.eclipse.viatra.parent.core/pom.xml`
2. Remaining projects:
   `mvn clean install -f releng/org.eclipse.viatra.parent.all/pom.xml`

The core parent explicitly includes the VIATRA Maven plugin in its reactor.

Therefore the current TGCV workflow's targeted Maven-plugin installation is technically sufficient for the compiler plugin itself, but is not the canonical complete core build path.

### 2. Examples CPS reactor

At the pinned examples revision, `cps/pom.xml` is the authoritative CPS reactor parent.

It declares, among others:

- `releng/org.eclipse.viatra.examples.cps.target`
- `releng/org.eclipse.viatra.examples.cps.domain.parent`
- CPS transformations
- CPS tests

The domain parent explicitly declares:

- `org.eclipse.viatra.examples.cps.deployment`
- `org.eclipse.viatra.examples.cps.model`
- `org.eclipse.viatra.examples.cps.traceability`
- their edit/editor bundles
- the metamodel feature

### 3. Direct dependency of the runtime target

The pinned `incr.expl` bundle manifest declares:

`org.eclipse.viatra.examples.cps.traceability;bundle-version="[2.9.0,3.0.0)"`

The observed failed build confirms that Tycho could not resolve this OSGi bundle.

### 4. Why the previous partial build failed

The workflow used:

`mvn -B -f cps/pom.xml -pl transformations/org.eclipse.viatra.examples.cps.xform.m2m.incr.expl,tests/org.eclipse.viatra.examples.cps.xform.m2m.tests -am test`

This does **not** mean "build all modules required by the CPS reactor". Maven's `-am` follows the Maven dependency graph; merely being another module in the parent reactor does not make the traceability bundle a reactor dependency of `incr.expl`.

The domain bundles were therefore not part of the same Tycho reactor context.

Installing the domain parent separately also does not make its OSGi bundles available to Tycho target-platform resolution in the same way as a complete CPS reactor build.

## Determination

The iterative sequence of:

- target install
- domain-parent install
- selected transformation `-pl`
- selected tests `-pl`

is **not the canonical or reliable build path for this CPS example**.

The correct next build experiment is to use the complete pinned CPS reactor:

`mvn -B -f cps/pom.xml clean install -DskipTests=false`

with the already established Java/toolchain and isolated Maven repository controls.

This should allow the CPS domain bundles and transformation bundles to participate in the same Tycho reactor rather than attempting to satisfy their OSGi dependencies through Maven-local installation alone.

## Workflow implication

Before the next execution, replace the current selected-module CPS build with the complete CPS reactor build.

Do not change:

- pinned revisions
- fixture
- runtime target
- HostMapping artifact pin
- Java versions
- scientific execution gates
- adapter

Do not add further ad-hoc dependency installation steps unless the complete CPS reactor itself demonstrates a reproducible dependency failure.

## Scientific boundary

This is an engineering/build-path correction only. No scientific execution is authorized or implied.

## Source revisions

- Core: `6f7d2d7860ed901c33029700387d3535bd2553f1`
- Examples: `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`
