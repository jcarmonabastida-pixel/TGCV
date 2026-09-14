# TGCV — C09 OLPC Peru TR-132 Operational Preflight 001

**Status:** `COMPLETED — TARGETED TR-132 OPERATIONAL AUDIT P4 PASS / FULL EXECUTION STILL NOT AUTHORIZED`
**Date:** 2026-09-14
**Candidate:** Beuermann, Cristia, Cueto, Malamud & Cruz-Aguayo — *One Laptop per Child at Home: Short-Term Impacts from a Randomized Experiment in Peru*
**Domain:** Home computer access / educational transformations
**Data package:** openICPSR 113587, Version V2 (2024-03-28)
**Publication DOI:** 10.1257/app.20130267
**Replication DOI:** 10.3886/E113587V2

## 1. Search decision

This candidate was identified in a new targeted real-world search. It is not part of the previously closed C09 candidate sequence.

It is materially attractive because the intervention itself is explicitly reported to increase access to home computers, the assignment is randomized, the observation unit is the student, follow-up outcomes are available, and a public replication package exists.

## 2. TR-132 operational screen

| Gate | Status | Evidence / remaining condition |
|---|---|---|
| P1 — identifiable unit | **PASS** | openICPSR identifies Student as unit of observation. |
| P2 — baseline and assignment reconstructibility | **PASS DESIGN / DATA PACKAGE CONFIRMED** | Randomized controlled trial; approximately 1,000 primary-school children in Lima; public V2 replication package contains original, intermediate, final, instruments and results materials. |
| P3 — intervention changes accessibility | **PASS CONCEPTUALLY** | Treatment provided an OLPC XO laptop for home use and the publication reports increased access and use of home computers. |
| P4 — bounded `U*` and `T_acc,0/T_acc,1` | **PASS — BOUNDED TRANSFORMATIONAL-SPACE OPERATIONALISATION** | A finite, reproducible `U*` is restricted to domestic transformations dependent on having a computer/laptop at home, within activity classes explicitly represented by OLPC instruments. `T_acc,0` is defined from pre-treatment domestic conditions/resources; `T_acc,1` is defined for the same bounded `U*` after XO assignment. Realized post-treatment use, acquired XO skills and outcomes are explicitly excluded from `T_acc`. |
| P5 — independent trajectory / endpoint | **PASS DESIGN** | Follow-up outcomes include XO proficiency, academic effort, academic achievement and cognitive skills; publication reports post-intervention measurement. |
| P6 — treatment / counterfactual | **PASS DESIGN** | Randomized lottery assignment supplies a credible counterfactual. |
| P7 — public independent reproducibility | **PASS PROVISIONALLY** | openICPSR V2 is publicly listed as experimental/survey data with Student as observation unit and includes multiple data stages plus README/materials. |
| P8 — C09 execution | **NOT AUTHORIZED** | This preflight records operational sufficiency of P4 but does not itself authorize causal execution or a C09 claim upgrade. |

## 3. Candidate operationalization under TGCV

### Unit

Student `u_i` enrolled in the randomized Lima primary-school sample.

### Intervention and assignment

`Z_i = won_lottery_i`: randomized lottery assignment indicator used as the causal assignment variable.

`received_laptop_i` is retained as an implementation/compliance or effective-exposure variable and is not substituted for `Z_i`.

`treatment_school` is a school-level experimental condition and is not used as the individual-level random assignment variable in this bounded TR-132 causal representation.

### Bounded transformation universe `U*`

`U*` is defined as the family of domestic transformations dependent on having a computer/laptop available in the home, restricted to the classes of computer-related activity explicitly represented by the OLPC study instruments. The construction is deliberately bounded to transformations the study can observe or reconstruct; it does not claim to represent the student's complete transformation space.

The following are excluded from `U*`/`T_acc` as realized outcomes or post-treatment states: academic performance, cognitive skills, acquired XO skills, effective subsequent use, and economic or educational outcomes.

### Accessibility profiles

`T_acc,0`: transformations in the declared `U*` accessible under pre-treatment domestic conditions, including observed baseline resources/access conditions and pre-treatment declared capabilities.

`T_acc,1`: transformations in the same declared `U*` accessible after the XO accessibility intervention, with the baseline state/context held fixed except for the intervention-induced availability condition.

The operational definition is bounded: it does not require reconstruction of the student's complete global transformation space. It requires only a reproducible accessibility representation within `U*`.

