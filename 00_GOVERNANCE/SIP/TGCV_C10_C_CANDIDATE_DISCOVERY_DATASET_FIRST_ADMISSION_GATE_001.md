# TGCV — C10-C Candidate Discovery / Dataset-First Admission Gate 001

**Status:** FROZEN — DISCOVERY/ADMISSION ONLY; NO EMPIRICAL EXECUTION AUTHORIZED
**Date:** 2026-09-14
**Claim:** C10 — causal `ΔT_acc → ΔV`
**Design contract:** `TGCV_C10_C_EMPIRICAL_DESIGN_GATE_001.md`

## 1. Purpose

Apply the frozen C10-C empirical design contract to real-world datasets/cases **without changing the design retrospectively**.

This gate authorizes only candidate discovery, documentary screening and admission assessment. It does not authorize data analysis, reconstruction, estimation, downloading of large datasets, or empirical execution.

## 2. Discovery principle

Search is **dataset-first**, not hypothesis-first.

A candidate is admissible only if its pre-existing study design and public/documented evidence can satisfy the frozen C10-C requirements. The research question, value endpoint, treatment definition or accessibility representation must not be rewritten after inspecting attractive results.

Candidate discovery must therefore prioritize studies with:

1. a credible accessibility-changing intervention or exposure;
2. a structural change that can plausibly define `T_acc,0` and `T_acc,1`;
3. an independently measured value endpoint;
4. a defensible counterfactual;
5. sufficient downstream observations to separate accessibility from execution and trajectory;
6. reproducible public/procurable provenance.

## 3. Search domains

Discovery may cover, without commitment to any one domain:

- infrastructure and transport accessibility;
- financial inclusion and service access;
- digital/platform access;
- organizational or production-system capability changes;
- healthcare access;
- education/service accessibility;
- energy or communications infrastructure;
- other systems where a structural intervention changes accessible transformations and an independent value endpoint exists.

Domain selection must follow evidence fit, not presumed positive value.

## 4. Candidate screening sequence

Every candidate must pass the following gates in order.

### D1 — Study identity and provenance

Record:

- study title and citation;
- original investigators;
- repository/source;
- DOI or stable identifier where available;
- data release/version;
- public/private access status;
- study population and unit;
- intervention period;
- documentation and replication materials.

**FAIL** if the study identity or provenance cannot be independently established.

### D2 — Causal design eligibility

Determine whether the original design contains credible variation capable of identifying a causal effect of the accessibility-changing intervention/exposure.

Acceptable families are those permitted by the frozen C10-C design gate.

**FAIL** for purely descriptive, correlational or predictive studies.

### D3 — Structural accessibility transition

Establish from documentation, before empirical reconstruction, that the intervention plausibly changes structural conditions relevant to accessible transformations.

Document the proposed mapping:

`S_0 → S_1`

and candidate transformation-accessibility mapping:

`T_acc,0 → T_acc,1`.

At this stage, this is a **candidate operational hypothesis**, not yet an empirical result.

**FAIL** if the intervention changes only downstream behavior/outcomes with no defensible structural accessibility interpretation.

### D4 — Independent value endpoint

Verify that the study contains an outcome that can satisfy the frozen definition of `V` independently of `T_acc` and treatment-path success.

Record:

- exact variable/measure;
- units/scale;
- timing;
- aggregation;
- whether it is monetary, welfare, utility-like, performance-based or otherwise evaluative;
- whether the value interpretation was defined independently of the accessibility construct.

**FAIL** if value must be retrospectively defined from observed success.

### D5 — Counterfactual adequacy

Verify that the study design supplies or can defensibly construct the relevant counterfactual accessibility condition.

Record treatment/control, comparison group, assignment mechanism, timing and any identification assumptions.

**FAIL** if the candidate relies only on uncontrolled before/after comparison or another inadmissible counterfactual.

### D6 — Downstream pathway adequacy

Verify that the candidate contains sufficient information to distinguish:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.

The study need not measure every intermediate natively, but any reconstructed layer must be reproducible and non-circular.

**FAIL** if value is observed but the pathway cannot distinguish accessibility from execution/selection/competing mechanisms at the level required by the causal design.

### D7 — Competing mechanisms and interference

Screen for material alternative explanations:

- simultaneous interventions;
- selection/take-up changes;
- execution intensity/quality;
- price or market changes;
- policy changes;
- spillovers/interference;
- compositional changes;
- differential attrition;
- measurement changes.

Record whether each is randomized away, controlled, measured, bounded, or unresolved.

**FAIL** if a dominant competing mechanism makes the C10-C attribution uninterpretable.

### D8 — Reproducibility/provenance

Verify availability of sufficient documentation to reproduce:

- unit definition;
- treatment assignment;
- value endpoint;
- structural/accessibility mapping;
- derived variables;
- sample restrictions;
- analysis dataset provenance.

