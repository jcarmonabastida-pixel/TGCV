# C10-S V_cont — Gate 184: CI execution boundary and workflow split

**Status:** GOVERNANCE DECISION APPLIED TO RESEARCH BRANCH — STATIC CONFIGURATION REVIEW ONLY  
**Branch:** `research/c10-s-consolidation-draft`  
**Decision:** Adopt Option A — separate pure v2 tests from integrated synthetic tests  
**Parent:** Gate 183 implementation preflight  
**Execution:** GitHub file operations and static reread only. No workflow dispatch, CI run, dependency installation, compilation, tests, synthetic generation, calibration, package build or scientific execution.

## 1. Decision

The user approved Option A (workflow split). This gate applies the decision on the research branch:

1. The legacy integrated harness workflow is no longer push-triggered.
2. Its only trigger is manual `workflow_dispatch`, with a required boolean confirmation `confirm_synthetic_test_execution`, default false.
3. The legacy job runs only when dispatch is on `research/c10-s-consolidation-draft` and the confirmation is true.
4. A dedicated pure V_cont package v2 workflow is added. It runs only an explicit list of v2 fixture-based test modules and never invokes the full unittest discovery suite.
5. The pure workflow is triggered by changes to the v2 capture/package/verifier source files, its five dedicated test modules, and the hash-locked JCS dependency file. It also supports manual dispatch.
6. Both workflows retain least-privilege `contents: read`.

This separates code changes from implicit execution of synthetic producers. Manual dispatch with explicit confirmation is a distinct execution authorization signal for the legacy workflow; it is not implied by a push or by the existence of the workflow.

## 2. Legacy integrated workflow

Updated file: `.github/workflows/c10-s-focal-harness-tests.yml`.

Changes:

- Removed all `push` triggers, including broad harness and calibration path filters.
- Retained only `workflow_dispatch`.
- Added required boolean input `confirm_synthetic_test_execution`, default false.
- Job-level guard requires:
  - event is `workflow_dispatch`;
  - ref is exactly `refs/heads/research/c10-s-consolidation-draft`;
  - confirmation input is true.
- Existing compile, full unittest, clean-source replay and provenance capture steps are retained.

The workflow's test body is still an integrated synthetic execution suite. It is not reclassified as a pure software test. If dispatched without confirmation or from another ref, its job is skipped.

## 3. Dedicated pure v2 workflow

New file: `.github/workflows/c10-s-vcont-package-v2-pure-tests.yml`.

Push trigger is restricted to the research branch and these paths:

- `requirements-vcont-v2.lock`;
- `vcont_evidence_export.py`;
- `vcont_package_v2.py`;
- `vcont_package_v2_verify.py`;
- `test_vcont_capture_v2.py`;
- `test_vcont_package_v2_serialization.py`;
- `test_vcont_package_v2_verifier.py`;
- `test_vcont_package_v2_companions.py`;
- `test_vcont_package_v2_compatibility.py`.

It compiles only those modules and runs only the five named v2 test modules. It does not call `unittest discover`, does not compile/run `test_vcont_integrated_harness.py`, and does not run the legacy clean-source replay.

The test modules are planned files and do not yet exist. The pure workflow is therefore a forward trigger contract; it must not be considered runnable or passing until those modules and v2 source files are implemented. Any commit touching one of its path filters before the complete test set exists would fail closed as a missing-file error. Implementation must add the source and corresponding test modules atomically.

The pure tests may import typed source definitions needed for fixtures, but MUST NOT instantiate/call Generator, Sealer, Analyzer, Evaluator, `produce_and_capture_outer_world` or `produce_and_capture_benchmark`. A static import of a module containing these classes is not an execution; the pure suite must assert no producer invocation by construction.

## 4. JCS dependency lock

New file: `03_EXPERIMENTS/C10-S/harness/requirements-vcont-v2.lock`.

Pinned dependency:

- distribution: `rfc8785`
- version: `0.1.4`
- artifact: universal `py3-none-any` wheel
- SHA-256: `520d690b448ecf0703691c76e1a34a24ddcd4fc5bc41d589cb7c58ec651bcd48`
- license: Apache-2.0
- runtime dependencies: none, per package metadata
- install mode: `pip --require-hashes --only-binary=:all:`

The wheel hash and version are taken from the PyPI release record for rfc8785 0.1.4. PyPI reports no provenance attestation for this release. The hash pins the exact artifact bytes but does not authenticate its publisher. The implementation is a dependency selection, not an independent conformance result.

Before accepting the JCS layer, the pure v2 suite must execute RFC 8785 conformance vectors independently covering property ordering (including UTF-16 ordering), string escaping, Unicode, number serialization, negative zero, exponent formatting and rejection of non-finite values. Until those tests pass, JCS conformance remains NOT VERIFIED.

## 5. Authorization and scope boundaries

- The workflow split does not authorize either workflow to run now.
- No workflow was dispatched and no CI run was started.
- No dependency was installed; no compile or test command was executed.
- No Generator/Sealer/Analyzer/Evaluator or producer was invoked.
- No seed bank, calibration, package, benchmark or scientific experiment was generated.
- No scientific contract, estimand, DGP, N/M/R, assignment mechanism, claim or canonical state was changed.
- `main`, canonical RMA, Evidence→Claim Matrix, STATUS and PR base remain untouched.
- PR #116 remains Draft; this gate does not change PR readiness.

## 6. Static acceptance checklist

| Check | Result |
|---|---|
| Legacy workflow has no push trigger | PASS — static file review |
| Legacy job requires manual dispatch | PASS — static file review |
| Legacy job requires explicit boolean confirmation | PASS — static file review |
| Legacy job restricted to research branch | PASS — static file review |
| Pure workflow uses explicit v2 test module list | PASS — static file review |
| Pure workflow avoids integrated test discovery | PASS — static file review |
| Pure workflow path filters include lock/source/test files | PASS — static file review |
| JCS dependency version and wheel hash pinned | PASS — manifest declaration |
| JCS conformance vectors executed | NOT EXECUTED |
| Pure workflow executed | NOT EXECUTED |
| Legacy synthetic workflow executed | NOT EXECUTED |
| Scientific execution | NOT AUTHORIZED / NOT EXECUTED |

**Overall:** `GOVERNANCE DECISION APPLIED — WORKFLOW SPLIT STATICALLY CONFIGURED; EXECUTION NOT PERFORMED`.

## 7. Next operation — Gate 185

Gate 185 should implement the pure capture primitives and their fixture-only tests, including the RFC 8785 conformance vectors. The implementation commit must include all test modules named by the pure workflow path filters, or otherwise adjust the workflow atomically so it cannot trigger against missing files. No integrated producer test or scientific execution is authorized by Gate 184.

## 8. Corrective configuration record — YAML parse defect

After the first push, GitHub recorded seven failed workflow-run entries for the new pure workflow, each with **zero jobs**. The failure was in workflow configuration parsing, not in the test command: the unquoted plain-scalar pip command contained the :all: token followed by whitespace, which made the YAML invalid.

The command was quoted in commit 84d6e4695e7e94f694ca5bb40125a81c8936eefe. The corrected workflow was fetched back from the branch and parsed successfully with a YAML parser. No job was present in any of the seven failed runs, and no dependency installation, compilation, test, producer or scientific operation occurred.

This correction supersedes any reading of §5/§6 that might imply no workflow-run records were created. Accurate state: push events created failed configuration-only run records with zero jobs; no workflow job executed. The corrected workflow file has not yet been executed.
