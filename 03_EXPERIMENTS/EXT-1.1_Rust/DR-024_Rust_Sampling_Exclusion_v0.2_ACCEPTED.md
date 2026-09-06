# DR-024 — EXT-1.1 Rust Sampling / Exclusion v0.2

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION  
**Supersedes design proposal:** `DR-024_Sampling_Exclusion_ExAnte_Design_v0.1.md`  
**Audit:** `AUDIT_DR-024_Sampling_Exclusion_v0.1.md`  
**Experiment:** EXT-1.1 Rust  
**Date:** 2026-09-06

## Decision

The EXT-1.1 analytical population is defined as the deterministic census of Rust package releases satisfying the frozen structural eligibility rules and complete follow-up for the accepted DR-023 horizon `H = 180` elapsed days.

Observed eligible population:

`N_eligible = 507,279` package-release origins.

No confirmatory sample is selected. No random seed is selected.

## Eligibility

An origin release is eligible when:

1. canonical package identity is present and valid;
2. release identity/version information is present and valid;
3. `created_at` is present and valid;
4. `origin_created_at + 180d <= snapshot_max_created_at`.

The frozen dataset snapshot boundary is:

`2022-09-07 01:50:04.004956`

## Structural audit result

The audit processed 607,498 package-version observations and found:

- missing `created_at`: 0;
- invalid `created_at`: 0;
- missing required identity fields: 0;
- duplicate version IDs: 0;
- complete 180-day follow-up: 507,279;
- incomplete 180-day follow-up: 100,219.

The deterministic eligibility classification was reproduced exactly on replay.

`DR024_STRUCTURAL_AUDIT_PASS = True`

## Exclusion policy

No exclusion or selection may depend on outcome, subsequent activity, `T_acc`, `R*`, baseline `B`, downloads, adoption, popularity, downstream success, manual package selection, or confirmatory/pilot results.

Incomplete follow-up is excluded solely because the pre-specified outcome cannot be observed completely at `H = 180`; it is never coded as outcome zero.

## Sampling policy

Census-first is accepted. Sampling is not currently required by the structural audit.

This decision does **not** prohibit a later sampling decision if a distinct ex-ante computational feasibility gate establishes that census computation is impracticable or methodologically inferior. Such a decision would require its own frozen N, randomization mechanism, seed, and eligibility frame before confirmatory outcome analysis.

## Confirmatory boundary

DR-024 acceptance does not authorize confirmatory execution by itself. The analytical population is now frozen, but remaining pre-confirmatory gates must still be completed before any outcome/predictor association or final confirmatory run.
