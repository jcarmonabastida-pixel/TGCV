# TGCV-EMP-1.1 — Reconstruction Gate v0.2

**Status:** CLOSED — REPRODUCIBILITY BOUNDARY ESTABLISHED
**Date:** 2026-08-27

## 1. Decision

The historical executable implementation of MVE-1.0 has not been recovered. EMP-1.1 is therefore retained as the canonical explicit operationalisation used for the completed empirical test, but the repository does not claim independent bit-level re-executability of the historical run.

## 2. What is reproducibly preserved

The canonical record preserves the frozen experimental protocol, the sealed confirmatory dataset/result record, seeds and primary/secondary evaluation definitions to the extent explicitly recorded in the recovered artifacts.

## 3. What is not reproducibly established

The following remain unavailable at the required level of exactness:

- historical executable transformation-family predicates;
- exact transition implementation;
- exact accessibility implementation;
- exact R feature encoding/order;
- complete model hyperparameter configuration;
- complete historical generator implementation and environment.

## 4. Scientific consequence

The completed EMP-1.1 result remains valid as a documented result of the experiment as recorded. It must not be upgraded to a claim of independently reproduced computation from the present repository.

Conversely, the missing executable provenance does not justify changing TGCV Core, the recorded result, the decision rule, or the historical interpretation retrospectively.

## 5. TR-181E consequence

TR-181E may reuse the frozen conceptual and operational boundaries of EMP-1.1, but it must not be described as an exact replication of unavailable historical source code.

If exact executable replication is required, it constitutes a new reconstruction experiment and must be separately protocolled, with all reconstructed assumptions frozen before test data are evaluated.

## 6. Gate status

**EMP-1.1 scientific freeze:** PASS

**EMP-1.1 provenance documentation:** PASS

**Historical executable recovery:** FAIL / NOT RECOVERABLE

**Independent exact reproduction:** NOT CLAIMED

**Controlled reconstruction:** PERMITTED as a separate, explicitly labelled activity

**TR-181E:** UNBLOCKED only for protocol design; execution remains subject to its own pre-registration/freeze gate.

## 7. Integrity rule

No future document may silently convert `SPECIFIED` or `RECONSTRUCTED` artifacts into `HISTORICAL` artifacts. Provenance labels are part of the scientific record.

## 8. Next operational step

Move from archaeology to experiment design: finalize TR-181E as an independently specified stability/replication study, explicitly stating which elements are inherited from EMP-1.1 and which are newly reconstructed or independently generated.
