# TGCV — Rust Ω-Primary U Implementation Preflight Review v0.1

**Status:** CLOSED — PREFLIGHT CONTRACT FROZEN / IMPLEMENTATION NOT YET BUILT OR EXECUTED
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_PREFLIGHT_REVIEW

## 1. Purpose

Define the non-scientific preflight that must pass before the new Ω-primary U implementation may be created/executed against the retained Rust snapshot.

## 2. Preflight inputs

The preflight must bind, without ambiguity, all of:

- retained snapshot identity and recorded SHA-256;
- required archive members;
- exact field names and types;
- frozen temporal rule `DR-035-v0.1-ADJACENT-CREATED-AT`;
- `H=1`;
- transformation identity tuple;
- canonicalisation rule;
- coverage states;
- κ rule where longitudinal output is prepared;
- information-firewall prohibition list;
- implementation version/commit.

## 3. Static checks

The preflight must verify:

1. required files exist in the retained snapshot;
2. required columns exist;
3. identifier fields have declared types;
4. timestamps are parseable under the frozen convention;
5. no prohibited input field is referenced by the U implementation;
6. deterministic ordering/serialization is specified;
7. unknown/missing handling is fail-closed;
8. output schema contains provenance and coverage fields;
9. implementation does not call live external registries;
10. historical EXT-1.1 identity-recovery code is not imported as an Ω construction dependency.

## 4. Non-scientific boundary

The preflight may inspect code, schemas, manifests and configuration.

It may not compute scientific U_t results, estimate accessibility, calculate Reach, evaluate trajectories/outcomes/value, or select transformations using downstream information.

Opening or hashing the retained archive for identity verification is a provenance operation and is distinct from scientific execution.

## 5. Required preflight artifact

A successful preflight must emit a compact immutable record containing:

- PASS/FAIL per check;
- input snapshot hash;
- implementation commit/hash;
- specification version;
- firewall result;
- schema result;
- deterministic serialization result;
- execution authorization state.

Any FAIL blocks the next gate.

## 6. Authorization boundary

Passing this preflight does not authorize scientific execution. Scientific execution remains a separate explicit authorization step under the repository's governance policy.

## 7. Decision

**PREFLIGHT CONTRACT:** FROZEN.

**IMPLEMENTATION:** NOT YET CREATED.

**PREFLIGHT EXECUTION:** NOT PERFORMED.

**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 8. Next gate

`RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_BUILD_REVIEW`