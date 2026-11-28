# C10-S V_cont — Gate 203: coordinated workflow and materialization implementation plan

**Status:** IMPLEMENTATION PLAN — CONDITIONAL / NOT APPROVED FOR IMPLEMENTATION / NO EXECUTION AUTHORIZED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 202 — runtime and source-materialization boundary audit  
**Scope:** define one coordinated, minimal implementation sequence for EP-01, EP-02 and EP-03, preserving their distinct execution purposes. This is a plan only. No workflow, source, lockfile, test, package schema or governance file is changed by this gate. No CI, tests, Monte Carlo, producer, package writer, calibration or scientific execution is performed or authorized.

## 1. Purpose and decision

Gates 200–202 established:
- EP-01 and EP-02 use unrestricted unittest discovery broader than their declared compile lists;
- EP-01's automatic push trigger can initiate synthetic tests and a 27 × 10,000 Monte Carlo without a per-dispatch confirmation;
- EP-01/EP-02 have incomplete dependency declarations;
- Gate 201 proposed explicit module lists and recorded PyPI wheel checksums;
- Gate 202 found mutable runtime/action selectors and a primary/replay bytecode-cache mismatch.

The corrections are interdependent. Implementing only the test allowlists without dependency locks, or adding a materialization manifest without resolving the bytecode boundary, would leave the profiles internally inconsistent.

**Decision:** implement the three workflow profiles as one coordinated infrastructure-only change after approval. Keep the C10 scientific design, DGP, estimands, seeds, statistical criteria and package-v2 schema untouched.

## 2. Intended end state by profile

### EP-01 — P178 Analyzer Monte Carlo

1. Trigger: `workflow_dispatch` only; remove `push`.
2. Required boolean input: `confirm_p178_profile_execution`, default `false`.
3. Job guard: exact `research/c10-s-consolidation-draft` ref and confirmation true.
4. Explicit test modules in primary and replay:
   - `test_focal_harness`
   - `test_p178_analyzer_bridge`
   - `test_p178_analyzer_monte_carlo`
5. Preserve the 27-cell × 10,000-replication primary Monte Carlo and byte-for-byte CSV/manifest comparison with clean replay.
6. Candidate lock: NumPy 2.3.5 + SciPy 1.17.0 with Gate 201 wheel hashes.
7. Replay archive: exact profile-specific source/data closure, not the entire harness directory.
8. Confirmation scope includes deterministic synthetic tests, the primary Monte Carlo, clean replay and output capture.

### EP-02 — integrated synthetic contract suite

1. Trigger: manual dispatch only.
2. Preserve required `confirm_synthetic_test_execution`, default false, and exact research-branch guard.
3. Explicit eight-module test list in primary and replay, exactly as Gate 201 §2.
4. Candidate lock: NumPy 2.3.5 + SciPy 1.17.0 + rfc8785 0.1.4 with Gate 201 wheel hashes.
5. Replay archive: exact integrated source/data closure.
6. Confirmation scope covers only the eight-module integrated suite and replay. It does not authorize the P178 27 × 10,000 Monte Carlo, package production, calibration or confirmatory execution.

### EP-03 — package-v2 pure capture/writer/verifier

1. Preserve manual dispatch, research-branch guard and exact three-module pure allowlist.
2. Preserve the existing hash-pinned JCS dependency and no-synthetic-producer boundary.
3. Add only the common runtime/source manifest capture and artifact retention needed for provenance.
4. Do not merge EP-03 into EP-02 or broaden its test modules.

## 3. Dependency lock implementation

Create two new, profile-specific lockfiles; do not repurpose the existing JCS-only lock:

- `requirements-p178-analyzer.lock`: NumPy 2.3.5 and SciPy 1.17.0.
- `requirements-vcont-integrated.lock`: NumPy 2.3.5, SciPy 1.17.0 and rfc8785 0.1.4.

Use only the exact CPython 3.12 Linux x86-64 manylinux wheel filenames and PyPI SHA-256 values recorded in Gate 201. Install with:
`python -m pip install --require-hashes --only-binary=:all: -r <profile-lock>`.

Do not change `requirements-vcont-v2.lock`; EP-03 continues to use it.

