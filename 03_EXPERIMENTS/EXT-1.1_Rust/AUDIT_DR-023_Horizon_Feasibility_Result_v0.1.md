# EXT-1.1 Rust — DR-023 Horizon Feasibility Audit Result v0.1

**Status:** PASS — STRUCTURAL FEASIBILITY EVIDENCE
**Execution:** local user run on frozen Rust dataset
**Mode:** PRE-CONFIRMATORY / STRUCTURAL ONLY
**Decision:** DR-023

## 1. Execution evidence

Dataset ZIP:

`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

Horizon grid:

`H ∈ {30, 90, 180, 365}` days

The grid was treated strictly as a set of design candidates. No primary horizon was selected by the audit.

## 2. Dataset temporal coverage

- `PACKAGE_VERSION_ROWS`: 607,498
- `VALID_CREATED_AT_ROWS`: 607,498
- `MISSING_CREATED_AT_ROWS`: 0
- `MIN_CREATED_AT`: 2014-11-11 00:22:07.370652
- `MAX_CREATED_AT`: 2022-09-07 01:50:04.004956
- `OBSERVED_SPAN_DAYS`: 2857.061072156296

## 3. Horizon coverage

Observation-coverage counts only; no outcome event was searched or labelled.

| Horizon | Complete follow-up | Incomplete follow-up | Coverage | Structural feasibility |
|---|---:|---:|---:|---|
| 30d | 589,846 | 17,652 | 0.970943 | PASS |
| 90d | 555,636 | 51,862 | 0.914630 | PASS |
| 180d | 507,279 | 100,219 | 0.835030 | PASS |
| 365d | 416,112 | 191,386 | 0.684960 | PASS |

## 4. Firewall / non-contamination

The execution explicitly confirmed:

- `PRIMARY_HORIZON_SELECTED = False`
- `OUTCOME_LABELS_COMPUTED = False`
- `OUTCOME_PREVALENCE_COMPUTED = False`
- `TACC_COMPUTED = False`
- `ASSOCIATIONS_COMPUTED = False`
- `EFFECT_SIZES_COMPUTED = False`
- `SAMPLING_DECISION_COMPUTED = False`
- `BASELINE_B_COMPUTED = False`
- `R_SERIALIZATION_COMPUTED = False`
- `HORIZON_SELECTION_BY_STATISTICAL_CRITERION = False`

## 5. Result

`DR023_HORIZON_FEASIBILITY_AUDIT_PASS = True`

All four pre-declared horizons are structurally feasible in the frozen snapshot. The result does not rank or select them.

## 6. Governance consequence

The structural feasibility sub-gate of DR-023 is now closed as PASS. DR-023 itself remains OPEN pending an explicit ex-ante methodological decision freezing:

`Outcome + primary horizon H + follow-up/censoring rule`.

The already recorded DR-024 population rule uses `H = 180` days, but that does not substitute for the required ex-ante scientific selection of the primary horizon within DR-023.

No confirmatory execution is authorized by this evidence record.

## 7. Reproducibility

No extraction was performed and no complete dataset was loaded into memory. The execution was structural only.
