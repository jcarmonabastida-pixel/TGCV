# TGCV — Domain-Specific VSL Freeze B
## Petroleum / Petrochemical / Natural-Gas Life-Cycle Costing

**Date:** 2026-09-19  
**Status:** FROZEN — PROSPECTIVE METHODOLOGICAL SPECIFICATION  
**Protocol basis:** VSL-SPEC-01 v0.1 FROZEN; VSL-EXP-01 v0.1 FROZEN; Freeze Integrity Audit 001

## Frozen V01–V12 contract

- **V01 Domain/unit:** one explicitly identified facility/associated-activity option comparison in upstream, midstream, downstream or petrochemical operations. The decision unit is fixed before execution.
- **V02 Evaluative perspective:** operator/owner decision perspective, declared before execution.
- **V03 Outcome:** life-cycle cost/economic evaluation quantity for the frozen competing options and analysis period, using only pre-declared cost/economic variables.
- **V04 Reference:** a pre-declared competing option or baseline fixed before observing TGCV outcomes.
- **V05 Evaluative objective:** select the option with the lower declared life-cycle economic burden for the declared decision perspective and frozen scope.
- **V06 O → V* mapping:** `V* = -LCC` for the declared option comparison and frozen scope; higher V* corresponds to lower declared LCC. NPV may be recorded as a secondary economic outcome but is not silently substituted for V*.
- **V07 Directionality:** lower LCC is favorable under V05; direction is frozen before execution.
- **V08 Time horizon:** the declared life-cycle analysis period for the competing options, fixed before execution.
- **V09 Costs/trade-offs:** all cost/economic-value variables included in the declared LCC scope, including identified cost drivers and explicitly declared trade-offs. Scope is frozen before execution.
- **V10 Aggregation:** primary analysis is the declared facility/option comparison. Cross-facility aggregation is prohibited unless separately specified and frozen before execution.
- **V11 Missingness/uncertainty:** missing cost/economic inputs remain explicitly missing; assumptions, uncertainty treatment and sensitivity/scenario rules are frozen before execution; no rule may be chosen after TGCV outcomes.
- **V12 Identification status:** `VALUE_SPECIFICATION_FROZEN`.

## Independence boundary

The VSL does not define or alter `T_acc`, accessibility, transformation identity, trajectory selection or TGCV Core variables. The valuation layer is frozen independently of TGCV outcomes.

## Freeze statement

This artifact freezes a domain-bounded economic valuation convention. It does not constitute experimental evidence, causal evidence, predictive validity, or a claim that TGCV accessibility changes create Value.

## External basis

ISO 15663:2021 specifies requirements and guidance for applying life-cycle costing to create value in petroleum, petrochemical and natural-gas development and operations, including competing options differentiated by cost and/or economic value and life-cycle decision support. ISO currently lists the standard under review/revision status following its 2026 review process.

https://www.iso.org/standard/79198.html