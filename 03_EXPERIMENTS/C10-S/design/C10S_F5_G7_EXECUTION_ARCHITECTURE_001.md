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
- Candidate shard sizes are 25, 40, 50 and 100 datasets. The selected size is the largest candidate whose conservative p99 shard estimate is at most 150 minutes, after accounting for fixed runner setup overhead.
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
