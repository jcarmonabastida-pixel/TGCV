# TI-001 V012 NEXT4 — Power and Sensitivity Analysis Specification 001

**Status:** DESIGN REVIEW — NO SCIENTIFIC EXECUTION AUTHORIZED  
**Date:** 2026-09-30  
**Parent:** NEXT4 Fixture Architecture and Analysis Specification 001

## 1. Purpose

Determine whether the provisional 1,728-unit architecture is adequate for the pre-specified NEXT4 discriminating contrast, without using observed NEXT4 data to choose sample size.

This is a design-stage sensitivity analysis. It is not a scientific execution and does not produce evidence for or against the NEXT4 hypothesis.

## 2. Primary estimand

The target is the mapping-following change in the action×profile association induced by the independently imposed future-structure permutation.

The primary simulation must therefore preserve the factorial structure needed to estimate:

`action_identity × profile_id × future_mapping`

rather than simulating a generic condition main effect.

## 3. Fixed design inputs

The simulation must use the frozen design architecture:

- 4 actions;
- 4 profiles;
- 24 future-structure permutations;
- STATIC_CONTROL, FUTURE_REASSIGNED, SURFACE_CONTROL and UNINFORMATIVE_NULL;
- 3 domains;
- 2 operationalisations;
- 4 presentation strata;
- provisional 3 replicates per permutation × domain × operationalisation × condition cell;
- provisional total 1,728 units.

Any change to these factors requires a versioned design amendment before the simulation is interpreted.

## 4. Effect-size parameterisation

No effect size may be estimated from NEXT3 Q5 and inserted as if it were an expected NEXT4 effect.

The sensitivity analysis must therefore use a pre-declared grid of hypothetical mapping-following effects.

At minimum the grid must include:

- null effect;
- very small effect;
- small effect;
- moderate effect;
- an upper scenario explicitly labelled optimistic, not expected.

The parameterisation must be expressed in the primary model's natural scale and translated to the response-probability scale used by the simulator.

## 5. Calibration rule

The simulation must not use NEXT3 response frequencies to manufacture a predicted NEXT4 effect.

NEXT3 may be used only to justify broad variance/model-structure choices already frozen in the specification, and any such use must be explicitly documented.

## 6. Monte Carlo design

For each effect-size scenario and candidate sample size:

1. generate a complete synthetic NEXT4 design using the frozen factorial architecture;
2. generate responses from the pre-declared model;
3. fit the exact planned analysis model;
4. compute the exact frozen primary contrast;
5. apply the frozen multiplicity procedure;
6. record convergence, rank, estimability and contrast recovery;
7. repeat for the declared number of simulation replicates;
8. summarise empirical rejection probability and diagnostic failure rates.

The simulation must use deterministic, versioned seeds.

## 7. Replication count

The simulation replication count must be large enough that Monte Carlo uncertainty around estimated power is reported explicitly.

Target: at least 2,000 independent simulation replicates per effect-size × sample-size scenario unless computational diagnostics demonstrate a reproducible reason for a different count.

The final artifact must report the Monte Carlo standard error or an equivalent uncertainty interval for every power estimate.

## 8. Candidate sample sizes

Evaluate at least:

- 1,728 units;
- 2,304 units;
- 3,456 units;
- 5,184 units;
- 6,912 units.

These are candidate scaling points preserving the factorial architecture.

No reduction below 1,728 is permitted solely because the simulation produces high power under an optimistic effect.

## 9. Success criterion

The design is considered quantitatively adequate only if the provisional or selected sample size has acceptable sensitivity across the pre-declared small-effect scenarios while maintaining acceptable model convergence and estimability.

No single arbitrary power threshold may be used without being declared before reviewing simulation results.

The decision rule must be frozen before the results are inspected.

## 10. Model diagnostics

Every simulation replicate must record:

- design-matrix rank;
- expected rank;
- convergence status;
- covariance validity;
- primary contrast estimability;
- singular-fit status;
- false-positive rejection under the null;
- whether the fitted model matches the frozen formula.

A sample-size scenario with unacceptable structural failure rates cannot be selected merely because its nominal power is high.

## 11. Type-I error calibration

The null scenario is mandatory.

Empirical rejection under the null must be reported after the frozen Holm procedure.

If type-I error is materially inflated or structurally unstable, the analysis model or design must be revised before any fixture is frozen.

Such a revision requires a new versioned specification and rerun of the full sensitivity analysis.

## 12. Mapping-alignment recovery

Because a generic condition difference is not sufficient evidence, the simulation must separately evaluate recovery of the **direction/alignment of the known permutation-induced reorganisation**.

Power is therefore reported for:

1. primary mapping-alignment contrast;
2. generic stable-versus-reassigned contrast as a diagnostic only.

The second quantity must never replace the first as the scientific criterion.

## 13. Domain dependence

Domain effects must be simulated as nuisance/design structure, not as the scientific signal.

At least one sensitivity scenario must include heterogeneous domain baselines while preserving the same true mapping-following effect across domains.

An additional scenario may include moderate domain-specific effect heterogeneity, explicitly labelled exploratory.

## 14. Operationalisation and presentation

Operationalisation and presentation effects must be included in simulation as non-primary factors.

At least one scenario must include modest presentation variation while preserving the mapping-following signal.

The simulation must verify that the primary contrast remains identifiable under these controls.

## 15. No post-hoc tuning

After simulation results are inspected, the following may not be tuned to improve power:

- effect-size definition;
- contrast definition;
- sample allocation;
- permutation family;
- model terms;
- multiplicity family.

Any change creates a new specification version and requires a fresh sensitivity analysis.

## 16. Required output artifact

The completed analysis must produce a machine-readable artifact containing:

- specification hash;
- code hash;
- simulation seed set;
- design scenarios;
- effect-size grid;
- sample-size grid;
- replicate count;
- power estimates;
- Monte Carlo uncertainty;
- null rejection rates;
- convergence/rank failure rates;
- covariance diagnostics;
- mapping-alignment recovery;
- selected design, if any;
- rationale tied only to the pre-declared decision rule.

## 17. Decision rule

The final sample size is selected by the frozen rule applied to the complete sensitivity table.

If no candidate satisfies the rule, NEXT4 does not proceed to fixture freeze. The design must be revised rather than executing an underpowered experiment.

## 18. Scientific boundary

This artifact does not establish a NEXT4 result and does not use NEXT3 Q5 as an assumed effect.

It exists solely to determine quantitative adequacy of the frozen design before fixture construction.

## 19. Next step

After this specification is reviewed, implement the deterministic power/sensitivity simulation and produce its audit artifact. Do not generate the scientific fixture or execute model decisions until the sensitivity analysis has passed its pre-declared decision rule.