# EXT-1.1 Rust — Resolver Reconstruction v0.2

**Date:** 2026-08-30
**Status:** TOOLING PREPARED — EXECUTION PENDING
**Related:** CHR-MICRO-3_AMENDMENT_v0.2; HRSV v0.2

## Action completed

A deterministic snapshot-only candidate-universe replay tool has been added at:

`tools/replay_snapshot_resolver.py`

The tool consumes only a local newline-delimited crates.io index snapshot and explicitly rejects network/current-state inputs. It filters non-yanked releases and currently implements caret requirement candidate enumeration.

## Scope limitation

This is intentionally a **candidate-universe replay scaffold**, not yet a full Cargo resolver equivalence test. It does not claim to reproduce Cargo's complete feature unification, target-specific dependency activation, build/dev dependency semantics, resolver-version behavior, or lockfile selection.

Therefore it cannot yet produce a CHR PASS.

## Next execution

1. Materialize the three declared archived snapshot records and all dependency records required by the selected micro-slice.
2. Run the tool against those local snapshots.
3. Compare its candidate universe with a pinned Cargo resolver execution in an isolated historical registry environment.
4. Record exact resolver version/configuration and output.
5. Independently establish the version-ID bridge.

**Current verdict:** C remains BLOCKED pending executable full-resolution equivalence; D remains BLOCKED pending independent identity bridge.

**EXT-1.1 FREEZE remains BLOCKED.**
