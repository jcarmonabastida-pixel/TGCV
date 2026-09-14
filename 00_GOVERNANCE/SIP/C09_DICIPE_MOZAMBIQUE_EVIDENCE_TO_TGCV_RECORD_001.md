# C09 DICIPE Mozambique — Evidence-to-TGCV Record 001

**Date:** 2026-09-14  
**Status:** RECORDED — METHODOLOGICAL EVIDENCE / D5-C  
**Scope:** C09 real-world candidate discovery; DICIPE Mozambique only

## 1. Candidate

**Study:** *From Access to Achievement: The Primary School-Age Impacts of an At-Scale Preschool Construction Program in Highly Deprived Communities*  
**Setting:** rural, highly deprived communities in Mozambique.  
**Design:** randomized intervention with public reproducibility/data package.

## 2. Gate disposition

| Gate | Result |
|---|---|
| D0 | PASS strong |
| D6-E-F | PASS strong |
| D1 | PASS |
| D2 | PASS provisional |
| D3 | PASS |
| D4 | PASS |
| D5 | **D5-C — DIAGNOSTIC ONLY** |
| D6 | Not opened as an admission gate after D5-C |

**Candidate disposition:** NOT ADMISSIBLE for C09 causal-closure execution under the current evidence. Historical screening result remains immutable.

## 3. What the candidate contributes to TGCV

DICIPE provides useful methodological evidence even though it does not identify the TGCV C09 contribution estimand.

### 3.1 Structural-accessibility architecture

The intervention can be represented as a transition from a community without an effective preschool opportunity to a community with an operating preschool opportunity:

`S0 -> S1`  
`T_acc,0 -> T_acc,1`  
`Delta T_acc = structural expansion of the accessible preschool opportunity`

This is useful because **preschool enrollment must not be used as the definition of `T_acc,1`**. Enrollment is a downstream realization/take-up of the newly available opportunity.

### 3.2 Stable unit and downstream trajectory

The public package supports longitudinal child/household analysis from baseline to endline. The downstream outcomes include primary-school enrollment/progression and cognitive/social-emotional outcomes, which are conceptually distinct from the structural preschool-access transition.

This provides a concrete example of the TGCV sequence:

`structural accessibility change -> take-up/use -> subsequent trajectory`

### 3.3 Multicausal mechanism architecture

The study explicitly considers more than one mechanism, including preschool enrollment and parental stimulation. This is valuable evidence for the revised Protocol 005 interpretation of D5:

`Y = f(Delta T_acc, X1, X2, ..., Xk, interactions, epsilon)`

The presence of parallel mechanisms is not itself a reason to reject a TGCV candidate.

### 3.4 Boundary between mediator evidence and TGCV causal-contribution evidence

The study provides instrumented mediation evidence for preschool enrollment and parental stimulation. However, the published estimand identifies a contribution associated with **preschool enrollment/take-up**, not the causal contribution of the structural accessibility change `Delta T_acc` itself.

The intervention is also bundled: construction, instructors and parenting-related components are not independently randomized in a way that identifies the marginal causal contribution of `Delta T_acc` to downstream outcomes.

Therefore the evidence supports:

`Z -> Delta T_acc -> enrollment -> Y`

as a plausible and empirically supported mechanism architecture, but does **not** by itself identify:

`Delta T_acc -> Y`

as the TGCV contribution estimand.

### 3.5 Why D5-C is useful evidence rather than a scientific failure

DICIPE establishes a useful negative boundary condition:

> Identification of a downstream mediator and evidence that the mediator explains part of the treatment effect are not sufficient to claim identification of the causal contribution of the structural transformation-space change itself.

This distinction operationalizes Protocol 005 and prevents TGCV from conflating:

- structural accessibility,
- take-up/realization,
- downstream trajectory, and
- causal contribution of the structural change.

## 4. TGCV methodological value

DICIPE is retained as **methodological evidence**, not as evidence closing C09.

It demonstrates that a real-world candidate can simultaneously provide:

1. a plausible structural accessibility transition;
2. stable unit-level longitudinal linkage;
3. an independent downstream trajectory;
4. multiple concurrent mechanisms;
5. sophisticated mediation analysis;
6. public reproducibility;
7. yet still fail to identify the specific TGCV contribution estimand.

This is directly useful for designing the next D0 search: prioritize cases where the structural accessibility-producing component itself has independent exogenous variation, factorial/separate randomization, or another defensible identification strategy.

## 5. Non-upgrade constraint

This record does **not**:

- upgrade C09;
- upgrade TGCV Core;
- modify RMA;
- modify the Evidence Matrix;
- modify STATUS;
- authorize C09 real-world execution.

## 6. Historical integrity

DICIPE's D5-C disposition is immutable. Any future methodological re-reading must be recorded as a new artifact and must not rewrite this record.

## 7. Next discovery implication

Return to D0 with priority for candidates where:

`Z_access -> Delta T_acc`

has independent identification from other intervention components, while downstream outcomes remain independent of the accessibility representation and the multicausal D5 contribution estimand can be stated explicitly.
