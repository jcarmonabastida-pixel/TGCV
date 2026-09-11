# IUT-A-01 — U2 Decision-Performance Fixture Specification 001

**Date:** 2026-09-11  
**Status:** `FIXTURE DESIGN FROZEN — EXECUTION NOT AUTHORIZED`  
**Case:** `IUT-A-01`  
**Utility layer:** `U2 — DECISION-PERFORMANCE UTILITY`

## 1. Purpose

Provide the smallest reproducible fixture capable of testing whether TGCV-assisted decision-making improves decision performance relative to a conventional baseline.

The fixture is deliberately synthetic and bounded. It is intended to establish methodological utility before industrial deployment.

## 2. Decision problem

Each trial represents a system configuration in which a decision-maker must choose one transformation from a finite option universe.

For every trial, the frozen fixture defines:

- current state `S_t`;
- available transformation candidates;
- prerequisites/dependencies for each candidate;
- hard feasibility constraints;
- a frozen task objective;
- the correct admissible decision set;
- a preferred decision where more than one feasible option exists.

The decision-maker must select one admissible option within the time budget.

## 3. Experimental arms

### Control

A conventional representation containing:

- current-state description;
- static option descriptions;
- directly listed prerequisites;
- task objective.

The representation does not explicitly construct a transformation-accessibility relation.

### TGCV

A representation containing the same underlying information plus an explicit decision-time mapping of:

`state → accessible transformations → dependency conditions → admissible decision space`

No additional factual information may be introduced by the TGCV arm.

## 4. Trial classes

The frozen trial set should contain at least four classes so that utility cannot depend on a single trivial pattern:

1. **Direct-feasibility trials** — the best option is directly available.
2. **Dependency trials** — the preferred option depends on conditions that must be tracked explicitly.
3. **Constraint-conflict trials** — superficially attractive options violate one or more hard constraints.
4. **Alternative-space trials** — the preferred option is not the default/current option but is reachable through a valid transformation path.

Each class must contain multiple independent trials.

## 5. Ground truth

Ground truth is generated exclusively from the frozen fixture rules.

For each trial the reference artifact must contain:

- admissible options;
- inadmissible options and violated constraint(s);
- preferred option(s), where defined;
- minimum justification required for a correct decision.

Ground truth is produced before any participant/executor sees the task and remains immutable during execution.

## 6. Primary U2 metrics

### M1 — Decision correctness

Binary/ordinal score indicating whether the selected option satisfies the frozen admissibility and preference rules.

### M2 — Decision time

Elapsed time from task presentation to recorded decision.

### M3 — Missed viable alternative rate

Fraction of trials in which the decision-maker fails to identify/select a viable preferred alternative when such an alternative exists in the frozen ground truth.

## 7. Secondary metrics

Where instrumentation permits:

- invalid-option selection rate;
- number of options inspected before decision;
- justification completeness;
- number of dependency/constraint violations;
- post-decision correction/rework;
- confidence versus correctness.

Secondary metrics cannot replace a primary metric post hoc.

## 8. Practical significance threshold

For the first execution, U2 success requires all of the following:

1. no statistically/evidentially material degradation in M1;
2. a predeclared improvement in M2 **or** M3 exceeding the execution threshold frozen in the trial manifest;
3. the effect must be attributable to the representation difference rather than unequal information or unequal task difficulty.

The numeric threshold shall be frozen in the execution manifest before trial execution.

## 9. Trial allocation

For repeated human/agent execution, trials should be randomly allocated or counterbalanced between control and TGCV conditions.

No participant/executor may receive the same trial first in one arm and then use memory to solve it in the other arm unless the experimental design explicitly models and controls the learning effect.

## 10. Information symmetry

Both arms receive identical source facts and identical decision-time cutoff.

Only the representation of those facts differs.

Forbidden:

- outcome leakage;
- additional facts in the TGCV arm;
- hidden manual hints;
- analyst intervention during execution;
- changing the trial universe after observations begin.

## 11. Execution record

The execution artifact must record per trial:

- trial ID;
- arm;
- fixture version/hash;
- task start timestamp or monotonic timer reference;
- decision timestamp/duration;
- selected option;
- correctness score;
- missed viable alternative flag;
- invalid-option flag;
- optional justification and confidence;
- protocol deviations.

## 12. Expected evidence products

The U2 execution shall produce:

1. frozen fixture manifest;
2. trial dataset;
3. control/TGCV presentation specification;
4. execution log;
5. scoring output;
6. primary comparison report;
7. integrity hashes;
8. final U2 classification: `POSITIVE`, `NULL`, `MIXED`, or `INDETERMINATE`.

## 13. Interpretation limits

A positive result means:

`TGCV_DECISION_PERFORMANCE_UTILITY_WITHIN_FIXTURE = SUPPORTED`

It does not mean:

`TGCV_EXPLANATORY_SUPERIORITY = PROVEN`

nor:

`TGCV_INDUSTRIAL_UTILITY = PROVEN`

The result is methodological utility evidence bounded to this fixture until replicated in additional contexts.

## 14. Execution gate

Execution remains `NOT AUTHORIZED` until the numeric practical-significance threshold, trial count, and exact trial manifest are frozen and hashed.
