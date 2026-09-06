# EXT-1.1 Rust — DR-023 Horizon Feasibility Audit v0.1

**Status:** PROTOCOL COMMITTED — EXECUTION PENDING
**Mode:** PRE-CONFIRMATORY / STRUCTURAL ONLY
**Scope:** Feasibility of pre-declared elapsed-time horizons for DR-023
**Prerequisite:** DR-023 structural PASS; DR-023A ex-ante design analysis

## 1. Purpose

This audit determines whether explicitly pre-declared candidate elapsed-time horizons are structurally observable in the frozen Rust snapshot.

It is not an outcome analysis. It does not construct `Y_H`, inspect outcome prevalence, compute `T_acc`, `B`, `R`, associations, effect sizes, significance, or sampling decisions.

## 2. Frozen input

The audit reads only:

`package_versions(id, package_id, created_at)`

from the frozen local dataset:

`rust_repos_2022_09_07.zip`

No live registry, external source, dependency resolution, outcome field, or predictor-derived quantity is used.

## 3. Candidate horizon grid

The initial design grid is:

`H ∈ {30, 90, 180, 365} days`

These are **design candidates only**. The script must not select a primary horizon.

The grid exists to distinguish two questions:

1. whether a candidate horizon is structurally measurable in the frozen snapshot;
2. which horizon should be scientifically registered as primary.

Only the first question is addressed by this audit.

## 4. Measurement rule

For candidate horizon `H`, an origin release has complete follow-up only if:

`created_at(origin) + H <= max(created_at(package_versions))`.

Origins beyond that boundary are incomplete-follow-up observations. They are counted as censored/ineligible for a fixed-horizon primary outcome and are never converted into negative outcome labels.

The audit therefore uses the terminal timestamp only as an observation-coverage boundary.

## 5. Structural feasibility criterion

A candidate horizon receives `PASS` when:

- the required `package_versions` schema exists;
- timestamps are parseable;
- the snapshot has an observable temporal span of at least `H` days;
- at least one origin has complete follow-up through `H`.

This is a minimum structural criterion, not a scientific ranking criterion.

The audit must not choose the horizon with the largest eligible population, highest coverage, or any other numerical advantage.

## 6. Explicit prohibitions

The implementation must not:

- construct outcome labels;
- search for later releases of individual origins;
- compute outcome prevalence;
- calculate or load `T_acc`;
- inspect `B` or `R`;
- estimate associations or effects;
- perform hypothesis tests;
- optimize horizon selection statistically;
- perform sampling;
- use downstream adoption, downloads, popularity, or future-resolution fields.

## 7. Expected execution

From the repository root on Windows PowerShell:

```text
python .\\03_EXPERIMENTS\\EXT-1.1_Rust\\src\\audit_dr023_horizon_feasibility_v01.py
```

The execution must print:

- dataset temporal minimum and maximum;
- observed temporal span;
- for each candidate `H`: complete-follow-up count, incomplete-follow-up count, and coverage;
- structural PASS/FAIL for each candidate;
- explicit confirmation that no primary horizon was selected;
- explicit confirmation that no outcome labels or confirmatory quantities were computed.

## 8. Interpretation rule

If one or more candidate horizons pass, DR-023 remains OPEN. The result only establishes the feasible design space.

If no candidate horizon passes, the horizon design must be revised before DR-023 acceptance.

A passing candidate is not thereby the selected primary horizon.

## 9. Next decision gate

After local execution, the exact output must be preserved as an evidence record. Then the primary horizon may be selected only through an explicit ex-ante methodological decision, independent of confirmatory associations.

The intended sequence is:

`structural feasibility → ex-ante horizon selection → DR-023 acceptance → sampling/exclusion decision → pilot/confirmatory preparation`.

## 10. Reproducibility

The script streams `package_versions.csv` directly from the ZIP and does not extract the archive or materialize the full dataset in memory. A repeated execution against the same frozen ZIP must reproduce the same structural coverage results.
