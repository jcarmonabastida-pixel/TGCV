# AUDIT — DR-025A EXT-1.1 Rust Baseline B Representation v0.1

**Audit status:** PASS  
**Decision status:** OPEN PENDING FORMAL ACCEPTANCE  
**Execution mode:** PRE-CONFIRMATORY / STRUCTURAL ONLY  
**Horizon context:** 180 elapsed days (DR-023)  
**Date:** 2026-09-06

## 1. Purpose

Audit the concrete ex-ante representation specified by `DR-025A_Rust_Baseline_Representation_ExAnte_v0.1.md` for deterministic reconstruction, temporal safety and separation from `T_acc^(R*)`, `R*` and the post-origin outcome.

## 2. Input

Frozen Rust dataset ZIP:
`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

The audit streamed `package_versions.csv` and `package_dependencies.csv` directly from the ZIP. No extraction was performed and no complete raw dataset was loaded into memory.

## 3. Observed structural results

- package-version rows: **607,498**
- valid `created_at`: **607,498**
- invalid `created_at`: **0**
- missing required identity fields: **0**
- duplicate version IDs: **0**
- non-empty `version_str`: **607,498**
- dependency declaration rows: **3,618,523**
- dependency rows with missing origin: **0**
- packages represented: **91,437**
- reconstructed historical rows: **607,498**
- chronology violations: **0**

## 4. Representation checks

The audit reconstructed the four primary baseline components:

1. `V_o`: `version_str` as nominal categorical release-state attribute;
2. `prior_release_count_o`: number of earlier releases of the same package using strict timestamp precedence;
3. `package_age_days_o`: elapsed time from earliest observed release of the package to origin;
4. `D_o`: number of raw dependency declaration rows attached to the origin release.

No SemVer resolution was performed for the baseline.

## 5. Non-circularity and leakage checks

All structural checks passed:

- B1 pre-origin boundary: **True**
- B2 outcome independent: **True**
- B3 `T_acc` independent: **True**
- B4 `R*` independent: **True**
- B5 no future leakage: **True**
- B6 deterministic: **True**
- B7 domain valid: **True**
- B8 ex ante fixed: **True**
- B9 minimality: **REVIEWED CANDIDATE**

Prohibited/leakage flags were all false:

- `TACC_AS_FEATURE`: False
- `RSTAR_AS_FEATURE`: False
- `OUTCOME_AS_FEATURE`: False
- `POST_ORIGIN_DATA_AS_FEATURE`: False
- `PACKAGE_ID_AS_PREDICTIVE_FEATURE`: False
- `TARGET_ENCODING`: False
- `LEARNED_PACKAGE_EMBEDDING`: False
- `RESOLVED_TARGET_VERSION_AS_FEATURE`: False

## 6. Deterministic reconstruction

The independent replay reproduced both historical features exactly:

`DETERMINISTIC_REPLAY_MATCH: True`

Version representation and dependency count were also reconstructible from the frozen schema.

## 7. Prohibited computations

The audit confirms that the following were not computed:

- outcome prevalence;
- `T_acc`;
- `R*`;
- associations;
- effect sizes;
- significance;
- model fitting.

## 8. Audit decision

`DR025A_STRUCTURAL_AUDIT_PASS: True`

The structural audit establishes that the DR-025A candidate representation is deterministic, reconstructible, temporally bounded and structurally separated from the analytical accessibility construction and the post-origin outcome.

The audit does **not** establish predictive superiority, scientific optimality, or statistical validity. Those remain downstream questions.

On the evidence available, there is no structural objection to formal acceptance of DR-025A as the frozen primary baseline representation.
