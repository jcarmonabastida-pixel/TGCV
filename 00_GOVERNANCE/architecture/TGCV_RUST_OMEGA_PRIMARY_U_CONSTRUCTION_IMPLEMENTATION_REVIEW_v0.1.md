# TGCV — Rust Ω-Primary U Construction Implementation Review v0.1

**Status:** CLOSED — EXISTING CODE NOT ADMITTED AS Ω U_t IMPLEMENTATION / NEW IMPLEMENTATION SPECIFICATION REQUIRED
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_U_CONSTRUCTION_IMPLEMENTATION_REVIEW

## 1. Audit scope

The existing Rust codebase was inspected for an implementation that directly materializes the frozen Ω-primary U_t contract.

The existing `03_EXPERIMENTS/EXT-1.1_Rust/src/identity_recovery.py` is an identity-recovery helper for a different bounded task. It reads current crates.io database material and performs historical identity cross-checks. It is explicitly described as an acquisition aid and not confirmatory analysis.

Therefore it is **not admitted** as the Ω-primary U_t implementation.

## 2. Why the existing helper is insufficient

The helper:

- operates on a current crates.io database dump;
- recovers current version/crate identity;
- compares against historical pairs/checksums;
- does not construct `τ=(origin_version_id,target_package_id,target_version_id)`;
- does not implement the frozen `DR-035-v0.1-ADJACENT-CREATED-AT` / `H=1` candidate rule;
- does not emit the frozen U_t provenance/coverage contract;
- does not implement the Ω canonicalisation as the primary construction.

Reusing it directly would therefore mix the old identity-recovery route with the new Ω-primary route.

## 3. Required Ω implementation

A dedicated implementation must be created against the retained historical snapshot and must:

1. read only the admitted structural members;
2. construct candidate transformations under the frozen temporal boundary;
3. emit `τ=(origin_version_id,target_package_id,target_version_id)`;
4. canonicalise deterministically;
5. preserve provenance and coverage state;
6. fail closed on unknown transformation-defining fields;
7. produce deterministic diagnostics and output hash;
8. never consult live crates.io or downstream outcomes.

## 4. Separation from previous EXT-1.1 tooling

The existing identity-recovery helper remains historical/bounded tooling and is not deleted or reclassified.

The Ω-primary implementation must be a separate governed artifact so that the new architectural object is not contaminated by assumptions from the previous route.

## 5. Decision

**EXISTING IMPLEMENTATION:** NOT ADMITTED.

**Ω IMPLEMENTATION SPECIFICATION:** REQUIRED.

**NEW CODE CREATION:** NOT YET EXECUTED BY THIS REVIEW.

**DATASET EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 6. Next gate

`RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_SPECIFICATION_REVIEW`