# TGCV TR-131 — Expanded-State Closure Decision 001

**Status:** CLOSED — PATH A EXHAUSTED
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Decision

The existing TR-131 frozen construction does not contain an independently specified pre-realization semantic variable, other than X, capable of supporting a non-tautological expanded-state/context representation.

The operational-specification gate is therefore closed as:

**PATH A — CLOSE USING EXISTING FROZEN SEMANTICS: NOT AVAILABLE.**

No further attempt shall reinterpret the existing `policy_A` / `policy_B` definitions as an independent state/context variable.

## 2. Evidence basis

The canonical frozen policy definition specifies:

- `policy_A.select = tau_accept`;
- `policy_B.select = tau_defer`;
- `selection_source = X`;
- `post_hoc = false`.

The frozen bundle and X schema likewise define X as the realization/selection policy and explicitly require that X, rather than S0, C or T_acc, carry the contrast.

Therefore, replacing X with a structure such as `decision_priority`, `preference_state`, `policy_state` or another equivalent representation would be a new semantic construction, not an absorption test over the frozen construction.

## 3. Scientific implication

The original TR-131 result remains:

- `(S,C,T_acc)_A = (S,C,T_acc)_B`;
- `X_A != X_B`;
- `H_A != H_B`.

This establishes representation insufficiency of the tested narrower representation.

It does **not** establish formal irreducibility of Pi.

The present closure decision also establishes neither PASS nor FAIL for the expanded-state scientific challenge, because that challenge has not been executable without adding new semantics.

## 4. Path B — New challenge construction

Any continuation must be a separately governed challenge that introduces an independently justified pre-realization semantic variable.

That variable must satisfy all of the following before freeze:

1. It is defined independently of the observed TR-131 H and T_real.
2. It is not merely an alias, encoding or decomposition of X introduced solely for this challenge.
3. Its semantics have a specification independent of the challenge outcome.
4. It is part of the pre-realization system description under the new challenge's declared ontology.
5. Its value can be fixed before realization.
6. A deterministic realization rule can consume it without a separate X/Pi input.
7. At least one pre-registered counterfactual can vary the new semantic condition without using observed outcomes.
8. The construction does not modify the frozen TR-131 package.

## 5. Mandatory independent justification

The new variable cannot be invented merely because it would make absorption possible.

Before a new package is constructed, its semantic source must be identified and recorded as one of:

- an independently specified system property;
- an independently specified policy/rule parameter with semantics not defined by observed realization;
- an independently specified capability, constraint, preference or mechanism variable;
- another explicitly justified pre-realization construct.

If no such source can be justified, the expanded-state programme stops at the current representation-insufficiency result and proceeds instead to a separately designed formal irreducibility assessment.

## 6. Governance boundary

This decision:

- does not modify the frozen TR-131 package;
- does not modify the original result;
- does not authorize execution;
- does not freeze the expanded-state package;
- does not modify TGCV Core, RMA or Evidence Matrix.

## 7. Next gate

**NEW CHALLENGE SEMANTIC-BASIS GATE**

Required output:

- identify the candidate pre-realization semantic variable;
- identify its independent semantic source;
- define its admissible values;
- define how it differs from X without merely renaming X;
- define the realization rule;
- define the counterfactual;
- then perform a new design audit.

No execution is permitted before these steps.
