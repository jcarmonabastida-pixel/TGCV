# TGCV — Rust Ω-Primary U Implementation Specification Review v0.1

**Status:** CLOSED — IMPLEMENTATION SPECIFICATION FROZEN / CODE CREATION AND EXECUTION NOT AUTHORIZED BY THIS GATE
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_SPECIFICATION_REVIEW

## 1. Governing basis

This specification follows the repository README freeze/reproducibility policy: the large Rust dataset remains outside GitHub; GitHub stores protocol, manifest, hash, provenance, code, configuration and derived results.

The implementation is a new Ω-primary route and must remain separate from historical EXT-1.1 identity-recovery tooling.

## 2. Input contract

Only the retained historical snapshot admitted by the preceding governance gates may be used.

Required structural inputs:

- `package_versions.csv`;
- `package_dependencies.csv`.

Required fields for the primary U construction:

- version identity;
- package identity;
- version creation time;
- dependency source version;
- dependency target package;
- dependency version constraint where needed for relation construction.

## 3. U_t construction contract

For each origin release and admissible target release under the frozen temporal rule `DR-035-v0.1-ADJACENT-CREATED-AT`, construct:

`τ=(origin_version_id,target_package_id,target_version_id)`.

Apply:

`Canon_T(τ)=(origin_version_id,target_package_id,target_version_id)`.

Then:

`U_t=unique(Canon_T(Raw_t))`.

No semantic deduplication beyond this rule is permitted.

## 4. Fail-closed rules

The implementation must return an explicit unresolved/unknown status rather than infer:

- missing transformation-defining identifiers;
- ambiguous temporal boundaries;
- incomplete coverage;
- ambiguous target release resolution;
- undocumented identity mappings.

Unknown is never converted into absence.

## 5. Required output schema

Each emitted U record must contain at least:

- canonical transformation identity;
- snapshot/observation time;
- origin provenance reference;
- target provenance reference;
- coverage state;
- construction-rule version;
- resolution status.

A deterministic output manifest must additionally record counts and cryptographic hash of the emitted canonical representation.

## 6. Firewall

The implementation may not access or derive from:

`T_acc`, Reach, `ΔReach`, execution/accessibility status, build/test success, downstream outcome, reward/utility/value, future activity/trajectory, or any variable derived from these.

No live crates.io lookup is permitted.

## 7. Determinism

The implementation must define deterministic ordering, duplicate handling, temporal comparison, missingness handling and serialization before execution.

Any nondeterminism discovered in preflight is a gate failure.

## 8. Required implementation artifact

A new dedicated implementation should be placed under the governed Ω/Rust experiment code path. It must not modify the historical `identity_recovery.py` route.

The implementation must expose a non-executing validation/preflight mode before any scientific execution mode.

## 9. Decision

**SPECIFICATION:** FROZEN.

**NEW Ω IMPLEMENTATION:** NOT YET CREATED.

**PRE-FLIGHT EXECUTION:** NOT AUTHORIZED BY THIS GATE.

**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 10. Next gate

`RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_PREFLIGHT_REVIEW`