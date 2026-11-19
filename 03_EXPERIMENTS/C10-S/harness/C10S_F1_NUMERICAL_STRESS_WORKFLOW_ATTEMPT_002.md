# C10-S F1 — Numerical Stress Workflow Attempt 002

**Status:** BLOCKED BEFORE JOB CREATION — NO PRIMARY RUNNER EXECUTION  
**Authorization:** C10S-F1-NUMERICAL-STRESS-20261119-002  
**Authorization commit:** 85b0ae622d004fe4961abc08961dc211bebdb9e5  
**Observed Actions run:** 44531064922  
**Run URL:** https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44531064922  
**Frozen numerical source:** d5edc0010f7a8c6587677eb2004b545367fc4b35  
**Intended workflow:** .github/workflows/c10s-f1-numerical-stress-002.yml  
**Observed workflow:** .github/workflows/c10s-f1-numerical-stress-001.yml

## 1. What happened

The user requested a retry after attempt 001 had been closed. A separate authorization 002 was created with a new one-shot ID and approval marker. A second workflow definition, c10s-f1-numerical-stress-002.yml, was committed and its Git blob was recorded in the authorization.

The authorization commit triggered GitHub Actions run 44531064922. GitHub selected the legacy workflow path c10s-f1-numerical-stress-001.yml, not the intended workflow 002. The legacy workflow's job-level condition is bound to authorization marker 001, so it does not admit authorization 002.

Observed run metadata:
- event: push;
- head commit: 85b0ae622d004fe4961abc08961dc211bebdb9e5;
- selected workflow: .github/workflows/c10s-f1-numerical-stress-001.yml;
- status: completed;
- conclusion: failure;
- run attempt: 1;
- jobs: 0;
- artifacts: 0.

No run for workflow 002 was observed for the authorization commit.

## 2. Execution boundary

The new authorization was not consumed. No Actions job was created. The frozen source checkout, runtime setup, dependency installation, numerical CLI, stress runners and evidence writer were not invoked.

Therefore no 115 polynomial/Sturm records or seven F1 scale records exist from this attempt. No numerical result can be inferred.

## 3. Diagnosis

The immediate routing mismatch is established: the authorization-002 push was handled by legacy workflow 001, whose job condition accepts only marker 001. The reason GitHub did not select the newly added workflow 002 is NOT ESTABLISHED from the available run metadata. No unsupported claim about YAML validity, branch registration or GitHub internals is made.

## 4. Authorization disposition

Authorization 002 is closed as BLOCKED_PRE_EXECUTION:
- execution_authorized=false;
- consumed=false;
- attempt_closed=true;
- retry_authorized=false.

The approval is not reusable. No workflow rerun, replay, second trigger or alternate execution route is authorized by this record.

## 5. Next permitted work

Only static workflow discovery/registration diagnosis and governance-safe correction remain in scope. The next solution must not rely on an unverified branch-local workflow being selected. It must establish, before any new authorization, which workflow GitHub will actually execute and how its exact identity is pinned. Any later primary runner invocation requires a new one-shot authorization and fresh explicit user approval.

The frozen numerical source remains unchanged.
