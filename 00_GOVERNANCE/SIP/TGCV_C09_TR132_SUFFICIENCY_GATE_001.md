# TGCV — TR-132 Sufficiency Gate for C09 v0.1

**Status:** `CONTROLLED GATE — APPLIES TO C09 SCREENING / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories

## 1. Purpose

TR-132 determines whether the operational representation of the accessible transformation space is **sufficient for the specific bounded causal question under test**.

TR-132 does **not** require exhaustive observation of the complete transformation space of the system.

The relevant requirement is bounded sufficiency:

`U_tau^TR132 ⊆ U_tau^system`

with the retained representation sufficient to evaluate the prespecified causal estimand and falsification criteria for the declared unit, intervention, accessibility predicate, trajectory endpoint and horizon.

## 2. Gate principle

A candidate passes TR-132 when the available representation permits all of the following without post-treatment leakage or ad-hoc redefinition:

1. define the relevant transformation profile before treatment/outcome observation;
2. define `P_tau` independently of realized trajectory/outcome;
3. distinguish `T_acc,0` from `T_acc,1` under the intervention;
4. identify the treatment/control or counterfactual contrast;
5. reconstruct the prespecified subsequent trajectory endpoint;
6. test the causal estimand and falsification conditions;
7. establish that omitted transformations cannot alter the specific causal conclusion within the declared scope.

The last condition is a **sufficiency argument**, not an exhaustiveness claim about the entire system.

## 3. What TR-132 does not require

TR-132 does not require:

- enumeration of every transformation conceivable in the domain;
- complete reconstruction of the system-wide `T_acc`;
- observation of transformations irrelevant to the declared causal estimand;
- public availability of variables that cannot affect the tested causal contrast;
- a universal transformation ontology.

A bounded transformation profile is admissible if its boundary is frozen ex ante and its sufficiency for the causal question is demonstrated.

## 4. Required sufficiency argument

For a candidate profile `U*`:

`U* = U_tau^TR132`

TR-132 must establish that the causal estimand is invariant to admissible omissions outside `U*`, or that such omissions are proven irrelevant to the tested accessibility contrast and trajectory endpoint.

Operationally, the protocol must document:

- scope boundary of `U*`;
- why each retained transformation class is relevant;
- why omitted classes cannot create an alternative accessibility pathway affecting the estimand;
- why `P_tau` is complete within the frozen profile;
- why `T_acc,1 ≠ T_acc,0` is identified within that profile;
- why `Y` is independently defined;
- why no post-treatment information is required to establish sufficiency.

## 5. Causal non-identification / null-result use

TR-132 may support a **non-causal or null conclusion** without complete system-wide `T_acc` when the bounded representation is sufficient to exclude the tested causal pathway under the declared scope.

Conversely, a null result cannot be generalized to transformations omitted from the tested profile unless TR-132 establishes that those omissions cannot change the causal conclusion.

Thus:

`TR-132 PASS ≠ complete T_acc`

and

`TR-132 PASS ≠ universal non-causality`.

## 6. Relation to existing C09 design

The existing C09 design already requires `S0`, `C0`, frozen accessibility semantics, intervention `Z`, counterfactual identification and independently defined trajectory `Y`. TR-132 adds the missing **representation-sufficiency gate** between domain identification and causal execution.

A candidate therefore follows:

`Domain identification → TR-132 sufficiency → C09 operational preflight → execution authorization`

No candidate passes merely because a conventional randomized experiment exists.

## 7. Failure conditions

TR-132 FAIL if:

- the bounded profile omits a transformation class that could change treatment accessibility or the causal estimand;
- `P_tau` requires post-treatment information;
- `T_acc,0/T_acc,1` cannot be distinguished within the profile;
- the trajectory endpoint depends on omitted transformations in an uncontrolled way;
- sufficiency depends on an untestable narrative;
- the profile boundary is selected after inspecting outcomes;
- the result is generalized beyond the declared bounded scope.

## 8. Evidence status

TR-132 is a **methodological sufficiency gate**, not evidence for C09 itself. Passing TR-132 does not upgrade C09 and does not authorize execution.

**Execution authorization = NONE.**

## 9. Governance consequence

Historical candidate audits that were closed solely because they lacked a complete system-wide/public `T_acc` must be eligible for retrospective TR-132 review. Their original audit records remain immutable historical records; retrospective review is a new governed operation and does not erase prior dispositions.

## 10. Decision

**TR-132 = ADOPTED AS C09 SUFFICIENCY GATE.**

The C09 candidate criterion is therefore revised from:

`complete public system-wide T_acc reconstruction`

to:

`public or independently reproducible bounded representation sufficient under TR-132 to identify the declared C09 causal contrast without leakage or uncontrolled omitted-path alternatives`.

No claim-matrix upgrade follows.
No C09 causal result follows.
No execution is authorized.
