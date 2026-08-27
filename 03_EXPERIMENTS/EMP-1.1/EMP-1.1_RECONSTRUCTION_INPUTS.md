# EMP-1.1 Reconstruction Inputs

**Status:** SPECIFICATION RECOVERED — IMPLEMENTATION PENDING
**Date:** 2026-08-27

## Recovered frozen inputs

The Library contains the frozen EMP-1.1 protocol with the following executable-level parameters:

- representation-level hypothesis: `R` adds reproducible out-of-sample predictive utility beyond `B`;
- primary estimand: paired out-of-sample `Delta LogLoss = LL_B - LL_B+R`;
- alpha: `0.05`;
- historical confirmatory threshold: `delta = 0.04`;
- training episodes: `30,000`;
- locked test episodes: `10,000`;
- training seed: `3,100,000`;
- test seed: `4,100,000`;
- primary learner: `HistGradientBoostingClassifier`, identical fixed hyperparameters in both arms;
- sign-flip permutations: `200,000`, seed `13,579`;
- controls: count-only R, permuted-marginals R, RandomForest alternative;
- baseline B: component count + three resource values + objective identity;
- R: accessible-transformation structure derived at the frozen snapshot.

These parameters are directly supported by the frozen protocol artifact recovered from the Library. They are therefore labelled `SPECIFIED`, not `HISTORICAL CODE`.

## Still missing

The following executable details are not yet recovered from the available record and must not be invented:

1. exact six transformation-family definitions;
2. exact transition/update equations;
3. exact component/resource/objective value domains;
4. exact construction of the feature vector supplied to the learner;
5. exact fixed hyperparameter dictionary for HistGradientBoostingClassifier;
6. exact RandomForest configuration;
7. exact data-generation implementation;
8. exact pilot generation procedure and seed;
9. exact fold construction used in the 20,000-episode pilot;
10. any preprocessing/encoding details not explicit in the protocol.

## Reconstruction rule

A missing detail may be implemented only when it can be derived unambiguously from another frozen artifact. Otherwise it must be marked `RECONSTRUCTED` and separately justified, or remain `OPEN`.

The known result (`Delta=0.07942359585`) is an acceptance criterion after implementation, never a tuning target.

## Current gate

`SPECIFICATION_RECOVERED`

`IMPLEMENTATION_INCOMPLETE`

`EMP-1.1_REPRODUCIBILITY = NOT YET VERIFIED`
