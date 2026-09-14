# TGCV — C10-C Empirical Design Gate 001

**Status:** FROZEN FOR DESIGN — NO EXECUTION AUTHORIZED
**Date:** 2026-09-14
**Claim:** C10 — causal `ΔT_acc → ΔV`
**Precondition:** C10-A/B methodological sufficiency audit = PASS; exact C10-C gap defined.

## 1. Purpose

Freeze the minimum admissible empirical architecture for testing whether a credibly identified change in accessible transformations contributes causally to downstream value.

This gate defines what a study must establish **before** dataset selection, execution or case-specific adaptation. It is an ex-ante design contract, not an empirical result.

## 2. Target causal question

For a unit exposed to an accessibility-changing intervention or other credible source of exogenous variation:

> What is the causal contribution of the induced change in `T_acc` to an explicitly defined value endpoint, relative to the admissible counterfactual accessibility condition?

Canonical structure:

`Z → S_0/S_1 → T_acc,0/T_acc,1 → ΔT_acc → Reach/Trajectory → Outcome → V`

The target is a bounded causal contribution, not the generic association `ΔT_acc ↔ ΔV`.

## 3. Primary estimand

The default estimand is a treatment-effect contrast over value:

`τ_V = E[V(1) − V(0)]`

where treatment status indexes the accessibility-changing intervention/exposure and the intervention must induce a reconstructible change in `T_acc`.

Where the intervention does not deterministically map to the same `ΔT_acc` for all units, the design must distinguish:

- effect of assignment/intervention `Z` on value;
- effect attributable to induced accessibility change `ΔT_acc`;
- any instrumental-variable/complier or mediation estimand actually identified.

No stronger estimand may be claimed than the identification strategy supports.

## 4. Value endpoint requirements

`V` must be defined independently of `T_acc`, treatment assignment and observed downstream success.

The value endpoint must specify ex ante:

- construct being valued;
- unit of analysis;
- measurement scale and units;
- aggregation rule;
- time horizon;
- objective(s), preferences and constraints where relevant;
- direction of desirability;
- treatment of zero, negative and missing values;
- whether value is monetary, utility-like, performance-based, welfare-based or another explicit evaluative construct.

A value endpoint may be multidimensional, but the aggregation rule must be fixed before outcome inspection if a scalar estimand is required.

## 5. Accessibility operationalization

For each relevant unit, define:

`T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`

and reconstruct:

`ΔT_acc = T_acc,1 \ T_acc,0`,
`T_acc,0 \ T_acc,1`,

and any retained reconfiguration/substitution component.

The operationalization must state:

- transformation universe `U_τ`;
- accessibility predicate `P_τ`;
- structural state variables `S`;
- context variables `C`;
- fixed/local knowledge or enabling conditions `L`;
- observation times;
- rules for partial observability;
- reproducibility procedure;
- exclusion of downstream value/outcome variables from the accessibility predicate.

Native dataset fields may be used only when their semantic role is explicit. If `ΔT_acc` is reconstructed, the reconstruction must be auditable independently of the value endpoint.

## 6. Intervention / treatment requirement

The preferred design has a credible accessibility-changing intervention:

`Z → structural change → ΔT_acc`.

Acceptable identification families may include:

1. randomized structural accessibility intervention;
2. quasi-random or natural experiment with defensible exogeneity;
3. credible instrumental-variable design where the instrument changes accessibility and satisfies explicit exclusion assumptions;
4. other pre-specified causal designs with auditable identification assumptions.

A purely observational accessibility/value correlation is not sufficient for C10-C closure.

## 7. Counterfactual

The design must identify the value that would have occurred for the relevant unit under the counterfactual accessibility condition.

The counterfactual must be specified ex ante and must not be defined as “what happened before” unless the design provides a defensible reason that the untreated potential outcome is identified by that comparison.

Potential outcomes notation:

`V(1)` = value under the intervention-induced accessibility condition;

`V(0)` = value under the counterfactual accessibility condition.

## 8. Downstream mechanism architecture

The design should preserve the analytical chain:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.

At minimum, the study must observe or defensibly reconstruct the value endpoint and the major downstream outcome pathway.

Where data permit, mediation/mechanism analysis should distinguish:

- accessibility change;
- changed reachable alternatives;
- trajectory/sequence selection;
- execution intensity/quality;
- realized outcome;
- value evaluation.

Mechanism analysis is subordinate to causal identification and must not be used to manufacture an apparent `ΔT_acc` effect post hoc.

## 9. Confounding and competing mechanisms

Before admission, identify plausible simultaneous changes that could affect value independently of accessibility.

The design must specify how each material competitor is:

- randomized away;
- controlled by design;
- measured and adjusted under a justified model;
- isolated through timing or mechanism;
- or explicitly retained as an identification limitation.

