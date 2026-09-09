# D-OPS-24 — EXT-UPD-4.8 Stage B Comparative Industrial Utility Test — Preflight v0.1

**Status:** CLOSED / PREFLIGHT PASS — EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-09  
**Design:** `D-OPS-24_EXT-UPD-4.8_STAGE_B_COMPARATIVE_INDUSTRIAL_UTILITY_TEST_DESIGN_v0.1.md`  
**Design audit:** `D-OPS-24_EXT-UPD-4.8_STAGE_B_COMPARATIVE_INDUSTRIAL_UTILITY_TEST_DESIGN_AUDIT_v0.1.md`

## 1. Purpose

Verify that the Stage-B comparative industrial utility test is operationally controlled sufficiently to justify a separate execution-authorization decision.

This preflight does not execute the test and does not establish industrial utility.

## 2. Preflight result

**PASS — EXECUTION NOT AUTHORIZED BY PREFLIGHT.**

All mandatory controls below are required to remain true at execution authorization.

## 3. Governance controls

- PF-01 Parent Stage-B governance decision exists and opens design route only — **PASS**.
- PF-02 Stage-B design exists and is frozen — **PASS**.
- PF-03 Design audit is closed PASS WITH CONTROLLED REFINEMENTS — **PASS**.
- PF-04 No third domain is opened — **PASS**.
- PF-05 I-01 is not reopened — **PASS**.
- PF-06 Frozen TGCV definitions are unchanged — **PASS**.
- PF-07 Stage B remains bounded to IUT-A-01 — **PASS**.

## 4. Hypothesis and epistemic controls

- PF-08 H0-IUT is explicitly frozen — **PASS**.
- PF-09 H1-IUT is explicitly frozen — **PASS**.
- PF-10 Positive result requires differentiated decision capability — **PASS**.
- PF-11 Descriptive richness alone cannot yield IUT-2 — **PASS**.
- PF-12 Causality is not being tested — **PASS**.
- PF-13 Financial/economic value is not being tested — **PASS**.
- PF-14 Universal TGCV validity is not being tested — **PASS**.
- PF-15 Complete global T_acc operationalization is not being tested — **PASS**.

## 5. Case and option-universe controls

- PF-16 Native case remains the Stage-A IUT-A-01 manufacturing decision episode — **PASS**.
- PF-17 Native state/context schema remains frozen — **PASS**.
- PF-18 Native option universe remains `{O1,O2,O3}` — **PASS**.
- PF-19 RF-01 inclusion rule is explicit and outcome-independent — **PASS**.
- PF-20 RF-01 provenance/version/timestamp must be captured before outcome inspection — **PASS**.
- PF-21 No post-hoc option inclusion/exclusion is permitted — **PASS**.

## 6. RF-B01 baseline controls

- PF-22 Baseline must be frozen before TGCV construction — **PASS**.
- PF-23 Baseline input schema must be frozen — **PASS**.
- PF-24 Baseline output schema must be frozen — **PASS**.
- PF-25 Baseline procedure/stopping rule/allowed analyst intervention must be frozen — **PASS**.
- PF-26 Baseline version, timestamp and provenance must be recorded — **PASS**.
- PF-27 Failure to freeze a reproducible baseline forces INDETERMINATE — **PASS**.

## 7. RF-B02 accessibility/recommendation separation

- PF-28 TGCV identifies accessibility/option-space membership, not recommended choice — **PASS**.
- PF-29 No optimization objective is introduced — **PASS**.
- PF-30 No economic objective is introduced — **PASS**.
- PF-31 Recommendation quality cannot be used as a proxy for option-space utility — **PASS**.

## 8. RF-B03 decision-relevance controls

- PF-32 Decision relevance must be defined before outcome inspection — **PASS**.
- PF-33 Decision relevance must be tied to the bounded decision episode — **PASS**.
- PF-34 Decision relevance cannot be established from favorable downstream outcome — **PASS**.
- PF-35 Outcome correlation cannot substitute for decision relevance — **PASS**.

## 9. RF-B04 comparison and replication controls

- PF-36 Comparison unit must be frozen before execution — **PASS**.
- PF-37 Aggregation rule, if multiple episodes are used, must be frozen before outcome inspection — **PASS**.
- PF-38 If evidence remains single-case, interpretation remains single-case — **PASS**.
- PF-39 No post-hoc replication/aggregation rule is permitted — **PASS**.

## 10. Outcome-blind construction controls

- PF-40 Baseline and TGCV construction use the same permitted pre-decision information — **PASS**.
- PF-41 Downstream outcomes are unavailable during primary construction — **PASS**.
- PF-42 Primary outputs are frozen before outcome unblinding — **PASS**.
- PF-43 Outcome-derived labels are prohibited — **PASS**.

## 11. Reproducibility and provenance controls

- PF-44 Case specification is immutable for execution — **PASS**.
- PF-45 TGCV output schema is immutable for execution — **PASS**.
- PF-46 Metrics/scoring rules are immutable for execution — **PASS**.
- PF-47 Provenance is required for each material analytical input/output — **PASS**.
- PF-48 Computational execution, if used, must be deterministic/reconstructable where applicable — **PASS**.

## 12. Metric controls

The following metrics are permitted only where operationally constructible without arbitrary analyst completion:

- missed-option rate;
- false-option rate;
- lead time;
- structural completeness;
- reproducibility.

Any metric that requires arbitrary thresholds, unsupported completion, or outcome-dependent definitions must be classified **INDETERMINATE** and must not be retrofitted.

## 13. Positive-result control

For IUT-2, all of the following must be demonstrated:

1. reproducible TGCV output;
2. reproducible baseline output;
3. same decision-time information;
4. native option universe frozen independently of outcome;
5. decision relevance established independently of outcome;
6. differentiated capability beyond baseline;
7. difference not reducible to relabelling;
8. no prohibited analyst completion;
9. auditable provenance.

Failure of any mandatory element prevents IUT-2 classification.

## 14. Negative/indeterminate controls

The execution result must be classified **IUT-0** or **INDETERMINATE** when:

- TGCV and baseline are materially equivalent;
- the alleged differentiation is descriptive only;
- the result is not reproducible;
- decision relevance cannot be established;
- baseline cannot be frozen;
- option inclusion is outcome-aware;
- arbitrary completion is required;
- the comparison boundary cannot be maintained.

## 15. Hard-stop controls

Execution must stop immediately if any of the following occurs:

- analyst-invented transformation/option classes;
- arbitrary discretization, bounds or thresholds;
- outcome-defined accessibility;
- post-hoc option-universe changes;
- post-hoc baseline changes;
- post-decision information leakage;
- causal inference presented as IUT evidence;
- financial value presented as IUT evidence;
- universal/generalized claim from bounded evidence;
- modification of frozen TGCV definitions.

## 16. Execution authorization boundary

This preflight establishes readiness for a **separate Stage-B Execution Authorization**. It does not authorize:

- comparative execution;
- dataset acquisition;
- industrial-partner engagement;
- Stage C decision-consequence testing;
- Stage D value linkage;
- causal analysis;
- prediction testing;
- universal theory validation.

## 17. Required next artifact

`EXT-UPD-4.8_STAGE_B_COMPARATIVE_INDUSTRIAL_UTILITY_TEST_EXECUTION_AUTHORIZATION_v0.1.md`

That authorization must restate the frozen case, baseline, RF-01, RF-B01–RF-B04, outcome-blind boundary and hard stops, and must authorize **only the bounded Stage-B comparative execution**.

## 18. Conclusion

Stage B is operationally ready for an authorization decision under the controls above. The preflight does not upgrade any scientific or industrial claim.
