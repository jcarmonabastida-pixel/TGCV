# C10-S F5 G7 — staged and resumable execution architecture

**Record:** C10S-F5-G7-EXECUTION-ARCHITECTURE-001  
**Version:** 1.0  
**Status:** RESEARCH IMPLEMENTATION DRAFT — NOT AUTHORIZATION TO RUN HOLDOUT  
**Scientific protocol:** C10S-F5-G7-TIERA-PROSPECTIVE-001 v1.0 (unchanged)  
**Branch:** `research/c10s-f1-integrated-correction-20261119`

## 1. Purpose and non-change boundary

This document changes only execution topology, checkpointing, resource accounting and recovery. It does not change the G7 scientific estimands, target cells, K=1,000 per cell, C0/C5 B=1,000, seed schedule/namespaces, method roster, primary/replay identity requirement, interval-emission threshold, coverage bounds, Wilson rule, no-pooling rule or failure dispositions.

The resource-only preflight is not a holdout and does not perform coverage adjudication. It must never be mixed into the primary/replay denominators.

## 2. Performance evidence

The exact-certificate arithmetic optimization at commit `5d3174de14fe9f5a5a19ddc5a97a44d7a7da88d8` reduced the same resource-only M30/R20 dataset comparison from 164.601 s to 24.676 s (6.67×), with the same resource seed, K=1, B=1,000 and `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED` outcome. Governed F5 tests passed on runs 44925771538 and 44926090717.

A larger resource-only sample is running as GitHub Actions run 44926453920, from source commit `469ecdd6f17639d10b9142158c527727e9add303`. It uses K=100 per cell, C0/C5 B=1,000, the disjoint resource namespace, per-dataset latency capture and no coverage adjudication. Its final artifact ID, archive digest, JSON digest, p95/p99 and shard recommendation are to be appended after completion. No primary or replay holdout data is involved.

## 3. Required execution graph

The former single sequential job (preflight → complete primary → complete replay) is replaced by distinct jobs with explicit dependencies:

1. **Authorization:** validate one-use approval, exact code parent, source hashes and frozen G7 protocol.
2. **Preflight evidence validation:** load the already completed resource-profile artifact; verify its digest, source-compatibility fingerprint, cell roster, K/B, namespace and `coverage_adjudication=NOT_PERFORMED`. Do not recompute the preflight when downstream jobs are retried.
3. **Primary matrix:** execute each frozen cell as independent global replicate-index shards. Each shard writes one immutable JSON artifact with a full record digest and exact seed/index manifest. No shard-level coverage adjudication.
4. **Replay matrix:** start only after every primary shard is complete and integrity-valid. Re-execute the same global replicate ranges from the clean approved source and same holdout seed schedule. Upload replay artifacts separately.
5. **Final aggregation:** verify complete, gap-free and non-overlapping coverage of indices 0–999 for each cell; verify seeds, method roster, dataset/truth pairing, row digests and primary/replay shard equality; rehydrate records and invoke the existing `adjudicate_matched_datasets` exactly once on the full K=1,000 denominator per cell; then apply the unchanged G7 adjudicator.

## 4. Shard sizing and execution ceiling

- Per-job target: at most 150 minutes at the measured p99 dataset latency.
- Per-job hard workflow timeout: 165 minutes.
- Maximum matrix parallelism: 20 jobs; this is a ceiling, not a promise of available hosted-runner capacity.
- Candidate shard sizes are 25, 40, 50 and 100 datasets. A candidate is safe only when its worst-observed shard estimate plus 5 minutes of fixed runner setup overhead is at most 150 minutes. Among safe candidates, select the one with the lowest conservative end-to-end wall-time estimate.
- If no candidate satisfies the ceiling, the preflight stage fails closed. No holdout shard starts.
- Report both aggregate runner-compute hours and estimated wall-clock time at the configured parallelism. Never present one as the other.

## 5. Recovery and no-repeat guarantee

Each primary/replay shard is a separate job and artifact. A transient failure must be retried only for the failed shard. Successful preflight, primary and replay artifacts remain intact within the workflow run. A later failure must not trigger regeneration of completed datasets. A replay mismatch is an integrity failure and blocks adjudication; it is not repaired by silently replacing one side.

The preflight artifact is immutable and reused for the exact source-compatible execution snapshot. Any change to a performance-critical fitting/certificate/engine/fixture/dependency input invalidates its compatibility and requires a new resource-only profile before holdout authorization. Changes confined to orchestration/shard bookkeeping are covered by explicit equivalence tests against the original `run_cell` output.

