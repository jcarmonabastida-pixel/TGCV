# TGCV — VSL-SPEC-01
## Domain-Independent Specification for Value Identification

**Status:** DRAFT / CANDIDATE FOR FREEZE  
**Version:** v0.1  
**Scope:** Domain-independent methodological specification  
**Role:** Pre-domain specification for subsequent domain-specific VSL construction

---

## 1. Purpose

VSL-SPEC-01 defines the methodological conditions that a domain-specific Value Specification Layer (VSL) must satisfy before a candidate domain is selected for experimental study of Value.

It does **not** define a universal substantive meaning of Value.

Its purpose is to specify the conditions under which Value may be considered identifiable within a particular domain, while preserving independence from the experimental results that will later be evaluated.

The specification therefore precedes domain selection.

---

## 2. Scope and non-retroactivity

VSL-SPEC-01 is domain-independent and does not select, prefer or rank candidate domains.

It does not:
- modify the TGCV transformational core;
- redefine S, T_acc, transformations, trajectories or mechanisms;
- establish a universal Value function;
- establish causal relations between accessibility, trajectories, outcomes and Value;
- establish cross-domain Value comparability;
- constitute empirical evidence.

The specification must be frozen before a candidate domain is selected for the corresponding VSL experiment.

---

## 3. Relationship to VSL Synthetic Minimum v0.1

VSL_SYNTHETIC_MIN_v0.1 remains a frozen synthetic demonstrator and is not redefined by this specification.

Its frozen synthetic mapping is:

V*(S) = O(S)

and:

Delta V* = Delta O

That mapping is an artificial, domain-bounded convention of the synthetic demonstrator. It is not a universal definition of Value.

VSL-SPEC-01 is a higher-level methodological specification governing the requirements for future domain-specific VSLs.

No retroactive reclassification of the synthetic demonstrator is authorized.

---

## 4. Outcome and Value distinction

### 4.1 Outcome

Outcome is an observed, measured or reconstructed downstream result of the system under the applicable experimental protocol.

### 4.2 Value

Value is a domain-specific evaluative construct whose semantic content must be specified explicitly for the selected domain.

VSL-SPEC-01 specifies **requirements for identifying Value**, rather than defining its universal substantive content.

Therefore:

Outcome != Value

An Outcome may contribute to identifying Value only through an explicit, pre-specified evaluative mapping.

---

## 5. Required domain-specific VSL fields

Before execution, a domain-specific VSL must specify, at minimum:

1. **Unit of analysis** — the entity, system, episode, trajectory, decision or result to which Value applies.
2. **Evaluative perspective** — the beneficiary, stakeholder, decision criterion or other declared perspective from which Value is assessed.
3. **Outcome construct** — the downstream observations or variables from which the evaluation is constructed.
4. **Reference** — baseline, benchmark, target, alternative, counterfactual or other reference frame.
5. **Evaluative mapping** — the explicit rule translating Outcome into the domain-specific Value construct.
6. **Directionality** — whether and how changes correspond to higher, lower or neutral Value, or to a non-ordinal classification.
7. **Time horizon** — the period over which the evaluation is valid.
8. **Costs, benefits and trade-offs** — how multiple evaluative dimensions are treated.
9. **Aggregation** — how multiple Outcomes, dimensions or perspectives are combined, where aggregation is required.
10. **Uncertainty and missingness** — treatment of incomplete, uncertain, interval-valued or ambiguous observations.
11. **Identification status** — the resulting classification of Value identifiability under this specification.

These fields must be defined independently of the experimental results to which they will later be applied.

---

## 6. Independence requirements

The domain-specific VSL must be specified before inspection of the experimental results that it will evaluate.

The following may not be selected or changed retrospectively to obtain a desired Value classification:

- Outcome definition;
- reference or counterfactual;
- evaluative perspective;
- directionality;
- time horizon;
- aggregation rule;
- treatment of costs or benefits;
- missing-data rule;
- Value proxy or substitute.

The VSL must not derive its semantic identity from the transformation that happened to occur.

In particular, the VSL specification must not define Value as a function of:

- T_acc;
- Delta T_acc;
- transformation identity;
- selected transformation;
- treatment assignment;
- accessibility-change status;
- a case label encoding an expected result;
- a variable already derived from Value.

This does not prevent subsequent experimental analysis of relations between those variables and Value.

---

## 7. Causal neutrality

VSL-SPEC-01 is causally neutral.

It does not assume:

Delta T_acc -> Outcome

or:

Delta T_acc -> Delta Value

or:

Delta T_acc -> trajectory -> Delta Value

A domain-specific VSL may provide the downstream evaluative interface required for a later causal protocol, but causal claims require separate experimental identification and evidence.

The existence of an Outcome-to-Value mapping is not itself a causal claim.

---

## 8. Reference and evaluative mapping

A domain-specific VSL must declare the reference against which Value is evaluated before execution.

The reference may be a baseline, benchmark, target, alternative or counterfactual, provided that its methodological status is explicitly specified.

The mapping:

Outcome -> Value

must be explicit.

VSL-SPEC-01 does not require this mapping to be:
- linear;
- monotonic;
- scalar;
- additive;
- deterministic.

Those properties, if applicable, belong to the domain-specific specification and must be justified and frozen before execution.

---

## 9. Costs, benefits, trade-offs and aggregation

Where Value depends on multiple dimensions, the domain-specific VSL must specify how those dimensions are jointly evaluated.

