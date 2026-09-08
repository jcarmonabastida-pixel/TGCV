# TGCV — RUST-DYN-2 Configuration Multiplicity Audit v0.1

**Date:** 2026-09-08  
**Status:** DESIGN FROZEN — STRUCTURAL AUDIT ONLY / REAL EXPERIMENT NOT AUTHORIZED

## 1. Purpose

Determine whether the frozen Rust dataset permits lossless use of the assignment-level successor representation required by the historical Potential Reach contract.

This audit resolves only a representation question. It does not construct `T_acc`, `ΔT_acc`, `Reach`, `Trajectory`, outcomes, value, or predictive metrics.

## 2. Frozen inputs

Dataset SHA-256:
`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Exact members:
- `rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv`
- `rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv`

Frozen dependency header:
`depending_version,depending_on_package,semver_str`

## 3. Unit of audit

For every focal package-version origin, inspect its dependency declarations as rows:

`d = (origin_version_id, target_package_id, semver_str)`.

The primary structural question is whether an origin contains more than one dependency declaration targeting the same `target_package_id`.

## 4. Required measurements

Report at minimum:

- total dependency rows;
- total focal origins with dependency rows;
- number of origins with at least two declarations to the same target package;
- number of duplicated target-package groups;
- maximum declaration multiplicity for one `(origin,target_package)` pair;
- number of origins containing distinct requirements for the same target package;
- number of origins containing identical repeated declarations for the same target package;
- counts of affected origins and affected declaration rows;
- deterministic hash of the canonical audit summary.

For each repeated `(origin,target_package)` group, distinguish:

1. **identical repetition:** same `semver_str` repeated;
2. **requirement multiplicity:** more than one distinct `semver_str`.

## 5. Decision rule

### A — LOSSLESS FOR CURRENT SUCCESSOR REPRESENTATION

Only if every origin has at most one declaration per target package.

Then the assignment-level successor representation may be used without declaration-multiplicity loss for the frozen dataset.

### B — LOSSLESS ONLY WITH EXPLICIT CANONICALIZATION AMENDMENT

If repeated declarations exist but all repetitions are identical and an explicit deterministic deduplication rule can be frozen without changing the historical successor semantics.

No such rule is assumed by this audit; it must be separately accepted if required.

### C — LOSSY / IMPLEMENTATION BLOCKER

If any origin contains multiple distinct requirements for the same target package, the current assignment-level configuration is not demonstrably lossless. A richer canonical representation must be designed and frozen before real Reach execution.

## 6. Firewall

The audit MUST NOT:

- construct `T_acc`;
- evaluate `P_tau`;
- resolve or select target versions;
- construct successor configurations;
- compute Reach or Trajectory;
- read later release activity or future metadata;
- read downloads, adoption, popularity, success, outcomes or value;
- execute Cargo or any package build;
- sample rows;
- use historical temporal ordering;
- modify the dataset or historical artifacts.

## 7. Determinism

The audit must read the exact frozen archive members, use deterministic integer/string parsing, sort canonical audit keys before hashing, and fail closed on malformed rows or duplicate CSV headers.

## 8. Scientific boundary

This audit establishes only whether a chosen structural serialization is lossless for declaration multiplicity in the frozen dataset. It does not establish validity of the Rust operationalization, Reach non-redundancy, causality, prediction, universal validity, value, or originality.

## 9. Governance

**REAL-DATASET RUST-DYN-2 EXECUTION AUTHORIZED: NO.**

A PASS here only clears the configuration-representation blocker. It does not authorize RUST-DYN-2.
