# C10-S V_cont — Gate 197: run-attempt and artifact association resolution

**Status:** API ATTEMPT RESOLUTION VERIFIED; ARTIFACT↔ATTEMPT ASSOCIATION POLICY DEFINED FAIL-CLOSED; MULTI-ATTEMPT LIVE VECTOR NOT OBSERVED  
**Branch:** research/c10-s-consolidation-draft  
**Parent:** Gate 196 — GitHub Actions API contract and artifact-digest audit  
**Scope:** Read-only inspection of existing GitHub Actions runs, attempt-specific endpoints, attempt-specific jobs, artifact metadata and existing workflow definitions. No workflow was launched or rerun. No producer or scientific code was executed.

## 1. Question

Can the adapter independently resolve a concrete (repository, workflow, run_id, run_attempt, artifact_id) tuple, and what evidence is sufficient to assert that a given artifact belongs to that exact attempt?

The key distinction is between resolving the attempt itself from GitHub, resolving the artifact itself from GitHub, and proving the artifact was produced by that attempt. These are separate assertions and must not collapse into one boolean.

## 2. Live attempt endpoint verification

The documented endpoint was called successfully for both existing Gate 196 samples:

GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}?exclude_pull_requests=true

| Run | Attempt queried | API result | Returned run_attempt | previous_attempt_url |
|---|---:|---|---:|---|
| 43412059150 | 1 | HTTP 200 | 1 | null |
| 43411488324 | 1 | HTTP 200 | 1 | null |
| 43412059150 | 2 | HTTP 404 | — | — |

The 404 for attempt 2 is the expected negative result for a run whose current run_attempt is 1; it is not evidence of an API defect. The earlier apparent endpoint failure arose from a batched call in which the nonexistent attempt 2 request failed the batch. The attempt 1 endpoint itself is live-verifiable.

The exclude_pull_requests=true query parameter was included in successful direct calls. The response retained the exact run ID, workflow ID/path, head SHA, run number, event, status/conclusion, run_attempt, run_started_at and other run metadata.

**Conclusion:** the attempt-specific run endpoint is both documented and live-observed in this repository for attempt 1. Gate 196's live-observation limitation is superseded for these sample attempts.

## 3. Attempt-specific jobs verified

For both runs, the corresponding attempt-specific jobs endpoint was called:

GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs?per_page=100

| Run | Attempt | Job ID | Job run_attempt | Job conclusion | Upload-artifact step |
|---|---:|---:|---:|---|---|
| 43412059150 | 1 | 131840643599 | 1 | success | step 9, success |
| 43411488324 | 1 | 131838734939 | 1 | failure | step 9, success |

The returned job objects explicitly include run_id, run_attempt, head_sha, job start/completion timestamps, and per-step names/status/timestamps. Thus the attempt identity can be cross-checked at both run and job levels.

For Sample A, the upload step ran 10:49:46–10:49:48 UTC and the artifact metadata reports creation at 10:49:48 UTC. For Sample B, the upload step ran 10:45:19–10:45:20 UTC and the artifact metadata reports creation at 10:45:20 UTC. This is temporal corroboration, not a direct artifact-ID-to-job foreign key.

## 4. What the API does and does not bind

Observed artifact metadata for both samples exposes numeric artifact ID, name and size, digest and expiry state, creation/update timestamps, and workflow_run.id, repository ID, head repository ID, branch and head SHA.

It does not expose run_attempt, a job ID, a step ID, or an independently documented foreign key from artifact ID to a specific attempt/job.

The attempt-specific jobs API exposes the attempt number and job/step timeline, but does not return the artifact ID created by the upload step.

Consequently, the available independent observations support two separate chains:

- artifact_id → artifact metadata → run_id + head_sha
- (run_id, attempt_number) → attempt response → attempt-specific jobs → job/step timeline

The two chains share the run ID and can be temporally corroborated. They do not currently join on an API-issued artifact-to-attempt key.

## 5. Normative fail-closed association policy

The adapter must represent three distinct resolution statuses.

### 5.1 ATTEMPT_RESOLVED

Set only when:
1. exact repository identity is resolved;
2. exact workflow run ID is fetched;
3. the requested attempt-specific endpoint returns successfully;
4. returned id, workflow_id, run_attempt, head_sha, workflow path and repository identity match the request and the expected source declaration;
5. attempt-specific jobs are fetched and their run_id, run_attempt and head_sha agree.

Failure or mismatch must not be downgraded to a producer declaration.

### 5.2 ARTIFACT_RESOLVED

Set only when:
1. the exact numeric artifact ID is fetched;
2. repository identity, artifact ID, run ID, head SHA, expiry state, size and digest are captured;
3. exact ZIP bytes are downloaded and their size and SHA-256 are compared with GitHub metadata.

