# C10-S V_cont — Gate 200: execution-profile registry and source-closure boundaries

**Status:** PROFILE RECONSTRUCTION COMPLETE; TWO WORKFLOW SCOPE/DEPENDENCY DISCREPANCIES IDENTIFIED; MATERIALIZATION MANIFEST NOT AUTHORIZED  
**Branch:** research/c10-s-consolidation-draft  
**Parent:** Gate 199 — historical source-materialization reconciliation  
**Scope:** static reconstruction of the three existing C10-S GitHub Actions execution profiles, their command-level source/test closure, dependency declarations, external runtime inputs and authorization boundaries. No workflow was dispatched, no tests/imports/compilation were run, no producer or package writer was invoked, and no scientific execution occurred.

## 1. Purpose and decision

Gate 199 required execution profiles and source-closure rules to be defined before a canonical materialization manifest is designed.

This gate establishes the profile registry from the actual workflow YAML and source imports. It distinguishes the profile's declared purpose, commands actually executed, actual test-discovery scope, source/dependency closure, authorization controls and residuals that a later materialization manifest must bind.

**Critical finding:** two workflows use unrestricted Python unittest discovery from the harness directory. This is broader than their explicit compile lists and, in the P178 workflow, reaches integrated V_cont producer tests despite automatic push activation and no explicit synthetic-execution confirmation input. The P178 workflow also does not install the JCS dependency imported by discovered package-v2 tests. This is a static source/workflow finding only; no workflow was run to test the observed consequences.

## 2. Registry of existing execution profiles

### EP-01 — P178 legacy Analyzer Monte Carlo

**Workflow:** .github/workflows/c10-s-analyzer-monte-carlo.yml  
**Declared purpose:** 27-cell P178 Analyzer Monte Carlo plus clean replay.  
**Trigger:** push on selected P178/harness paths and manual dispatch.  
**Runner:** ubuntu-latest.  
**Authorization:** no explicit confirmation input; push trigger is automatic.  
**Checkout:** actions/checkout@v4, ref github.sha.  
**Python:** actions/setup-python@v5, python-version 3.12.  
**Dependencies installed:** numpy==2.3.5, scipy==1.17.0; no hash lock and no explicit JCS dependency installation.

**Commands:**
- Compile five named P178/legacy harness files.
- Run unrestricted python -B -m unittest -v from 03_EXPERIMENTS/C10-S/harness.
- Execute run_p178_analyzer_monte_carlo.py with 10,000 replications and strict protocol.
- Replay after extracting git archive containing the entire harness directory plus p178_focal_monte_carlo.py and p178_reference_N700.csv.
- Run unrestricted unittest discovery again from the extracted harness directory.
- Compare primary/replay CSV and manifest bytes.

**Declared P178-specific source inputs:**
- 03_EXPERIMENTS/C10-S/harness/run_p178_analyzer_monte_carlo.py
- 03_EXPERIMENTS/C10-S/harness/focal_harness.py
- 03_EXPERIMENTS/C10-S/harness/test_focal_harness.py
- 03_EXPERIMENTS/C10-S/harness/test_p178_analyzer_bridge.py
- 03_EXPERIMENTS/C10-S/harness/test_p178_analyzer_monte_carlo.py
- 03_EXPERIMENTS/C10-S/calibration/p178_focal_monte_carlo.py
- 03_EXPERIMENTS/C10-S/calibration/p178_reference_N700.csv
- External Python packages NumPy and SciPy.

**Actual test-discovery closure:** the command is not restricted to the five compile targets. Default unittest discovery in the harness directory discovers all test*.py modules, including:
- test_vcont_integrated_harness.py
- test_vcont_benchmark_protocol.py
- test_vcont_capture_v2.py
- test_vcont_package_v2_serialization.py
- test_vcont_package_v2_verifier.py

The integrated test module explicitly calls Generator.generate(...) in numerous test methods and exercises the Generator → Sealer → Analyzer → Evaluator path. Therefore the actual P178 workflow test command is not a P178-only test profile. Its push trigger can run those integrated synthetic producer tests without a dedicated explicit confirmation input.

