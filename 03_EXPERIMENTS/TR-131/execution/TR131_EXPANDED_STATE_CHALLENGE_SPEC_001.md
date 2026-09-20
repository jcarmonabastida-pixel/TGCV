# TGCV TR-131 — Expanded-State Challenge Specification 001

**Status:** CANDIDATE — NOT EXECUTED
**Scientific execution authorization:** NOT GRANTED
**Date:** 2026-09-20

## 1. Purpose

Test whether the realization dependence identified by TR-131 can be absorbed into an expanded state/context representation without retaining a distinct realization operator Π and without encoding the observed outcome tautologically.

This challenge is a prerequisite to any claim of irreducibility or any Core modification.

## 2. Starting evidence

TR-131 established, under its frozen construction:

(S,C,T_acc)_A = (S,C,T_acc)_B

X_A ≠ X_B

H_A ≠ H_B

This challenge does not repeat that execution. It tests whether the additional information represented by X can be incorporated into an admissible expanded representation.

## 3. Candidate expanded representations

The challenge shall test, at minimum:

### E1 — Expanded state

S' = G(S,C,X)

### E2 — Expanded context

C' = G(C,X)

A candidate G must be specified independently of the observed H, T_real, O or V.

## 4. Non-tautology constraint

A candidate representation is invalid if it encodes any of the following directly or through an isomorphic label:

- realized transformation T_real;
- trajectory H;
- final outcome;
- value;
- a post-execution classification of the case.

G may encode pre-realization information available to the system, including a policy, rule, capability, preference, constraint or other mechanism-state representation, provided that its semantics are independently defined before execution.

## 5. Sufficiency criterion

A candidate expanded representation passes the challenge only if a single deterministic realization rule can be specified as:

T_real = F(S',C',T_acc)

or an equivalent state-only formulation, with no separate X/Π input, and reproduces the admissible realization behavior of both cases.

The mapping must be defined before observing the challenge outcome.

## 6. Compression / explanatory-distinction criterion

The expanded representation must preserve the distinction between:

1. what the system is or has available before realization;
2. what transformation is realized;
3. the resulting trajectory.

A representation that simply renames policy_A, policy_B, tau_accept, tau_defer, H, or the case outcome as a state variable fails the challenge.

## 7. Counterfactual criterion

The candidate representation must support at least one counterfactual evaluation in which the same admissible pre-realization system representation is evaluated under an alternative realization condition, without inserting the observed T_real or H into the representation. If changing X necessarily changes the candidate representation only because X was copied into it, the candidate fails the absorption challenge rather than passing it.

The purpose is to test whether G represents a genuine pre-realization system condition rather than an outcome code.

## 8. Acceptance outcomes

### PASS — absorbable

A valid expanded representation satisfies the non-tautology, pre-realization, deterministic sufficiency and counterfactual criteria.

Interpretation: the TR-131 representation insufficiency survives only as insufficiency of the narrower representation (S,C,T_acc). No irreducibility of Π is established.

### FAIL — not absorbable

No admissible non-tautological expanded representation satisfying the frozen criteria can reproduce the realization dependence.

Interpretation: evidence supports progression to a formal irreducibility assessment of the realization layer.

### INCONCLUSIVE

The candidate representations cannot be evaluated without introducing post hoc information, changing the frozen construction, or leaving a material identification condition unresolved.

No Core modification follows.

## 9. Governance boundary

This specification:

- does not modify the frozen TR-131 package;
- does not authorize scientific execution;
- does not modify TGCV Core;
- does not modify RMA;
- does not modify the Evidence Matrix;
- does not upgrade the TGCV claim level.

Any execution requires a separate freeze and authorization process.

## 10. Design-audit invariants

The design audit must verify that the challenge does not make absorption trivial by construction. In particular, it must verify:

- X is not merely renamed and copied into S' or C';
- the semantics of every added component are independently defined before execution;
- the candidate representation is not defined from T_real, H, O or V;
- the counterfactual test distinguishes genuine state/context absorption from relabelling of X;
- a PASS outcome cannot be obtained solely by changing the notation used for X.

## 11. Next gate

The immediate next gate is Expanded-State Challenge Design Audit.

Only after that audit passes may a candidate challenge package be constructed and independently audited.
