# TGCV VIATRA V002 External Target Platform Binding v001

## Status

SOURCE-VERIFIED TARGET PLATFORM BINDING.

## Source

Repository: `eclipse-viatra/org.eclipse.viatra.examples`

Revision:

`eb68158a3d74581f69ccb8bc4f47673b12abdf85`

Target project:

`cps/releng/org.eclipse.viatra.examples.cps.target`

## Target definition

Path:

`org.eclipse.viatra.examples.cps.target.target`

Source SHA:

`7481dee30f1ae07d7dd9212d7891dc336f1e96ae`

The historical target definition is a fixed PDE target generated from a Demo Targlet Platform (sequenceNumber 20).

It pins, among others:

- Eclipse/EMF SDK 2.13.0
- Eclipse platform SDK 4.7.1 (Oxygen)
- Xtext SDK 2.13.0
- e(fx)clipse runtime 3.1.0
- GEF 5.0.0/5.0.1 components
- Eclipse Collections 9.2.0
- Eclipse license feature 1.0.1

The target definition also pins the exact p2 repository locations and installable-unit versions.

## Target POM

Path:

`cps/releng/org.eclipse.viatra.examples.cps.target/pom.xml`

Source SHA:

`91a9f6a00ec37bc735e15b787c27dc00259052b3`

Facts:

- parent: `org.eclipse.viatra.examples.cps.parent`
- version: `2.1.0-SNAPSHOT`
- artifactId: `org.eclipse.viatra.examples.cps.target`
- packaging: `eclipse-target-definition`

## Consequence

The historical implementation environment is now sufficiently bound at the target-platform level to distinguish the original Eclipse/OSGi build environment from the later TGCV host skeleton.

TGCV MUST NOT silently substitute a modern Eclipse/VIATRA target platform while claiming historical implementation equivalence.

## Scientific boundary

No build, dependency resolution, runtime execution, or scientific execution was performed.

## Next gate

Reconcile the TGCV host packaging model against this exact historical target definition before any build is considered.
