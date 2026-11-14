# C10-S V_cont — Gate 183: package v2 implementation preflight

**Status:** CONDITIONAL / BLOCKED FOR IN-BRANCH IMPLEMENTATION UNTIL CI EXECUTION BOUNDARY IS GOVERNED  
**Branch inspected:** research/c10-s-consolidation-draft  
**Canonical governance inspected:** main  
**Parent:** Gate 182 integrated implementation contract  
**Scope:** static dependency, source-layout, workflow-trigger, test-execution and file-by-file implementation preflight  
**Execution:** GitHub source inspection only. No code imports, compilation, tests, CI dispatch, workflow run, dependency installation, synthetic generation, calibration, package creation or scientific execution.

## 1. Disposition

Gate 182's code architecture is implementable in principle, but the preflight finds a material execution-governance blocker:

**A push changing any file under 03_EXPERIMENTS/C10-S/harness/** automatically triggers c10-s-focal-harness-tests.yml, which runs the entire unittest suite. The integrated V_cont tests instantiate Generator and call Generator.generate(...), and the test module invokes both produce_and_capture_outer_world and produce_and_capture_benchmark. Therefore, an ordinary code commit for the v2 implementation would automatically execute synthetic generation and benchmark-producing test paths.**

This conflicts with the current authorization boundary: technical tests and especially synthetic producer invocation have not been authorized. The current workflow is not a pure static/serializer-only suite. Gate 183 therefore does NOT authorize code changes to the harness branch, because a push would trigger an execution that cannot be safely assumed authorized.

No workflow trigger has been changed in this gate. Changing CI triggers or splitting tests requires an explicit governance change and review of the execution semantics.

## 2. Governance recovery

Read from GitHub main:

- 00_GOVERNANCE/README.md — GitHub main is canonical; historical reconstruction mandatory; technical execution must follow the governed sequence; execution authorization must be explicit; state categories must not be conflated.
- 00_GOVERNANCE/CHATGPT_BOOTSTRAP.md — canonical state pointers and no execution authorization for the current recovery/design operation.
- STATUS.md — RMA v3.38 and Evidence→Claim Matrix v1.47; C10 downstream value linkage remains open; no authorization to run a new C10-S experiment.

The Gate 182 implementation contract remains on the research branch. This preflight is a research-branch audit artifact only and does not change canonical main, scientific status or PR base.

## 3. Dependency and source-layout findings

### 3.1 No harness dependency lock or project manifest

The exact harness directory listing contains source, tests and Markdown records, but no requirements.txt, pyproject.toml, pytest.ini or equivalent lock/manifest. The repository root has no dependency manifest either. Existing workflows install NumPy 2.3.5 and SciPy 1.17.0 directly with pip.

There is no pinned RFC 8785/JCS dependency, version, wheel hash or dependency-lock artifact in the inspected source tree. Gate 182 §5 remains an unmet prerequisite. Do not select a package/version or claim conformance solely from a name; the chosen artifact and RFC 8785 vector results must be recorded before implementation.

### 3.2 Existing module and test layout

Current V_cont files:

- vcont_integrated_harness.py — Generator, Sealer, Analyzer, Evaluator and aggregation.
- vcont_benchmark_protocol.py — scenario/seed/matrix protocol.
- vcont_evidence_export.py — immutable RUN/R and M capture plus benchmark-wide producer.
- test_vcont_integrated_harness.py — existing integrated harness suite.
- test_vcont_benchmark_protocol.py — protocol suite.

There is no existing v2 package writer/verifier module and no JCS package dependency lock.

### 3.3 Existing workflow behavior

.github/workflows/c10-s-focal-harness-tests.yml:

- triggers on push to research/c10-s-consolidation-draft for every path under 03_EXPERIMENTS/C10-S/harness/**;
- also exposes workflow_dispatch;
- uses contents: read;
- sets up Python 3.12 and installs NumPy/SciPy;
- compiles the harness and test files;
- runs python -B -m unittest -v;
- on success, runs a clean-source archive replay of the same suite.

The workflow is not scoped to the P178-only focal files; it compiles and executes the integrated V_cont test module.

Static call-site inspection of test_vcont_integrated_harness.py found direct calls to Generator.generate and calls to produce_and_capture_outer_world and produce_and_capture_benchmark. Those test methods create synthetic observations. They are not limited to pure serialization fixtures.

The other P178 Monte Carlo/replay workflows also exist, but the decisive blocker is the broad harness-path push trigger in the focal contract workflow. This gate does not dispatch or modify any workflow.

## 4. File-by-file implementation plan after blocker resolution

Implementation order, preserving Gate 182's module boundaries:

| Order | File | Change | Execution dependency |
|---|---|---|---|
| 0 | New dependency lock under harness | Pin Python version, RFC 8785 implementation/version and artifact hash; record conformance vectors | Dependency installation and isolated JCS tests require explicit technical authorization |
| 1 | vcont_evidence_export.py | Add MatrixCapture, FrozenReportSnapshot, additive CapturedBenchmark fields, pure capture/fingerprint/identity helpers | Pure fixture tests; producer integration excluded |
| 2 | vcont_evidence_export.py | Capture exact matrix before Evaluator and report immediately after Evaluator | Editing producer is allowed only after CI trigger is governed; invoking it remains separately unauthorized |
| 3 | New vcont_package_v2.py | Strict source projections, uint64 registry, effective-config projection, companion validation, JCS JSON and deterministic TAR | Fixed inline fixtures only |
| 4 | New vcont_package_v2_verify.py | Independent parser, canonical-byte check, schema/path/uint64/join/digest/provenance verification | Adversarial byte fixtures only |
| 5 | New focused test files | Capture, serialization, verifier, companions and v1/v2 compatibility tests | Must not invoke Generator, Sealer, Analyzer, Evaluator or producer |
| 6 | .github/workflows/c10-s-focal-harness-tests.yml or a new workflow | Split pure-v2 tests from the legacy integrated suite; explicit path triggers; ensure v2 workflow runs only fixture-based tests | Requires governance decision; no workflow change made here |
| 7 | Existing integrated test suite | Run only under separate explicit authorization because it generates synthetic observations and invokes benchmark producers | Explicit authorization required |

No test should import or execute the producer as an incidental module-level side effect. The pure v2 suite should be independently runnable by a dedicated workflow. A later producer-integration test is a distinct execution class and must remain disabled until authorized.

## 5. Required CI/governance resolution before any harness code push

One of the following must be explicitly selected and persisted before changing files under the harness path:

**Option A — workflow split (recommended):**
1. Add a dedicated pure-v2 workflow triggered by v2 module/test/dependency paths.
2. Change the existing broad workflow so pure-v2 file changes do not invoke the integrated synthetic suite; preserve its execution for the legacy harness only when explicitly triggered or separately governed.
3. Keep producer integration and all Generator/Sealer/Analyzer/Evaluator tests behind manual, separately authorized execution.
4. Verify that a push containing only v2 pure code/tests cannot invoke the synthetic producer workflow.

**Option B — isolated implementation branch:**
1. Implement on a separate branch not matched by the existing branch-specific push trigger.
2. Run only pure fixture tests after explicit authorization.
3. Before merge/cherry-pick into research/c10-s-consolidation-draft, resolve the workflow trigger and obtain authorization for any resulting run.

Option B only postpones the trigger; it does not resolve it for eventual integration. Option A is the sustainable route, but requires an explicit governance decision because it changes CI execution behavior.

## 6. Scope controls

- Do not modify Generator, Sealer, Analyzer, Evaluator, DGP, estimands, seed derivation or M/R assignment logic.
- Do not change main, canonical RMA, Evidence→Claim Matrix, STATUS or scientific claim status.
- Do not alter Gate 164 v1 or historical fingerprint algorithms.
- Do not run tests, compile, install dependencies, dispatch workflows, invoke producers, generate seeds, calibrate, package benchmark outputs or conduct scientific execution under this gate.
- Do not infer that a push-triggered workflow is authorized merely because a code change is authorized.
- No PR base change or PR readiness transition.

## 7. Gate 183 result

| Check | Result |
|---|---|
| Governance/bootstrap recovery | PASS — read-only |
| Harness source/test inventory | PASS — static |
| Dependency lock exists | FAIL — absent |
| RFC 8785 dependency pinned | FAIL — absent |
| Pure v2 package modules exist | FAIL — not implemented |
| Existing broad push workflow identified | PASS — blocker |
| Existing integrated tests are pure | FAIL — Generator and producer calls present |
| Safe in-branch code push under current workflow | BLOCKED |
| CI workflow split authorized | NOT AUTHORIZED |
| Technical tests / CI | NOT EXECUTED |
| Synthetic producer / scientific execution | NOT AUTHORIZED / NOT EXECUTED |

**Overall status:** CONDITIONAL — IMPLEMENTATION ARCHITECTURE DEFINED; BLOCKED PENDING CI EXECUTION-BOUNDARY DECISION AND PINNED JCS DEPENDENCY.

## 8. Next operation — Gate 184

Gate 184 should resolve the CI execution boundary as a governance change before implementation. It should define which existing test paths are pure software checks and which invoke synthetic data generation, then establish a dedicated pure-v2 workflow with no producer imports/calls. The JCS dependency and its artifact identity can then be pinned. Only after these conditions are persisted should implementation begin.

This gate does not request or imply authorization for synthetic producer execution, calibration, seed generation, Monte Carlo execution or scientific experimentation.

## Gate 184 — resolution of the CI execution-boundary blocker

The user approved Option A. Gate 184 applies the workflow split on the research branch:

- the legacy integrated workflow no longer has push triggers and requires manual dispatch, explicit boolean confirmation, and the exact research branch;
- a dedicated pure v2 workflow uses an explicit list of fixture-only test modules and never invokes full unittest discovery;
- the pure workflow is path-filtered to the v2 capture/package/verifier sources, dedicated tests and hash-locked JCS dependency;
- `rfc8785==0.1.4` is pinned to the PyPI universal wheel SHA-256 `520d690b448ecf0703691c76e1a34a24ddcd4fc5bc41d589cb7c58ec651bcd48`.

The pure test modules are not implemented yet; the workflow is a forward contract and is not runnable/passing until the complete source/test set is added atomically. JCS conformance vectors remain unexecuted. No workflow was dispatched and no test, dependency installation, compilation, synthetic generation or scientific execution occurred. See Gate 184 for exact configuration and limitations.
