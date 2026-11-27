# C10-S — Static design review of the direct theta_A calibration protocol

**Date:** 2026-11-27  
**Status:** STATIC REVIEW COMPLETE / FOUR OBJECTIVES CONFIRMED / DESIGN DECISIONS OPEN / NO EXECUTION  
**Branch:** research/c10s-m1-engine12-source-only-20261127  
**Scope:** Direct theta_A Analyzer/Evaluator, calibration protocol, focal DGP and nested M/R precision module  
**Authorization:** No code changes, tests, seed-bank generation, calibration, simulation, benchmark, holdout, workflow or scientific execution.

## 1. Decision

The next C10-S calibration phase is organized around four objectives, evaluated on the same direct causal experiment:

1. causal point recovery of theta_A(q_X*, g_A0, g_A1; r_common, V_cont);
2. inferential interval coverage and availability;
3. Monte Carlo precision sufficient to choose N, M and R economically;
4. correct identification, non-identification and abstention behaviour.

These are not four separate experiments and do not justify four new workstreams. The existing direct DGP → sealed evidence → Analyzer → independent Evaluator → calibration aggregator is the primary pipeline.

M1-PCT remains F5-only. It does not replace or calibrate the direct theta_A interval. No additional interval-engine implementation is recommended.

## 2. Historical reconstruction and reuse

This review reuses the existing work:

- Gate 129: theta_A estimand selection, identification limits and P178 boundary. P178 remains a bounded benchmark, not direct theta_A evidence.
- V_cont Calibration and Seed-Bank Protocol: disjoint banks, scenario-specific reporting, explicit numeric targets and no automatic promotion of test tolerances. Its earlier Phase-A benchmark and N/R values are not automatically transferable to direct theta_A.
- theta_a_analyzer.py and theta_a_evaluator.py: current direct interval implementation and independent reconstruction.
- theta_a_calibration_protocol.py: current N×M×R capture, truth binding, metrics, bank separation and aggregation.
- theta_a_nested_mc_precision.py: existing nested precision analysis of per-R contributions.

No new estimand, DGP family, scenario, test ID or execution gate is introduced.

## 3. Direct inferential interval: source-level finding

The direct Analyzer uses the history-standardized two-arm Horvitz–Thompson contrast. For each target history it uses the declared assignment probabilities and target mass to construct the bounded contribution range, then computes the HOEFFDING_TWO_STAGE_BOUNDED_HT_V1 radius from the sum of squared ranges and the declared confidence level.

The Evaluator independently reconstructs the same range sum, radius, confidence level and interval endpoints from sealed evidence and the analysis contract. Calibration capture stores the Evaluator's inference_truth_covered and interval width against separately materialized/reserved theta_A truth.

**Finding:** the calibration protocol is pointed at the correct inferential object. It assesses coverage of the actual direct theta_A interval; it does not mistake logical identification bounds for inferential intervals.

Keep these outcomes separate:
- evaluator_truth_within_bounds_rate: logical identification bounds contain independent truth;
- interval_coverage: direct inferential interval contains independent truth;
- interval_width: inferential interval width;
- interval_availability_rate: frequency with which an inferential interval is emitted.

A source-level reconstruction PASS is computational conformance, not evidence that nominal coverage has been achieved. Only calibration evidence can answer that.

## 4. Four objectives and minimum useful metrics

The existing 16-metric registry is broader than the minimum decision set. Keep the registry intact for now; designate a small primary subset and retain the rest as diagnostic/audit outputs.

| Objective | Primary metrics from the existing registry | Interpretation |
|---|---|---|
| Causal point recovery | point_bias, point_mae, point_rmse; point_recovery_rate only after a scientific tolerance is approved | Error against independent theta_A truth; no test-fixture tolerance is promoted |
| Interval calibration | interval_coverage, interval_availability_rate, interval_width | Coverage is interpreted jointly with availability and width |
| Monte Carlo precision | MCSE/precision targets for selected primary metrics, with nested M/R projections where applicable | Precision of simulated calibration summaries, not real-world sampling uncertainty |
| Identification/abstention | identification_rate, false_abstention_rate, correct_abstention_rate, wrong_cause_abstention_rate, false_identification_rate; partial_identification_rate as diagnostic | Distinguishes correct identification from appropriate and inappropriate abstention |

Evaluator audit metrics remain necessary integrity checks, but should not multiply primary acceptance criteria unnecessarily.

Retain the existing five candidate scenarios:
- positive truth (+0.5);
- null truth (0);
- negative truth (−0.5);
- alternative active pathway with focal truth 0;
- target-history support failure, expected NOT_IDENTIFIED.

Do not add scenarios in this review. The alternative zero-truth case is not interchangeable with the null case: it exercises a different active pathway. The current roster does not separately establish calibration for a truth class of PARTIALLY_IDENTIFIED or INDETERMINATE. Their observed rates can be reported diagnostically, but no broader claim should be made.

**Type-I error and power remain undefined.** A null-truth scenario and an interval-coverage calculation do not, by themselves, define a hypothesis test, type-I error or power. Do not add these metrics until a separate test procedure is specified.

## 5. Denominators and abstention: decision required before calibration

