# TGCV — Transformational Dynamics Formal Conformance Test Design 004

**Status:** DESIGN DRAFT — NOT EXECUTED
**Date:** 2026-10-01
**Supersedes for development:** Design 003
**Purpose:** define the deterministic state-only comparator `G_S` identified in Final Freeze Audit 003.

## 1. Scope

This document changes only the state-reducibility comparator. No other v0.3 or Design 003 semantics are changed.

## 2. State-only comparator

`G_S(S_a, S_b)` is a deterministic comparator applied separately to each frozen member of `C_S`.

Inputs are exactly:
- one state representation `S_a`;
- one state representation `S_b`;
- the fixed canonicalization/comparison rules for that representation class.

Forbidden inputs are `U`, `R`, action identities, preconditions, effects, relation graphs, goals, plan success, future states, execution traces, perturbation labels, oracle descriptors, and outcomes.

## 3. Output domain

`G_S` returns exactly one of:
- `NO_STRUCTURAL_CHANGE`;
- `STRUCTURAL_CHANGE`;
- `NON_COMPARABLE`.

`NON_COMPARABLE` is returned if the two state representations cannot be compared under their frozen schema or canonical correspondence.

## 4. Representation-specific comparison

### S_raw

Canonical typed predicate-set equality:
- equal canonical predicate/literal sets → `NO_STRUCTURAL_CHANGE`;
- both comparable and unequal → `STRUCTURAL_CHANGE`;
- missing/incompatible schema → `NON_COMPARABLE`.

### S_typed

Compare canonical predicate/type groups under the frozen type signature. Equal groups → `NO_STRUCTURAL_CHANGE`; unequal comparable groups → `STRUCTURAL_CHANGE`; incompatible signatures → `NON_COMPARABLE`.

### S_predicate_multiset

Compare the canonical count vector over the frozen predicate vocabulary. Equal vectors → `NO_STRUCTURAL_CHANGE`; unequal vectors → `STRUCTURAL_CHANGE`; incompatible vocabularies → `NON_COMPARABLE`.

### S_object_inventory

Compare the canonical typed-object count vector. Equal vectors → `NO_STRUCTURAL_CHANGE`; unequal vectors → `STRUCTURAL_CHANGE`; incompatible type schemas → `NON_COMPARABLE`.

## 5. State-reducibility decision

For a tested pair, let `D_struct` be the structural comparator's binary decision:
- `0` = no structural change;
- `1` = structural change.

For each `c ∈ C_S`, let `G_S(c)` be its result.

A member reproduces the structural decision iff:
- `D_struct = 0` and `G_S(c) = NO_STRUCTURAL_CHANGE`; or
- `D_struct = 1` and `G_S(c) = STRUCTURAL_CHANGE`.

`NON_COMPARABLE` never reproduces a structural decision.

The tested pair is `STATE-REDUCIBLE` iff at least one member of the finite frozen `C_S` reproduces `D_struct`.

The oracle records all reproducing members. No additional state representation may be introduced after execution.

## 6. Independence

`G_S` is not permitted to call the structural comparator, read `Ω_T`, or consume the perturbation manifest. Its implementation is frozen independently and its output is computed solely from its declared state representation.

## 7. Determinism

For identical serialized inputs and schema, `G_S` must return the same output byte-for-byte and classification. Any nondeterminism is a test failure.

## 8. Execution boundary

Execution remains **NOT AUTHORIZED**. Design 004 must pass the final no-open-issues audit before freeze.

## 9. Decision

**DESIGN 004 — READY FOR FINAL NO-OPEN-ISSUES AUDIT.**

No empirical claim, Core, RMA, Matrix, or claim status changes.