The design must not treat every downstream improvement as evidence for `ΔT_acc`.

## 10. Required falsification / robustness tests

At minimum, candidate studies must define applicable tests for:

**F-C10-1 — Accessibility reconstruction integrity:** independently reproduce `T_acc,0`, `T_acc,1` and `ΔT_acc`.

**F-C10-2 — Pre-treatment balance / identification:** test the assumptions required by the selected causal design.

**F-C10-3 — Outcome timing:** verify that value changes occur after the accessibility intervention/change under the proposed causal ordering.

**F-C10-4 — Placebo / negative-control outcome or period:** where feasible, test an outcome or period that should not respond through the proposed pathway.

**F-C10-5 — Alternative mechanism:** test or bound a plausible competing explanation for the value difference.

**F-C10-6 — Accessibility-null comparison:** where feasible, identify a comparison in which structural conditions change without the hypothesized `ΔT_acc`, or where `ΔT_acc` remains unchanged despite treatment exposure.

**F-C10-7 — Heterogeneity:** pre-specify materially relevant effect heterogeneity rather than interpreting it post hoc as universality.

**F-C10-8 — Negative/null possibility:** retain zero and negative value effects as admissible outcomes.

## 11. Minimum evidence admission package

A C10-C candidate may enter empirical execution only if it can provide, at minimum:

1. frozen study/unit definition;
2. provenance and access record for all source data;
3. explicit `U_τ` and accessibility predicate or equivalent operational mapping;
4. reproducible `T_acc,0` and `T_acc,1` construction;
5. intervention/treatment definition;
6. identification strategy and assumptions;
7. counterfactual definition;
8. value endpoint specification;
9. downstream outcome/trajectory variables relevant to the pathway;
10. pre-specified estimand and analysis plan;
11. falsification/robustness plan;
12. frozen exclusion and admission rules;
13. exact provenance of derived variables;
14. reproducibility artifacts sufficient for independent reconstruction.

## 12. Evidence hierarchy

Preferred evidence, in descending order:

**Tier A — randomized structural accessibility intervention + explicit value endpoint + reproducible downstream pathway.**

**Tier B — strong quasi-experimental accessibility intervention with credible identification + explicit value endpoint.**

**Tier C — other defensible causal identification strategy with explicit assumptions and value endpoint.**

**Tier D — observational association or predictive evidence.**

Tier D may inform design or mechanism discovery but cannot by itself close C10-C.

## 13. C09 inheritance rule

C09 is already closed at bounded empirical causal-support level for accessibility effects on subsequent trajectories. Therefore a C10-C study must not repeat C09 as its primary research question.

C09 evidence can be inherited as upstream methodological/scientific context, but the C10-C study must independently establish the value endpoint and its causal contribution.

The incremental target is:

`ΔTrajectory → Outcome → Value`

under an accessibility change whose causal origin is credibly identified.

## 14. Closure criterion for C10-C

C10-C may be considered for claim-level closure only when a real-world study provides all of the following:

- independently defined accessibility states;
- reproducible `ΔT_acc`;
- credible causal identification of the accessibility-changing exposure/intervention;
- explicit independently defined value endpoint;
- defensible counterfactual;
- separation/bounding of major competing mechanisms;
- reproducible downstream data;
- causal estimate with uncertainty and identification assumptions;
- bounded interpretation.

The sign of the effect is not predetermined.

Possible outcomes:

- positive → supports a positive value contribution under the studied context;
- null → no evidence of value contribution in that context;
- negative → evidence that accessibility expansion/reconfiguration can reduce value under that context;
- heterogeneous → context-dependent causal contribution.

None of these results authorizes universalization without broader evidence.

## 15. Explicit exclusions

The following do not constitute C10-C closure:

- correlation alone;
- before/after without credible counterfactual;
- value inferred from outcome without an explicit value criterion;
- intervention without reconstructible `ΔT_acc`;
- `ΔT_acc` reconstructed using downstream value;
- C09 trajectory evidence alone;
- synthetic causal simulation alone;
- predictive superiority alone;
- industrial utility without a controlled value estimand.

## 16. Governance status

**C10-A:** PASS — bounded formal coherence.

**C10-B:** PASS — bounded architectural/non-redundancy sufficiency.

**C10-C:** OPEN — design frozen; empirical validation not yet performed.

**C10 overall:** OPEN.

**Execution authorization:** NONE.

**Dataset search authorization:** NONE under this gate. A subsequent explicit discovery/admission gate must authorize any candidate dataset or case search.

## 17. Next controlled operation

The next operation is a **C10-C Candidate Discovery / Dataset-First Admission Gate** that applies this frozen design contract to candidate real-world datasets/cases without changing the design retrospectively.
