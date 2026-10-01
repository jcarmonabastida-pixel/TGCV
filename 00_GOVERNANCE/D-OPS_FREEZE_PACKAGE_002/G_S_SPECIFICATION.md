# G_S — frozen state-only comparator

Inputs: one member of C_S for each snapshot, plus the frozen representation schema.
Forbidden: U, R1, R2, R3, perturbation labels, oracle descriptors, execution, outcomes.

C_S = {S_raw, S_typed, S_predicate_multiset, S_object_inventory}.

Output: NO_STRUCTURAL_CHANGE | STRUCTURAL_CHANGE | NON_COMPARABLE.

The comparator is deterministic and representation-specific. NON_COMPARABLE never reproduces a structural decision.
