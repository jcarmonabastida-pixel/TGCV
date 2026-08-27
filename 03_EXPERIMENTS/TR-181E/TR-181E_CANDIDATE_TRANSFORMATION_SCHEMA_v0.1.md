# TR-181E — Candidate Transformation Schema v0.1

**Status:** DESIGN / UNIT-TEST SPECIFICATION — NOT FROZEN
**Date:** 2026-08-27

## 1. Scope

This document defines the first concrete, testable candidate schema for TR-181E. It is not claimed to be the historical EMP-1.1 schema.

## 2. Transformation object

Each candidate transformation is a deterministic tuple:

`τ = (type, target, pre, eff)`

where `type` is a pre-declared transformation class, `target` identifies the affected component/resource/objective element, `pre` is a conjunction of snapshot predicates, and `eff` is the declared post-state change.

## 3. Candidate classes

Use only classes whose preconditions/effects can be expressed from the frozen snapshot schema:

- `ACTIVATE`: make an existing component/resource capability available;
- `COMPOSE`: create an executable relation between compatible existing components;
- `RECONFIGURE`: change a declared configuration of an existing component;
- `ACQUIRE`: convert an available resource condition into a component capability;
- `LEARN`: expose a capability when a declared learning precondition is satisfied;
- `RECOMBINE`: create a new configuration from compatible existing elements.

These six labels are **new TR-181E operational classes**, not recovered EMP-1.1 historical families.

## 4. Accessibility predicate

A candidate `τ` is accessible iff all of its declared preconditions are true in the pre-outcome snapshot and all required targets/resources exist:

`Pτ(S,C,L) = 1 iff Preτ(S,C,L) ∧ Targetτ(S,C,L) ∧ Resourceτ(S,C,L)`.

No future state, trajectory or outcome may enter the predicate.

## 5. Important restriction on effects

`eff` describes the potential transformation only. It is not executed recursively to create additional transformations during R computation. Therefore R is a one-snapshot accessibility representation and cannot silently become a multi-step planner.

## 6. R candidate vector

For each snapshot, construct a fixed-length vector containing:

- total number of accessible candidates;
- count per class (six values);
- class entropy/diversity, using a pre-declared convention;
- number of distinct affected components;
- number of distinct affected resource types;
- candidate-to-component incidence density.

Exact encoding and normalisation remain OPEN until unit tests establish that each feature is deterministic, pre-outcome, and non-duplicative of B.

## 7. Required unit tests

Before freeze:

1. identical snapshot → identical R;
2. changing only outcome → R unchanged;
3. changing only future trajectory → R unchanged;
4. removing a required resource cannot increase accessibility for any candidate requiring it;
5. adding a satisfied precondition cannot decrease accessibility for that candidate;
6. candidate ordering does not change R;
7. no feature reads outcome/trajectory fields;
8. B and R have no accidental feature duplication;
9. empty candidate set is handled deterministically;
10. malformed snapshots fail closed rather than silently producing R.

## 8. Selection rule

This schema is a candidate because it is minimal enough to implement and broad enough to represent distinct mechanisms without making mechanism ontologically primitive. It must not be selected because it reproduces the EMP-1.1 effect.

## 9. Gate

**Candidate schema:** DEFINED

**Formal predicates:** PARTIALLY DEFINED

**Executable encoding:** OPEN

**Test execution:** NO CONFIRMATORY TEST AUTHORIZED

**Next:** implement only unit-test scaffolding and verify the invariants above before freezing the executable representation.