## 6. Integrity schemas

- Per-shard record schema: `TGCV-C10S-F5-G7-SHARD-001`.
- Full result schema: `TGCV-C10S-F5-G7-RESULT-002`.
- Full manifest schema: `TGCV-C10S-F5-G7-MANIFEST-002`.
- Shard record digest is SHA-256 over canonical sorted-key JSON of the complete record list.
- The full-bank primary/replay digest is computed only after the exact same ordered records and adjudicated metrics have been reconstructed for both phases.

## 7. Scientific blocker remains separate

The M10/R5 resource evidence previously showed only 67/100 global interior certificates, 19 certified boundary suprema and 14 unresolved global orderings. This is not a coverage estimate, but it indicates that current C5 interval emission may be below the frozen 95% minimum. The staged execution architecture does not fix or conceal that issue. No boundary case may be relabelled as interior, no abstention may be dropped, and no G7 threshold may be lowered.

## 8. Authorization status

The earlier one-use G7 authorization is consumed and bound to the monolithic executor. This staged executor requires a fresh hash-bound authorization on a dedicated authorization branch. This document, the shard executor, aggregator, tests, profile evidence and new workflow must be included in that hash set. This draft does not authorize generation of holdout datasets.


## 9. Measured resource profile and selected shard plan — run 44926453920

The 100-dataset-per-cell resource-only preflight completed successfully in 2,469.19 s wall time (41.15 min) and 2,636.46 s process CPU. The artifact is `c10s-f5-g7-resource-parallel-profile-469ecdd6f17639d10b9142158c527727e9add303`, artifact ID `14717426261`, archive SHA-256 `90399529105bffbe50205a68fd7bad30809c3d328a8172a331740f1b417d71a4`. Source commit: `469ecdd6f17639d10b9142158c527727e9add303`.

Observed per-dataset latency:
- M10/R5: mean 0.444 s, p95 0.864 s, p99 0.961 s, max 1.005 s.
- M30/R20: mean 24.246 s, p95 36.014 s, p99 40.423 s, max 42.551 s.

The candidate comparison is based on the **holdout denominator K=1,000**, not the K=100 resource-profile sample. The optimal plan is **50 datasets per shard**, 20 jobs per cell and 40 jobs per phase, with `max-parallel=20`. Including 5 minutes setup per shard, worst-observed shard estimates are 40.46 min for M30/R20 and 5.84 min for M10/R5. The conservative serialized-by-cell upper bound is 46.30 min per phase, 92.59 min for primary plus replay, and 133.75 min (2.23 h) including the one-time 41.15-minute resource preflight. Estimated aggregate primary-plus-replay runner compute remains 13.72 hours; the distinction between compute-hours and wall time is retained.

This projection assumes up to 20 concurrently scheduled GitHub jobs. If the repository's actual concurrency allowance is lower, wall time increases, but every shard remains independently below the 150-minute work budget and 165-minute hard timeout. The resource preflight is reused from its immutable artifact; it is not repeated by primary/replay retries.

The same resource profile also confirms the separate M10/R5 scientific emission blocker: 67/100 interior certificates and emitted intervals, 18 boundary suprema, 14 unresolved global orderings and one missing certificate status. These are resource-sample diagnostics, not coverage estimates. The staged executor does not change this distribution or lower the 95% G7 emission criterion.


### Planner correction — 2026-11-22

The resource-plan regression now asserts the true minimum among candidate sizes (25, 40, 50, 100). The former test expected 50 despite the candidate projection making 25 faster. The corrected deterministic plan is 25 datasets/shard, 8 shard jobs per phase, 20-way concurrency ceiling, 56.30 minutes conservative primary+replay wall time and 97.45 minutes including the one-time resource profile. This is a planning correction only: no G7 holdout data, seeds, estimands, thresholds or adjudication rules change.


### Denominator clarification — 2026-11-22

The planner uses the frozen holdout denominator `g7.K_PER_CELL=1,000` to calculate shard count and phase waves. The resource profile's `K_per_cell=100` is used only to estimate per-dataset latency and must not be substituted for the holdout denominator. With K=1,000, 25-row shards require 40 shards per cell and two waves per cell; 50-row shards require 20 shards per cell and one wave per cell. The latter minimizes the conservative serialized-by-cell primary/replay wall-time projection while every shard remains well below the 150-minute work budget. The prior 25-row note was an arithmetic interpretation error and is superseded.
