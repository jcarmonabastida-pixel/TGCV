# EXT-1.1 Rust — CHR-MICRO-3 Execution v0.1

**Date:** 2026-08-30
**Protocol:** CHR-MICRO-3_GATE_v0.1
**Execution status:** COMPLETED TO AVAILABLE-EVIDENCE LIMIT

## Cases

The micro-slice was instantiated with three historical crate releases chosen to span increasing resolution complexity, without using downstream outcome as a selection criterion:

- **C1:** `serde@1.0.0` — simple historical case.
- **C2:** `tokio@1.0.0` — multi-dependency case with several compatible candidate ranges.
- **C3:** `rand@0.8.0` — interdependent dependency family with multiple semver-constrained candidates.

## Evidence

### C1 — serde@1.0.0

The release is historically identifiable; public documentation records `serde 1.0.0` as released 2017-04-20. The registry-index schema exposes version-specific dependency metadata, and the public index is the authoritative registry metadata source.

### C2 — tokio@1.0.0

Public historical documentation records the release as 2020-12-23 and lists its normal dependency constraints, including `mio ^0.7.6`, `parking_lot ^0.11.0`, `pin-project-lite ^0.2.0`, `tokio-macros ^1.0.0`, etc. The release was subsequently yanked; that later fact is not used as a resolution input for the historical release itself.

### C3 — rand@0.8.0

Public historical documentation records the release as 2020-12-18 and lists its dependency constraints, including `rand_core ^0.6.0`, `rand_chacha ^0.3.0`, `rand_hc ^0.3.0`, `libc ^0.2.22`, `serde ^1.0.103`, and others.

## Gate assessment

| Case | A Identity | B Temporal availability | C Reproducibility | D No leakage | E Registry bridge | F T_acc construction |
|---|---|---|---|---|---|---|
| C1 serde@1.0.0 | PASS | PASS for release identity; dependency candidate resolution not fully demonstrated | OPEN | PASS | OPEN | OPEN |
| C2 tokio@1.0.0 | PASS | PASS for release identity; dependency candidate resolution not fully demonstrated | OPEN | PASS | OPEN | OPEN |
| C3 rand@0.8.0 | PASS | PASS for release identity; dependency candidate resolution not fully demonstrated | OPEN | PASS | OPEN | OPEN |

## Critical finding

The currently recoverable public evidence establishes release identity, release chronology and dependency constraints, but does **not yet establish reproducible historical dependency resolution from a time-indexed registry state** for all three cases. In particular, the available path does not provide a directly auditable historical crates.io index snapshot sufficient to prove the exact candidate universe and resolver result at each cutoff, nor has the `package@version → registry version_id` bridge been independently demonstrated for the three cases.

This is a substantive gap, not a convention. Therefore CHR-MICRO-3 cannot be declared PASS on the current evidence.

## Verdict

**FAIL / BLOCKED — historical resolution reproducibility not demonstrated.**

This verdict does **not** establish that the Cargo-native route is impossible. It establishes that the present acquisition/evidence path is insufficient to pass the chrono-resolution gate. A recoverable historical index snapshot (or an equivalently auditable historical reconstruction) is required before proceeding to minimal confirmatory extraction.

## Consequence

- Full EXT-1.1 extraction remains blocked.
- EXT-1.1 FREEZE remains blocked.
- No outcome variable is used to repair or infer the missing historical resolution.
- The next action is an acquisition/reconstruction sub-gate specifically targeting the historical registry/index state and the version_id bridge.
