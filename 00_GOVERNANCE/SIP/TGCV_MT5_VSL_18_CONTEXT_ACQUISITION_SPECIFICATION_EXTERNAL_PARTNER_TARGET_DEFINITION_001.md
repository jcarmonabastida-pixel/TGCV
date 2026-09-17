# TGCV — MT5-VSL-18 Context Acquisition Specification / External Partner Target Definition 001

**Date:** 2026-09-17  
**Status:** `FROZEN ACQUISITION SPECIFICATION — NO PARTNER SELECTED`

## 1. Purpose

Translate MT5-VSL-16 I1–I10 and MT5-VSL-17 findings into a concrete target profile for external outreach.

This artifact defines what a prospective partner/study must be able to provide. It does **not** select a partner, claim collaboration, authorize recruitment, or create an experiment.

## 2. Target-context definition

A qualified context must be a real prospective study in which the following can be frozen before outcome observation:

`system transformation → independently reconstructed ΔT_acc → subsequent trajectory → external VSL → individual V*`

The context must permit Value measurement and accessibility analysis to coexist without either construct defining the other.

## 3. Minimum partner/study commitment

### C1 — Concrete study

Partner must identify a named study/programme/deployment with:
- responsible organization;
- responsible investigator/programme lead;
- operational site(s);
- expected study period;
- prospective recruitment or enrolment mechanism.

### C2 — Individual respondents

Partner must provide an individual respondent population, not merely household, organization or aggregate records.

Required:
- target population;
- eligibility;
- sampling/recruitment frame;
- individual identifier strategy;
- expected sample size/range.

### C3 — Measurement language and mode

Before recruitment, partner must freeze:
- target language;
- exact CFPB instrument/version or formally justified alternative external VSL;
- administration mode;
- instructions;
- age/scoring metadata.

Any non-official translation requires a separately documented translation/validation pathway.

### C4 — Observable system transformation

The study must contain a concrete system/intervention transformation whose initial and resulting states can be independently specified.

Examples of admissible transformation classes include changes in access infrastructure, service availability, system configuration, institutional capability or other structurally defined transformation domains.

The example classes are illustrative only; no specific intervention is selected by this artifact.

### C5 — Independent accessibility specification

The partner must supply enough pre-treatment/system information to reconstruct the relevant `T_acc,0`, `T_acc,1` and `ΔT_acc` without using Value measurements or treatment effects.

If accessibility cannot be independently reconstructed, the context is not eligible even if Value measurement is excellent.

### C6 — Prospective Value measurement

Partner must agree to collect item-level responses required by the frozen VSL:
- respondent ID;
- item responses;
- date/time or measurement window;
- age/scoring metadata;
- administration metadata;
- version identifier;
- missing-response status.

Final scores alone are insufficient for independent reproduction.

### C7 — Frozen temporal structure

Partner must freeze before outcome observation:
- baseline window;
- transition/post window;
- pairing rule;
- follow-up horizon;
- allowable measurement deviations.

### C8 — VSL independence

Partner must accept that the Value instrument, scoring and interpretation rules are frozen independently of observed treatment effects.

No endpoint selection, item deletion, weighting, scoring modification or interpretation change may be justified by post-treatment results.

### C9 — Data access and reproducibility

Partner must permit, subject to ethics/privacy requirements, an independently reproducible Value computation from item-level observations and frozen metadata.

Minimum reproducibility package:
- item-level dataset or controlled reproducibility equivalent;
- instrument version;
- translation version;
- scoring implementation;
- metadata schema;
- missing-data rules;
- provenance/hash manifest.

### C10 — Ethics, privacy and legal basis

Partner must identify the applicable ethics/IRB process, consent basis where required, GDPR/data-protection basis where applicable, data controller/steward, access mechanism and retention rules.

TGCV does not require personal data to be disclosed during initial opportunity screening.

### C11 — Independent executor

