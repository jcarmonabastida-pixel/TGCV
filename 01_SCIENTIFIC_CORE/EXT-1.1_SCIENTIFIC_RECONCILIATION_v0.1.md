# EXT-1.1 Scientific Reconciliation v0.1

**Status:** CURRENT SCIENTIFIC RECONCILIATION — HISTORICAL DOCUMENTS PRESERVED
**Date:** 2026-09-07

## 1. Purpose

This document records the formal reconciliation between the closed EXT-1.1 Rust confirmatory execution and earlier post-EMP-1.1 scientific documents whose wording predates the confirmed execution result.

It is a correction of scientific-state documentation, not a re-analysis and not a new empirical execution.

## 2. Governing evidence

The confirmatory sequence was closed under `DR-027C_Rust_Confirmatory_Execution_Closure_v0.1.md` after primary/replay structural identity verification passed.

The frozen primary result was:

- `LogLoss(B) = 0.40512255638027656`
- `LogLoss(T_acc) = 0.41124528865339655`
- `ΔLogLoss = LogLoss(B) - LogLoss(T_acc) = -0.006122732273119991`
- `Brier(B) = 0.12862999557185928`
- `Brier(T_acc) = 0.13123035232566702`
- `AUC(B) = 0.7671989511641575`
- `AUC(T_acc) = 0.759314009238935`

Under DR-026C, positive `ΔLogLoss` favors `T_acc`. Therefore the observed negative value is descriptively unfavorable to the tested `T_acc` representation relative to `B` for `Y_180`.

Primary and replay reproduced these critical results exactly.

## 3. Documentation conflict identified

The following historical documents contain statements that are inconsistent with the confirmed EXT-1.1 result:

1. `01_SCIENTIFIC_CORE/TGCV_CORE_ONTOLOGY_POST_EMP11_v0.2.md`
2. `01_CORE/architecture/TGCV_CORE_v_current.md`

Specifically, earlier wording described the EMP-1.1 computational evidence as supporting predictive usefulness of the tested `T_acc` representation and characterized the accessibility hypothesis as empirically supported in the tested computational setting.

Those statements cannot remain the operative empirical interpretation after the closed EXT-1.1 confirmatory result.

## 4. Historical preservation rule

The historical documents named above MUST NOT be retroactively edited, deleted, or normalized merely to remove the discrepancy. Their prior wording is part of the research traceability record.

This reconciliation document establishes the current interpretation while preserving the historical state from which the discrepancy arose.

## 5. Current empirical interpretation

The correct current empirical statement is:

> Under the frozen EXT-1.1 Rust protocol, the tested operational representation of `T_acc` did not demonstrate incremental out-of-sample predictive utility over the frozen baseline representation `B` for the predefined outcome `Y_180`.

The negative result is descriptive and protocol-local. It does not establish that `T_acc` is universally irrelevant, that the TGCV theory is false, that accessibility has no causal or value relevance, or that the ontological core must be rejected.

No p-value, confidence interval, population-level effect, causal effect, or universal claim is authorized by EXT-1.1/DR-027C.

## 6. Separation from TGCV ontology

The EXT-1.1 result does not by itself alter the stabilized ontological core.

The current conceptual formulation remains:

- `Core_ontological = S`
- `T_acc = F(S,C,L)` as a derived analytical object
- `I` as explanatory mechanism/occasion rather than an ontological primitive
- central analytical phenomenon: change in accessible transformations, `ΔT_acc`
- analytical chain: `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

The empirical test evaluated one operationalization of `T_acc` against one predefined outcome and model protocol. Predictive utility for that task is not equivalent to ontological or descriptive validity of `T_acc` within TGCV.

## 7. Relation to TR-130 and DR-028

This reconciliation is consistent with TR-130's exclusion of `I` from the ontological core and with the current Core's distinction between ontology and empirical operationalization.

It also establishes the factual state required for review of `DR-028_Rust_Scientific_Interpretation_and_Next_Test_Gate_v0.1.md`.

DR-028 MUST be reviewed against this reconciliation before acceptance. No new execution is authorized by this document.

## 8. Temporal split discrepancy

A previously observed difference between the DR-026C audit boundary and the executed EXT-1.1 boundary is retained as a documentation/audit-reference discrepancy, not a scientific protocol change.

The executed runner formed the temporal partition over the DR-024 eligible population with complete 180-day follow-up. The executed boundary was:

`2020-09-21T15:56:13.527172+00:00`

with 280,760 train origins and 226,519 test origins.

The earlier DR-026C audit output used a different reference population when reporting its boundary. This does not alter the closed execution evidence and MUST NOT be retroactively rewritten into the execution artifacts.

## 9. Governance rule for subsequent scientific-state changes

Any substantive revision of the TGCV scientific state, Core, outcome, baseline, `T_acc` operationalization, model, inference procedure, or empirical claim MUST be versioned and governed explicitly. No post-hoc favorable-result adjustment is permitted.

Any future empirical test must have its own ex-ante design and execution gate.

## 10. Reconciliation conclusion

The apparent conflict is resolved by distinguishing:

1. **Historical pre-result wording:** preserved unchanged for traceability.
2. **Closed EXT-1.1 evidence:** negative descriptive result for the tested `T_acc` operationalization on `Y_180`.
3. **Current scientific interpretation:** no demonstrated incremental predictive utility in this test; no universal ontological conclusion.
4. **TGCV Core:** not falsified or revised by this result alone.

**RECONCILIATION STATUS: RECORDED. HISTORICAL DOCUMENTS PRESERVED. EXT-1.1 CURRENT EMPIRICAL INTERPRETATION ESTABLISHED.**
