# TGCV — Rust Potential Reach Successor Semantics Gate v0.1

**Status:** PASS — SUCCESSOR SEMANTICS FROZEN FOR STRUCTURAL REACH IMPLEMENTATION

## Purpose

Resolve the successor-semantics defect detected in the first Reach implementation attempt before any further execution.

## Decision

The selected successor is **configuration replacement**, not a no-op and not an observed package-version execution.

For a focal configuration `C` and an accessible transformation `τ=(e_o,p_d,v_d)`, the successor is defined by replacing the focal declaration for target package `p_d` with a canonical target-version assignment `v_d`:

`Succ(C,τ) = C \ {(p_d, *)} ∪ {(p_d,v_d)}`

where `*` denotes any prior resolved structural assignment for the same target package.

This operation represents a **potential structural configuration**. It does not assert that Cargo executed, resolved, built, or successfully used the dependency.

## Identity separation

Transformation identity remains:

`τ_id=(origin_version_id,target_package_id,target_version_id)`.

Declaration text is not part of identity.

The successor is therefore capable of changing when `target_version_id` differs from the currently assigned target version, while preserving transformation identity independently of declaration text.

## Important limitation of available data

The dataset records dependency declarations but does not record historical resolver-selected target versions. Consequently the initial configuration cannot be reconstructed as an observed resolved Cargo lockfile configuration.

Therefore the implementation must use an explicitly labelled **declaration-induced potential configuration**, not a claim about the actual resolved configuration.

If a deterministic target assignment cannot be established without importing resolver behavior absent from the dataset, the corresponding successor must remain `NOT_RECONSTRUCTABLE` rather than being fabricated.

## Closure depth

The first implementation is authorized only at **depth 1**:

`Reach¹(C) = {C} ∪ {Succ(C,τ) | τ ∈ T_acc(C) and Succ is reconstructable}`

No recursive multi-step closure is authorized by this gate.

This prevents the implementation from silently importing missing execution/resolution semantics. A future recursive Reach gate would be required for depth > 1.

## Reach distinction

`T_acc` is the set of currently accessible transformations.

`Reach¹` is the set of potential structural configurations obtainable by applying one accessible transformation under the frozen successor operation.

Thus:

`T_acc ≠ Reach¹`.

## Empty and unresolved cases

- Empty `T_acc` yields `{C}` for the bounded potential Reach object.
- Unsupported requirements remain `UNSUPPORTED`.
- Unresolved candidate identity remains `UNRESOLVED`.
- Neither is silently converted to inaccessible, executed, or reachable.

## Falsifiers

**F-S1:** no deterministic structural replacement can be defined without unsupported resolver assumptions.

**F-S2:** the successor operation is invariant under every transformation, making Reach identical to the initial configuration for all valid cases.

**F-S3:** successor construction requires observed execution or outcome information.

**F-S4:** depth-1 Reach cannot be represented deterministically and reproducibly.

**F-S5:** Reach collapses analytically into T_acc membership.

## Gate criteria

| Criterion | Status |
|---|---|
| SS-G1 successor is not a no-op | PASS — frozen by definition |
| SS-G2 configuration replacement semantics | PASS |
| SS-G3 transformation identity independent of declaration | PASS |
| SS-G4 execution/result separation | PASS |
| SS-G5 resolver semantics not silently imported | PASS |
| SS-G6 depth-1 boundary | PASS |
| SS-G7 empty/unresolved handling | PASS |
| SS-G8 actual implementation validation | OPEN |
| SS-G9 Reach computation | OPEN |
| SS-G10 ΔReach | OPEN |
| SS-G11 trajectory | BLOCKED |
| SS-G12 outcome/model/value | BLOCKED |

## Integrity lock

`Core_ontological = S` unchanged.

`T_acc` remains derived analytical object and `ΔT_acc` remains the primary differentiated candidate.

R* v0.2, temporal pairing, accessibility predicate, SLR-1, and prior EXT-1.1 outcome/model results remain unchanged.

No scientific conclusion is drawn from the failed implementation attempt.

## Next controlled operation

**TGCV Rust Potential Reach Structural Audit v0.2 — Depth-1 Configuration Successor Validation**

This must first validate that the frozen successor produces non-trivial deterministic successors on the actual dataset. Only after that validation may Reach_t0/Reach_t1 and ΔReach be considered for computation.