The lockfile implementation must:
- preserve exact version and hash lines from Gate 201;
- record the lockfile path and Git blob SHA in the profile manifest;
- avoid unpinned direct installs in EP-01/EP-02;
- verify the selected architecture/platform before installation;
- fail closed if pip selects a wheel not covered by the lock.

The hashes are PyPI-published wheel metadata, not locally re-hashed bytes. The first authorized install will enforce them against downloaded bytes. No lockfile is created by this plan.

## 4. Runtime identity implementation

For all three workflows:

1. Replace `ubuntu-latest` with an explicit supported Ubuntu runner label compatible with the selected manylinux wheel tags (proposed `ubuntu-24.04`).
2. Assert `x86_64` before installing platform-specific locks.
3. Pin `actions/checkout`, `actions/setup-python`, and, where used, `actions/upload-artifact` to immutable commit SHAs. Resolve and record the exact SHAs during implementation; do not invent them in this plan.
4. Retain Python 3.12 only after choosing the supported patch policy. Capture the full interpreter version/build and implementation.
5. Capture pip version and exact install command/flags.
6. Capture runner image metadata (`ImageOS`, `ImageVersion` where provided), `/etc/os-release`, architecture and libc/glibc version.
7. Record workflow path/blob SHA, commit, root tree, event/ref, run ID, run attempt, job and step identity, and the actual confirmation input value where applicable.

A mutable hosted-runner image cannot be made immutable merely by changing its label. Its actual image revision must be recorded; if that metadata is unavailable, the manifest must state the limitation.

## 5. Bytecode-cache equivalence correction

Preserve the syntax-check step only if its generated output is excluded from the test-import boundary.

Required sequence for EP-01, EP-02 and EP-03:
1. Run the declared compile command.
2. Remove every generated `__pycache__` directory and `.pyc` file from the source tree.
3. Assert no bytecode cache remains.
4. Run tests with `python -B` and the explicit module list.
5. For EP-01/EP-02, create the clean replay archive from the same commit and exact file list; assert no cache exists there; run the identical test command under the same `-B` policy.

Do not treat `PYTHONDONTWRITEBYTECODE=1` or `-B` as a substitute for deleting caches already generated by `py_compile`. The manifest must record the cleanup and boundary assertion.

## 6. Profile-specific source/data archive allowlists

The following are the planned archive roots. The exact path inventory and file hashes must be generated from the implementation commit before a workflow is eligible for dispatch.

### EP-01
- `03_EXPERIMENTS/C10-S/harness/test_focal_harness.py`
- `03_EXPERIMENTS/C10-S/harness/test_p178_analyzer_bridge.py`
- `03_EXPERIMENTS/C10-S/harness/test_p178_analyzer_monte_carlo.py`
- `03_EXPERIMENTS/C10-S/harness/focal_harness.py`
- `03_EXPERIMENTS/C10-S/harness/run_p178_analyzer_monte_carlo.py`
- `03_EXPERIMENTS/C10-S/calibration/p178_focal_monte_carlo.py`
- `03_EXPERIMENTS/C10-S/calibration/p178_reference_N700.csv`

### EP-02
- all eight explicit test modules in Gate 201 §2;
- `focal_harness.py`;
- `run_p178_analyzer_monte_carlo.py`;
- `vcont_integrated_harness.py`;
- `vcont_benchmark_protocol.py`;
- `vcont_evidence_export.py`;
- `vcont_package_v2.py`;
- `vcont_package_v2_verify.py`;
- `p178_focal_monte_carlo.py`;
- `p178_reference_N700.csv`.

### EP-03
- preserve the existing three pure test modules;
- `vcont_evidence_export.py`;
- `vcont_package_v2.py`;
- `vcont_package_v2_verify.py`;
- `vcont_benchmark_protocol.py`;
- `vcont_integrated_harness.py`;
- `requirements-vcont-v2.lock`.

No extra calibration CSV, seed bank, generated producer input or network resource may be added by inference. Any newly discovered runtime file must be reconciled and added explicitly before the manifest can PASS.

## 7. Execution/source manifest design

Add a common, profile-versioned manifest outside the 14-file V_cont package inventory. It must include:

