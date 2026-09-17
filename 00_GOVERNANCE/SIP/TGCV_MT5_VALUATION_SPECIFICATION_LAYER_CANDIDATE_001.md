# TGCV — MT5 Valuation Specification Layer Candidate 001

**Date:** 2026-09-17  
**Status:** `CURRENT_INDEPENDENT ANALYSIS`  
**Scope:** Value track following MT5-11e

## 1. Trigger and research question

MT5-11 closed with a bounded reproducibility result: two independent analysts, using the same frozen C09/KGFS evidence boundary, independently recovered the same underdetermination of `V*`. The unresolved information was substantive valuation specification: valuation objective, direction, and explicit `O → V*` mapping, together with the absence of a uniquely designated Value endpoint.

The present analysis asks whether that missing information can be represented as an explicit **domain-bounded Valuation Specification Layer** (`VSL`) that remains external to `T_acc`, is independently auditable, and can be tested for reproducibility without presupposing a universal substantive definition of Value.

This is a new methodology candidate. It is not an upgrade of the existing Value construct.

## 2. Separation principle

The candidate architecture is:

`T_acc / trajectory → independently measured outcome O → VSL → V*`

with the strict boundary:

`VSL ⟂ construction of Pτ, T_acc, ΔT_acc`

The valuation specification is downstream of the empirically reconstructed outcome. It cannot be used to define accessibility, admissibility, transformation identity, or the treatment itself.

The layer is therefore external to the TGCV transformational core and functions as an explicit interpretive specification for a domain-bounded Value candidate.

## 3. Candidate VSL components

### VSL1 — Reference entity

Declare the entity relative to which Value is assessed: e.g. household, user, organization, system, population, or other explicitly bounded unit.

### VSL2 — Valuation objective

Declare the substantive objective under which the outcome is considered value-relevant. The objective must be explicit rather than inferred from the fact that the outcome improved.

### VSL3 — Direction rule

Declare which outcome changes are value-increasing, value-decreasing, or neutral under the stated objective. The direction rule must be reproducible and must not be smuggled in through generic language such as “better” or “beneficial”.

### VSL4 — Outcome-to-Value mapping

Declare the explicit mapping from the independently measured outcome `O` to the domain-bounded candidate `V*`. The mapping may be multidimensional and need not collapse the outcome into a universal scalar.

### VSL5 — Reference frame

Declare baseline/comparator, temporal horizon, population/domain scope, and any other comparison frame required to interpret `O`.

### VSL6 — Measurement rule

Declare the reproducible endpoint, index, vector, contrast, or estimand used to represent `V*`. Measurement of `O` and interpretation as `V*` must remain distinguishable.

### VSL7 — Decision/interpretation rule

Declare the deterministic or explicitly parameterized rule that converts the specified outcome representation into `V*`. This is the formal point at which the valuation specification becomes executable rather than merely descriptive.

### VSL8 — Provenance and versioning

Record the source, version, date/effective period, and provenance of the valuation specification itself. Changes to the specification must be distinguishable from changes in empirical outcome data.

### VSL9 — Non-circularity

The VSL must not contain `ΔT_acc`, treatment assignment, the observed causal effect, or the downstream conclusion as part of the Value definition. It may be applied after those quantities are reconstructed, but must not define them.

### VSL10 — Domain-boundedness

Declare the domain, population, actor, and substantive scope to which the specification applies. No domain-specific objective or direction rule is promoted to a TGCV universal primitive by default.

### VSL11 — Independent reproducibility

A second analyst, given the frozen outcome evidence and the frozen VSL specification, must be able to reconstruct the same `V*` without additional coaching or unstated normative assumptions.

## 4. Distinction from I_V

`I_V` previously captured the information architecture needed to interpret outcomes as Value. MT5-11 showed that the architecture is reproducible but that the empirical evidence alone does not supply the missing substantive valuation specification.

The VSL candidate therefore does not replace `I_V`; it makes its unresolved substantive inputs explicit as a separately declared and versioned methodological object.

Conceptually:

`Outcome O + VSL(domain-bounded) → V*`

while:

