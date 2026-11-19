# C10-S F1 — V003 pre-execution readiness record 005

**Status:** SOURCE AND WORKFLOW PREPARED — AUTHORIZATION DRAFT — NO NUMERICAL EXECUTION  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Frozen source commit:** `e526acb04e1d2c2421fa2663a43e31b537985522`  
**Main head verified unchanged:** `e22928eb79adb5bc74295967a45b9c440b78f849`

## 1. Frozen v003 source

Freeze manifest:
- Path: `03_EXPERIMENTS/C10-S/harness/C10S_F1_NUMERICAL_STRESS_FREEZE_MANIFEST_005.md`
- Commit: `72458c5cca7daf53ef492b936c570b9ba7def41d`
- Blob: `aabe552fa3e9d5524c31db6e6a41b97dff01ff45`

Frozen inputs:
- Path: `03_EXPERIMENTS/C10-S/harness/C10S_F1_N4_V002_FROZEN_INPUTS_001.json`
- Blob: `413e96c5478381ac615f3d44dd8a30a41d88513f`
- Source artifact: v002 run `44545538187`, artifact `14541730681`.
- Source JSONL SHA-256: `b350693e3e8f492ccb179631a703c45a6af45d661b21a033f280c0546fcc9a26`.

Generator blob: `fe43d0252f4a56d93b187091680fa16bca21a13d`  
CLI blob: `177838e6fc6baaacca004f0d2179fd50c1ddd7a1`  
The exact transitive v001/v002/isolator blobs are recorded in Freeze Manifest 005.

## 2. Dedicated workflow

- Workflow: `.github/workflows/c10s-f1-numerical-stress-v3.yml`
- Workflow blob: `85ffcb58d1859a3621dcd29a7b1c479c08a75b27`
- Source checkout is pinned to the immutable v003 source commit.
- Preflight verifies the authorization, manifest blob, workflow blob, frozen-input blob, exact source blobs, 79-record scope including the N4 isolation width (1/10^12) and max depth (256), runtime, command, output contract, one-shot limit, unused retry state and prohibitions. A static review found these two N4 scope fields and retry_authorized=false were not explicitly checked in the first workflow draft; the preflight was tightened before any approval or numerical execution.
- Authorization consumption occurs only after source/blob preflight and immediately before the single primary diagnostic invocation.
- No external Python dependencies are installed.

Workflow registration/admission checks:
- Run `44548521641`: `completed / skipped`.
- Run `44548562180`: `completed / skipped`.
- Run `44548599419`: `completed / skipped`.
- These were push-triggered workflow admission checks without the approval marker. Jobs did not execute; no numerical runner or artifact was produced.

## 3. Authorization 005

- File: `00_GOVERNANCE/authorizations/C10S_F1_NUMERICAL_STRESS_AUTHORIZATION_005.json`.
- ID: `C10S-F1-NUMERICAL-STRESS-20261119-005`.
- State: `DRAFT`.
- `execution_authorized=false`.
- `approved_by_user=false`.
- `consumed=false`.
- `attempt_closed=false`.
- `retry_authorized=false`.
- Exact manifest, workflow, source commit and frozen-input blobs are pinned.

Proposed one-shot scope:
- 64 N2 discriminant-proximity ULP records;
- 1 N5 exact rounding-cell diagnostic;
- 14 N4 Fujiwara-bound comparisons;
- 79 total records;
- CPython 3.12.3 on ubuntu-24.04, standard library only;
- one primary execution, zero retries, no replay, 15-minute timeout.

Explicit exclusions: unit tests, bytecode compilation, Monte Carlo calibration, DGP experiment, inferential coverage, parameter tuning, external data, source changes during execution, scientific C10-S execution and causal/value claims.

## 4. Static review and execution boundary

- Design v003: DEFINED.
- Implementation v003: IMPLEMENTED.
- Source-level review: CONDITIONAL; private v001/v002 helpers are blob-pinned.
- Imports/compilation/tests: NOT EXECUTED.
- Numerical diagnostics: NOT EXECUTED.
- Monte Carlo calibration: NOT AUTHORIZED.
- Scientific C10-S execution: NOT AUTHORIZED.
- Authorization 005: DRAFT, not approved or consumed.

The previous v002 final execution-result audit remains INDETERMINATE because replay was prohibited. V003 neither replays nor waives that gate.

Fresh explicit user approval is required for this exact authorization. Any change to the frozen source, input, workflow, runtime, command or scope invalidates the prepared authorization and requires reconciliation.
