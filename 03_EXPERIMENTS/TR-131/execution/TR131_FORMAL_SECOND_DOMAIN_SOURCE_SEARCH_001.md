# TGCV — Formal Second-Domain Source Search 001

**Status:** CLOSED — SECOND DOMAIN IDENTIFIED; DOMAIN SELECTION REQUIRES FIXTURE AUDIT
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Search objective
Identify a second adaptive domain with explicit state/action/transition semantics and sufficient pre-realization information to derive a transformation-space representation without researcher-defined outcome semantics.

## 2. Search result
A suitable candidate is **robotic planning / adaptive robot behavior**.

Formal and benchmarked robotics/planning sources already specify finite states, actions, preconditions and transition dynamics. For example, ACPBench defines domains in terms of action applicability, state progression, reachability and state-transition reasoning across thirteen domains. citeturn0search16

RoboPlanner likewise defines a state-transition system with finite states, actions, events and a transition function for planning and execution. citeturn0search13

Earlier work on incremental adaptation of reactive robotic systems explicitly formalizes how a planner modifies a reactive system under changing goals/environment, with mathematically analyzable modification rules. citeturn0search0turn0search7

These properties make robotics/planning materially more suitable for the current representation test than the previously selected qualitative organizational case.

## 3. Why this solves the previous blockage
The candidate domain supplies the missing operational ingredients:

- explicit state representation;
- explicit action/transformation vocabulary;
- applicability/preconditions;
- successor-state rules;
- plan/realization sequence;
- explicit temporal progression;
- in some sources, adaptation/modification rules.

These are sufficient to derive a candidate accessibility space from pre-realization applicability conditions without observing the selected action or later outcome.

## 4. Critical qualification
Robotics/planning is close to existing state-transition and planning formalisms. This is not a weakness for the test; it is a useful stress test.

If TGCV cannot demonstrate representational gain in a domain where action/state semantics are already explicit, the cross-domain claim becomes substantially weaker.

Conversely, if T_acc dynamics exposes a reproducible distinction even here, that is stronger evidence than obtaining the result from a loosely specified organizational case.

## 5. Proposed domain pair
Retain the two-domain architecture as:

**Domain A:** self-adaptive software/system configuration.
**Domain B:** formal robotic planning/adaptation.

Organizational transformation remains a secondary qualitative comparison, not a primary experimental fixture.

## 6. Fixture-source hierarchy
Primary candidates for Domain B:

1. ACPBench — explicit action applicability, progression, reachability and state-transition domains. citeturn0search16
2. RoboPlanner — explicit finite state-transition formalization for planning/execution. citeturn0search13
3. Lyons & Hendriks — formally analyzed incremental adaptation of a reactive robotic system. citeturn0search0turn0search7

These sources should not be mixed into a single fixture. One source/domain model must be selected and frozen before construction.

## 7. Important methodological consequence
The new domain makes the test more demanding:

`T_acc` may be mathematically equivalent to an applicable-action set in the source model.

That equivalence must be tested rather than assumed away.

The representation test should therefore include a **null comparator condition** in which:

`T_acc ≡ applicable-actions`

and determine whether the proposed TGCV analysis nevertheless yields information about changes in future accessibility that the ordinary model does not expose.

If it does not, the result should be FAIL — NO DISTINCT REPRESENTATIONAL GAIN.

## 8. Decision
The previous second-domain source blockage is resolved.

Scientific execution remains unauthorized.

No fixture is frozen yet.

No TGCV Core/RMA/Evidence→Claim Matrix modification is authorized.

## 9. Next gate
**DOMAIN B SOURCE SELECTION AND FIXTURE EXTRACTION AUDIT**

Select one formal robotics/planning source, extract a minimal finite fixture, document every source-to-fixture mapping, derive T_acc mechanically from pre-realization applicability, and audit the result before constructing Domain A.