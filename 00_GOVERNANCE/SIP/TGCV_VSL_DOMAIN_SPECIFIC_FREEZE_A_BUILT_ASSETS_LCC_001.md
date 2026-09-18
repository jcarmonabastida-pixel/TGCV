# TGCV — Domain-Specific VSL Freeze Specification A — Built Assets / Infrastructure LCC

**Date:** 2026-09-19  
**Status:** FROZEN — PROSPECTIVE DOMAIN-BOUNDED VALUE SPECIFICATION  
**Basis:** VSL-SPEC-01 v0.1 FROZEN; VSL-EXP-01 v0.1 FROZEN; Candidate Compatibility Audit 001

## 1. Scope

This specification defines a prospective, domain-bounded Value construct for a single built-asset decision unit under life-cycle costing. It is independent of TGCV transformation/accessibility variables and must be frozen before any TGCV experimental outcome is inspected.

ISO 15686-5:2017 covers LCC of buildings and constructed assets and their parts, including relevant costs/cash flows over an agreed analysis period and comparison between alternatives. The edition was confirmed current in 2024. https://www.iso.org/standard/61148.html

## 2. Frozen V01–V12

| ID | Frozen rule |
|---|---|
| V01 | **Domain/unit:** one defined building, constructed asset, component or project decision unit; the unit identifier is frozen before execution. No portfolio aggregation unless separately specified. |
| V02 | **Evaluative perspective:** owner/investor/procuring decision-maker. The perspective must be declared before execution and cannot change after results are observed. |
| V03 | **Outcome O:** discounted life-cycle cost of the decision unit over the frozen analysis period, including only cost/cash-flow categories declared in the protocol. |
| V04 | **Reference:** one pre-existing or otherwise prospectively designated reference alternative for the same decision unit, fixed before execution. |
| V05 | **Evaluative objective:** minimize discounted life-cycle cost from the frozen owner/investor/procurer perspective. |
| V06 | **Outcome → Value mapping:** `V* = O_ref − O_option`. Positive V* means the option has lower discounted life-cycle cost than the frozen reference; negative V* means higher cost. |
| V07 | **Directionality:** higher V* is favorable within this domain-bounded construct because the frozen objective is cost minimization. No normative claim outside the declared perspective is implied. |
| V08 | **Time horizon:** one fixed analysis period declared before execution; it must be identical for option and reference. |
| V09 | **Costs/trade-offs:** acquisition, operation, maintenance, renewal/replacement and disposal costs are included when declared in the experimental scope. Income or externalities are excluded unless explicitly frozen before execution. |
| V10 | **Aggregation:** primary analysis is at the single decision-unit level. If multiple units are later studied, V* is computed per unit; cross-unit aggregation requires a new specification. |
| V11 | **Uncertainty/missingness:** all missing cost inputs are flagged; no silent imputation. Uncertainty assumptions, discount rate and sensitivity rules are frozen before execution. Invalid/incomplete cases are not assigned V*. |
| V12 | **Identification status:** `VALUE_IDENTIFIED_READY` → `VALUE_SPECIFICATION_FROZEN`. The construct is identified prospectively but is not empirical evidence of Value and has no TGCV causal implication by itself. |

## 3. Independence condition

`O → V*` is defined entirely by the frozen domain rules above. No T_acc, accessibility variable, TGCV intervention, trajectory, transformation identity or post-treatment outcome may determine the Value mapping.

## 4. Non-claims

This specification does not claim that lower LCC is universally preferable, does not define universal Value, does not establish causal influence of accessibility on Value, and does not authorize execution.

## 5. Freeze boundary

Any change to V01–V12, the perspective, reference, objective, cost scope, analysis horizon, or mapping requires a new specification version and cannot be introduced after outcome inspection.

**Frozen status:** DOMAIN-SPECIFIC VSL A = FROZEN.