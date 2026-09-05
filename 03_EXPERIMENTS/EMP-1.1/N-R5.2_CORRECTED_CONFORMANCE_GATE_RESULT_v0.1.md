# N-R5.2 — CORRECTED CONFORMANCE GATE RESULT v0.1

**Status:** PASS / CLOSED  
**Date:** 2026-09-05  
**Runner:** N_R5_CONFORMANCE_RUNNER_v0.3  
**Scientific execution:** NOT PERFORMED

## Result

The corrected N-R5 predictor implementation passes all registered representation, traceability, semantic-state-hash, determinism, leakage, and dependency checks.

Implementation SHA-256 observed in the user execution:

`d26c89fc9e194149d9fc722aa012858b8d265787e9b422e85df20b12c37a15dd`

## Critical repair verified

`initial_snapshot_sha256` now identifies the semantic initial state S0 only. The hash excludes `episode_id`, excludes post-snapshot fields, uses sorted compact JSON, ASCII-safe content, and no terminal newline. This restores compatibility with the N-R4B.4 initial-state hash convention.

## Checks

All 18 checks reported PASS, including:

- B dimension 16;
- R dimension 58;
- B+R dimension 74;
- deterministic B layout and objective one-hot;
- direct B+R concatenation;
- episode identity does not alter S0 hash;
- no trajectory/outcome dependency;
- post-snapshot fields excluded from S0 hash;
- semantic state-hash bytes verified independently;
- episode_id excluded;
- newline excluded;
- no learner/network dependency;
- no historical result literal;
- no trajectory-generation dependency.

No scientific learner fitting, prediction, LogLoss calculation, or confirmatory inference was performed.

## Gate decision

**N-R5.2 CORRECTED CONFORMANCE: PASS / CLOSED.**

The next authorized action is controlled regeneration of the N-R5.3 predictor dataset from the unchanged frozen N-R4B.4 snapshot corpus. The previous N-R5.3 dataset is superseded for scientific use because its snapshot hashes were generated under the incompatible pre-repair convention.
