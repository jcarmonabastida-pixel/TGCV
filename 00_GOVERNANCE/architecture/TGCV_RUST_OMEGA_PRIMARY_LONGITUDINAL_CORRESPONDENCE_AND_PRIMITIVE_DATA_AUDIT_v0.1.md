# TGCV — Rust Ω-Primary Longitudinal Correspondence and Primitive Data Audit v0.1

**Status:** CLOSED — PRIMITIVE LONGITUDINAL BASIS CONDITIONALLY AVAILABLE / Ω-PRIMARY NOT ADMITTED
**Date:** 2026-10-01
**Gate:** RUST_OMEGA_PRIMARY_LONGITUDINAL_CORRESPONDENCE_AND_PRIMITIVE_DATA_AUDIT
**Predecessor:** RUST_OMEGA_PRIMARY_STATE_REDUCIBILITY_AND_NON_CIRCULARITY_AUDIT_v0.1

## 1. Audit question

Can adjacent Rust observations support a frozen longitudinal construction of Ω_T,t = (U_t, ≡_T, R_t) from primitive, pre-outcome records, without using accessibility or downstream outcome to establish correspondence?

## 2. Primitive observational basis

The candidate Rust route has a plausible primitive basis:
- package/crate identity;
- release/version identity;
- release timestamps;
- dependency declarations;
- dependency target identity/version information where retained.

These are observational records of the software ecosystem. They are not, by themselves, outcome measurements.

## 3. Longitudinal snapshots

A longitudinal Ω snapshot requires a frozen temporal boundary. The same construction must be applied at t and t+1, independently of successful execution, downstream outcome, accessibility, future trajectory, or value/reward/utility.

## 4. Correspondence κ

κ must not be defined from transformations that remain accessible or are executed at both times. Correspondence must be established from stable transformation-defining identifiers.

For τ = (origin_version_id, target_package_id, target_version_id), distinguish component correspondence, transformation correspondence, new transformation, and removed transformation. No category may use accessibility or outcome.

## 5. Primitive relation observations

Dependency declarations remain a candidate primitive source for R_t. Relation records require source, target, frozen relation type, provenance and observation time. The relation must not be reconstructed from successful builds, executed upgrades, observed failures, downstream performance or accessibility.

## 6. Representation invariance

The frozen ≡_T canonicalisation must be applied before longitudinal comparison. Canon_T(Raw_t) → U_t and Canon_T(Raw_t+1) → U_t+1; κ then operates on canonical identities.

## 7. Missingness and disappearance

Absence from a snapshot is not automatically structural disappearance. The protocol must distinguish observed presence, observed absence under complete coverage, unknown/missing observation, and not-in-scope. A coverage/completeness rule must therefore be frozen before interpreting U_t+1 \ U_t or U_t \ U_t+1 as structural appearance/disappearance.

## 8. Accessibility firewall

The construction of κ, U_t, ≡_T and R_t must not consult accessibility. Accessibility remains derived: T_acc,t = F(Ω_T,t,S_t,C_t,L_t). Reach and ΔReach remain derived quantities and are not admissible inputs to κ.

## 9. Audit finding

The Rust data model provides a conditionally adequate primitive basis for longitudinal Ω construction. Unresolved items are: fully frozen temporal coverage policy; fully frozen transformation-level κ rule; complete missingness/coverage convention; empirical test against inherited A reconstruction; and raw-data audit establishing that primary Ω fields precede outcome observation.

**PRIMITIVE LONGITUDINAL BASIS: CONDITIONAL PASS.**

**Ω-PRIMARY EMPIRICAL ADMISSION: NOT GRANTED.**

## 10. Architectural significance

This strengthens the candidate route by identifying a plausible source of longitudinal structural observations independent of outcome. It does not establish irreducibility to the inherited architecture.

Candidate primitive structure ≠ demonstrated architectural irreducibility.

## 11. Disposition

No fixture is created. No scientific execution is authorized. Core remains unchanged. Evidence→Claim Matrix remains v1.44. RMA remains v3.37.

**Next gate:** RUST_OMEGA_PRIMARY_COVERAGE_AND_KAPPA_FREEZE_REVIEW