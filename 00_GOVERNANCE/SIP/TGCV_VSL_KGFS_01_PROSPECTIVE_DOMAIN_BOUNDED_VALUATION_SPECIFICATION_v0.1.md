# TGCV — VSL-KGFS-01
## Prospective Domain-Bounded Valuation Specification — C09 / KGFS

**Status:** DRAFT — NOT FROZEN  
**Version:** v0.1  
**Parent requirements:** VSL-SPEC-01 v0.1 — FROZEN  
**Compatibility protocol:** VSL-EXP-01 v0.1 — FROZEN  
**Candidate:** CD-05 — C09 / KGFS Rural Banking  
**Purpose:** Construct, prospectively and explicitly, a domain-bounded valuation specification capable of resolving the Value-identification fields that were underdetermined in MT5-08/10/11.

---

## 1. Purpose and boundary

This artifact is a **prospective specification attempt**, not a reinterpretation of the existing KGFS results.

Its purpose is to determine whether the unresolved Value-identification fields can be specified explicitly, independently and reproducibly while remaining external to `T_acc`.

It does not:

- redefine VSL-SPEC-01;
- reinterpret MT5-11;
- convert an existing outcome into Value retrospectively;
- claim that the proposed construct is already valid;
- establish causal Value creation;
- modify C09;
- modify TGCV Core or RMA;
- modify the Evidence-to-Claim Matrix.

No field in this draft is considered frozen merely because it is written here.

---

## 2. Why CD-05 is used as the prospective test case

CD-05 is used because the canonical MT5 sequence already identified the exact missing methodological fields and completed an independent underdetermination test.

This is not a ranking of CD-05 against other candidates.

It is a controlled methodological continuation of the already documented KGFS Value-interpretation problem.

The starting point is therefore:

`MT5-11: UNDERDETERMINATION OF V* FROM FROZEN EVIDENCE`

The question is whether a **new prospective specification**, frozen before any new Value-oriented execution, can remove that underdetermination without importing unsupported assumptions.

---

## 3. Frozen facts versus new specification

### 3.1 Frozen empirical/material facts

The existing evidence establishes, within its documented boundaries:

- a defined KGFS empirical setting;
- downstream financial/economic and poverty/wellbeing outcomes;
- longitudinal temporal structure;
- independent measurement of downstream outcomes;
- separation of those outcomes from `T_acc`;
- reproducible reconstruction of the existing outcome material;
- independent reconstruction agreement in MT5-11 that the existing evidence does not uniquely determine `V*`.

These facts are not altered by this draft.

### 3.2 New methodological content

Everything below is a **candidate specification** and must be justified independently before freeze.

In particular, the following cannot be inherited merely from the fact that the outcomes are described as beneficial, welfare-relevant, economic, or downstream:

- Value perspective;
- Value reference entity;
- valuation objective;
- directionality;
- Outcome-to-Value mapping;
- aggregation;
- treatment of trade-offs.

---

## 4. Required Value specification object

The candidate domain-specific Value construct is represented provisionally as:

`V*_KGFS = F(O, R, P, G, H, A, U)`

where:

- `O` = independently measured downstream Outcome;
- `R` = reference entity/frame;
- `P` = evaluative perspective;
- `G` = valuation objective;
- `H` = time horizon;
- `A` = aggregation/trade-off rule where required;
- `U` = uncertainty/missingness rule.

This notation is an interface placeholder, not a substantive definition of Value.

The function `F` must not inspect:

- `T_acc`;
- `Delta T_acc`;
- transformation identity;
- selected transformation;
- treatment assignment;
- accessibility-change status;
- case labels encoding expected results.

---

## 5. Unit of analysis

### Candidate specification

**Unit:** household/beneficiary-level longitudinal observation, subject to the exact unit defined by the frozen domain dataset and measurement protocol.

### Required freeze condition

The final specification must identify:

- the entity to which Value is attributed;
- whether the unit is household, individual beneficiary or another explicitly supported entity;
- whether Value is individual, household-level or aggregated;
- the rule for changes in unit membership.

### Status

**DRAFT — REQUIRES EVIDENCE-BACKED FREEZE.**

The existing evidence supports household/beneficiary-level interpretation but does not by itself settle the complete Value attribution rule.

---

## 6. Evaluative perspective

### Candidate requirement

The specification must declare whose Value is being evaluated.

Candidate perspectives that may be investigated include:

- beneficiary/household;
- another explicitly documented actor;
- a declared decision perspective.

No perspective is selected by this draft solely because it produces a particular interpretation.

### Freeze condition

The selected perspective must be justified independently of observed experimental results and frozen before any new Value-oriented execution.

### Status

**UNRESOLVED.**

---

## 7. Outcome construct

### Candidate specification

The Outcome must be selected from independently measured downstream variables already admissible under the domain evidence boundary.

Potential outcome families include documented financial/economic and poverty/wellbeing measures.

The final Outcome construct must be:

- independently measured;
- reproducible;
- external to `T_acc`;
- fixed before new execution;
- independent of the observed transformation result.

### Prohibition

The Outcome may not be selected after inspection of a new experimental result because it produces the most favorable Value classification.

### Status

**PARTIALLY SPECIFIED.**

---

## 8. Reference entity and reference frame

### Candidate requirement

The specification must distinguish:

1. the entity to which Value is attributed; and
2. the reference against which Value is evaluated.

A reference may be:

- baseline;
- benchmark;
- alternative;
- target;
- counterfactual;

but its methodological status must be explicit.

### Freeze condition

The reference must be fixed before new Value-oriented results are inspected.

### Status

**UNRESOLVED.**

---

## 9. Valuation objective

This is the principal unresolved semantic field.

The specification must state **why the selected Outcome is Value-relevant for the declared perspective**.

A valid objective cannot simply be:

- “improvement”;
- “benefit”;
- “economic relevance”;
- “welfare”;

without a domain-supported operational interpretation.

The objective must be sufficiently explicit that two independent analysts can determine whether a given Outcome satisfies it without importing different normative assumptions.

### Status

**UNRESOLVED — CRITICAL GATE.**

No `V*` is defined until this field is resolved.

---

## 10. Directionality

The specification must state how changes in the Outcome map to Value.

Possible forms include:

- ordinal;
- scalar;
- non-monotonic;
- thresholded;
- multidimensional/non-ordinal.

No form is assumed by VSL-SPEC-01.

### Freeze condition

The direction rule must be justified independently and frozen before execution.

### Status

**UNRESOLVED — CRITICAL GATE.**

---

## 11. Outcome-to-Value mapping

The mapping must be explicit and reproducible:

`O -> V*_KGFS`

It must identify:

- admissible inputs;
- transformation rule;
- output type;
- treatment of ties/neutral cases;
- treatment of incompatible observations;
- any normalization;
- any aggregation.

The mapping must not be inferred from the empirical result.

### Status

**UNRESOLVED — CRITICAL GATE.**

---

## 12. Time horizon

The specification must define the temporal interval over which Value is evaluated.

The existing KGFS material provides longitudinal framing, but the Value horizon must be explicitly declared.

### Status

**CANDIDATE: longitudinal baseline-to-endline horizon, subject to evidence-backed specification.**

This is not frozen.

---

## 13. Costs, benefits and trade-offs

If the declared Value construct includes multiple dimensions, the specification must state:

- which dimensions count;
- which are costs;
- which are benefits;
- whether trade-offs are allowed;
- how adverse effects are treated;
- whether one dimension can offset another;
- what happens when dimensions conflict.

A dimension may not be omitted after observing results.

### Status

**UNRESOLVED — CRITICAL GATE if multidimensional Value is retained.**

---

## 14. Aggregation