Artifact name is descriptive only and never an identity key.

### 5.3 ARTIFACT_ATTEMPT_ASSOCIATION

Use the following values:

- **DIRECTLY_VERIFIED:** only if GitHub supplies an independently observed artifact-to-attempt/job association (or a future equivalent cryptographically/structurally bound evidence source).
- **CORROBORATED_NOT_DIRECT:** run ID/head SHA agree, artifact creation time falls within the unique attempt's observed execution window, and the attempt-specific job timeline contains a successful upload step; however no API field directly joins artifact ID to that attempt.
- **UNVERIFIABLE:** attempt-specific data is missing, inaccessible, incomplete, ambiguous, or cannot be uniquely correlated.
- **MISMATCHED:** repository, run ID, head SHA, attempt, or timing observations conflict.

**Acceptance rule:** the adapter must not emit an overall externally verified SourceExecutionEvidence assertion that requires exact attempt binding when the association status is only CORROBORATED_NOT_DIRECT or UNVERIFIABLE. It may preserve the separate run, attempt, job and artifact observations and report the bounded correlation. A producer manifest field such as run_attempt, artifact name, or filename can never upgrade this association status.

A run with run_attempt=1 and no prior attempt is not automatically proof of artifact origin. It removes rerun ambiguity for the observed run history but does not create an artifact-ID-to-attempt API foreign key. Preserve that distinction.

## 6. Sample disposition

Both Gate 196 samples:
- resolve attempt 1 successfully;
- resolve attempt-specific jobs successfully;
- agree on run ID and head SHA across run, job and artifact metadata;
- show a successful artifact-upload step;
- have artifact creation timestamps coincident with the upload step's end;
- have previous_attempt_url=null and run_attempt=1.

Their disposition is therefore **CORROBORATED_NOT_DIRECT**, not DIRECTLY_VERIFIED. The repository sample contains no observed multi-attempt run in the first 1,000 listed workflow runs; this is a bounded search, not proof that the repository has never had a rerun.

No actual multi-attempt run vector was available in this pass. The resolver's behavior on a run with attempt 2+ remains a required integration test before any contract freeze.

## 7. Required schema changes to Gate 195

Keep separate nested observations, rather than a single producer-populated composite:
- workflow_run_observation
- workflow_attempt_observation
- attempt_jobs_observation
- artifact_metadata_observation
- artifact_download_observation
- artifact_attempt_association

Each observation must retain:
- exact API resource URL/path and retrieval time;
- repository identity and API version/header used;
- raw response digest or immutable response capture reference;
- relevant returned IDs and source SHA;
- explicit state: observed, absent, contradictory, or not verifiable.

The association object must retain the method and supporting observation IDs. It must never be silently derived from a producer declaration.

## 8. Evidence disposition

| Question | Result |
|---|---|
| Attempt-specific run endpoint documented? | DOCUMENTED |
| Attempt 1 endpoint live-tested for both samples? | PASS, 2/2 |
| Attempt-specific jobs endpoint live-tested? | PASS, 2/2 |
| Negative request for nonexistent attempt 2? | 404 as expected |
| Artifact metadata includes run ID/head SHA? | YES |
| Artifact metadata includes run_attempt/job ID? | NO |
| Temporal correlation with upload step? | YES, 2/2 |
| Direct artifact-ID-to-attempt API binding? | NOT EXPOSED |
| Multi-attempt live test vector? | NOT AVAILABLE |
| Overall attempt/artifact exact association? | NOT DIRECTLY VERIFIED |

## 9. Sources

- GitHub REST workflow-run endpoints: https://docs.github.com/en/rest/actions/workflow-runs
- GitHub REST workflow-job endpoints: https://docs.github.com/en/rest/actions/workflow-jobs
- GitHub REST artifact endpoints: https://docs.github.com/en/rest/actions/artifacts

Repository samples:
- Run 43412059150, attempt 1, job 131840643599, artifact 14029179772.
- Run 43411488324, attempt 1, job 131838734939, artifact 14029612439.

## 10. Gate disposition and next step

**Gate 197: PARTIAL PASS.** The attempt-specific run and jobs endpoints are now live-verified. The attempt identity can be resolved independently. The exact artifact-to-attempt association remains only corroborated, not directly verified, because the API does not expose an artifact-ID-to-attempt/job join field.

Do not freeze Gate 195's full evidence envelopes yet. Do not implement a permissive resolver that promotes temporal coincidence, artifact names or producer manifests to direct proof.

**Next operation:** audit the source-tree digest definition against GitHub's Git object/tree semantics and build deterministic test vectors covering nested trees, executable mode, symlinks, submodules, .gitattributes/LFS pointers, and empty directories. This is the next independently closable Gate 195 item; multi-attempt association remains an explicit integration-test blocker.
