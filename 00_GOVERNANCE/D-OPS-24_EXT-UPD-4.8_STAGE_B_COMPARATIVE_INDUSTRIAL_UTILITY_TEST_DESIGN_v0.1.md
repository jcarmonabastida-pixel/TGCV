# D-OPS-24 — EXT-UPD-4.8 Stage B Comparative Industrial Utility Test — Design v0.1

**Status:** FROZEN / DESIGN — AUDIT REQUIRED; EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-09  
**Parent decision:** `EXT-UPD-4.8_STAGE_B_COMPARATIVE_INDUSTRIAL_UTILITY_TEST_DECISION_v0.1.md`  
**Case:** IUT-A-01 — Manufacturing / machine-level alternative process-plan & tooling decision

## 1. Purpose

Design a controlled comparative test of whether TGCV provides differentiated decision-relevant analytical capability beyond a frozen incumbent/baseline for the bounded industrial case established in Stage A.

This design does not authorize execution and does not establish industrial utility.

## 2. Test question

> **Under the same pre-decision information boundary, does TGCV identify or explain a decision-relevant difference in accessible native alternatives that the frozen incumbent/baseline does not identify or explain, or identifies materially less effectively?**

### H0-IUT

TGCV provides no differentiated decision-relevant capability beyond the baseline.

### H1-IUT

TGCV provides at least one reproducible decision-relevant capability beyond the baseline under the controlled information boundary.

## 3. Frozen case boundary

The Stage-A case remains the starting boundary:

- manufacturing system preparing a new batch/part;
- machine-level process-plan and tooling decision;
- native state representation: `S_D = (M, Tool, Plan, Setup)`;
- context: `C_D = (Part, Batch, ProductionSchedule, ToolRequirements)`;
- native candidate alternatives: `Uτ,D = {O1,O2,O3}`;
- O1: static/local process-plan alternative;
- O2: current tooling already available;
- O3: partially set-up machine plus alternative tooling not currently in place.

The final execution case specification must preserve the exact Stage-A option universe unless a separately justified and authorized refinement is made.

## 4. RF-01 option-universe control

The option universe and any bounded subset must be frozen before outcome inspection.

For every included option/class the execution record must preserve:

1. inclusion universe;
2. inclusion/exclusion rule;
3. rationale independent of observed outcome;
4. version/timestamp before outcome evaluation;
5. source/native provenance.

If the rule cannot be demonstrated independently of outcome, Stage B is INDETERMINATE.

## 5. Decision-time information boundary

### Permitted

Only information available before the decision, including where applicable:

- machine configuration;
- current tooling inventory;
- setup state;
- part/batch requirements;
- production schedule;
- tool requirements;
- other explicitly frozen native constraints.

### Prohibited for construction of comparative outputs

- achieved production performance;
- observed quality/cost/time result;
- post-decision setup;
- realised success/failure;
- any information unavailable at decision time;
- outcome-derived labels.

Outcome data, if retained, can only be used after the analytical outputs are frozen and only for a separately authorized consequence analysis.

## 6. Baseline

The baseline is the conventional fixed/linear process-plan decision representation identified in Stage A.

Before execution, the baseline must be operationally specified sufficiently to reproduce its output from the same decision-time inputs.

The baseline specification must freeze:

- input variables;
- transformation/decision procedure;
- output schema;
- analyst intervention allowed;
- stopping rule;
- metrics.

No baseline may be selected or modified after observing TGCV results.

## 7. TGCV analytical construction

The TGCV arm must construct, from the same decision-time information:

`S_t, C_t → Uτ,D → Pτ,D → decision-relevant T_acc,D subset → ΔT_acc,D+ / ΔT_acc,D−`

where the bounded option-space construction is explicitly limited to the frozen native alternatives and does not imply complete global `T_acc` closure.

The execution must distinguish:

- candidate transformation/option existence;
- accessibility/feasibility;
- observed downstream outcome.

No accessibility label may be assigned because an option eventually succeeded or failed.

## 8. Primary comparative output

The primary output is a **pre-decision option-space difference record**:

- options identified as accessible by TGCV;
- options identified as inaccessible by TGCV;
- corresponding baseline output;
- TGCV-specific structural explanation of the difference;
- evidence/provenance supporting each classification.

The output must be frozen before any downstream outcome is inspected.

## 9. Secondary outputs

Where constructible without introducing arbitrary assumptions:

- newly accessible options detected;
- lost options detected;
- structural conditions explaining changes;
- missed-option rate;
- false-option rate;
- decision-relevant lead time;
- reproducibility;
- structural completeness within the frozen option universe.

Metrics that cannot be defined without arbitrary analyst completion must be marked INDETERMINATE rather than manufactured.