The discovered package-v2 test modules import rfc8785 directly or through vcont_evidence_export.py / vcont_package_v2.py. EP-01 installs NumPy and SciPy but does not install the requirements-vcont-v2.lock dependency. This is an undeclared dependency in the actual discovery closure. Whether a runner image happens to provide it is not an acceptable contract.

**Clean replay boundary:** git archive extracts the entire harness directory, not only the P178 closure. The replay repeats unrestricted test discovery, so it reproduces the same broad test scope and undeclared dependency exposure.

**Disposition:** EP-01 is currently a mixed legacy-P178 + integrated-V_cont + package-v2 test-discovery execution, not a narrowly bounded P178 profile. Its declared purpose and actual execution scope are inconsistent. The automatic push trigger is incompatible with the discovered integrated synthetic producer calls unless those calls are deliberately included in an authorization decision. No such explicit per-run confirmation is present in this workflow.

**Design requirement before further execution:** either (a) restrict P178 test commands and replay to explicitly named P178 test modules and the exact P178 source closure, or (b) retain the broad suite only under a separately explicit synthetic-execution authorization and complete dependency lock. This gate does not choose or implement either correction.

### EP-02 — Legacy integrated synthetic harness suite

**Workflow:** .github/workflows/c10-s-focal-harness-tests.yml  
**Declared purpose:** integrated synthetic contract tests.  
**Trigger:** manual dispatch only, with required boolean confirm_synthetic_test_execution, default false.  
**Job guard:** exact research branch and confirmation true.  
**Runner:** ubuntu-latest.  
**Checkout:** actions/checkout@v4, exact github.sha.  
**Python:** actions/setup-python@v5, python-version 3.12.  
**Dependencies installed:** numpy==2.3.5, scipy==1.17.0; no hash lock and no explicit JCS dependency installation.

**Commands:**
- Compile an explicit list of P178 and integrated harness files.
- Run unrestricted python -B -m unittest -v from the harness directory.
- After primary PASS, replay unrestricted unittest discovery from a clean archive of the entire harness directory plus the P178 calibration source and reference CSV.
- Capture stdout/stderr and upload the execution manifest.

**Actual test-discovery closure:** all test*.py modules in the harness directory, not only the compile list or integrated test module. It therefore includes legacy P178, integrated V_cont, benchmark protocol, capture, package serialization and package verifier tests. The explicit boolean gate does authorize the declared integrated synthetic suite, but the actual test command is broader than the workflow name and compile list. The missing explicit JCS installation is the same undeclared dependency problem as EP-01.

**Disposition:** EP-02 has a meaningful manual synthetic-execution confirmation and branch guard, but its test scope is implicit and wider than its name suggests. The future profile must explicitly enumerate all test modules intended to run and all dependencies they import. Do not infer a narrower test scope from the compile list.

### EP-03 — V_cont package-v2 pure capture/writer/verifier tests

**Workflow:** .github/workflows/c10-s-vcont-package-v2-pure-tests.yml  
**Declared purpose:** pure capture, package writer and independent verifier fixtures; no synthetic producer execution.  
**Trigger:** manual dispatch only.  
**Job guard:** exact research branch.  
**Runner:** ubuntu-latest.  
**Checkout:** actions/checkout@v4, exact github.sha.  
**Python:** actions/setup-python@v5, python-version 3.12.  
**Dependency:** requirements-vcont-v2.lock; installs rfc8785==0.1.4 with pip --require-hashes --only-binary=:all: and the declared wheel SHA-256.

**Compile list:** vcont_evidence_export.py, vcont_package_v2.py, vcont_package_v2_verify.py, test_vcont_capture_v2.py, test_vcont_package_v2_serialization.py, test_vcont_package_v2_verifier.py.

**Test command:** only the three named pure test modules.

**Resolved local source/import closure:**
- Test roots: test_vcont_capture_v2.py, test_vcont_package_v2_serialization.py, test_vcont_package_v2_verifier.py.
- Local modules: vcont_evidence_export.py, vcont_package_v2.py, vcont_package_v2_verify.py, vcont_benchmark_protocol.py, vcont_integrated_harness.py.
- External runtime dependency: rfc8785==0.1.4, hash-pinned by the lockfile.
- Python standard library modules imported by the above files.
- Inline deterministic test fixtures; no separately declared benchmark data file or producer input is passed by the workflow.

