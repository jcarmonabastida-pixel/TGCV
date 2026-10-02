# TGCV — Rust Ω-Primary Provenance Manifest and Coverage Freeze Review v0.1

**Status:** CLOSED — PROVENANCE/COVERAGE MANIFEST FROZEN AS CONDITIONAL / Ω-PRIMARY ADMISSION NOT GRANTED  
**Date:** 2026-10-02  
**Gate:** RUST_OMEGA_PRIMARY_PROVENANCE_MANIFEST_AND_COVERAGE_FREEZE_REVIEW

## 1. Purpose

Freeze the provenance and coverage record for the **existing** Rust snapshot without reacquisition, byte substitution, or scientific execution.

This gate separates what is already established by canonical preflight evidence from what remains unverified.

## 2. Frozen candidate snapshot identity

| Field | Frozen record | Status |
|---|---|---|
| Local artifact | `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip` | RECORDED |
| ZIP SHA-256 | `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224` | PREVIOUS PREFLIGHT PASS |
| Archive root | `rust_repos_2022_09_07/` | PREVIOUS PREFLIGHT PASS |
| Temporal rule | `DR-035-v0.1-ADJACENT-CREATED-AT` | PREVIOUS PREFLIGHT PASS |
| Horizon | `H=1` | PREVIOUS PREFLIGHT PASS |
| Required structural member 1 | `dumps/postgresql/data/package_versions.csv` | PASS |
| Required structural member 2 | `dumps/postgresql/data/package_dependencies.csv` | PASS |

The ZIP hash is not recomputed in this governance action; it is inherited from the executed local preflight, which recorded an expected-hash match.

## 3. Historical source/provenance

The empirical route is tied to the already retained historical Rust corpus associated with the 2022-09-07 snapshot.

The repository currently lacks a single canonical manifest that independently proves, in one record, the complete chain:

`authoritative publication identity → exact published version → source archive → local acquisition → local bytes`.

Therefore:

**PROVENANCE = CONDITIONALLY FROZEN, NOT FULLY VERIFIED.**

This is a governance limitation, not a reason to download another dataset.

## 4. Coverage freeze

Coverage semantics are frozen as:

- **OBSERVED_PRESENT:** record/member observed.
- **OBSERVED_ABSENT_COMPLETE:** absence established only where the relevant source is demonstrably complete for the frozen scope.
- **UNKNOWN_MISSING:** absence cannot be inferred.
- **OUT_OF_SCOPE:** deliberately excluded by the frozen scope.

Only `OBSERVED_PRESENT` and `OBSERVED_ABSENT_COMPLETE` may support structural appearance/disappearance claims.

For the present candidate, member/schema presence is PASS. Full row-level completeness of the historical transformation universe has **not** been demonstrated by this gate.

Consequently, set differences in `U_t` must not yet be interpreted as true transformation appearance/removal unless the applicable coverage condition is independently established.

## 5. Ω-primary consequences

The manifest supports continued development of:

`Ω_T,t=(U_t,≡_T,R_t)`

from primitive Rust records, but does not itself admit Ω-primary empirically.

Still open:

1. transformation canonicalisation `≡_T`;
2. complete/frozen relation schema for `R_t`;
3. longitudinal transformation correspondence `κ`;
4. row-level coverage/completeness;
5. state-reducibility/non-circularity discrimination.

## 6. Decision

**PROVENANCE MANIFEST:** CONDITIONALLY FROZEN.

**COVERAGE SEMANTICS:** FROZEN.

**SNAPSHOT BYTE IDENTITY:** PREVIOUS PREFLIGHT PASS.

**STRUCTURAL SCHEMA:** PASS.

**Ω-PRIMARY DATASET ADMISSION:** NOT GRANTED.

**NEW DOWNLOAD:** NOT PERMITTED AS A SUBSTITUTE.

**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

No change to TGCV Core, Evidence→Claim Matrix v1.44, or RMA v3.37.

## 7. Next gate

`RUST_OMEGA_PRIMARY_TRANSFORMATION_CANONICALISATION_FREEZE_REVIEW`
