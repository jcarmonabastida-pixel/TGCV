# C10-S F1 — Integrated Validation Result 003

**Result:** PASS — DETERMINISTIC SOFTWARE TEST SUITE  
**Authorization:** `C10S-F1-INTEGRATED-VALIDATION-20261119-03`  
**Authorization record commit:** `25955851d954a3d3b7b2c605c81b527b3a110d39`  
**Workflow run:** [44524421759](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44524421759)  
**Workflow run commit:** `25955851d954a3d3b7b2c605c81b527b3a110d39`  
**Frozen source commit executed:** `d65686beb2b242c0acb8ffbbcfe8ff55437f6c8b`  
**Artifact:** `c10s-f1-integrated-validation-002` (ID `14528952946`)  
**Artifact SHA-256:** `8db9c9da799464e02ebd944fba58e984cff1cdbd24649e290a866c4bdcea532e`

## 1. Execution result

GitHub Actions completed with conclusion `success`. The authorized job `validate-frozen-f1` completed every step successfully:

- exact frozen detached checkout;
- CPython 3.12.3 setup;
- clean checkout and frozen commit verification;
- nine of nine source blob identities matched;
- isolated virtual environment and pinned dependency installation;
- all four test modules imported;
- the exact authorized unittest command completed with exit code 0;
- immutable run evidence uploaded.

Runtime:
- Ubuntu 24.04.5 (GitHub-hosted `ubuntu-24.04`);
- CPython 3.12.3;
- NumPy 2.1.3;
- SciPy 1.14.1.

The isolated environment's `pip freeze` contained exactly:
`numpy==2.1.3`, `scipy==1.14.1`.

## 2. Test accounting

| Module | Tests | Result |
|---|---:|---|
| `test_c10s_f1_between_profile_likelihood` | 39 | PASS |
| `test_c10s_f1_independent_root_isolator` | 12 | PASS |
| `test_c10s_f1_root_adjudication` | 10 | PASS |
| `test_c10s_nested_mr_comparative_inference_engine` | 12 | PASS |
| **Total** | **73** | **73 PASS / 0 FAIL / 0 ERROR** |

Unittest summary in captured stderr:

```text
Ran 73 tests in 0.712s

OK
```

Captured process exit code: `0`. Captured stdout was empty; verbose unittest output was captured in stderr.

The executed suite includes the observation-scale equivariance regression for the profile interval and log-likelihood; exact binary-rational score-coefficient construction and overflow/underflow abstention; multiple and near-degenerate critical-root handling; exact-rational Sturm isolation including multiple, close and boundary roots; F1/Sturm agreement/discrepancy/unresolved adjudication; and F1/F5 comparative-engine integration contracts.

## 3. Evidence integrity

The workflow checked out exactly `d65686beb2b242c0acb8ffbbcfe8ff55437f6c8b` in detached HEAD state. All nine frozen Git blob hashes matched the expected values. The four test modules imported successfully before the test command.

Artifact contents:
- `preflight.txt`
- `expected-blobs.tsv`
- `blob-verification.txt`
- `dependencies.txt`
- `runtime-imports.txt`
- `import-preflight.txt`
- `test.stdout`
- `test.stderr`
- `exit-code.txt`

The GitHub-hosted setup action upgraded pip in its hosted toolcache from 24.0 to 26.3. The isolated test virtual environment's recorded installed-package set remained exactly NumPy 2.1.3 and SciPy 1.14.1; no extra test dependency was installed into that environment.

## 4. Replay and authorization boundary

The authorization explicitly permitted one execution only and prohibited automatic retry/replay. Therefore no replay was performed. The result is the primary deterministic software-test execution and its artifact/log audit, not a replay-certified execution.

No DGP experiment, outer Monte Carlo calibration, parameter tuning, broad repository test suite, external dataset, or scientific C10 execution was performed.

## 5. Interpretation and remaining limits

**Accepted result for this gate:** `PASS — 73/73 DETERMINISTIC SOFTWARE TESTS`.

This supports that the tested F1 solver, independent Sturm isolator, F1/Sturm adjudicator and F1/F5 comparative-engine integration satisfy the 73 encoded test cases on the exact frozen source and runtime.

It does **not** establish:
- exhaustive mathematical correctness for every polynomial or floating-point input;
- certification for uncertain/interval-valued original statistics;
- exhaustive global optimizer behavior beyond encoded tests;
- inferential validity or statistical coverage;
- robustness across all platforms, dependency versions or hardware;
- causal contribution of accessibility to Value;
- completion or scientific closure of C10-S.

**Next scientific status:** F1's integrated deterministic software validation gate is PASS. Mathematical exhaustiveness, broader numerical validation/calibration and any authorized scientific DGP experiment remain separate open gates and require their own design, review and authorization.
