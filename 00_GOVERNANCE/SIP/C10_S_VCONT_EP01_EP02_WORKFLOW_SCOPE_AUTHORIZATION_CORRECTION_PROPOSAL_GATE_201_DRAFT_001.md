# C10-S V_cont — Gate 201: EP-01/EP-02 workflow scope and authorization correction proposal

**Status:** RECONCILED DESIGN PROPOSAL — PYPI WHEEL HASHES RECORDED / RUNTIME AND MATERIALIZATION CLOSURE OPEN / NOT APPROVED / NOT IMPLEMENTED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 200 — execution-profile registry and source-closure boundaries  
**Scope:** static reconciliation of the complete tracked test-module inventory visible in PR #116, test behavior, import/dependency closure and the minimum EP-01/EP-02 workflow correction. No workflow, source, lockfile, test, or governance contract is changed. No test, CI, Monte Carlo, producer, package-writer, calibration, or scientific execution is performed or authorized.

## 1. Purpose

Gate 200 found unrestricted unittest discovery in EP-01 and EP-02, a missing explicit JCS dependency in those discovered test sets, and an authorization mismatch in EP-01's automatic push trigger.

This gate reconciles the proposed correction against the current PR changed-file inventory, source imports and published wheel metadata. It preserves the historical workflows and the distinct purposes of EP-01, EP-02 and EP-03.

## 2. Test inventory and source-level classification

The current PR #116 tracked changed-file inventory contains eight C10-S harness test modules. This matches the eight modules identified by Gate 200's discovery audit:

| Module | Static behavior / relevant imports | Proposed profile |
|---|---|---|
| `test_focal_harness` | Calls `Generator().generate(cfg)` through `run_case`; synthetic deterministic fixtures; local `focal_harness` | EP-01, EP-02 |
| `test_p178_analyzer_bridge` | Constructs a deterministic finite P178 sample; imports NumPy and SciPy; local P178 calibration and focal harness | EP-01, EP-02 |
| `test_p178_analyzer_monte_carlo` | Runs a small-cell Monte Carlo smoke test (8 replicates); local P178 runner; NumPy/SciPy runtime path | EP-01, EP-02 |
| `test_vcont_integrated_harness` | Calls integrated `Generator`, `Sealer`, `Analyzer`, `Evaluator`; synthetic integrated fixtures | EP-02 |
| `test_vcont_benchmark_protocol` | Deterministic statistical/protocol summaries and validation; no simulation indicated by module contract; local benchmark protocol | EP-02 |
| `test_vcont_capture_v2` | Fixture-based capture/snapshot tests; imports `rfc8785`, benchmark/integrated/export modules | EP-02, EP-03 |
| `test_vcont_package_v2_serialization` | Pure deterministic archive/writer tests; no synthetic producer invocation; writer imports `rfc8785` | EP-02, EP-03 |
| `test_vcont_package_v2_verifier` | Pure independent-verifier primitive tests; imports `rfc8785`; no producer invocation by the test module's declared boundary | EP-02, EP-03 |

The eight-module inventory is supported by the PR's tracked changed-file listing and Gate 200's prior directory-discovery reconstruction. It is not a claim that the GitHub connector exposed a direct directory-listing API. At implementation time, the allowlist must be checked again against the exact target commit and any test files inherited from the PR base.

### 2.1 Qualification to Gate 200

`test_focal_harness.py` itself calls `Generator().generate(cfg)` in multiple test cases. The P178 bridge test constructs a deterministic generated sample, and the P178 smoke test runs a small simulated cell. These are generated-data test operations even though they are not the full 27-cell × 10,000-replication P178 primary Monte Carlo.

Therefore EP-01 must not be described as non-synthetic after excluding the V_cont integrated and package-v2 modules. Its confirmation input must cover the named synthetic tests as well as the primary/replay Monte Carlo.

No test was run to establish these classifications; they are static source-level observations.

## 3. Proposed EP-01 correction — P178 Analyzer profile

Workflow: `.github/workflows/c10-s-analyzer-monte-carlo.yml`

### 3.1 Trigger and authorization

Propose:
- remove the automatic `push` trigger;
- retain `workflow_dispatch` only;
- add a required boolean input `confirm_p178_profile_execution`, default `false`;
- require both the exact research branch ref and confirmation `true` at the job guard;
- describe the confirmation as authorizing the complete named profile: P178 synthetic/contract tests, the 27-cell × 10,000-replication primary Monte Carlo, clean replay, and output capture.

The confirmation is a per-dispatch guard, not a standing authorization. No dispatch is authorized by this proposal.

### 3.2 Test selection