- profile ID/version and exact workflow path/blob SHA;
- repository, tested commit and root tree;
- action implementation SHAs;
- event/ref/run/attempt/job/step identity;
- actual authorization input and scope;
- runner image/OS/architecture/libc;
- Python full version/build, executable, pip version and install flags;
- lockfile path/blob SHA and installed distribution versions;
- selected wheel filenames/platform tags/PyPI SHA-256 values;
- exact test module list, command, working directory and relevant environment;
- exact archive file list and per-file type/mode/size/SHA-256;
- bytecode-cache cleanup and no-cache assertion result;
- primary/replay output and log hashes, plus GitHub artifact ID and digest where available.

Keep the evidence vocabulary conservative:
- `declared_input`;
- `materialized_input`;
- `observed_consumed_input`;
- `not_observed`.

Do not mark a file `observed_consumed_input` solely because it was checked out, compiled or imported. If actual file-open observation is not implemented, leave consumption unobserved and report only the declared/materialized closure.

EP-01 already has an execution manifest; extend it without removing its existing output hashes. EP-02's manifest must bind the actual input rather than hard-code confirmation true and should add output hashes. EP-03 should emit a pure-test execution manifest and retain it as a GitHub artifact or equivalent durable run attachment.

Do not add a fifteenth package file or change the frozen 14-file package inventory.

## 8. Implementation sequence and review gates

Implementation, if separately authorized, should be one coordinated research-branch change in this order:

1. Add the two profile-specific lockfiles and verify exact candidate hash entries.
2. Pin runtime/action selectors and add runtime identity capture.
3. Apply EP-01 trigger/input/module-list correction.
4. Apply EP-02 module-list and dependency correction while preserving its confirmation gate.
5. Preserve EP-03 pure test scope; add only common manifest/runtime capture and bytecode cleanup.
6. Apply bytecode cleanup and no-cache assertions to all profiles.
7. Narrow primary/replay source archives to the exact path lists.
8. Add/extend manifests and artifact capture.
9. Perform static-only review of workflow YAML, allowlists, lock hashes, source lists, manifest schema and Git diff.
10. Stop. Do not dispatch any workflow as part of implementation or static review.

A separate explicit authorization is required for any later EP-01, EP-02 or EP-03 workflow dispatch. EP-01/EP-02 confirmations are per-dispatch gates and do not substitute for the user's authorization to initiate the run.

## 9. Acceptance criteria for the coordinated implementation

The implementation may be considered statically ready only if:

- EP-01 has no push trigger and requires its explicit confirmation input;
- EP-01 and EP-02 use their exact explicit module lists in primary and replay;
- EP-01 and EP-02 use separate complete hash-enforced dependency locks;
- EP-03 retains its pure three-module test allowlist and JCS lock;
- all profiles use an explicit runner label and immutable action SHAs, with actual runtime identity captured;
- primary and replay have equivalent source/data file lists and bytecode-cache policies;
- no `.pyc`/ `__pycache__` input exists at test-import boundaries;
- source archives contain only the declared profile closure;
- manifests bind exact run/attempt/artifact identities and avoid unsupported consumed-input claims;
- no scientific code, DGP, estimand, calibration, seed or package schema is modified;
- no workflow is dispatched and no test or scientific execution is performed.

Static readiness is not execution PASS and is not scientific evidence.

## 10. Governance and non-goals

This plan does not:
- authorize implementation or execution;
- modify `main`, RMA, Evidence→Claim Matrix, STATUS or C09;
- alter C10 estimands, DGPs, scientific thresholds, seeds or causal claims;
- alter Gate 195–202 historical records;
- change the package's 14-file inventory or 28-component configuration fingerprint;
- create lockfiles, edit workflows, run tests, dispatch CI or execute Monte Carlo.

## 11. Disposition and next operation

**Gate 203: COORDINATED IMPLEMENTATION PLAN — CONDITIONAL / NOT APPROVED / NOT IMPLEMENTED / EXECUTION NOT AUTHORIZED.**

The plan consolidates the minimum changes needed to make EP-01, EP-02 and EP-03 explicit, reproducible and evidence-bounded without changing their scientific purpose.

**Next operation:** obtain explicit approval for this coordinated infrastructure-only implementation plan. Until then, keep all workflows, lockfiles and source code unchanged; continue only with static review or clarification.
