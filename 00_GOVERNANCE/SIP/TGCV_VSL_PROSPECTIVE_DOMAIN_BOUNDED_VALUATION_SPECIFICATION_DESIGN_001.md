# TGCV — Prospective Domain-Bounded Valuation Specification Design 001

**Date:** 2026-09-19  
**Status:** DESIGN GATE — NOT FROZEN  
**Governance basis:** VSL-SPEC-01 v0.1 — FROZEN; VSL-EXP-01 v0.1 — FROZEN

## 1. Purpose

This artifact defines the methodological design gate for constructing a prospective, domain-bounded Value specification after the existing candidate set failed the frozen VSL-EXP-01 compatibility assessment.

It does not define Value substantively, select a domain, select an endpoint, or authorize an experiment.

It exists to prevent the domain, available data, or observed results from determining the Value construct retrospectively.

## 2. Non-retrospective rule

Any future domain-specific Value specification MUST be created and frozen:

1. before inspecting experimental outcomes;
2. before selecting observations that support the proposed mapping;
3. before executing the corresponding Value experiment;
4. independently of TGCV T_acc construction and intervention results.

Existing TGCV outcomes may be used to establish domain context and feasibility, but not to infer or retrofit the Value mapping.

## 3. Required separation

The specification must preserve the architecture:

TGCV state / accessibility → Outcome → Value

The arrows are an architectural ordering only. They do not constitute a causal claim.

The Value specification must not define, modify, or optimize T_acc, accessibility, transformation identity, treatment assignment, trajectory selection, or intervention exposure.

## 4. Mandatory fields

### V01 — Domain and unit
- domain;
- population;
- unit of analysis;
- inclusion/exclusion rules;
- observation unit versus evaluative unit.

### V02 — Evaluative perspective
- whose evaluation is represented;
- whether the perspective is individual, household, organizational, societal, regulatory, or another explicitly defined perspective;
- whether multiple perspectives are permitted;
- if multiple perspectives are permitted, whether they remain separate rather than being aggregated.

### V03 — Outcome
- exact Outcome construct;
- measurement instrument or operational definition;
- measurement scale/unit;
- observation timing;
- distinction between Outcome and Value.

### V04 — Reference / counterfactual
- reference entity or state;
- baseline/reference period;
- counterfactual definition where applicable;
- rule establishing the reference independently of observed results.

### V05 — Evaluative objective
- substantive objective represented by Value;
- explicit relation between Outcome and the objective;
- justification that the objective is domain-appropriate and independently declared.

### V06 — Outcome-to-Value mapping
- exact mapping O → V*;
- mathematical or deterministic rule where applicable;
- treatment of thresholds, nonlinearities, normalization and transformations;
- rule must be fixed before execution.

### V07 — Directionality
- what constitutes an increase/decrease in Value;
- direction rule;
- handling of ambiguous or multidirectional effects.

### V08 — Time horizon
- evaluation horizon;
- timing convention;
- treatment of delayed effects;
- rule for longitudinal aggregation if applicable.

### V09 — Costs, benefits and trade-offs
- relevant cost dimensions;
- relevant benefit dimensions;
- trade-offs;
- exclusions;
- whether these are part of Value or merely contextual Outcome information.

### V10 — Aggregation
- unit-level aggregation rule, if any;
- temporal aggregation;
- dimension aggregation;
- multi-perspective aggregation, if explicitly justified;
- prohibition on aggregation unless its rule is frozen.

### V11 — Missingness and uncertainty
- admissible missingness;
- missing-data rule;
- uncertainty representation;
- exclusion/imputation rules;
- sensitivity rules where applicable.

### V12 — Identification status
The specification must declare one of:
- VALUE_IDENTIFIED
- VALUE_PARTIALLY_IDENTIFIED
- VALUE_NOT_IDENTIFIED
- VALUE_NOT_APPLICABLE

VALUE_IDENTIFIED requires all essential Value-identification rules to be explicit and frozen.

## 5. Independence requirements

A proposed domain-specific Value specification must demonstrate:
- no dependency on experimental outcome values;
- no selection of endpoint because of observed effect;
- no post-hoc directionality;
- no post-hoc reference selection;
- no universal normative Value definition imported into the domain;
- no modification of VSL-SPEC-01 to accommodate the domain;
- no circular use of T_acc as both treatment/explanatory construct and Value definition.

## 6. Pre-freeze review gates

Before a specification can be frozen, the following gates must be passed:

**G1 — Domain declaration**  
The domain and evaluative unit are fixed independently of expected findings.

**G2 — Perspective declaration**  
The evaluative perspective is explicit.

**G3 — Outcome/Value separation**  
Outcome and Value are operationally distinct.

**G4 — Reference freeze**  
Reference/counterfactual is fixed before outcome inspection.

**G5 — Objective freeze**  
The evaluative objective is explicit and domain-bounded.

**G6 — Mapping freeze**  
O → V* is deterministic or otherwise explicitly operationalized.

**G7 — Direction freeze**  
Directionality is explicit.

**G8 — Horizon freeze**  
The evaluation horizon is explicit.

**G9 — Trade-off/aggregation freeze**  
Costs, benefits, trade-offs and aggregation rules are explicit or formally declared not applicable.

**G10 — Uncertainty freeze**  
Missingness and uncertainty rules are explicit.

**G11 — Independence audit**  
No retrospective information has entered the specification.

**G12 — Execution separation**  
The specification can be handed to an independent executor without requiring interpretation from TGCV results.

## 7. Freeze outcomes

The review may produce only one of the following dispositions:
- VALUE_SPECIFICATION_FROZEN
- VALUE_SPECIFICATION_PARTIALLY_IDENTIFIED
- VALUE_SPECIFICATION_NOT_IDENTIFIED
- VALUE_SPECIFICATION_INCOMPATIBLE

A failed gate must not be repaired by weakening VSL-SPEC-01.

## 8. Experimental boundary

Even a VALUE_SPECIFICATION_FROZEN result does not authorize execution.

A separate domain-specific experimental protocol must subsequently freeze:
- sampling/population;
- treatment/intervention;
- controls;
- trajectory protocol;
- observation schedule;
- execution environment;
- randomization or assignment rules where applicable;
- analysis plan;
- independent reconstruction requirements.

## 9. Synthetic versus real-world use

A synthetic Value specification may satisfy the methodological interface using explicitly declared synthetic conventions.

Such a result must remain labelled synthetic and cannot be promoted automatically to:
- real-world Value;
- causal Value creation;
- predictive validity;
- cross-domain Value comparability.

A real-world specification requires domain-specific substantive justification in addition to operational reproducibility.

## 10. Candidate-selection neutrality

This design gate deliberately does not select among candidate domains.

Domain selection and Value specification are separate governance decisions:

candidate domain → prospective Value specification → compatibility/freeze audit → domain-specific experiment

A candidate may fail because Value cannot be identified under the frozen specification. That is an admissible negative result.

## 11. Current status

This artifact is DESIGN GATE — NOT FROZEN.

It creates no Value claim and authorizes no execution.

It does not modify:
- TGCV Core;
- C09;
- RMA;
- Evidence-to-Claim Matrix;
- VSL-SPEC-01;
- VSL-EXP-01;
- existing experimental evidence.

## 12. Next authorized action

The next action is to identify a new prospective domain candidate independently of the existing blocked candidates, then apply this design gate without using expected results to choose or define the Value construct.

No domain-specific Value specification should be frozen until that candidate-domain boundary has been independently declared.