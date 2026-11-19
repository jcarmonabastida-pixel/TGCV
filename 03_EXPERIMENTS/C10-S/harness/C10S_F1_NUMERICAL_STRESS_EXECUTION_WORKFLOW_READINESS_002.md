# C10-S F1 — Numerical Stress Execution Workflow Readiness 002

**Status:** WORKFLOW ATTEMPT 001 FAILED BEFORE JOB CREATION — AUTHORIZATION CLOSED — NO NUMERICAL EXECUTION  
**Branch:** research/c10s-f1-integrated-correction-20261119  
**Frozen source commit:** d5edc0010f7a8c6587677eb2004b545367fc4b35

## 1. Frozen execution package

- Freeze manifest: C10S_F1_NUMERICAL_STRESS_FREEZE_MANIFEST_003.md
- Freeze manifest commit: aa30ab98eae2f8d505d569149aa4b342d32718bd
- Freeze manifest blob: d54aec3adaca0eef95d529a987dfb28a294119b3
- Stress generator blob: cc047a3b112caf84533c94e77d1908c99a0c2bdf
- CLI runner blob: b08ee28a1423b7a6c598db69c0ef15dff5f0ac22
- F1 solver blob: 39f1732e1571f9d0705378d924b58b9475277e7a
- Sturm isolator blob: 3ac9ce31eb82421022fd8d2a65a0daee049322be
- Adjudicator blob: 9fa1cb21cd47e32030db8a00420e7dacfdc77321
- Observed-data interface blob: 6d193798e792dd5129fbfb0c312286763791d463

## 2. Workflow controls

Workflow: .github/workflows/c10s-f1-numerical-stress-001.yml  
Workflow blob: 6b0fde557f2b2a2a1a72f34c3543226f8c1dc14a

The workflow triggers only on a change to the one-shot authorization JSON on the research branch, and only when the triggering commit message includes:

AUTHORIZE-C10S-F1-NUMERICAL-STRESS-20261119-001

The workflow requires status APPROVED, execution_authorized=true, approved_by_user=true, consumed=false, exact source/freeze identities, the exact command, runtime, scope, limits and exclusions. It checks the frozen source commit and every executable/transitive source Git blob before setting up the runtime.

It consumes the authorization in a branch commit immediately before the primary runner invocation. The consumption commit records run ID and UTC time. No retry or replay is configured. Evidence includes the preflight record, stdout, stderr, exit code and canonical JSONL/summary/hash-manifest files.

## 3. Authorization record

Path: 00_GOVERNANCE/authorizations/C10S_F1_NUMERICAL_STRESS_AUTHORIZATION_001.json  
Current blob: 1d36028348a2e0e1417e02e71f2b129bfd1d259a  
Authorization ID: C10S-F1-NUMERICAL-STRESS-20261119-001

Current state after explicit approval and failed workflow attempt 001:
- status = BLOCKED_PRE_EXECUTION
- execution_authorized = false
- approved_by_user = true (approval recorded; attempt subsequently closed)
- consumed = false (primary runner was never reached)
- attempt_closed = true
- retry_authorized = false

The command arguments are bound to frozen source commit d5edc0010f7a8c6587677eb2004b545367fc4b35. The workflow and authorization agree on the source, freeze manifest and exact runner command.

## 4. Execution state

No tests, compilation, smoke tests, stress runners, evidence writer, Monte Carlo calibration, DGP experiment or scientific C10-S execution has been performed during workflow preparation.

**No execution is authorized.** Explicit user approval is required before changing the authorization to APPROVED and committing it with the exact approval marker. That commit triggers the one-shot workflow; the workflow then consumes the authorization before executing.
