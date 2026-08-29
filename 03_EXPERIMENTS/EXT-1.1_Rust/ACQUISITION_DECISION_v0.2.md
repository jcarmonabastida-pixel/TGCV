# EXT-1.1 — Acquisition decision v0.2

**Date:** 2026-08-29
**Status:** ROUTE B-CARGO OPEN / PIPELINE PREPARATION AUTHORIZED

## Decision

The original Figshare replication artifact remains the preferred reference dataset, but its historical download endpoint is currently not recoverable through the available access path. The authors' GitHub release documents the SQLite export but does not currently expose that binary as a repository blob or release asset.

The project therefore opens a **Cargo-native reconstruction route** for EXT-1.1. This route is not silently substituted for the original replication dataset; it is a separately identified experimental acquisition route with its own provenance and freeze.

## Evidence supporting the route

The original paper states that the dataset contains package identities, package versions, version-to-package semver dependencies, and daily downloads of package versions. It also states that the database can be recreated as SQLite or PostgreSQL and that the collection code is available in the authors' repository.

The authors' `rust_repos_2022_09_07` release fixes the relevant upper-bound date at 2022-09-07 and identifies the crates.io dump as the source used for that snapshot. The release also fixes `repodepo` 0.1.3 at commit `5c592800cbbb09f5b43c91f937f03141140f3c78`.

## Critical acquisition finding

Current crates.io documentation makes current database dumps available every 24 hours, but the crates.io project does **not archive old database dumps**. Therefore the exact 2022-09-07 database dump should not be treated as directly recoverable from the current official dump endpoint without independent archival evidence.

However, crates.io maintains an archive of daily version-download CSV files, including dates around 2022-09-07. These files contain `version_id` and daily download counts. This provides a potentially recoverable historical download component.

## Proposed Cargo-native data construction

Construct the minimum EXT-1.1 observational dataset from independently recoverable sources:

1. package/version/dependency history from the crates.io index and its Git history, using historical state/cutoffs rather than current-state metadata;
2. daily version downloads from the official `static.crates.io/archive/version-downloads/` archive;
3. package/version identifiers joined through the crates.io version identifiers;
4. explicit temporal cutoffs and censoring rules.

## Non-circularity rule

`T_acc` must be defined from package/version/dependency constraints and observed package/version state, not from download success itself. Downloads are an outcome/validation variable, never an input used to define accessibility.

## New gate

Before FREEZE, verify:

- historical dependency reconstruction is possible without current-state leakage;
- package/version IDs can be joined to the archived download series;
- semver constraints can be evaluated deterministically;
- the chosen observation window has complete enough download coverage;
- left/right censoring is explicitly handled;
- the resulting `T_acc(t)` definition is operational and auditable.

## Freeze status

`FIGSHARE_REFERENCE = IDENTIFIED / PHYSICAL ARTIFACT UNRECOVERED`
`CARGO_NATIVE_ROUTE = OPEN`
`HISTORICAL_DOWNLOAD_ARCHIVE = AVAILABLE IN PRINCIPLE`
`HISTORICAL_DEPENDENCY_RECONSTRUCTION = OPEN`
`FREEZE = BLOCKED`
