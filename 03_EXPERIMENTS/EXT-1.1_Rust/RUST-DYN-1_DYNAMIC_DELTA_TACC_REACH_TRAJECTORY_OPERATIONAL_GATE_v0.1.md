# RUST-DYN-1 — Dynamic ΔT_acc / Reach-Trajectory Operational Gate v0.1

**Status:** PASS — DYNAMIC STRUCTURAL DESIGN FROZEN / EXECUTION NOT YET AUTHORIZED
**Date:** 2026-09-08
**Domain:** Rust package ecosystem
**Predecessor:** D-OPS-1 Rust Domain Operational Specification v0.1

## 1. Purpose

Freeze an ex-ante operational design for testing whether changes in the accessible transformation space can be represented over time and whether those changes preserve a non-degenerate analytical distinction from Reach and Trajectory.

This gate does not execute the dataset, reopen TR-131, or infer downstream effects from the completed TR-131 result.

## 2. Frozen architecture

`S_t` = package-version structural state at time `t`.

`C_t` = origin-time admissibility context.

`L` = frozen restricted resolver semantics `R* v0.2`.

`T_acc,t = {τ ∈ U_tau,t | P_tau(S_t,C_t,L)=1}`.

`ΔT_acc(t1,t2)` is the exact canonical membership difference between the two accessible-transformation sets.

Reach and Trajectory are downstream objects and are not inputs to `P_tau`.

## 3. Temporal observation design

The basic temporal unit is a pair of package-version origins belonging to the same package and ordered by creation time:

`o_i <_time o_j` iff `created_at_i < created_at_j`.

Only pairs satisfying the frozen comparability rules may be compared. Exact timestamp ties are not assigned an artificial order.

For each valid pair:

`T_i = T_acc(o_i)`

`T_j = T_acc(o_j)`

and:

`ΔT_acc(i,j) = T_j \ T_i` (expansion component)

`ΔT_acc(i,j)^- = T_i \ T_j` (contraction component)

`ΔT_acc(i,j)^↔ = T_i ∩ T_j` (persistent component).

A non-zero event exists iff either difference set is non-empty.

## 4. Dynamic event classes

Every valid temporal pair is classified into one of:

1. **PERSISTENCE:** `T_i = T_j`.
2. **EXPANSION:** `T_i ⊂ T_j`.
3. **CONTRACTION:** `T_j ⊂ T_i`.
4. **RECONFIGURATION:** neither set is a subset of the other and `T_i ≠ T_j`.

Equal-cardinality reconfiguration is retained as a first-class case.

No scalar cardinality metric can replace exact membership comparison.

## 5. Separation from ordinary state change

The test explicitly distinguishes:

- `ΔS ≠ 0, ΔT_acc = 0` — state change without accessible-space change;
- `ΔS ≠ 0, ΔT_acc ≠ 0` — state change accompanied by accessibility change;
- where observable under the frozen representation, `ΔT_acc ≠ 0` is not interpreted as a causal effect merely because it co-occurs with `ΔS`.

The gate tests representational distinction, not causal identification.

## 6. Reach operationalization

For RUST-DYN-1, Reach is defined as the set of package-version configurations reachable within a separately specified finite continuation horizon `H` by repeatedly applying transformations that are accessible under the frozen structural semantics.

Formally, for an origin `o`:

`Reach_H(o) = {s' | there exists a valid transformation sequence from S_o to s' of length <= H, with each applied τ admissible under the frozen transition rules}`.

A Reach implementation must specify transition identity, state update, admissibility at each step, duplicate handling and horizon before execution.

Crucially, Reach is **not** allowed to use observed later release activity as a substitute for the counterfactual continuation space.

## 7. Trajectory operationalization

Trajectory is the ordered structure of valid transformation/state sequences within the same finite horizon `H`.

Two origins may have the same Reach set while having different trajectory structures. Therefore trajectory comparison must retain ordered path information rather than only endpoint membership.

The first implementation must use an explicitly frozen canonical path identity and deterministic ordering. No learned or outcome-derived ranking is permitted.

## 8. Required non-degeneracy cases

The operational test must attempt to identify, without outcome information:

### R-D1 — ΔT_acc without Reach change

`ΔT_acc ≠ 0` and `Reach_H` equal.

### R-D2 — ΔT_acc with Reach change

