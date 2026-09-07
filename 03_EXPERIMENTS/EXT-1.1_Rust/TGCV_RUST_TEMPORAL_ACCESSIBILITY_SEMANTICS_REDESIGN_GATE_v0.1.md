# TGCV Rust Temporal Accessibility Semantics Redesign Gate v0.1

**Status:** PASS — OPTION A SELECTED; COVERAGE ISSUE SEPARATELY FROZEN

## Purpose

Select, ex ante and outcome-blind, the temporal construction for the next Rust structural validation after the diagnostic finding that the first construction was monotone.

## Starting constraint

The prior diagnostic used a target-release cutoff at `t0` and `t1` with otherwise fixed dependency declarations. Therefore it induced:

`T_acc,t0 ⊆ T_acc,t1`

and could not produce removals. This is accepted as a diagnostic result and is not retroactively changed.

## Alternatives

### Option A — Fixed candidate universe + time-varying present accessibility

Construct a fixed, independently defined `U_τ` and evaluate `P_τ` separately at `t0` and `t1` using frozen present-state conditions. A transformation may therefore become inaccessible when a present condition ceases to hold, while remaining distinct from execution.

### Option B — Time-indexed candidate validity

Allow the candidate universe itself to change over time through explicit validity conditions. This can represent additions/removals but risks conflating transformation identity/validity with historical data accumulation.

### Option C — Other construction

Permitted only with an independent formal justification, non-circularity, outcome blindness, deterministic reconstruction and ability in principle to distinguish additions from removals.

## Decision: Option A

**Selected:** fixed candidate universe + time-varying present accessibility.

### Rationale

Option A best preserves the locked TGCV distinction:

`τ exists → P_τ(S_t,C_t,L) → selection/execution → result`

It makes `ΔT_acc` a change in accessibility conditions rather than a mechanical consequence of adding later target releases to the candidate universe.

It also permits the following theoretically distinct cases without using outcome information:

1. `τ` accessible at `t0`, inaccessible at `t1` → removal;
2. `τ` inaccessible at `t0`, accessible at `t1` → addition;
3. both membership changes → reconfiguration/substitution;
4. membership unchanged → persistence.

## Required operational consequence

The next implementation must **not** define `U_τ(t)` by `created_at(target) <= t`.

Instead, `U_τ` must be fixed independently of the temporal comparison, and `P_τ(S_t,C_t,L)` must contain the explicitly frozen temporal conditions that determine accessibility at each boundary.

The exact present-state conditions must be specified in a subsequent implementation gate before execution. They must use only information available at the boundary being evaluated and must not use future execution, outcome or value.

## R* v0.2 coverage decision

R* v0.2 remains historically frozen and is not silently modified.

The diagnostic run identified `1,413,037` unsupported dependency declarations. These remain explicitly unresolved/unsupported for the current semantic contract.

**No new grammar is introduced in this gate.** A future grammar expansion, if justified, requires its own versioned ex-ante gate and cannot alter the R* v0.2 historical result.

## What this gate does NOT establish

- It does not establish that Rust exhibits contraction or reconfiguration empirically.
- It does not establish universal validity of Option A.
- It does not establish causal effects.
- It does not establish predictive superiority.
- It does not establish value creation.
- It does not alter SLR-1 or TR-130–TR-140.

## Next controlled operation

Create and pass:

**TGCV Rust Present-State Accessibility Predicate Freeze Gate v0.1**

That gate must specify the exact temporal conditions inside `P_τ(S_t,C_t,L)` required to make Option A executable without circularity or future leakage.

## Integrity lock

- Diagnostic execution remains immutable.
- Core remains `S`.
- `T_acc` remains a derived analytical object.
- `ΔT_acc` remains the primary differentiated candidate.
- SLR-1 remains closed.
- TR-130–TR-140 remain closed.
- No outcome/model/value computation is authorized.
- No rerun is authorized until the present-state predicate is frozen.
