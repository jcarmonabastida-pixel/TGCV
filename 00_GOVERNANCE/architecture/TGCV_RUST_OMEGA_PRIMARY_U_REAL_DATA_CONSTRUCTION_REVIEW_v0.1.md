# TGCV — Rust Ω-Primary U Real-Data Construction Review v0.1

**Status:** CLOSED — CONSTRUCTION CONTRACT REVIEW BLOCKED / CODE CORRECTION REQUIRED  
**Date:** 2026-10-02  
**Gate:** RUST_OMEGA_PRIMARY_U_REAL_DATA_CONSTRUCTION_REVIEW

## 1. Review basis

The retained historical Rust snapshot has passed the real-data preflight. The dedicated constructor has also passed its synthetic test suite.

Before real-data construction, the implementation was compared against the frozen U_t contract.

## 2. Findings

### F1 — provenance completeness

The frozen contract requires origin provenance and target provenance. The current constructor emits a provenance tuple containing the dependency-row reference and target-version reference, but does not emit an explicit provenance reference to the origin version record.

**Disposition:** correction required before real-data execution.

### F2 — coverage semantics

The frozen contract distinguishes OBSERVED_PRESENT, OBSERVED_ABSENT_COMPLETE, UNKNOWN_MISSING and OUT_OF_SCOPE. The current constructor emits only OBSERVED_PRESENT records and counters for unresolved/out-of-scope inputs. It does not persist the required coverage state model as a governed construction output.

**Disposition:** correction required before real-data execution.

### F3 — output auditability

The constructor emits an output hash, counts and construction metadata, but the real-data execution protocol must persist input snapshot identity, implementation commit/version, temporal rule, coverage counts and output hash in a governed result artifact.

**Disposition:** required execution packaging, not yet an execution failure.

## 3. What is already satisfactory

- Exact historical snapshot was verified by SHA-256.
- Required structural CSVs and schemas were verified.
- Constructor uses the frozen tuple `τ=(origin_version_id,target_package_id,target_version_id)`.
- Canonicalisation is exact tuple identity.
- Temporal rule is explicitly bound.
- No live registry is used.
- Historical `identity_recovery` route is separate.
- Synthetic suite passed 11/11.
- Scientific execution remains unauthorized.

## 4. Decision

**REAL-DATA U CONSTRUCTION: NOT AUTHORIZED.**

The current constructor must be corrected and retested synthetically before any real-data construction.

No real-data rows are to be processed by the constructor under this review.

## 5. Required next gate

`RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_CORRECTION_AND_SYNTHETIC_REVALIDATION`

Only after correction and synthetic revalidation may a new real-data construction review be opened.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.
