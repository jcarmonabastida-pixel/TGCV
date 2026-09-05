# N-R7 Run 02 — Independent Repeat Authorization Gate Result v0.1

**Status:** PASS / CLOSED  
**Date:** 2026-09-05  

## 1. Decision

The N-R7 corrected preflight was rerun after sealing Run 01 and returned `status: PASS` with zero blocking checks.

**Run 02 independent repeat is AUTHORIZED.**

## 2. Verified frozen inputs

- Train predictor artifact SHA-256: `6559e31c7ef369c3d93f00d4c4dd0dfc481f7a001c4d89896994051872749bb9`
- Test predictor artifact SHA-256: `6c2bebff931aaeae4b542ef9846645c0d88b07c86ad6962d19c166ed0a59cd98`
- Train count: 30,000
- Test count: 10,000
- Predictor dimensions: B=16, R=58, BR=74
- NumPy: 2.5.2
- scikit-learn: 1.9.0
- Python: 3.14.7, 64-bit Windows
- Permuted-marginals seed: 24681357
- Historical-network/trajectory firewall: PASS
- No fit at import: PASS
- Exact learner configuration instantiation: PASS

## 3. Independence constraints

Run 02 must be executed without changing any frozen specification, dataset, learner configuration, control definition, seed, join key, or inference rule. Run 01 results must not be used for tuning, feature selection, threshold adjustment, model selection, or procedural modification.

The Run 01 artifact package remains sealed and is not an input to the prospective learner procedure.

## 4. Gate boundary

The preflight confirms readiness only. It does not constitute Run 02 execution and does not produce scientific results.

**Run 02 scientific execution: NOT YET PERFORMED.**

## 5. Next permitted action

Execute the already frozen N-R7 scientific runner once for the independent repeat. Do not modify the command, runner, or environment between this gate and execution.