The writer and evidence-export modules define producer APIs, but the three selected pure test modules exercise fixture/capture/serialization/verifier boundaries and do not call the synthetic producer entry points. The independent verifier module does not import the writer module. This is the narrowest and best-delimited current profile.

**Residual runtime identity:** Python selector 3.12 does not identify a patch/build; the setup action is a mutable tag; ubuntu-latest is a mutable runner label; pip itself is not pinned; the resolved OS image, architecture and action implementation commits are not recorded.

**Disposition:** EP-03 is the current reference profile for pure package-v2 verification, with source/test module scope and the JCS wheel dependency substantially explicit. It is not producer execution, package generation, calibration, or scientific execution.

### EP-04 — Future authorized confirmatory producer/package operation

No current workflow was found that defines a complete, authorized confirmatory V_cont producer → capture → package operation. Gate 171/172 producer APIs exist in source, but their presence is not an execution profile and calling them requires applicable execution authority. Package-v2 writer/verifier pure tests do not establish producer execution.

**Disposition:** NOT REGISTERED / OPEN. Do not infer this profile from EP-02 or EP-03.

## 3. Profile comparison

| Dimension | EP-01 P178 | EP-02 Integrated suite | EP-03 Package-v2 pure | EP-04 Confirmatory |
|---|---|---|---|---|
| Trigger | Push + manual | Manual | Manual | None |
| Explicit synthetic confirmation | No | Yes | Not applicable; pure only | Must be governed |
| Test scope | Unrestricted discovery | Unrestricted discovery | Three named modules | Not defined |
| Producer calls in discovered tests | Yes, V_cont tests | Yes | No in selected tests | Intended |
| NumPy/SciPy | Direct version pins | Direct version pins | Not needed by selected test set | To be specified |
| JCS dependency | Imported by discovered tests, not installed explicitly | Imported by discovered tests, not installed explicitly | Hash-locked | To be specified |
| Source archive | Whole harness + P178 calibration files | Whole harness + P178 calibration files | Checkout only; explicit module commands | Not defined |
| Scientific execution | P178 Monte Carlo 27 × 10,000 | No benchmark Monte Carlo specified; synthetic contract tests | No | Not authorized |
| Source/runtime manifest | Absent | Absent | Absent | Open |

## 4. Canonical source-closure rules for the next manifest design

The later materialization manifest MUST be profile-specific and command-derived. It MUST NOT hash the entire repository indiscriminately or treat a workflow's compile list as the complete runtime closure.

For each profile and each command boundary, the manifest design must capture:

1. **Workflow identity:** repository, workflow path and blob SHA, workflow name, job ID/name, step ordinal/name, exact command/script and relevant environment/inputs.
2. **Checkout identity:** event commit, checkout action resolved implementation identity, checkout options, repository root/tree identity, sparse/path selection, submodule and LFS policy.
3. **Test/entrypoint roots:** exact script/module names and command-line arguments; for unittest, explicit module list or discovery root, pattern and top-level directory.
4. **Transitive local closure:** every imported local module and data/configuration file actually consumed, resolved against the exact commit. Dynamic imports and runtime path reads must be explicitly declared or detected; an incomplete closure must not PASS.
5. **External inputs:** exact CSV/data files, fixtures, schemas, environment-provided configuration and secrets references (record presence/identity policy, never secret values), network-fetched resources and their hashes or explicit absence.
6. **Dependencies:** direct and transitive distribution names/versions, wheel filename/platform tags/SHA-256, lockfile path/blob SHA, installer version and install flags.
7. **Runtime:** Python implementation, full version/build, executable identity, OS image/revision, architecture, relevant system libraries/toolchain, pip version and action implementation commits.
8. **Materialized bytes:** canonical relative path, entry type, executable/mode semantics, byte length and SHA-256 for actual file bytes consumed; preserve symlink identity and fail closed on unsupported special entries.
9. **Generated/untracked inputs:** declared creation step, producer command/source, exact post-generation hashes and the time boundary at which the target command consumes them. Undeclared generated/untracked inputs block closure.
10. **Execution association:** bind profile/manifest to exact workflow run, attempt, job, step, tested commit and output/artifact IDs through the independent GitHub evidence contract (Gates 195–197).

