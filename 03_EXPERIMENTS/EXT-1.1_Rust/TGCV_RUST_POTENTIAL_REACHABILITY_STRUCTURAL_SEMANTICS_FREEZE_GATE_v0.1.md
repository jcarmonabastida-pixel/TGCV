# TGCV — Rust Potential Reachability Structural Semantics Freeze Gate v0.1

**Status:** RECONSTRUCTED / WORKING

## 1. Purpose

Freeze an outcome-blind, non-circular, structural definition of **potential Reach** for the Rust instantiation, using only the already accepted transformation-accessibility representation and observable dependency graph semantics.

This gate does not claim to reconstruct executed dependency resolution or realized runtime trajectories.

## 2. Locked architecture

- `Core_ontological = S`
- `T_acc,t = {(e_o, τ_id) | P_τ(e_o,t)=1}`
- `ΔT_acc = T_acc,t1 ≄ T_acc,t0`
- `Reach` is downstream from `T_acc`.
- `Trajectory` remains distinct and is not directly reconstructed from the present dataset.
- `I` remains explanatory, not primitive.
- R* v0.2 remains frozen.
- SLR-1 and TR-130–TR-140 remain closed.

## 3. Reach concept

For this gate, **potential Reach** means the set of package-version configurations that are structurally obtainable through finite admissible dependency transformations under frozen semantics.

The word *potential* is essential: membership represents structural possibility, not observed execution.

Formally, for a focal state `S_t`:

`Reach_t = {s' | exists finite sequence (τ_1,...,τ_n), each τ_i is accessible under the frozen transition semantics, and the sequence maps S_t to s'}`

The implementation must define the transition function and admissibility conditions before computing Reach.

## 4. Rust transition boundary

The current dataset directly observes:

- package/version identity;
- declared dependency relations;
- target package/version identity;
- SemVer constraints;
- release chronology.

It does not observe runtime resolution events.

Therefore the permitted structural transition is a **counterfactual dependency-configuration transition**, not an execution event.

A candidate transition may be represented as:

`τ(e_o,p_d,v_d)`

where the candidate is already fixed by the frozen transformation identity and its accessibility is determined by the frozen Rust predicate.

No later selected dependency, build result, execution trace, or outcome may be used to establish Reach membership.

## 5. Non-circularity requirements

Reach must satisfy all of the following:

1. candidate transformation identity is fixed independently of Reach;
2. accessibility is fixed independently of Reach;
3. Reach is computed from present structural conditions and frozen transition semantics;
4. future observed behavior is not used to define Reach;
5. outcome/value are not used to define Reach;
6. the transition closure cannot use its own result as an accessibility condition.

## 6. Candidate construction

The candidate universe remains inherited from the accepted Rust transformation contract and is not redefined by this gate.

For the Reach test, each candidate transformation must have:

- stable origin package-version identity;
- stable target package/version identity;
- independently evaluated accessibility;
- deterministic successor representation.

If a successor state cannot be represented without importing execution or outcome semantics, the corresponding Reach construction must be marked **NOT RECONSTRUCTABLE** rather than approximated silently.

## 7. Reach levels

- **R0 Direct:** observed transition/reachability semantics.
- **R1 Reconstructed:** deterministic reconstruction from explicitly observable structural records.
- **R2 Partial:** structurally coherent counterfactual/potential reachability reconstructed from frozen semantics but not directly observed.
- **R3 Proxy:** indirect substitute; insufficient for a primary identity claim without separate validation.

The present Rust dataset is expected to support at most **R2 potential Reach** unless additional structural evidence is discovered.

## 8. Required distinction from T_acc

The test must preserve:

`T_acc ≠ Reach`

A transformation can be accessible without producing a unique new reachable state because an alternative transformation may already reach the same state.

Therefore the audit must distinguish:

- `ΔT_acc ≠ 0, ΔReach = 0`;
- `ΔT_acc ≠ 0, ΔReach ≠ 0`;
- `ΔReach ≠ 0, ΔT_acc = 0` where changed initial/context conditions permit it.

No universal implication is claimed.

## 9. Required temporal comparison

Use the already frozen focal pairing:

`t0 = origin package-version timestamp`

`t1 = next release timestamp of the same focal package`.

Where a valid potential Reach representation exists:

`ΔReach = Reach_t1 ≄ Reach_t0`.

Terminal focal versions remain excluded from paired temporal analysis.

## 10. Primary structural tests

### PR-G1 — Transition closure

Can a finite closure from the focal structural state be defined without execution data?

### PR-G2 — Non-circular accessibility

Does every transition used in the closure inherit accessibility independently from Reach?

### PR-G3 — Deterministic successor

Can the successor configuration be represented deterministically from a candidate dependency transformation?

### PR-G4 — T_acc / Reach distinction

Can two accessible transformations be represented as distinct alternatives even when they yield the same successor state?

### PR-G5 — ΔT_acc / ΔReach distinction

Can a change in accessible transformations be represented without assuming an identical change in reachable states?

### PR-G6 — Coverage

Can the construction operate on a bounded resolved subset while explicitly preserving unresolved cases?

### PR-G7 — Execution firewall

Is observed or inferred execution absent from the definition?

## 11. Strong falsifiers

**F-PR1:** potential Reach cannot be defined without importing observed execution or future outcome.

**F-PR2:** the successor state is not deterministically reconstructable from the frozen structural representation.

**F-PR3:** Reach membership is circularly required to define accessibility.

**F-PR4:** every change in T_acc necessarily produces the same Reach change, eliminating the analytical distinction.

**F-PR5:** Reach collapses into the existing T_acc membership relation under correct semantics.

**F-PR6:** unresolved/unsupported cases cannot be preserved without silent recoding.

**F-PR7:** only an outcome-derived or execution-derived proxy can be constructed.

## 12. Gate criteria

| Criterion | Status |
|---|---|
| PR-G1 potential Reach explicitly defined | PASS — protocol |
| PR-G2 Reach independent of outcome | PASS — protocol |
| PR-G3 accessibility independent of Reach | PASS — protocol |
| PR-G4 transition identity independent of Reach | PASS — protocol |
| PR-G5 T_acc ≠ Reach preserved | PASS — protocol |
| PR-G6 ΔT_acc / ΔReach distinction specified | PASS — protocol |
| PR-G7 temporal pairing inherited unchanged | PASS |
| PR-G8 deterministic successor semantics | OPEN — implementation feasibility |
| PR-G9 finite closure reconstructability | OPEN |
| PR-G10 bounded empirical ΔReach reconstruction | OPEN |
| PR-G11 execution exclusion | PASS |
| PR-G12 outcome/value/model exclusion | PASS |
| PR-G13 universal Reach law | NOT CLAIMED |
| PR-G14 causal ΔT_acc → ΔReach | NOT CLAIMED |

## 13. Decision

**PASS — POTENTIAL REACHABILITY SEMANTICS FROZEN FOR A BOUNDED RUST STRUCTURAL TEST; IMPLEMENTATION FEASIBILITY REMAINS OPEN.**

This gate authorizes only a subsequent implementation-feasibility audit. It does not authorize outcome/model execution and does not treat potential Reach as observed execution.

## 14. Integrity lock

- Core `S` unchanged.
- T_acc remains derived.
- ΔT_acc remains primary differentiated candidate.
- Reach is downstream and potentially R2.
- Trajectory remains blocked pending independent sequence semantics.
- R* v0.2 unchanged.
- No outcome/model/value variables.
- No post-hoc semantics.
