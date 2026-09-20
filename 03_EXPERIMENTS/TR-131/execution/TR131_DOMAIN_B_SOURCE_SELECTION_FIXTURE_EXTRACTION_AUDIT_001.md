# TGCV — Domain B Source Selection and Fixture Extraction Audit 001

**Status:** PASS — DOMAIN B SOURCE SELECTED / FIXTURE EXTRACTION AUDITED
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Source selection
Selected source: ACPBench formal planning domains, using the PDDL representation underlying the benchmark.

ACPBench is constructed from formal PDDL planning domains and explicitly includes Action Applicability, Progression, Reachability and Validation tasks across 13 domains. This supplies pre-realization action applicability and state-transition semantics independently of TGCV. citeturn0search24turn0search4

## 2. Concrete fixture choice
Primary fixture: **VisitAll** domain.

Reason for selection: the domain provides a compact state/action interpretation in which a robot moves between grid locations and action applicability depends on the current location and available neighboring cells. The benchmark documentation contains explicit applicability examples for VisitAll. citeturn0search6

The fixture must be reconstructed from the underlying formal domain/problem representation, not from benchmark answers.

## 3. Canonical fixture semantics
Let the state contain at least:
- robot position;
- set of available/non-blocked cells;
- any additional VisitAll state variables required by the selected PDDL problem.

Let the transformation/action vocabulary contain the domain's movement actions.

An action is accessible at time t iff its PDDL preconditions are satisfied by the pre-realization state at t.

Therefore, for this fixture:

`T_acc,t = { a ∈ A | preconditions(a) hold in S_t }`

This is an independently defined derivation from the source formalism, not a TGCV-specific semantic invention.

## 4. Realization
`T_real,t` is the movement action selected/executed from `T_acc,t`.

The successor state is obtained from the action's declared PDDL effects.

No goal achievement, plan success, benchmark answer, or later state may be used to define `T_acc,t`.

## 5. Why this is a strong stress test
RoboPlanner and related planning formalisms already define state-transition systems with finite states/actions and explicit transition functions. citeturn0search0turn0search2

Accordingly, this fixture intentionally permits the null hypothesis:

`T_acc,t ≡ applicable-actions(S_t)`.

If the TGCV representation adds no information beyond this existing formal object, the test must return FAIL rather than relabel the action set as a TGCV construct.

## 6. Minimal test instance
A minimal VisitAll fixture should contain:
- at least four grid locations;
- at least one unavailable cell or boundary constraint;
- one initial robot position;
- at least two simultaneously accessible movement transformations;
- at least two admissible successor trajectories;
- at least one later state in which accessibility changes.

The exact PDDL problem instance must be selected and frozen from the source before scientific execution.

## 7. Required traceability
For every fixture element, record:
- source PDDL domain/problem identifier;
- source predicate/action name;
- source precondition;
- source effect;
- derived state field;
- derived transformation identity;
- derived accessibility condition;
- derived successor-state rule.

No fixture element may exist solely because it is convenient for the TGCV hypothesis.

## 8. Baseline comparator
The comparator is the source-native transition model:

`S_t → applicable action → S_(t+1)`.

The TGCV representation adds only the explicit object:

`T_acc,t = applicable actions(S_t)`

and its change over time:

`ΔT_acc,t = D(T_acc,t,T_acc,t+1)`.

Underlying source facts are identical in both representations.

## 9. Current audit result
The source-selection and extraction audit passes because:
1. the domain is independently specified;
2. applicability is pre-realization;
3. actions and effects are explicit;
4. successor states are mechanically derivable;
5. T_acc has a deterministic source-derived construction;
6. the comparator can use exactly the same source information;
7. the domain provides a natural null hypothesis in which T_acc equals the applicable-action set.

## 10. Remaining blocker
PASS here does **not** authorize scientific execution.

Before execution, the exact PDDL domain/problem instance, fixture size, representation schema, equivalence relation, ΔT_acc operator, null/control case and ambiguity case must be frozen and independently audited.

## 11. Next gate
**DOMAIN A SOURCE SELECTION AND FIXTURE EXTRACTION AUDIT**

Select a concrete self-adaptive-system model with comparable formal resolution and perform the same source-to-fixture audit. Only after both domains pass may the cross-domain representation package be constructed.