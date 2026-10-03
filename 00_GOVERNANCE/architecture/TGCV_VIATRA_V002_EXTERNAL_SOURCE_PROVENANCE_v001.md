# TGCV VIATRA V002 External Source Provenance v001

## Status

SOURCE RECOVERED — PACKAGING STILL UNRESOLVED.

## Recovered source

The concrete CPS batch transformation implementation containing the V002-bound `hostRule` was recovered from the historical VIATRA examples repository:

Repository:
`eclipse-viatra/org.eclipse.viatra.examples`

Historical source commit:
`eb68158a3d74581f69ccb8bc4f47673b12abdf85`

The recovered source contains:

`cps/transformations/org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra/src/org/eclipse/viatra/examples/cps/xform/m2m/batch/viatra/CPS2DeploymentBatchViatra.xtend`

and the concrete rule:

`createRule(HostInstance.instance).name("HostRule").action[...] .build`

The rule action reads `hostInstance.nodeIp`, creates a `DeploymentHost`, assigns its IP, and creates a `CPS2DeploymentTrace` linking the source host and deployment host.

## Relationship to V002

This historical source is provenance evidence for the concrete implementation family underlying the tutorial `hostRule`.

It is NOT silently substituted for the already frozen VIATRA documentation revision `ffa111db...`.

The V002 source binding remains anchored to the documented tutorial revision. This recovered repository/commit is an external provenance reference used to resolve the previously missing implementation source.

## Packaging status

The discovery recovered transformation source, but did not establish the exact OSGi bundle packaging for:

`com.incquerylabs.course.cps.viatra.batch;bundle-version="0.1.0"`

Therefore:

- transformation source provenance: PASS;
- exact bundle packaging provenance: OPEN;
- exact external binary artifact provenance: OPEN.

No `MANIFEST.MF`, feature definition, binary checksum, or release artifact is claimed unless independently located.

## Reproducibility boundary

The recovered source may be used for source-level comparison and provenance analysis.

It SHALL NOT be copied into TGCV as if it were the original bundle, and it SHALL NOT be treated as runtime-equivalent merely because the source implements the same semantic rule.

## Scientific boundary

No build, runtime execution, runtime-equivalence claim, or scientific execution was performed.

## Next gate

Resolve the exact historical bundle packaging/release artifact for `com.incquerylabs.course.cps.viatra.batch`, or formally close that item as unavailable and redesign the host around a source-verifiable implementation.
