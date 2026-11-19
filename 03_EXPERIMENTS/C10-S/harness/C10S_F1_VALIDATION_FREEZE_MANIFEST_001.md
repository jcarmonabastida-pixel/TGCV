# C10-S F1 — Integrated Validation Freeze Manifest 001

**Status:** FROZEN SOURCE SNAPSHOT — VALIDATION NOT AUTHORIZED  
**Freeze branch:** `research/c10s-f1-validation-freeze-20261119`  
**Frozen source commit:** `0d430adae891b3914475c60334d93e977efc44cc`  
**Parent workstream:** `research/c10s-nested-mr-calibration-design-20261119`  
**Scope:** deterministic F1 coefficient/root reconstruction, exact-rational Sturm isolation, F1/Sturm adjudication, and F1/F5 comparative-engine integration tests.  
**Non-scope:** C10 scientific execution, DGP experiment, Monte Carlo calibration, bootstrap method validation outside the listed test suite, inference claims, or scientific closure.

## 1. Freeze rule

The source snapshot is the exact Git commit above. Validation, if separately authorized, MUST check out this commit in detached mode and run only the command in the paired authorization draft. Do not run from a moving branch tip. Do not amend or replace the frozen source commit. Any code change requires a new freeze manifest and a new authorization tied to the successor commit.

This freeze identifies the implementation for validation; it does not certify correctness or authorize execution.

## 2. Frozen source inventory

The GitHub blob SHAs below are Git blob identities (not SHA-256 digests). They are pinned together with the frozen commit SHA.

| Role | Path | Git blob SHA |
|---|---|---|
| F1 solver and rational coefficient construction | `03_EXPERIMENTS/C10-S/harness/c10s_f1_between_profile_likelihood.py` | `b03697432fbcc0bacfc88f500c5003ac529448fb` |
| Independent exact-rational Sturm isolator | `03_EXPERIMENTS/C10-S/harness/c10s_f1_independent_root_isolator.py` | `3ac9ce31eb82421022fd8d2a65a0daee049322be` |
| F1/Sturm adjudicator | `03_EXPERIMENTS/C10-S/harness/c10s_f1_root_adjudication.py` | `9fa1cb21cd47e32030db8a00420e7dacfdc77321` |
| F1/F5 comparative inference engine | `03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_comparative_inference_engine.py` | `d277db712f8d2fdc7efbb5da5213d3087a84358a` |
| F1 solver tests | `03_EXPERIMENTS/C10-S/harness/test_c10s_f1_between_profile_likelihood.py` | `a012755a695eeefa03100ed8d4024de0c0bfb2f1` |
| Sturm isolator tests | `03_EXPERIMENTS/C10-S/harness/test_c10s_f1_independent_root_isolator.py` | `bb5cd2b8d2819fdb8757ea293d7e8f8fb9a1b4ce` |
| F1/Sturm adjudication tests | `03_EXPERIMENTS/C10-S/harness/test_c10s_f1_root_adjudication.py` | `2bcaed7423528fbbf9a6783c3f32e5edd30a10bc` |
| F1/F5 comparative engine tests | `03_EXPERIMENTS/C10-S/harness/test_c10s_nested_mr_comparative_inference_engine.py` | `1061998ba93f363fbaaaed050c67acd6eb1c45b5` |
| Integrated concordance design matrix | `03_EXPERIMENTS/C10-S/harness/C10S_F1_INTEGRATED_CONCORDANCE_MATRIX_DRAFT_001.md` | `2ee2b9dd20381c5f5ded18a57a3ac2b7f1e7fe92` |

The frozen commit was queried directly for every listed path; the returned blob SHAs match this inventory.

## 3. Runtime and preflight requirements

- Python baseline: 3.12.3 (verify actual interpreter before execution).
- Run from the harness directory after checking out the frozen commit.
- Verify all eight Python source/test files against the blob identities above.
- Verify imports/dependencies without modifying the environment or source.
- Capture complete stdout, stderr, exit code, interpreter version, platform, command, and the frozen commit SHA.
- Any missing dependency, hash mismatch, import failure, unexpected file modification, or mismatch against the frozen commit is a STOP condition.
- Do not install/upgrade dependencies during the authorized run. Resolve environment differences before requesting a new authorization if necessary.

## 4. Validation boundary

The suite is limited to the four listed deterministic test modules. It may exercise fixed fixtures and seeded operations explicitly encoded by those tests. It does not authorize a DGP experiment, outer Monte Carlo calibration, parameter calibration, new data generation, broad repository test runs, or scientific interpretation beyond the technical behavior asserted by the tests.

## 5. Evidence interpretation

A successful test-suite result can establish only that the frozen implementation passes the specified software tests in the recorded environment. It does not establish:
- exhaustive mathematical correctness for all degree-≤3 polynomials;
- uncertainty-aware root certification for uncertain statistical inputs;
- global optimizer exhaustiveness;
- inferential validity or coverage;
- causal contribution of accessibility to Value;
- scientific closure of C10-S or C10.

## 6. State

- Source snapshot: **FROZEN**
- Test definitions: **PERSISTED**
- Static source review: **COMPLETED WITH DOCUMENTED LIMITATIONS**
- Execution authorization: **NOT GRANTED**
- Tests executed: **NO**
- Numerical validation: **PENDING**
- Monte Carlo calibration: **NOT AUTHORIZED**
- Scientific execution: **NOT AUTHORIZED**
