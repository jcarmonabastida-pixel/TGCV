# N-R7 PREFLIGHT GATE RESULT v0.1

**Date:** 2026-09-05  
**Status:** PASS / CLOSED  
**Branch:** N — controlled prospective reconstruction  
**Scientific execution:** NOT PERFORMED

## 1. Decision

The N-R7 preflight/conformance check was executed as `N_R7_PREFLIGHT_RUNNER_v0.2` and returned **PASS** with no blocking checks.

This closes the **environment and execution-boundary preflight** only. It does not constitute learner execution, confirmatory inference, or scientific evidence.

## 2. Registered preflight result

All required checks passed:

- specification exists;
- learner implementation exists;
- frozen N-R5.3 predictor artifacts exist;
- frozen predictor hashes match exactly;
- frozen counts are train=30,000 and test=10,000;
- dimensions are B=16, R=58, BR=74;
- episode identifiers are canonical;
- BR is exact concatenation B||R;
- NumPy/scikit-learn APIs support the frozen configuration;
- exact HGB and RandomForest configurations instantiate;
- historical/network/trajectory firewall passes with no forbidden tokens;
- no top-level learner `.fit()` call is present;
- the permuted-marginals R control is fully frozen prospectively.

Environment reported by the run:

- Python 3.14.7, 64-bit Windows;
- NumPy 2.5.2;
- scikit-learn 1.9.0.

## 3. Permuted-marginals control

The preflight confirms the exact prospective control:

- scope: training R only;
- operation: independent column-wise permutation;
- seed: `24681357`.

The procedure is defined in N-R6.1 and is not a historical-code recovery claim.

## 4. Scientific firewall

The run explicitly reports:

- scientific execution: NOT_PERFORMED;
- learner execution: NOT_PERFORMED;
- confirmatory inference: NOT_PERFORMED;
- blocking checks: none.

No test result, historical result, trajectory, outcome, or external network state was consumed by the preflight.

## 5. Important provenance note

The learner implementation was corrected after an earlier preflight false positive. The previous `no_fit_at_import` failure was caused by source-text matching of a `.fit()` call inside a function rather than by an actual import-time fit. N-R7 runner v0.2 uses a top-level-fit check and returned `top_level_fit_lines: []`.

The N-R6.1 learner specification was also updated before this PASS to freeze the previously blocked permuted-marginals control prospectively.

Because the learner implementation and N-R6.1 specification changed after the earlier N-R6.2 conformance result, **N-R6.2 conformance must be rerun before scientific execution**. This is a provenance safeguard, not a scientific-data change.

## 6. Gate interpretation

**N-R7 PREFLIGHT: PASS / CLOSED.**

This authorizes preparation for the next conformance step but does not itself authorize scientific execution until the updated learner implementation/specification have passed N-R6.2 re-conformance.

## 7. Next authorized sequence

1. Re-run N-R6.2 learner conformance against the corrected learner and updated N-R6.1 specification.
2. Record the resulting implementation hash and close the updated N-R6.2 conformance gate.
3. If PASS/CLOSED, perform the first controlled N-R7 scientific learner execution exactly once.
4. Seal outputs and provenance.
5. Perform the independently repeated identical execution.
6. Only then interpret confirmatory statistics.

No historical EMP-1.1 executable recovery is claimed at any stage.
