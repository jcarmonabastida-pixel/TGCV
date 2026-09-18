# TGCV — VSL Prospective V01–V12 Specification Worksheet 001

**Date:** 2026-09-19  
**Status:** PRELIMINARY — NO VALUE SPECIFICATION FROZEN  
**Basis:** VSL-SPEC-01 v0.1 FROZEN; VSL-EXP-01 v0.1 FROZEN; prospective design gate 001; candidate screening 002

## Purpose

Apply the same V01–V12 gate to the three retained external candidate families. This worksheet is preliminary: unresolved fields remain unresolved and cannot be filled retrospectively from TGCV outcomes.

## Candidate A — Built assets / infrastructure life-cycle costing

**External basis:** ISO 15686-5:2017 defines life-cycle cost analysis for buildings and constructed assets, including relevant costs/cash flows over an agreed analysis period and comparison between alternatives or estimation of future costs.

| Field | Preliminary status |
|---|---|
| V01 Domain/unit | PARTIALLY IDENTIFIED — buildings/constructed assets; unit requires experimental freezing |
| V02 Evaluative perspective | NOT FROZEN |
| V03 Outcome | PARTIALLY IDENTIFIED — life-cycle cost/cash-flow outcome is externally specified |
| V04 Reference/counterfactual | PARTIALLY IDENTIFIED — comparison between alternatives is supported; exact counterfactual not frozen |
| V05 Evaluative objective | NOT FROZEN |
| V06 O → V* mapping | NOT IDENTIFIED |
| V07 Directionality | NOT FROZEN |
| V08 Time horizon | PARTIALLY IDENTIFIED — agreed analysis period is required |
| V09 Costs/trade-offs | PARTIALLY IDENTIFIED — costs/cash flows; scope of income/externalities must be frozen |
| V10 Aggregation | NOT FROZEN |
| V11 Missingness/uncertainty | NOT FROZEN |
| V12 Identification status | VALUE_SPECIFICATION_NOT_IDENTIFIED at present |

**Disposition:** compatible enough for a full VSL-EXP-01 compatibility audit, but not Value-identified.

## Candidate B — Petroleum/petrochemical/natural-gas life-cycle costing

**External basis:** ISO 15663:2021 specifies requirements and guidance for life-cycle costing in petroleum, petrochemical and natural-gas development and operations. It addresses decisions between competing options differentiated by cost and/or economic value and supports life-cycle decision-making.

| Field | Preliminary status |
|---|---|
| V01 Domain/unit | PARTIALLY IDENTIFIED — facilities/activities; experimental unit not frozen |
| V02 Evaluative perspective | NOT FROZEN |
| V03 Outcome | PARTIALLY IDENTIFIED — LCC and economic evaluation measures are externally grounded |
| V04 Reference/counterfactual | PARTIALLY IDENTIFIED — competing options are explicit; exact comparison rule not frozen |
| V05 Evaluative objective | PARTIALLY IDENTIFIED — decision support between competing options; TGCV objective still requires declaration |
| V06 O → V* mapping | NOT IDENTIFIED |
| V07 Directionality | NOT FROZEN |
| V08 Time horizon | PARTIALLY IDENTIFIED — life-cycle framing is explicit |
| V09 Costs/trade-offs | PARTIALLY IDENTIFIED — cost/economic-value differentiation is explicit |
| V10 Aggregation | NOT FROZEN |
| V11 Missingness/uncertainty | NOT FROZEN |
| V12 Identification status | VALUE_SPECIFICATION_NOT_IDENTIFIED at present |

**Disposition:** compatible enough for a full VSL-EXP-01 compatibility audit, but not Value-identified. The standard's use of the term “value” is not treated as TGCV Value identification.

## Candidate C — Systems/software product quality

**External basis:** ISO/IEC 25010:2023 defines a product-quality model for ICT and software products, with characteristics/subcharacteristics for specification, measurement and evaluation across the lifecycle.

| Field | Preliminary status |
|---|---|
| V01 Domain/unit | PARTIALLY IDENTIFIED — ICT/software product; exact unit not frozen |
| V02 Evaluative perspective | NOT FROZEN |
| V03 Outcome | PARTIALLY IDENTIFIED — product-quality characteristics can be measured/evaluated |
| V04 Reference/counterfactual | NOT FROZEN |
| V05 Evaluative objective | NOT FROZEN |
| V06 O → V* mapping | NOT IDENTIFIED |
| V07 Directionality | NOT FROZEN |
| V08 Time horizon | PARTIALLY IDENTIFIED — lifecycle applicability; experimental horizon not frozen |
| V09 Costs/trade-offs | NOT FROZEN |
| V10 Aggregation | NOT FROZEN |
| V11 Missingness/uncertainty | NOT FROZEN |
| V12 Identification status | VALUE_SPECIFICATION_NOT_IDENTIFIED at present |

**Disposition:** retain only as a secondary candidate. Quality measurement is not treated as Value without an independently specified evaluative objective and O → V* mapping.

## Cross-candidate gate result

No candidate reaches VALUE_SPECIFICATION_FROZEN.

Candidates A and B have an externally explicit economic/LCC evaluation architecture and therefore justify a full compatibility audit. Candidate C has a well-defined measurement architecture but requires a larger prospective Value construction step.

No ranking or winner is assigned.

## Governance boundary

This worksheet:
- does not select a domain;
- does not define universal Value;
- does not infer Value from TGCV outcomes;
- does not authorize an experiment;
- does not modify Core, C09, RMA or the Evidence-to-Claim Matrix;
- does not modify VSL-SPEC-01 or VSL-EXP-01.

## Next operation

Perform full VSL-EXP-01 compatibility audits for Candidates A and B, with all unresolved V01–V12 fields treated as explicit gates. Candidate C remains outside the immediate full audit unless the economic/LCC routes fail.

## External evidence

- ISO 15686-5:2017: https://www.iso.org/standard/61148.html
- ISO 15663:2021: https://www.iso.org/standard/79198.html
- ISO/IEC 25010:2023: https://www.iso.org/standard/78176.html