**FAIL** if critical elements cannot be independently reconstructed or audited.

## 5. Candidate classification

Each candidate receives exactly one provisional classification:

**A — ADMISSIBLE FOR NEXT-STAGE EMPIRICAL PACKAGE**

All D1–D8 pass, with no unresolved exclusion that prevents construction of the frozen C10-C evidence package.

**B — PROMISING / EVIDENCE GAP**

The candidate is conceptually compatible but one or more requirements need documentary clarification before admission. No execution is authorized.

**C — REJECTED — DESIGN INCOMPATIBLE**

One or more mandatory gates fail materially.

**D — INDETERMINATE**

Evidence is insufficient to determine compatibility without obtaining additional primary documentation or data-access information.

## 6. Mandatory candidate record

For every screened candidate, record:

| Field | Required content |
|---|---|
| Candidate ID | Stable internal identifier |
| Study | Full citation |
| Domain | System/domain |
| Unit | Unit of analysis |
| Structural transition | `S_0 → S_1` |
| Candidate `T_acc` | Explicit transformation-accessibility interpretation |
| Intervention `Z` | Exact treatment/exposure |
| Counterfactual | Exact comparison/potential-outcome basis |
| Value `V` | Exact endpoint and units |
| Downstream pathway | Reach/trajectory/outcome availability |
| Identification | Design and assumptions |
| Competing mechanisms | Known threats and handling |
| Provenance | Source/version/access |
| Reproducibility | Documentation/code/data status |
| D1–D8 | PASS / FAIL / UNKNOWN |
| Classification | A/B/C/D |
| Admission rationale | Concise evidence-based rationale |
| Exclusion risks | Explicit unresolved issues |

## 7. Anti-retrospective rules

The following are prohibited during candidate screening:

1. redefining `V` after seeing treatment effects;
2. redefining `T_acc` to fit available outcome variables;
3. selecting only statistically positive outcomes;
4. changing the estimand because a preferred dataset lacks required variables;
5. treating treatment take-up as accessibility without structural justification;
6. treating access, availability, use and outcome as interchangeable;
7. importing C09 evidence as if it established C10 value causality;
8. excluding negative/null candidates merely because they do not support a positive-value hypothesis;
9. modifying the frozen C10-C design gate to rescue a candidate.

Any proposed modification must be recorded as a separate methodological change and cannot be applied to the current discovery round.

## 8. Evidence priority

When several candidates are available, rank them by:

1. strength of causal identification;
2. clarity of structural accessibility transition;
3. independence and quality of value endpoint;
4. counterfactual quality;
5. ability to separate downstream mechanisms;
6. completeness of provenance and reproducibility;
7. feasibility of independent reconstruction.

Do **not** rank primarily by magnitude or sign of the observed value effect.

## 9. Admission package required before execution

An A-class candidate does not automatically receive execution authorization.

Before empirical execution, a separate candidate-specific package must freeze at minimum:

- candidate identity/version;
- admissible data files;
- unit/sample definition;
- `T_acc,0`, `T_acc,1`, `ΔT_acc` operationalisation;
- treatment/intervention variable;
- value endpoint and estimand;
- counterfactual;
- identification assumptions;
- downstream variables;
- exclusion rules;
- falsification tests;
- provenance hashes/identifiers where applicable;
- independent reconstruction procedure;
- explicit execution authorization record.

## 10. Relationship to C09

C09 evidence is inherited only as bounded upstream support for accessibility-related trajectory effects.

A C10-C candidate must independently supply the additional value-identification layer:

`ΔT_acc → downstream trajectory/outcome → explicit V`

with a defensible counterfactual.

No candidate may be admitted merely because it resembles KGFS, SWIM or another C09 case.

## 11. Stop conditions

Discovery must stop and return to methodological review if:

- no candidate passes D1–D8;
- all promising candidates require changing the frozen design;
- value endpoints are systematically non-independent of treatment/path;
- accessibility cannot be reconstructed without outcome leakage;
- counterfactual identification is systematically unavailable;
- competing mechanisms cannot be separated or bounded;
- provenance prevents independent reconstruction.

A failed discovery round is a legitimate scientific result about the empirical gap; it does not justify weakening the gate.

## 12. Current authorization

**Discovery/documentary screening:** AUTHORIZED by this gate once the C10-C design gate is frozen.

**Dataset download for empirical execution:** NOT AUTHORIZED by this gate.

**Empirical reconstruction:** NOT AUTHORIZED.

**Causal estimation:** NOT AUTHORIZED.

**Claim-level upgrade:** NOT AUTHORIZED.

## 13. Next controlled operation

Execute a **candidate discovery round only**, producing a screened candidate register with D1–D8 evidence and A/B/C/D classification.

No candidate may proceed to empirical execution until a candidate-specific C10-C evidence package is separately frozen and authorized.
