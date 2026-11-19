# C10-S F1 — V002 pre-execution readiness record 004

**Status:** SOURCE SNAPSHOT AND WORKFLOW PREPARED — AUTHORIZATION DRAFT — NO NUMERICAL EXECUTION  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Branch head at record:** `5ec22b73e2b62d86868906e2fca764bb7c2dc0a7`  
**Main head at record:** `e22928eb79adb5bc74295967a45b9c440b78f849` (unchanged during this operation)

## 1. Frozen source snapshot

- Source commit: `a42351e374e3624a498b11199cea45cd0dc20c09`.
- Freeze manifest: `03_EXPERIMENTS/C10-S/harness/C10S_F1_NUMERICAL_STRESS_FREEZE_MANIFEST_004.md`.
- Freeze manifest blob: `a25828d42732ea345dd36c623fd384c6218d54d8`.
- Manifest commit: `7a73dc22cf6f4226cb6e7c0c8fe2dea28b767f6d`.
- The v002 source and all transitive numerical source blobs were re-read at the exact source commit and matched the manifest inventory.

## 2. Dedicated workflow

- Workflow: `.github/workflows/c10s-f1-numerical-stress-v2.yml`.
- Workflow blob: `f5fd3ebe2570e371b97d139f64be10c333b62df5`.
- The workflow checks exact branch, one-shot authorization, manifest/workflow blob identity, source commit, scope, record counts, runtime pins, exact command, outputs, limits and prohibitions.
- It checks out the immutable source commit and verifies the v002 and transitive source blobs before dependency installation and authorization consumption.
- It consumes the one-shot authorization immediately before the primary numerical command.
- It enforces 131 + 7 + 14 = 152 records in the CLI and uploads canonical records, summary, manifest and runner captures.

Structural workflow registration check:
- Run `44544590055`: `completed / skipped`.
- Job `numerical-stress-v2`: `completed / skipped`.
- No runner steps executed; no artifacts produced.
- This is only a workflow parsing/admission-gate check, not a numerical execution or test result.

## 3. Authorization 004

- File: `00_GOVERNANCE/authorizations/C10S_F1_NUMERICAL_STRESS_AUTHORIZATION_004.json`.
- ID: `C10S-F1-NUMERICAL-STRESS-20261119-004`.
- State: `DRAFT`.
- `execution_authorized=false`.
- `approved_by_user=false`.
- `consumed=false`.
- `attempt_closed=false`.
- Workflow blob and freeze-manifest blob match the exact values above.
- Authorization 003 remains `CONSUMED` and `attempt_closed=true`; it cannot be reused.

## 4. Exact scope proposed

- 131 polynomial/Sturm records, including the historical 115 plus 16 near-double ULP perturbations;
- 7 N3 covariant variable-scale records;
- 14 N4 observation-scale records;
- 152 total records;
- Python 3.12.3, NumPy 2.1.3, SciPy 1.14.1, ubuntu-24.04;
- one primary execution, no automatic retries, no replay, 15-minute timeout.

Explicitly excluded: unit tests, bytecode compilation, Monte Carlo calibration, DGP experiments, inferential coverage, parameter tuning, external datasets, source modifications during execution and scientific C10-S execution.

## 5. Final boundary

No v002 Python module was imported, compiled or executed. No v002 numerical record exists. No calibration or scientific C10-S experiment was run.

The only remaining gate before the proposed one-shot numerical execution is fresh explicit user approval of authorization 004. Approval must be applied to that exact authorization and exact frozen workflow/source snapshot. Any intervening change to the source, manifest or workflow invalidates the prepared authorization and requires reconciliation.
