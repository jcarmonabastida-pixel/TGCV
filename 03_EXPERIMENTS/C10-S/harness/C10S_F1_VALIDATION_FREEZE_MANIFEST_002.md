# C10-S F1 — Integrated Validation Freeze Manifest 002

**Status:** FROZEN SOURCE SNAPSHOT — NEW VALIDATION AUTHORIZATION REQUIRED  
**Freeze branch:** `research/c10s-f1-integrated-correction-20261119`  
**Frozen source commit:** `41d91bd19ba0dfd789d21b3d8398184daa100ff9`  
**Predecessor validated snapshot:** `0d430adae891b3914475c60334d93e977efc44cc`  
**Parent correction commit:** `7ef3420b59d13d0db2c2a72827fd5b58b6993380`  
**Scope:** corrected F1 profile-LR endpoint inversion, root-restoration tests, exact-rational Sturm isolation, F1/Sturm adjudication, F1/F5 comparative-engine integration tests, and integrated concordance matrix v002.

## 1. Freeze rule

The source snapshot is the exact Git commit above. Any validation must check out this commit in detached mode and verify all nine Git blob identities below. Do not execute from a moving branch tip. This manifest does not itself authorize execution.

The predecessor attempt 002 is retained unchanged as historical evidence. This is a new source snapshot because the F1 solver and its tests changed.

## 2. Correction scope

- F1 profile LR lower and upper endpoints are now solved in the dimensionless coordinate (x=\tau/s_{ref}), with (s_{ref}=\max(MSW,S^2_{means})>0).
- The root tolerance `xtol=1e-12) applies to the dimensionless coordinate, not the physical variance units.
- The fixed absolute (10^{-12}) variance floor was removed from the profile-likelihood reference-scale selection. The profile optimizer uses a positive data-derived reference scale.
- Conversion from the dimensionless coordinate back to physical variance rejects overflow and positive underflow.
- The F1 test module explicitly imports `_restore_polynomial_scale`; the existing underflow/overflow tests now target the helper.
- The observation-scale regression keeps factors (10^{-4},10^{-2},10^2,10^4), compares both interval endpoints in baseline units at `delta=1e-8), and compares the MLE at `delta=1e-10). These bounds are tighter than the previous assertions; no tolerance was relaxed.

## 3. Frozen source inventory

Git blob SHAs (not SHA-256):

| Role | Path | Git blob SHA |
|---|---|---|
| F1 solver | `03_EXPERIMENTS/C10-S/harness/c10s_f1_between_profile_likelihood.py` | `ae2fc89c8da09bbeba88a9309b5ba37750bcd631` |
| Independent exact-rational Sturm isolator | `03_EXPERIMENTS/C10-S/harness/c10s_f1_independent_root_isolator.py` | `3ac9ce31eb82421022fd8d2a65a0daee049322be` |
| F1/Sturm adjudicator | `03_EXPERIMENTS/C10-S/harness/c10s_f1_root_adjudication.py` | `9fa1cb21cd47e32030db8a00420e7dacfdc77321` |
| F1/F5 comparative engine | `03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_comparative_inference_engine.py` | `d277db712f8d2fdc7efbb5da5213d3087a84358a` |
| F1 solver tests | `03_EXPERIMENTS/C10-S/harness/test_c10s_f1_between_profile_likelihood.py` | `e7684bd3f70687ed5eeccb515db1d9e161407223` |
| Sturm isolator tests | `03_EXPERIMENTS/C10-S/harness/test_c10s_f1_independent_root_isolator.py` | `bb5cd2b8d2819fdb8757ea293d7e8f8fb9a1b4ce` |
| F1/Sturm adjudication tests | `03_EXPERIMENTS/C10-S/harness/test_c10s_f1_root_adjudication.py` | `2bcaed7423528fbbf9a6783c3f32e5edd30a10bc` |
| F1/F5 comparative-engine tests | `03_EXPERIMENTS/C10-S/harness/test_c10s_nested_mr_comparative_inference_engine.py` | `1061998ba93f363fbaaaed050c67acd6eb1c45b5` |
| Integrated concordance matrix v002 | `03_EXPERIMENTS/C10-S/harness/C10S_F1_INTEGRATED_CONCORDANCE_MATRIX_DRAFT_002.md` | `f4f7f771d4027de33d2892441e2da512ce3f793b` |

## 4. Runtime and preflight contract

- GitHub-hosted `ubuntu-24.04`.
- CPython `3.12.3`.
- Isolated virtual environment under `RUNNER_TEMP`.
- Only `numpy==2.1.3` and `scipy==1.14.1), installed as binary wheels with `--no-deps`.
- Verify the exact frozen commit, clean checkout, Python version, and all nine Git blob identities before creating evidence or environment directories.
- Import all four test modules before running the exact approved unittest command.
- Capture complete stdout, stderr, exit code, platform, dependency versions, and provenance.

## 5. Exact test scope

Working directory: `03_EXPERIMENTS/C10-S/harness`

```bash
$RUNNER_TEMP/c10s-f1-validation-venv/bin/python -m unittest -v \
  test_c10s_f1_between_profile_likelihood \
  test_c10s_f1_independent_root_isolator \
  test_c10s_f1_root_adjudication \
  test_c10s_nested_mr_comparative_inference_engine
```

One execution only. No retries under the same authorization.

## 6. Exclusions

No C10 scientific execution, DGP experiment, outer Monte Carlo calibration, parameter tuning, broad repository suite, new dataset, source modification during run, or scientific-closure claim is authorized by this freeze.

## 7. Evidence boundary

Even a PASS would establish only that the four listed software test modules pass for this exact snapshot and runtime. It would not establish exhaustive mathematical correctness, uncertainty-aware certification, inferential validity, causal contribution of accessibility to Value, or scientific closure.

**Current state:** source snapshot FROZEN; corrections IMPLEMENTED; static review recorded in concordance matrix v002; tests NOT EXECUTED; new one-shot authorization REQUIRED.
