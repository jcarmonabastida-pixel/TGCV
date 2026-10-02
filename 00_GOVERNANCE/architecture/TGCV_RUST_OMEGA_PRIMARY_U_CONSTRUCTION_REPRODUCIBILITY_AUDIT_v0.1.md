# TGCV — Rust Ω-Primary U Construction Reproducibility Audit v0.1

**Status:** CLOSED — REPRODUCIBILITY CONTRACT PASSED / EMPIRICAL U_t BUILD NOT EXECUTED
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_U_CONSTRUCTION_REPRODUCIBILITY_AUDIT

## 1. Audit question

Can the frozen U_t construction be reproduced deterministically from the retained Rust snapshot, using only the frozen structural inputs and rules?

## 2. Reproducibility contract

A conforming implementation must use the exact retained snapshot, the frozen temporal rule `DR-035-v0.1-ADJACENT-CREATED-AT`, `H=1`, the frozen transformation identity `τ=(origin_version_id,target_package_id,target_version_id)`, and the canonicalisation rule `Canon_T(τ)=τ`.

The implementation must emit the same canonical identity for the same primitive inputs, preserve provenance, and fail closed on unknown transformation-defining fields.

## 3. Determinism requirements

The following must be deterministic:

- snapshot selection;
- temporal boundary evaluation;
- candidate generation;
- identifier canonicalisation;
- duplicate handling;
- ordering of emitted records;
- handling of missing/unknown fields;
- provenance references.

No random seed, model inference, live registry query, accessibility computation or downstream outcome is permitted.

## 4. Audit result

The governance specification is reproducible in principle because every transformation-defining operation is explicitly frozen and all required inputs are identified.

However, this gate does **not** claim that an implementation has now been run against the local bytes. No byte-level execution is performed by this governance commit.

Therefore:

**REPRODUCIBILITY CONTRACT = PASS.**

**EMPIRICAL IMPLEMENTATION REPLAY = PENDING.**

## 5. Required execution artifact

Before scientific execution, a governed implementation replay must record:

1. exact input snapshot hash;
2. implementation/version identifier;
3. construction-rule version;
4. counts by coverage state;
5. raw candidate count;
6. unique U_t count;
7. duplicate/collision count;
8. unresolved/unknown count;
9. deterministic output hash;
10. provenance integrity check.

These diagnostics must not incorporate accessibility, outcome, reward/value or future trajectory.

## 6. Decision

**U_t REPRODUCIBILITY CONTRACT:** PASS.

**BYTE-LEVEL REPLAY:** NOT YET EXECUTED.

**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 7. Next gate

`RUST_OMEGA_PRIMARY_U_CONSTRUCTION_IMPLEMENTATION_REVIEW`