# TGCV TR-131 — EXACT-SOURCE SCIENTIFIC RUNNER RECONSTRUCTION DESIGN 001

**Status:** PASS — DESIGN DECISION FROZEN FOR IMPLEMENTATION
**Scientific execution:** NOT AUTHORIZED

## 1. Design objective

Replace the synthetic tau_accept/tau_defer baseline with a domain-preserving realization/selection layer operating on the exact, source-defined T_acc established by the source lock.

The design must not invent a semantic correspondence between VisitAll and Rainbow transformations.

## 2. Core design decision

X is not a transformation name.

X is a selection policy over the canonical ordered T_acc of the current domain.

The realization operator is Pi_X(S,C,T_acc,X) -> T_real, with T_real in T_acc.

The operator is domain-agnostic. Domain-specific meaning remains entirely inside the source-defined transformation object and its transition semantics.

## 3. Frozen X contrast

The minimal controlled contrast is:
- X_A = SELECT_RANK_0
- X_B = SELECT_RANK_1

where rank is computed over a canonical deterministic ordering of the source-defined T_acc representation.

X_A selects the first admissible transformation; X_B selects the second admissible transformation.

The ordering rule is frozen before execution and is independent of state outcomes, trajectory, value, or any post-execution observation.

No cross-domain semantic mapping is introduced.

## 4. Domain instantiation

### VisitAll

Canonical T_acc ordering:
1. move:loc-x2-y2->loc-x1-y2
2. move:loc-x2-y2->loc-x3-y2
3. move:loc-x2-y2->loc-x2-y1
4. move:loc-x2-y2->loc-x2-y3

Therefore X_A selects the first move and X_B selects the second move.

### Rainbow/SWIM

Canonical T_acc ordering uses the pinned source-defined tactic identifiers.

The minimum locked set is:
1. TIncDimmer
2. TRemoveServer

Therefore X_A selects TIncDimmer and X_B selects TRemoveServer.

No assertion is made that either tactic is semantically equivalent to a VisitAll move.

## 5. Why rank selection is admissible

The purpose of X is to test whether an external realization/selection condition can affect realized trajectory while S, C and T_acc remain fixed.

The rank policy acts only after T_acc has been constructed; does not modify S, C, T_acc, admissibility or transition rules; selects an actual member of T_acc; is independently reproducible; and is defined before observing H.

The intended causal ordering is: (S,C,T_acc) -> X -> T_real -> H.

## 6. Required runner architecture

1. LOAD_SOURCE_LOCK
2. CONSTRUCT_CANONICAL_STATE
3. CONSTRUCT_CANONICAL_CONTEXT
4. CONSTRUCT_T_ACC
5. CANONICALIZE_T_ACC
6. VERIFY_T_ACC_INVARIANCE
7. DECLARE_X
8. SELECT_T_REAL
9. APPLY_SOURCE_DEFINED_TRANSITION
10. RECORD_TRACE
11. DERIVE_H
12. COMPARE_A_B

The runner must fail closed if X is applied before T_acc is frozen or if the selected transformation is not a member of T_acc.

## 7. Critical implementation constraint

The current source-lock JSON is sufficient for selection and integrity preflight, but not sufficient by itself to execute authentic domain transitions.

The scientific runner must therefore either invoke the pinned source-domain transition implementation, or include a separately frozen, source-derived executable representation of the transition function whose provenance and transformation-level semantics are independently auditable.

Until one of these is available, scientific execution remains blocked.

## 8. Required trace

Each realized transition must expose: case_id, step, S_t, C_t, T_acc_t, T_acc_hash, X_t, selected_rank, T_real_t, S_t1.

The trace must prove same S0, same C, same T_acc, distinct X, T_real in T_acc, deterministic selection, resulting state from the source-defined transition, and trajectory H derived from trace.

## 9. Primary outcome

Use the already specified exact trajectory criterion: H_A = H_B or H_A != H_B, where H is the canonical realized-transformation sequence.

No value metric is introduced.

## 10. Design gate result

EXACT-SOURCE SCIENTIFIC RUNNER RECONSTRUCTION DESIGN: PASS

The synthetic tau_accept/tau_defer abstraction is retired for the new package.

The replacement is a domain-neutral rank-based selector operating only over source-defined T_acc.

However, scientific execution remains NOT AUTHORIZED because authentic source-defined transition execution is still required.

## 11. Next gate

SOURCE-DEFINED TRANSITION EXECUTION ADAPTER AUDIT

Determine the minimum auditable mechanism for applying the selected VisitAll and Rainbow transformations using their pinned source semantics, without reconstructing or inventing transformation effects.