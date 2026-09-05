# N-R4B.3 — Controlled Trajectory/Outcome Corpus Conformance Gate Result v0.1

**Date:** 2026-09-05
**Status:** PASS / CLOSED
**Runner:** `N_R4B3_CORPUS_CONFORMANCE_RUNNER_v0.1`
**Implementation:** `03_EXPERIMENTS/EMP-1.1/src/branch_n_r4b3_corpus_v01.py`
**Implementation runtime SHA-256:** `41c3109d275ffe5574e9048d90e4305ad13686ecb79ebb2bac703061f29ca7a6`
**Smoke corpus:** 64 train + 64 test

## Decision

N-R4B.3 conformance **PASS / CLOSED**.

All registered conformance checks executed against the smoke-scale controlled corpus passed. The corrected dependency-loading implementation was exercised successfully, including snapshot and trajectory deterministic byte identity.

## Passed checks

- registered counts and seeds: PASS
- snapshot schema: PASS
- snapshot domain integrity: PASS
- canonical episode ordering: PASS
- same-seed snapshot byte identity: PASS
- same-seed trajectory byte identity: PASS
- train/test seed separation: PASS
- trajectory integrity: PASS
- trajectory schema: PASS
- initial snapshot hash consistency: PASS
- no learner or network dependency: PASS
- historical boundary: PASS

## Scientific-execution boundary

The following were explicitly **NOT PERFORMED**:

- full 30,000-train / 10,000-test corpus generation
- learner execution
- confirmatory inference

Therefore this gate establishes **implementation/conformance**, not a scientific result and not historical recovery.

## Interpretation

N-R4B.3 is authorized to proceed to controlled full-corpus generation under the frozen N-R4B.3 specification. The generated corpus must remain prospective controlled reconstruction data and must not be described as recovered historical EMP-1.1/MVE-1.0 data.

No historical result may be used as a tuning target.

## Next authorized step

Generate the registered controlled corpus:

- train: 30,000 episodes, seed `3,100,000`
- test: 10,000 episodes, seed `4,100,000`

Before any learner fitting or confirmatory inference, freeze the generated corpus, provenance, hashes, and predictor/outcome separation artifacts.
