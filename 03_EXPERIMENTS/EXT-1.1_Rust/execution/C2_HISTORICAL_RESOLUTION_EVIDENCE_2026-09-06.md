# C2 — Historical Resolution Evidence

**Date:** 2026-09-06  
**Experiment:** EXT-1.1 Rust  
**Protocol:** CHR-MICRO-3  
**Target:** `tokio 1.0.0`  
**Historical snapshot:** `2021-05-05`  
**Snapshot commit:** `a5dcd8438da2d8f99e3661a1956afbfb8f026fa0`  
**Status:** C2 HISTORICAL RESOLUTION — PARTIAL PASS WITH EXPLICIT R5a BLOCK

## 1. Scope

C2 tests whether the historical dependency graph required by `tokio 1.0.0` can be reconstructed and reproduced using a historical crates.io index snapshot, historically matching crate archives, and the historical Rust/Cargo toolchain.

This evidence concerns historical reconstruction only. It does **not** constitute scientific execution of EXT-1.1, does not consume the empirical Rust dataset, and does not modify the frozen N-R8-C2 corpus.

## 2. Historical inputs

The historical crates.io index snapshot is pinned to commit:

`a5dcd8438da2d8f99e3661a1956afbfb8f026fa0`

Target package record:

- `tokio 1.0.0`
- checksum: `9f4bfdcbd00fa893ac0549b38aa27080636a0104b0d0c38475a99439405e1df8`
- historical state: `yanked=true`

Required normal dependency:

- `pin-project-lite ^0.2.0`

Build dependency:

- `autocfg ^1.0.1`

Historically selected dependency versions used in the reconstructed graph:

- `pin-project-lite 0.2.6`, checksum `dc0e1f259c92177c30a4c9d177246edd0a3568b25756a977d0632cf8fa37e905`
- `autocfg 1.0.1`, checksum `cdb031dd78e28731d87d56cc8ffef4a8f36ca26c38fe2de700543e627f8a464a`

Historical crate archive checksums were independently verified against the historical index metadata.

## 3. Toolchain

Historical toolchain used for C2:

- target: `1.51.0-x86_64-pc-windows-msvc`
- Cargo: `1.51.0 (43b129a20 2021-03-16)`
- rustc: `1.51.0 (2fd73fabe 2021-03-23)`

Toolchain evidence SHA-256:

`E388A681376F41E6038A9553B0DBC4C974755BF79F4BAD88349C3731704724A1`

## 4. R5a — Fresh exact resolution

A fresh Cargo resolution was attempted with:

`tokio = "=1.0.0"`

against the historical local registry.

Cargo rejected the exact target because `tokio 1.0.0` is yanked. The candidate set contained later non-yanked releases, but none satisfies the exact requirement `=1.0.0`.

**Decision: R5a = BLOCKED_BY_YANKED_TARGET.**

This is an expected semantic property of Cargo resolution and is not treated as an environment or acquisition failure.

No substitution by `tokio 1.0.1` or any later version was made.

## 5. R5b — Reproducibility of a pre-existing historical lock graph

A `Cargo.lock` was manually reconstructed from verified historical metadata, explicitly fixing:

- `tokio 1.0.0`
- `pin-project-lite 0.2.6`
- `autocfg 1.0.1`

Initial manual lockfile SHA-256:

`7E8004200C52106FCEA3722D802452FFA547F27946403B3E34BDC0AEF7B11347`

Cargo normalized the lockfile by adding its generated header and the explicit `autocfg` package entry required by the dependency graph. Importantly, the selected historical versions and checksums were unchanged.

A subsequent offline build succeeded using only the local historical registry:

`rustup run 1.51.0 cargo check --offline`

Observed result:

`Finished dev [unoptimized + debuginfo] target(s) in 3.11s`

The normalized lockfile was then tested with:

`rustup run 1.51.0 cargo check --offline --locked`

Observed result:

`Finished dev [unoptimized + debuginfo] target(s) in 0.02s`

Therefore Cargo accepted the normalized lockfile without requesting or recording further dependency changes.

**Decision: R5b = PASS.**

## 6. Interpretation

C2 establishes two distinct facts that must not be conflated:

1. A **fresh exact resolution** of `tokio = 1.0.0` is blocked because the historical target release is yanked.
2. A **pre-existing historical lock graph** containing `tokio 1.0.0` can nevertheless be reproduced/materialized offline with Cargo 1.51.0 from the reconstructed historical local registry.

The second result is the relevant positive evidence for historical graph reproducibility. It does not convert R5a into a PASS.

## 7. Boundary conditions

This C2 evidence does not claim:

- full equivalence with Cargo's complete historical resolver implementation;
- successful fresh resolution of the yanked target;
- reconstruction of the complete Rust crates.io ecosystem;
- scientific execution of EXT-1.1;
- consumption of the empirical Rust dataset;
- validation of the N-R8-C2 scientific hypothesis.

The empirical dataset remains unconsumed, and the frozen N-R8-C2 corpus remains untouched.

## 8. C2 decision

**C2 = PARTIAL PASS / R5a BLOCKED / R5b PASS.**

The historical graph required for the selected C2 target is reproducible from pinned historical evidence under the historical toolchain, while fresh exact resolution remains correctly blocked by the historical yank state.

## 9. Next authorized step

Proceed to **C3**, preserving the R5a/R5b distinction and carrying forward only the historically verified graph and provenance. No current registry access and no substitution of the yanked target are authorized.
