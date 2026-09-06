# DR-024 — EXT-1.1 Rust Sampling / Exclusion Ex-Ante Design v0.1

**Status:** PROPOSED — EX-ANTE DESIGN, NO ACCEPTANCE  
**Scope:** Sampling and exclusion policy after accepted DR-023  
**Experiment:** EXT-1.1 Rust  
**Depends on:** DR-019, DR-020, DR-021, DR-022, DR-023  

## 1. Governing question

Can the analytical population for EXT-1.1 be defined by deterministic, outcome-independent eligibility rules, while avoiding sampling or exclusion decisions that could introduce post-outcome or predictor-derived selection?

## 2. Observational universe

The observational universe is the set of Rust package releases represented by the frozen dataset:

`U = { package@version }`

The unit is the package release defined under DR-007/DR-019. Version is a state attribute of the package-level component.

The universe is not restricted by downloads, adoption, popularity, dependency-network position, subsequent activity, or any outcome.

## 3. Deterministic structural eligibility

An origin release may enter the analytical population only when all required conditions are satisfied:

1. canonical package identity is present and valid;
2. release identity/version information is present and valid;
3. `created_at` is present and valid;
4. the release has complete follow-up for the ex-ante horizon fixed by DR-023 (`H = 180` elapsed days).

Where dataset-governance checks require uniqueness of release identity, duplicate or structurally ambiguous records are treated as technical invalidity rather than substantive exclusion.

## 4. Follow-up eligibility

For DR-023's primary outcome, an origin release is eligible only if the dataset provides the full 180-day observation window after its timestamp.

Incomplete follow-up is **not** coded as outcome zero and is excluded from the analytical population solely because the outcome cannot be observed completely at the frozen horizon.

The follow-up criterion is determined from the frozen temporal coverage boundary and origin timestamp; it does not inspect whether a later release actually occurred.

## 5. Prohibited exclusion criteria

No origin release may be excluded, retained, stratified, or down-weighted on the basis of:

- the value of the DR-023 outcome;
- subsequent package activity;
- `T_acc` or any derivative of `T_acc`;
- `R*` or any accessibility-derived quantity;
- baseline `B` or any predictor-derived quantity;
- downloads, adoption, usage, popularity, or downstream success;
- package size, dependency count, or other substantive package characteristics unless a separate ex-ante technical justification is later accepted;
- manual package selection;
- results from a pilot, confirmatory run, association test, effect estimate, or significance test.

## 6. Census-first principle

Sampling is **not assumed to be necessary**.

The preferred analytical population is the census of all structurally eligible origin releases with complete 180-day follow-up. A sampling mechanism may be introduced only if a separate methodological or computational constraint makes census analysis impracticable or otherwise unjustified.

This preserves the distinction between defining the target population and selecting a computational sample.

## 7. Sampling policy if sampling becomes necessary

If a later gate establishes a justified need for sampling, the mechanism must be frozen ex ante before confirmatory outcome analysis. At minimum it shall specify:

- target sample size `N`;
- randomization mechanism;
- fixed random seed;
- sampling without replacement unless a contrary design is explicitly justified;
- the eligible-population frame from which sampling occurs;
- a rule that does not condition selection on outcome, `T_acc`, `R*`, `B`, or post-origin information.

No N or seed is selected by this document.

## 8. Separation of technical invalidity and substantive exclusion

Technical invalidity concerns whether an observation can satisfy the frozen observational and temporal schema. It must not be conflated with substantive exclusion based on the observed behavior of a package.

The audit associated with DR-024 must therefore report structural invalidity and follow-up incompleteness separately and must not compute outcome labels, `T_acc`, associations, effect sizes, or baseline representations.

## 9. Audit requirements

The structural audit shall establish, at minimum:

- total package-version observations;
- observations with missing or invalid required timestamps;
- observations failing required identity/schema checks, if any;
- observations with complete 180-day follow-up;
- observations with incomplete 180-day follow-up;
- resulting eligible-origin count;
- deterministic reproducibility of the classification;
- confirmation that no outcome, `T_acc`, `R*`, `B`, association, effect-size, or significance calculation is performed.

The audit may stream the frozen ZIP and must not require full dataset loading into memory.

## 10. Decision status

This document is an ex-ante design proposal only. It does not accept DR-024 and does not authorize confirmatory execution.

Acceptance requires a structural audit showing that the proposed eligibility/exclusion rules are reconstructible and independent of post-origin outcomes and predictor-derived quantities.

After acceptance, a separate decision may determine whether census analysis is computationally feasible or whether a fixed sampling design is necessary.
