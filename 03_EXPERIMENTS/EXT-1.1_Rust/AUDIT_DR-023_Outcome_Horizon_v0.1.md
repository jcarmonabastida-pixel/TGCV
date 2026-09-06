# EXT-1.1 Rust — DR-023 Outcome / Horizon Structural Audit v0.1

**Status:** EVIDENCE RECORD — STRUCTURAL GATE PASSED; DR-023 REMAINS OPEN

**Audit implementation:** `src/audit_dr023_outcome_v01.py` v0.2  
**Implementation SHA:** `6430055412837863cf9353a2385ec9332507f2e6`  
**Dataset:** `rust_repos_2022_09_07.zip`  
**Execution mode:** PRE-CONFIRMATORY / STRUCTURAL ONLY

## 1. Purpose

This record preserves the local execution evidence for the DR-023 structural audit. The audit asks whether the frozen Rust snapshot contains the pre-outcome fields needed to define and reconstruct a subsequent observable outcome and a fixed observation horizon without deriving the outcome from `T_acc`, `R*`, `B`, or other predictor-derived quantities.

This record does **not** select the final outcome, does **not** select the primary horizon length, and does **not** authorize confirmatory execution.

## 2. User execution result

The audit was executed locally against the frozen ZIP snapshot. The observed output was:

```text
TGCV EXT-1.1 — DR-023 outcome/horizon structural audit v0.2
ZIP: C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip
MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY
TOTAL FILES: 73

O1_pre_outcome_reconstructable: PASS
  Accepted DR-020/021 pre-outcome schema is present under the frozen Rust dump's actual column names.
O2_temporal_ordering_support: PASS
  package_versions.created_at supplies the release timestamp used for post-origin ordering.
O3_non_circularity_with_tacc: PASS
  Candidate outcome events are later package-version events, not accessibility states or dependency constraints.
O4_outcome_not_predictor_derived: PASS
  Candidate outcomes do not use T_acc, R*, B, or any predictor-derived quantity.
O5_deterministic_reconstruction: PASS
  Given frozen package/version tables, later-release event membership is a deterministic timestamp comparison.
CANDIDATE_STRUCTURAL_SUPPORT subsequent_release_activity: PASS
CANDIDATE_STRUCTURAL_SUPPORT later_package_state_transition: PASS
O6_horizon_feasibility_support: PASS
  package_versions.created_at observed range: 2014-11-11 00:22:07.370652 .. 2022-09-07 01:50:04.004956
  A post-origin window is structurally measurable; the primary horizon length remains OPEN and must be frozen ex ante.
O7_no_future_leakage_in_candidate_inputs: PASS
  No prohibited downstream/outcome fields are used by the structurally feasible candidate definitions.
O8_incremental_trajectory_relevance: NOT TESTED
  This cannot be decided from structural availability and must not be optimized using confirmatory results.
O9_minimality: PASS
  The audit introduces no proxy outcome, threshold, sampling rule, baseline, or selected horizon.

CANDIDATE_OUTCOME_FAMILIES:
  - subsequent_release_activity
  - later_package_state_transition

DR023_STRUCTURAL_AUDIT_PASS: True
DR023_DECISION_STATUS: OPEN_PENDING_EX_ANTE_OUTCOME_AND_HORIZON_SELECTION
No outcome labels, associations, significance tests, sampling decisions, B encoding, or R serialization were computed.

DONE.
No extraction was performed.
No complete dataset was loaded into memory.
```

## 3. Audit interpretation

The structural gate is **PASS**.

The result establishes that the frozen snapshot supports at least two deterministic, post-origin candidate outcome families:

1. `subsequent_release_activity`
2. `later_package_state_transition`

Both are reconstructable from package-version metadata and do not require `T_acc`, `R*`, `B`, downloads, adoption, popularity, or other outcome-derived quantities.

The timestamp range demonstrates structural support for a post-origin observation window. It does **not** justify any particular horizon length.

## 4. Explicit non-decisions

The following remain OPEN and were not resolved by this audit:

- final outcome family;
- primary horizon length `H`;
- censoring / complete-follow-up rule;
- sampling and exclusion rules;
- pilot `N` and seed;
- baseline `B` encoding;
- `R` serialization.

In particular, no horizon such as 30, 90, 180, or 365 days is implied by this evidence record.

## 5. Governance consequence

DR-023 may now proceed to a separate **ex ante outcome-and-horizon design decision**. That decision must be justified independently of confirmatory associations and must freeze:

`Outcome + primary horizon H + follow-up/censoring rule`

before confirmatory execution.

No confirmatory result may be inspected or optimized in order to choose among candidate outcomes or horizon lengths.

## 6. Reproducibility / scope

The audit implementation streams the ZIP and reads only the required schema/timestamp information. It does not extract the archive or load the complete dataset into memory. The audit is structural and pre-confirmatory; it does not estimate any outcome label or association.

**Conclusion:** `DR023_STRUCTURAL_AUDIT_PASS = True`; `DR-023` remains **OPEN** pending an explicit ex ante selection of outcome, horizon, and follow-up/censoring rule.
