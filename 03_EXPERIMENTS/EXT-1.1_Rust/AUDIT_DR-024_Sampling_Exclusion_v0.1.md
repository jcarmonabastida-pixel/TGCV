# AUDIT DR-024 — EXT-1.1 Rust Sampling / Exclusion v0.1

**Status:** PASS — STRUCTURAL AUDIT  
**Execution:** local user run on frozen Rust dataset  
**Mode:** PRE-CONFIRMATORY / STRUCTURAL ONLY  
**Horizon:** `H = 180` elapsed days (accepted by DR-023)

## 1. Execution evidence

Dataset ZIP:

`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

Audit implementation:

`src/audit_dr024_sampling_exclusion_v01.py`

No extraction was performed and the complete dataset was not loaded into memory.

## 2. Structural observations

- `PACKAGE_VERSION_ROWS`: 607,498
- `VALID_CREATED_AT_ROWS`: 607,498
- `MISSING_CREATED_AT_ROWS`: 0
- `INVALID_CREATED_AT_ROWS`: 0
- `MISSING_REQUIRED_IDENTITY_FIELDS`: 0
- `DUPLICATE_VERSION_IDS`: 0

The required observational fields were therefore structurally complete for the audited release table.

## 3. Follow-up eligibility

Snapshot boundary:

`2022-09-07 01:50:04.004956`

Eligibility rule:

`origin_created_at + 180d <= snapshot_max_created_at`

Results:

- complete 180-day follow-up: **507,279** origins;
- incomplete 180-day follow-up: **100,219** origins;
- eligible origins: **507,279**.

Incomplete follow-up is excluded only because the pre-specified outcome cannot be observed completely. It is not coded as outcome zero.

## 4. Exclusion-policy audit

All prohibited selection channels were absent from the audit:

- outcome used for exclusion: `False`;
- `T_acc` used for exclusion: `False`;
- `R*` used for exclusion: `False`;
- baseline `B` used for exclusion: `False`;
- downloads/adoption used for exclusion: `False`;
- post-origin activity used for exclusion: `False`;
- manual package selection: `False`;
- pilot/confirmatory results used: `False`;
- substantive package characteristics used: `False`.

## 5. Census / sampling result

The audit establishes the following methodological state:

- census-first principle: `True`;
- sampling required by the structural audit: `False`;
- `N` selected: `False`;
- random seed selected: `False`.

Therefore the accepted analytical population is the deterministic census of the 507,279 structurally valid package releases with complete 180-day follow-up, subject to any later separately justified computational feasibility decision. No sample has been selected.

## 6. Determinism

A replay of the same deterministic classification returned:

`REPLAY_COMPLETE_FOLLOWUP_ORIGINS = 507,279`

matching the first pass exactly.

`DETERMINISTIC_CLASSIFICATION = True`

## 7. Prohibited computations confirmed absent

The audit did not compute:

- outcome prevalence;
- `T_acc`;
- associations;
- effect sizes;
- significance tests;
- baseline `B`;
- sample size selection;
- random seed selection.

## 8. Decision

`DR024_STRUCTURAL_AUDIT_PASS = True`

The audit satisfies the structural acceptance requirement defined by DR-024. The ex-ante eligibility/exclusion policy is deterministic, reconstructible, and independent of post-origin outcomes and predictor-derived quantities.

**DR-024 acceptance:** `ACCEPTED — NEW EXPERIMENTAL DECISION`

**Important boundary:** acceptance of DR-024 fixes the analytical population rule; it does not authorize confirmatory execution, does not select a sample, and does not by itself establish that full census computation of later `T_acc`/predictor representations is computationally optimal. Any computationally necessary sampling decision requires a separate ex-ante gate.
