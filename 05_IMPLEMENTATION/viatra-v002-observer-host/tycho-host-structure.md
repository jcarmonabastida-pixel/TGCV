# TGCV VIATRA V002 Minimal Tycho Host Structure

## Purpose

Define the minimum materialization required to represent the frozen historical VIATRA packaging boundary without executing a build.

## Structure

```
viatra-v002-observer-host/
├── pom.xml
├── target-definition/
│   ├── pom.xml
│   └── org.eclipse.viatra.examples.cps.target.target
└── observer/
    ├── META-INF/
    │   └── MANIFEST.MF
    └── build.properties
```

## Rules

1. The target-definition project SHALL preserve the historical target file byte content and source revision.
2. The observer SHALL be a distinct TGCV OSGi bundle; it SHALL NOT reuse the historical VIATRA example Bundle-SymbolicName.
3. The historical transformation bundle SHALL remain a provenance reference, not be silently copied and renamed.
4. OSGi dependencies SHALL be declared through MANIFEST.MF.
5. The parent reactor SHALL use Tycho-compatible packaging.
6. Java compatibility SHALL follow the frozen historical JavaSE-1.8 boundary.
7. No generated sources, compiled classes, target-platform resolution, or runtime artifacts SHALL be introduced by this materialization step.
8. Canonical V002 fixtures remain immutable inputs.

## Build boundary

This document authorizes only repository materialization of the static Tycho structure. It does not authorize Maven/Tycho build execution, dependency resolution, runtime execution, or scientific execution.
