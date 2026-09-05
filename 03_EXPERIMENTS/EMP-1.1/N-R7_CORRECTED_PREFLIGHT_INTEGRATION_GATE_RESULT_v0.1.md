# N-R7 Corrected Preflight / Integration Gate — Result v0.1

**Date:** 2026-09-05
**Status:** PASS / CLOSED

## Scope

This gate records the corrected N-R7 preflight after updating the scientific execution runner to expect the frozen corrected N-R5.3 v0.2 predictor dataset hashes.

## Scientific runner correction

The scientific runner `03_EXPERIMENTS/EMP-1.1/tools/run_n_r7_scientific_execution_v01.py` was updated in commit `df07f284813bb0aee2be1efbde7f591ce93735e7`.

Correct frozen predictor hashes:

- Train: `6559e31c7ef369c3d93f00d4c4dd0dfc481f7a001c4d89896994051872749bb9`
- Test: `6c2bebff931aaeae4b542ef9846645c0d88b07c86ad6962d19c166ed0a59cd98`

## Observed preflight result

Runner: `N_R7_PREFLIGHT_RUNNER_v0.2`

All blocking checks returned `PASS` and `blocking_checks` was empty.

Validated:

- specification exists
- learner implementation exists
- frozen predictor artifacts exist
- corrected frozen predictor hashes
- train/test counts: 30,000 / 10,000
- dimensions B=16, R=58, BR=74
- canonical episode IDs
- BR concatenation
- NumPy 2.5.2 / scikit-learn 1.9.0 support
- exact learner configuration instantiation
- historical network/trajectory firewall
- no fit at import
- frozen permuted-marginals control

Scientific execution, learner execution, and confirmatory inference remained `NOT_PERFORMED` at preflight, as required.

## Decision

**PASS / CLOSED.**

The corrected N-R7 scientific execution runner and the frozen corrected N-R5.3 predictor artifacts are now integrated at the hash level. No scientific execution result is implied by this gate.

The next permitted action is the first N-R7 scientific execution. The resulting execution is prospective Branch N evidence only and must not be interpreted as historical EMP-1.1 reconstruction, universality, cross-domain validity, novelty, or TGCV validation.
