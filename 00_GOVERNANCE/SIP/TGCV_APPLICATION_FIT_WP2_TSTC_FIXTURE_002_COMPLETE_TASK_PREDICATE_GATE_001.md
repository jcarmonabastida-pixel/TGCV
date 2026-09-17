# TGCV Application Fit WP2 — TSTC Fixture 002 `complete_task` Predicate Gate 001

**Status:** `CLOSED — EXECUTION SUBSET EXCLUSION SELECTED; NO PREDICATE INVENTION`
**Date:** 2026-09-17

## 1. Gate question

Determine how Fixture 002 handles inherited `c03.complete_task`, whose Fixture-001 predicate is:

`task pending AND required declared task preconditions are satisfied`.

The required task preconditions are not enumerated in the frozen fixture.

## 2. Options

### Option A — Define missing preconditions now

Rejected for this gate.

Reason: defining them would constitute a new scientific fixture-semantic decision. No evidence in Fixture 001 identifies which state/context variables are the required conditions. Substituting `db available`, `permission_db`, `tool_query`, or any other condition would be implementation inference.

### Option B — Exclude from executable Fixture-002 subset

**Selected.**

`c03.complete_task` is retained only as an inherited transformation identity for traceability/documentation. It is **not included in the executable transformation universe `Uτ` for the Fixture-002 minimum demonstrator** until its admissibility predicate is explicitly defined in a future fixture-definition revision.

No predicate is invented and no hidden condition is substituted.

## 3. Conformance consequence

This treatment is compatible with the TSTC Implementation Specification because every transformation actually present in the executable `Uτ` can then have a deterministic declared predicate, affected-variable declaration and transition operator. The inherited `complete_task` identity is not silently represented as an executable transformation with a non-machine-executable predicate.

The exclusion MUST be explicit in Fixture-002 metadata and MUST NOT be implemented as a runtime filter that silently removes the transformation after fixture loading.

## 4. Scientific boundary

This gate does not conclude that `complete_task` is impossible, invalid, or scientifically irrelevant. It concludes only that its current inherited predicate is insufficiently specified for the minimum deterministic TSTC demonstrator.

A future fixture version may explicitly define its preconditions and reintroduce it into `Uτ`.

## 5. Required Fixture-002 update

Before freeze, Fixture-002 must explicitly record:

- inherited transformation identity: `c03.complete_task`;
- status: `TRACEABILITY_ONLY / NON_EXECUTABLE`;
- exclusion from executable `Uτ`;
- reason: `INHERITED_PREDICATE_UNDER_SPECIFIED`;
- no inferred preconditions;
- no trajectory eligibility.

The executable C03 transformation universe therefore contains the transformations whose predicates and transition semantics are explicitly defined, including `c03.modify_repo`, but excludes `c03.complete_task`.

## 6. Governance boundary

- Fixture 001: unchanged and frozen.
- Fixture 002: still not frozen until the explicit exclusion is incorporated into its frozen specification and the final freeze conformance review passes.
- TSTC execution: not authorized.
- No TGCV Core change.
- No RMA or Evidence→Claim Matrix change.
- No C09/C10 change.

**Next controlled gate:** incorporate this explicit execution-subset exclusion into the Fixture-002 specification, then perform the final freeze/conformance review of Fixture 002 as a whole.
