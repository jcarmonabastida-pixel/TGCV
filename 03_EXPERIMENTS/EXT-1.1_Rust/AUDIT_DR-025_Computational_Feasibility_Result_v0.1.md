# AUDIT DR-025 — Computational Feasibility Result v0.1

**Status:** PASS  
**Date:** 2026-09-07  
**Mode:** COMPUTATIONAL_FEASIBILITY_STRUCTURAL_ONLY

## 1. Execution result

`EXECUTION_RESULT=PASS`

The deterministic computational-feasibility audit establishes that the frozen EXT-1.1 Rust primary analytical population can be enumerated as a complete census under the current local execution environment.

## 2. Frozen analytical population

- Primary horizon: `H = 180` days
- Snapshot maximum: `2022-09-07 01:50:04.004956`
- Complete-follow-up cutoff: `2022-03-11 01:50:04.004956`
- Package-version rows: `607,498`
- Complete-followup origins: `507,279`
- Incomplete/right-censored origins: `100,219`
- Target population: `507,279`
- Frozen target matched: `true`

## 3. Computational observations

- Dataset member processed directly from the ZIP: `rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv`
- Compressed member size: `10,799,750` bytes
- Uncompressed member size: `28,140,303` bytes
- Python: `3.14.7`
- Platform: Windows 11
- Wall-clock time: `3.112532` seconds
- Full dataset materialized in memory: `false`
- Deterministic census: `true`

Peak working-set memory was not available from this execution (`null`). Therefore DR-025 establishes feasibility by successful streaming census enumeration and absence of full in-memory materialization, but does not claim a measured peak RSS value.

## 4. Integrity and methodological firewall

The execution reported:

- invalid created_at pass 1: `0`
- invalid created_at pass 2: `0`
- outcome computed: `false`
- outcome prevalence computed: `false`
- association computed: `false`
- effect size computed: `false`
- T_acc used for selection: `false`
- Reach used for selection: `false`
- R* used for selection: `false`
- B used for selection: `false`
- adaptive sampling: `false`
- sampling performed: `false`
- confirmatory analysis: `false`

## 5. Decision

**DR-025 = PASS.**

The frozen primary population of `507,279` origins is computationally feasible for deterministic census enumeration on the tested local environment. No computational sampling gate is therefore required at this stage.

This decision does **not** authorize confirmatory outcome analysis. It only closes the computational-feasibility gate for the already frozen analytical population.

## 6. Consequence for EXT-1.1

The primary analytical population remains the complete set of `507,279` origins with complete 180-day follow-up. The `100,219` incomplete origins remain right-censored/ineligible and must not be recoded as outcome `0`.

The next gate must concern the exact confirmatory computation specification and its implementation/conformance, not population selection or computational sampling.
