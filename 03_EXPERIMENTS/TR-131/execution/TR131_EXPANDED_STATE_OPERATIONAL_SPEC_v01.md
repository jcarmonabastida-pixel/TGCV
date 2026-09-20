# TGCV TR-131 — Expanded-State Challenge Operational Specification v01

**Status:** CANDIDATE — OPERATIONALLY SPECIFIED / NOT FROZEN
**Scientific execution:** NOT AUTHORIZED
**Design basis:** Expanded-State Challenge Design Audit PASS
**Date:** 2026-09-20

## 1. Objective

Determine, using a pre-specified finite construction, whether the realization distinction represented by X can be absorbed into an independently defined state/context representation without:

- copying or merely renaming X;
- encoding T_real, H, outcome or value;
- using post-execution information;
- retaining X or Π as a separate input to the realization rule.

This specification is the operational closure of the challenge design. It does not authorize execution.

## 2. Inherited frozen construction

The challenge inherits the already executed TR-131 fixture only as baseline evidence:

- S0 = {node:S0, resources:1, status:ready}
- C0 = {context:frozen, version:1}
- T_acc,0 = [
  {id:tau_accept, pre:ready, post:accepted},
  {id:tau_defer, pre:ready, post:deferred}
  ]
- X_A = policy_A
- X_B = policy_B
- H_A = S0 -> tau_accept -> S1(accepted)
- H_B = S0 -> tau_defer -> S1(deferred)

The challenge does not use H_A or H_B to construct G or F. They are used only as pre-registered target behaviors for the absorption test.

## 3. Operational semantics available before realization

The only candidate information available to G is a pre-realization policy specification.

The policy specification is a structured mapping from admissible transformation identifiers to an ordered decision priority:

- policy_A: priority(tau_accept)=1; priority(tau_defer)=2
- policy_B: priority(tau_defer)=1; priority(tau_accept)=2

The policy semantics are defined before execution as a system decision rule: select the highest-priority admissible transformation.

No field contains T_real, H, final outcome or value.

## 4. E1 — Expanded-state construction

Define:

S' = G1(S,C,PolicySemantics)

where G1 appends the independently defined policy semantics to the pre-realization state as a system capability/decision structure:

S' = {
  S,
  decision_priority = PolicySemantics
}

The construction is valid only if PolicySemantics is represented by its pre-realization semantic content, not by a case label and not by the observed realization.

A representation of the form {S, X=X_A} or {S, X=X_B} is explicitly invalid.

## 5. E2 — Expanded-context construction

Define:

C' = G2(C,PolicySemantics)

where:

C' = {
  C,
  decision_priority = PolicySemantics
}

The same anti-renaming rule applies. A mere field carrying the original X identifier is invalid.

## 6. Deterministic realization rule

For both E1 and E2, the only realization rule permitted is:

T_real = F(S',C',T_acc)

F selects the admissible transformation with the highest pre-realization decision priority.

F receives no X, Π, H, outcome or value input.

If two admissible transformations have equal highest priority, F returns INCONCLUSIVE rather than resolving the tie post hoc.

## 7. Counterfactual

Before execution, the challenge defines the counterfactual:

Given the same S0, C0 and T_acc, replace the policy semantics with the independently admissible alternative priority ordering and evaluate F.

The counterfactual must be computed entirely from pre-realization representation.

A result is invalid if the counterfactual representation is produced by copying the observed T_real or H.

## 8. Acceptance test

For each candidate E1 and E2:

PASS — ABSORBABLE if:

1. G is reproducible from the specification;
2. no X identifier is copied/renamed into the representation;
3. no post-execution field enters G;
4. F uses no separate X/Π input;
5. F deterministically reproduces the registered A and B realization behaviors;
6. the counterfactual is evaluated from pre-realization semantics.

FAIL — NOT ABSORBABLE if a candidate cannot satisfy these conditions.

INCONCLUSIVE if any condition cannot be independently reconstructed.

## 9. Critical interpretation rule

A PASS does not establish that Π is irreducible. It establishes that the tested realization dependence is absorbable into an expanded pre-realization state/context representation.

A FAIL is evidence for progression to a formal irreducibility assessment.

No result alone modifies TGCV Core.

## 10. Executor-2 reconstruction requirement

Executor-2 must reconstruct independently:

- S0, C0 and T_acc,0;
- the two policy semantic structures;
- G1 and G2;
- F;
- the counterfactual;
- all PASS/FAIL/INCONCLUSIVE determinations.

Executor-2 must not receive observed H_A/H_B as construction inputs, except as the pre-registered target behaviors contained in the audit envelope.

## 11. Governance

This operational specification is not frozen and does not authorize scientific execution.

The next gate is:

**Operational Specification Audit → Package Freeze → Executor-2 Reconstruction → Freeze Audit → Explicit Authorization.**
