# TGCV — Rust Ω-Primary Relation Vocabulary and Endpoint Construction Freeze Review v0.1

**Status:** CLOSED — DEPENDENCY RELATION CANDIDATE FROZEN / COMPLETE R_t NOT CLAIMED
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_RELATION_VOCABULARY_AND_ENDPOINT_CONSTRUCTION_FREEZE_REVIEW

## 1. Purpose

Freeze the admissible Rust primitive relation currently supported by the retained dataset, and specify how its transformation endpoints are constructed under the already frozen observational canonicalisation.

This gate does not claim that the selected relation exhausts R_t.

## 2. Admissible relation vocabulary

The sole relation type admitted for the present Rust candidate is:

`DEPENDS_ON`

It is sourced from the primitive `package_dependencies.csv` record:

`(depending_version, depending_on_package, semver_str)`

The relation is directed:

`source_version -> target_package`

The `semver_str` field is retained as provenance/constraint information for the primitive dependency declaration. It is not interpreted as an outcome, accessibility or success variable.

No other relation types are admitted at this gate.

## 3. Endpoint construction

The source endpoint is resolved from `depending_version` to the corresponding observational Rust version record using the frozen `package_versions.csv` identity fields.

The target endpoint is resolved from `depending_on_package` to candidate target releases using the frozen pre-outcome temporal registry rule.

A dependency observation therefore supplies candidate transformation-level structure only after the endpoint transformations are constructed under the frozen rule:

`τ = (origin_version_id, target_package_id, target_version_id)`

No endpoint may be selected because it is accessible, executed, successful, popular, active in the future, or associated with an outcome.

## 4. Relation record

The canonical relation record is:

`r = (τ_i, τ_j, DEPENDS_ON, provenance, observation_time)`

where `τ_i` is the source-side candidate transformation; `τ_j` is the target-side candidate transformation; `DEPENDS_ON` is the frozen relation type; `provenance` identifies the primitive dependency record; and `observation_time` is derived from the frozen temporal snapshot rule, not downstream activity.

## 5. Important semantic limitation

A single dependency declaration can identify a target package and version constraint without uniquely selecting one target release when multiple releases satisfy the constraint.

Therefore endpoint resolution must be deterministic and explicitly frozen. Where the primitive record does not uniquely identify a target release at the frozen observation boundary, the relation must remain **UNRESOLVED/UNKNOWN**, not be assigned by hindsight or by downstream accessibility.

This prevents semver resolution from silently introducing future information.

## 6. Coverage interaction

The relation is admissible only within the previously frozen coverage semantics:

- `OBSERVED_PRESENT` supports an observed relation.
- `OBSERVED_ABSENT_COMPLETE` supports absence only where completeness is established.
- `UNKNOWN_MISSING` cannot be treated as no relation.
- `OUT_OF_SCOPE` is excluded by design.

The present gate does not establish row-level completeness of the entire dependency relation universe.

## 7. Information firewall

The construction of R_t may not use:

- `T_acc`;
- Reach / `ΔReach`;
- execution status;
- build/test success;
- downstream performance;
- reward/utility/value;
- future trajectory;
- any derived variable depending on those quantities.

The pre-existing real-data preflight confirms these prohibited quantities were not constructed/read in that preflight.

## 8. Architectural status

This freezes one **candidate primitive relation vocabulary**, not the complete structural relation set:

`R_t ⊇ R_t^DEPENDS_ON`

The inclusion is conceptual; completeness is not claimed.

## 9. Decision

**RELATION TYPE:** `DEPENDS_ON` — FROZEN CANDIDATE.

**DIRECTION:** source dependency declaration → target package/release candidate.

**ENDPOINT RULE:** FROZEN IN PRINCIPLE; unresolved semver cases fail closed.

**PROVENANCE:** REQUIRED.

**COMPLETE R_t:** NOT CLAIMED.

**Ω-PRIMARY ADMISSION:** NOT GRANTED.

No fixture or scientific execution is authorized.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 10. Next gate

`RUST_OMEGA_PRIMARY_LONGITUDINAL_KAPPA_FREEZE_REVIEW`