# EXT-1.1 Dataset Selection Decision v0.1

Date: 2026-08-29

## Decision

Rust/Schueller is **closed for confirmatory EXT-1.1 execution** because the historical `version_id -> (crate, version)` identity required to join the 2022-09-07 download series to the historical index cannot be established from the publicly recoverable historical artifacts currently available.

This is a data-identification failure, not a conceptual failure of the Rust operationalization.

## Candidate comparison

### 1. npm-follower — PRIORITY CANDIDATE

npm-follower archives package metadata and code for npm versions as they are published and explicitly retains versions later deleted. Collection began in July 2022. The published paper reports that the dataset also includes download metrics and describes a database organized around packages, versions, dependencies and download metrics. This makes npm the strongest alternative for the same dependency-space operationalization. The principal risk is acquisition size and the need to define a small reproducible historical slice rather than depend on the entire archive.

Evidence: Pinckney et al., npm-follower (2023); ESEC/FSE demonstration and artifact documentation.

### 2. Chrono-Resolution — SECONDARY / HIGH-INTEREST CANDIDATE

A 2026 dataset paper reports release-point dependency-resolution data for npm, PyPI and crates.io, with historical resolution information. This is highly relevant to `T_acc` because it directly addresses temporal dependency resolution. However, the reported dataset used special access to Google deps.dev for the resolution data and cannot be rebuilt solely through the public deps.dev API. This makes it less attractive as the primary reproducible dataset unless access and redistribution conditions are verified.

### 3. Libraries.io — BACKUP ONLY

Libraries.io provides explicit Version and Dependency entities and is structurally clean, but the openly archived Zenodo release identified in the audit is from 2020 and is a 24.9 GB archive. It therefore has weaker temporal fit and substantial acquisition cost for this experiment.

## Selection rule

The next primary candidate must pass an executable small-slice gate covering:

1. stable historical package identity;
2. stable version identity;
3. historical publication timestamp;
4. dependency constraints;
5. reconstruction of `T_acc,t`;
6. calculation of `Delta T_acc` between adjacent observations;
7. independent outcome or outcome path;
8. no use of current-state data to reconstruct historical state;
9. reproducible acquisition of the slice;
10. auditable provenance for every observation.

A candidate fails if any of criteria 1-4 or 8-10 cannot be established.

## Operational consequence

Do **not** download a full alternative dataset yet.

The next action is a metadata-only or API-level slice test for npm-follower, using a small set of packages and two or more historical release points. If the slice passes, EXT-1.1 will be reparameterized to npm without discarding the existing Rust resolver/pipeline abstractions. If it fails, Chrono-Resolution will be evaluated for access feasibility before any large acquisition.

## Reuse of existing TGCV assets

The following Rust work remains reusable:

- SemVer normalization and reference tests;
- dependency constraint representation;
- `T_acc` construction interface;
- `Delta T_acc` expansion/invariance/contraction tests;
- identity-recovery audit logic;
- dataset governance and freeze gates.

No confirmatory result from Rust has been produced and no Rust result should be cited as empirical evidence for TGCV.
