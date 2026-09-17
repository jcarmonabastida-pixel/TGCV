# TGCV — MT5-VSL-10 Prospective VSL Freeze-and-Reproduction Gate 001

**Date:** 2026-09-17  
**Status:** `FROZEN GATE — EXECUTION NOT AUTHORIZED`

## 1. Purpose

Convert MT5-VSL-08/09 into a fail-closed pre-execution gate. The purpose is to determine whether a prospective individual-level Value measurement package can be frozen independently of treatment outcomes and later reconstructed by an independent executor from item-level observations.

This gate does **not** establish Value empirically and does **not** test `ΔT_acc → ΔV*` causality.

## 2. Frozen architecture

`External VSL specification → item-level responses → reproducible score V*`

Separately:

`Z → state/configuration transition → ΔT_acc → subsequent trajectory`

The two pipelines may be linked analytically only after both have independently passed their own integrity gates.

## 3. Mandatory frozen package

A prospective package is complete only if all components below are versioned and hashable:

### P1 — Instrument
- exact CFPB scale version;
- 10-item or other explicitly selected official version;
- exact questionnaire wording;
- response categories/order;
- official user/scoring documentation.

### P2 — Respondent
- individual-level respondent identifier;
- eligibility criteria;
- age-group variable required for scoring;
- no household aggregation unless a separately validated household instrument is substituted.

### P3 — Administration
- language/version;
- administration mode;
- enumerator/respondent instructions;
- timing relative to treatment;
- baseline and follow-up windows.

### P4 — Scoring
- frozen scoring implementation or official scoring table;
- exact version;
- missing-response handling;
- deterministic input/output specification;
- test fixture with known expected score where officially available.

### P5 — Population validity
- target population and sampling frame;
- language/cultural adaptation justification;
- measurement-validity evidence or explicitly designated validation/pilot stage;
- no assumption that existence of the CFPB instrument establishes validity in the target population.

### P6 — Value estimand
Candidate primary estimand:

`ΔV*_i = V*_{i,post} − V*_{i,pre}`

The estimand is frozen before outcome analysis. It is a measurement endpoint, not by itself a causal effect.

### P7 — Missingness
Freeze:
- item-level missing-response rule;
- respondent-level exclusion rule;
- treatment of incomplete baseline/follow-up pairs;
- reporting of missingness by treatment group;
- no post hoc imputation selected because it improves a treatment result.

### P8 — Provenance
Record source URLs, document versions/dates, repository paths, cryptographic hashes and acquisition dates for every component.

## 4. Gate A — Freeze integrity

All must PASS:

A1 exact instrument/version identified;
A2 respondent unit identified as individual;
A3 language/translation version identified;
A4 administration mode frozen;
A5 age-group input frozen;
A6 scoring implementation frozen;
A7 missing-data rule frozen;
A8 baseline/follow-up timing frozen;
A9 target population specified;
A10 population/translation validity disposition explicitly recorded;
A11 primary estimand frozen;
A12 provenance/version/hash package complete.

Any FAIL or unresolved field blocks prospective confirmatory execution.

## 5. Gate B — Independent reproduction

After data collection, an independent executor receives only:

1. frozen VSL package;
2. frozen item-level response dataset;
3. respondent metadata required by the official scoring rule;
4. blank reproduction worksheet;
5. no treatment outcomes, effect estimates, prior VSL interpretations or analyst coaching.

The executor must reproduce:

`responses → V*`

and, where applicable:

`baseline responses → V*_pre`
`follow-up responses → V*_post`
`V*_post − V*_pre → ΔV*`

## 6. Gate C — Separation tests

### C1 Outcome invariance
Changing treatment/outcome labels must not change the computed V* from the same item responses.

### C2 T_acc invariance
Changing the T_acc reconstruction must not alter V* computation.

### C3 Trajectory invariance
The Value scoring procedure must not use downstream trajectory results to determine the score.

### C4 Specification sensitivity
Any change to instrument version, language, scoring rule, missing-data rule or population specification must create a new VSL version rather than silently modifying the frozen one.

## 7. Gate D — Reproduction decision

Decision classes:

- `PASS — VSL FROZEN AND V* REPRODUCIBLE`
- `PARTIAL — SCORE REPRODUCIBLE WITH MATERIAL PROCEDURAL DIVERGENCE`
- `FAIL — VSL FREEZE OR SCORING INSUFFICIENT`
- `BLOCKED — POPULATION/TRANSLATION VALIDITY OR FROZEN INPUTS INSUFFICIENT`

A PASS does not establish causal `ΔT_acc → ΔV*`; it only establishes measurement specification and reproduction.

## 8. Population-validity fail-closed rule

Because MT5-VSL-09 left target-population validity unresolved, this gate currently cannot authorize confirmatory data collection for an unvalidated target population.

A validation/pilot phase may be specified separately, but it must not be relabeled as confirmatory evidence for TGCV Value.

## 9. Governance boundary

This gate authorizes no changes to:
- TGCV Core;
- RMA;
- Evidence→Claim Matrix;
- STATUS;
- C09 status;
- M9 `ΔT_acc → ΔV`.

No retrospective C09 V* may be generated from existing proxy variables.

## 10. Current decision

**`MT5-VSL-10 — BLOCKED FOR CONFIRMATORY EXECUTION.`**

Reason: the measurement architecture and reproduction requirements can be specified, but population/translation validity remains unresolved for a new target population. The correct next step is therefore not data collection under an unvalidated interpretation, but a bounded validation/translation protocol.

## 11. Next authorized movement

**MT5-VSL-11 — Target-Population Measurement-Validity / Translation Pilot Protocol:** define the smallest prospective non-confirmatory pilot capable of evaluating translation, comprehension, response distribution, missingness, administration fidelity and preliminary measurement properties, while keeping the VSL frozen and treatment-independent.
