# TGCV — Transformational Dynamics Formal Conformance Test Design 007

**Status:** DESIGN DRAFT — NOT EXECUTED
**Date:** 2026-10-01
**Supersedes for development:** Design 006
**Purpose:** close the simultaneous U-gain/U-loss edge case identified in Design 006 Final Audit.

## 1. Identity-level classification

Let ΔU_added = U_new minus U_old; ΔU_removed = U_old minus U_new.

Apply this deterministic rule after NON_COMPARABLE checking:
1. If ΔU_added is nonempty and ΔU_removed is empty: EXPANSION.
2. If ΔU_added is empty and ΔU_removed is nonempty: CONTRACTION.
3. If both are nonempty: OTHER_STRUCTURAL_CHANGE.
4. If both are empty, continue to relation-level classification.

This rule takes precedence over all relation-level descriptors.

## 2. Relation-level classification

When both identity diffs are empty:
- PERSISTENCE iff Δ≡=ΔR1=ΔR2=ΔR3=empty;
- RECONFIGURATION_ONLY iff Δ≡=ΔR1=ΔR2=empty and ΔR3 contains exactly one deletion and one addition;
- otherwise OTHER_STRUCTURAL_CHANGE.

## 3. Complete classifier

The complete descriptor function is therefore:

NON_COMPARABLE → pure EXPANSION → pure CONTRACTION → mixed identity change OTHER_STRUCTURAL_CHANGE → PERSISTENCE → RECONFIGURATION_ONLY → OTHER_STRUCTURAL_CHANGE.

The complete canonical diff is retained for every case.

## 4. Freeze boundary

No other Design 006 semantics change.

Execution remains NOT AUTHORIZED.

Freeze Package 001 remains invalid.

A new package must be generated from Design 007 and pass final no-open-issues audit and freeze preflight before any conformance execution can be considered.

## 5. Decision

**DESIGN 007 — READY FOR FINAL NO-OPEN-ISSUES AUDIT.**

No empirical claim, Core, RMA, Matrix, or claim status changes.