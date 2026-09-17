# TGCV — MT5 VSL C09 Domain-Bounded Specification v0.1

**Date:** 2026-09-17  
**Status:** `CANDIDATE — NOT YET FROZEN`  
**Case:** C09 / KGFS Rural Banking  
**Purpose:** candidate substantive valuation specification for subsequent Gate A audit

## 1. Scope and boundary

This specification is restricted to the C09 KGFS rural-finance domain and is external to TGCV transformational construction.

`T_acc / trajectory -> Outcome O -> VSL -> V*`

The VSL MUST NOT alter `Pτ`, `T_acc`, `ΔT_acc`, treatment assignment, or reconstruction of the empirical trajectory.

## 2. Substantive provenance

The valuation objective is grounded in the pre-existing KGFS/Yale source material identifying **financial wellbeing** as an institutional objective and household wellbeing as an evaluated downstream domain.

This source-level objective is provenance, not a universal TGCV definition of Value.

## 3. Candidate VSL fields

### VSL-1 Reference entity

Primary empirical reference entity: household, identified by `hhid`.

Rationale: C09 longitudinal outcome evidence is organized at household level. The source-level objective also concerns individuals/enterprises; therefore this specification explicitly treats household as the empirical reference entity for this case rather than silently generalizing the source objective across units.

### VSL-2 Valuation objective

Objective: assess domain-bounded change in household financial wellbeing associated with the downstream consequences of the KGFS financial-access intervention.

Provenance: external KGFS/Yale substantive objective concerning financial wellbeing/household wellbeing.

### VSL-3 Direction rule

Candidate direction: higher measured financial-wellbeing value is interpreted as greater Value, subject to the sign convention of each selected outcome measure.

For negatively oriented outcomes, the measurement rule must reverse the sign before aggregation or comparison.

**Status:** candidate rule; requires Gate A audit because the external source does not itself prescribe this exact operational direction rule.

### VSL-4 Outcome selection

Candidate outcome family: downstream household financial-wellbeing indicators that are explicitly available in the frozen C09 evidence and are conceptually distinct from `T_acc`.

No single outcome is selected solely because it improved under treatment. Candidate selection must be justified by pre-declared financial-wellbeing relevance and availability at the reference entity/time frame.

**Status:** incomplete until the exact variable list is frozen.

### VSL-5 Outcome-to-Value mapping

Candidate mapping:

`O_financial_wellbeing -> V*`

where `O_financial_wellbeing` is the explicitly frozen vector of selected downstream financial-wellbeing indicators, transformed according to the measurement rules below.

The mapping is domain-bounded and does not imply that every downstream outcome is Value.

**Status:** incomplete until the exact outcome vector and aggregation/comparison rule are frozen.

### VSL-6 Reference frame

Empirical frame: C09 baseline/endline comparison, with randomized service-area assignment and the documented 18–24 month transition period.

Value interpretation is restricted to this empirical horizon and reference population.

### VSL-7 Measurement rule

Candidate measurement rule: compute the pre-declared change in each selected financial-wellbeing indicator between baseline and endline, orient all indicators so higher values represent greater financial wellbeing, and apply a pre-declared aggregation or vector comparison rule.

**Status:** incomplete because the exact aggregation/comparison rule and handling of missing components are not yet frozen.

### VSL-8 Decision / interpretation rule

A candidate `V*` is a domain-bounded representation of financial-wellbeing change only when all selected components are observed or their missingness treatment is specified ex ante, the transformation and aggregation rules are reproducible, and the result is interpreted only within the stated KGFS domain and horizon.

No treatment effect, statistical significance, or positive observed change is itself substituted for Value.

### VSL-9 Provenance and versioning

Substantive objective provenance: external KGFS/Yale source material.

Empirical evidence provenance: canonical C09 KGFS closure and its frozen underlying evidence.

VSL operationalization provenance: this candidate specification, version `v0.1`.

Any later change to objective, outcome selection, direction, mapping, measurement, or decision rule creates a new VSL version and must not overwrite this version's meaning.

### VSL-10 Non-circularity

The VSL does not use observed KGFS treatment effects to define the substantive objective. Outcome selection is intended to be based on pre-declared financial-wellbeing relevance and measurement availability, not on observed effect magnitude or direction.

### VSL-11 Domain-boundedness

The specification applies only to the C09 KGFS rural-finance case and must not be generalized to other domains without separate substantive provenance and a new specification.

### VSL-12 Independent reproducibility

The specification is intended to be executable by independent analysts from a frozen specification plus frozen empirical evidence, without access to prior interpretations.

## 4. Explicit unresolved items before Gate A

1. exact outcome-variable list;
2. exact sign/orientation rule for every variable;
3. exact aggregation or vector-comparison rule;
4. missing-data rule;
5. exact definition of what constitutes an admissible `V*` result;
6. final source citation/version for substantive objective provenance.

These are deliberately exposed rather than silently filled by analyst judgment.

## 5. Gate status

`GATE_A_READY = NO`

This document is therefore a **candidate VSL specification**, not a frozen VSL.

## 6. Governance boundary

No changes to TGCV Core, RMA, Evidence→Claim Matrix, STATUS, C09 status, or M9 `ΔT_acc → ΔV` are authorized by this artifact.

The next authorized operation is to complete or explicitly reject the unresolved operational fields, then run MT5-VSL-02 Gate A against the resulting specification. Independent analyst execution remains prohibited until Gate A passes.
