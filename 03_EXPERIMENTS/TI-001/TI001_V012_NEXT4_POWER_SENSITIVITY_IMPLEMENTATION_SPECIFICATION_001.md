# TI-001 V012 NEXT4 — Power/Sensitivity Simulation Implementation Specification 001

**Status:** IMPLEMENTATION DESIGN — NOT SCIENTIFIC EXECUTION AUTHORIZED  
**Date:** 2026-09-30  
**Parent:** TI001_V012_NEXT4_POWER_SENSITIVITY_ANALYSIS_SPECIFICATION_001

## 1. Purpose

Define the reproducible implementation of the pre-registered NEXT4 power/sensitivity simulation.

This is a design-stage simulation only. It does not call the model provider, does not generate the scientific NEXT4 fixture, and does not constitute scientific execution.

## 2. Execution boundary

The implementation may generate only synthetic responses from the frozen simulation model.

Hard prohibition:
- no OpenAI/provider API calls;
- no NEXT4 scientific executor;
- no use of observed NEXT4 responses;
- no use of NEXT3 Q5 coefficient estimates as an assumed effect;
- no fixture freeze;
- no scientific result artifact.

## 3. Inputs

The implementation must consume versioned immutable inputs:
1. NEXT4 Power/Sensitivity Analysis Specification 001;
2. NEXT4 Fixture Architecture and Analysis Specification 001;
3. frozen action/profile/future-mapping design;
4. candidate sample-size grid;
5. pre-declared effect-size grid;
6. deterministic seed set;
7. frozen statistical-model implementation.

It must fail closed if any required input hash differs.

## 4. Simulation data-generating model

The simulator must generate categorical choices using the same bounded four-action response space planned for NEXT4.

The synthetic model must include action baseline terms, profile terms, action×profile structure, mapping-following action×profile reorganisation, and domain, operationalisation and presentation nuisance effects.

The exact coefficient parameterisation must be stored in the simulation configuration and cannot be altered after result inspection.

## 5. Effect grid

The effect grid must be defined on the primary model's natural parameter scale before simulation.

Required labels:
- NULL;
- VERY_SMALL;
- SMALL;
- MODERATE;
- OPTIMISTIC.

Each label must have a numerical definition in the configuration.

No label may be assigned from observed NEXT3 coefficients.

## 6. Mapping-following mechanism

For every simulated unit, the true action×profile structure must be generated from the declared profile→future permutation.

The simulator must expose a deterministic ground-truth object permitting recovery testing.

The primary signal is alignment with the known permutation, not merely a difference between condition means.

## 7. Candidate designs

At minimum simulate:
- N=1,728;
- N=2,304;
- N=3,456;
- N=5,184;
- N=6,912.

Every N must preserve the factorial architecture and balanced permutation family.

## 8. Replicates

Default target: 2,000 Monte Carlo replicates per effect-size × N scenario.

The implementation must record the actual completed count and fail the analysis audit if the declared minimum is not met.

## 9. Deterministic randomisation

Use a frozen seed schedule derived deterministically from master seed, scenario identifier, sample-size identifier and replicate identifier.

The derivation must be collision-free for declared identifiers and recorded in the result artifact.

No wall-clock or provider randomness may enter the simulation.

## 10. Exact analysis pipeline

Each replicate must:
1. construct the synthetic dataset;
2. construct the exact primary design matrix;
3. verify rank and expected rank;
4. fit the frozen primary model;
5. preserve convergence diagnostics;
6. compute the frozen primary mapping-alignment contrast;
7. apply the frozen Holm procedure;
8. classify rejection/non-rejection;
9. record covariance validity and singularity;
10. record mapping-alignment recovery;
11. record generic stable-vs-reassigned effect only as diagnostic.

No model term may be removed after a failed fit.

## 11. Null calibration

NULL scenarios must estimate empirical type-I error after multiplicity correction.

Type-I error must be reported separately from power.

A scenario with inflated null rejection or unstable estimation cannot be accepted by nominal power alone.

## 12. Diagnostic failure classes

Each replicate must be classified as applicable:
- FIT_PASS;
- RANK_FAIL;
- NONCONVERGENCE;
- COVARIANCE_INVALID;
- CONTRAST_NONESTIMABLE;
- OTHER_NUMERICAL_FAILURE.

Failures must not be silently converted to non-rejections.

## 13. Mapping-alignment recovery

The implementation must calculate whether the fitted interaction pattern recovers the known permutation-induced direction.

This requires a deterministic alignment criterion specified before execution and stored with the simulation configuration.

## 14. Monte Carlo uncertainty

For every estimated power and null-rejection rate, report an uncertainty interval or Monte Carlo standard error based on the actual completed replicate count.

No power estimate may be presented without its simulation uncertainty.

## 15. Pre-declared design-selection rule

The implementation must apply the decision rule from the parent specification without modification after results are visible.

The result must state whether each candidate N passes, which criterion failed where applicable, the selected N if any, and the exact rule version used.

If no N passes, status is DESIGN_REVISION_REQUIRED.

## 16. Output artifact

Produce one canonical machine-readable result containing:
- specification SHA256;
- implementation source SHA256;
- dependency/runtime versions;
- master seed;
- scenario seeds;
- effect grid;
- sample-size grid;
- completed replicate counts;
- power estimates;
- null rejection;
- Monte Carlo uncertainty;
- rank/convergence/covariance/estimability failures;
- alignment-recovery estimates;
- decision-rule evaluation;
- final status.

A human-readable report may accompany it but cannot replace the machine-readable artifact.

## 17. Reproducibility audit

Before accepting the simulation result:
1. rerun a fixed audit subset using the same seeds;
2. verify byte-identical synthetic data or equivalent deterministic hashes;
3. verify identical model outputs;
4. verify identical contrast values;
5. verify identical classifications.

Any mismatch blocks the result.

## 18. No scientific fixture contamination

Simulation output remains separate from the NEXT4 scientific fixture, scientific execution result, provider logs, model responses and primary scientific analysis artifact.

No simulation-generated response may enter the scientific fixture.

## 19. Implementation gate

Implementation-equivalence passes only if:
- all input hashes match;
- forbidden provider access is absent;
- deterministic replay passes;
- exact model/contrast match the frozen specifications;
- diagnostic fields are complete;
- no post-hoc tuning is detected.

Only after this gate may the power simulation be run.

## 20. Next action

Run the deterministic implementation audit first. If it passes, execute the design-stage Monte Carlo sensitivity analysis and publish the resulting audit artifact.

**Scientific NEXT4 execution remains unauthorized.**
