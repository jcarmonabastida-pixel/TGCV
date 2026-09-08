# TGCV — RUST-DYN-2 Real Adapter / Successor Serialization Design Review v0.1

**Date:** 2026-09-08  
**Status:** CONDITIONAL PASS — SEMANTIC DESIGN ACCEPTED / IMPLEMENTATION AMENDMENT REQUIRED / REAL EXECUTION NOT AUTHORIZED

## 1. Purpose

Review the proposed real-data implementation against the historically frozen Potential Reach semantics and the current RUST-DYN-2 re-anchoring before any real computation is authorized.

## 2. Historical semantic baseline

The authoritative successor contract is:

`Succ(C,τ) = C \\ {(p_d, *)} ∪ {(p_d,v_d)}`

with a declaration-induced structural starting configuration. The successor is a potential structural configuration, not a Cargo-resolved or executed state. The historical semantic gate also requires deterministic canonicalization, preservation of multiple admissible target versions, and no silent resolver selection. 

The current RUST-DYN-2 amendment correctly reuses this semantics and retains H=1 only.

## 3. Findings

### F1 — Successor operator semantics

**PASS.**

The current synthetic `successor_config()` implements the intended replacement operation at the level of target-package assignment: remove the existing assignment for `p_d` and add `(p_d,v_d)`. This is semantically aligned with the frozen successor equation.

### F2 — Starting configuration semantics

**PASS for design.**

The real adapter must construct `C_decl(e_o,t)` from the frozen dependency declarations and supported R* semantics. It must not reconstruct a historical Cargo lockfile or import observed resolver output.

### F3 — Configuration identity completeness

**OPEN / IMPLEMENTATION BLOCKER.**

The current synthetic representation is:

`Config = ((target_package_id,target_version_id,target_version_str), ...)`.

This representation is acceptable only if the frozen empirical configuration model guarantees at most one declaration assignment per target package and if requirement/declaration multiplicity is intentionally outside configuration identity. That condition has not yet been established for the real dataset.

The historical semantic contract defines the starting configuration using declaration-level objects containing `(p_d,r)` and then explicitly permits the successor to replace the target-package declaration/assignment. Therefore a real implementation must first establish, from the dataset, whether collapsing all declarations for a package to a single target-version assignment is lossless for the intended structural identity.

If multiple dependency declarations to the same target package can coexist with distinct requirements, the current `Config` representation is lossy and cannot be used for real execution without an explicit canonicalization rule.

### F4 — No arbitrary resolver selection

**PASS.**

The implementation must preserve every admissible target version represented by `T_acc`; it must not select a maximum or otherwise single version merely because Cargo might do so.

### F5 — Transformation / successor identity separation

**PASS.**

The successor must remain a canonical configuration object and must never be replaced by the four-field transformation identity.

### F6 — Temporal population

**PASS.**

The population is already reconciled exactly with DR-035: 516,061 adjacent temporal pairs and zero timestamp ties.

### F7 — Trajectory at H=1

**CONDITIONAL PASS.**

The only defensible H=1 representation is a canonical successor collection unless the source data supplies an independent ordering among alternative successors. No arbitrary ordering may be invented. H>1 remains outside scope.

### F8 — Firewall

**PASS.**

No execution, outcome, future activity, downloads/adoption/popularity, post-origin metadata, predictive target, sampling, or value information may enter the computation.

## 4. Required implementation amendment

Before real-data authorization, create a real adapter/executor design that explicitly validates configuration cardinality and multiplicity assumptions.

Minimum requirements:

1. Read only the frozen dataset members and frozen R* semantics.
2. Construct declaration-induced `C_decl` explicitly.
3. Detect and report multiple declarations for the same target package before collapsing anything.
4. If multiplicity exists, define a canonical lossless configuration identity before execution.
5. Preserve unsupported/unresolved states according to the frozen contract.
6. Construct each `Succ(C,τ)` deterministically.
7. Verify successor differs from transformation identity as an object type/serialization.
8. Compute `Reach¹_pot` as exact canonical successor-set membership, not cardinality alone.
9. Keep Reach downstream from `T_acc`; Reach must never feed back into `Pτ`.
10. Preserve the exact DR-035 population.
11. Keep trajectory H=1 unordered unless a non-arbitrary source ordering is available.
12. Produce deterministic hashes and primary/replay-compatible output.

## 5. Decision

The semantic re-anchoring itself is accepted, but the current synthetic `Config` representation is **not yet cleared for real-data use** because its losslessness for the actual dependency-declaration population has not been demonstrated.

This is an implementation/design blocker, not a failure of the frozen Potential Reach semantics.

**REAL-DATASET RUST-DYN-2 EXECUTION AUTHORIZED: NO.**

## 6. Next controlled operation

Perform a **real-data configuration multiplicity / canonicalization audit** on the frozen dataset. The audit must be structural only and must not construct `T_acc`, `ΔT_acc`, Reach, Trajectory, outcomes, or predictive metrics. Its purpose is solely to determine whether declaration-level configuration can safely be represented by the current assignment-level canonical form or whether a richer canonical representation is required.
