# N-R7 — Epistemic Interpretation and Claim Boundary v0.1

**Status:** FROZEN / CLOSED
**Date:** 2026-09-05
**Branch:** N-R7 / EMP-1.1

## 1. Purpose

This document freezes the epistemic interpretation of the completed N-R7 controlled learner experiment. It does not modify, retune, regenerate, or reinterpret the sealed N-R7 executions. Its purpose is to establish the exact claim supported by the experiment and the claims that remain open.

## 2. Experimental question actually tested

N-R7 tests whether structural features derived from the accessible-transformation structure `T_acc` contain incremental predictive information about a future controlled outcome beyond the baseline representation `B`.

Operational comparison:

`P(Y | B, R)` versus `P(Y | B)`

where `B` is the frozen baseline representation and `R` is the frozen 58-dimensional representation of structural properties of `T_acc`.

This is a predictive-information question. It is not, by itself, a direct test of `mechanism -> ΔT_acc`, causal identification, value creation, historical Cargo equivalence, or cross-domain validity.

## 3. Frozen primary result

Run 01 and Run 02 produced exactly concordant scientific outputs under the same frozen data, specification, implementation, learner configuration, controls, seeds and execution conditions.

Primary:

- Base log loss: `0.36012118987132763`
- TGCV (`B+R`) log loss: `0.2301141852417799`
- Delta log loss: `+0.13000700462954773`
- SD of paired delta: `0.47085270367973225`
- Paired sign-flip p-value: `4.9999750001249995e-06`
- Alpha criterion: PASS
- Practical-delta criterion: PASS
- Test prediction SHA-256: `3C576ED6304BAA2EF6ACF8FC21D10DB2E90D284CEBA72563BFC3DEC F398E223F` (canonical value is recorded in the sealed execution artifacts without spaces)

The exact scientific outputs and artifact hashes are governed by the Run 01 and Run 02 sealing gates and the Run 01/Run 02 reproducibility concordance gate.

## 4. Control interpretation

### 4.1 Count-only control

The count-only representation produced:

- Delta log loss: `-0.00205673981071788`
- Practical criterion: FAIL
- Paired sign-flip p-value: `0.023114884425577874`

Interpretation: the observed primary signal is not adequately accounted for by the six family-cardinality variables alone.

### 4.2 Permuted-marginals control

The independently permuted marginal control produced:

- Delta log loss: `-0.0045819302276459326`
- Practical criterion: FAIL
- Paired sign-flip p-value: `4.9999750001249995e-06`

Interpretation: the result is compatible with information residing in joint structural organization rather than being recoverable from the isolated marginal distributions of the 58 `R` variables. This is evidence against a simple marginal-distribution explanation, not proof of a unique mechanism.

### 4.3 Random-forest control

The RF control produced:

- Delta log loss: `+0.42405530131964725`
- Practical criterion: PASS
- Paired sign-flip p-value: `4.9999750001249995e-06`

Interpretation: the predictive signal is not specific to the HGB learner family. This supports robustness of predictive information in the representation, while not establishing that any particular learner identifies the TGCV mechanism.

## 5. Claim authorized by N-R7

The following claim is authorized and frozen:

> **H1-N:** In the controlled Branch N domain, certain structural properties of the accessible-transformation structure `T_acc` contain incremental information for predicting future controlled outcomes beyond the frozen baseline state representation `B`.

A stronger equivalent formulation is permitted only with the qualification that this is a controlled-domain predictive result, not a causal or universal result.

## 6. Claims not authorized by N-R7

N-R7 does **not** establish any of the following:

1. That changes in `T_acc` causally produce future outcomes.
2. That the underlying mechanism has been identified causally.
3. That `T_acc` is the unique or necessary carrier of the observed signal.
4. That the signal generalizes outside the controlled Branch N generator/domain.
5. That the result constitutes cross-domain validation of TGCV.
6. That the result establishes universality or transversal validity of TGCV.
7. That the result establishes novelty of the TGCV theoretical construct.
8. That the result establishes historical equivalence to Cargo resolution or any external historical system.
9. That the result validates the complete TGCV chain from mechanism through `ΔT_acc`, trajectory and value.
10. That the result constitutes causal identification.
11. That the result constitutes new-data replication.

## 7. Alternative explanations still open

The following explanations remain scientifically live and must be treated as falsifiable alternatives in the next experimental block:

- **A — Genuine structural signal:** structural properties of `T_acc` contain predictive information relevant to future outcomes.
- **B — Generator artifact:** the signal is induced by the particular synthetic generator or its distribution.
- **C — Proxy explanation:** `R` captures latent properties of the generator or state that are predictive, without `T_acc` itself being explanatory.
- **D — Representation effect:** the observed improvement depends on the particular encoding of `T_acc`, rather than on the ontological object claimed by TGCV.

N-R7 does not adjudicate among A–D.

## 8. Relation to the TGCV theoretical sequence

The result is coherent with, but does not prove, the sequence established by prior gates:

`I ∉ Core` → `T_acc` is structural → accessibility is operationalizable non-circularly → structural `T_acc` is computationally representable → structural `T_acc` representation carries incremental predictive information.

This means the selected TGCV object is empirically non-empty in the controlled Branch N experiment. It does not mean that the full TGCV theory has been validated.

## 9. Governance consequence

The following items are frozen and must not be altered as a consequence of this interpretation:

- N-R4B.4 controlled outcome corpus
- N-R5.1 v0.2 predictor representation
- N-R5.3 v0.2 corrected predictor dataset
- N-R6 learner specification and controls
- N-R7 execution specification
- N-R7 Run 01 artifacts and sealing record
- N-R7 Run 02 artifacts and sealing record
- N-R7 Run 01/Run 02 reproducibility concordance

No feature selection, representation change, learner change, threshold change, seed change, data regeneration, or retrospective tuning is authorized on the basis of the N-R7 results.

## 10. Next scientific question

The next block must attack the surviving interpretation rather than repeat N-R7.

Primary question for N-R8:

> **Does the predictive signal attributed to structural properties of `T_acc` survive controlled attacks on generator dependence, proxy explanations, representation dependence, and structural confounding?**

The next permitted work is therefore design and pre-registration/freeze of **N-R8 Robustness & Mechanism Discrimination**, followed by its own conformance gates. No N-R8 execution is authorized by this document alone.

## 11. Final frozen interpretation

> **N-R7 provides favorable experimental evidence that a structural representation of accessible transformations contains incremental predictive information about future outcomes in a controlled synthetic domain. The signal is reproducible and is not adequately explained by family cardinality alone or by isolated marginal distributions of the structural features. However, the evidence does not yet identify causality, establish generality, demonstrate cross-domain validity, establish novelty or universality, or validate TGCV as a general theory.**

**Decision: PASS / INTERPRETATION FROZEN / N-R8 DESIGN AUTHORIZED.**