It must explicitly identify, where applicable:

- benefits;
- costs;
- constraints;
- adverse effects;
- trade-offs;
- interactions among dimensions;
- aggregation rules.

A dimension may not be omitted retrospectively because its observed contribution is inconvenient for a hypothesis or expected result.

If a legitimate aggregation rule cannot be specified, the corresponding Value construct may be only partially identifiable or not identifiable.

---

## 10. Uncertainty and missingness

A domain-specific VSL must specify treatment of:

- missing observations;
- uncertain measurements;
- intervals;
- ambiguous outcomes;
- incompatible observations;
- incomplete reference information.

The handling rule must be fixed before the relevant results are interpreted.

Missingness must not be converted retrospectively into a favorable or unfavorable Value classification without a pre-specified rule.

---

## 11. Identification states

A candidate domain must be classifiable using the following states.

### VALUE_IDENTIFIED

The domain-specific Value construct, its evaluative perspective, Outcome, reference, mapping and required supporting rules are sufficiently specified and frozen to permit reproducible identification.

### VALUE_PARTIALLY_IDENTIFIED

Some Value dimensions, perspectives or conditions are identifiable, but the complete declared Value construct is not sufficiently specified or operationalized.

### VALUE_NOT_IDENTIFIED

The available domain information does not permit a sufficiently independent, reproducible and pre-specified identification of Value.

This is a valid methodological result and must not be repaired by weakening the specification retrospectively.

### VALUE_NOT_APPLICABLE

This state may be used only where the domain-specific specification explicitly establishes, before execution, that a particular Value-identification component is genuinely not applicable.

It must not be used as a convenience category for unresolved incompatibility.

---

## 12. Domain compatibility rule

A candidate domain is compatible with VSL-SPEC-01 only if the essential identification requirements can be specified and frozen before execution.

If an essential requirement cannot be satisfied, the result is methodological incompatibility, expressed as:

VALUE_NOT_IDENTIFIED

or, where justified:

VALUE_PARTIALLY_IDENTIFIED

The specification must therefore be capable of rejecting a candidate domain.

A domain may not redefine the semantic requirements of VSL-SPEC-01 merely to become compatible.

---

## 13. Protection against retrospective specification

The following sequence is prohibited:

1. inspect experimental results;
2. select the most favorable Outcome;
3. select or change the Value reference;
4. choose the direction of evaluation;
5. select a Value proxy;
6. choose an aggregation rule;
7. declare the resulting construct to have been pre-specified.

A substantive change after result inspection constitutes a new specification version.

It cannot silently replace the frozen specification under which the results were obtained.

---

## 14. Separation of specification, execution and evidence

A frozen VSL specification is not experimental evidence.

The methodological sequence is:

VSL specification -> frozen rules -> execution -> observed Outcome -> Value identification -> evidence

The specification determines what may be identified.

Execution determines what was actually observed and whether the frozen rules could be applied.

Evidence classification must distinguish specification-level facts from execution findings and from subsequent inference.

---

## 15. Relationship to TGCV

VSL-SPEC-01 is external to the TGCV transformational core.

It provides a downstream methodological interface for evaluating Outcome as Value under domain-specific rules.

The conceptual separation is:

TGCV transformation/accessibility/trajectory -> Outcome -> domain-specific VSL -> Value

This representation is architectural, not a causal assertion.

No TGCV Core primitive, relation or threshold is added by VSL-SPEC-01.

---

## 16. Claim boundaries

VSL-SPEC-01 alone does not establish:

- a universal definition of Value;
- a universal Value function;
- empirical Value validity;
- causal Value creation;
- Delta T_acc -> Delta Value;
- cross-domain Value comparability;
- predictive validity;
- economic, monetary, organizational or social Value;
- superiority of one candidate domain or VSL over another.

Any such claim requires separate evidence.

---

## 17. Freeze gate

Before VSL-SPEC-01 can be frozen, a governance review must verify:

1. Outcome and Value remain explicitly distinct.
2. The specification defines identification requirements rather than universal Value semantics.
3. The specification is independent of candidate-domain selection.
4. The specification is causally neutral.
5. Retrospective Value construction is prohibited.
6. Domain incompatibility can be reported without weakening the rules.
7. The frozen Synthetic Minimum v0.1 is preserved without reinterpretation.
8. No C09 field or unresolved C09 valuation assumption is imported.
9. No TGCV Core modification is introduced.
10. No RMA modification is introduced.
11. No Evidence-to-Claim Matrix upgrade follows from specification freeze alone.
12. GL-07 requirements are respected if later evidence is routed into the cumulative matrix.

---

## 18. Next methodological artifact

After VSL-SPEC-01 is frozen, the next artifact should be:

VSL-EXP-01 — Domain Candidate Compatibility and Experimental Protocol

Its purpose will be to evaluate candidate domains against the already-frozen Value-identification requirements.

The intended sequence is:

VSL-SPEC-01 -> freeze -> candidate-domain compatibility -> domain-specific VSL -> experimental protocol -> execution -> evidence

Domain selection must occur after the methodological rules for Value identification have been frozen.

---

## 19. Governance disposition

This artifact is a candidate methodological specification.

It does not modify:

- VSL_SYNTHETIC_MIN_v0.1;
- C09;
- TGCV Core;
- RMA;
- Evidence-to-Claim Matrix;
- any claim status.

No execution evidence is generated by creating this specification.

**Current status:** DRAFT / CANDIDATE FOR FREEZE
