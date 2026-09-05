# N-R2 — Branch N Implementation Conformance Gate v0.1

**Status:** PASS / CLOSED  
**Date:** 2026-09-05  
**Scope:** Controlled New Reconstruction (Branch N), implementation-level conformance only.

## 1. Decision

N-R2 is **PASS / CLOSED**.

The Branch N implementation `branch_n_r_v02.py` conforms to the currently frozen N-R1.2 transformation-system specification and N-R1.3 v0.2 R-encoding specification across the registered conformance checks.

This gate does **not** constitute scientific execution, historical recovery, confirmatory validation, or reproduction of historical EMP-1.1 results.

## 2. Execution record

Runner: `BRANCH_N_CONFORMANCE_RUNNER_v0.1`

Observed implementation path:
`03_EXPERIMENTS/EMP-1.1/src/branch_n_r_v02.py`

Observed implementation SHA-256:
`08fbd60b5f3edbfdc72f8d783c6dd77c415cf3feb1dba0768438a29045c578f2`

Fixture `T_acc` size: `19`

R dimension: `58`

Scientific execution: `NOT_PERFORMED`

Overall runner status: `PASS`

## 3. Conformance checks

All registered checks passed:

1. six transformation families present
2. canonical transformation ordering
3. ADD_COMPONENT transition
4. REMOVE_COMPONENT transition
5. ADD_EDGE transition
6. REMOVE_EDGE transition
7. REWIRE_EDGE transition
8. MODIFY_RESOURCE transition
9. R dimension = 58
10. same-state determinism
11. serialization determinism
12. input-order invariance
13. empty `T_acc` maps to 58 zero features
14. no no-op transformations
15. family-count completeness
16. objective exogeneity

The runner also internally exercised global transition validity, objective preservation, absence of self-loops, and absence of duplicate edges.

## 4. Scientific boundary

The following remain explicitly outside N-R2:

- no confirmatory model fitting
- no outcome generation
- no A/B/C scientific execution
- no claim that Branch N reproduces the historical EMP-1.1 implementation
- no claim of historical Cargo or Rust resolver equivalence
- no claim that the frozen historical EMP-1.1 numerical result has been reproduced

## 5. Gate consequence

The implementation/conformance blocker is closed.

The next work may proceed to the next controlled reconstruction gate, while preserving the distinction between:

`HISTORICAL` → unrecovered historical executable semantics

`SPECIFIED` → frozen protocol/specification content

`RECONSTRUCTED` → prospective Branch N operationalisation choices

`VERIFIED` → properties demonstrated by execution of the present implementation

No scientific result may be retrofitted into the Branch N specification or implementation.
