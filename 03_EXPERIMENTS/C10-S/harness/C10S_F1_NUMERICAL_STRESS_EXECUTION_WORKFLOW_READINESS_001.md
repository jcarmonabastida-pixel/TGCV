# C10-S F1 — Numerical Stress Execution Workflow Readiness 001

**Status:** WORKFLOW IMPLEMENTED — AUTHORIZATION DRAFT — NOT DISPATCHED  
**Branch:** research/c10s-f1-integrated-correction-20261119  
**Frozen source commit:** f19ae92bed172f502cceb89fd26e86b5e37c5227

## 1. Workflow

Workflow path: .github/workflows/c10s-f1-numerical-stress-001.yml  
Workflow Git blob: 85cb705d5d51eb4bb3e768984aa2aec7f9da9829

Trigger: push to the research branch that changes only the one-shot authorization record. The job proceeds only when the approval commit message contains:

AUTHORIZE-C10S-F1-NUMERICAL-STRESS-20261119-001

A draft or unapproved authorization does not satisfy the job condition. The workflow is not dispatched or run by this implementation operation.

## 2. Fail-closed controls

Before execution, the workflow requires:
- exact research branch;
- approval marker in the triggering commit message;
- authorization status APPROVED;
- execution_authorized=true and approved_by_user=true;
- consumed=false and one_shot=true;
- exact source commit and freeze-manifest path, commit and blob;
- exact runtime, command, record counts, limits and exclusions;
- exact Git blob identities for the stress generator, CLI, F1 solver, Sturm isolator, adjudicator and transitive observed-data interface.

The workflow checks out the authorization branch separately from the detached frozen source snapshot. It installs only NumPy 2.1.3 and SciPy 1.14.1 under CPython 3.12.3 on ubuntu-24.04.

Immediately before the primary runner command, it atomically consumes the one-shot authorization by committing status CONSUMED, consumed=true, run ID and UTC timestamp to the authorization branch. The authorization is not reusable if the run subsequently fails. No replay or automatic retry is configured.

The workflow captures preflight provenance, runner stdout/stderr, exit code and the three canonical evidence files, and uploads the resulting directory as a GitHub Actions artifact.

## 3. Authorization state

Authorization ID: C10S-F1-NUMERICAL-STRESS-20261119-001  
Authorization path: 00_GOVERNANCE/authorizations/C10S_F1_NUMERICAL_STRESS_AUTHORIZATION_001.json  
Authorization Git blob: fc0431f18f7689a43390728ff43881f204f476b4

Current fields:
- status = DRAFT
- execution_authorized = false
- approved_by_user = false
- consumed = false

Therefore the workflow is **not authorized to execute**.

## 4. Frozen identities

| Artifact | Identity |
|---|---|
| Source commit | f19ae92bed172f502cceb89fd26e86b5e37c5227 |
| Freeze manifest 002 commit | 5463e5662f9095267369601789ccf541627893f6 |
| Freeze manifest 002 blob | 8c1fbd0681e784148646c97bbc07d5ca78bf0e22 |
| Stress generator blob | 80ff414e076b06de14ea1190dd9e877b6045b88f |
| CLI runner blob | b08ee28a1423b7a6c598db69c0ef15dff5f0ac22 |
| F1 solver blob | 39f1732e1571f9d0705378d924b58b9475277e7a |
| Sturm isolator blob | 3ac9ce31eb82421022fd8d2a65a0daee049322be |
| Adjudicator blob | 9fa1cb21cd47e32030db8a00420e7dacfdc77321 |
| Observed-data interface blob | 6d193798e792dd5129fbfb0c312286763791d463 |

## 5. Operational boundary

No tests, compilation, smoke tests, stress runner, evidence writer, calibration, DGP experiment or scientific C10-S execution has been performed as part of this workflow preparation.

The next operation requiring user input is explicit approval of this exact one-shot authorization. If approved, the authorization record must be changed to APPROVED and execution_authorized/approved_by_user set true in a commit whose message contains the exact marker above. That commit itself triggers the workflow. Without that explicit approval, no execution is permitted.
