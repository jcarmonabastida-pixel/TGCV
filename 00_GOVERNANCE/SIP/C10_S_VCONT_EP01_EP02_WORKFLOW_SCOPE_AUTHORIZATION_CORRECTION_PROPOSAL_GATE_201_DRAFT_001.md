# C10-S V_cont — Gate 201: EP-01/EP-02 workflow scope and authorization correction proposal

**Status:** DRAFT — DESIGN PROPOSAL ONLY / NOT APPROVED / NOT IMPLEMENTED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 200 — execution-profile registry and source-closure boundaries  
**Scope:** propose the smallest bounded correction to the two existing workflows before any future dispatch. Static source inspection only. No workflow, source, lockfile, test, or governance contract is changed by this proposal. No test, CI, Monte Carlo, producer, package-writer, calibration, or scientific execution is performed or authorized.

## 1. Purpose

Gate 200 found unrestricted unittest discovery in EP-01 and EP-02, a missing explicit JCS dependency in those discovered test sets, and an authorization mismatch in EP-01's automatic push trigger.

This proposal makes test scope, trigger authorization, and dependency closure explicit while preserving the historical workflows and the distinct purposes of EP-01, EP-02, and EP-03.

## 2. Additional source-level qualification to Gate 200

Inspection of `test_focal_harness.py` shows that its `FocalHarnessContractTests.run_case()` calls `Generator().generate(cfg)` for multiple deterministic fixtures. Therefore this module itself performs synthetic data generation when its tests execute; it is not merely a passive software-contract test.

The P178 bridge test also constructs a deterministic finite synthetic sample, and the P178 Monte Carlo smoke test executes a small number of simulated replicates. These operations are distinct from the 27-cell × 10,000-replication P178 primary Monte Carlo, but they are still generated-data test execution.

Accordingly, EP-01 must not be described as non-synthetic even after package-v2 and integrated V_cont modules are excluded. Its authorization input must explicitly cover its named synthetic test modules as well as the primary/replay Monte Carlo operation.

This is a static source finding; none of those tests were run in this gate.

## 3. Proposed EP-01 correction — P178 Analyzer profile

Workflow: `.github/workflows/c10-s-analyzer-monte-carlo.yml`

### 3.1 Trigger and authorization

Propose:
- remove the automatic `push` trigger;
- retain `workflow_dispatch` only;
- add a required boolean input `confirm_p178_profile_execution`, default `false`;
- require both the exact research branch ref and confirmation `true` at the job guard;
- describe the confirmation as authorizing the complete named profile: P178 contract/synthetic tests, the 27-cell × 10,000-replication primary Monte Carlo, clean replay, and their output capture.

The confirmation is a per-dispatch guard, not a standing authorization. No dispatch is authorized by this proposal.

### 3.2 Test selection

Replace unrestricted `python -B -m unittest -v` discovery in both primary and replay with the same explicit module allowlist:
- `test_focal_harness`
- `test_p178_analyzer_bridge`
- `test_p178_analyzer_monte_carlo`

The existing five-file compile list may remain if it matches the final command/source closure, but compilation must not be represented as proof that a file was executed or consumed.

Explicitly exclude:
- `test_vcont_integrated_harness`
- `test_vcont_benchmark_protocol`
- `test_vcont_capture_v2`
- `test_vcont_package_v2_serialization`
- `test_vcont_package_v2_verifier`

The replay must invoke the exact same three-module list from the clean archive. Do not use directory-wide discovery.

### 3.3 Dependencies

The selected P178 test and Monte Carlo path requires NumPy and SciPy. Replace unhashed direct installation with a profile-specific, complete dependency lock that pins exact distributions and accepted wheel SHA-256 hashes for the supported runner/Python platform.

Do not add JCS merely to compensate for excluded package-v2 tests. If later source-closure analysis finds a genuine import path to JCS in EP-01, either include it explicitly in the lock or narrow/fix the source boundary under a separately reviewed proposal.

No hashes are invented in this gate; lockfile creation and wheel-hash verification remain a prerequisite to implementation.

## 4. Proposed EP-02 correction — integrated synthetic contract suite

Workflow: `.github/workflows/c10-s-focal-harness-tests.yml`

### 4.1 Trigger and authorization

