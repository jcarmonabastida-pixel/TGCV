# EXT-1.1 Rust — Resolver Specification `R` v0.1

**Status:** DRAFT — environment capture required before freeze
**Purpose:** Freeze the deterministic resolution semantics used by the `T_acc` identifiability experiment.

## 1. Role

`R` is an explicit input to the measurement function:

`T_acc,t = F(S_t, C_t, R)`

This artifact is intentionally separate from package state `S_t` and historical registry context `C_t`.

## 2. Required captured environment

The following values MUST be captured from the actual execution environment before final freeze:

- `cargo --version` — **NOT YET CAPTURED**
- `rustc --version` — **NOT YET CAPTURED**
- `rustup show active-toolchain` — **NOT YET CAPTURED**
- host triple — **NOT YET CAPTURED**
- target triple — **NOT YET CAPTURED**
- Cargo resolver generation — **TO BE FROZEN**

The C3 resolution log proves offline resolution occurred, but it does not contain a sufficiently explicit toolchain/version capture to make those values part of `R` yet.

## 3. Registry policy

- Registry: crates.io historical index.
- Historical snapshot: explicit dated snapshot supplied as `C_t`.
- Live registry access: **PROHIBITED** during historical accessibility computation.
- Current index substitution: **PROHIBITED**.
- Future package versions: **PROHIBITED**.
- Source replacement: none unless explicitly recorded in this artifact.

## 4. Candidate-resolution policy

For the minimal confirmatory ontology:

- dependency kind: normal;
- target condition: unconditional;
- optional: false;
- candidate feature set: empty;
- candidate requirement: exact version `=v`;
- one dependency edge inserted per candidate;
- path/git dependencies excluded;
- dev/build dependencies excluded.

## 5. Resolver policy

The final `R` MUST explicitly record:

1. Cargo resolver generation;
2. exact Cargo version;
3. exact Rust toolchain;
4. target/platform;
5. feature resolution policy;
6. yanked-version handling;
7. registry source configuration;
8. lockfile generation mode;
9. relevant `.cargo/config.toml` settings;
10. environment variables affecting Cargo resolution.

No unspecified setting may be silently allowed to affect the accessibility result.

## 6. Deterministic invocation

The implementation must invoke resolution in an isolated directory using only frozen `S_t`, `C_t`, and `R` inputs.

The implementation MUST fail closed if:

- the historical registry snapshot is unavailable;
- the live registry is contacted;
- an unspecified source replacement is detected;
- a required resolver parameter is missing.

## 7. Reproducibility record

The final freeze package must include:

- this specification;
- environment capture output;
- configuration files used for resolution;
- hashes of all frozen inputs;
- deterministic invocation record;
- expected machine-readable output;
- repeat-run comparison showing byte-identical output.

## 8. Freeze status

**NOT FROZEN.**

The exact local Cargo/Rust toolchain values must be captured before this specification can become the immutable `R` referenced by the frozen identifiability protocol.
