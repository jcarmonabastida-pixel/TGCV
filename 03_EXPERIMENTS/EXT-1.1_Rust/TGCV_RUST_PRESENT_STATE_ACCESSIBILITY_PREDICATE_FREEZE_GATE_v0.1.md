# TGCV Rust Present-State Accessibility Predicate Freeze Gate v0.1

**Status:** PASS — PRESENT-STATE PREDICATE FROZEN FOR REDESIGN IMPLEMENTATION

## Purpose

Freeze the exact Rust accessibility predicate for the selected Option A construction: fixed candidate universe plus time-varying present accessibility. The predicate is outcome-blind and uses only information available at the boundary being evaluated.

## Fixed candidate universe

For each focal package-version `e_o`, the candidate transformation identity is:

`τ_id = (origin_version_id, target_package_id, target_version_id)`.

For the structural comparison, the candidate universe is fixed independently of `t0` and `t1` from canonical dataset entities and the frozen transformation relation. The temporal boundary must not create a new transformation identity merely because a target release becomes observable later.

## Frozen present-state predicate

For boundary `t`, define:

`P_τ(e_o,t) = 1`

iff all of the following hold:

1. `e_o` is a valid canonical focal package-version;
2. `τ_id` is a valid canonical candidate transformation for `e_o`;
3. the dependency declaration linking `e_o` to `target_package_id` exists in the frozen dependency data;
4. the declaration is supported and parsable under **R* v0.2**;
5. `target_version_id` identifies the canonical target release;
6. `target_version.created_at <= t`;
7. `target_version` satisfies the declaration's frozen R* v0.2 semantics;
8. no frozen historical exclusion applies.

The predicate evaluates present accessibility at `t`; it does not evaluate whether the transformation was selected or executed.

## Important limitation of this predicate

The above predicate remains monotone with respect to target-release availability if no additional present-state condition changes over time. Therefore this gate **does not claim** that Option A alone guarantees non-monotonic `T_acc`.

The next implementation must preserve the fixed-universe architecture and may only add present-state conditions that are independently observable and scientifically justified by Rust dependency semantics. It may not introduce outcome, future selection, later focal activity or model information merely to create removals.

## R* v0.2 handling

R* v0.2 remains frozen.

Unsupported declarations are not coerced and are not silently classified as inaccessible. They are recorded as `UNSUPPORTED` and excluded from the resolved accessibility relation.

This means the structural reconstruction is explicitly bounded to the subset of dependency declarations representable under R* v0.2.

A future grammar expansion requires a separate versioned gate and cannot overwrite this contract or the prior diagnostic result.

## Temporal evaluation

At each boundary, `P_τ` may use only:

- focal package-version identity;
- target identity;
- dependency declaration present in the frozen dataset;
- target release metadata available by the boundary;
- frozen R* v0.2 semantics;
- frozen historical exclusion rules.

It must not use:

- subsequent execution;
- subsequent dependency selection;
- subsequent focal releases beyond the boundary;
- subsequent release activity as outcome;
- value;
- model predictions or fitted parameters.

## T_acc and ΔT_acc

`T_acc,t = {(e_o,τ_id) | P_τ(e_o,t)=1}`.

`Add = T_acc,t1 \ T_acc,t0`.

`Rem = T_acc,t0 \ T_acc,t1`.

`ΔT_acc` is classified from Add/Rem exactly as frozen by the temporal-pairing contract.

## Decision

**PASS — PRESENT-STATE PREDICATE FROZEN FOR REDESIGN IMPLEMENTATION.**

This is a methodological freeze, not an empirical validation.

## Integrity lock

- Diagnostic run remains immutable.
- R* v0.2 remains historically frozen.
- Core remains `S`.
- `T_acc` remains derived analytical object.
- `ΔT_acc` remains primary differentiated candidate.
- SLR-1 remains closed.
- TR-130–TR-140 remain closed.
- No outcome/model/value computation is authorized.
- No confirmatory claim follows from this gate.

## Next controlled operation

Implement a revised Rust structural audit against this predicate, first with a **shadow/diagnostic validation** of predicate behavior and coverage, before any confirmatory outcome/model protocol.
