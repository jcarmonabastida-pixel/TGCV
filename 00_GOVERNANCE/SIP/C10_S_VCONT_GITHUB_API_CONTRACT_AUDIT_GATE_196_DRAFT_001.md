# C10-S V_cont — Gate 196: GitHub Actions API contract and artifact-digest audit

**Status:** PARTIAL AUDIT PASS — ARTIFACT DIGEST VERIFIED 2/2; ATTEMPT-TO-ARTIFACT BINDING OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 195 — external GitHub evidence schema closure preflight  
**Audit basis:** GitHub REST documentation, read-only GitHub connector observations, retrieval and local hashing of two existing workflow-artifact ZIPs. No workflow was launched, no source code was executed, and no scientific execution occurred.

## 1. Purpose and boundary

This gate continues Gate 195's expressly stated next operation. It audits the documented GitHub REST resources for workflow runs, run attempts and artifacts, then tests the reported artifact digest against exact downloaded ZIP bytes.

This is a bounded API/evidence-contract audit. It does not freeze the complete SourceExecutionEvidence or TechnicalTestEvidence schemas, implement the resolver, authenticate the resolver, or establish scientific validity.

No changes to `main`, C10 estimands/DGPs, producer, Analyzer, Evaluator, calibration, seed generation, Monte Carlo, attestation permissions or scientific claims are made or authorized.

## 2. API contract findings

### 2.1 Workflow run

The REST workflow-run resource exposes the fields required to resolve the principal execution identity, including run ID, workflow ID, workflow path, event, head branch/SHA, status, conclusion, repository identity and `run_attempt`.

The run resource is addressed independently of its attempt. The response's `run_attempt` is the current/latest attempt number; it must not be treated as a historical attempt-specific response when a run has been rerun.

Documented resource family:
- `GET /repos/{owner}/{repo}/actions/runs`
- `GET /repos/{owner}/{repo}/actions/runs/{run_id}`

### 2.2 Attempt-specific resolution

GitHub documents an independently addressable attempt endpoint:

`GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}`

The endpoint requires both `run_id` and `attempt_number`, returns a workflow-run-shaped response including `run_attempt`, and requires Actions read permission for fine-grained credentials. GitHub also documents attempt-specific job listing:

`GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs`

**Contract conclusion:** Gate 195's proposal to resolve a specific attempt is supported by the current REST contract. The attempt is not merely a producer-supplied integer; the resolver can request the exact attempt resource and compare its returned identity and execution fields.

**Live observation limitation:** the available GitHub connector exposed latest-attempt job listing but rejected direct retrieval of the attempt-specific REST URL as an unsupported fetch URL. Consequently, this gate verifies the documented endpoint and response contract, not a live response from that endpoint for the two historical runs. The resolver implementation must test this endpoint directly and record the actual response.

### 2.3 Artifact metadata and run association

GitHub documents:
- `GET /repos/{owner}/{repo}/actions/runs/{run_id}/artifacts`
- `GET /repos/{owner}/{repo}/actions/artifacts/{artifact_id}`
- `GET /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip`

Artifact metadata exposes `id`, `name`, `size_in_bytes`, `expired`, timestamps, `digest`, and a `workflow_run` object containing the run ID, repository ID, head repository ID, branch and head SHA.

The artifact download endpoint returns a redirect; GitHub documents that the download URL expires after one minute. The resolver should therefore resolve and validate the artifact ID first, then download promptly and retain the exact response bytes used for hashing.

**Important limitation:** the documented artifact metadata's `workflow_run` object contains the run ID and source identity but does not expose a `run_attempt` field. The artifact-list endpoint is run-scoped, not attempt-scoped. The artifact ID is an exact artifact identity, but the API response alone does not directly prove which attempt of a rerun-created workflow run produced it.

Therefore:
- artifact ID must remain the lookup key; name is descriptive only;
- run ID/repository/head SHA binding can be checked from artifact metadata;
- attempt identity must be independently resolved through the attempt endpoint;
- **artifact-to-attempt binding is not established by the artifact metadata alone**;
- when a run has multiple attempts, the resolver must return an explicit non-success/indeterminate state unless an additional independently observed binding is available. A producer manifest or artifact name containing the attempt number is only a declaration, not independent proof.

This is a required refinement to Gate 195's step that proposes verifying that an artifact belongs to the exact run/attempt.

## 3. Experimental artifact-digest verification

The GitHub connector retrieved artifact metadata and downloaded each exact artifact by numeric artifact ID. The ZIP bytes were saved without extraction or recompression. Local SHA-256 was computed over the complete downloaded file.

