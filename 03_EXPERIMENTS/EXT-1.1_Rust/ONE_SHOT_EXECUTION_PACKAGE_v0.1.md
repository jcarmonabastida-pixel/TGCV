# EXT-1.1 Rust — ONE-SHOT EXECUTION PACKAGE v0.1

**Date:** 2026-08-30
**Status:** PREPARED — WAITING FOR COMPUTER EXECUTION
**Purpose:** make the remaining CHR/HRSV execution reproducible in one controlled run.

## Canonical objective

Execute the amended CHR-MICRO-3/HRSV test using only pinned historical crates.io index snapshots, then independently establish the `package@version → version_id` bridge. No current registry state or downstream outcome may enter historical resolution.

## Required local prerequisites

- Git
- Rust toolchain including Cargo
- Python 3
- network access during snapshot acquisition only

## Step 1 — acquire snapshots

```bash
git clone --branch snapshot-2018-09-26 --single-branch --depth 1 https://github.com/rust-lang/crates.io-index-archive.git tgcv-index-2018-09-26
git clone --branch snapshot-2021-05-05 --single-branch --depth 1 https://github.com/rust-lang/crates.io-index-archive.git tgcv-index-2021-05-05
```

Immediately record immutable commit identifiers:

```bash
(cd tgcv-index-2018-09-26 && git rev-parse HEAD) > snapshot_2018.commit
(cd tgcv-index-2021-05-05 && git rev-parse HEAD) > snapshot_2021.commit
```

Do not pull, checkout another branch, or modify these directories afterwards.

## Step 2 — capture environment

```bash
cargo --version > cargo.version.txt
rustc --version > rustc.version.txt
python3 --version > python.version.txt
uname -a > host.txt
```

## Step 3 — run the snapshot-only candidate replay

Use the versioned tool:

`tools/replay_snapshot_resolver.py`

The tool must be run only against local snapshot files. Its current scope is candidate-universe enumeration for caret requirements; it is not by itself a full Cargo-equivalence proof.

## Step 4 — full Cargo equivalence run

Create an isolated local registry/index environment from the pinned snapshot. Pin the Cargo toolchain used for the run. Execute the minimal C1-C3 dependency graphs against the snapshot-only registry.

Record:

- exact Cargo/rustc versions;
- resolver configuration/version;
- commands;
- stdout/stderr;
- exit codes;
- generated lockfiles;
- SHA-256 hashes of all input/output artifacts.

If Cargo cannot be made to resolve against the historical snapshot without consulting current crates.io, stop and record the failure. Do not silently substitute current metadata.

## Step 5 — version-ID bridge

For every resolved `package@version`, establish the corresponding crates.io `version_id` independently of downloads/outcomes. Preserve the source and method of the identity mapping. The mapping must not be inferred from download statistics.

## Step 6 — evidence bundle

Create:

```text
execution/
  manifest.json
  snapshot_2018.commit
  snapshot_2021.commit
  cargo.version.txt
  rustc.version.txt
  python.version.txt
  host.txt
  commands.txt
  C1/
  C2/
  C3/
  VERSION_ID_BRIDGE.json
  SHA256SUMS.txt
```

`manifest.json` must contain the snapshot SHAs, tool versions, case definitions, and execution timestamp.

## Step 7 — stop condition

Do not interpret the result locally. Preserve the raw evidence first. Then upload the evidence bundle (or the smallest complete set of artifacts) to the TGCV repository/working context for audit.

## Scientific decision rule

- If snapshot-only Cargo resolution is reproducible and the version-ID bridge passes: return to CHR-MICRO-3 and evaluate PASS.
- If snapshot acquisition works but Cargo equivalence fails: record the precise failure mode; do not substitute a different resolver silently.
- If the version-ID bridge fails independently: CHR remains blocked even if resolution succeeds.
- Only a complete evidential pass can unblock EXT-1.1 FREEZE.

## No-current-state rule

Current crates.io index data, current dependency resolution, downloads, popularity, adoption, survival, success, or downstream outcomes are prohibited from historical candidate-universe construction and resolution.

## Current canonical state

HIAR: PARTIAL PASS / ROUTE OPEN.
HRSV v0.2: A PASS; B PARTIAL; C BLOCKED; D BLOCKED.
CHR-MICRO-3: BLOCKED pending reproducible resolver + bridge evidence.
EXT-1.1 FREEZE: BLOCKED.