Preserve:
- manual dispatch only;
- required `confirm_synthetic_test_execution`, default `false`;
- exact research-branch guard;
- no push, schedule, or pull-request trigger.

Clarify that the confirmation authorizes only the explicitly enumerated integrated test suite and its clean replay. It does not authorize the P178 27 × 10,000 Monte Carlo, package production, calibration, or any confirmatory scientific execution.

### 4.2 Test selection

Replace unrestricted discovery in both primary and replay with an explicit module allowlist matching the intended current suite:
- `test_focal_harness`
- `test_p178_analyzer_bridge`
- `test_p178_analyzer_monte_carlo`
- `test_vcont_integrated_harness`
- `test_vcont_benchmark_protocol`
- `test_vcont_capture_v2`
- `test_vcont_package_v2_serialization`
- `test_vcont_package_v2_verifier`

This list is a proposal based on Gate 200's reconstructed discovery scope, not a frozen allowlist. Before implementation, compare it with the complete set of `test*.py` files and imports at the exact target commit. Any omitted test module must be explicitly classified as excluded with rationale; any newly added test module must not enter execution implicitly.

Use the identical explicit module list for primary and replay. A clean archive must contain the exact transitive source/data closure required by those modules, not an indiscriminate entire-directory extraction unless the manifest explicitly records that broader materialization.

### 4.3 Dependencies

The integrated suite requires the NumPy/SciPy dependencies used by the P178 modules and `rfc8785` used by package-v2 modules.

Before any future dispatch:
- define a single complete EP-02 dependency lock covering direct and transitive distributions;
- retain exact versions and verified wheel SHA-256 hashes for the selected Python/platform;
- preserve `--require-hashes` and binary-only installation policy where compatible;
- do not assume the EP-03 lock containing only `rfc8785==0.1.4` is a complete lock for EP-02;
- do not rely on runner-preinstalled packages.

No dependency lock is created or changed by this proposal.

## 5. EP-03 preservation

Do not broaden or merge EP-03 (`c10-s-vcont-package-v2-pure-tests.yml`) into either profile.

Preserve its current:
- manual-only trigger and research-branch guard;
- exact three-module pure-test allowlist;
- hash-pinned `rfc8785` dependency;
- no synthetic Generator execution boundary.

EP-03 remains the reference pure package/capture/verifier profile. Any source-closure refinement must preserve its semantic separation from EP-02.

## 6. Cross-profile acceptance conditions before implementation

The workflow correction must not be implemented until the following design checks are closed:

1. Exact current test-file inventory at the target branch commit is reconciled against EP-01 and EP-02 allowlists.
2. Every selected test module is classified as pure, synthetic data generation, or Monte Carlo; its authorization scope is explicit.
3. Primary and replay commands use identical explicit module lists and equivalent source/data boundaries.
4. EP-01 no longer has an automatic trigger capable of initiating synthetic tests or Monte Carlo.
5. EP-01 and EP-02 each have complete, reproducible, hash-verified dependency locks.
6. The exact clean-archive input list includes every runtime file/data input and excludes unrelated test modules.
7. The future source-materialization manifest binds the workflow, job/step, exact command, source closure, dependencies, runtime observations and execution identity without claiming that compile/checkout implies consumption.
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

**Gate 201: DESIGN PROPOSAL — CONDITIONAL / NOT APPROVED / NOT IMPLEMENTED.**

The proposal resolves the intended direction:
- EP-01 becomes manual-only and explicitly confirms its complete P178 synthetic-test + Monte Carlo profile.
- EP-01 and EP-02 use explicit primary/replay module allowlists rather than directory-wide discovery.
- EP-02 retains its existing explicit synthetic-execution confirmation.
- EP-01 and EP-02 receive complete hash-verified dependency locks.
- EP-03 remains separate and unchanged.

A further source-level inventory is required to verify the complete test-module list and transitive runtime dependencies before this proposal can be approved. Only after approval may a separate implementation authorization be considered.

**Next operation:** audit the exact `test*.py` inventory and transitive imports at the current research-branch HEAD, verify the proposed EP-01/EP-02 allowlists and dependency closures, and return a corrected acceptance-ready proposal. Do not edit workflows or run tests during that audit.
