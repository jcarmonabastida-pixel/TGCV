# TGCV — MT5-VSL-11 Target-Population Translation / Measurement-Validity Pilot Protocol 001

**Date:** 2026-09-17  
**Status:** `CANDIDATE PILOT PROTOCOL — NOT EXECUTED`

## 1. Purpose

Define the smallest non-confirmatory prospective pilot capable of determining whether the externally specified CFPB Financial Well-Being Scale can be administered and interpreted with sufficient measurement integrity in a target population before any confirmatory TGCV Value experiment.

The pilot is a **measurement-validation activity**, not a test of `ΔT_acc → ΔV*` and not evidence of TGCV Value construction.

## 2. Why this pilot is required

The CFPB states that its scale was developed and tested to quantify individual financial well-being, with documented scoring procedures and evidence concerning reliability and validity. The official materials also provide Spanish versions. citeturn0search0turn0search1

However, the published development evidence does not by itself establish measurement equivalence in an arbitrary new population. The technical report describes iterative cognitive testing, item refinement, factor/IRT analyses and testing across survey modes in the scale-development programme. citeturn0search19turn0search22

Therefore target-population validity must be treated as an empirical precondition rather than assumed.

## 3. Pilot boundary

The pilot MUST NOT:
- assign or manipulate TGCV treatment;
- use treatment results to select, modify or interpret Value items;
- alter `Pτ`, `T_acc`, `ΔT_acc` or trajectory reconstruction;
- create a household CFPB score from individual responses;
- claim causal Value effects;
- silently modify official item wording or scoring.

Architecture:

`Frozen external VSL → translated/administered items → item responses → official scoring → V*`

No intervention is required for the pilot.

## 4. Target population specification

Before recruitment freeze:

1. geographic population;
2. age eligibility;
3. sampling frame;
4. inclusion/exclusion criteria;
5. target language;
6. literacy/administration constraints;
7. administration mode;
8. individual respondent unit.

If the intended target is rural India, the protocol must explicitly identify the language(s) and population rather than treating the C09 household population as automatically equivalent to CFPB's individual respondent population.

## 5. Translation pathway

### T11-1 Existing official language
Use an official CFPB language version where one exists. Spanish is explicitly available in CFPB materials. citeturn0search1

### T11-2 No official target language
If the target language lacks an official CFPB version, translation/adaptation must be independently documented before pilot administration.

Minimum translation record:
- source version and hash;
- translator qualifications;
- forward translation;
- independent back-translation or equivalent reconciliation process;
- item-by-item discrepancy log;
- response-category preservation;
- cognitive debriefing record;
- final frozen translation version/hash.

No translation may be changed after pilot results are inspected without creating a new version and explicitly treating the prior pilot as evidence about the previous version only.

## 6. Cognitive/comprehension assessment

A bounded cognitive pretest should assess whether respondents understand each item and response category as intended.

For each item record:
- comprehension issue, if any;
- interpretation/reasoning reported by respondent;
- response difficulty;
- culturally specific ambiguity;
- administration-mode issue;
- proposed corrective action, if any.

The purpose is not to optimize scores but to detect construct/wording incompatibility before confirmatory use.

The CFPB development process itself used cognitive interviewing and respondent feedback during item development. citeturn0search19turn0search22

## 7. Quantitative pilot checks

The pilot should pre-specify, at minimum:

1. item completion/missingness;
2. response-category utilization;
3. floor/ceiling concentration;
4. administration-mode failures;
5. age-group/scoring metadata completeness;
6. score computability under official scoring;
7. internal consistency as a descriptive diagnostic, not a stand-alone validity decision;
8. item-level distributions and anomalous response patterns;
9. reproducibility of score calculation from frozen item-level data.

No single pilot statistic is sufficient to establish validity. Results must be interpreted against the intended construct and administration conditions.

## 8. Measurement-integrity decision gates

### M1 — Instrument fidelity
Exact official item content, response structure and scoring retained.

### M2 — Translation fidelity
Target-language version independently documented and frozen.

### M3 — Comprehension
No unresolved evidence of systematic item interpretation incompatible with intended construct.

### M4 — Response integrity
Response categories are usable and do not exhibit unexplained structural failure that prevents scoring.

### M5 — Score integrity
All admissible respondents can be scored using the frozen official procedure or are handled by a pre-declared missingness rule.

### M6 — Reproducibility
An independent executor reproduces scores from frozen item-level responses and scoring materials.

### M7 — Population interpretation
Available pilot evidence is sufficient to justify using the instrument's intended construct in the specified population, or the result is explicitly classified as insufficient.

All gates must be resolved before confirmatory use.

## 9. Pilot outcomes

Allowed decisions:

- `PASS — PILOT SUPPORTS PROSPECTIVE MEASUREMENT USE`
- `PARTIAL — MEASUREMENT ISSUES IDENTIFIED; REVISION REQUIRED`
- `FAIL — INSTRUMENT/TRANSLATION INCOMPATIBLE WITH TARGET POPULATION`
- `BLOCKED — INSUFFICIENT VALIDATION EVIDENCE`

A PASS authorizes only progression to a confirmatory VSL freeze/reproduction package. It does not establish a treatment effect or causal `ΔT_acc → ΔV*` relationship.

## 10. Independent scoring reproduction

After pilot data collection, an independent executor receives:
- frozen instrument/translation;
- frozen item-level data;
- required age-group and administration-mode metadata;
- frozen scoring implementation;
- blank worksheet.

The executor does not receive treatment information or prior interpretation of the pilot results.

Agreement target:

`item responses + scoring metadata → identical V*`

Any divergence must be classified and resolved before confirmatory progression.

## 11. Sample-size boundary

This is a measurement-validation pilot, not a powered causal efficacy study. Therefore sample size must be justified for the planned comprehension/administration and preliminary measurement diagnostics rather than reverse-engineered from an expected TGCV treatment effect.

A confirmatory sample-size calculation, if later required, belongs to a separate protocol after the measurement gate has passed.

## 12. Governance boundary

This pilot creates no TGCV Value evidence until its predefined validation gates are passed and the resulting measurement package is independently reproduced.

No changes are authorized to Core, RMA, Evidence→Claim Matrix, STATUS, C09 or M9.

## 13. Current disposition

**`MT5-VSL-11 — CANDIDATE PILOT PROTOCOL; NOT EXECUTED.`**

The protocol closes the immediate methodological gap identified by MT5-VSL-10: instead of assuming transportability, it specifies a bounded empirical route to test translation, comprehension, administration and score reproducibility before confirmatory Value measurement.

## 14. Next authorized movement

**MT5-VSL-12 — Pilot Readiness / Material Package Gate:** freeze the target population, language and administration design; assemble the exact instrument/translation, scoring implementation, consent/field procedures as applicable, blank independent-scoring worksheet and provenance/hash manifest. The gate must remain blocked if any target-population or translation prerequisite is unresolved.
