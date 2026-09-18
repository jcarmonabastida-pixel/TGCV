# TGCV — Domain-Specific VSL Freeze Specification B — Petroleum / Petrochemical / Natural Gas LCC

**Date:** 2026-09-19  
**Status:** FROZEN — PROSPECTIVE DOMAIN-BOUNDED VALUE SPECIFICATION  
**Basis:** VSL-SPEC-01 v0.1 FROZEN; VSL-EXP-01 v0.1 FROZEN; Candidate Compatibility Audit 001

## 1. Scope

This specification defines a prospective, domain-bounded Value construct for a single facility/option decision unit in petroleum, petrochemical or natural-gas development/operations using life-cycle cost comparison. It is independent of TGCV transformation/accessibility variables and must be frozen before any TGCV experimental outcome is inspected.

ISO 15663:2021 specifies requirements and guidance for life-cycle costing in petroleum, petrochemical and natural-gas activities and applies to decisions between competing options differentiated by cost and/or economic value. ISO/TC67 also identifies LCC and NPV as economic evaluation measures. https://www.iso.org/standard/79198.html

## 2. Frozen V01–V12

| ID | Frozen rule |
|---|---|
| V01 | **Domain/unit:** one defined facility/option decision unit and its associated activities; the unit identifier and option pair are frozen before execution. |
| V02 | **Evaluative perspective:** owner/operator decision-maker for the defined facility/option decision. The perspective is fixed before execution. |
| V03 | **Outcome O:** discounted life-cycle cost of the candidate option over the frozen analysis horizon, using only cost categories declared in the protocol. |
| V04 | **Reference:** one prospectively designated competing option for the same decision context, fixed before execution and before inspection of TGCV outcomes. |
| V05 | **Evaluative objective:** minimize discounted life-cycle cost from the frozen owner/operator perspective. |
| V06 | **Outcome → Value mapping:** `V* = O_ref − O_option`. Positive V* means lower discounted life-cycle cost than the frozen reference; negative V* means higher cost. |
| V07 | **Directionality:** higher V* is favorable within this declared cost-minimization construct only. This is not a universal normative Value direction. |
| V08 | **Time horizon:** one fixed life-cycle analysis horizon declared before execution and applied identically to option and reference. |
| V09 | **Costs/trade-offs:** capital, operating, maintenance, intervention, replacement and decommissioning/disposal cost categories are included only if declared in the protocol. Benefits/revenues are excluded from this VSL unless a new specification explicitly incorporates them. |
| V10 | **Aggregation:** primary analysis is one facility/option pair. If multiple decision units are studied, V* remains unit-level; portfolio or project aggregation requires a new specification. |
| V11 | **Uncertainty/missingness:** missing cost inputs are explicitly flagged; no silent imputation. Discount rate, uncertainty distributions/ranges, scenario rules and sensitivity analysis are frozen before execution. Cases failing minimum completeness are not assigned V*. |
| V12 | **Identification status:** `VALUE_IDENTIFIED_READY` → `VALUE_SPECIFICATION_FROZEN`. The construct is prospective methodological identification, not empirical evidence and not a TGCV causal claim. |

## 3. Independence condition

`O → V*` is defined entirely by the frozen domain rules above. No T_acc, accessibility variable, TGCV intervention, trajectory, transformation identity or post-treatment outcome may determine the Value mapping.

## 4. Non-claims

This specification does not equate the ISO 15663 phrase “create value” with TGCV Value, does not claim universal economic Value, does not establish causal influence of accessibility on Value, and does not authorize execution.

## 5. Freeze boundary

Any change to V01–V12, the perspective, reference, objective, cost scope, analysis horizon, or mapping requires a new specification version and cannot be introduced after outcome inspection.

**Frozen status:** DOMAIN-SPECIFIC VSL B = FROZEN.