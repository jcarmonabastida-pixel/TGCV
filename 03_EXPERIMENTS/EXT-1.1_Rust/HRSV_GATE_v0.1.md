# EXT-1.1 Rust — HRSV Gate v0.1

**HRSV:** Historical Registry State & Version-ID Gate
**Date:** 2026-08-30
**Status:** EXECUTED — FAIL / BLOCKED
**Parent:** EXT-1.1_Rust
**Predecessor:** CHR-MICRO-3 (FAIL/BLOCKED on available evidence)

## Purpose
Resolve the specific evidential blockage identified by CHR-MICRO-3 without changing the TGCV ontology or using outcome data retrospectively.

## Questions

### HRSV-A — Historical registry state
Can the crates.io index Git history provide an auditable registry state at each required cutoff?

### HRSV-B — Candidate universe
Given that historical state, can all candidate releases satisfying each dependency constraint be enumerated using only information available at the cutoff?

### HRSV-C — Deterministic resolution
Can the historical candidate universe be resolved deterministically under the declared Cargo/semver resolution rule, without current-state leakage?

### HRSV-D — Version-ID bridge
Can each resolved `package@version` be mapped reproducibly to the crates.io `version_id` used by the historical daily download archive, without using downloads/outcomes to establish the mapping?

## Evidence hierarchy

1. Historical crates.io index Git state / commit history.
2. Official crates.io version metadata/API where used only for identity cross-checks.
3. Official archived daily version-download CSVs, used only after identity mapping and never as a resolution input.
4. Secondary documentation only as corroboration, never as sole evidence for a gate-critical historical fact.

## Execution findings

### HRSV-A — Historical registry state: FAIL

The current public `rust-lang/crates.io-index` Git repository exposes the index as a Git repository, but the accessible commit history has been collapsed into a current snapshot commit. The repository's commit for the current snapshot explicitly states that the previous HEAD was moved to `snapshot-2026-08-19` and the resulting commit has no parent. Direct historical-path queries for the three micro-slice files return no commits at the required historical cutoffs.

Therefore the current Git history cannot provide an auditable registry state for the 2017/2020 cutoffs needed by C1-C3.

### HRSV-B — Candidate universe: FAIL / NOT IDENTIFIABLE FROM CURRENT INDEX HISTORY

Current index entries expose publication timestamps and dependency metadata, but these do not reconstruct the historical index state or historical yank state at each cutoff. A current-state entry cannot be treated as proof that the same entry/yank status was observable at the historical cutoff.

### HRSV-C — Deterministic resolution: BLOCKED

Cargo/semver rules are deterministic when supplied with a valid historical candidate universe. The Cargo documentation confirms that version requirements define the candidate range. However, because HRSV-B cannot supply the exact historical candidate universe and yank state, deterministic historical resolution cannot be demonstrated without leakage or an unsupported reconstruction assumption.

### HRSV-D — Version-ID bridge: PARTIAL / NOT YET PROVEN

The official crates.io daily download archive confirms that its files contain `version_id` and daily download counts. This establishes the outcome-side identifier format. The present evidence does not independently establish the exact `package@version → version_id` mapping for all three cases in a reproducible, gate-ready manner.

## Case assessment

| Case | A | B | C | D | Evidence / notes |
|---|---|---|---|---|---|
| C1 serde@1.0.0 | FAIL | FAIL | BLOCKED | PARTIAL | Historical index path has no accessible pre-cutoff commit history. |
| C2 tokio@1.0.0 | FAIL | FAIL | BLOCKED | PARTIAL | Same historical-state limitation. |
| C3 rand@0.8.0 | FAIL | FAIL | BLOCKED | PARTIAL | Same historical-state limitation. |

## Verdict

**HRSV = FAIL / BLOCKED.**

This is an acquisition/evidence failure, not a finding that the Cargo-native route or TGCV is invalid. The missing object is a recoverable historical registry state (or an independently auditable archival equivalent) sufficient to reconstruct candidate universes and historical resolution.

## Consequences

- CHR-MICRO-3 remains FAIL/BLOCKED.
- CARGO_NATIVE_ROUTE remains OPEN.
- EXT-1.1 FREEZE remains BLOCKED.
- No T freeze is authorized.
- No downloads/outcomes are used to infer missing historical resolution.

## Next gate

Open a dedicated **Historical Index Archive Recovery Gate (HIAR)** to determine whether an external archival copy, snapshot, release artifact, or other independently auditable source can recover the required pre-cutoff registry states. If HIAR fails, EXT-1.1 should be assessed for empirical identifiability under an alternative domain/acquisition route rather than relaxing the temporal gate.
