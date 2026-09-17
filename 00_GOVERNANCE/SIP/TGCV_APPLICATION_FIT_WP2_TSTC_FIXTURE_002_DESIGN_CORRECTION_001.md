# TGCV Application Fit WP2 — TSTC Fixture 002 Design Correction 001

**Status:** `DESIGN CORRECTION — NOT FROZEN; SECOND CONFORMANCE REVIEW PENDING`
**Date:** 2026-09-17
**Upstream blocker:** `TGCV_APPLICATION_FIT_WP2_TSTC_FIXTURE_002_TRANSITION_SEMANTICS_CONFORMANCE_REVIEW_001.md`

## 1. Purpose

Resolve the three blockers identified by the first conformance review without modifying Fixture 001 and without supplying semantics by implementation inference.

This document is a controlled design correction, not a fixture freeze and not an execution authorization.

## 2. C03 `complete_task`

### Finding

Fixture 001 defines:

`complete_task iff task pending AND required declared task preconditions are satisfied.`

The phrase `required declared task preconditions` is not enumerated in the frozen fixture. The TSTC implementation contract requires executable deterministic predicates and predicate traces.

### Correction

Do **not** invent the missing preconditions.

For Fixture 002, `c03.complete_task` is therefore classified as:

`INHERITED IDENTITY / EXECUTION-BLOCKED PREDICATE`

It remains documented as an existing transformation identity, but it is excluded from the executable trajectory subset until its admissibility predicate is explicitly specified in a subsequent fixture-design decision.

No implementation may silently substitute `db available`, `permission_db granted`, `tool_query available`, or any other condition as the missing requirement.

A future fixture version may make the predicate explicit, but that is a separate scientific-definition change.

## 3. C05 `redirect_A_to_B`

### Finding

The frozen state contains `ev_A`, `ev_B`, and site availability, but no vehicle location/destination variable. The proposed operator `ev_A waiting -> charging` therefore does not encode the semantic destination B.

### Correction

For the minimum Fixture-002 demonstrator, `c05.redirect_A_to_B` is changed to an **identity-preserving represented-state transformation**:

- affected variables: `[]`;
- transition operator: identity on the represented state/context;
- admissibility predicate remains the inherited frozen predicate;
- explicit limitation: the fixture does not represent destination/location state and therefore does not claim to model the physical relocation itself.

This preserves the transformation identity without inventing a hidden destination variable or falsely encoding redirection as charging.

The trajectory may record the transformation identity, but no represented-state claim about destination B may be inferred from it.

## 4. C05 `reduce_power_A`

`c05.reduce_power_A` remains identity-preserving with respect to represented fixture state/context:

- affected variables: `[]`;
- transition: identity;
- explicit limitation: no power-level state variable exists;
- no hidden mutation of `grid_capacity` is permitted.

This is an explicit modelling boundary, not an implementation omission.

## 5. C01 → C03 → C05 composed scenario

### Finding

The previous design proposed:

`C01 restrict_security`
→ `permission_repo=denied`
→ `C03 modify_repo`
→ `repo=changed`
→ `mobility_requirement_A=urgent`.

But `c03.modify_repo` requires `permission_repo=granted`. Therefore that sequence is internally impossible after the C01→C03 propagation.

### Correction

Do not weaken either predicate and do not alter the coupling rule.

The composed fixture is split into two explicitly declared scenarios:

### Scenario A — C01→C03 propagation

1. Initial state/context.
2. `c01.restrict_security`.
3. Propagate `permission_repo: granted -> denied`.
4. Recalculate C03 `T_acc`.
5. Record the closed repository transformations, including `c03.modify_repo`.

This scenario tests the first coupling edge only.

### Scenario B — C03→C05 propagation

1. Independent declared initial/control condition with `permission_repo=granted`.
2. `c03.modify_repo` produces `repo: clean -> changed`.
3. Propagate `mobility_requirement_A: normal -> urgent`.
4. Recalculate C05 `T_acc`.

This scenario tests the second coupling edge independently.

### Combined chain

The full C01→C03→C05 path is therefore **not claimed as a single executable trajectory in Fixture 002**. The two propagation mechanisms are tested separately because their frozen predicates make simultaneous execution incompatible.

This is a design limitation, not a failure to be repaired by implementation.

## 6. Conformance consequences

The correction removes the semantic mismatch for `redirect_A_to_B` and the logical contradiction in the composed sequence without changing Fixture 001.

The `complete_task` predicate remains the outstanding blocker for a fully executable Fixture-002 transformation universe. It must be resolved explicitly before Fixture 002 can be frozen as a complete executable fixture.

## 7. Freeze gate

Fixture 002 remains:

`NOT FROZEN`

Execution remains:

`NOT AUTHORIZED`

Required next gate:

**Second conformance review**, verifying:

1. `complete_task` handling is acceptable under the TSTC schema/trajectory contract;
2. identity-preserving `redirect_A_to_B` is explicitly bounded and does not generate hidden destination claims;
3. Scenario A and Scenario B satisfy explicit coupling and baseline-parity requirements;
4. negative controls remain unchanged;
5. no Fixture-001 semantics were modified.

No TGCV Core, RMA, Evidence→Claim Matrix, C09, C10 or industrial governance change is permitted by this document.
