# N-R7 Run 01 — Artifact Integrity / Sealing Gate Result v0.1

**Status:** PASS / CLOSED  
**Execution:** N-R7 Run 01 — First Scientific Execution  
**Date:** 2026-09-05  

## 1. Purpose

This gate records the post-execution integrity audit of the local artifact package produced by the first N-R7 scientific execution. It is a sealing gate only; it does not rerun the learner, alter results, or constitute a second scientific execution.

## 2. Artifact completeness

The expected seven Run 01 artifacts were confirmed present in:

`03_EXPERIMENTS/EMP-1.1/artifacts/N-R7_SCIENTIFIC_EXECUTION`

- `control_count_only_results.json`
- `control_permuted_marginals_results.json`
- `control_random_forest_results.json`
- `EXECUTION_MANIFEST.json`
- `primary_results.json`
- `primary_test_predictions.jsonl`
- `PROVENANCE.json`

## 3. SHA-256 integrity record

The following hashes were computed from the local Run 01 artifact files:

| Artifact | SHA-256 |
|---|---|
| `control_count_only_results.json` | `7643030B5B843EE4DCDC8B32FA120345C1A7A170BF998779D8EF1043B9B8AB43` |
| `control_permuted_marginals_results.json` | `5D5F86844ED82383C56A0630DDD86DE5B16011A140D7CD76F9DADF7A6471B95C` |
| `control_random_forest_results.json` | `B2FD8349A366E9A5B75C0232D56FBA81EE658CF5D43E546730F9CDEB8F110754` |
| `EXECUTION_MANIFEST.json` | `C82AB831ADD7B2B13087B171861C2F781808443AF3705FE1D26E09BB71809970` |
| `primary_results.json` | `0DB65AE352EF799265D261FF33EE239607B411EF6DBDF6B3546A49E0D1A53614` |
| `primary_test_predictions.jsonl` | `3C576ED6304BAA2EF6ACF8FC21D10DB2E90D284CEBA72563BFC3DECF398E223F` |
| `PROVENANCE.json` | `50DE35232E3857A01392D0C24C53DEC356D6E3BE1F9B0509ECC2F7E9889A3ABC` |

The `primary_test_predictions.jsonl` hash matches the `prediction_sha256` recorded by Run 01, and the `PROVENANCE.json` hash matches the `provenance_sha256` recorded by Run 01.

## 4. Gate decision

**PASS / CLOSED.** The Run 01 artifact package is considered cryptographically sealed for the purposes of subsequent analysis and repeat-execution governance.

No artifact has been modified, regenerated, or substituted as part of this gate.

## 5. Scientific boundary

This gate does not change the scientific interpretation already frozen in `N-R7_RUN01_FIRST_EXECUTION_RESULT_FREEZE_v0.1.md`.

Run 01 remains prospective controlled Branch N evidence. It is not evidence of historical Cargo equivalence, universality, cross-domain validity, novelty, causal identification beyond the registered design, or general validation of TGCV.

## 6. Run 02 authorization boundary

With this gate closed, the artifact-integrity prerequisite for a repeat execution is satisfied. **Run 02 is now permitted**, but must remain an independent repeat under the already frozen specifications, configurations, seeds, controls, and execution protocol. No Run 01 result may be used to tune or modify the prospective procedure before Run 02.
