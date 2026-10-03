# TGCV VIATRA V002 Observer Target Dependency Audit 001

Status: BLOCKED — MODEL BUNDLES NOT SUPPLIED

## Scope

Static reconciliation of the current TGCV V002 observer host target platform against the effective dependencies introduced by the semantic fixture loader.

No build or runtime execution was performed.

## Effective observer dependencies

The loader directly imports:

- org.eclipse.emf.common
- org.eclipse.emf.ecore
- org.eclipse.emf.ecore.xmi
- org.eclipse.viatra.examples.cps.model
- org.eclipse.viatra.examples.cps.deployment
- org.eclipse.viatra.examples.cps.traceability

## Target-platform finding

The preserved historical target definition
`org.eclipse.viatra.examples.cps.target.target`
is byte-identical to the historical target at source revision
`eb68158a3d74581f69ccb8bc4f47673b12abdf85` (source SHA:
`7481dee30f1ae07d7dd9212d7891dc336f1e96ae`).

Its installable units provide the Eclipse/EMF/Xtext/etc. environment, including
the EMF SDK, but do not themselves declare the three VIATRA CPS model bundles.

The current TGCV observer reactor contains only:

- target-definition
- observer

It does not contain the three historical CPS model bundles as reactor modules.

Therefore the current target/reactor combination does not yet establish a complete supply path for:

- org.eclipse.viatra.examples.cps.model
- org.eclipse.viatra.examples.cps.deployment
- org.eclipse.viatra.examples.cps.traceability

## Historical bundle evidence

At the pinned historical source revision:

- CPS model bundle: Bundle-Version 2.1.0.qualifier
- Deployment model bundle: Bundle-Version 2.1.0.qualifier
- Traceability bundle: Bundle-Version 2.1.0.qualifier

Traceability reexports the CPS model and Deployment bundles.

These historical manifests are source evidence; their versions must not be substituted into the current target definition without establishing the corresponding artifact/repository provenance.

## Decision

Do not build and do not modify the target definition speculatively.

The next required operation is to establish an exact, reproducible supply mechanism for the three historical model bundles, preserving the pinned source revision and distinguishing source provenance from Maven/OSGi version coordinates.

## Firewall

This audit does not authorize:

- build
- runtime execution
- fixture execution
- VIATRA transformation execution
- scientific execution
- changes to fixture bytes