Replace unrestricted `python -B -m unittest -v` discovery in both primary and replay with the same explicit module allowlist:
- `test_focal_harness`
- `test_p178_analyzer_bridge`
- `test_p178_analyzer_monte_carlo`

Explicitly exclude:
- `test_vcont_integrated_harness`
- `test_vcont_benchmark_protocol`
- `test_vcont_capture_v2`
- `test_vcont_package_v2_serialization`
- `test_vcont_package_v2_verifier`

The replay must invoke the exact same three-module list from the clean archive. Do not use directory-wide discovery. The compile list is not evidence that a module was executed or consumed.

### 3.3 Candidate EP-01 dependency lock

Static import inspection identifies NumPy and SciPy as the external runtime dependencies for the selected P178 test/runner path.

For a CPython 3.12, Linux x86-64, manylinux-compatible runner, PyPI publishes these exact wheel identities and SHA-256 checksums:

| Distribution | Exact wheel | PyPI SHA-256 |
|---|---|---|
| NumPy 2.3.5 | `numpy-2.3.5-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl` | `0d8163f43acde9a73c2a33605353a4f1bc4798745a8b1d73183b28e5b435ae28` |
| SciPy 1.17.0 | `scipy-1.17.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl` | `9eeb9b5f5997f75507814ed9d298ab23f62cf79f5a3ef90031b1ee2506abdb5b` |

Candidate requirements entries:

```text
numpy==2.3.5 \\
    --hash=sha256:0d8163f43acde9a73c2a33605353a4f1bc4798745a8b1d73183b28e5b435ae28
scipy==1.17.0 \\
    --hash=sha256:9eeb9b5f5997f75507814ed9d298ab23f62cf79f5a3ef90031b1ee2506abdb5b
```

SciPy 1.17.0's release notes support Python 3.11–3.14 and NumPy 1.26.4 or later; the existing NumPy 2.3.5 selection satisfies that declared minimum. The exact selected wheels are CPython 3.12 x86-64 manylinux builds.

**Integrity qualification:** the checksums above are the SHA-256 values published in PyPI's release-file metadata for the exact wheel filenames. An attempted direct binary download from the current environment was unavailable, so this gate does not claim an independent local re-hash of the wheel bytes. The future `pip --require-hashes` installation will enforce the published values against the bytes actually downloaded.

Do not add JCS merely to compensate for excluded package-v2 tests. If later source-closure analysis finds a genuine import path to JCS in EP-01, include it explicitly or revise the source boundary under a separately reviewed proposal.

## 4. Proposed EP-02 correction — integrated synthetic contract suite

Workflow: `.github/workflows/c10-s-focal-harness-tests.yml`

### 4.1 Trigger and authorization

Preserve:
- manual dispatch only;
- required `confirm_synthetic_test_execution`, default `false`;
- exact research-branch guard;
- no push, schedule, or pull-request trigger.

Clarify that confirmation authorizes only the explicitly enumerated eight-module suite and its clean replay. It does not authorize the P178 27 × 10,000 Monte Carlo, package production, calibration, or confirmatory scientific execution.

### 4.2 Test selection

Replace unrestricted discovery in both primary and replay with the exact eight-module allowlist in §2:
- `test_focal_harness`
- `test_p178_analyzer_bridge`
- `test_p178_analyzer_monte_carlo`
- `test_vcont_integrated_harness`
- `test_vcont_benchmark_protocol`
- `test_vcont_capture_v2`
- `test_vcont_package_v2_serialization`
- `test_vcont_package_v2_verifier`

Use the identical list for primary and replay. Reconcile it against the exact target commit before implementation; any newly added test module must not enter execution implicitly. Any excluded module must be named with a rationale.

The clean replay source archive must include the exact transitive source/data closure. Do not extract the entire harness directory merely for convenience unless that broader materialization is explicitly captured and justified in the future source manifest.

### 4.3 Candidate EP-02 dependency lock

Static import inspection identifies:
- NumPy 2.3.5 and SciPy 1.17.0 for the P178 bridge/smoke-test path;
- `rfc8785==0.1.4` for capture and package-v2 serialization/verifier paths;
- Python standard-library modules for the remaining inspected test and harness paths.

PyPI publishes the following JCS wheel checksum, which matches the existing `requirements-vcont-v2.lock` entry:

| Distribution | Exact wheel | PyPI SHA-256 |
|---|---|---|
| rfc8785 0.1.4 | `rfc8785-0.1.4-py3-none-any.whl` | `520d690b448ecf0703691c76e1a34a24ddcd4fc5bc41d589cb7c58ec651bcd48` |

Candidate EP-02 requirements are the two entries in §3.3 plus:

