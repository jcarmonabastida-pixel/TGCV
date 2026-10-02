# TGCV — Rust Ω-Primary U Implementation Build Review v0.1

**Status:** CLOSED — BUILD DESIGN PASSED / IMPLEMENTATION NOT YET BUILT / DATASET NOT EXECUTED
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_BUILD_REVIEW

## 1. Build objective

Define the implementation boundary for the dedicated Ω-primary U constructor. The build must implement only the frozen U_t contract and remain independent from historical EXT-1.1 identity-recovery tooling.

## 2. Required module boundary

The implementation should have separate stages: input/archive binding; primitive schema validation; temporal candidate construction; transformation canonicalisation; coverage/missingness classification; deterministic U_t emission; provenance/manifest emission; and non-scientific diagnostics.

No accessibility, Reach, outcome or value stage belongs in this implementation.

## 3. Build invariants

The implementation must preserve `τ=(origin_version_id,target_package_id,target_version_id)`, `Canon_T(τ)=τ`, the frozen temporal rule, fail-closed unknown handling, deterministic serialization, source provenance, coverage state, and snapshot hash binding. Any deviation is a build failure rather than an analytical choice.

## 4. Dependency isolation

The new constructor must not import historical `identity_recovery.py` as a semantic dependency. Generic archive/CSV utilities may be reused only if they do not alter the frozen Ω contract. Live network access must be absent from the scientific construction path.

## 5. Test boundary

Before dataset use, unit tests should cover one valid transformation, duplicate canonical records, missing identity, ambiguous temporal boundary, unknown coverage, deterministic ordering, provenance preservation, and prohibited-field firewall. These tests validate implementation behavior, not the scientific hypothesis.

## 6. Build artifact

The eventual build review must identify implementation path, commit/hash, test result, dependency/version environment, specification version, preflight compatibility, and whether the scientific dataset was touched.

## 7. Decision

**BUILD DESIGN:** PASS.

**IMPLEMENTATION:** NOT YET BUILT.

**DATASET:** NOT EXECUTED.

**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 8. Next gate

`RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_UNIT_TEST_REVIEW`