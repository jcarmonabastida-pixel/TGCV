# DR-023 — EXT-1.1 Rust Outcome Definition and Horizon v0.1

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION
**Scope:** Outcome definition and observation horizon for the Rust dependency-target transformation family defined by DR-020/DR-021/DR-022

## 1. Decision

The primary post-origin outcome is `subsequent_release_activity` for the same Rust package, measured over a fixed elapsed-time horizon of **180 days**.

For origin release `v_o`:

`Y_180(v_o) = 1` iff there exists a later release `v'` of the same package such that:

`created_at(v_o) < created_at(v') <= created_at(v_o) + 180 days`.

`Y_180(v_o) = 0` iff no such later release is observed and complete 180-day follow-up is available.

## 2. Acceptance basis

DR-023 is accepted following:

- structural outcome audit PASS;
- ex-ante outcome/horizon design analysis;
- horizon-feasibility audit PASS;
- explicit ex-ante horizon proposal selecting H=180 days.

The frozen Rust snapshot contains 607,498 package-version observations with complete `created_at` values. Complete-follow-up coverage was 97.0943% at 30 days, 91.4630% at 90 days, 83.5030% at 180 days, and 68.4960% at 365 days. The design-stage primary coverage floor was 80%; therefore 365 days was rejected and 180 days selected as the longest candidate satisfying that structural criterion.

No outcome prevalence, `T_acc`, association, effect size, significance test, or sampling result contributed to the selection.

## 3. Follow-up and censoring

An origin release is eligible for the primary outcome only when the frozen snapshot provides complete observation opportunity through `created_at(v_o) + 180 days`.

Origins without complete 180-day follow-up are excluded from the primary outcome analysis and are not assigned `Y_180 = 0`.

Complete follow-up is determined from the frozen dataset's terminal observable `package_versions.created_at` boundary and does not depend on whether a later release occurs.

## 4. Outcome-family closure

`later_package_state_transition` is not retained as a co-primary outcome because, under the accepted observational unit `package@version`, a later package-version observation is itself a release event and does not provide a substantively distinct primary outcome.

The primary outcome is therefore frozen as `subsequent_release_activity`.

## 5. Non-circularity and leakage controls

The outcome is strictly post-origin and is reconstructed from later package-version release timestamps. It does not use `T_acc`, `R*`, `B`, dependency constraints, accessibility-derived quantities, downloads, adoption, downstream success, or predictor-derived quantities.

Future releases may contribute only as the post-origin outcome evidence defined by this decision. They must not enter the pre-outcome predictor representation.

## 6. Governance consequences

This decision closes the DR-023 outcome-definition and horizon question.

The following remain OPEN:

- sampling/exclusion rules beyond the frozen complete-follow-up eligibility rule;
- pilot N and seed;
- baseline `B` encoding in Rust;
- `R` serialization.

No confirmatory execution is authorised merely by accepting DR-023.

## 7. Explicit non-claims

This decision does not claim that 180 days is universally optimal for Rust or software ecosystems, nor that `T_acc` predicts subsequent release activity. It establishes the ex-ante primary measurement horizon and outcome definition for EXT-1.1 under the committed experimental criteria.
