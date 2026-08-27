# TGCV — TR-181E Experimental Baseline v1.0

**Status:** RECONSTRUCTED — PENDING CERTIFICATION
**Date:** 2026-08-27
**Purpose:** pre-experimental baseline for the predictive pilot TR-181E. This document does not freeze the pilot and does not authorize execution by itself.

## 1. Scientific invariants

TR-181E must not modify the stabilized TGCV Core, the frozen MVE-1.0, or the ontological role of interaction.

Core representation:

- ontological primitive: `S`
- accessible transformations: `T_acc = F(S,C,L)`
- phenomenon: `Delta T_acc`
- downstream consequence: `Delta Reach -> Delta Trajectory`
- interaction `I`: mechanism, not primitive

## 2. Frozen operational baseline

The EMP-1.1 operationalisation is the baseline to be reused rather than retrospectively redesigned:

- potential components: `A1, A2, B1, B2, C1, C2`
- initial component count: 3–5
- six transformation families
- three discrete resources
- twelve objectives
- horizon `H=6`
- stochastic, objective-independent execution
- representation-level hypothesis: `R` adds reproducible out-of-sample predictive utility beyond conventional snapshot representation `B`
- null: `R` adds no incremental predictive utility beyond `B`

## 3. Pilot purpose

TR-181E is a predictive pilot, not the confirmatory experiment. Its purpose is to estimate effect size and uncertainty sufficiently to determine the confirmatory design inputs `delta`, `N*`, and `alpha` without opening or fitting the confirmatory dataset.

The pilot must assess:

- paired out-of-sample `Delta LogLoss`
- uncertainty / variability of the effect
- AUROC and AUPRC
- calibration / Brier score
- stability across pre-specified splits
- structural controls
- null / permutation controls

## 4. Anti-retrofitting rules

After the pilot begins, the following may not be changed in response to observed results:

1. TGCV Core
2. MVE-1.0
3. operational definition of `R`
4. outcome definition
5. eligibility rules
6. pre-specified model-selection rule
7. confirmatory dataset definition

No component of `R` may be selected because of pilot predictive performance unless that selection rule was specified before execution.

## 5. Confirmatory hand-off

TR-181E may recommend values/ranges for `delta`, `N*`, and `alpha`, but these become confirmatory inputs only after explicit review and a separate protocol freeze.

The confirmatory EXT-1.1 dataset must remain unopened until the confirmatory protocol is frozen.

## 6. Interpretation boundary

EMP-1.1 produced a PRIMARY TEST PASS for its frozen computational operationalisation. That result is not universal validation of TGCV and must not be used to modify the Core retrospectively.

TR-181E is therefore an independent design/estimation gate. It is not a second opportunity to optimize TGCV against an observed result.

## 7. Required certification checklist

Before execution, the following must be verified:

- [ ] exact executable definition of `R` recovered
- [ ] exact MVE-1.0 implementation/configuration identified
- [ ] pilot dataset generation and provenance identified
- [ ] train/test or resampling scheme fixed
- [ ] model and hyperparameters fixed
- [ ] primary and secondary metrics fixed
- [ ] control specifications fixed
- [ ] stopping rule fixed
- [ ] reporting template fixed
- [ ] confirmatory dataset remains unopened
- [ ] protocol hash recorded
- [ ] TR-181E freeze issued

**Decision state:** NOT YET FROZEN.
