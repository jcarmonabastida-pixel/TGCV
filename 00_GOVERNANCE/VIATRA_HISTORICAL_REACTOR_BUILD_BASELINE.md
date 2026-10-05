# VIATRA Historical Reactor Build Baseline

Status: FROZEN / REPRODUCIBLE
Date: 2026-10-05

## Purpose

This document freezes the validated build recipe for the historical VIATRA 2.0.2 reactor used by the TGCV execution infrastructure.

This baseline is an infrastructure reference. It is not a scientific result and does not alter any scientific input, estimator, DGP, fixture, or result.

## Source of truth

Repository: jcarmonabastida-pixel/TGCV
Workflow: .github/workflows/tgcv-viatra-v002-historical-source-build-probe.yml

The workflow content is identical on:
- main
- probe/viatra-xtend-212-jdt-compat

Workflow blob SHA on both branches:
fbb117ad9f8c865451071ae1ec540156dacb305a

## Validated reference runs

- Probe reference: 37319099389 — SUCCESS
- Main reference: 37322828418 — SUCCESS

Both executions completed the same 31-step build/diagnostic chain successfully, including the full historical reactor build.

## Frozen build sequence

1. Checkout pinned VIATRA 2.0.2 source.
2. Use Java 8 and the configured Maven toolchain.
3. Inspect and constrain the historical Eclipse/JDT execution environment.
4. Isolate modern JDT/Eclipse dependencies from the historical Maven plugin realm.
5. Pin/normalize historical Eclipse and EMF dependencies.
6. Provide the missing EMF Codegen runtime dependency required by the historical VIATRA Maven Plugin.
7. Run EMF Codegen before VIATRA query generation.
8. Precompile generated EMF sources exclusively from `emf-gen` before the VIATRA Maven Plugin consumes generated model types.
9. Run the complete historical reactor build.
10. Preserve the resulting workflow as the reproducible baseline.

## Critical compatibility corrections frozen in this recipe

The validated workflow contains the accumulated corrections for:
- historical Xtend 2.12 / JDT compatibility;
- modern JDT Core isolation;
- historical Eclipse core.resources compatibility;
- core.expressions isolation;
- core.contenttype isolation;
- equinox.app isolation;
- core.commands isolation;
- historical core.resources pinning;
- normalized historical Eclipse/EMF dependency realm;
- missing EMF Codegen runtime dependency;
- generated-EMF precompilation ordering.

The generated-source ordering is intentionally:

EMF Codegen -> precompile emf-gen -> VIATRA Maven Plugin -> normal compilation

## Validation criterion

The baseline is considered valid because the complete historical reactor reaches BUILD SUCCESS in both the validated probe and main executions.

## Freeze rule

Do not modify this workflow baseline as part of scientific execution.

If a future build requires a change, create and validate a new probe/baseline rather than changing this frozen recipe in place.

## Scientific boundary

Successful compilation establishes infrastructure reproducibility only. It does not constitute evidence for TGCV, Transformational Intelligence, or any scientific hypothesis.

Before scientific execution, verify the already-audited scientific artifact identity, configuration, SHA chain, authorization gate, and execution parameters. Do not repeat closed audits/preflights unless an input has changed.
