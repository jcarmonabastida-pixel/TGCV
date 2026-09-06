# AUDIT — DR-025 Baseline B Structural Audit v0.1

**Experiment:** EXT-1.1 Rust  
**Design under audit:** `DR-025_Rust_Baseline_ExAnte_Design_v0.1.md`  
**Audit implementation:** `src/audit_dr025_baseline_v01.py`  
**Status:** PASS — STRUCTURAL AUDIT ONLY  
**Decision status after audit:** OPEN PENDING METHODOLOGICAL REVIEW / ACCEPTANCE

## 1. Execution

The audit was executed against the frozen Rust dataset ZIP:

`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

Execution mode was pre-confirmatory and structural. No extraction was performed and the complete dataset was not loaded into memory.

## 2. Dataset integrity observed

- Package-version rows: **607,498**
- Valid `created_at`: **607,498**
- Invalid `created_at`: **0**
- Missing required identity fields: **0**
- Duplicate version IDs: **0**
- Dependency declaration rows: **3,618,523**
- Dependency rows with missing origin release: **0**
- Package count: **91,437**
- Minimum `created_at`: **2014-11-11 00:22:07.370652+00:00**
- Maximum `created_at`: **2022-09-07 01:50:04.004956+00:00**
- Pre-origin historical release pairs: **13,679,134**
- Chronology violations: **0**

## 3. Candidate baseline manifest audited

The structural candidate consists of four feature families:

1. origin `version_str` as a release-state attribute;
2. prior release count within the same package, using timestamps at or before the origin;
3. package age at origin, measured from the earliest observed package release;
4. raw declared dependency count attached to the origin release.

Package identity is not used as a feature in this candidate.

## 4. Independence checks

The execution reported all required structural checks as satisfied:

- B1 Pre-origin boundary: **PASS**
- B2 Outcome independent: **PASS**
- B3 `T_acc` independent: **PASS**
- B4 `R*` independent: **PASS**
- B5 No future leakage: **PASS**
- B6 Deterministic: **PASS**
- B7 Domain valid: **PASS**
- B8 Ex ante fixed: **PASS**
- B9 Minimality: **STRUCTURAL CANDIDATE**

The audit also confirmed that outcome prevalence, associations, effect sizes, significance, and model fitting were not computed.

## 5. Interpretation

The result establishes that the proposed baseline boundary is structurally implementable on the frozen dataset and that the candidate feature families can be constructed without invoking the outcome, `T_acc^(R*)`, or `R*`.

The audit does **not** establish that the candidate is scientifically optimal, predictive, or superior to `T_acc^(R*)`. No outcome analysis was performed.

The audit also does not by itself freeze the final encoding of `version_str` or any model-side representation. Those remain subject to an explicit methodological specification before confirmatory execution.

## 6. Decision

`DR025_STRUCTURAL_AUDIT_PASS = TRUE`.

`DR025_DECISION_STATUS = OPEN_PENDING_METHODOLOGICAL_REVIEW_AND_ACCEPTANCE`.

No confirmatory execution is authorized by this audit alone.
