# EXT-UPD-4.8 — Stage B Comparative Industrial Utility Test — Execution Authorization v0.1

**Status:** CLOSED / EXECUTION AUTHORIZED — BOUNDED STAGE B ONLY  
**Date:** 2026-09-09  
**Parent:** `EXT-UPD-4.8_STAGE_B_COMPARATIVE_INDUSTRIAL_UTILITY_TEST_DECISION_v0.1.md`  
**Design:** `D-OPS-24_EXT-UPD-4.8_STAGE_B_COMPARATIVE_INDUSTRIAL_UTILITY_TEST_DESIGN_v0.1.md`  
**Design audit:** `D-OPS-24_EXT-UPD-4.8_STAGE_B_COMPARATIVE_INDUSTRIAL_UTILITY_TEST_DESIGN_AUDIT_v0.1.md`  
**Preflight:** `D-OPS-24_EXT-UPD-4.8_STAGE_B_COMPARATIVE_INDUSTRIAL_UTILITY_TEST_PREFLIGHT_v0.1.md`

## 1. Authorization purpose

Authorize one controlled comparative execution of the Stage-B Industrial Utility Test (IUT) for the bounded IUT-A-01 manufacturing case, under the frozen design, audit refinements and preflight controls.

This authorization does not establish industrial utility, scientific validity, causality, prediction, financial value or universal superiority.

## 2. Authorized test question

> **Under the same pre-decision information boundary, does TGCV identify or explain a decision-relevant difference in accessible native alternatives that the frozen incumbent/baseline does not identify or explain, or identifies materially less effectively?**

### H0-IUT

TGCV provides no differentiated decision-relevant capability beyond the baseline.

### H1-IUT

TGCV provides at least one reproducible decision-relevant capability beyond the baseline under the controlled information boundary.

## 3. Authorized case

Only **IUT-A-01 — Manufacturing / machine-level alternative process-plan & tooling decision** is authorized.

Frozen Stage-A boundary:

`S_D = (M, Tool, Plan, Setup)`

`C_D = (Part, Batch, ProductionSchedule, ToolRequirements)`

Native option universe:

`Uτ,D = {O1,O2,O3}`

where:

- O1 = static/local process-plan alternative;
- O2 = current tooling already available;
- O3 = partially set-up machine plus alternative tooling not currently in place.

No new option class, domain or decision family is authorized.

## 4. RF-01 authorization

The option universe is frozen before outcome inspection.

The authorized inclusion rule is:

> Include exactly the native machine-level alternatives explicitly identified by the frozen source/case specification.

No option may be included, excluded, subdivided or merged because of its observed downstream outcome or apparent TGCV performance.

The execution record must preserve the option-universe version, timestamp and provenance before construction.

## 5. Information-parity authorization

Both baseline and TGCV must receive the same information available at the decision point.

Authorized information includes, where present in the frozen case:

- machine configuration;
- tooling inventory;
- setup state;
- part/batch requirements;
- production schedule;
- tool requirements;
- explicitly frozen native constraints.

The following are prohibited during primary construction:

- achieved performance;
- realized quality/cost/time;
- post-decision setup;
- realized success/failure;
- outcome-derived labels;
- any later information unavailable at decision time.

## 6. Baseline authorization

Before TGCV construction, the baseline must be frozen and versioned with:

- input schema;
- output schema;
- decision procedure;
- stopping rule;
- permitted analyst intervention;
- scoring/comparison rule;
- provenance and timestamp.

If this cannot be reproduced, execution must classify **INDETERMINATE** and stop.

## 7. TGCV authorization

TGCV may construct only the bounded decision-relevant option-space representation required by the frozen case.

The execution must preserve the distinction:

`candidate option existence → accessibility/feasibility → downstream outcome`

No outcome may determine accessibility.

No optimization or recommendation objective is authorized.

## 8. Primary comparative output

The primary output must be frozen before outcome inspection and contain:

