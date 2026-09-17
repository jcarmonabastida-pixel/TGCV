# TGCV — MT5-VSL-08 Prospective Value Measurement Protocol Candidate 001

**Date:** 2026-09-17  
**Status:** `CANDIDATE METHODOLOGY — NOT YET FROZEN / NOT EXECUTED`  
**Scope:** MT5 Value / prospective TGCV empirical testing

## 1. Purpose

Define a prospective empirical route in which an external substantive Value measurement standard is frozen before outcome collection, so that Value is measured independently of treatment effects and is not reconstructed retrospectively from observed outcomes.

## 2. External measurement basis

Candidate standard: **CFPB Financial Well-Being Scale**, using the official standard questionnaire and scoring materials. CFPB describes the scale as a standardized way to quantify financial well-being and provides the questionnaire, scoring materials and technical report. urlCFPB Financial Well-Being Scale guidehttps://www.consumerfinance.gov/data-research/research-reports/financial-well-being-scale/ citeturn0search0turn0search1

The CFPB construct is individual-level and concerns financial security and freedom of choice; it is not equivalent to income, savings, poverty or other conventional financial outcomes. citeturn0search5turn0search4

## 3. Protocol boundary

The Value instrument must be frozen before treatment assignment/outcome observation for the confirmatory analysis.

Required separation:

`Treatment / system intervention → ΔT_acc → subsequent trajectory → independent Value measurement V*`

The VSL must not be used to define:
- Pτ;
- T_acc;
- ΔT_acc;
- treatment assignment;
- trajectory inclusion/exclusion;
- post-treatment endpoint selection.

## 4. Minimum frozen specification

Before execution, freeze:

1. exact external instrument/version;
2. exact questionnaire wording and response categories;
3. administration mode;
4. scoring software/table and version;
5. respondent unit;
6. respondent eligibility;
7. observation timing;
8. missing-response rule;
9. primary Value estimand;
10. analysis population;
11. treatment-independent interpretation rule;
12. provenance and hashes of all protocol/instrument/scoring files.

The CFPB standard requires its questions to be used with the same wording/order to preserve accurate scoring and comparability. citeturn0search9

## 5. Critical respondent-unit issue

The CFPB scale measures an **individual**. Therefore a prospective TGCV experiment must not silently convert the score into a household-level Value measure.

Two admissible designs remain conceptually distinct:

- **Individual-level design:** administer the CFPB scale to defined individual respondents and treat V* at individual level.
- **Household-level design:** would require a separately justified household valuation instrument; aggregating individual CFPB scores into household V* is NOT authorized by this candidate protocol.

## 6. Primary estimand candidate

Candidate primary endpoint:

`ΔV*_i = V*_{i,post} − V*_{i,pre}`

where `V*` is the externally specified CFPB Financial Well-Being Scale score for individual respondent `i`.

This is only a candidate estimand. It does not imply a causal `ΔT_acc → ΔV*` relationship until treatment identification, timing, interference, attrition and the full causal protocol are separately specified and passed.

The CFPB score is on a 0–100 metric and is explicitly intended for tracking change over time. citeturn0search18turn0search6

## 7. Prospective causal separation

A future experiment may test whether an intervention that changes `T_acc` is followed by a change in independently measured `V*`.

The minimum chain to preserve is:

`Z → state/configuration transition → ΔT_acc → subsequent trajectory → V*`

with explicit tests for:
- treatment assignment validity;
- baseline equivalence;
- interference/spillovers;
- attrition/missingness;
- temporal ordering;
- measurement fidelity;
- independence of VSL specification from treatment results.

## 8. Population validity gate

Because the CFPB scale was developed and validated in U.S. populations, use in another population must not be treated as automatically validated. A prospective TGCV execution therefore requires a separate population/translation/measurement-validity justification before confirmatory use.

The CFPB technical report describes validity as an ongoing process across studies and populations. citeturn0search20

## 9. Decision gates before execution

**G1 — Instrument integrity:** exact official instrument/version frozen.

**G2 — Respondent-unit integrity:** individual respondent explicitly defined.

**G3 — Administration integrity:** wording/order/response mode preserved.

**G4 — Scoring integrity:** official scoring implementation frozen and independently tested.

**G5 — Population validity:** applicability/translation/measurement validity justified for target population.

**G6 — Temporal design:** pre/post observation windows frozen before outcome analysis.

**G7 — Causal separation:** VSL cannot depend on treatment outcomes.

**G8 — Reproducibility:** independent executor can reconstruct V* from frozen responses and scoring package.

Only G1–G8 PASS would authorize a prospective empirical execution.

## 10. Current disposition

This document is a **candidate protocol**, not an executed experiment and not evidence for TGCV Value.

No retrospective C09 V* is created.
No Core/RMA/Matrix/STATUS/C09/M9 modification is authorized.

## 11. Next authorized movement

**MT5-VSL-09 — Population/Translation and Instrument-Integrity Audit**: determine whether the CFPB scale can be legitimately frozen for a prospective target population, including exact instrument version, translation requirements, respondent unit, administration mode and measurement-validity evidence. If this cannot be justified, the CFPB route remains a methodological reference rather than an executable TGCV Value measurement.