The current aggregator is fail-closed:
- interval coverage/width for an identified scenario are NOT_EVALUABLE if any planned R replicate lacks an inferential interval;
- point bias/MAE/RMSE/recovery are NOT_EVALUABLE for an M-world if any R replicate is not identified;
- availability and false-abstention rates are still recorded over all planned R.

This prevents silent complete-case deletion, which is correct. It also means one abstention can make a whole M contribution unavailable for coverage or point-error aggregation.

Before freezing the calibration acceptance manifest, confirm whether to retain this strict all-R evaluability rule as the primary rule. If conditional coverage among emitted intervals is ever reported diagnostically, it must be labelled conditional, include its emitted denominator, and always be paired with all-R availability. It must not replace the strict primary rule or conceal abstention. Any point-error diagnostic among identified outputs must likewise be labelled conditional and shown alongside all-R identification/false-abstention rates.

Do not silently relax the current denominator rules in code. This is a statistical estimand/acceptance decision, not an implementation convenience.

## 6. N, M and R: meaning and economical calibration

The direct protocol's dimensions are:

- N: experimental units (UEs) in each generated world.
- M: independent outer synthetic worlds.
- R: repeated randomized direct-g_A assignments within each fixed outer world.

The seed-bank implementation fixes world identity/seed across R, while each R receives a distinct assignment randomization salt and a distinct S3 seed. Thus R currently represents a repeat of the complete assignment-and-observation pipeline: it includes assignment randomness and fresh S3 observation randomness. This is appropriate for end-to-end calibration of measured V_cont and should be stated explicitly; it is not an assignment-only replication count.

Required decisions, without selecting numerical values here:

1. **N grid:** use only sizes feasible for the existing focal DGP and report all four objectives by scenario and N. Earlier Phase-A V_cont N constraints/defaults are not inherited automatically. Select the smallest tested N satisfying every predeclared primary precision/recovery criterion; if none qualifies, report no qualifying candidate rather than extrapolating.
2. **M:** define the target distribution of outer worlds and source-backed independence basis before declaring DECLARED_IID_PSEUDORANDOM. This is a modeling assumption about the synthetic world generator, not empirical proof of real-world independence. The nested precision module treats M<3 as insufficient outer support; M=2 is suitable only for smoke/contract checks, not a precision conclusion.
3. **R:** retain the current full-pipeline interpretation (fresh direct assignment and S3 observation stream per R). Choose R only after a small calibration sample estimates within-world variability and the nested design's precision contribution.
4. **Nested MCSE:** reconcile the aggregator's across-M MCSE with the separate nested M/R projection module. They answer related but different questions (observed precision at the current design versus projected precision at candidate M/R). The prospective manifest must say which result governs each target; do not count both as independent acceptance evidence.
5. **Within-world sampling declaration:** theta_a_nested_mc_precision.py requires an explicit within-world sampling mode for inferential projections, but ThetaACalibrationDesign currently versions the outer-world sampling contract only. Before claiming nested R-based MCSE, bind R assignment/S3 sampling assumptions to existing randomization and seed contracts, or leave the projection descriptive. Do not infer IID merely from distinct seeds.

Use staged calibration: first a small, bounded development sample to estimate variability and detect obvious coverage/availability failures; then expand only dimensions that materially affect the primary criteria. Keep the development bank separate from the untouched evaluation bank. Never use the evaluation bank to tune N, M, R, tolerances, confidence level or thresholds.

## 7. Confidence, MCSE and acceptance thresholds

The design requires an explicit confidence level and supports a versioned metric-target manifest, but it does not select scientific values. The test fixture's 0.95 confidence level and 0.05 point-recovery tolerance are not scientific decisions.

Before calibration, freeze only the minimum required values:
- inferential confidence level;
- point-recovery tolerance, if a binary recovery-rate criterion is wanted;
- MCSE target for each primary metric/scenario/N where a precision verdict is required;
- acceptable coverage range and availability floor;
- any width/informativeness criterion needed to prevent trivially wide intervals from passing on coverage alone;
- development stopping rule and maximum run budget/time.

Justify targets from intended precision and the bounded estimand, not convenience, F5 thresholds or defaults. Do not import the F5 93–97% band, Wilson rule or 95% emission threshold without a separate theta_A justification.

The calibration summary's PASS_PRECISION means only that observed MCSE meets the supplied target under the declared outer-world IID assumption. It does not certify interval coverage, causal identification or external validity.

## 8. Minimal next operation

One focused design reconciliation, not more implementation:

1. confirm the all-R denominator/evaluability rule and paired reporting of availability;
2. bind the within-R sampling declaration to the existing assignment/S3 randomization contract;
3. specify the primary metric subset and which MCSE result governs each target;
4. prepare a small, bounded development N/M/R proposal and execution budget only after the above;
5. freeze confidence, coverage, availability, width and MCSE acceptance criteria before any calibration execution;
6. keep the independent evaluation bank disjoint and unopened until calibration design and selection rules are frozen.

No N, M, R, confidence level, tolerance, MCSE target, coverage band, availability floor, width limit, power or type-I error value is selected by this report.

## 9. Governance and execution boundary

Static design review only. No implementation changes, tests, seed-bank generation, calibration, simulation, workflow dispatch or scientific execution are authorized. No change to estimand, DGP, Analyzer, Evaluator, M1, C0/C5, C10 scientific status, main or governance authorization.

scientific_execution=false  
execution_authorized=false