1. baseline option-space output;
2. TGCV option-space output;
3. option-level differences;
4. TGCV structural explanation of differences;
5. source/provenance supporting classifications;
6. decision-relevance classification under the frozen rule.

## 9. Differentiated capability authorization criterion

A result can qualify as differentiated only if:

- it is reproducible;
- it is decision-relevant under the pre-frozen rule;
- it uses the same pre-decision information as baseline;
- it is attributable to the TGCV analytical construction;
- the baseline cannot trivially reproduce the same information;
- it is not merely relabelling or richer terminology;
- it does not depend on post-hoc interpretation.

## 10. Authorized metrics

Where constructible without arbitrary assumptions, the execution may record:

- newly accessible options;
- lost options;
- missed-option rate;
- false-option rate;
- decision-relevant lead time;
- structural completeness within the frozen universe;
- reproducibility.

Metrics requiring arbitrary thresholds, unsupported completion or outcome-dependent definitions must be marked **INDETERMINATE**.

## 11. Outcome-blind execution sequence

1. Freeze case and source provenance.
2. Freeze RF-01 option universe.
3. Freeze information boundary.
4. Freeze baseline procedure.
5. Freeze TGCV output schema.
6. Freeze decision-relevance rule.
7. Freeze metrics/scoring.
8. Construct baseline output.
9. Construct TGCV output.
10. Freeze primary outputs.
11. Compare outputs.
12. Classify differentiated capability.
13. Only then, if needed and permitted by the execution result, unblind downstream outcome for descriptive consequence recording.
14. Preserve all evidence and provenance.

## 12. Replication boundary

The execution may use only the replication structure frozen by the preflight/execution record.

If more than one decision episode is available within the same authorized case family, all inclusion and aggregation rules must remain pre-specified.

No post-hoc selection of episodes is authorized.

A single-case result remains single-case evidence.

## 13. Hard stops

Immediate stop and **INDETERMINATE** if any of the following occurs:

- analyst-invented option class;
- arbitrary discretization/bound/threshold;
- outcome-defined accessibility;
- post-hoc option inclusion/exclusion;
- post-hoc baseline modification;
- post-decision information leakage;
- inability to reproduce the baseline;
- inability to reproduce TGCV;
- inability to establish decision relevance independently of outcome;
- differentiation reducible to relabelling;
- unsupported causal or financial inference;
- modification of frozen TGCV definitions.

## 14. Result classes authorized

Only the following Stage-B classifications are authorized:

- **IUT-0 — No differentiated utility demonstrated.**
- **IUT-1 — Descriptive/explanatory utility only.**
- **IUT-2 — Differentiated decision-support utility demonstrated.**
- **INDETERMINATE — Defensible classification prevented by methodological/evidentiary boundary.**

IUT-3 and IUT-4 are not authorized.

## 15. Explicit exclusions

This authorization does not authorize:

- a third scientific domain;
- reopening I-01 constructive operationalization;
- global exhaustive reconstruction of `T_acc`;
- causal identification;
- prediction testing;
- financial/economic value estimation;
- Stage C decision-consequence testing;
- Stage D value linkage;
- universal TGCV validation;
- claims of general superiority;
- industrial-partner engagement;
- modification of external scientific assets.

## 16. Post-execution governance

After the bounded execution, the required sequence is:

**Execution Result → Evidence→Claim Impact Assessment → propagation/current-state reconciliation → consistency closure.**

No scientific or industrial claim may be upgraded before the impact assessment and consistency closure.

## 17. Authorization conclusion

**EXECUTION AUTHORIZED — ONE BOUNDED STAGE-B COMPARATIVE IUT EXECUTION ONLY.**

The authorization is deliberately narrow: the purpose is to determine whether TGCV exhibits a reproducible, decision-relevant analytical differentiation from the incumbent baseline in IUT-A-01, under equal pre-decision information and without outcome leakage or analyst-invented completion.

No further scientific or industrial route is opened by this authorization.
