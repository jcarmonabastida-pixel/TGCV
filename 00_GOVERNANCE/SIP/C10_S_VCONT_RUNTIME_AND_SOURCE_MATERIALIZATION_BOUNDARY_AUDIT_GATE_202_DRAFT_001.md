# C10-S V_cont — Gate 202: runtime and source-materialization boundary audit

**Status:** STATIC AUDIT COMPLETE / MATERIALIZATION GAPS IDENTIFIED / NO WORKFLOW OR EXECUTION AUTHORIZED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 201 — EP-01/EP-02 workflow scope and authorization correction proposal  
**Scope:** inspect the three existing workflow definitions, exact source archive commands, compile/test sequencing, runtime selectors and current execution-manifest fields. Identify the minimum requirements for a profile-specific materialization manifest. No workflow, source, dependency lock, or package schema is changed. No test, workflow dispatch, producer, package writer, calibration, Monte Carlo, or scientific execution is performed.

## 1. Purpose and decision

Gate 201 reconciled the test-module allowlists and recorded candidate PyPI wheel hashes. The next prerequisite is to determine whether the current workflows materialize equivalent inputs and record enough runtime identity to support a reproducible execution claim.

**Decision:** current workflows do not yet establish a complete runtime/source-materialization identity. In particular, the compile step creates bytecode caches before primary test execution, while clean replay starts from a Git archive without those caches. This makes primary and replay materialized inputs non-identical unless caches are removed or isolated. The workflows also use mutable runner/action selectors and record only partial runtime identity.

## 2. Exact workflow source identities inspected

| Profile | Workflow | Blob SHA |
|---|---|---|
| EP-01 | `.github/workflows/c10-s-analyzer-monte-carlo.yml` | `54eccca47a1dd5628dafabcba70a0e1c872a44a1` |
| EP-02 | `.github/workflows/c10-s-focal-harness-tests.yml` | `d471cc4340a457567bc6dff0f9160fdf7f74be48` |
| EP-03 | `.github/workflows/c10-s-vcont-package-v2-pure-tests.yml` | `43968790b5c90c9859fdadf75c8291d72eb373b9` |

All three currently select `runs-on: ubuntu-latest`, `actions/checkout@v4`, and `actions/setup-python@v5` with `python-version: '3.12'`. EP-01 and EP-02 also use `actions/upload-artifact@v4`.

These action references are mutable tags, the runner label is mutable, and Python 3.12 resolves to a patch release at execution time. None of the workflows records the resolved action commit SHAs, full Python build, pip version, runner image version, OS release, or architecture.

## 3. Runtime profile findings

### EP-01

- Runner: `ubuntu-latest`, not an immutable image identifier.
- Actions: checkout@v4, setup-python@v5, upload-artifact@v4.
- Python selector: 3.12, patch/build not pinned or recorded.
- Dependencies: direct unhashed `numpy==2.3.5 scipy==1.17.0` installation.
- Test invocation: unrestricted discovery in the harness directory (correction proposed in Gate 201).
- Primary Monte Carlo: 27 cells × 10,000 replications.
- Clean replay: full harness directory plus `p178_focal_monte_carlo.py` and `p178_reference_N700.csv`.
- Execution manifest: workflow, tested commit, run ID, attempt, event, ref, and hashes of selected outputs/logs. No dependency, runtime, action, test-module, source-tree, job/step, or per-input materialization identity.

### EP-02

- Runner/actions/Python selector: same mutable selectors as EP-01.
- Dependencies: direct unhashed `numpy==2.3.5 scipy==1.17.0`; discovered package-v2 tests additionally import `rfc8785`, which is not explicitly installed by this workflow.
- Test invocation: unrestricted discovery in the harness directory (correction proposed in Gate 201).
- Clean replay: full harness directory plus the two P178 calibration inputs.
- Execution manifest: workflow, tested commit, run ID, attempt, event, ref, and a hard-coded `synthetic_execution_confirmed: true`. It does not record actual dependency/runtime/action identities, test-module allowlist, source hashes, or output hashes. The workflow input guard requires the boolean to be true, but the manifest does not bind its value directly to the workflow input field.

