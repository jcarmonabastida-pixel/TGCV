# C10-S V_cont — Gate 201: EP-01/EP-02 workflow scope and authorization correction proposal

**Status:** RECONCILED DESIGN PROPOSAL — DEPENDENCY LOCKS OPEN / NOT APPROVED / NOT IMPLEMENTED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 200 — execution-profile registry and source-closure boundaries  
**Scope:** static reconciliation of the complete tracked test-module inventory visible in PR #116, test behavior, import/dependency closure and the minimum EP-01/EP-02 workflow correction. No workflow, source, lockfile, test, or governance contract is changed. No test, CI, Monte Carlo, producer, package-writer, calibration, or scientific execution is performed or authorized.

## 1. Purpose

Gate 200 found unrestricted unittest discovery in EP-01 and EP-02, a missing explicit JCS dependency in those discovered test sets, and an authorization mismatch in EP-01's automatic push trigger.

This gate reconciles the proposed correction against the current PR changed-file inventory and source imports. It preserves the historical workflows and the distinct purposes of EP-01, EP-02 and EP-03.

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

### 3.3 Dependency closure

Static import inspection identifies NumPy and SciPy as the external runtime dependencies for the selected P178 test/runner path. The selected modules do not require JCS merely by virtue of the V_cont package tests, which are excluded.

Replace unhashed direct installation with a profile-specific complete dependency lock that pins exact distributions and accepted wheel SHA-256 hashes for the supported runner/Python platform. Do not invent hashes. Lockfile creation and wheel-hash verification remain open prerequisites.

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

### 4.3 Dependency closure

Static import inspection identifies:
- NumPy and SciPy for the P178 bridge/smoke-test path;
- `rfc8785==0.1.4` for capture and package-v2 serialization/verifier paths;
- Python standard-library modules for the remaining inspected test and harness paths.

The existing `requirements-vcont-v2.lock` contains only the hash-pinned JCS dependency and is not a complete EP-02 lock. Before any dispatch:
- define one complete EP-02 dependency lock covering direct and transitive distributions;
- retain exact versions, platform wheel filenames/tags and verified SHA-256 hashes;
- preserve `--require-hashes` and binary-only installation where compatible;
- do not rely on runner-preinstalled packages.

No dependency lock is created or changed by this gate. Exact resolved transitive versions and wheel hashes remain OPEN.

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
5. EP-01 and EP-02 each have complete, reproducible, hash-verified dependency locks.
6. The clean-archive input list includes every required runtime file/data input and excludes unrelated test modules.
7. The future source-materialization manifest binds workflow, job/step, exact command, source closure, dependencies, runtime observations and execution identity without claiming that compile/checkout implies consumption.
8. EP-03 remains unchanged in purpose and test scope.
9. No workflow is dispatched as part of design approval or implementation review.

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

## 8. Disposition and next operation

**Gate 201: RECONCILED DESIGN PROPOSAL — CONDITIONAL / NOT APPROVED / NOT IMPLEMENTED.**

The design direction is now explicit:
- EP-01 becomes manual-only and explicitly confirms its complete P178 synthetic-test + Monte Carlo profile.
- EP-01 uses the three named P178 modules only.
- EP-02 retains its explicit synthetic-execution confirmation and uses the eight named modules only.
- EP-01 and EP-02 receive separate complete hash-verified dependency locks.
- EP-03 remains separate and unchanged.

The test-module allowlists are reconciled against the tracked PR inventory and Gate 200's discovery audit. Dependency lock contents, exact wheel hashes, and the final source/runtime closure are not yet closed. This proposal therefore remains conditional and is not implementation authorization.

**Next operation:** close the exact dependency-lock contents and wheel-hash verification for EP-01 and EP-02, then conduct the final source-materialization closure audit. Do not edit workflows or dispatch runs during that design step.
