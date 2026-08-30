# EXT-1.1 Rust — Execution Package v0.1

**Date:** 2026-08-30
**Purpose:** provide the exact external-download/run instructions required to execute the snapshot-only resolver test in an environment with network access.

## What the user needs to do

No manual selection of individual crate files is required.

The preferred route is to download the three official historical index snapshots as Git branches and run the supplied tooling against local snapshot files.

Official archive repository:
`https://github.com/rust-lang/crates.io-index-archive`

Official crates.io index documentation confirms that the index contains the metadata Cargo uses to resolve dependencies. cite-reference: official crates.io-index repository. 

## Required snapshots

1. `snapshot-2018-09-26` — C1 `serde@1.0.0`
2. `snapshot-2021-05-05` — C2 `tokio@1.0.0`
3. `snapshot-2021-05-05` — C3 `rand@0.8.0`

## Recommended download method

From a machine with Git and network access:

```bash
git clone --branch snapshot-2018-09-26 --single-branch --depth 1 https://github.com/rust-lang/crates.io-index-archive.git tgcv-index-2018-09-26
git clone --branch snapshot-2021-05-05 --single-branch --depth 1 https://github.com/rust-lang/crates.io-index-archive.git tgcv-index-2021-05-05
```

Do NOT use the current `crates.io-index` master as a substitute.

## Integrity

After cloning, record:

```bash
cd tgcv-index-2018-09-26 && git rev-parse HEAD
cd ../tgcv-index-2021-05-05 && git rev-parse HEAD
```

The resulting commit SHAs must be stored in the execution record. The test is snapshot-identified by commit, not merely by branch name.

## What to return/upload

The user does not need to upload the complete Git repositories into ChatGPT if local execution is possible. The preferred handoff is:

- the two snapshot commit SHAs;
- the stdout/stderr of the resolver execution;
- the generated candidate-universe JSON/CSV for C1-C3;
- the exact Cargo/rustc versions (`cargo --version`, `rustc --version`);
- the final `package@version → version_id` mapping evidence.

If local execution is not possible, upload the two cloned snapshot directories as ZIP files. Do not modify their contents before zipping.

## Execution boundary

The downloaded snapshots are inputs only. No current registry state, downloads, popularity, adoption or downstream outcome may be used to construct the candidate universe or perform resolution.

## Current TGCV state

CHR-MICRO-3 amended protocol: APPROVED.
HRSV: A PASS; B PARTIAL; C BLOCKED; D BLOCKED.
EXT-1.1 FREEZE: BLOCKED.

The next scientific decision is authorized only after the snapshot-only resolver and independent version-ID bridge have been executed and persisted.
