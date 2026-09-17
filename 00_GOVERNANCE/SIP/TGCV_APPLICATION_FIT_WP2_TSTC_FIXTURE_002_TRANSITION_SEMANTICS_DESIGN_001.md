# TGCV Application Fit WP2 — TSTC Fixture 002 Transition Semantics Design 001

**Status:** `DESIGN GATE — NOT FROZEN`

## 1. Objective

Resolve the transition-semantic gaps identified by the Fixture-001 inheritance audit without modifying Fixture 001.

The design below distinguishes three categories:

- **INHERITED:** semantics already explicit in Fixture 001;
- **EXPLICIT-NEW:** semantics that must be added to Fixture 002;
- **BLOCKED:** semantics that cannot be supplied without an unresolved fixture-design decision.

## 2. C03 — required resolution

### 2.1 Existing transformations

`c03.query_db`, `c03.inspect_repo`, `c03.open_pr`, and `c03.complete_task` remain unchanged as identities and admissibility predicates.

Their transition operators must be explicitly defined in Fixture 002 before execution.

### 2.2 New repository-changing transformation

To make the already-declared C03→C05 coupling executable without assigning an arbitrary mutation to a read/review/PR-completion action, Fixture 002 should add:

`c03.modify_repo`

Semantics:

- precondition: `repo=clean AND permission_repo=granted`;
- affected variables: `[repo]`;
- transition: `repo: clean -> changed`;
- postcondition: `repo=changed`;
- provenance: `EXPLICIT-NEW — Fixture 002 synthetic scenario`.

This is a genuine Fixture-002 transformation-universe change. It must not be described as an implementation repair to Fixture 001.

### 2.3 C03 trajectory operators

The following minimal operators are proposed:

- `query_db`: identity-preserving read; affected variables `[]`;
- `inspect_repo`: identity-preserving inspection; affected variables `[]`;
- `open_pr`: identity-preserving action with respect to the variables represented in the fixture; affected variables `[]`;
- `complete_task`: `task: pending -> completed`; affected variables `[task]`;
- `modify_repo`: `repo: clean -> changed`; affected variables `[repo]`.

The identity-preserving operators are deliberate: the fixture contains no state variable representing query results, inspection output, PR existence, or workflow artefact creation. The design therefore does not invent hidden state merely to make these actions appear transformational.

## 3. C01 — transition semantics

Fixture 002 should explicitly define:

- `deploy_A`: `service absent -> deployed`, `compute_A free -> occupied`; affected `[service, compute_A]`;
- `deploy_B`: `service absent -> deployed`, `compute_B free -> occupied`; affected `[service, compute_B]`;
- `route_A_to_B`: `routing A -> B`; affected `[routing]`;
- `route_B_to_A`: `routing B -> A`; affected `[routing]`;
- `restrict_security`: `security normal -> restricted`; affected `[security]`;
- `restore_security`: `security restricted -> normal`; affected `[security]`.

These operators are proposed as explicit Fixture-002 synthetic semantics. They are not being retroactively attributed to Fixture 001.

The deployment operators intentionally leave routing unchanged because Fixture 001 does not state that deployment changes routing. No hidden routing mutation may be introduced.

## 4. C05 — transition semantics

Fixture 002 should explicitly define:

- `start_A`: `ev_A waiting -> charging`; affected `[ev_A]`;
- `start_B`: `ev_B waiting -> charging`; affected `[ev_B]`;
- `defer_A`: identity-preserving; affected `[]`;
- `defer_B`: identity-preserving; affected `[]`;
- `redirect_A_to_B`: `ev_A waiting -> charging`; affected `[ev_A]`;
- `reduce_power_A`: identity-preserving with respect to represented fixture state; affected `[]`.

The last two are intentionally conservative. Fixture 001 has no vehicle-location variable and no power-level variable, so the design must not invent either merely from the transformation names.

## 5. Cross-domain semantics

The coupling sequence becomes:

1. C01 `restrict_security` changes `security` to `restricted`.
2. Coupling rule propagates `permission_repo: granted -> denied` to C03.
3. C03 accessibility is recalculated.
4. Independently, a C03 `modify_repo` transition can produce `repo: clean -> changed` when its own admissibility predicate is satisfied.
5. Coupling rule propagates `mobility_requirement_A: normal -> urgent` to C05.
6. C05 accessibility is recalculated.

The local C03 repository mutation and the propagated C01→C03 permission effect must be logged as separate events.

## 6. Important interaction with the C03 positive intervention

Under the positive C03 intervention:

`permission_repo: granted -> denied`

`c03.modify_repo` becomes inaccessible.

That is acceptable and scientifically informative at the fixture level: the intervention closes both existing repository actions and the newly explicit repository-changing transformation.

It does not justify changing the intervention to preserve the desired cross-domain path.

Therefore the cross-domain sequence must be tested under its own declared initial/control condition rather than silently combining it with the C03 positive intervention if that would make the sequence impossible.

## 7. Negative controls

The existing negative controls remain unchanged.

Expected:

`Delta_T_acc = empty`

No transition operator may manufacture an accessibility change from an identity-preserving negative control.

## 8. Design decision gate

Before Fixture 002 is frozen, the following must be explicitly accepted:

- adding `c03.modify_repo` is a deliberate synthetic fixture change;
- identity-preserving operators are acceptable where the fixture has no state variable representing the real-world side effect;
- deployment consumes the declared compute resource but does not silently change routing;
- the cross-domain sequence is a separate composed scenario and is not required to coincide with every positive intervention;
- no additional state variable is needed for the minimum demonstrator.

If any of these are rejected, Fixture 002 must remain unfrozen and the design must be revised rather than implemented by inference.

## 9. Next gate

This document is a **design proposal**, not a frozen fixture.

Next controlled action: run a conformance review of these proposed operators against the TSTC implementation specification and frozen Fixture-001 predicates, with particular attention to predicate/operator consistency and intervention compatibility.

No execution is authorized by this document.
