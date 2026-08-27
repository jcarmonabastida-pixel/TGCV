# TR-181E — Predictive Pilot & Effect-Size Estimation

## Status

**NEXT RESEARCH OPERATION — not executed by this repository bootstrap.**

## Purpose

Estimate the empirical behaviour of the current operational representation without changing the stabilized Core or the frozen MVE-1.0. The pilot is explicitly exploratory and is not the confirmatory experiment.

## Inputs that are already fixed

- Core architecture: `S` as ontological Core.
- Analytical structure: `T_acc = F(S,C,L)`.
- Operational representation: `R` as defined by the current experimental design.
- MVE-1.0: frozen.
- Comparative logic: conventional representation versus the same representation plus `R`.
- Primary metric: probabilistic predictive performance, with LogLoss as the principal metric in the recovered design.
- Secondary metrics: AUROC, AUPRC and Brier Score.
- Leakage controls and out-of-sample discipline.

## Pilot objectives

Estimate:

- `ΔLogLoss`;
- `σ_Δ` / variability of the paired effect;
- predictive discrimination and calibration;
- stability across appropriate splits;
- behaviour of structural and cardinality controls;
- behaviour of null/permuted-structure controls.

The recovered protocol explicitly requires `δ`, `N*` and `α` to be determined from the pilot before the confirmatory dataset is opened. fileciteturn9file3

## Non-negotiable constraints

1. Do not modify MVE-1.0.
2. Do not modify the Core to accommodate pilot results.
3. Do not use the confirmatory dataset to tune the pilot.
4. Do not select `R` components retrospectively because they predict well.
5. Record data lineage for every predictor.
6. Keep future information and post-outcome information excluded.
7. Preserve all pilot configurations and results.

## Next gate

After the pilot, pre-specify the confirmatory effect threshold and sample size, freeze the Experimental Protocol v1.0, and only then proceed to confirmatory data access/execution.