```text
rfc8785==0.1.4 \\
    --hash=sha256:520d690b448ecf0703691c76e1a34a24ddcd4fc5bc41d589cb7c58ec651bcd48
```

The existing `requirements-vcont-v2.lock` contains only this JCS dependency and is not a complete EP-02 lock. Before any dispatch:
- define separate complete EP-01 and EP-02 lock files from the candidate entries above;
- retain exact versions, platform wheel filenames/tags and published SHA-256 hashes;
- preserve `--require-hashes` and `--only-binary=:all:`;
- pin the workflow runner to a Linux x86-64 environment compatible with the selected manylinux wheels, rather than leaving architecture implicit;
- record Python full version/build, pip version, runner image version and architecture in the execution-profile/source-materialization evidence;
- do not rely on runner-preinstalled packages.

No dependency lock is created or changed by this gate. The wheel hashes are sourced from PyPI release-file metadata; local binary re-hashing was not performed.

## 5. EP-03 preservation

Do not broaden or merge EP-03 (`.github/workflows/c10-s-vcont-package-v2-pure-tests.yml`) into either profile.

Preserve its current:
- manual-only trigger and research-branch guard;
- exact three-module pure-test allowlist;
- hash-pinned `rfc8785` dependency;
- no synthetic Generator execution boundary.

EP-03 remains the reference pure package/capture/verifier profile. Its existing test scope and semantics remain separate from EP-02's integrated synthetic suite.

## 6. Cross-profile acceptance conditions before implementation

The workflow correction must not be implemented until:

1. The eight-module inventory is reconciled against the exact target branch commit and PR base.
2. Every selected module is classified as pure, synthetic data generation, or Monte Carlo; its authorization scope is explicit.
3. Primary and replay commands use identical explicit module lists and equivalent source/data boundaries.
4. EP-01 has no automatic trigger capable of initiating synthetic tests or Monte Carlo.
5. EP-01 and EP-02 use separate complete, reproducible, hash-enforced dependency locks.
6. The runner platform is constrained to match the selected wheel tags and its actual image/Python/pip identity is captured.
7. The clean-archive input list includes every required runtime file/data input and excludes unrelated test modules.
8. The future source-materialization manifest binds workflow, job/step, exact command, source closure, dependencies, runtime observations and execution identity without claiming that compile/checkout implies consumption.
9. EP-03 remains unchanged in purpose and test scope.
10. No workflow is dispatched as part of design approval or implementation review.

## 7. Non-goals and governance boundary

This proposal does not:
- change any C10 estimand, DGP, causal architecture, policy contrast, acceptance criterion, calibration, seed, or statistical method;
- alter Gate 195–200 historical records;
- alter the 14-file package inventory or 28-component configuration fingerprint;
- add a generic source-execution companion or a fifteenth package file;
- freeze the materialization-manifest schema or digest algorithm;
- implement a workflow, dependency lock, test command, adapter, or verifier;
- authorize CI, producer, calibration, Monte Carlo, or scientific execution;
- modify `main`, RMA, Evidence→Claim Matrix, STATUS, or C09.

## 8. Sources and hash evidence

- NumPy 2.3.5 PyPI release files: https://pypi.org/project/numpy/2.3.5/
- SciPy 1.17.0 PyPI release files: https://pypi.org/project/scipy/1.17.0/
- SciPy 1.17.0 release requirements: https://docs.scipy.org/doc/scipy/release/1.17.0-notes.html
- rfc8785 0.1.4 PyPI release files: https://pypi.org/project/rfc8785/0.1.4/

The hashes are published PyPI SHA-256 metadata for the exact wheel filenames. No local wheel bytes were available for a second hash calculation in this pass.

## 9. Disposition and next operation

**Gate 201: RECONCILED DESIGN PROPOSAL — CONDITIONAL / NOT APPROVED / NOT IMPLEMENTED.**

The design direction is now explicit:
- EP-01 becomes manual-only and explicitly confirms its complete P178 synthetic-test + Monte Carlo profile.
- EP-01 uses the three named P178 modules only.
- EP-02 retains its explicit synthetic-execution confirmation and uses the eight named modules only.
- EP-01 and EP-02 use separate candidate hash-enforced dependency locks.
- EP-03 remains separate and unchanged.

The test-module allowlists are reconciled against the tracked PR inventory and Gate 200's discovery audit. Candidate wheel identities, versions and PyPI checksums are recorded. The runner/runtime profile, local wheel-byte re-hash, final source-materialization closure, and implementation approval remain OPEN. This proposal is not implementation authorization.

**Next operation:** close the runtime profile and exact source-materialization inventory for the three workflows, then reconcile the candidate lock files against the actual runner/platform. Do not edit workflows or dispatch runs during that design step.