`I_V` describes the information requirements and audit conditions that the VSL must satisfy.

Thus the candidate preserves the useful transversal architecture without pretending that the substantive valuation objective is discovered automatically from outcome data.

## 5. Minimal admissibility conditions for a VSL

A VSL candidate is admissible only if all of the following hold:

1. **Externality:** it is downstream of outcome measurement and does not construct `T_acc`.
2. **Explicitness:** objective, direction, mapping, reference and measurement are stated rather than inferred.
3. **Domain-boundedness:** substantive semantics are explicitly scoped.
4. **Non-circularity:** the TGCV causal pathway is not embedded in the Value definition.
5. **Reproducibility:** another analyst can execute the same specification and recover the same `V*`.
6. **Versionability:** the specification can be frozen, hashed, cited and changed independently of empirical data.
7. **Substantive provenance:** any normative or domain-specific content has an identifiable declared source or rationale rather than being silently introduced by the analyst.

## 6. What this candidate does NOT assert

The candidate does not assert:

- that Value is a universal scalar;
- that all domains share one substantive valuation objective;
- that valuation is necessarily monetary;
- that an outcome is Value merely because it is downstream or statistically improved;
- that `VSL` belongs in TGCV Core;
- that `ΔT_acc → ΔV` is causally identified;
- that a domain-bounded `V*` is automatically comparable across domains.

## 7. Testable propositions

### P1 — Specification completeness

A frozen VSL can explicitly instantiate the unresolved valuation fields identified by MT5-11 without altering the empirical outcome definition.

### P2 — Execution reproducibility

Two independent analysts applying the same frozen VSL to the same frozen outcome evidence recover materially equivalent `V*`.

### P3 — Outcome/specification separation

Changing the VSL while holding the empirical outcome evidence fixed changes only the valuation interpretation, not `T_acc`, the reconstructed trajectory, or the outcome measurement.

### P4 — Version separation

Changes in VSL version can be tracked independently from changes in empirical evidence version.

### P5 — Domain boundedness

A VSL can be valid within its declared domain without being promoted to a universal TGCV Value definition.

These propositions are methodological and do not establish a causal `ΔT_acc → ΔV` relation.

## 8. Candidate failure modes

The candidate must be rejected or narrowed if any of the following occurs:

- the VSL cannot be written without hidden normative assumptions;
- different analysts derive materially different `V*` from the same frozen VSL and outcome evidence;
- the VSL changes the operational definition of `T_acc` or treatment;
- the VSL embeds the observed treatment effect or downstream conclusion;
- the substantive source of the valuation objective cannot be identified;
- a purported domain-bounded specification silently becomes a universal Value ontology;
- specification version changes cannot be distinguished from empirical-data changes.

## 9. Relation to MT5-11

MT5-11 establishes the empirical motivation for this candidate: the current frozen C09/KGFS evidence did not determine the valuation objective, direction, or `O → V*` mapping, despite two independent analysts agreeing on that underdetermination.

Therefore the correct response is not to infer those fields retrospectively from the data. The methodological alternative is to make them an explicit external specification and test whether that specification is itself reproducible.

## 10. Proposed next controlled test

The next test should be a **VSL Specification Completeness and Reproducibility Gate** using one domain-bounded case and a frozen VSL specification.

The gate should first test specification completeness before asking analysts to execute it. It should then test independent reconstruction from the frozen specification and frozen outcome evidence.

The test must preserve the MT5-11 controls:

- no cross-analyst coaching;
- frozen input evidence;
- frozen specification before execution;
- independent analysts;
- explicit recording of unresolved assumptions;
- no Core/RMA/Matrix change by protocol alone;
- no inference of universal Value from a domain-bounded result.

## 11. Governance disposition

**MT5-VSL-01: `CANDIDATE METHODOLOGY IDENTIFIED — NOT YET EMPIRICALLY TESTED`.**

No TGCV Core modification.  
No RMA modification.  
No Evidence→Claim Matrix upgrade.  
No STATUS claim upgrade.  
No C09 status change.  
No causal claim `ΔT_acc → ΔV`.

The candidate remains external to the transformational core until independently tested.