### EP-03

- Runner/actions/Python selector: same mutable selectors except no upload-artifact action.
- Dependency: hash-enforced `rfc8785==0.1.4` via `requirements-vcont-v2.lock`.
- Test invocation: explicit three-module pure-test allowlist.
- No clean replay, output artifact, or execution manifest is defined in the workflow. GitHub run logs remain available as platform records but are not a profile-specific execution companion.

## 4. Materialization mismatch: generated Python bytecode caches

All three workflows run `python -m py_compile` before their primary tests. The compile step sets `PYTHONDONTWRITEBYTECODE=1`, but `py_compile` explicitly writes `.pyc` files under `__pycache__`; the environment variable controls normal import-time cache writes and does not suppress explicit compilation output.

EP-01 and EP-02 then run primary tests with `python -B` / `PYTHONDONTWRITEBYTECODE=1`. Those flags prevent new cache writes but do not prevent the import system from reading existing valid bytecode caches. Their primary tests may therefore load the generated `.pyc` files.

The clean replay uses `git archive`, which materializes tracked source files but not the ignored/untracked `__pycache__` files generated in the primary working tree. Replay tests consequently import from source and compile in memory rather than reading the primary run's pre-generated bytecode caches.

EP-03 has no replay, but it has the same compile-then-test sequence and therefore may execute from the generated caches.

**Finding:** primary and replay do not have an identical materialized file set at the test-import boundary. This is a materialization/source-closure discrepancy even if the generated bytecode corresponds to the same source. It must be resolved before byte-identical replay is used as evidence of source/runtime equivalence.

**Minimal correction candidates (not implemented):**
1. after explicit compilation, delete every generated `__pycache__` directory before primary tests and replay; or
2. compile to a dedicated temporary cache outside the source tree and ensure test imports use the same declared policy; or
3. remove the separate compile step and let the explicitly named tests import source under one consistent bytecode-cache policy.

The simplest fail-closed design is to compile for syntax checking, delete generated caches, then run the same explicit module list under `-B` for primary and replay. The materialization manifest must record the cleanup step and verify that no cache directory remains at the test boundary.

## 5. Candidate source/data closure by profile

The following is a source-level closure candidate from the workflow commands and imports. It is not yet a final observed-consumption manifest.

### EP-01 — after Gate 201 allowlist correction

**Test roots:**
- `test_focal_harness.py`
- `test_p178_analyzer_bridge.py`
- `test_p178_analyzer_monte_carlo.py`

**Execution entrypoint:**
- `run_p178_analyzer_monte_carlo.py`

**Local Python source:**
- `focal_harness.py`
- `p178_focal_monte_carlo.py`

**External data/configuration:**
- `p178_reference_N700.csv` (read by the Analyzer Monte Carlo runner for paired-seed reference comparisons)
- explicit CLI parameters: `--replications 10000`, `--strict-protocol`, and output directory
- workflow commit/ref/run/attempt and explicit authorization input

**External packages:**
- NumPy 2.3.5
- SciPy 1.17.0

### EP-02 — after Gate 201 allowlist correction

**Test roots:** all eight modules listed in Gate 201 §2.

**Local Python source:**
- `focal_harness.py`
- `run_p178_analyzer_monte_carlo.py`
- `vcont_integrated_harness.py`
- `vcont_benchmark_protocol.py`
- `vcont_evidence_export.py`
- `vcont_package_v2.py`
- `vcont_package_v2_verify.py`
- `p178_focal_monte_carlo.py`

**External data/configuration:**
- `p178_reference_N700.csv` for the P178 bridge/smoke-test imports and runner path
- inline deterministic fixtures in test modules
- exact eight-module command list and explicit authorization input

**External packages:**
- NumPy 2.3.5
- SciPy 1.17.0
- rfc8785 0.1.4

### EP-03 — current pure package profile

**Test roots:**
- `test_vcont_capture_v2.py`
- `test_vcont_package_v2_serialization.py`
- `test_vcont_package_v2_verifier.py`

