# EXT-UPD-4.9 — IT-G1 Case Identifiability Review — ICD-01

**Date:** 2026-09-09  
**Candidate:** ICD-01 — BPI-2019 Purchase-item workflow  
**Gate:** IT-G1 Case Identifiability  
**Decision:** **FAIL / NOT ADMITTED**  
**Execution:** NOT AUTHORIZED  
**Dataset execution:** NOT PERFORMED

## 1. Purpose

Determine whether ICD-01 is sufficiently closed, before any execution, to support independent reconstruction of:

`(S_t, C_t) → candidate transformation → accessibility/admissibility conditions → (S_{t+1}, C_{t+1})`

The review is documentary and does not execute or inspect the dataset locally.

## 2. Documentary basis

The BPI Challenge 2019 documentation describes a real purchase-order handling process from a large multinational coatings/paints company. Each purchase document contains one or more line items; the case identifier is the combination of purchase document and item. The public description reports 251,734 cases, 1,595,923 events and 42 activities, with timestamps, resources and case attributes. citeturn0search0turn0search5

The documentation therefore supports natural case identity, temporal event ordering and a bounded process context. It does not, by itself, establish the complete set of transformations that were accessible at each decision point.

## 3. IT-G1 assessment

| Requirement | Result | Finding |
|---|---|---|
| Concrete industrial decision context | PASS-BOUND | Purchase-to-pay handling of a purchase-order line item is concretely described. |
| System boundary S | PASS-BOUND | The candidate can be bounded to the lifecycle of one purchase-document line item within the documented purchase-order handling process. |
| Unit of analysis | PASS | Case = purchase document + item is explicitly documented. |
| Temporal frame | PASS | Dataset is documented as covering 2018; event timestamps permit ordering within cases. |
| State representation | CONDITIONAL | Observable event history and case attributes support a provisional state reconstruction, but the sufficiency of that state for all accessibility decisions is not established. |
| Transformation identity | PASS-CANDIDATE | Recorded activities can be identified independently of downstream outcome; however, an activity observed in the log is not automatically equivalent to the complete transformation option set. |
| Accessibility/admissibility rule | **FAIL** | The public event log records realized events, resources and contextual attributes, but does not independently establish the counterfactual set of actions that was accessible/admissible at each decision time. Non-observation cannot be treated as evidence of inaccessibility. |
| Independent evidence sufficiency | **FAIL for IT-G1 closure** | The available documentary evidence is sufficient for case identification but insufficient to close decision-time accessibility ex ante. |
| Downstream separation | PASS-BOUND | Case/event identity can be defined before evaluating throughput, compliance or other outcomes. |

## 4. Decisive finding

**IT-G1 fails on accessibility closure.**

The candidate is substantially better delimited than C-IND-01: its natural unit, case identifier, process context and temporal coverage are externally documented. However, the decisive TGCV requirement is not merely the existence of recorded transformations. IT-G1 requires an independently defensible rule for determining whether a candidate transformation was accessible/admissible at the relevant decision time.

The documentary description identifies realized activities and contextual attributes, including human/batch resources and process categories, but does not establish the full feasible/admissible alternative set for each state. Consequently, the following inference is not licensed:

`activity not observed → transformation inaccessible`

Nor is the converse sufficient:

`activity observed → all relevant accessibility conditions independently closed`.

The accessibility gap is therefore methodological, not a failure of the TGCV Core itself.

## 5. Non-retroactivity

No accessibility criterion, threshold, transformation definition or Core primitive was relaxed to obtain a positive result. No favorable downstream outcome was used to rescue the candidate.

## 6. Consequence

ICD-01 is **NOT ADMITTED** beyond IT-G1 and must not proceed to IT-G2, dataset execution or utility assessment in its present form.

A future revision would require an independently grounded accessibility source or protocol that specifies, ex ante, the admissible alternatives and their material/setup/temporal conditions. Such a revision would constitute a new governance proposal and could not reuse the present documentary screening as if it closed accessibility.

## 7. Scientific impact

- Scientific evidence introduced: **NO**
- C01–C16 changed: **NO**
- Core changed: **NO**
- Scientific gate upgraded/closed: **NO**
- Industrial utility established: **NO**
- Causality established: **NO**
- Value evidence: **NO**

**Disposition:** `ICD-01 = IT-G1 FAIL / NOT ADMITTED / ACCESSIBILITY CLOSURE INSUFFICIENT`.
