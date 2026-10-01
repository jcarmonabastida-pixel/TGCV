# TGCV — D-OPS Formal Conformance Freeze Preflight 001

**Status:** PREFLIGHT DESIGN — NOT EXECUTED
**Date:** 2026-10-01
**Protocol:** D-OPS Formal Conformance Test Design 004
**Purpose:** define the exact preflight required before the formal conformance protocol may be frozen or executed.

## 1. Boundary

This preflight validates the integrity of the freeze package. It does not execute the scientific/formal test and does not establish empirical evidence.

No execution is authorized by this document.

## 2. Required freeze-package contents

The package MUST contain, as immutable inputs:

1. one finite D0 domain/problem fixture;
2. canonicalization implementation;
3. R1/R2/R3 relation-builder implementation;
4. perturbation manifest for persistence, expansion, contraction and reconfiguration;
5. finite C_S schema and implementation;
6. independent G_S implementation;
7. independent oracle implementation;
8. expected-result manifest;
9. deterministic executor/environment manifest;
10. result JSON schema and canonical serialization rules;
11. complete SHA-256 manifest;
12. provenance/readme manifest identifying versions and source paths.

A missing item is a preflight FAIL.

## 3. Structural checks

The preflight MUST verify:
- D0 is finite and deterministic;
- all referenced files exist;
- every package file has a SHA-256 entry;
- hashes recompute exactly;
- no generated result is included as an input;
- oracle and SUT are distinct implementations;
- G_S has no dependency on Ω_T, R, perturbation labels, oracle output or downstream evidence;
- reconfiguration fixture satisfies U/≡/R1/R2 equality and exactly one R3 deletion/addition;
- C_S contains exactly the four frozen representations;
- expected results are generated independently of SUT descriptor labels.

## 4. Clean-room check

The package MUST be testable from a clean environment using only frozen inputs and declared dependencies.

The preflight records runtime/version, dependency lock, operating-system/runtime assumptions, locale/encoding assumptions, line-ending/serialization assumptions, and deterministic seed where applicable.

Any undeclared dependency is a FAIL.

## 5. Information-firewall check

The execution graph must be inspected before authorization.

Forbidden information flow into the construction of Ω_T or G_S includes outcomes, rewards/utilities, planner success, realized trajectories, future states, perturbation labels, and oracle classifications.

Any such dependency is a FAIL.

## 6. Expected-result check

The independent oracle is run in preflight only to generate/verify the expected-result manifest. The SUT is NOT run.

The expected-result manifest must contain all test IDs and expected classifications, including persistence, expansion, contraction, reconfiguration-only, representation invariance, structural null, state-only variation, structural change at fixed state, NON-COMPARABLE, conditional H0, and conditional H1.

## 7. Freeze decision

Preflight PASS requires all mandatory checks to pass and all package hashes to be internally consistent.

A PASS authorizes freeze-package creation, not scientific execution.

A FAIL blocks freeze and execution.

## 8. Output artifacts

A successful preflight must produce machine-readable preflight result, SHA-256 manifest, dependency/environment manifest, expected-result manifest, audit log, and package-level SHA-256.

These outputs must be independently auditable.

## 9. Decision

**READY TO RUN PREFLIGHT — NOT EXECUTED.**

The next operation is to materialize the actual package from the frozen repository artifacts and run this preflight. No execution of the conformance tests is permitted before a successful preflight and explicit execution authorization.