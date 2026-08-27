# TR-181E — Stability and Replication Protocol v1.1

**Status:** DRAFT — PRE-REGISTRATION CANDIDATE
**Date:** 2026-08-27

## 1. Purpose

TR-181E is an independent follow-up study designed to test whether the predictive signal observed in EMP-1.1 remains stable under a newly sealed experimental specification.

It is **not** a claim of exact reproduction of the unavailable historical MVE-1.0 executable implementation.

## 2. Scientific question

Does a representation containing accessible-transformation structure provide incremental out-of-sample predictive utility over the frozen conventional snapshot representation when evaluated under an independently sealed experiment?

## 3. Inheritance from EMP-1.1

TR-181E inherits only the following scientific boundaries:

- the TGCV Core ontological distinction between state and accessible transformations;
- the representation-level comparison between B and B+R;
- paired out-of-sample predictive evaluation;
- LogLoss as the primary metric;
- controls that test whether the signal is reducible to counts or arbitrary relational structure.

TR-181E does not inherit unknown executable implementation details as if they were historical facts.

## 4. Independence requirements

Before any test-set evaluation, the following must be frozen:

- exact R operationalisation;
- data-generation procedure;
- training/test split;
- seeds;
- model configurations;
- primary estimand;
- decision threshold;
- permutation procedure;
- control definitions;
- reproducibility tolerance.

No parameter may be selected by inspecting TR-181E test outcomes.

## 5. Provenance classes

Every TR-181E artifact must be marked `INHERITED`, `NEWLY_SPECIFIED`, `RECONSTRUCTED`, `DERIVED`, or `VERIFIED`.

## 6. Primary hypothesis

H1: B+R improves out-of-sample predictive performance relative to B by a pre-specified minimum effect.

H0: B+R provides no such incremental predictive utility.

The exact numerical effect threshold is **OPEN** until the protocol is fully justified and frozen; the EMP-1.1 observed effect must not be used to tune it.

## 7. Required controls

At minimum:

1. B only;
2. B + R;
3. B + count-only relational surrogate;
4. B + permuted relational surrogate;
5. an independently specified alternative learner.

## 8. Current gate

**DESIGN ACTIVE — NOT YET FROZEN FOR EXECUTION.**

The next gate is to specify the exact operationalisation of R and the independent data-generation/splitting scheme. Only after that gate passes may executable code and sealed test data be created.

## 9. Integrity rule

TR-181E must remain analytically downstream of EMP-1.1 without being retrofitted to reproduce its numerical result. A successful TR-181E result would constitute independent evidence of stability; a failure would be retained as evidence about the limits of the effect.
