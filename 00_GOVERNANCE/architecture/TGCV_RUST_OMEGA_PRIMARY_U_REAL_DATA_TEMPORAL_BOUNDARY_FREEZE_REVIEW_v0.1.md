# TGCV — Rust Ω-Primary Real-Data Temporal Boundary Freeze Review v0.1

**Status:** CLOSED — TEMPORAL BOUNDARY RULE FROZEN / EMPIRICAL CONSTRUCTION NOT EXECUTED  
**Date:** 2026-10-02  
**Gate:** RUST_OMEGA_PRIMARY_U_REAL_DATA_TEMPORAL_BOUNDARY_FREEZE_REVIEW

## 1. Purpose

Freeze an exact, reproducible temporal boundary for the retained historical Rust snapshot before real-data construction of U_t.

## 2. Boundary rule

The inclusive snapshot cutoff is defined as:

`cutoff = max(created_at)`

over all valid records in the admitted `package_versions.csv` member of the retained snapshot.

The rule is deterministic and depends only on the admitted primitive structural snapshot. It does not inspect accessibility, execution, downstream outcome, reward/value, or future trajectory.

## 3. Interaction with DR-035

The frozen temporal rule remains:

`DR-035-v0.1-ADJACENT-CREATED-AT`

with `H=1`.

For an origin release at `source.created_at`, an eligible target release must satisfy:

- `target.created_at > source.created_at`;
- `target.created_at <= cutoff`;
- target is selected by the deterministic earliest-later ordering already frozen in the constructor.

## 4. Why this boundary is admissible

The dataset artifact and byte identity are already frozen. The boundary is therefore a deterministic function of the retained primitive snapshot rather than an externally chosen date/time.

This avoids inventing an unrecorded wall-clock cutoff such as end-of-day 2022-09-07.

## 5. Coverage interaction

The temporal boundary does not establish completeness.

Therefore:

- `OBSERVED_PRESENT` remains admissible for observed candidates;
- `UNKNOWN_MISSING` remains the default when absence cannot be certified;
- `OBSERVED_ABSENT_COMPLETE` still requires an independent completeness certificate;
- `OUT_OF_SCOPE` applies only outside the frozen scope.

## 6. Execution boundary

This review does not read or transform the real dataset. It only freezes the boundary rule.

The next execution must calculate the actual cutoff from the admitted `package_versions.csv`, record that value in the result artifact, and then pass it to constructor v0.4 with `complete_target_packages=[]`.

## 7. Decision

**TEMPORAL BOUNDARY RULE:** FROZEN.

**ACTUAL CUTOFF VALUE:** TO BE DERIVED DURING REAL-DATA EXECUTION FROM THE ADMITTED SNAPSHOT.

**SCIENTIFIC EXECUTION:** NOT YET PERFORMED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 8. Next gate

`RUST_OMEGA_PRIMARY_U_REAL_DATA_CONSTRUCTION_EXECUTION`