**Local Python source:**
- `vcont_evidence_export.py`
- `vcont_package_v2.py`
- `vcont_package_v2_verify.py`
- `vcont_benchmark_protocol.py`
- `vcont_integrated_harness.py`

**External data/configuration:**
- inline deterministic fixture objects; no P178 CSV or calibration run input is passed by the selected pure test command
- `requirements-vcont-v2.lock`

**External packages:**
- rfc8785 0.1.4

All source/data lists remain candidate closures until exact file-level hashes and actual runtime reads are recorded. Imports alone do not prove that every imported function or path was exercised.

## 6. Minimal governed runtime/materialization contract

Before any future profile dispatch, its companion manifest should record at least:

1. exact repository commit and root tree identity;
2. workflow path/blob SHA, action references resolved to immutable action commit SHAs, workflow run/attempt, job and step identities;
3. exact event/ref and authorization input value;
4. exact runner image identifier/version, OS release, architecture and libc version;
5. Python implementation/full version/build, executable path, pip version and install flags;
6. exact dependency lock path/blob SHA, selected wheel filename/platform tags/SHA-256 and installed distribution versions;
7. exact test module allowlist, entrypoint, arguments, working directory and environment relevant to execution;
8. exact source/data archive path list, per-file type/mode/size/SHA-256, and Git tree/commit identity;
9. explicit generated-file/cache policy and a fail-closed check that no undeclared generated inputs exist at the test boundary;
10. output/log hashes and association to the exact run/attempt/artifact identifiers.

The manifest must distinguish `declared_input`, `materialized_input`, `observed_consumed_input` and `not_observed`. It must not claim that an imported module's every dependency was executed, or that a checked-out/compiled file was consumed.

## 7. Required corrections before manifest freeze

1. Apply the Gate 201 trigger and test allowlist correction only after separate approval/implementation authorization.
2. Use candidate lock entries from Gate 201 with `--require-hashes --only-binary=:all:`; preserve the exact CPython 3.12 manylinux wheel platform contract.
3. Replace `ubuntu-latest` with an explicit supported Ubuntu runner label and assert x86-64 before installing platform-specific wheels; record the actual runner image version.
4. Pin checkout/setup-python/upload-artifact actions to immutable commit SHAs, or record and verify their resolved immutable implementation identities.
5. Capture full Python and pip versions and install flags.
6. Resolve the bytecode-cache discrepancy by clearing/isolation before both primary and replay tests; assert the same cache policy at both boundaries.
7. Narrow Git archive path lists to the profile-specific source/data closure; do not archive the entire harness directory after explicit module allowlists are adopted.
8. Add a source/runtime manifest to EP-02 and EP-03 with equivalent identity fields; do not infer a manifest from GitHub run logs alone.
9. Keep all workflows manual-only for profiles that can generate synthetic data; EP-01 push trigger removal remains a stop condition.
10. Do not dispatch workflows or run tests as part of this design audit.

## 8. Governance and non-goals

This gate does not:
- implement the Gate 201 proposal;
- create or alter dependency lockfiles;
- change source code, tests, workflow YAML, package schema, 14-file inventory or 28-component configuration fingerprint;
- run `py_compile`, unittest, Monte Carlo, producer, package writer, calibration or scientific execution;
- authorize any future workflow dispatch;
- modify `main`, RMA, Evidence→Claim Matrix, STATUS or C09.

## 9. Disposition and next operation

**Gate 202: STATIC RUNTIME/MATERIALIZATION AUDIT COMPLETE / BYTECODE CACHE MISMATCH IDENTIFIED / MATERIALIZATION MANIFEST NOT FROZEN.**

Gate 201's candidate dependency hashes are sufficient to define candidate lock entries for the selected CPython 3.12 Linux x86-64 wheels, but runtime identity remains mutable and the primary/replay test boundary is not materialization-equivalent due to generated `.pyc` caches.

**Next operation:** prepare a coordinated implementation plan covering Gate 201 workflow scope/authorization corrections, the bytecode-cache cleanup/isolation rule, immutable action/runtime identity, and profile-specific source-manifest capture. Do not edit workflows, create lockfiles, or dispatch tests without separate approval.
