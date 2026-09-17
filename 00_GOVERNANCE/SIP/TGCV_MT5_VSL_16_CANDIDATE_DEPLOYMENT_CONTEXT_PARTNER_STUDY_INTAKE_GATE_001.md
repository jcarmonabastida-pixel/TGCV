# TGCV — MT5-VSL-16 Candidate Deployment Context / Partner-Study Intake Gate 001

**Date:** 2026-09-17  
**Status:** `FROZEN GATE — NO CANDIDATE SUBMITTED`

## 1. Purpose

Define the minimum evidence package required before an external partner, doctoral host, programme, research infrastructure or prospective study may be admitted as a candidate context for the MT5-VSL prospective Value-measurement route.

This gate prevents the research programme from turning a funding call, partnership mechanism, public dataset or generic research interest into an experimental context without a concrete study design.

## 2. Scientific boundary

The candidate context must preserve the separation:

`system/intervention context → state/configuration transition → ΔT_acc → subsequent trajectory → independently frozen VSL → individual Value measurement V*`

The partner/study may not use observed treatment effects, post-treatment outcomes or analyst preference to define the VSL, select the primary Value endpoint, modify `T_acc`, or alter the accessibility reconstruction.

## 3. Mandatory intake package

### I1 — Named study/context

Must identify a concrete prospective study, programme, deployment, doctoral project or research collaboration with a responsible organization/person and a defined operational setting.

**Required:** documentary source or formal partner statement.

### I2 — Target population

Must specify:
- geography/site;
- population definition;
- individual respondent unit;
- eligibility/inclusion/exclusion;
- sampling/recruitment frame;
- expected recruitment mechanism.

No inheritance of C09 household population by analogy is permitted.

### I3 — Language and administration

Must specify before recruitment:
- target language;
- exact instrument version;
- administration mode;
- instructions;
- age/scoring metadata;
- baseline and post/transition timing.

Any translation/adaptation must have its own version and validation pathway.

### I4 — System transformation

Must identify the concrete system/intervention whose transition is to be studied.

The candidate must provide enough information to define independently:
- relevant initial state;
- accessible transformation space;
- intervention/treatment assignment or exposure;
- resulting structural/configurational transition;
- admissible trajectory observation window.

The Value instrument may not be used to define this transformation.

### I5 — Accessibility reconstruction feasibility

Must demonstrate that `T_acc,0`, `T_acc,1` and/or the relevant `ΔT_acc` can be operationalized without using Value outcomes.

A candidate with a valid Value instrument but no independently reconstructible accessibility transition is **not** a TGCV deployment context.

### I6 — Value measurement feasibility

Must guarantee prospective collection of the exact item-level observations required by the frozen external VSL, not merely a final score.

Required:
- individual identifier;
- complete item responses;
- age/scoring metadata;
- administration metadata;
- measurement date/window;
- version identifier;
- missing-response recording.

### I7 — Temporal design

Must freeze before outcome collection:
- baseline timing;
- post/transition timing;
- allowable measurement window;
- pairing rule;
- follow-up horizon.

### I8 — VSL independence

The candidate must accept that the VSL is frozen independently of treatment results.

Disallowed:
- choosing the instrument after seeing outcomes;
- selecting a subset of items because it responds to treatment;
- changing scoring after treatment observation;
- defining Value as statistical significance or treatment effect;
- constructing a Value index from post-treatment variables selected for favorable results.

### I9 — Governance / ethics / access

Must identify the applicable:
- ethics/IRB pathway;
- informed-consent basis where required;
- privacy/data-protection basis;
- data-access agreement;
- ownership/stewardship of item-level data;
- retention and reproducibility arrangements.

No sensitive respondent data is required at intake.

### I10 — Independent reproduction

The context must permit an independent executor to receive a frozen package containing:
- VSL specification;
- instrument/translation;
- scoring implementation;
- item-level observations;
- metadata;
- provenance/hash manifest;
- blank reconstruction worksheet.

The original study team must not be the sole source of the final Value computation.

## 4. Admission gates

| Gate | Requirement | Decision if unresolved |
|---|---|---|
| G16.1 | Concrete prospective context | BLOCK |
| G16.2 | Individual target population | BLOCK |
| G16.3 | Language/admin context | BLOCK |
| G16.4 | Identifiable system transformation | BLOCK |
| G16.5 | Independent `ΔT_acc` reconstruction | BLOCK |
| G16.6 | Prospective item-level VSL measurement | BLOCK |
| G16.7 | Frozen temporal design | BLOCK |
| G16.8 | VSL independence | BLOCK |
| G16.9 | Ethics/access pathway | BLOCK |
| G16.10 | Independent reproduction | BLOCK |

All ten gates must pass before the context can proceed to MT5-VSL-17 material freezing.

## 5. Candidate classes

### A — Qualified candidate

All G16.1–G16.10 PASS and documentary evidence is available.

### B — Conditional candidate

A real context exists, but one or more operational inputs remain unresolved. It may be developed, but cannot enter pilot execution.

### C — Opportunity only

A funding call, collaboration mechanism, public dataset or generic programme exists without a concrete study context.

### D — Inadmissible

The candidate depends on retrospective outcome selection, proxy reconstruction, household/individual unit substitution, or other violation of the VSL/T_acc boundary.

## 6. Current intake state

No candidate has been submitted with the complete I1–I10 package.

The opportunities identified in MT5-VSL-15 therefore remain **Class C — Opportunity only**.

No prospective pilot is authorized.

## 7. Fail-closed rules

The following cannot be used to bypass the gate:

- existence of the CFPB instrument;
- availability of Spanish materials;
- existence of C09/KGFS data;
- a doctoral funding call;
- a public financial-well-being dataset;
- an interested organization without a defined study;
- an intervention whose outcomes are already known;
- a plausible population selected solely because it is convenient.

## 8. Decision

**`MT5-VSL-16 — FROZEN GATE — NO CANDIDATE SUBMITTED.`**

The gate is now the canonical admission boundary for any future prospective VSL deployment context.

No Core/RMA/Matrix/STATUS/C09/M9 modification is authorized by this gate.

## 9. Next authorized movement

**MT5-VSL-17 — Candidate Context Submission / External Context Audit:** apply I1–I10 to the first concrete prospective study/partner context that can supply the missing operational inputs. If no context is available, the gate remains open for future submission without inventing one.