| Field | Sample A | Sample B |
|---|---:|---:|
| Workflow run ID | `43412059150` | `43411488324` |
| Artifact ID | `14029179772` | `14029612439` |
| Tested commit | `244896092e6414ccd92bd31a19776dcf71266c15` | `dd886afd1bc68de231f5675e5364602914088453` |
| API size_in_bytes | 2,994 | 1,888 |
| Downloaded ZIP size | 2,994 | 1,888 |
| API digest | `sha256:1ab1879cc39787bb43f252b83fc3482a8c352052c86e6cc95a494a6053685fd3` | `sha256:f3792fb0ed34e56c43b560c969d3cebdbe33304300f2ab43de3d7ceddca07a54` |
| Local SHA-256 of ZIP bytes | `1ab1879cc39787bb43f252b83fc3482a8c352052c86e6cc95a494a6053685fd3` | `f3792fb0ed34e56c43b560c969d3cebdbe33304300f2ab43de3d7ceddca07a54` |
| Equality | MATCH | MATCH |
| API expired | false | false |

Both tested workflow definitions at their exact tested commits used `actions/upload-artifact@v4`. Both ZIPs contained the expected execution capture(s) and a producer-written execution manifest. The manifests declared `run_attempt: "1"`; that declaration was inspected as package content and was **not** treated as an independent API observation.

### Digest conclusion

For both observed v4 artifacts, the GitHub API `digest` equals:

`SHA-256(exact downloaded ZIP archive bytes)`

The equality also holds for the API `size_in_bytes` and the downloaded ZIP byte length.

**Proposed normative interpretation for the current adapter:** preserve the API digest exactly as reported (including the `sha256:` algorithm prefix), compute a separate local SHA-256 over the exact downloaded ZIP bytes, and compare the normalized algorithm/value pair. Never hash extracted files and call that the GitHub artifact digest. Never replace the API value with a locally computed value without retaining both observations.

The two successful vectors establish empirical agreement for these two existing artifacts and the observed upload-artifact v4 workflow path. They do not establish behavior for every historical artifact version or future GitHub API implementation. Keep both vectors as regression fixtures and revalidate after a material API/artifact-action version change.

## 4. Required Gate 195 schema refinements

1. Preserve separate `run` and `attempt` observations. The attempt observation must cite the attempt-specific API resource actually queried.
2. Add an explicit attempt/artifact binding status, with at least `VERIFIED`, `UNVERIFIABLE`, `MISMATCHED`. Do not infer `VERIFIED` from artifact name or producer manifest.
3. For multiple-attempt runs, do not return `MATCHED` for source-execution evidence solely because artifact ID, run ID and producer-declared attempt agree. Require an independently observed artifact-to-attempt link; otherwise return `INCOMPLETE` or `UNVERIFIABLE`.
4. Define artifact digest comparison as SHA-256 over the exact downloaded ZIP bytes, retaining API-reported and locally recomputed values separately.
5. Retain artifact ID as the identity key. Artifact name remains descriptive.
6. Pin and record the REST API version used for each observation. Do not assume that a field observed under a newer API version exists under an older pinned version.

## 5. Evidence-state disposition

| Question | Result | State |
|---|---|---|
| Does GitHub document an attempt-specific run endpoint? | Yes; exact run ID + attempt number path | DOCUMENTED |
| Does the attempt response expose run_attempt? | Yes, in documented response schema | DOCUMENTED |
| Was the attempt-specific endpoint live-read through the available connector? | No; connector rejected the URL | NOT_VERIFIABLE IN THIS PASS |
| Does artifact metadata expose exact artifact ID and run association? | Yes | DOCUMENTED + OBSERVED |
| Does artifact metadata independently expose run_attempt? | No | NOT EXPOSED |
| Does the API digest match raw downloaded ZIP bytes? | Yes, 2 of 2 samples | EXPERIMENTAL PASS — BOUNDED |
| Is artifact-to-attempt binding solved for reruns? | No | OPEN |
| Is source-tree digest algorithm frozen? | No | OPEN |
| Are runtime identity and dependency-lock schemas closed? | No | OPEN |
| Is test target/command allowlist frozen? | No | OPEN |
| Is resolver implemented/authenticated? | No | NOT IMPLEMENTED / NOT AUTHENTICATED |

## 6. Sources

GitHub REST documentation:
- Workflow runs: https://docs.github.com/en/rest/actions/workflow-runs
- Workflow jobs, including attempt-specific jobs: https://docs.github.com/en/rest/actions/workflow-jobs
- Workflow artifacts, metadata and download: https://docs.github.com/en/rest/actions/artifacts
- Workflow artifact digest behavior: https://docs.github.com/en/actions/tutorials/store-and-share-data

Repository evidence:
- Run 43412059150; artifact 14029179772; tested commit `244896092e6414ccd92bd31a19776dcf71266c15`.
- Run 43411488324; artifact 14029612439; tested commit `dd886afd1bc68de231f5675e5364602914088453`.

## 7. Disposition and next operation

**Gate 196: PARTIAL AUDIT PASS.** The API supports explicit attempt-specific resolution, and the GitHub artifact digest has been empirically matched to exact downloaded ZIP bytes in two independent existing artifacts. The attempt-to-artifact binding limitation is material and remains open.

No adapter implementation or schema freeze is authorized by this gate. No code, workflow, test, producer, calibration or scientific execution was performed.

**Next operation:** define a fail-closed attempt/artifact association rule for reruns using only independently observable GitHub evidence; then close the canonical source-tree digest algorithm and its test vectors. Reconcile the Gate 195 envelopes only after those rules are explicit.
