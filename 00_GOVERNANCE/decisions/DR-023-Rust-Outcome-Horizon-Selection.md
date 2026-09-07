# DR-023 — Rust outcome and primary horizon selection

**Status:** ACCEPTED
**Date:** 2026-09-07
**Experiment:** EXT-1.1_Rust
**Decision type:** Ex-ante methodological design

## Decision

For EXT-1.1 Rust, the primary outcome is frozen as **`subsequent_release_activity`** and the primary observation horizon is frozen as **H = 180 elapsed days**.

The primary analytical population consists of origins with complete 180-day follow-up in the frozen snapshot. Origins without complete follow-up are excluded from the primary analysis as right-censored/incomplete observations and are **never coded as outcome = 0**.

`later_package_state_transition` is not the primary outcome because it is redundant with the intended observable release-activity event at the level required for the primary empirical test; it may remain auxiliary/descriptive only if later required by the protocol.

## Ex-ante rationale

### Outcome

`subsequent_release_activity` is selected because it is directly observable in the frozen temporal dataset, has an explicit temporal ordering relative to the origin, can be reconstructed without using `T_acc`, `Reach`, `R*`, `B`, or predictor-derived quantities, and provides a minimal subsequent-state outcome suitable for testing the empirical relation under study.

### Horizon

H = 180 days is selected ex ante as the primary horizon because it provides a medium-term observation window while retaining a large deterministic complete-follow-up population. The feasibility audit showed that all candidate horizons {30, 90, 180, 365} are structurally feasible, with complete-follow-up coverage of 97.0943%, 91.4630%, 83.5030%, and 68.4960%, respectively. The 180-day choice is therefore a methodological design choice balancing temporal distance against observation completeness, **not** a choice optimized using outcome prevalence, association, effect size, significance, T_acc, Reach, or any confirmatory result.

## Follow-up and censoring rule

An origin is complete for H = 180 days iff:

`created_at(origin) + 180 days <= snapshot_max_created_at`.

Incomplete origins are right-censored/ineligible for the primary fixed-horizon analysis. They are not assigned negative outcome labels.

The resulting deterministic complete-follow-up population is 507,279 origins, with 100,219 incomplete origins excluded from the primary fixed-horizon population.

## Anti-leakage constraints

This decision was made without computing:

- outcome labels or outcome prevalence;
- associations or effect sizes;
- statistical significance or model performance;
- `T_acc`, `Reach`, `B`, or `R` for horizon selection;
- sampling based on observed outcomes or predictors.

No confirmatory execution is authorized merely by this decision.

## Governance consequence

DR-023 is now **CLOSED / ACCEPTED**. The primary outcome, primary horizon, and fixed-horizon follow-up/censoring rule are frozen for EXT-1.1.

The next gate is the computational feasibility / population execution decision for the deterministic 507,279-origin analytical population, followed by pilot/confirmatory preparation as separately authorized.

## Evidence

- `03_EXPERIMENTS/EXT-1.1_Rust/AUDIT_DR-023_Outcome_Horizon_v0.1.md`
- `03_EXPERIMENTS/EXT-1.1_Rust/AUDIT_DR-023_Horizon_Feasibility_v0.1.md`
- `03_EXPERIMENTS/EXT-1.1_Rust/AUDIT_DR-023_Horizon_Feasibility_Result_v0.1.md`
- `03_EXPERIMENTS/EXT-1.1_Rust/AUDIT_DR-024_Sampling_Exclusion_v0.1.md`

## Scope boundary

This decision freezes outcome/horizon/follow-up design only. It does not by itself freeze computational sampling, baseline representation, final `R` serialization, confirmatory model specification, or confirmatory results.
