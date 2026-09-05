# N-R8.2.5 — C Identifiability Re-analysis v0.1

**Status:** PROPOSED — DESIGN BLOCKER
**Date:** 2026-09-05
**Parent:** N-R8.2 Operationalisation Specification v0.1
**Supersedes for N-R8-C design:** N-R8.2.3 and N-R8.2.4

## 1. Trigger

The bounded N-R8.4 conformance runner was executed against the amended C design and returned:

`FAIL r8c_full_r_inequality_fixture: NO_C_FIXTURE_FOUND_WITHIN_64_EDGE_SUBSETS`

All other conformance checks passed. Full pair-corpus generation was not performed.

This failure is not treated as evidence against H1-N. It is a design-identifiability failure that requires resolution before any corpus construction.

## 2. Re-analysis of the amended key

The N-R8.2.3 amendment removed explicit graph edge-count equality from `K_C*`, while retaining R2 family cardinality equality.

That does **not** leave edge count free under the frozen Branch N representation.

In N-R1.3 v0.2, the R2 family-cardinality vector contains the cardinality of `REMOVE_EDGE`. Therefore equality of R2 already fixes the number of existing edges. It also fixes the cardinality of `ADD_EDGE` and `REWIRE_EDGE` for a fixed component set under the frozen transformation universe.

Consequently, removing a separately repeated `edge_count` term from the key does not create the intended residual degree of freedom. The amended key remains effectively constrained by R2.

## 3. Stronger identifiability result

Under the current frozen Branch N semantics and current 58-dimensional R definition, the full R vector is determined by quantities already fixed by `K_C*`.

Specifically:

1. R1 is fixed by R-family availability.
2. R2 is fixed by R-family cardinality.
3. R3 is fixed by the matched component-incidence features.
4. R4 coordinates 1–7 repeat R2 family/resource-direction counts and are therefore fixed.
5. R4 coordinate 8 (`n_noop`) is identically zero because every valid transformation changes the state under N-R1.2.
6. R4 coordinates 9 and 13–14 are determined by component count and component-transform family counts already fixed by the key.
7. R4 coordinates 10 and 15–16 are determined by edge count and edge-transform family counts, with edge count already fixed by R2 cardinality.
8. R4 coordinate 11 is determined by the fixed resource tuple and resource transformation semantics.
9. R4 coordinate 12 (`len(set(next_states))`) is determined by the injective mapping from valid canonical transformations to successor states in the frozen transformation universe; equivalently, it is fixed by `|T_acc|` for this representation.

Therefore, for any two states satisfying the current `K_C*` equality, the complete 58-dimensional R vector is also equal. The required condition `R(A) != R(B)` is structurally impossible, not merely absent from the tested 3-component fixture.

## 4. Consequence

The N-R8-C design is currently **non-identifiable / impossible under the present R definition**.

The failure must NOT be solved by:

- enlarging the fixture search space;
- increasing the 64-subset limit;
- increasing the corpus budget;
- weakening the full-R inequality;
- fabricating an exception;
- using outcomes, learner results, trajectories, or N-R7 results to select a pair.

Such actions would not resolve the underlying specification problem.

## 5. Required scientific design decision

A new C design must change at least one of the following at the specification level:

### Option A — Redefine the matched low-order key

Remove one or more R-derived constraints (for example some R2/R3 components) so that a genuine residual degree of freedom remains, while explicitly revising the scientific claim about what is controlled.

### Option B — Extend the authoritative R representation

Introduce pre-specified higher-order structural features that are not deterministic functions of the existing R1–R4 summaries. This requires a new R specification and its own identifiability analysis before use in C.

### Option C — Redesign N-R8-C around an independent representation

Use an independently specified representation of `T_acc`/structural organisation as the primary contrast, rather than requiring inequality in the current 58-dimensional R. Any such redesign must preserve pre-execution specification, determinism, leakage exclusion, and independent validation.

No option is selected by this document. Selection requires an explicit scientific-design decision.

## 6. Status and gate

- N-R8.2.2: superseded for C design by this re-analysis.
- N-R8.2.3: superseded for C design by this re-analysis.
- N-R8.2.4: superseded for C design by this re-analysis.
- N-R8-C: **BLOCKED — NON-IDENTIFIABLE UNDER CURRENT R DEFINITION**.
- N-R8.3: **BLOCKED** pending a new C specification.
- N-R8.4: **BLOCKED**.
- Full 5,000-pair corpus: **NOT GENERATED**.
- Scientific execution: **NOT PERFORMED**.
- N-R7: **INTACT / UNMODIFIED**.

The next authorized action is a new N-R8-C scientific design amendment. No corpus generation is authorized until that amendment passes identifiability and conformance review.