A manifest is not allowed to assert that a declared path was consumed merely because it was checked out or compiled. The profile contract must distinguish declared_input, materialized_input, observed_consumed_input and not_observed where appropriate. If the runtime cannot prove actual file consumption, the evidence must state that limitation rather than overclaim.

## 5. Authorization and scope corrections required before a future run

1. **EP-01:** do not treat the current P178 workflow as a bounded P178-only test profile. Its unrestricted test discovery includes integrated synthetic Generator tests and package tests. Its automatic push trigger therefore has a synthetic-execution authorization mismatch. Before any new EP-01 run, either explicitly authorize the entire discovered suite and install all its dependencies, or change the test invocation/trigger under a separately authorized workflow correction. No change is made by Gate 200.
2. **EP-01 and EP-02:** unrestricted discovery imports package-v2 tests that depend on rfc8785, while neither workflow installs the lockfile dependency. Declare a complete dependency set or narrow the test modules; do not rely on runner preinstallation.
3. **EP-02:** retain its explicit confirmation gate, but name the exact intended test modules and replay scope so that future test additions cannot silently expand execution.
4. **EP-03:** preserve the current exact allowlist and hash-locked JCS dependency; later improve runtime/action identity without changing the pure test boundary.
5. **EP-04:** do not create or dispatch until the source closure, runtime, authorization, evidence association and package companion requirements are governed.

These are static design findings and stop conditions. No workflow was dispatched or changed.

## 6. Relationship to existing package and evidence contracts

- Preserve Gate 164's exact 14-file package inventory.
- Preserve Gate 178/181/182 serialization, source-to-wire and writer/verifier boundaries.
- Preserve Gate 194-G/194-I configuration fingerprint semantics; do not fold source/runtime identity into the 28 configuration components.
- Preserve Gate 167's independent external producer-evidence boundary and Gates 195–197's source/run/attempt/artifact association.
- Preserve Gate 198's Git commit/root-tree identity as a separate committed-source locator.
- Reuse the D-OPS exact-byte manifest principle only for a profile-specific, independently recomputable file inventory.
- Do not create a second generic source-execution companion or add a fifteenth package file. Schema placement remains open under existing package governance.

## 7. Governance and repository observations

This gate is a research-branch design/reconciliation record only. It does not change canonical main, the scientific Core, RMA, Evidence→Claim Matrix, C10 claim state, authorization state, code, workflows or execution artifacts.

At inspection:
- research branch HEAD was f377bf9d4ac5718afdad2554111ce6f294742840;
- PR #116 was open and Draft, with head at that research commit;
- PR #116 base was research/c10-d1-protocol-draft, not main;
- canonical main remained at a8b83f4b3955bcb602f97adf0c4dc716a5123f8d.

The PR base is recorded as a repository-routing observation only. Gate 200 does not retarget or modify the PR because that is a separate governance action and no authorization to change its base was supplied.

## 8. Gate disposition and next step

**Gate 200: PROFILE RECONSTRUCTION COMPLETE / WORKFLOW SCOPE DISCREPANCIES IDENTIFIED / MANIFEST DESIGN NOT YET FROZEN.**

The registry distinguishes three existing profiles and one missing future profile. EP-03 is the best bounded current pure-test profile. EP-01 is materially broader than P178 and its automatic trigger can execute integrated synthetic producer tests without explicit confirmation. EP-01 and EP-02 also have an undeclared JCS dependency in their actual unittest discovery closure.

**Next operation:** prepare a minimal, governed correction proposal for EP-01/EP-02 test selection, trigger/authorization and dependency closure, while preserving historical workflows and evidence semantics. Do not dispatch either workflow. After command scopes are explicit and accepted, derive the canonical SHA-256 materialization manifest and deterministic vectors for each profile. No source or workflow edits are authorized by this gate.
