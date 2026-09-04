# EXT-1.1 Rust — Resolver Specification `R` v0.1

**Status:** DRAFT — configuration audit negative; resolver policy boundary frozen; fixture execution required before scientific freeze
**Purpose:** Freeze the deterministic resolution semantics used by the `T_acc` identifiability experiment.

## 1. Role

`R` is an explicit input to the measurement function:

`T_acc,t = F(S_t, C_t, R)`

This artifact is intentionally separate from package state `S_t` and historical registry context `C_t`.

`R` specifies resolver semantics and execution constraints. It MUST NOT silently include the user's incidental Cargo cache, registry cache, filesystem state, or other machine-local state.

## 2. Captured execution environment

Captured from the actual EXT-1.1/C3 execution environment:

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
| `CARGO_*` / `RUST*` environment variables | None reported |
| ambient `%USERPROFILE%\\.cargo` file count | 17,525 |

The `.cargo` file count is an audit observation only. It is **not** part of `R` and MUST NOT be treated as scientific input.

## 3. Cargo configuration audit

The following checks were performed from the isolated C3 environment:

- `%USERPROFILE%\\.cargo\\config`
- `%USERPROFILE%\\.cargo\\config.toml`
- configuration files in the current project directory
- `.cargo` configuration in the current project tree

**Observed result:** no matching Cargo configuration files were reported by the performed probes.

The stable Cargo channel rejected `cargo -Z unstable-options config get`; this is an expected channel limitation, not evidence of a configuration value. Therefore configuration absence is established only for the paths actually probed, not as a universal claim about every possible Cargo configuration mechanism.

Before scientific fixture freeze, the execution harness MUST still construct its own explicit configuration and isolated Cargo home so that resolution does not depend on ambient configuration discovery.

## 4. Resolver generation

The C3 manifest is:

```toml
[package]
name = "tgcv_cargo_probe_c3"
version = "0.1.0"
edition = "2021"

[dependencies]
rand = "=0.8.0"
```

The scientific fixture MUST NOT infer resolver semantics from edition alone. Its manifest MUST declare the resolver generation explicitly. The chosen generation for the confirmatory fixture is **Cargo resolver 2**, declared as:

```toml
[package]
resolver = "2"
```

This explicit declaration is part of the frozen fixture input, rather than an assumption about ambient Cargo defaults.

## 5. Registry policy

- Registry: crates.io historical index represented by the frozen fixture context `C_t`.
- Historical snapshot: explicit dated snapshot supplied as `C_t`.
- Live registry access: **PROHIBITED** during historical accessibility computation.
- Current index substitution: **PROHIBITED**.
- Future package versions: **PROHIBITED**.
- Source replacement: none unless explicitly recorded in the fixture's frozen configuration.

## 6. Candidate-resolution policy

For the minimal confirmatory ontology:

- dependency kind: normal;
- target condition: unconditional;
- optional: false;
- candidate feature set: empty;
- candidate requirement: exact version `=v`;
- one dependency edge inserted per candidate;
- path/git dependencies excluded;
- dev/build dependencies excluded;
- workspace inheritance excluded;
- target-specific and feature-dependent dependencies excluded.

## 7. Resolver semantics to freeze

The confirmatory fixture MUST explicitly record:

1. resolver generation: Cargo resolver 2;
2. exact Cargo version: `1.98.1 (797e8a9bc 2026-08-05)`;
3. exact Rust toolchain: `stable-x86_64-pc-windows-msvc`, rustc `1.98.1 (48a229cea 2026-09-01)`;
4. target/platform: `x86_64-pc-windows-msvc`;
5. feature policy: empty candidate feature set;
6. yanked-version policy: yanked candidate versions excluded from the fixture candidate universe;
7. registry source: frozen historical local registry/index context only;
8. lockfile mode: generated deterministically from the frozen manifest/context, with no live registry access;
9. Cargo configuration: explicitly supplied by the fixture harness; no ambient source replacement permitted;
10. environment variables: no `CARGO_*` or `RUST*` variables were present in the captured environment; the harness MUST reject undeclared resolution-affecting variables;
11. Cargo home/index/cache isolation: explicit isolated paths only;
12. fail-closed behaviour whenever a required frozen input is absent.

## 8. Local-state non-contamination rule

The scientific accessibility result MUST be invariant to unrelated user-local Cargo state.

Therefore the execution harness MUST construct an isolated Cargo home/cache containing only explicitly frozen inputs. The ambient `%USERPROFILE%\\.cargo` directory is not an admissible implicit input.

The C3 portability probe already demonstrated why this matters: an isolated copy of the C3 project could not resolve `rand_hc` without the historical index/cache context. This is treated as evidence about C3 portability, not as scientific Rust dataset evidence.

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
- explicit fixture Cargo configuration;
- hashes of all frozen inputs;
- deterministic invocation record;
- expected machine-readable output;
- repeat-run comparison showing byte-identical output;
- explicit record of the isolated Cargo home/cache used by the fixture.

## 11. Freeze status

**NOT YET SCIENTIFICALLY FROZEN.**

The environment capture and configuration audit are complete enough to define the resolver boundary. The remaining gate is executable fixture construction and verification: exact fixture registry records, isolated Cargo home/index, A/B/C execution, deterministic two-run comparison, and hashes.

No scientific Rust dataset processing is authorised before that gate passes.
