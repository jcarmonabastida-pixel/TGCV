# EXT-1.1 Rust — HRSV Gate v0.1

**HRSV:** Historical Registry State & Version-ID Gate
**Date:** 2026-08-30
**Status:** OPEN — execution pending
**Parent:** EXT-1.1_Rust
**Predecessor:** CHR-MICRO-3 (FAIL/BLOCKED on available evidence)

## Purpose
Resolve the specific evidential blockage identified by CHR-MICRO-3 without changing the TGCV ontology or using outcome data retrospectively.

## Questions

### HRSV-A — Historical registry state
Can the crates.io index Git history provide an auditable registry state at each required cutoff?

### HRSV-B — Candidate universe
Given that historical state, can all candidate releases satisfying each dependency constraint be enumerated using only information available at the cutoff?

### HRSV-C — Deterministic resolution
Can the historical candidate universe be resolved deterministically under the declared Cargo/semver resolution rule, without current-state leakage?

### HRSV-D — Version-ID bridge
Can each resolved `package@version` be mapped reproducibly to the crates.io `version_id` used by the historical daily download archive, without using downloads/outcomes to establish the mapping?

## Evidence hierarchy

1. Historical crates.io index Git state / commit history.
2. Official crates.io version metadata/API where used only for identity cross-checks.
3. Official archived daily version-download CSVs, used only after identity mapping and never as a resolution input.
4. Secondary documentation only as corroboration, never as sole evidence for a gate-critical historical fact.

## Non-circularity

The following are prohibited as inputs to A-C:
- downloads;
- popularity/adoption;
- survival/success;
- downstream outcomes;
- any variable derived from the eventual trajectory.

## PASS criteria

HRSV passes only if all A-D are demonstrated for the three CHR micro-slice cases with reproducible evidence and explicit cutoff timestamps.

**PASS:** A-D demonstrated for all cases.
**CONDITIONAL PASS:** only a documented identity-only convention remains, with no temporal or outcome information introduced.
**FAIL:** any historical state cannot be reconstructed, resolution is non-deterministic/unverifiable, or the version-ID bridge cannot be established without retrospective information.

## Current state

- CHR-MICRO-3: FAIL/BLOCKED.
- CARGO_NATIVE_ROUTE: OPEN.
- EXT-1.1 FREEZE: BLOCKED.
- No T freeze authorized.

## Execution record

| Case | A | B | C | D | Evidence / notes |
|---|---|---|---|---|---|
| C1 serde@1.0.0 | PENDING | PENDING | PENDING | PENDING | |
| C2 tokio@1.0.0 | PENDING | PENDING | PENDING | PENDING | |
| C3 rand@0.8.0 | PENDING | PENDING | PENDING | PENDING | |

**Overall verdict:** PENDING
