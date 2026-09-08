# RUST-DYN-2 — EXEC-1A Replay Consistency Closure v0.1

**Status:** CLOSED — DETERMINISTIC REPLAY CONSISTENCY PASS
**Date:** 2026-09-08
**Scope:** EXT-1.1 Rust / RUST-DYN-2 / EXEC-1A
**Authorization:** DR-043

## 1. Replay result

The mandatory replay was executed with the same authorized command, dataset, executor, R*, temporal rule and horizon as the primary run.

The replay returned the same structured result as the primary execution across all supplied result fields.

## 2. Exact consistency observed

Primary and replay both report:

- dataset SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- R* Git blob SHA: `669d4f01131af518f32b1b4b3da27f676ae4ae55`
- temporal rule: `DR-035-v0.1-ADJACENT-CREATED-AT`
- horizon: `1`
- eligible origins: `607498`
- excluded origins due to ties: `0`
- temporal pairs: `516061`
- zero-pair packages: `30713`
- classification counts: PERSISTENCE `77858`, EXPANSION `8295`, CONTRACTION `3786`, RECONFIGURATION `426122`
- ND-1: `159921`
- ND-2: `278282`
- ND-4: `266201`
- pair evidence SHA-256: `fdab99039990d0e0a5ab221e6b98e857349048e8a26bf3f6a7ffe6fcd179bad8`
- platform: `Windows-11-10.0.26200-SP0`
- Python: `3.14.7`
- all firewall flags: `false`

The three supplied witnesses (ND-1, ND-2, ND-4) are identical between primary and replay in the received outputs, including origin identifiers and canonical T_acc / Reach membership data.

## 3. Consistency assessment

The primary and replay outputs are **field-identical as supplied through the coordination surface**. This establishes deterministic replay consistency for the received structured result.

A byte-level comparison of two independently captured result files is not claimed here because the raw primary/replay JSON files were not independently provided as file artifacts in this coordination step.

## 4. Closure decision

The mandatory replay requirement of DR-043 is satisfied on the evidence received. No exploratory rerun or parameter variation was performed.

The execution layer can now be considered technically closed, subject to recording the final scientific integration decision.

## 5. Scientific boundary

The result remains bounded to the frozen Rust operationalization at H=1. It does not establish universal TGCV validity, causality, predictive superiority, positive value implication, or originality.

## 6. Next operation

Record the final scientific integration/closure decision for RUST-DYN-2, including the precise empirical claims supported by the primary + replay evidence and the remaining open hypotheses.
