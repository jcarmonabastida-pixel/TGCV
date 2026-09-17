# TGCV — WP2 TSTC Fixture 001 Execution Adapter Specification 001

**Status:** FROZEN — ADAPTER DEFINITION; EXECUTION BLOCKED UNTIL CONFORMANCE PASS
**Date:** 2026-09-17
**Purpose:** operationalise Fixture Freeze 001 without changing its scientific/fixture identity

## 1. Scope

This document defines the implementation boundary between the frozen synthetic fixture definitions and an executable deterministic engine.

It is an **adapter specification**, not a new fixture and not a scientific result.

Fixture Freeze 001 remains authoritative for:

- state variables and domains;
- context variables and domains;
- transformation identities;
- admissibility predicates;
- positive interventions;
- negative controls;
- cross-domain coupling conditions;
- baseline information.

The adapter may supply executable metadata only where that metadata is an operational representation of an already frozen definition.

It must not invent missing transition semantics.

## 2. Adapter principles

1. Frozen fixture identity is immutable.
2. Every executable transformation must have explicit `affected_variables`.
3. Every executable transition must be deterministic and explicit.
4. An adapter declaration must be traceable to the frozen fixture text.
5. A missing semantic cannot be repaired by inference at execution time.
6. If a required transition is not defined by Fixture 001, execution fails closed.
7. A new fixture version is required for any genuine semantic addition.

## 3. Classification of executable metadata

Each adapter field receives one of three classifications:

- **DERIVED:** mechanically recoverable from the frozen definition without adding semantic content.
- **EXPLICIT-IMPLEMENTATION:** an implementation encoding of a semantic already specified by the frozen fixture.
- **MISSING:** required for execution but not specified by Fixture 001; cannot be invented.

Only DERIVED and EXPLICIT-IMPLEMENTATION fields may be supplied by the adapter.

## 4. Transition contract

For each transformation:

```text
transformation_id
predicate
affected_variables
transition_operator
```

The predicate is frozen by Fixture 001.

`affected_variables` and `transition_operator` are executable representations of the transformation semantics. They must be checked together:

- every changed variable must be declared;
- no undeclared variable may change;
- no declared variable may change without a deterministic operator;
- applying a transformation must preserve all variables outside its declared effect set.

An empty effect set is valid only for a genuinely state/context-preserving transformation. It is not valid for a transformation whose semantics require a state change.

## 5. C01 adapter determination

`c01.restrict_security` has an executable semantic directly implied by its identity and predicate:

```text
precondition: security=normal
transition: security=restricted
affected_variables: [security]
```

`c01.restore_security` similarly maps:

```text
precondition: security=restricted
transition: security=normal
affected_variables: [security]
```

These mappings are classified **EXPLICIT-IMPLEMENTATION**, because they encode the frozen transformation meaning rather than adding a new transformation.

The remaining C01 transitions must be operationalised only through their already declared state-changing semantics. No additional transformation identity may be introduced.

## 6. C03 adapter determination

The frozen fixture explicitly defines the state variable:

```text
repo = {clean, changed}
```

and the transformations:

```text
c03.query_db
c03.inspect_repo
c03.open_pr
c03.complete_task
```

However, Fixture 001 does **not** explicitly state which transformation changes `repo` from `clean` to `changed`.

The required cross-domain sequence nevertheless requires:

```text
repo=clean → repo=changed
```

before the C03→C05 coupling can fire.

Therefore the required `repo` transition is classified:

**MISSING — NOT EXECUTABLE FROM FIXTURE 001 WITHOUT ADDITIONAL SEMANTIC ASSUMPTION.**

In particular, the adapter MUST NOT silently assign `repo=clean → changed` to `inspect_repo`, `open_pr`, or `complete_task` merely from their names.

## 7. Consequence for cross-domain execution

Coupling rule 1 is executable in principle:

```text
C01 security=restricted
→ C03 permission_repo=denied
```

because both source and target variables are explicitly frozen.

Coupling rule 2 is conditionally executable:

```text
C03 repo=changed
→ C05 mobility_requirement_A=urgent
```

but only after a valid C03 transformation has produced `repo=changed`.

Since Fixture 001 does not specify that transition, the composed C01→C03→C05 sequence MUST remain blocked.

This is an implementation specification finding, not an empirical finding.

## 8. Baseline adapter

Each baseline receives exactly the same frozen information as the TGCV representation.

The adapter may construct:

- C01 finite-state feasible-action representation;
- C03 actor/permission/tool capability representation plus workflow state;
- C05 constrained-feasibility representation;
- cross-domain directed dependency graph.

The adapter must not add information to either representation.

No aggregate superiority metric is permitted.

## 9. Required adapter manifest

The executable adapter should expose, for each transformation:

```json
{
  "transformation_id": "...",
  "predicate_source": "Fixture-001",
  "affected_variables_status": "DERIVED|EXPLICIT-IMPLEMENTATION|MISSING",
  "affected_variables": [],
  "transition_status": "DERIVED|EXPLICIT-IMPLEMENTATION|MISSING",
  "transition_operator": "...",
  "traceability": "..."
}
```

For the C03 repository transition the manifest must explicitly contain `MISSING`; it must not fabricate an operator.

## 10. Gate conditions

The adapter may proceed to executable TSTC only if:

1. every required transformation has a non-missing effect declaration;
2. every required transition operator is explicit and deterministic;
3. undeclared mutations are rejected;
4. C01→C03 coupling is executable;
5. the required C03→C05 source transition is executable;
6. baseline parity is verified;
7. negative controls remain `ΔT_acc=∅`;
8. fixture digest remains identical to Fixture Freeze 001.

Failure of any condition means **BLOCKED**.

## 11. Versioning rule

If the missing C03 repository transition must be supplied by specifying a new semantic transformation effect, then Fixture Freeze 001 cannot be silently amended.

The correct sequence would be:

```text
Adapter audit
  ↓
semantic gap confirmed
  ↓
new fixture specification/version proposed
  ↓
new authorization
  ↓
new preflight
  ↓
new execution
```

No result from Fixture 001 may be retroactively reinterpreted as evidence for a later fixture version.

## 12. Current disposition

**Fixture 001:** unchanged.

**TSTC v001:** bounded local accessibility execution retained as partial observation.

**TSTC v002:** BLOCKED by empty effect declarations and missing C03 repository-state transition semantics.

**Next controlled action:** implement an adapter-audit script that emits the manifest above and verifies which fields are DERIVED, EXPLICIT-IMPLEMENTATION, or MISSING. It must not execute the TSTC trajectory.

## 13. Non-claims

This specification establishes no scientific validity, empirical causality, superiority, generality, value, deployment, ROI, or `ΔT_acc → ΔV` claim.

No TGCV Core, RMA, Evidence→Claim Matrix, C09, C10, or industrial authorization status changes.
