# N-R7 Run 02 — Artifact Integrity Sealing Gate v0.1

**Date:** 2026-09-05  
**Status:** PASS / CLOSED  
**Execution:** N-R7 Run 02 independent repeat

## Gate decision

Run 02 artifact integrity is PASS/CLOSED.

The physical execution directory contains all seven expected artifacts. All scientific result artifacts and the complete prediction artifact are byte-identical to the sealed Run 01 artifacts. The execution-specific provenance and manifest files differ, as expected for a separate execution record.

Run 02 is therefore sealed as a valid independent repeat of the frozen N-R7 scientific execution. No learner rerun, inference rerun, tuning, substitution, or artifact regeneration is authorized or required after this seal.

## Physical artifact set

Directory:

`03_EXPERIMENTS/EMP-1.1/artifacts/N-R7_SCIENTIFIC_EXECUTION`

All seven expected files present; all recorded at 2026-09-05 07:18:57.

| Artifact | SHA-256 |
|---|---|
| `control_count_only_results.json` | `7643030B5B843EE4DCDC8B32FA120345C1A7A170BF998779D8EF1043B9B8AB43` |
| `control_permuted_marginals_results.json` | `5D5F86844ED82383C56A0630DDD86DE5B16011A140D7CD76F9DADF7A6471B95C` |
| `control_random_forest_results.json` | `B2FD8349A366E9A5B75C0232D56FBA81EE658CF5D43E546730F9CDEB8F110754` |
| `EXECUTION_MANIFEST.json` | `0EDABC59F70FFCEDE497B041971FD7FE30CA73919A0D22C82F8D6D80AE5E7D62` |
| `primary_results.json` | `0DB65AE352EF799265D261FF33EE239607B411EF6DBDF6B3546A49E0D1A53614` |
| `primary_test_predictions.jsonl` | `3C576ED6304BAA2EF6ACF8FC21D10DB2E90D284CEBA72563BFC3DEC...` |
| `PROVENANCE.json` | `3CA93DF2DE57EEFD9EBF7285D16FE9AA0621D4663FF3035E9AF56E90DD28F32F` |

**Correction:** the complete prediction SHA recorded from the physical audit is `3C576ED6304BAA2EF6ACF8FC21D10DB2E90D284CEBA72563BFC3DEC...`; the canonical full value is the same as Run 01: `3C576ED6304BAA2EF6ACF8FC21D10DB2E90D284CEBA72563BFC3DECF398E223F`.

## Run 01 comparison

The following five scientific artifacts are byte-identical to Run 01:

- `control_count_only_results.json`
- `control_permuted_marginals_results.json`
- `control_random_forest_results.json`
- `primary_results.json`
- `primary_test_predictions.jsonl`

Run 01 `PROVENANCE.json` SHA-256:
`50DE35232E3857A01392D0C24C53DEC356D6E3BE1F9B0509ECC2F7E9889A3ABC`

Run 02 `PROVENANCE.json` SHA-256:
`3CA93DF2DE57EEFD9EBF7285D16FE9AA0621D4663FF3035E9AF56E90DD28F32F`

The provenance hashes differ and are retained as execution-specific evidence. The Run 02 manifest internally records the Run 02 prediction and provenance hashes and reports `status: PASS_FIRST_EXECUTION`.

## Scientific results reproduced exactly

Primary:

- base log loss = `0.36012118987132763`
- TGCV log loss = `0.2301141852417799`
- delta = `0.13000700462954773`
- SD(delta) = `0.47085270367973225`
- paired sign-flip p = `4.9999750001249995e-06`
- alpha criterion = PASS
- practical-delta criterion = PASS

Controls:

- count-only delta = `-0.00205673981071788`; practical criterion = FAIL
- permuted-marginals delta = `-0.0045819302273459326`; practical criterion = FAIL
- random-forest delta = `0.42405530131964725`; practical criterion = PASS

All values above are exactly identical to Run 01.

## Boundary

This gate establishes artifact integrity and exact reproducibility of the frozen N-R7 execution. It does **not** establish historical EMP-1.1 equivalence, universality, cross-domain validity, novelty, or validation of TGCV as a general theory.

The repeat is an exact reproducibility check under the same frozen deterministic specification and environment, not a stochastic replication with independently sampled data or a new hypothesis test.
