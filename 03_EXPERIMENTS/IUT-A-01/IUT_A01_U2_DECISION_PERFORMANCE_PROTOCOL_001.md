# IUT-A-01 — U2 Decision-Performance Utility Protocol 001

**Date:** 2026-09-11  
**Status:** `DESIGN FROZEN — EXECUTION NOT AUTHORIZED`  
**Case:** `IUT-A-01`  
**Utility layer:** `U2 — DECISION-PERFORMANCE UTILITY`

## 1. Research question

When decision-makers are given the same decision-time information, does a TGCV-assisted representation improve decision performance relative to the conventional baseline representation?

This question is independent of whether TGCV has already demonstrated explanatory or discriminatory superiority.

## 2. Hypotheses

**H0-U2:** TGCV assistance produces no practically meaningful improvement over the conventional baseline in the predeclared decision-performance metrics.

**H1-U2:** TGCV assistance produces a practically meaningful improvement in at least one predeclared primary decision-performance metric without introducing a material degradation in the remaining primary metrics.

The practical significance threshold must be frozen before outcome observation for the concrete execution.

## 3. Experimental arms

### Control — conventional baseline

Decision is performed using the frozen conventional representation/method already defined for the relevant IUT-A-01 task.

### Treatment — TGCV-assisted

Decision is performed using the frozen TGCV representation/method for the same task.

No arm may receive additional task information unavailable to the other arm except information constituting the intended representation difference.

## 4. Unit of analysis

The primary unit is one independent decision task under a frozen decision-time state/context.

A single task must have:

- a frozen decision state;
- a frozen option/reference universe or adjudication basis;
- identical underlying source information for both arms;
- a defined decision objective;
- a recorded final decision;
- predeclared scoring criteria.

Repeated tasks must be independently sampled or independently instantiated so that performance cannot be explained by simple memory of a previous trial.

## 5. Primary metrics

At least one primary metric from each category below should be selected before execution:

1. **Decision quality / accuracy** — correctness against a frozen reference or adjudicated ground truth.
2. **Decision time / effort** — time or bounded effort required to reach an admissible decision.
3. **Decision completeness** — capture of relevant viable alternatives and/or avoidance of relevant invalid alternatives.

Secondary metrics may include:

- number of alternatives considered;
- number of unnecessary alternatives explored;
- number of missed feasible alternatives;
- rework after decision;
- explanation/justification completeness;
- confidence calibration;
- user-reported cognitive effort.

Metrics must be frozen before outcome collection.

## 6. Reference and adjudication

Where no objective ground truth exists, the experiment must define an independent adjudication procedure before execution.

The adjudicator must not be given the TGCV result as the correctness criterion. The reference should be derived from frozen case information, domain rules, or an independently constructed expert/reference process.

The adjudication procedure is part of the experiment and must itself be reproducible.

## 7. Randomisation / counterbalancing

Where human or agent decision-makers perform repeated tasks, the execution should randomise or counterbalance treatment/control presentation order to reduce order and learning effects.

The exact allocation procedure must be frozen and recorded.

Where a paired design is used, the pairing variable and task equivalence criteria must be frozen.

## 8. Information-control rule

The following must remain identical across arms unless the difference is itself the intended TGCV intervention:

- underlying task data;
- decision-time cutoff;
- option/reference universe;
- task objective;
- time budget;
- external data availability;
- execution authority;
- adjudication standard.

Outcome information must never be available during the decision phase.

## 9. Practical-significance rule

Statistical significance alone is insufficient.

Before execution, a minimum practically meaningful improvement threshold must be frozen, for example:

- minimum reduction in median decision time;
- minimum improvement in decision accuracy;
- minimum reduction in missed viable alternatives;
- or another domain-specific threshold.

The concrete experiment may use a composite criterion, but the criterion must be specified ex ante.

## 10. Analysis contract

The analysis must report separately:

- TGCV vs baseline effect on each primary metric;
- direction and magnitude of each effect;
- uncertainty interval or equivalent uncertainty representation where applicable;
- task-level distribution rather than only an aggregate average where feasible;
- any trade-off between decision quality and decision effort;
- protocol deviations;
- exclusions and missing data;
- adverse effects or regressions attributable to TGCV assistance.

No post-hoc selection of the winning metric is permitted.

## 11. Interpretation matrix

Possible U2 conclusions include:

- `U2-POSITIVE`: practically meaningful improvement under the frozen criterion;
- `U2-NULL`: no practically meaningful improvement;
- `U2-MIXED`: improvement in some metrics with material degradation in others;
- `U2-INDETERMINATE`: protocol, evidence or reference integrity insufficient.

None of these conclusions establishes explanatory superiority, causal generalisation or industrial utility by itself.

## 12. Relationship to IUT-A-01 U1

U1 asks whether TGCV changes the decision-space representation.

U2 asks whether that representational difference changes the quality/efficiency of decisions.

Therefore the intended chain is:

`TGCV representation → changed accessible decision-space representation (U1) → changed decision performance (U2)`

U1 may be null while U2 is null or unexpectedly positive through other mechanisms; such a result must be analysed explicitly rather than assumed impossible.

## 13. Relationship to explanatory/discriminatory line

U2 does not require an earlier PASS on explanatory or discriminatory superiority.

Conversely:

`U2-POSITIVE ≠ EXPLANATORY_SUPERIORITY`

A positive U2 result establishes practical decision-performance utility under the tested conditions, not a stronger scientific explanation of the underlying phenomenon.

## 14. Execution boundary

This document freezes design only.

Execution is **not authorized** until a concrete U2 fixture/task package is frozen with:

- task set;
- control representation;
- TGCV representation;
- reference/adjudication method;
- primary metrics;
- practical-significance thresholds;
- allocation/randomisation rule;
- stopping rule;
- provenance and integrity hashes.

No industrial transformation is required for the first U2 execution. A bounded reproducible fixture is acceptable for methodological validation.

## 15. Non-claims

This protocol does not establish:

- explanatory superiority;
- discriminatory superiority;
- action/outcome utility;
- financial/value realization;
- industrial utility;
- general validity;
- TGCV Core modification.
