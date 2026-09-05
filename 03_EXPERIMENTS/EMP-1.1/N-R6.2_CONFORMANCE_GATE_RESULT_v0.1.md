# N-R6.2 — LEARNER CONFORMANCE GATE RESULT v0.1

**Date:** 2026-09-05  
**Status:** **PASS / CLOSED — CONFORMANCE ONLY**

## 1. Decision

N-R6.2 Learner Conformance is **PASS / CLOSED**.

The prospective Branch N learner implementation conforms to the registered N-R6.1 learner specification as checked by `N_R6_CONFORMANCE_RUNNER_v0.1`.

This gate establishes implementation/specification conformance only. It does **not** constitute scientific execution, confirmatory evidence, historical code recovery, causal validation, or validation of the historical EMP-1.1 result.

## 2. Registered inputs

- Frozen predictor dataset: N-R5.3
- Train: 30,000 records; seed 3,100,000
- Test: 10,000 records; seed 4,100,000
- B dimension: 16
- R dimension: 58
- B+R dimension: 74
- Primary learner: `sklearn.ensemble.HistGradientBoostingClassifier`
- Primary metric: paired out-of-sample LogLoss
- Practical threshold: ΔLogLoss >= 0.04
- Alpha: 0.05
- Sign-flip permutations: 200,000
- Sign-flip seed: 13,579
- Control: RandomForestClassifier with registered fixed configuration

## 3. Conformance execution

Runner: `N_R6_CONFORMANCE_RUNNER_v0.1`

All registered checks returned PASS:

1. specification_exists
2. frozen_predictor_inputs_exist
3. B_R_BR_dimensions
4. primary_learner_class
5. HGB_fixed_configuration
6. same_HGB_configuration_for_both_arms
7. primary_metric_and_thresholds
8. signflip_registration
9. RF_control_configuration
10. historical_result_and_external_dependency_firewall
11. implementation_contains_no_execution_at_import
12. implementation_hash_recorded

Implementation SHA-256:

`08ccce5b8c41e8164872d81fa63756cced47c0fa2bfe5e36f00e7b9ab55ed079`

## 4. Scientific execution boundary

The conformance run reports:

- `scientific_execution = NOT_PERFORMED`
- `learner_execution = NOT_PERFORMED`
- `confirmatory_inference = NOT_PERFORMED`

No model was fitted to the frozen 30k/10k scientific corpus by this gate.

## 5. Historical-result firewall

The historical EMP-1.1 result was not used as a tuning target. The implementation/conformance firewall found no forbidden historical-result or external-dependency tokens.

The historical EMP-1.1 executable remains unrecovered. N-R6 is therefore explicitly a **controlled prospective reconstruction**, not a historical implementation recovery.

## 6. Environment

The conformance was executed in the user's local environment with:

- Python 3.14.7
- NumPy 2.5.2
- scikit-learn 1.9.0

The installed learner API was available sufficiently for all registered N-R6.2 configuration checks to pass.

## 7. Scientific claim boundary

This gate permits the next controlled step: execute the registered learner protocol against the frozen N-R5.3 predictor dataset.

It does **not** permit claims of:

- historical Cargo or historical EMP-1.1 implementation equivalence;
- causal effect of R in the general sense;
- universal superiority of the TGCV representation;
- cross-domain validity;
- literature novelty;
- reproduction of the historical numerical result.

## 8. Next authorized gate

**N-R7 — Controlled Learner Execution / Primary Evaluation**

Execution must use the frozen N-R5.3 predictor dataset without modification, preserve the B versus B+R paired evaluation, retain deterministic provenance, and produce an auditable execution record before any confirmatory interpretation is accepted.
