# TGCV VIATRA V002 Build Installation Path Review 002

## Purpose

Determine the exact Maven/Tycho build path required to make the pinned VIATRA CPS runtime `incr.expl` executable for the V002 runtime-equivalence preflight, without building unrelated CPS transformations or tests.

## Immutable inputs

- VIATRA core: `6f7d2d7860ed901c33029700387d3535bd2553f1`
- VIATRA examples: `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`
- CPS root: `cps/pom.xml`
- Runtime target: `cps/releng/org.eclipse.viatra.examples.cps.target`
- Runtime target artifact: `org.eclipse.viatra.examples.cps.target`
- Runtime under test: `transformations/org.eclipse.viatra.examples.cps.xform.m2m.incr.expl`

## Evidence reviewed

### 1. CPS root reactor

`cps/pom.xml` declares all CPS modules, including the target, domain parent, M2M utility, `incr.expl`, multiple unrelated transformation variants, and the broad test suite.

Therefore a complete CPS reactor is broader than the runtime under test and is not required.

### 2. Runtime dependency closure

`incr.expl/META-INF/MANIFEST.MF` requires:

- `org.eclipse.viatra.examples.cps.traceability`
- `org.eclipse.viatra.examples.cps.deployment`
- `org.eclipse.viatra.examples.cps.model`
- `org.eclipse.viatra.examples.cps.xform.m2m.util`
- VIATRA query runtime
- VIATRA transformation EVM

The utility bundle additionally requires CPS model, deployment and traceability. Traceability requires CPS model and deployment.

Thus the concrete CPS bundle closure required by `incr.expl` is:

- deployment
- model
- traceability
- M2M utility
- incr.expl

with external Eclipse/VIATRA dependencies supplied by the target platform/core installation.

### 3. Why the separate domain-parent install was insufficient

The domain parent declares the domain bundles as Maven reactor modules, including traceability.

However, installing the domain parent in a separate Maven invocation does not make an Eclipse bundle automatically available to a later Tycho OSGi target-platform resolution merely because a Maven artifact exists in `~/.m2`.

The failed run provides direct confirmation: while resolving `incr.expl`, Tycho reported that `org.eclipse.viatra.examples.cps.traceability [2.9.0,3.0.0)` could not be found.

Therefore the previous sequence

1. install target
2. install domain parent separately
3. build incr.expl later

does not close the OSGi dependency boundary.

### 4. Why the CPS test bundle must not be included

`org.eclipse.viatra.examples.cps.xform.m2m.tests` requires numerous unrelated transformations, including `batch.viatra`, `incr.viatra`, `incr.qrt`, `incr.aggr`, `incr.puregratra`, and others.

Including this test bundle would therefore reintroduce unrelated runtime dependencies and the previously observed batch-transformation build problem.

The V002 preflight adapter is the dedicated test harness. The upstream CPS transformation test suite is not part of the runtime-equivalence target.

## Closed build path

The CPS build must use one Tycho reactor invocation from `cps/pom.xml` that explicitly includes:

1. `releng/org.eclipse.viatra.examples.cps.target`
2. `domains/org.eclipse.viatra.examples.cps.deployment`
3. `domains/org.eclipse.viatra.examples.cps.model`
4. `domains/org.eclipse.viatra.examples.cps.traceability`
5. `transformations/org.eclipse.viatra.examples.cps.xform.m2m.util`
6. `transformations/org.eclipse.viatra.examples.cps.xform.m2m.incr.expl`

Maven dependency expansion may then add only dependencies required by this selected closure.

The build must not select:

- batch.simple
- batch.eiq
- batch.optimized
- batch.viatra
- incr.viatra
- incr.qrt
- incr.aggr
- incr.puregratra
- the broad CPS transformation test bundle
- unrelated application/update-site modules

## Workflow implication

The current three-stage CPS sequence is architecturally incorrect:

1. install target
2. install domain parent separately
3. build `incr.expl` plus the broad tests

The next workflow revision should replace that sequence with the single selected CPS reactor described above.

Before executing the workflow, the reactor-selection command should be checked for the expected reactor order. The build log must demonstrate that the selected reactor contains the required runtime closure and does not pull the excluded transformation/test modules.

No scientific execution is implied by this build review.

## Conclusion

**BUILD PATH CLOSED FOR NEXT WORKFLOW REVISION.**

The latest failure is explained by a concrete Tycho reactor/OSGi dependency boundary. It is not a Maven-download problem and does not justify another exploratory build variant.

The next change should be a single workflow correction implementing this closed reactor path, followed by one controlled preflight execution.
