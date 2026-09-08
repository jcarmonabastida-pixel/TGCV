# RUST-DYN-2 — EXEC-1A Primary Technical Result Review v0.1

**Status:** PRIMARY TECHNICAL PASS — REPLAY PENDING
**Date:** 2026-09-08
**Scope:** EXT-1.1 Rust / RUST-DYN-2 / EXEC-1A
**Authorization:** DR-043

## 1. Result receipt

The authorized primary real-dataset execution completed without a runtime stop condition and returned the structured `RUST_DYN_2_REAL_PRIMARY` result. The complete JSON result was supplied through the coordination surface immediately after the authorized execution.

The result is treated as primary execution evidence. No rerun was performed after receipt.

## 2. Frozen integrity facts

- Dataset SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- R* Git blob SHA: `669d4f01131af518f32b1b4b3da27f676ae4ae55`
- Temporal rule: `DR-035-v0.1-ADJACENT-CREATED-AT`
- Horizon: `1`
- Eligible origins: `607498`
- Timestamp-tie origins excluded: `0`
- Temporal pairs: `516061`
- Zero-pair packages: `30713`
- Execution authorization flag: `true`

## 3. Classification result

| Classification | Count |
|---|---:|
| PERSISTENCE | 77,858 |
| EXPANSION | 8,295 |
| CONTRACTION | 3,786 |
| RECONFIGURATION | 426,122 |
| **Total** | **516,061** |

Non-persistence count: `438,203 / 516,061` (approximately `84.91%`).

## 4. Downstream structural distinctions

- ND-1 — `ΔT_acc` without `ΔReach`: **159,921** pairs.
- ND-2 — `ΔT_acc` with `ΔReach`: **278,282** pairs.
- ND-4 — equal Reach cardinality with different Reach membership: **266,201** pairs.
- Pair evidence SHA-256: `fdab99039990d0e0a5ab221e6b98e857349048e8a26bf3f6a7ffe6fcd179bad8`

ND-1 + ND-2 = `438,203`, matching the observed non-persistence count and therefore the reported ΔT_acc-changing population.

## 5. Information firewall

All reported forbidden-access flags are `false`:

- sampling: false
- outcome read: false
- future activity read: false
- predictive metrics: false
- Cargo execution: false
- runtime outcomes: false
- lockfile read: false
- value read: false

## 6. Witness receipt

Canonical witnesses were returned for ND-1, ND-2 and ND-4. The supplied primary result includes exact origin identifiers and canonical T_acc / Reach membership evidence for each witness.

The ND-1 witness demonstrates a T_acc difference with equal Reach membership. The ND-2 witness demonstrates T_acc difference accompanied by Reach difference. The ND-4 witness demonstrates equal Reach cardinality with different Reach membership.

## 7. Technical assessment

The primary result is technically admissible under the DR-043 boundary as received:

1. frozen dataset identity matches;
2. frozen R* identity matches;
3. frozen temporal population is reported as 516,061 pairs with zero ties;
4. H=1 is preserved;
5. required classification counts are internally consistent with the pair count;
6. ND-1 and ND-2 sum to the reported non-persistence population;
7. ND-4 is reported independently;
8. the information firewall is closed;
9. execution authorization is explicitly true;
10. no outcome, predictive, value or runtime information is reported as accessed.

## 8. Scientific boundary

This review does **not** yet constitute scientific closure. The mandatory deterministic replay under DR-043 remains outstanding.

If replay reproduces the canonical result exactly, the combined primary/replay evidence may support bounded structural statements about ND-1, ND-2 and ND-4 under the frozen Rust operationalization.

No universal TGCV validation, causal claim, predictive-superiority claim, positive-value claim, or originality claim is inferred from the primary run.

## 9. Mandatory next operation

Execute exactly one deterministic replay using the same frozen dataset, executor, R*, temporal population, horizon and command authorized by DR-043.

No exploratory rerun, parameter change, sampling, filtering, alternative dataset, alternative executor or horizon change is authorized.
