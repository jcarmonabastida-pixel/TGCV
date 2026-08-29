# EXT-1.1 NPM Small-Slice Gate v0.1

Date: 2026-08-29

## Gate result

**STRUCTURAL IDENTIFIABILITY: PASS**

**HISTORICAL VERSION IDENTITY: PASS (for non-deleted published versions)**

**VERSION-LEVEL OUTCOME: FAIL for direct replication of the Rust design**

**PACKAGE-LEVEL OUTCOME: CONDITIONAL PASS**

Therefore npm is **not yet frozen as a direct Rust-equivalent replacement**, but it is a viable TGCV experimental candidate if the experiment is explicitly reformulated around package-level outcome rather than version-level downloads.

## Evidence

The official npm registry documentation defines package metadata as a document containing all published versions currently present, with each version carrying its dependency ranges and package identity. The full metadata format also contains a `time` object mapping each version to its publication timestamp. The abbreviated metadata format retains `name`, `version`, dependencies and `dist` information.

This means a historical package state can be reconstructed for a cutoff `t` by retaining versions with publication timestamp <= `t`, provided the experiment excludes later metadata mutations and deleted versions are not required. npm-follower is relevant precisely because it archives versions as published and retains versions later deleted; its published paper reports collection from July 2022 onward and identifies deleted-version retention as a core feature.

## What passes

1. **Entity identity:** package name is explicit.
2. **Version identity:** `(package name, version)` is explicit in package metadata and `_id`.
3. **Historical timestamp:** `time[version]` is available in the full packument.
4. **Dependency constraints:** version-level `dependencies` contain semver ranges.
5. **Historical structural reconstruction:** `S_t` can be constructed from versions published by cutoff `t` and their dependency constraints.
6. **T_acc construction:** the existing TGCV resolver abstraction can be adapted to npm semver and dependency semantics.
7. **Delta T_acc:** adjacent cutoffs can be compared without a numeric database key.
8. **Reproducibility:** the source package metadata is obtainable from the public registry for a small slice.

## What fails / remains conditional

The npm public download API is package-level, not version-level. Therefore it cannot directly reproduce the Rust outcome `downloads(version_id, day)`.

This is not fatal to TGCV, but it changes the experimental estimand. A valid npm experiment would use a package-level outcome, e.g. daily/weekly package downloads, while `T_acc` remains the set of package versions/dependency-resolutions accessible to that package at time `t`.

This must be treated as a deliberate experimental variant, not silently substituted for the Rust design.

## Proposed npm estimand

For package p at time t:

- `S_t(p)`: published version/dependency state available by cutoff t.
- `T_acc,t(p)`: admissible package-version transformations/resolutions under the pinned npm semver/resolution semantics.
- `Delta T_acc,t`: set difference/symmetric difference between adjacent states.
- `V_t(p)`: package-level download outcome over a predefined future observation window.

The outcome window must begin strictly after the structural cutoff to avoid temporal leakage.

## Required next test

Before freeze, run an executable micro-experiment on 3 packages with at least 3 historical cutoffs, and verify:

1. packument reconstruction is deterministic;
2. no version published after cutoff enters `S_t`;
3. dependency ranges are parsed identically across runs;
4. `T_acc,t` changes when and only when the pinned resolver semantics imply a change;
5. outcome windows do not overlap the information used to construct `T_acc,t`;
6. download data can be retrieved for the same packages and dates;
7. the resulting dataset can be regenerated from documented public endpoints without manual intervention.

## Decision

**Do not download npm-follower's full archive.**

Proceed with the small executable npm experiment using public packuments plus the public download API. If that experiment passes, freeze npm as **EXT-1.1-NPM-PACKAGE-OUTCOME v0.1**. If package-level outcome is theoretically insufficient for the TGCV hypothesis, stop and evaluate Chrono-Resolution rather than weakening the hypothesis post hoc.

## Provenance

- npm Registry package metadata documentation.
- npm Registry API documentation.
- Pinckney et al., `npm-follower: A Complete Dataset Tracking the NPM Ecosystem`, ESEC/FSE 2023 / arXiv:2308.12545.
