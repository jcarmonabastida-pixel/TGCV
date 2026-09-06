# DR-025A — EXT-1.1 Rust Baseline B Representation v0.2

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION  
**Accepted:** 2026-09-06  
**Supersedes:** DR-025A_Rust_Baseline_Representation_ExAnte_v0.1.md as the normative decision record for this design point  
**Depends on:** DR-019, DR-020, DR-021, DR-022, DR-023, DR-024, DR-025

## Decision

The primary conventional baseline representation `B` for EXT-1.1 Rust is formally accepted and frozen as follows:

`B(v_o) = (V_o, H_o, A_o, D_o)`

with primary predictive representation:

`B_num(v_o) = encode(V_o) || prior_release_count_o || package_age_days_o || D_o`

where:

- `V_o` = observed `version_str`, treated as nominal categorical release-state information;
- `prior_release_count_o` = number of earlier same-package releases with `created_at < created_at(v_o)`;
- `package_age_days_o` = elapsed time from earliest observed same-package release to `created_at(v_o)`;
- `D_o` = number of raw dependency declaration rows attached to the origin release.

Canonical package identity is not a predictive feature. Dependency declarations are not semantically resolved for baseline construction.

## Acceptance basis

The structural audit `AUDIT_DR-025A_Baseline_Representation_v0.1.md` returned `DR025A_STRUCTURAL_AUDIT_PASS: True`.

Observed evidence:

- 607,498 package-version observations;
- 607,498 valid `created_at` values;
- 0 invalid timestamps;
- 0 missing required identity fields;
- 0 duplicate version IDs;
- 607,498 non-empty version strings;
- 3,618,523 dependency declaration rows;
- 0 dependency rows with missing origin;
- 0 chronology violations;
- historical features reconstructible;
- dependency count reconstructible;
- deterministic replay match: True.

All prohibited/leakage flags were false, including `T_acc`, `R*`, outcome, post-origin data, predictive package identity, target encoding, learned package embeddings, and resolved target versions.

No outcome labels, `T_acc`, `R*`, associations, effect sizes, significance tests, or model fitting were performed during the audit.

## Normative constraints

1. `version_str` is nominal categorical data; no SemVer ordering, distance, arithmetic, or resolver semantics may be introduced into `B`.
2. Package identity is observational metadata only and cannot be used as a predictive feature or source of package-specific supervised encodings.
3. Historical features use only records strictly preceding the origin release for prior-release count; no post-origin information may enter the baseline.
4. `D_o` counts raw dependency declaration rows only; it does not resolve constraints and does not construct `T`, `R*`, or `T_acc`.
5. No outcome-derived feature engineering, target encoding, future leakage, or confirmatory feature selection is permitted.
6. Any model-specific categorical encoding must be frozen ex ante in the subsequent model/evaluation decision and must be outcome-independent.

## Scope boundary

This decision freezes the primary baseline representation only. It does **not** freeze the statistical model, categorical encoding implementation where model-native handling is unavailable, train/test or cross-validation protocol, hyperparameters, metric, threshold, or confirmatory execution procedure.

Those are subsequent methodological decisions and must be frozen before confirmatory outcome/T_acc/model fitting.

## Scientific interpretation

Acceptance establishes methodological validity of `B` as the conventional comparator representation. It does not establish predictive superiority, equivalence, or inferiority relative to `T_acc^(R*)`.

No confirmatory execution is authorized by DR-025A alone.