`ΔT_acc ≠ 0` and `Reach_H` different.

### R-D3 — Same Reach, different Trajectory

`Reach_H` equal but trajectory structures differ.

### R-D4 — Same observed execution, different accessible alternatives

Two observations may share an observed/realized local result while their pre-execution T_acc sets differ. This case must not be constructed by using the observed result to define T_acc.

### R-D5 — Reach change without identical ΔT_acc

Different accessible-space changes may lead to the same Reach difference, and the same Reach difference must not be assumed to identify a unique ΔT_acc.

These are representational test cases, not requirements that the real dataset necessarily contain every class.

## 9. H-R1 / H-R3 / H-R4 decision boundaries

**H-R1:** supported if the frozen Rust population contains valid comparable temporal observations with `ΔT_acc ≠ 0`.

**H-R3:** supported only if a separately frozen Reach/Trajectory construction yields at least one valid non-degenerate association between `ΔT_acc` and Reach and/or Trajectory while preserving the definitions independently.

**H-R4:** supported only if accessible-but-unexecuted alternatives can be identified from pre-execution structural information and cannot be reconstructed solely from realized execution.

None of these outcomes is presumed.

## 10. Information firewall

The following are prohibited inputs to structural accessibility classification and to any Reach construction intended to represent counterfactual accessibility:

- future releases beyond the origin's admissible information boundary;
- downloads, adoption, popularity or success;
- future outcome variables;
- predictive targets or metrics;
- learned models trained on future outcomes;
- post-origin labels used to define admissibility;
- package identity as an unapproved equivalence feature;
- results of this experiment used to redefine `T_acc`.

Observed later releases may only be used in a clearly separated descriptive validation layer if a later gate explicitly authorizes such use. They cannot define the counterfactual accessible space.

## 11. Execution boundary

RUST-DYN-1 is a **design gate only**.

No dataset execution is authorized by this document.

A subsequent execution-authorization decision must freeze at minimum:

- exact population;
- exact temporal-pair construction;
- horizon `H`;
- Reach transition semantics;
- Trajectory canonicalization;
- computational limits;
- dataset hash;
- executor commit;
- exact command;
- output schema;
- replay requirement;
- abort conditions.

## 12. Falsifiers

The design is falsified or must be redesigned if:

1. temporal ordering cannot be defined without arbitrary assumptions;
2. `T_acc` must be reconstructed from future execution/outcome;
3. Reach collapses identically into T_acc by definition;
4. Trajectory is only a relabelled Reach set;
5. every observed state transition necessarily determines the same ΔT_acc;
6. counterfactual alternatives cannot be represented independently of observed execution;
7. missing/unsupported structural information is silently converted into accessibility;
8. downstream metrics require retroactive modification of the frozen structural specification.

## 13. Gate criteria

| Criterion | Result |
|---|---|
| R-DYN-G1 Temporal unit identifiable | PASS |
| R-DYN-G2 Exact ΔT_acc comparison | PASS |
| R-DYN-G3 Expansion/contraction/reconfiguration distinction | PASS |
| R-DYN-G4 Separation from ΔS | PASS — representational, not causal |
| R-DYN-G5 Reach independently defined | PASS — finite-horizon design frozen |
| R-DYN-G6 Trajectory independently defined | PASS — ordered-path design frozen |
| R-DYN-G7 Non-degenerate counterfactual cases specified | PASS |
| R-DYN-G8 Information firewall | PASS |
| R-DYN-G9 Execution authorization | NOT YET |
| R-DYN-G10 Empirical result | NO — design gate only |

## 14. Scientific boundary

A positive result would support only the operational distinction established by the frozen test. It would not establish causality, universal validity, predictive superiority, value creation, or originality.

A negative result would be informative: it could show that the distinction is operationally redundant or not identifiable in this domain under the frozen semantics.

## 15. Decision

**RUST-DYN-1 = PASS — DYNAMIC STRUCTURAL DESIGN FROZEN.**

The design is sufficiently specified to permit a later execution-authorization gate. No execution is authorized yet.

## 16. Next controlled operation

The next gate is **RUST-DYN-EXEC-1 — Execution Authorization Gate**, which must freeze the exact temporal population, finite horizon, Reach/Trajectory executor, dataset integrity and replay protocol before any run.