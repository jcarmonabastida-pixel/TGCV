# N-R7 Run 01 — First Scientific Execution Result Freeze v0.1

**Date:** 2026-09-05
**Status:** PASS / FIRST EXECUTION COMPLETED

## Execution status

`N_R7_PREFLIGHT_RUNNER_v0.2`: PASS with no blocking checks.

Scientific runner result: `PASS_FIRST_EXECUTION`.

The scientific runner completed learner execution, prediction generation, loss evaluation, controls, and confirmatory inference. This is therefore a scientific execution result, unlike the earlier pre-learner hash-mismatch abort.

## Primary result

| Metric | Value |
|---|---:|
| Base log loss | 0.36012118987132763 |
| TGCV log loss | 0.2301141852417799 |
| Delta log loss | 0.13000700462954773 |
| SD delta | 0.47085270367973225 |
| Paired sign-flip p | 0.0000049999750001249995 |
| Meets alpha | true |
| Meets practical delta | true |

The primary prospective Branch N execution therefore meets the frozen statistical and practical criteria.

## Controls

### Count-only control

- Base log loss: 0.36012118987132763
- TGCV log loss: 0.3621779296820455
- Delta: -0.00205673981071788
- SD delta: 0.09051619647443229
- Paired sign-flip p: 0.023114884425577874
- Meets alpha: true
- Meets practical delta: false

### Permuted-marginals control

- Base log loss: 0.36012118987132763
- TGCV log loss: 0.3647031200986736
- Delta: -0.0045819302273459326
- SD delta: 0.09495905720376517
- Paired sign-flip p: 0.0000049999750001249995
- Meets alpha: true
- Meets practical delta: false

### Random-forest control

- Base log loss: 0.7190042013442883
- TGCV log loss: 0.2949489000246411
- Delta: 0.42405530131964725
- SD delta: 3.4893385744014527
- Paired sign-flip p: 0.0000049999750001249995
- Meets alpha: true
- Meets practical delta: true

## Integrity identifiers

- Prediction SHA-256: `3c576ed6304baa2ef6acf8fc21d10db2e90d284ceba72563bfc3decf398e223f`
- Provenance SHA-256: `50de35232e3857a01392d0c24c53dec356d6e3be1f9b0509ecc2f7e9889a3abc`

## Interpretation boundary

This result is **prospective Branch N controlled-reconstruction evidence** under the frozen N-R4B.4, N-R5.3, N-R6 and N-R7 specifications.

It does **not** establish:

- historical EMP-1.1 reproduction or equivalence;
- universality of the TGCV representation;
- cross-domain validity;
- novelty of the underlying phenomenon;
- causal identification beyond the frozen experimental design;
- validation of TGCV as a general theory.

The count-only and permuted-marginals controls do not meet the practical-delta threshold, which is relevant to interpretation of the primary result. The random-forest control shows substantial predictive performance but is a model-control result and must not be conflated with the primary HGB specification.

No tuning against the Run 01 result is permitted.

## Gate decision

**PASS / FREEZE RUN 01 RESULT.**

Run 01 is sealed as the first completed prospective scientific execution. Any repeat must use the same frozen specifications and must be treated as an independent execution; Run 01 results may not be used to modify predictors, features, learner configuration, controls, thresholds, or inference procedures.
