# IUT-A-01 — Utility Extension Protocol 001

**Date:** 2026-09-11  
**Status:** `DESIGN FROZEN — UTILITY EXTENSION DEFINED`  
**Programme:** TGCV experimental line  
**Case:** `IUT-A-01`

## 1. Purpose

Extend the existing IUT-A-01 line from decision-time accessibility differentiation to **practical utility**, without making practical utility contingent on a prior demonstration of explanatory or discriminatory superiority.

TGCV therefore maintains two independent empirical lines:

1. **Explanatory/discriminatory line:** tests whether TGCV provides superior explanation, discrimination or reconstruction of transformations, accessibility, trajectories or related structures against appropriate alternatives.
2. **Utility line:** tests whether use of TGCV produces a measurable practical improvement in decision-making, action selection, exploration or value-relevant outcomes relative to an appropriate baseline.

The two lines may inform one another, but neither is a prerequisite for the other.

## 2. IUT-A-01 current position

The existing IUT-A-01 Stage-B executor is a bounded, outcome-blind comparison of a conventional baseline representation against a TGCV accessibility representation. It tests whether the represented option space changes at decision time and whether that difference is decision-relevant. The executor explicitly does **not** use downstream performance or outcome variables. 

This is a useful first utility layer, but it does not by itself establish practical utility.

## 3. Utility hierarchy

IUT-A-01 shall be developed through the following evidence layers:

### U1 — Decision-space utility

Question:

> Does TGCV expose decision-relevant alternatives or constraints that the baseline representation does not expose at the same decision point?

Primary observables:

- newly identified alternatives;
- alternatives correctly ruled out;
- relevant dependencies/restrictions identified;
- decision-space coverage;
- analyst/decision-maker effort required to reach the representation.

The existing IUT-A-01 Stage-B executor belongs to this layer.

### U2 — Decision-performance utility

Question:

> When decision-makers use TGCV versus the conventional baseline, do they make measurably better decisions or reach adequate decisions more efficiently?

Possible observables, selected ex ante for the concrete experiment:

- time to decision;
- number of viable alternatives considered;
- invalid alternatives considered;
- missed feasible alternatives;
- decision accuracy against a frozen ground-truth or adjudicated reference;
- rework caused by an initially inadequate decision;
- cognitive/operational effort.

No single metric is mandatory globally. The metric set must be frozen for each concrete experiment before outcome observation.

### U3 — Action/outcome utility

Question:

> Does using TGCV to select or construct an action produce better downstream operational outcomes than the conventional baseline under a controlled comparison?

Possible observables:

- execution time;
- resource consumption;
- throughput;
- quality or defect rate;
- resilience/recovery effort;
- number of failed or retried transformations;
- lifecycle cost;
- other domain-specific operational outcomes.

These are empirical outcomes, not definitions of TGCV itself.

### U4 — Value-construction utility

Question:

> Does TGCV use lead to measurable value realization under a defined practical context?

Potential evidence includes domain-specific economic, operational or strategic value measures. Any monetary/value claim requires explicit provenance, measurement definition and comparator logic; it must not be inferred from U1–U3.

## 4. Independence from explanatory superiority

A result in the explanatory/discriminatory line is **not required** before U1, U2 or U3 can be investigated.

Conversely, practical utility does not retroactively establish explanatory superiority.

Interpretation must therefore distinguish at least:

- `EXPLANATORY_SUPERIORITY`
- `DISCRIMINATORY_SUPERIORITY`
- `DECISION_SPACE_UTILITY`
- `DECISION_PERFORMANCE_UTILITY`
- `ACTION_OUTCOME_UTILITY`
- `VALUE_CONSTRUCTION_UTILITY`

A single experiment may contribute evidence to more than one category only where each category has its own predeclared operationalisation.

## 5. Null and positive outcomes

The utility line is falsifiable. At least the following outcomes remain open:

- TGCV adds no useful decision information;
- TGCV exposes additional alternatives but does not improve decisions;
- TGCV improves decisions without improving downstream outcomes;
- TGCV improves downstream outcomes without establishing explanatory superiority;
- TGCV improves both decision quality and downstream outcomes;
- TGCV utility is domain-dependent or context-dependent rather than general.

No outcome is assumed in advance.

## 6. Experimental control requirements

A utility experiment must, where applicable, freeze before execution:

- baseline method;
- TGCV-assisted method;
- decision-time information boundary;
- option universe or reference universe;
- task/context;
- outcome metrics;
- scoring rules;
- adjudication/reference procedure;
- stopping/termination rule;
- provenance and hashes.

Outcome information must not leak into the decision-time representation used to construct accessibility or option-space claims.

## 7. Relationship to Class-II fixtures

A Class-II fixture may establish methodological and bounded practical utility under the fixture boundary.

It does **not** by itself establish industrial utility, production benefit, financial value or generalisation beyond the fixture.

Accordingly, Class-II utility evidence should be treated as evidence of:

`UTILITY_WITHIN_FROZEN_FIXTURE_BOUNDARY`

not as automatic evidence of:

`INDUSTRIAL_UTILITY`

## 8. Routing consequence

The AWS-PatchAsgInstance B1 blocker does not block the TGCV utility line as a whole. It blocks only that particular candidate transformation under its frozen authorization boundary.

The next utility experiment may therefore be selected independently, provided it satisfies the same methodological controls and does not reuse an inadmissible transformation path.

## 9. Immediate experimental objective

The immediate objective is **not** to score utility retrospectively for an already observed outcome.

It is to identify and execute the smallest controlled experiment capable of progressing from the existing IUT-A-01 U1 evidence toward U2, while preserving outcome blindness at decision time and keeping explanatory/discriminatory claims logically separate.

## 10. Non-claims

This protocol does not establish:

- explanatory superiority;
- discriminatory superiority;
- industrial utility;
- causality;
- financial/value realization;
- general validity of TGCV;
- TGCV Core modification.
