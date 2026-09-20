# TGCV — Cross-Domain Representation Package Construction Candidate 001

**Status:** CANDIDATE — NOT FROZEN
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Purpose
Construct the minimal candidate package for testing whether explicit transformation-space dynamics adds representational information beyond source-native state/action transition formalisms.

## 2. Domain A — Rainbow self-adaptation
Source basis: Rainbow architecture-based self-adaptation. The verified source basis establishes architecture models, adaptation strategies, monitoring, applicability conditions and adaptation effects. Rainbow is an established self-adaptation framework, so its native adaptation/action semantics remain the comparator baseline. citeturn0search15turn0search17

Candidate source-derived representation:
`S_t^A = relevant pre-realization architecture/configuration state`
`A^A = source-defined adaptation operators/strategies`
`T_acc,t^A = {a ∈ A^A | Pre_A(a,S_t^A)}`
`T_real,t^A ∈ T_acc,t^A`
`S_(t+1)^A = Apply_A(S_t^A,T_real,t^A)`

Exact Rainbow example/model identifiers and source-level operator definitions remain to be inserted before freeze.

## 3. Domain B — ACPBench VisitAll
Source basis: formal PDDL planning. ACPBench is constructed from formally specified planning domains and provides action applicability, progression and reachability tasks. citeturn0academia14

Candidate source-derived representation:
`S_t^B = PDDL state`
`A^B = VisitAll movement actions`
`T_acc,t^B = {a ∈ A^B | Pre_B(a,S_t^B)}`
`T_real,t^B ∈ T_acc,t^B`
`S_(t+1)^B = Apply_B(S_t^B,T_real,t^B)`

Exact VisitAll domain/problem identifiers remain to be inserted before freeze.

## 4. Common semantic schema
Both domains instantiate:
`state → accessible transformations → realized transformation → successor state`.

The semantic mapping is cross-domain, but the source-native meanings of state, action, precondition and effect remain unchanged.

## 5. TGCV analytical view
The only additional explicit object is:
`T_acc,t`.

And its temporal change:
`ΔT_acc,t = D(T_acc,t,T_acc,t+1)`.

No additional domain information may be introduced through this notation.

## 6. Baseline comparator
The comparator is the native source model:
`S_t → applicable action → S_(t+1)`.

The comparator receives exactly the same source facts as the TGCV representation.

Primary null hypothesis:
`T_acc,t ≡ applicable source actions/operators`.

Therefore a mere renaming of applicable actions is not a positive result.

## 7. Equivalence relation
Candidate equivalence:
`T_acc,A ≡_T T_acc,B` iff the two accessibility representations induce the same set/structure of admissible transformation identities and precondition relations under the declared domain representation.

For cross-domain comparison, semantic equivalence is assessed at the role level rather than by equality of domain labels.

Before freeze, this definition must be instantiated operationally for each domain and checked for non-circularity.

## 8. ΔT_acc operator
Candidate domain-native representation:
`ΔT_acc = (Added, Removed, Retained, StructuralChange)`.

Where:
- Added = transformations accessible at t+1 but not t;
- Removed = transformations accessible at t but not t+1;
- Retained = transformations accessible at both;
- StructuralChange records declared changes in preconditions/effects or transformation relations when the domain supports them.

The operator is descriptive and does not assign value or causality.

## 9. Required test cases
The final package must include:

### C1 — Accessibility change without immediate realized change
A pre-realization state change or environmental/configuration change modifies T_acc.

### C2 — Same T_acc, different realization
Two admissible realizations from equivalent T_acc produce different trajectories.

### C3 — Realization-induced future accessibility change
A realized transformation produces a successor state with a different T_acc.

### C4 — Null/control
The transition changes state or produces a trajectory event without changing T_acc.

### C5 — Ambiguity
Source information is insufficient to determine T_acc or its change; expected result is INCONCLUSIVE.

Cases must be derived from source models and fixed before execution.

## 10. Primary comparison question
Does explicit representation of:
`T_acc,t` and `ΔT_acc,t`
preserve a reproducible analytical distinction that is absent from:
`S_t → action → S_(t+1)`?

Positive evidence requires more than visual convenience or a different notation.

## 11. Falsification
The package must return FAIL if:
- T_acc is exactly an action-set alias and ΔT_acc adds no analytical distinction;
- every claimed distinction can be reconstructed from the baseline state-transition representation;
- cross-domain mapping requires domain-specific reinterpretation;
- T_acc cannot be determined before realization;
- the result depends on post-hoc outcome/value information.

INCONCLUSIVE is mandatory when source semantics are insufficient.

## 12. Freeze blockers
The candidate package cannot yet be frozen because:
1. exact source/model identifiers for the Rainbow fixture are not recorded;
2. exact ACPBench VisitAll domain/problem identifiers are not recorded;
3. the operational equivalence relation requires a final domain-specific instantiation;
4. the final null/control and ambiguity instances have not yet been selected.

## 13. Governance
No scientific execution is authorized.
No modification to the frozen TR-131 package.
No TGCV Core/RMA/Evidence→Claim Matrix change.

## 14. Next gate
**EXACT FIXTURE IDENTIFIER AND TRACEABILITY AUDIT**

Record the exact primary source/model identifiers and derive the smallest concrete fixture satisfying the test cases without introducing researcher-defined semantics. Then audit all source-to-fixture mappings before freeze.