If Value is multidimensional or applies across multiple entities, the specification must define aggregation before execution.

The specification must state whether aggregation is:

- unnecessary;
- additive;
- weighted;
- lexicographic;
- threshold-based;
- otherwise formally defined.

Weights or priorities cannot be selected from observed results.

### Status

**UNRESOLVED.**

---

## 15. Uncertainty and missingness

The specification must define treatment of:

- missing observations;
- uncertain observations;
- ambiguous coding;
- incomplete longitudinal records;
- incompatible measurements.

The rule must be fixed before interpreting Value.

Existing measurement reproducibility does not automatically establish a Value-specific missingness rule.

### Status

**PARTIALLY SPECIFIED.**

---

## 16. Non-circularity

The following boundary is mandatory and already inherited from VSL-SPEC-01:

`T_acc / transformation / treatment -> downstream trajectory -> O -> V*`

is an allowed analytical architecture.

However, the VSL itself must implement only the downstream evaluative mapping.

It must not use:

- `T_acc`;
- `Delta T_acc`;
- transformation identity;
- treatment;
- accessibility flags;
- case labels encoding expected results;
- Value-derived variables.

### Status

**PASS — ARCHITECTURAL REQUIREMENT.**

---

## 17. Independent reproducibility gate

Before any Value experiment is authorized, two independent analysts must be able to reconstruct the same `V*` from:

1. the frozen domain-specific VSL;
2. the frozen Outcome data/definition;
3. the frozen reference;
4. the frozen perspective;
5. the frozen objective;
6. the frozen mapping;
7. the frozen uncertainty/missingness rules.

No analyst may receive the other's interpretation before their own reconstruction is frozen.

### Status

**REQUIRED — NOT YET EXECUTED.**

---

## 18. Compatibility with MT5-11

This specification does not invalidate MT5-11.

MT5-11 remains the evidence that the **existing frozen evidence alone** underdetermined `V*`.

The present draft asks a different question:

> Can a new, explicit, prospective valuation specification supply the missing semantic rules without deriving them from observed outcomes?

If the answer is no, the domain remains blocked.

If the answer is yes, the resulting specification must still pass independent reproducibility before any experimental claim is considered.

---

## 19. Freeze gate for VSL-KGFS-01

This draft may be frozen only if all critical fields are resolved:

- unit;
- evaluative perspective;
- Outcome;
- reference entity/frame;
- valuation objective;
- directionality;
- Outcome-to-Value mapping;
- time horizon;
- costs/benefits/trade-offs where applicable;
- aggregation where applicable;
- uncertainty/missingness;
- non-circularity;
- independent reproducibility protocol.

A field is not “resolved” merely because a plausible choice exists.

Each substantive field requires an evidence-backed justification that is independent of future experimental results.

---

## 20. Failure condition

If the valuation objective, directionality or Outcome-to-Value mapping cannot be specified without importing unsupported normative assumptions, the correct result is:

`VALUE_NOT_IDENTIFIED`

The specification must not be weakened to obtain `VALUE_IDENTIFIED`.

---

## 21. Governance disposition

**Current status:** DRAFT — NOT FROZEN

This artifact:

- does not establish Value;
- does not establish `V*`;
- does not generate experimental evidence;
- does not authorize execution;
- does not modify C09;
- does not modify Core;
- does not modify RMA;
- does not modify the Evidence-to-Claim Matrix;
- does not alter MT5-08, MT5-10 or MT5-11.

The only purpose of this draft is to make the unresolved semantic requirements explicit and test whether they can be prospectively specified without circularity.

## 22. Next gate

Before any freeze decision, each unresolved field must be subjected to an **independent specification audit** against the canonical KGFS evidence and the frozen VSL-SPEC-01 requirements.

Only after that audit may the project determine whether VSL-KGFS-01 can be frozen or must remain `VALUE_NOT_IDENTIFIED`.
