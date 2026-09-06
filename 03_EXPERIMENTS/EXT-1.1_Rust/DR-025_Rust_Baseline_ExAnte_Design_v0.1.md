# DR-025 — EXT-1.1 Rust Baseline B Ex-Ante Design v0.1

**Status:** PROPOSED — EX-ANTE DESIGN, NO ACCEPTANCE  
**Scope:** Definition and information boundary of the conventional baseline `B` for EXT-1.1 Rust  
**Experiment:** EXT-1.1 Rust  
**Depends on:** DR-019, DR-020, DR-021, DR-022, DR-023, DR-024

## 1. Governing question

Can a conventional baseline representation `B_t` of the same Rust package-release observational unit be defined ex ante, deterministically and without post-origin information, such that the experimental contribution of `T_acc^(R*)` can later be evaluated as incremental information rather than as a comparison against an outcome-tuned or predictor-derived baseline?

## 2. Observational unit and time boundary

The observational unit is the Rust package release `v_o = package@version` defined under DR-007 and DR-019.

For every eligible origin release, the baseline is evaluated at the origin observation boundary:

`t_o = created_at(v_o)`.

`B_t` may use only information that is legitimately observable from the frozen dataset at or before `t_o`.

No information created strictly after `t_o` may enter `B_t`.

## 3. Baseline role

`B` is the conventional comparison representation. It must describe the origin release and its pre-origin/package-state context without explicitly encoding the accessibility construction defined by DR-020/DR-021.

The baseline is not intended to reproduce `T_acc^(R*)` indirectly. Its role is to establish what predictive/trajectory information is available from an ordinary package-release representation before introducing the TGCV-specific accessible-transformation representation.

## 4. Candidate baseline information families

The baseline candidate space is restricted to information reconstructible from the frozen dataset and available at `t_o`, including, subject to final audit:

1. package identity as a categorical identifier only where required for deterministic reconstruction;
2. origin release version/state attributes;
3. package release chronology available strictly before or at the origin boundary;
4. dependency declarations attached to the origin release, represented without resolving them through `R*`;
5. ordinary structural metadata directly attached to the origin release and retained by the frozen schema.

The following are not baseline inputs:

- any outcome or later release activity;
- `T_acc` or any derivative of `T_acc`;
- `R*` or accessibility-derived quantities;
- future releases or future dependency resolution;
- downloads, adoption, popularity, downstream success;
- any variable constructed using post-origin observations;
- any quantity selected because of association with the outcome.

## 5. Important distinction: declared dependency information vs resolved accessibility

The baseline may retain the origin release's declared dependency constraints as raw pre-outcome declarations, because those declarations are part of the package release state.

The baseline must not resolve those declarations into admissible target releases using `R*`. Such resolution belongs exclusively to the TGCV representation `T_acc^(R*)`.

This distinction is necessary to prevent the baseline from becoming an alternative implementation of the same accessibility representation.

## 6. Version and chronology treatment

The baseline may use the origin release's own version string and release timestamp because these are attributes of the observational unit.

Historical package-release information may be used only through a rule frozen ex ante and computable from records with timestamps no later than `t_o`.

No retrospective normalization may use the complete package history when that history contains information after `t_o`.

## 7. Non-circularity requirements

A valid baseline must satisfy all of the following:

- **B1 — Pre-origin:** every feature is computable at `t_o`.
- **B2 — Outcome-independent:** construction does not inspect `Y_180` or later activity.
- **B3 — T_acc-independent:** construction does not compute or require `T_acc^(R*)`.
- **B4 — R*-independent:** construction does not apply the frozen resolver as part of baseline construction.
- **B5 — No future leakage:** no record with timestamp strictly after `t_o` contributes to the baseline.
- **B6 — Deterministic:** identical frozen inputs produce identical baseline representation.
- **B7 — Domain-valid:** every retained feature has an explicit interpretation in the Rust package-release domain.
- **B8 — Ex-ante fixed:** feature families and transformations are fixed before confirmatory outcome analysis.
- **B9 — Minimality:** the baseline contains information necessary to constitute a credible conventional comparator, but no outcome-tuned feature expansion is permitted.

## 8. No feature selection by outcome

No feature may be added, removed, transformed, weighted, or encoded because of observed outcome prevalence, association, effect size, significance, or any confirmatory result.

Any dimensionality reduction, normalization, encoding, or feature selection must itself be specified ex ante and audited independently.

## 9. Baseline vs `T_acc^(R*)`

The eventual comparison is not permitted to assume that `T_acc^(R*)` is superior.

The scientific test remains open until execution. The baseline and TGCV representation must be constructed independently and then evaluated against the same frozen outcome definition and horizon established by DR-023.

A positive result, null result, or negative result must all remain admissible.

## 10. Required audit before acceptance

The DR-025 audit shall establish, at minimum:

- exact baseline fields/features used;
- provenance of every feature family;
- temporal admissibility at `t_o`;
- absence of outcome and post-origin information;
- absence of `T_acc` and `R*` computation in baseline construction;
- deterministic reconstruction;
- explicit treatment of package identity, version, timestamps, and raw dependency declarations;
- no outcome-driven feature selection;
- no retrospective use of complete package history;
- no association, effect-size, or significance calculation.

The audit should use synthetic or structural checks where possible and must not require confirmatory outcome analysis.

## 11. Open design points

This proposal deliberately does **not** yet freeze:

- the final feature vector;
- numerical encoding of categorical fields;
- whether package identity is represented explicitly, omitted, or handled through a pre-specified fixed encoding;
- the exact historical-summary features, if any;
- model family or hyperparameters;
- train/test or cross-validation procedure;
- any confirmatory performance metric beyond the already accepted outcome definition.

These require explicit ex-ante decisions and, where appropriate, separate audits before confirmatory execution.

## 12. Decision status

This document is an ex-ante design proposal only.

It does **not** accept DR-025 and does **not** authorize confirmatory execution.

Acceptance requires an audit showing that the final baseline specification is reconstructible, temporally valid, outcome-independent, independent of `T_acc^(R*)` and `R*`, and sufficiently conventional to provide a meaningful comparator for the subsequent TGCV representation.
