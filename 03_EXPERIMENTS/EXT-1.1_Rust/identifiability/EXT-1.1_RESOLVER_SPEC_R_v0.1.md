# EXT-1.1 Rust — Resolver Specification `R` v0.1

**Status:** DRAFT — environment capture substantially completed; configuration probe still required before freeze
**Purpose:** Freeze the deterministic resolution semantics used by the `T_acc` identifiability experiment.

## 1. Role

`R` is an explicit input to the measurement function:

`T_acc,t = F(S_t, C_t, R)`

This artifact is intentionally separate from package state `S_t` and historical registry context `C_t`.

`R` specifies resolver semantics and execution constraints. It MUST NOT silently include the user's incidental Cargo cache, registry cache, filesystem state, or other machine-local state.

## 2. Captured execution environment

Captured from the actual EXT-1.1/C3 execution environment on Windows:

| Parameter | Captured value |
|---|---|
| `rustc --version` | `rustc 1.98.1 (48a229cea 2026-09-01)` |
| rustc commit | `48a229ceaefd4985c50990b14116b6d856af0985` |
| LLVM | `22.1.8` |
| `cargo --version` | `cargo 1.98.1 (797e8a9bc 2026-08-05)` |
| Cargo commit | `797e8a9bca276c1c9f9f738d2a20f484fa4eea9d` |
| Cargo host | `x86_64-pc-windows-msvc` |
| Rust active toolchain | `stable-x86_64-pc-windows-msvc` |
| target | `x86_64-pc-windows-msvc` |
| OS | Windows 11 Professional, build `26200` |
| Cargo environment variables | None matching `CARGO_*` or `RUST*` were reported |
| User `.cargo` file count | 17,525 files |

The `.cargo` file count is recorded only as an audit observation. It is **not** part of `R` and MUST NOT be treated as scientific input. In particular, Cargo cache/index contents are not implicitly frozen by this count.

## 3. Configuration boundary

The following configuration surface remains to be explicitly inspected before freeze:

- user-level Cargo configuration (`%USERPROFILE%\\.cargo\\config.toml` / legacy `config`);
- project/local Cargo configuration (`.cargo\\config.toml` / legacy `config`);
- relevant parent-directory Cargo configuration discovered by Cargo's configuration hierarchy;
- source replacement and registry configuration;
- any other configuration that can alter dependency resolution.

If no such configuration exists, that negative result MUST be recorded explicitly.

No unspecified setting may silently affect the accessibility result.

## 4. Resolver generation

The resolver generation MUST be determined from the exact manifest used by the experiment and recorded explicitly. The C3 project manifest uses Rust edition 2021; the final fixture MUST additionally record the effective Cargo resolver generation rather than infer it from edition alone.

## 5. Registry policy

- Registry: crates.io historical index.
- Historical snapshot: explicit dated snapshot supplied as `C_t`.
- Live registry access: **PROHIBITED** during historical accessibility computation.
- Current index substitution: **PROHIBITED**.
- Future package versions: **PROHIBITED**.
- Source replacement: none unless explicitly recorded in this artifact.

## 6. Candidate-resolution policy

For the minimal confirmatory ontology:

- dependency kind: normal;
- target condition: unconditional;
- optional: false;
- candidate feature set: empty;
- candidate requirement: exact version `=v`;
- one dependency edge inserted per candidate;
- path/git dependencies excluded;
- dev/build dependencies excluded.

## 7. Resolver semantics to freeze

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
10. environment variables affecting Cargo resolution;
11. isolation policy for Cargo home, registry index and crate cache;
12. fail-closed behaviour when any required frozen input is absent.

## 8. Local-state non-contamination rule

The scientific accessibility result MUST be invariant to unrelated user-local Cargo state.

Therefore the execution harness MUST either:

- construct an isolated Cargo home/cache containing only explicitly frozen inputs; or
- prove that every accessed local artifact is an explicit member of the frozen `C_t`/`R` package and is hash-identified.

The ambient `%USERPROFILE%\\.cargo` directory is not an admissible implicit input.

## 9. Deterministic invocation

The implementation must invoke resolution in an isolated directory using only frozen `S_t`, `C_t`, and `R` inputs.

The implementation MUST fail closed if:

- the historical registry snapshot is unavailable;
- the live registry is contacted;
- an unspecified source replacement is detected;
- a required resolver parameter is missing;
- an ambient local cache is required to obtain a result that is not explicitly frozen.

## 10. Reproducibility record

The final freeze package must include:

- this specification;
- environment capture output;
- configuration files used for resolution;
- hashes of all frozen inputs;
- deterministic invocation record;
- expected machine-readable output;
- repeat-run comparison showing byte-identical output;
- explicit record of the isolated Cargo home/cache used by the fixture.

## 11. Freeze status

**NOT FROZEN.**

Toolchain, host, target and environment-variable capture are complete. The remaining prerequisite is explicit Cargo configuration/resolver inspection, followed by fixture execution and hashing.
