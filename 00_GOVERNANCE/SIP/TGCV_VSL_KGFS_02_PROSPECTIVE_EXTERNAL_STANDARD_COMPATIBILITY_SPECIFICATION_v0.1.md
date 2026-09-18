# TGCV — VSL-KGFS-02
## Prospective External-Standard Compatibility Specification

**Status:** DRAFT — NOT FROZEN  
**Version:** v0.1  
**Candidate:** CD-05 / C09 KGFS Rural Banking  
**Parent:** VSL-SPEC-01 v0.1 FROZEN  
**Experimental protocol:** VSL-EXP-01 v0.1 FROZEN  
**Predecessor:** VSL-KGFS-01 v0.1 NOT FROZEN

## 1. Purpose

Define the minimum prospective conditions under which an externally established financial-wellbeing measurement standard may be instantiated as a domain-bounded VSL for a future KGFS-compatible study.

This specification does **not** instantiate the standard in the historical C09 dataset.

It does not convert C09 proxy variables into a financial-wellbeing score.

It does not establish population validity.

It does not create experimental evidence.

## 2. Source-standard principle

The substantive objective and scoring semantics must come from an explicitly identified external standard and frozen version.

The project may not:

- alter the instrument to fit C09 variables;
- substitute proxy variables;
- remove inconvenient items after observing results;
- redefine scoring;
- alter directionality;
- construct a new composite while calling it the external standard.

If the exact source/version cannot be identified and frozen, this specification fails.

## 3. Required source-standard identity

Before freeze, the specification must record:

- issuing organization;
- exact instrument name;
- exact version/release;
- source provenance;
- scoring documentation;
- admissible administration mode;
- population/eligibility conditions;
- missing-response rules;
- interpretation rules;
- licensing/access constraints if applicable.

**Status: NOT YET FROZEN.**

## 4. Evaluative perspective

The candidate external standard is understood to operate at the individual respondent level.

Therefore a prospective KGFS study must explicitly decide whether:

- individual respondent Value is the target construct; or
- a formally justified aggregation to household-level Value is permissible.

Household-level Value must not be assumed merely because historical C09 analysis used household-level data.

**Status: CRITICAL COMPATIBILITY GATE — UNRESOLVED.**

## 5. Reference entity

The VSL must identify the entity to which each Value observation belongs.

Minimum requirement:

`Value observation -> identifiable respondent/entity -> frozen instrument response vector`

If aggregation is required:

`individual V* -> pre-specified aggregation -> household/group V*`

No aggregation rule may be selected after inspecting outcomes.

**Status: UNRESOLVED.**

## 6. Measurement compatibility gate

A prospective study may proceed only if it can collect the exact admissible observations required by the frozen external instrument.

The gate fails if the study substitutes:

- income;
- savings;
- borrowing;
- insurance;
- poverty indices;
- existing C09 proxies;
- analyst-defined composites

for the required instrument responses.

**Status: BLOCKED FOR HISTORICAL C09 DATA; PROSPECTIVE COMPATIBILITY TO BE TESTED.**

## 7. Population compatibility gate

The prospective study must establish whether the external standard can legitimately be administered to the intended KGFS population.

The gate must address, before execution:

- target population;
- language;
- literacy/administration requirements;
- cultural/measurement context;
- respondent eligibility;
- validation evidence;
- translation/adaptation requirements;
- measurement invariance or other appropriate comparability evidence where required.

Existence of the external instrument is not evidence of population validity.

**Status: UNRESOLVED — CRITICAL GATE.**

## 8. Direction and scoring

If the external standard is accepted, its published scoring and direction rules are inherited unchanged.

No TGCV analyst-defined direction rule is permitted.

The VSL becomes:

`frozen instrument responses -> published score -> V*`

subject only to the documented source-standard rules.

**Status:** SOURCE-DEPENDENT; NOT FROZEN UNTIL SOURCE IDENTITY IS FROZEN.

## 9. Reference/time protocol

Before execution the study must freeze:

- baseline/measurement occasion;
- follow-up/measurement occasion;
- admissible comparison;
- longitudinal interval;
- handling of repeated respondents;
- handling of attrition.

The historical C09 time structure cannot automatically be reused as the future VSL protocol.

**Status: PARTIAL — REQUIRES FREEZE.**

## 10. Missingness and data quality

The prospective protocol must reproduce the source-standard missing-response rules where applicable and separately specify:

- respondent-level missingness;
- item-level missingness;
- invalid responses;
- incomplete administrations;
- attrition;
- exclusions.

No missingness rule may be changed after outcome inspection.

**Status: SOURCE-DEPENDENT / NOT FROZEN.**

## 11. Non-circularity

The VSL may receive only admissible instrument responses and source-defined scoring inputs.

It must not receive:

- `T_acc`;
- `Delta T_acc`;
- transformation identity;
- treatment assignment;
- accessibility-change status;
- trajectory labels;
- case labels encoding expected Value;
- TGCV-derived Value variables.

**Status: PASS — FROZEN ARCHITECTURAL REQUIREMENT.**

## 12. Independent reconstruction

Before any substantive Value interpretation, two independent analysts must reconstruct the score from:

1. frozen source standard;
2. frozen instrument/version;
3. frozen response data;
4. frozen scoring procedure;
5. frozen missingness rules.

The reconstructions must be completed independently.

A disagreement blocks Value interpretation until reconciled under the frozen specification.

**Status: REQUIRED — NOT EXECUTED.**

## 13. Historical C09 boundary

This specification explicitly closes the retrospective route.

No historical C09 variable may be relabelled as a response to the external instrument.

No historical C09 dataset may be scored under this VSL unless the exact admissible instrument data are independently demonstrated to exist.

Current C09 evidence remains unchanged.

## 14. Freeze gate

VSL-KGFS-02 can be frozen only when all of the following are PASS:

- exact external standard/version identified;
- source scoring rules frozen;
- evaluative perspective justified;
- reference entity fixed;
- exact measurement inputs available prospectively;
- population compatibility justified;
- administration/language conditions fixed;
- direction inherited without modification;
- missingness rules frozen;
- reference/time protocol frozen;
- non-circularity confirmed;
- independent reconstruction protocol frozen.

A single critical FAIL returns:

`VSL-KGFS-02 = NOT_FROZEN`

and no execution may begin.

## 15. Governance boundary

This draft:

- does not alter C09;
- does not alter Core;
- does not alter RMA;
- does not alter the Evidence-to-Claim Matrix;
- does not produce Value evidence;
- does not authorize data collection;
- does not imply that KGFS is population-valid for the external standard.

## 16. Next gate

The next operation is a **source-standard and population-compatibility audit**.

It must establish the exact external standard/version and determine whether its measurement and administration requirements can be satisfied prospectively for the intended KGFS population.

If that gate fails, VSL-KGFS-02 closes without execution.