Partner must accept a second, independent reconstruction of the frozen Value measurement from the frozen package.

The independent executor must be separated from treatment-outcome interpretation and from construction of the accessibility measure.

### C12 — Pre-analysis separation

Partner must permit explicit separation of:
- intervention/treatment definition;
- `T_acc` operationalization;
- trajectory definition;
- Value measurement;
- causal estimand.

A partner may not condition the VSL on observed outcomes.

## 4. Target profile

The preferred target is therefore:

> **A prospective programme, deployment or applied research study involving an identifiable system transformation, individual participants, repeated measurement, and sufficient data governance to freeze an external financial-wellbeing instrument before observing treatment outcomes.**

The target does not need to be in finance. Financial wellbeing is the current Value measurement route because the external standard is already identified; the system transformation may belong to another domain only if a defensible substantive connection to financial wellbeing exists and is independently specified.

## 5. Priority partner categories

The following are target categories, not selected organizations:

1. Applied research groups running prospective service/intervention evaluations.
2. Financial-inclusion programmes with individual participant measurement.
3. Digital-finance or financial-service deployments with prospective evaluation.
4. Social-impact programmes where system/service accessibility changes are independently measurable.
5. Research infrastructures or doctoral projects able to establish a prospective field study.
6. Organizations already using the CFPB Financial Well-Being Scale prospectively and willing to expose sufficient item-level reproducibility material.

## 6. Minimum outreach package

An initial contact need only request confirmation of:

1. whether a named prospective study exists;
2. whether individual participants are recruited;
3. whether a concrete system/service transformation is present;
4. whether baseline and follow-up measurement are feasible;
5. whether item-level financial-wellbeing measurement is acceptable;
6. whether independent reproduction can be accommodated;
7. whether ethics/privacy/data access can support the design.

No participant data should be requested at this stage.

## 7. Admission decision classes

### PASS — QUALIFIED CONTEXT

All C1–C12 are evidenced sufficiently to construct the frozen material package.

### CONDITIONAL — CONTEXT PROMISING

A concrete study exists, but one or more C-fields require partner confirmation. No recruitment or measurement execution authorized.

### OPPORTUNITY ONLY

A collaboration mechanism, funding route, generic programme or research interest exists without a concrete study satisfying C1–C12.

### FAIL — INCOMPATIBLE

The context requires retrospective Value selection, proxy scoring, household/individual substitution, outcome-dependent VSL modification, or lacks independently reconstructible `ΔT_acc`.

## 8. No-go conditions

The following automatically prevent admission:

- using C09 household records as individual CFPB observations;
- reconstructing CFPB scores from unrelated C09 variables;
- choosing the Value endpoint after treatment results are known;
- defining Value as treatment effect or statistical significance;
- allowing the VSL to modify accessibility operationalization;
- no identifiable prospective transformation;
- no item-level reproducibility;
- no independent executor;
- unresolved ethics/privacy basis at the point of study initiation.

## 9. Current status

No partner or study is selected by this specification.

MT5-VSL-17 found no qualified context in the reviewed external pathways. MT5-VSL-18 therefore establishes an acquisition target rather than promoting any existing opportunity to experimental status.

## 10. Governance boundary

This artifact authorizes only **context acquisition and screening**.

It does not authorize:
- recruitment;
- translation;
- pilot execution;
- confirmatory measurement;
- treatment intervention;
- causal estimation;
- Value scoring from new data;
- Core/RMA/Matrix/STATUS/C09/M9 changes.

## 11. Decision

**`MT5-VSL-18 — FROZEN ACQUISITION SPECIFICATION — NO PARTNER SELECTED.`**

## 12. Next authorized movement

**MT5-VSL-19 — External Partner / Study Target Search and Qualification:** search current external opportunities against C1–C12 and document the first candidate(s) with sufficient public or partner-provided evidence. No candidate is admitted merely because it appears relevant; qualification remains fail-closed.
