# DR-013 — EXT-1.1 Rust outcome measure and censoring

**Status:** PROPOSED NEW EXPERIMENTAL DECISION

## Decision

The confirmatory outcome is defined at the **package-release observational unit** as the change in package-level adoption/use across subsequent releases, using Cargo downloads as the primary observable outcome.

For each eligible package release at cutoff `t`, define the post-release success measure for a release `r` as:

`Y(r) = log1p(sum of daily downloads of that package version during the first 7 complete calendar days after release)`.

The primary longitudinal outcome is:

`DeltaY_6 = Y(r_6) - Y(r_1)`

where `r_1 ... r_6` are the first six subsequent releases of the same package after the cutoff release, ordered by release timestamp.

The six-release horizon is inherited from DR-012. The seven-day post-release window is fixed here because the selected Rust dataset explicitly contains daily downloads at package-version level, making the measure directly observable without requiring external reconstruction.

## Eligibility and censoring

A focal release is eligible only if:

1. six subsequent releases of the same package are observable in the dataset;
2. the first and sixth subsequent releases each have seven complete post-release calendar days available within the dataset observation boundary;
3. the package-version identity and release timestamp can be resolved unambiguously;
4. no post-cutoff information is used to construct `S_t`, `B_t`, `T_t`, `T_acc,t`, `R_t`, candidate generation, accessibility, sampling eligibility, or feature normalization.

Releases failing any of these conditions are **censored/excluded before outcome calculation**, using only predeclared eligibility rules. No imputation of missing post-release downloads is permitted in the confirmatory analysis.

## Leakage prohibition

The outcome is strictly downstream of the focal release cutoff. No component of `DeltaY_6` may enter candidate generation, accessibility determination, baseline construction, R construction, sampling, or normalization at time `t`.

## Dataset basis

The selected source is the replication dataset associated with Schueller et al. (2022), *Evolving collaboration, dependencies, and use in the Rust Open Source Software ecosystem*, Scientific Data 9, 703. The published dataset contains package versions and daily package-version downloads and is distributed through Figshare under DOI `10.6084/m9.figshare.c.5983534.v1`.

The dataset is therefore suitable for this outcome definition at the observability level. Physical acquisition and integrity verification remain separate gates.

## Gate status

Outcome family: **PASS**.

Temporal separation: **PASS**.

Exact scalar outcome: **PASS — provisional confirmatory specification**.

Censoring rule: **PASS — predeclared eligibility rule**.

Physical dataset acquisition: **OPEN**.

Confirmatory EXT-1.1 freeze: **BLOCKED until the exact dataset artifact is acquired, hashed, and its schema/coverage is verified against this decision.**

## Provenance

This is a **NEW DECISION for EXT-1.1**. It does not claim to reproduce the outcome definition of any historical empirical study; it specifies the outcome for the TGCV confirmatory experiment.
