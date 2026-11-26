# C10-S F5 / G7 Tier-A — readjudication result audit 001

**Status:** CLOSED — TECHNICAL ADJUDICATION COMPLETE / G7 NOT VALIDATED  
**Protocol:** `C10S-F5-G7-TIERA-PROSPECTIVE-001`, version 1.1  
**Authorization:** `C10S-F5-G7-20261126-006`  
**Scope:** instrumental F5 Tier-A calibration only; not the C10 causal experiment.

## 1. Purpose and provenance

This record documents the post-hoc final adjudication of the preserved primary and replay artifacts from the original authorized execution. It resolves the aggregator contract mismatch between resource-profile manifest schemas `002` and `003`. It does not rerun or regenerate any primary or replay shard.

| Item | Identity |
|---|---|
| Original primary/replay run | [45750949936](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45750949936) |
| Original run head / authorization commit | `091de2c0420b88653e643dd8d8272bdc0d73bbe4` |
| Approved execution code commit | `937ded9d0e431ad819a19a3e0209a922d61c2713` |
| Corrected aggregator commit | `4dea11cceef81b6a56c42c1075e00edadadb0cfc` |
| Readjudication workflow run | [45806714156](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45806714156) |
| Readjudication workflow commit | `974dd821d25e09e6fe443de6d01555b7430689b1` |
| Readjudication artifact | [Artifact 15110261521](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45806714156/artifacts/15110261521) |

The original authorization evidence records `g7_tiera_calibration_authorized=true`, `tier_b_authorized=false`, and `c10_scientific_execution_authorized=false`. The dispatch attestation binds the original user approval to run 45750949936 and the approved code commit above.

## 2. Integrity and replay audit

All technical readjudication gates completed successfully:

- Original run identity, event, attempt and source commit verified.
- Preserved primary inventory: **250/250 shard artifacts**.
- Preserved replay inventory: **250/250 shard artifacts**.
- Resource profile and `C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-003` verified.
- Profile JSON SHA-256: `005ef265fa7dd8812c2572d9187cc7943c365506dc8e1169f1883487c0094d9f`.
- Aggregator validated shard ranges, denominators, scientific record digests, diagnostic-sidecar digests and primary/replay record equality.
- Final run manifest contains 500 shard entries: 250 primary and 250 replay.
- The SHA-256 of `g7_result.json` matches `run_manifest.json.result_sha256`.

**Primary/replay digest:** `c5ad9cf4927172c939d54e7cf7ff72244b03d100d7631cd95d29b71698dd267c`  
**Final result SHA-256:** `b902985d494133b91034380f7182e1c4748f2f1b9d8a72488c574e2f90a062a0`  
**Readjudication ZIP SHA-256:** `f8e0c4b022e47d45b7ee66d22af74aa6a4a03fac8d8d7e46949a187dc2503e6a`

The workflow completed with GitHub Actions conclusion `success`. This is a technical execution status only; it is not the scientific G7 disposition.

## 3. Frozen scientific adjudication

The protocol requires all four C5 components (two targets × two cells) to pass independently, without pooling. Each cell has 1,000 datasets. A component passes only if conditional coverage is within [0.93, 0.97], its two-sided 95% Wilson interval contains 0.95, interval emission is at least 0.95, and the remaining frozen accounting/endpoint requirements hold.

| Cell | Target | Conditional coverage | 95% Wilson interval | Interval emission | Abstentions | Component |
|---|---|---:|---:|---:|---:|---|
| `F5_beta22_M10_R5` | within | 0.9864406779661017 | [0.9764499432608156, 0.9922267441906969] | 0.885 | 115 | FAIL |
| `F5_beta22_M10_R5` | between | 0.9966101694915255 | [0.9900812715766191, 0.9988464964487928] | 0.885 | 115 | FAIL |
| `F5_beta22_M30_R20` | within | 0.9425981873111783 | [0.9263523950664273, 0.9554327596560644] | 0.993 | 7 | PASS |
| `F5_beta22_M30_R20` | between | 0.9335347432024169 | [0.9163109315593505, 0.947417189278039] | 0.993 | 7 | FAIL |

### 3.1 Limiting evidence

- In `M10_R5`, 115/1,000 datasets abstained: 18 because the algebraic certificate was unavailable and 97 because a global boundary supremum was certified. The resulting 0.885 interval-emission rate is below the frozen 0.95 minimum for both targets. Conditional coverage is also above the frozen upper bound of 0.97 for both targets.
- In `M30_R20`, 7/1,000 datasets abstained because the algebraic certificate was unavailable. The within component meets all frozen criteria.
- In `M30_R20` between, conditional coverage is within [0.93, 0.97] and interval emission is above 0.95, but the Wilson interval upper bound (0.947417...) is below 0.95. The Wilson inclusion criterion therefore fails.

**Overall adjudication:** `NOT_VALIDATED`  
**Machine status:** `G7_NOT_VALIDATED_PRIMARY_REPLAY_EXACT_MATCH`

This is a valid negative/limiting calibration result under the frozen criteria, not an indeterminate execution. The exact primary/replay match supports computational reproducibility of the observed result; it does not convert the failed C5 criteria into a PASS.

## 4. Scientific and authorization boundaries

- G7 Tier-A is **not validated**. Tier-B remains unauthorized.
- This is an instrumental F5 calibration result, not evidence for or against the causal contribution `ΔT_acc → Value`.
- No C10 scientific execution was authorized or performed.
- No protocol threshold, estimator, interval construction, DGP, target cell, seed schedule, denominator or adjudication rule was changed to fit the result.
- The consumed G7 bank must not be used for post-hoc retuning. Any future development/calibration must use a separately governed, independent development basis and a new explicit authorization where required.
- No automatic change to TGCV Core, C10 claim status, RMA, Evidence→Claim Matrix or canonical `STATUS.md` follows from this result.

## 5. Reuse and retention

The primary and replay shards were reused from run 45750949936. No shard was rerun, no new authorization was consumed, and the original authorization remains historical evidence only. The readjudication artifact is retained by GitHub Actions for 90 days under artifact ID 15110261521.

The governing protocol remains unchanged: `03_EXPERIMENTS/C10-S/design/C10S_F5_G7_TIERA_PROSPECTIVE_PROTOCOL_002.md`.
