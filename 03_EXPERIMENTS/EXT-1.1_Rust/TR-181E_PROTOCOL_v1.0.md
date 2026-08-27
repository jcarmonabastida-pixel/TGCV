# TGCV — TR-181E Protocol v1.0

**Status:** DRAFT — PENDING INTEGRITY REVIEW AND FREEZE
**Date:** 2026-08-27

## 1. Purpose

TR-181E is an independent predictive/stability pilot following the frozen TGCV-EMP-1.1 experiment. It is not a re-optimization of TGCV and does not modify the Core or the frozen operationalisation.

Primary question:

> Does the frozen TGCV representation `R` reproduce incremental out-of-sample predictive utility beyond the conventional baseline `B` under an independently generated pilot dataset and a pre-specified analysis pipeline?

## 2. Scientific invariants

The following are immutable during TR-181E:

- ontological Core `S`;
- `T_acc = F(S,C,L)`;
- phenomenon `Delta T_acc`;
- consequence `Delta Reach -> Delta Trajectory`;
- interaction `I` remains a mechanism, not a primitive;
- frozen MVE-1.0 operationalisation;
- frozen definition of `R`;
- outcome definition and eligibility rules once certified.

## 3. Relationship to EMP-1.1

EMP-1.1 remains a closed historical experiment. Its pilot established the historical confirmatory threshold `delta = 0.04`, and its confirmatory test produced a PRIMARY TEST PASS. These facts are not re-estimated or altered by TR-181E.

TR-181E therefore has a replication/stability role. It must not select a new `R`, tune the Core, or search for a result exceeding the historical effect.

## 4. Pilot data generation

The pilot dataset shall be generated independently from the sealed EMP-1.1 confirmatory dataset. No confirmatory EXT-1.1 dataset may be opened, inspected, fitted, or used for pilot tuning.

The exact generation seed, episode count, generator version, provenance, and integrity hash shall be recorded before execution.

If a genuinely independent empirical dataset is used instead of synthetic generation, its provenance, eligibility, access conditions, privacy/identifiability audit, and integrity metadata must be recorded before processing.

## 5. Representation and models

The frozen `R` from EMP-1.1 is used without post-hoc modification. The conventional baseline `B` and the TGCV arm use the same model family and pre-specified training procedure, subject only to parameters explicitly fixed before execution.

No component of `R` may be retained, removed, reweighted, or selected on the basis of TR-181E results.

## 6. Evaluation

Primary metric:

- paired out-of-sample LogLoss improvement `Delta LogLoss = LogLoss(B) - LogLoss(R)`.

Secondary metrics:

- AUROC;
- AUPRC;
- Brier score / calibration;
- stability across pre-specified splits;
- structural and null/permutation controls.

The analysis must remain out-of-sample and leakage-controlled.

## 7. Effect-size and sample-size reporting

`delta = 0.04` is retained as the historical EMP-1.1 threshold. TR-181E reports the observed effect, uncertainty, distribution across pre-specified resamples/splits, and any resulting planning information for a future external replication.

No post-hoc threshold will be substituted because it produces a more favorable interpretation.

If sample-size planning is performed, the assumed effect, variance estimate, target power, alpha, sidedness, and planning rule must be stated explicitly and frozen before being used for EXT-1.1.

## 8. Controls

At minimum, the pilot shall preserve the conceptual controls established in EMP-1.1:

- conventional baseline `B`;
- count-only representation control;
- permuted/null representation control;
- alternative fixed learner where computationally feasible;
- structural controls where applicable.

Controls are diagnostic and cannot be selectively omitted after results are observed.

## 9. Statistical discipline

The primary comparison, resampling/split scheme, random seeds, model family, hyperparameters, stopping rule, missing-data handling, and reporting format must be fixed before execution.

If paired sign-flip testing is retained, the number of permutations and exact pairing rule must be fixed before execution.

No early stopping for significance is permitted.

## 10. Decision logic

TR-181E is not itself the final falsification/confirmation of TGCV. Its outputs are:

1. reproducibility estimate;
2. uncertainty estimate;
3. stability assessment;
4. control behavior;
5. planning information for external replication.

A weak or null result must be reported as such and must not trigger retrospective modification of TGCV.

## 11. Freeze gate

Before execution, the following must be certified:

- [ ] exact `R` definition recovered and verified against EMP-1.1;
- [ ] MVE-1.0 implementation identified;
- [ ] pilot dataset generation/provenance fixed;
- [ ] independent-data boundary verified;
- [ ] sample size fixed;
- [ ] seeds fixed;
- [ ] model and hyperparameters fixed;
- [ ] primary/secondary metrics fixed;
- [ ] controls fixed;
- [ ] statistical procedure fixed;
- [ ] reporting template fixed;
- [ ] confirmatory EXT-1.1 dataset remains unopened;
- [ ] protocol hash recorded;
- [ ] formal TR-181E freeze issued.

**Execution status: BLOCKED until all freeze-gate items are certified.**
