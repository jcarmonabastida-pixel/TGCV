# TGCV — Rust Ω-Primary Longitudinal κ Freeze Review v0.1

**Status:** CLOSED — κ RULE FROZEN / EMPIRICAL LONGITUDINAL ADMISSION NOT GRANTED
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_LONGITUDINAL_KAPPA_FREEZE_REVIEW

## 1. Purpose

Freeze the longitudinal correspondence rule for Rust Ω observations at the semantic level, using the existing coverage contract and observational transformation identity.

## 2. Frozen correspondence principle

Adjacent snapshots use Ω_T,t = (U_t, ≡_T, R_t) and Ω_T,t+1 = (U_t+1, ≡_T, R_t+1).

A transformation correspondence exists only when the canonical transformation identities satisfy the pre-specified persistence rule.

The rule is: κ_t(τ_t, τ_t+1) = CORRESPONDING iff the canonical transformation-defining identity is preserved under the frozen observational protocol.

Otherwise: κ_t(τ_t, τ_t+1) = NO_CORRESPONDENCE.

No probabilistic or outcome-based matching is permitted at this stage.

## 3. Identity fields

For the current Rust candidate: τ = (origin_version_id, target_package_id, target_version_id).

Therefore the default longitudinal correspondence requires equality of the canonical identity tuple.

A change in any transformation-defining identifier means NO_CORRESPONDENCE unless a separately frozen semantic correspondence rule is later admitted.

Stable package identity alone is insufficient because the origin release is part of the candidate transformation identity.

## 4. New and removed transformations

With adequate coverage: New_t = U_t+1 \ U_t; Removed_t = U_t \ U_t+1.

These are descriptive structural observations.

They do not imply that a transformation became accessible/inaccessible, was executed, succeeded, failed, or produced any outcome.

## 5. Relation longitudinal correspondence

For R_t, the endpoints must first be resolved under the frozen endpoint construction rule.

A relation is longitudinally comparable only when:

1. its relation type is identical;
2. both endpoint transformations have valid κ correspondence;
3. provenance and temporal observation are retained.

If any condition fails, relation correspondence is UNKNOWN/NO_CORRESPONDENCE, not inferred.

## 6. Missingness and coverage

The κ rule is subordinate to the frozen coverage states: OBSERVED_PRESENT; OBSERVED_ABSENT_COMPLETE; UNKNOWN_MISSING; OUT_OF_SCOPE.

UNKNOWN_MISSING cannot produce a removal or failed correspondence.

OBSERVED_ABSENT_COMPLETE may support disappearance only when completeness is independently established.

## 7. Information firewall

κ may not inspect or use T_acc; Reach / ΔReach; execution status; build/test success; downstream outcome; reward, utility or value; future activity or trajectory.

This keeps longitudinal Ω correspondence structurally prior to accessibility and outcome.

## 8. Important limitation

This gate freezes a correspondence rule, not empirical proof that the rule captures semantic persistence.

In particular, exact tuple equality may be conservative. It may fail to identify a semantically persistent transformation whose observational identifiers change. Such cases must remain unmatched rather than being repaired after seeing results.

Any future semantic correspondence rule would require a separate pre-registration and architectural audit.

## 9. Decision

**κ CONTRACT:** FROZEN.
**DEFAULT MATCHING RULE:** exact equality of frozen canonical transformation identity.
**AMBIGUOUS / MISSING CASES:** FAIL CLOSED.
**OUTCOME/ACCESSIBILITY INPUT:** PROHIBITED.
**EMPIRICAL κ VALIDATION:** NOT YET PERFORMED.
**Ω-PRIMARY DATASET ADMISSION:** NOT GRANTED.

No fixture or scientific execution is authorized.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 10. Next gate

`RUST_OMEGA_PRIMARY_RAW_DATA_ADMISSION_AND_INFORMATION_FIREWALL_AUDIT`