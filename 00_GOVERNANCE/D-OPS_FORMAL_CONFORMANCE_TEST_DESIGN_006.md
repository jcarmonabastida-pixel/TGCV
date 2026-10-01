# TGCV — Transformational Dynamics Formal Conformance Test Design 006

**Status:** DESIGN DRAFT — NOT EXECUTED
**Date:** 2026-10-01
**Supersedes for development:** Design 005
**Purpose:** close the two specification points identified in Design 005 Audit 001.

## 1. R3 provenance

For every frozen formal fixture, R3 is an ex ante authored structural relation.

The fixture package MUST contain:
- a canonical R3 edge list;
- the SHA-256 of the exact serialized edge list;
- provenance metadata identifying the fixture authoring record/version;
- the R3 manifest path and schema version.

R3 MUST NOT be generated from R1, R2, initial state, goals, execution traces, planner success, outcomes, rewards/utilities, or downstream descriptors.

The oracle independently reads the frozen R3 manifest and recomputes its hash. Hash mismatch is a preflight FAIL.

## 2. Identity-level descriptor precedence

Classification uses this deterministic precedence:
1. NON_COMPARABLE if canonical correspondence cannot be established.
2. EXPANSION if U gains at least one transformation identity.
3. CONTRACTION if U loses at least one transformation identity.
4. Otherwise classify relation/identity structure:
   - PERSISTENCE if Δ≡=ΔR1=ΔR2=ΔR3=∅;
   - RECONFIGURATION_ONLY if Δ≡=ΔR1=ΔR2=∅ and ΔR3 contains exactly one deletion and one addition;
   - OTHER_STRUCTURAL_CHANGE otherwise.

Detailed diffs MUST always be retained, including relation changes incident to added/removed identities.

Thus EXPANSION/CONTRACTION are primary identity-level classes; they do not erase relational information.

## 3. Determinism

The classification function is pure and deterministic over the canonical five-way diff D=(ΔU, Δ≡, ΔR1, ΔR2, ΔR3).

No classifier input may include outcomes, execution, reward/utility, planner success or downstream evidence.

## 4. Freeze boundary

Design 005 Audit 001 findings are closed by Sections 1–2.

No other semantics are changed.

Execution remains NOT AUTHORIZED.

## 5. Package implications

Freeze Package 001 remains invalid.

A new package must be generated from Design 006 and independently audited before preflight.

## 6. Decision

**DESIGN 006 — READY FOR FINAL DESIGN AUDIT.**

No empirical claim, Core, RMA, Matrix, or claim status changes.