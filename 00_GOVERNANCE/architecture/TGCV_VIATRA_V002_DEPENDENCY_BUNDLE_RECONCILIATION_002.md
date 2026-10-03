# TGCV VIATRA V002 Dependency / Bundle Reconciliation 002

## Status

**SUPERSEDED — HISTORICAL RUNTIME DEPENDENCY RECONCILIATION**

This reconciliation is tied to the earlier VIATRA core revision `ffa111db...` and is not the current Observer Host packaging dependency contract. The current host build is based on the pinned historical examples revision `eb68158a...` and has been verified by run `37123064623`.

## Finding

The previous binding correctly identified the Eclipse/OSGi packaging boundary but retained an incorrect version interpretation for the VIATRA query runtime.

At source revision `ffa111dbb160c0bc55e89ea16430e97a38908662`:

- `org.eclipse.viatra.query.runtime` is an Eclipse plug-in with Maven project version `2.10.0-SNAPSHOT`;
- its OSGi bundle declaration in the tutorial uses bundle-version `1.2.0`.

These are different version namespaces and MUST NOT be conflated.

## Canonical consequence

The host specification SHALL record both values distinctly:

- Maven project version: `2.10.0-SNAPSHOT`;
- tutorial bundle-version: `1.2.0`.

The same distinction SHALL be preserved for every Eclipse/OSGi dependency where source evidence exposes both Maven and bundle versions.

## Build boundary

No build has been performed.

The current host remains a materialization skeleton and is not yet build-verified.

## Next gate

Reconcile the complete set of host dependencies using the source project's actual `MANIFEST.MF` / Maven metadata, preserving Maven project versions and OSGi bundle versions as separate provenance fields.
