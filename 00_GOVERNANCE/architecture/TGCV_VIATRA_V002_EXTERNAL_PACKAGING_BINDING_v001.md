# TGCV VIATRA V002 External Packaging Binding v001

## Status

SOURCE-VERIFIED PACKAGING BINDING.

## Source

Repository: `eclipse-viatra/org.eclipse.viatra.examples`

Revision:

`eb68158a3d74581f69ccb8bc4f47673b12abdf85`

Project:

`cps/transformations/org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra`

## MANIFEST.MF

Path:

`META-INF/MANIFEST.MF`

Source SHA:

`72569d0515199a55533d24f07de665a300a2e4c6`

Key packaging facts:

- Bundle-SymbolicName: `org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra`
- Bundle-Version: `2.1.0.qualifier`
- Bundle-RequiredExecutionEnvironment: `JavaSE-1.8`
- Packaging is an Eclipse/OSGi plug-in.
- Required bundles include CPS deployment/model/traceability, VIATRA query runtime, VIATRA transformation EVM/runtime/debug, Xtend, and the CPS transformation utility bundle.

## pom.xml

Path:

`cps/transformations/org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra/pom.xml`

Source SHA:

`c44efe454b8daf9f1fb37f7bd3463b1ded61b1e3`

Key packaging facts:

- parent: `org.eclipse.viatra.examples.cps.parent`
- parent version: `2.1.0-SNAPSHOT`
- artifactId: `org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra`
- packaging: `eclipse-plugin`
- VIATRA Maven plugin generates sources using the deployment, CPS and traceability metamodel package classes.
- Xtend Maven plugin compiles the Xtend implementation.

## Consequence

The previously unresolved packaging boundary is now source-verified.

The V002 host SHALL use this historical Eclipse/OSGi/Tycho-compatible project as the implementation packaging reference.

TGCV SHALL preserve the original source revision and SHALL NOT repackage the bundle under a different symbolic name while claiming source-equivalent provenance.

## Scientific boundary

No build, runtime execution, runtime-equivalence claim, or scientific execution was performed.

## Next gate

Materialize the host against this exact historical project/package boundary, preserving source provenance and the original OSGi identity.
