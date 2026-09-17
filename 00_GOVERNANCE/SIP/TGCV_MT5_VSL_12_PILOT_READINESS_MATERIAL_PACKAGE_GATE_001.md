# TGCV — MT5-VSL-12 Pilot Readiness / Material Package Gate 001

**Date:** 2026-09-17  
**Status:** `FROZEN GATE — BLOCKED PENDING TARGET-POPULATION SPECIFICATION`

## 1. Purpose

Determine whether the MT5-VSL-11 non-confirmatory measurement-validity pilot has a complete, reproducible material package ready for execution.

This gate is strictly preparatory. Passing it would authorize only the measurement-validity pilot, not a confirmatory Value experiment and not a causal test of `ΔT_acc → ΔV*`.

## 2. Required package

### R1 — Target population
Must freeze:
- geographic/population definition;
- sampling frame;
- individual respondent eligibility;
- age eligibility;
- inclusion/exclusion rules;
- target language(s);
- administration setting.

### R2 — Instrument
Must freeze:
- exact CFPB instrument/version;
- exact item wording/order;
- exact response categories;
- official user/scoring documentation;
- source provenance and hash.

### R3 — Translation
One of the following must be established:
1. official CFPB version exists for the target language; or
2. an independently documented translation/adaptation package exists, including forward translation, reconciliation/back-translation or equivalent process, item-level discrepancy log, cognitive debriefing plan and frozen version/hash.

No unofficial translation may be silently treated as an equivalent validated instrument.

### R4 — Administration
Freeze:
- administration mode;
- respondent instructions;
- enumerator instructions where applicable;
- age-group metadata collection;
- baseline administration procedure;
- pilot retest/follow-up procedure if included.

### R5 — Scoring
Freeze:
- official scoring table/code or deterministic implementation;
- version/hash;
- age-group and administration-mode inputs;
- missing-response handling;
- known-score test fixture where available.

### R6 — Data capture
Freeze:
- respondent identifier;
- item-level response schema;
- metadata schema;
- timestamp/date fields required by the pilot;
- audit trail;
- missing-value coding.

### R7 — Independent reproduction
Prepare:
- blank scoring worksheet;
- frozen scoring package;
- independent-executor instructions;
- separation rule excluding treatment results/prior interpretations;
- expected reproducibility criterion.

### R8 — Field/ethics readiness
Before actual respondent contact, any applicable consent, privacy, institutional, fieldwork or ethical requirements must be identified and satisfied by the responsible study team. This governance artifact does not substitute for institutional approval.

## 3. Gate conditions

| Gate | Condition | Current disposition |
|---|---|---|
| G12.1 | Target population frozen | BLOCKED |
| G12.2 | Individual respondent unit frozen | PASS — candidate design |
| G12.3 | Exact instrument/version frozen | PASS — candidate standard identified |
| G12.4 | Target-language version frozen | BLOCKED |
| G12.5 | Translation/adaptation provenance complete | BLOCKED unless official target-language version applies |
| G12.6 | Administration mode frozen | BLOCKED |
| G12.7 | Age-group metadata frozen | PASS — required by scoring |
| G12.8 | Scoring implementation frozen | PASS — candidate package defined; material hash package pending |
| G12.9 | Missing-response rule frozen | BLOCKED pending complete scoring package |
| G12.10 | Pilot dataset schema frozen | BLOCKED pending population/field design |
| G12.11 | Independent reproduction worksheet prepared | BLOCKED pending frozen package |
| G12.12 | Provenance/hash manifest complete | BLOCKED pending final package |
| G12.13 | Applicable field/ethics requirements resolved | UNRESOLVED — study-specific |

## 4. Fail-closed rule

The pilot MUST NOT begin while any mandatory G12 condition is BLOCKED or unresolved in a way that can alter the instrument, respondent population, administration, scoring or interpretation.

In particular, the following are not admissible substitutes for a frozen target-population package:
- using C09 household records as if they were individual CFPB observations;
- selecting a language after observing pilot responses;
- creating a local proxy from existing C09 financial outcomes;
- changing wording to improve comprehension without versioning the instrument;
- choosing missing-data treatment after inspecting Value-related results;
- using treatment assignment/effects to justify instrument or endpoint choices.

## 5. Pilot execution package contents

When G12 passes, the frozen package must contain:

1. `INSTRUMENT_VERSION.md`
2. exact questionnaire/source files as legally and operationally permissible;
3. translation/adaptation record, if applicable;
4. `ADMINISTRATION_PROTOCOL.md`;
5. scoring code/table and version record;
6. `DATA_DICTIONARY.md`;
7. `MISSING_DATA_RULE.md`;
8. `INDEPENDENT_SCORING_WORKSHEET.md`;
9. provenance/hash manifest;
10. pilot analysis plan containing only pre-specified measurement diagnostics;
11. field/ethics approval records where applicable.

## 6. Separation from TGCV causal evidence

No pilot artifact may redefine:
- `Pτ`;
- `T_acc`;
- `ΔT_acc`;
- treatment assignment;
- trajectory inclusion;
- C09 treatment/outcome interpretation.

The pilot produces measurement evidence only. Any future causal study must independently freeze its treatment, accessibility and trajectory protocol.

## 7. Current decision

**`MT5-VSL-12 — BLOCKED.`**

The methodology is ready for packaging, but the target population, target language and administration context have not been specified sufficiently to freeze the material package. Therefore no field pilot is authorized at this stage.

This is a deliberate fail-closed result, not a negative empirical finding about the CFPB scale.

## 8. Governance consequences

No changes authorized to:
- TGCV Core;
- RMA;
- Evidence→Claim Matrix;
- STATUS;
- C09;
- M9 `ΔT_acc → ΔV`.

No retrospective Value score may be created from C09 data.

## 9. Next authorized movement

**MT5-VSL-13 — Target Population / Language Selection Specification:** formally select the intended prospective population and language/administration context, with an explicit justification independent of treatment results. Only after that selection can the material package be frozen and the pilot readiness gate rerun.