## 10. Comparative protocol

For each bounded decision episode:

1. Freeze case specification.
2. Freeze RF-01 option universe.
3. Freeze decision-time information boundary.
4. Freeze baseline specification.
5. Freeze TGCV output schema.
6. Freeze metrics and scoring rules.
7. Construct baseline output without outcome information.
8. Construct TGCV output without outcome information.
9. Blind the two outputs to downstream outcome during construction and primary scoring.
10. Compare outputs using the frozen metrics.
11. Record whether the difference is decision-relevant.
12. Only after the primary comparison is frozen may downstream outcome be unblinded, if authorized.
13. Record reproducibility and any hard stop.

## 11. Differentiated capability criterion

A positive IUT result requires all of the following:

- the output is reproducible;
- the output is decision-relevant;
- the output is generated under the same pre-decision information boundary;
- the difference is attributable to the TGCV analytical construction;
- the baseline cannot trivially reproduce the same information;
- the result does not depend on post-hoc interpretation.

A richer description without decision-relevant differentiation is classified at most IUT-1.

## 12. Predefined failure conditions

Stage B must stop or classify negatively/indeterminately if:

- TGCV produces no differentiated output;
- baseline reproduces the same output equivalently;
- analyst invention is required to complete option classes;
- arbitrary discretization/bounds/thresholds are introduced;
- outcome information leaks into construction;
- the option universe changes after outcome inspection;
- baseline selection changes after TGCV inspection;
- reproducibility fails;
- the alleged utility is only terminology or relabelling;
- decision relevance cannot be demonstrated for the bounded episode.

## 13. Result classification

- **IUT-0:** no differentiated utility demonstrated.
- **IUT-1:** descriptive/explanatory utility only.
- **IUT-2:** differentiated decision-support utility demonstrated.
- **INDETERMINATE:** methodological or evidentiary boundary prevents defensible classification.

IUT-3 and IUT-4 are outside this Stage-B design boundary.

## 14. Replication and robustness

A single positive bounded episode must not be interpreted as universal industrial utility.

The design audit must determine the minimum number and structure of controlled episodes needed for a meaningful Stage-B inference. Any replication requirement must be frozen before observing comparative results where feasible.

If the evidence remains single-case, the final interpretation must explicitly remain bounded to that case.

## 15. Blindness and reproducibility

The design must support at least:

- outcome-blind analytical construction;
- deterministic/reproducible execution where computation is involved;
- immutable case specification;
- immutable baseline specification;
- immutable TGCV output schema;
- auditable provenance;
- preservation of intermediate evidence sufficient for independent reconstruction.

## 16. Industrial decision relevance

The design must distinguish analytical correctness from decision utility.

A TGCV output is decision-relevant only if it can affect a bounded decision concerning the available process-plan/tooling alternatives, for example by exposing an option that the baseline does not identify or by explaining a constraint/configuration change that changes the option set.

The test must not claim that this necessarily creates financial value.

## 17. Scientific interpretation

A positive Stage-B result may strengthen C16's practical translation pathway and the industrial applicability question, subject to Evidence→Claim impact assessment.

It does not automatically upgrade:

- C11 to full transversal conformance;
- causality;
- prediction;
- financial value;
- universal validity;
- superiority across domains;
- complete `T_acc` operationalization;
- originality beyond its existing bounded status.

A negative or indeterminate result must likewise be recorded without overgeneralizing beyond the tested conditions.

## 18. Data and source requirements

Before execution, the design audit/preflight must specify the exact documentary or empirical source required to instantiate the bounded decision episode and verify its native alternatives and constraints.

No dataset may be selected because it produces a favorable TGCV result.

No industrial partner or proprietary data is required or authorized by this design.

## 19. Governance sequence

The required sequence is:

**Design → Design Audit → Preflight → Execution Authorization → controlled comparative execution → Evidence→Claim Impact Assessment → propagation → consistency closure.**

No execution is authorized by this design artifact.

## 20. Hard stops

Immediate INDETERMINATE/STOP if closure requires:

- analyst-invented transformation classes;
- arbitrary discretization or thresholds;
- outcome-defined accessibility;
- post-hoc option-universe modification;
- post-hoc baseline modification;
- post-decision information;
- unsupported causal/value inference;
- modification of frozen TGCV definitions.

## 21. Design conclusion

The Stage-B design is intentionally narrower than a general industrial validation programme. Its purpose is to test one proposition cleanly:

> **TGCV may have practical industrial utility if its representation of decision-relevant changes in accessible transformation possibilities provides differentiated decision capability without requiring unjustified exhaustive reconstruction of the whole `T_acc`.**

Execution remains unauthorized until this design passes audit and preflight and receives a separate execution authorization.
