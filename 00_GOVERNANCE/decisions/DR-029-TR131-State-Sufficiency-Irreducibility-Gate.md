# DR-029 — TR-131 State Sufficiency / Transformational-Space Irreducibility Gate v0.1

**Status:** PROPOSED — EX-ANTE DESIGN / NO EXECUTION AUTHORIZED
**Date:** 2026-09-07
**Scope:** EXT-1.1 Rust / TGCV Core integrity
**Predecessors:** TR-130; DR-018; DR-028

## 1. Purpose

Determine whether the Rust empirical program can test the distinctness of `T_acc` from a conventional state representation without using predictive superiority as the criterion.

DR-029 is a design gate only. It does not execute the test and does not alter the accepted interpretation of EXT-1.1.

## 2. Discriminating question

Can two admissible system states that are equivalent under the candidate conventional state representation nevertheless differ in their accessible transformation space `T_acc`, under the frozen Rust transformation definition?

If yes, the candidate state representation is insufficient to determine `T_acc` and provides evidence that `T_acc` is not reducible to that representation. If no, the tested state representation is sufficient for `T_acc`; this would constitute evidence against irreducibility for that representation, not against TGCV universally.

## 3. Theoretical criterion

The test must distinguish:

- **state sufficiency:** the candidate state representation uniquely determines the accessible transformation set;
- **transformational-space irreducibility:** the accessible transformation set contains information not recoverable from the candidate state representation alone.

Cardinality alone is insufficient. Equality of counts does not establish equality of transformation spaces, and unequal counts do not by themselves establish non-redundancy if the candidate state already encodes the same membership information.

## 4. Candidate state representation

The candidate representation must be fixed ex ante from the already established Rust operational specification. No representation may be selected, expanded, or removed because it improves separation after inspecting the test results.

The test must explicitly document the mapping from the candidate state representation to the corresponding Rust system state and must not silently incorporate `T_acc`, `Reach`, future activity, outcome, or post-origin information.

## 5. Required empirical construction

The eventual executor, if authorized, must construct pairs or equivalence classes of origin states satisfying the candidate state's equality criterion and then determine whether their `T_acc` membership sets differ.

The primary structural object is therefore:

`S_a ~ S_b  AND  T_acc(S_a) != T_acc(S_b)`

where `~` denotes equality under the frozen candidate state representation.

The executor must report both:

1. the number of admissible state-equivalent comparisons;
2. the number and proportion for which the corresponding `T_acc` sets differ.

The comparison must be based only on information available at the origin state.

## 6. Prohibited channels

The design must not use:

- `Y_180` or any later outcome;
- future package activity;
- downloads, adoption, or success measures occurring after the origin;
- predictive performance, LogLoss, Brier, AUC, or model selection;
- `Reach` as a substitute criterion for `T_acc` irreducibility;
- `R*` or resource predicates unless independently required by the frozen state definition;
- post-hoc sampling or selection;
- any choice made in response to the closed DR-027 result.

## 7. Relationship to prior evidence

DR-027C remains closed with its localized negative predictive result. DR-028 remains the governing interpretation boundary.

DR-029 does not seek to reverse DR-027C. It asks a different theoretical question that DR-027C was not designed to answer.

The previously accepted Reach non-redundancy evidence under DR-018 is not sufficient to establish TR-131, because Reach non-redundancy concerns the relationship among transformations and successor configurations rather than whether `T_acc` itself is determined by a candidate state representation.

## 8. Falsification / decision logic

Subject to prior acceptance of the exact candidate state representation:

- **TR-131 support for the tested representation:** at least one valid state-equivalent pair has demonstrably different `T_acc` membership.
- **TR-131 non-support for the tested representation:** exhaustive evaluation of the admissible equivalence classes finds no `T_acc` difference.
- **Indeterminate:** the state equivalence relation or `T_acc` comparison cannot be constructed without violating the frozen specification or introducing prohibited information.

No statistical significance threshold is required for this structural test. The primary evidential object is constructive counterexample versus exhaustive sufficiency under the frozen domain and representation.

## 9. Required pre-execution audit

Before any execution is authorized, a separate audit must freeze:

1. exact candidate state representation;
2. exact Rust transformation identity;
3. exact definition of `T_acc` membership;
4. admissible origin-state universe;
5. equivalence relation;
6. treatment of terminal and missing states;
7. comparison algorithm;
8. deterministic ordering and replay requirements;
9. prohibited information firewall;
10. acceptance criteria and reporting format.

## 10. Governance decision

**DR-029 remains PROPOSED pending review.**

No script, dataset extraction, confirmatory execution, or TR-131 conclusion is authorized by this document.

The next gate is **DR-029 design review and candidate-state freeze**.