### Baseline evidence for `T_acc,0`

Ronda 1 provides direct pre-treatment indicators including:

- P2 — computer/laptop in the home;
- P3 — Internet in the home;
- P4 — prior computer experience;
- P12_A1–P12_A8 — declared computer capabilities.

These are explicitly coded Yes/No (with documented nonresponse/multiple-mark codes where applicable). P5–P9 describe use or activities and are not substituted as the accessibility state.

### Post-intervention accessibility evidence for `T_acc,1`

Ronda 2 provides post-intervention resource/access indicators including:

- P1 — computer/laptop in the home;
- P2 — Internet in the home;
- P3 — computer experience.

The operational separation is maintained:

- resource available → accessibility condition;
- activity effectively performed → trajectory/use;
- capability acquired or measured → outcome/capability layer.

The study's public evidence that provision of XO laptops increased home-computer access supports the intervention-to-accessibility interpretation without using realized activity as an accessibility proxy.

### Outcome / trajectory

The outcome layer is selected independently of `T_acc`. In particular, the causal endpoint construction recovered from the replication workflow defines:

`Y = raven_r2 ∈ [0,36]`

from 36 Raven items, with item-level correctness indicators and missing/nonresponse handling specified by the replication code. `Y` is explicitly separate from lottery assignment, laptop receipt, computer use, baseline access and XO skills.

Ronda 2 P4–P7 are treated as trajectory/use observations, not accessibility components. P9–P11 are treated as capability results, not accessibility components.

### Causal structure

The preferred bounded causal representation is:

`Z = won_lottery`

`Z → ΔT_acc → trajectory / use → capabilities / outcomes`

with `received_laptop` available for implementation/compliance or effective-exposure description but not substituted for the randomized assignment variable.

The inspected public data show that `won_lottery` and `received_laptop` are not identical, which reinforces this separation.

## 4. Information firewall

The following substitutions are prohibited unless independently justified as part of the frozen operational definition:

- realized laptop use as `T_acc`;
- post-treatment computer activity as the accessibility state;
- outcome variables as components of `T_acc`;
- acquired XO skills as components of `T_acc`;
- treatment assignment alone as the transformation-space representation;
- aggregate treatment/control statistics in place of unit-level accessibility data.

## 5. P4 PASS rationale

P4 passes with bounded scope because the operational definition establishes all of the following without requiring a global reconstruction of the student's transformation space:

1. `U*` is finite/bounded by explicitly represented OLPC computer-related domestic activity classes;
2. `T_acc,0` is grounded in pre-treatment domestic resources/access conditions and declared baseline capabilities;
3. `T_acc,1` refers to the same bounded `U*` after the XO accessibility intervention;
4. accessibility is kept separate from realized post-treatment activity;
5. accessibility is kept separate from acquired capabilities and all outcome variables;
6. the causal assignment variable is independently defined as `Z = won_lottery`;
7. `received_laptop` is retained as compliance/effective-exposure information rather than assignment;
8. `ΔT_acc` is therefore a bounded accessibility change, not a claim about the student's complete global `T_acc`.

This is a **bounded transformational-space operationalisation**, not a claim that every possible student transformation is observed or reconstructed.

## 6. Decision

**P1 = PASS**

**P2 = PASS DESIGN / DATA PACKAGE CONFIRMED**

**P3 = PASS CONCEPTUALLY**

**P4 = PASS — BOUNDED TRANSFORMATIONAL-SPACE OPERATIONALISATION**

**P5 = PASS DESIGN**

**P6 = PASS DESIGN**

**P7 = PASS PROVISIONALLY**

**P8 = NOT AUTHORIZED**

The previous provisional P4 condition requiring further proof of an admissible bounded construction is superseded by the operational definition recorded in this version.

No causal claim, C09 matrix/RMA/Core upgrade, or execution authorization follows automatically from this P4 closure.

## 7. External evidence

1. Beuermann et al. (2015), American Economic Journal: Applied Economics, documents the randomized trial and reports that provision of approximately 1,000 XO laptops for home use increased access and use of home computers. DOI 10.1257/app.20130267.
2. openICPSR replication package 113587 V2, released 2024-03-28, publicly lists experimental/survey data, Student as the observation unit, and data folders including Originales, Intermedias, Finales, Instrumentos and Resultados.

No causal claim or C09 matrix/RMA/Core upgrade follows from this preflight alone.
