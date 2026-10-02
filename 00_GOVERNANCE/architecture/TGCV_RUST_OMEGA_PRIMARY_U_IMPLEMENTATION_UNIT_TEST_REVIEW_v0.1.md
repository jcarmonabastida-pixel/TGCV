# TGCV — Rust Ω-Primary U Implementation Unit Test Review v0.1

**Status:** CLOSED — UNIT-TEST CONTRACT FROZEN / NO EXISTING Ω TEST SUITE ADMITTED
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_UNIT_TEST_REVIEW

## 1. Audit result

The canonical repository search found no existing test suite specifically implementing the frozen Ω-primary U_t contract. Existing EXT-1.1 identity-recovery tests are not automatically reusable as Ω-primary validation.

Therefore a dedicated Ω-primary unit-test suite is required.

## 2. Mandatory test classes

Before any retained Rust dataset is processed, the new implementation must pass deterministic tests for:

1. Valid transformation construction — one valid origin/target pair produces exactly one canonical τ.
2. Canonical duplicate collapse — repeated identical primitive records produce one U identity without changing provenance diagnostics.
3. Identity failure — missing origin, target package or target version produces UNKNOWN/FAIL-CLOSED, never an inferred identity.
4. Temporal boundary — candidates exactly at the frozen boundary are handled according to DR-035-v0.1-ADJACENT-CREATED-AT; out-of-window candidates are excluded.
5. Unknown temporal information — missing/ambiguous timestamps never become an inferred candidate.
6. Coverage semantics — UNKNOWN_MISSING is not converted to absence/removal.
7. Deterministic ordering — identical inputs produce byte-identical canonical output and hash.
8. Provenance preservation — every emitted U record can be traced to its primitive source records.
9. Firewall — prohibited fields (T_acc, Reach, outcome, value, future trajectory, etc.) cannot affect U construction.
10. No live dependency — construction remains functional without external registry/network access.
11. Historical-code isolation — the Ω constructor does not use identity_recovery.py as a semantic dependency.
12. Serialization stability — equivalent runs use the same declared serialization and hash representation.

## 3. Test fixtures

Fixtures must be synthetic and minimal. They must not be copied from the real Rust snapshot and must not contain downstream outcomes or accessibility labels.

At least one fixture must distinguish valid transformation, duplicate record, missing identity, unknown temporal field, complete absence, and unknown/missing coverage.

## 4. Scientific boundary

These tests validate software conformance only. Passing them does not establish that U_t is complete, semantically correct, irreducible to the inherited representation, or empirically supports Transformational Dynamics.

No scientific execution is authorized by this review.

## 5. Decision

**DEDICATED Ω TEST SUITE:** REQUIRED.
**EXISTING TEST SUITE:** NOT ADMITTED.
**REAL DATA:** NOT TOUCHED BY UNIT TESTS.
**UNIT-TEST EXECUTION:** NOT PERFORMED.
**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 6. Next gate

`RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_TEST_FIXTURE_REVIEW`