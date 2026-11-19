# C10-S V_cont — Gate 195: external GitHub evidence schema closure preflight

**Status:** DRAFT — PROPOSED CONTRACT, NOT FROZEN  
**Scope:** Close the field-level source contracts for `provenance/source_execution.json` and `validation/test_evidence.json`, and define the bounded read-only resolver boundary required before implementing a GitHub evidence adapter.  
**Branch:** `research/c10-s-consolidation-draft`  
**Canonical boundary:** no changes to `main`; no trusted-attestor workflow, OIDC permissions, artifact attestation, producer, calibration, seed generation, or scientific execution.

## 1. Purpose and governing sources

This gate continues the Gate 194-A crosswalk. It does not supersede Gates 160–164, 176, 178, 182, 193 or 194-I.

Gate 178 §8 establishes the minimum members of SourceExecutionEvidence and TechnicalTestEvidence. Gate 163 defines the trusted-builder threat model and requires GitHub-resolved run and artifact identity, with no execution of producer-supplied content. Gate 194-A identifies the exact package paths and states that source-execution and test-evidence schemas remain open. Gate 194-I closes substantial parts of the configuration-fingerprint companion but explicitly leaves source-execution provenance unverified.

This gate turns those minimum-member lists into a proposed field-level contract. It does not claim that all GitHub API fields are available, immutable, or sufficient for authentication.

## 2. Evidence model and trust boundary

Three layers MUST remain distinct:

1. **Producer declarations:** values written by the producer into the package. They are untrusted claims.
2. **Resolver observations:** values fetched independently from GitHub APIs by a read-only resolver, with the exact API resource identity and retrieval time recorded.
3. **Comparison result:** a deterministic comparison of declared and observed values. A match is reconciliation, not cryptographic authentication.

No value from a producer declaration may be copied into the resolver-observation object and relabelled as observed. No resolver may execute, import, deserialize polymorphically, or invoke code from a producer artifact. Package content is treated as untrusted data and parsed only with bounded strict JSON/archive handling.

The read-only adapter may resolve metadata and download an artifact by exact GitHub artifact ID after validating repository, workflow, run, attempt, event, ref and commit policy. It must not sign or attest the package.

## 3. SourceExecutionEvidence v1.0.0 — proposed exact envelope

Proposed schema ID: `TGCV-C10S-VCONT-SOURCE-EXECUTION-EVIDENCE`  
Proposed schema version: `1.0.0`

Exact top-level fields:

- `schema_id`
- `schema_version`
- `benchmark_export_id`
- `producer_declarations`
- `github_observations`
- `comparison`
- `resolver`

No additional or missing fields are permitted in this proposed version. Explicit null is distinct from a missing field.

### 3.1 producer_declarations

Exact fields:

- `repository_full_name`
- `workflow_path`
- `workflow_id`
- `run_id`
- `run_attempt`
- `event`
- `source_ref`
- `commit_sha`
- `source_tree_digest`
- `producer_artifact_id`
- `producer_artifact_digest`
- `tested_source_archive_digest`
- `runtime_identity`
- `dependency_lock_digest`

All fields are declarations only. IDs are positive integers where GitHub exposes numeric IDs; SHAs and digests are lowercase fixed-length hexadecimal strings only where the relevant algorithm and length are specified by the governing contract. `runtime_identity` is a bounded object whose exact members must be sourced from the producer runtime contract; it is not used as a trust anchor.

### 3.2 github_observations

Exact fields:

- `repository`
- `workflow`
- `run`
- `attempt`
- `artifact`
- `source_tree`

Each resource observation contains:
- `api_resource`: canonical GitHub API resource URL/path actually queried;
- `retrieved_at`: UTC RFC 3339 timestamp;
- `http_status`: observed successful status code;
- `response_digest`: SHA-256 of the exact response bytes retained by the resolver, if retained under the resolver's evidence policy.

Resource-specific observed fields:

**repository:** `repository_id`, `repository_full_name`, `visibility`, `archived`.

**workflow:** `workflow_id`, `workflow_path`, `workflow_state`.

**run:** `run_id`, `run_attempt`, `event`, `head_branch`, `head_sha`, `status`, `conclusion`, `repository_id`, `workflow_id`, `workflow_path`.

**attempt:** `run_id`, `run_attempt`, `event`, `head_branch`, `head_sha`, `status`, `conclusion`. If the GitHub API does not expose an independently addressable attempt resource, the resolver records the exact run resource and the API limitation; it must not fabricate a separate endpoint or imply attempt-level resolution.

**artifact:** `artifact_id`, `name`, `expired`, `size_in_bytes`, `digest`, `workflow_run_id`. Artifact name is descriptive only and never an identity key.

**source_tree:** `commit_sha`, `tree_object_sha`, `tree_digest_algorithm`, `tree_digest`, `tree_digest_status`.

The resolver MUST retain the distinction between Git object tree SHA and any separately computed normalized source-tree digest. They are not interchangeable.

### 3.3 comparison

Exact fields:

- `status`: `MATCHED`, `MISMATCHED`, `INCOMPLETE`, or `UNVERIFIABLE`;
- `matched_fields`: ordered unique field identifiers;
- `mismatched_fields`: ordered unique field identifiers;
- `unavailable_fields`: ordered unique field identifiers;
- `reason_codes`: ordered unique bounded codes.

A mismatch in repository identity, workflow identity, run ID/attempt, event/ref policy, commit SHA, artifact ID or artifact digest is fail-closed and cannot produce `MATCHED`. Missing required observations produce `INCOMPLETE` or `UNVERIFIABLE`, never a zero-mismatch PASS.

### 3.4 resolver

Exact fields:

- `resolver_id`
- `resolver_version`
- `resolver_source_commit`
- `resolver_source_digest`
- `api_version`
- `resolution_timestamp`
- `resolution_status`

`resolution_status` is one of `RESOLVED`, `PARTIAL`, `UNAVAILABLE`, `REJECTED`. Resolver identity is descriptive until a trusted workflow/attestation policy authenticates it.

## 4. TechnicalTestEvidence v1.0.0 — proposed exact envelope

Proposed schema ID: `TGCV-C10S-VCONT-TECHNICAL-TEST-EVIDENCE`  
Proposed schema version: `1.0.0`

Exact top-level fields:

- `schema_id`
- `schema_version`
- `benchmark_export_id`
- `test_class`
- `producer_source_execution_ref`
- `test_workflow_declaration`
- `github_observations`
- `test_result`
- `resolver`

### 4.1 test_class

Allowed values:
- `SERIALIZER_VERIFIER_PURE_TESTS`
- `SCIENTIFIC_HARNESS_TESTS`

These classes are never merged. A pure serializer/verifier test PASS does not establish that scientific harness tests ran.

### 4.2 producer_source_execution_ref

Exact fields:
- `producer_repository_full_name`
- `producer_run_id`
- `producer_run_attempt`
- `producer_commit_sha`
- `producer_artifact_id`
- `producer_artifact_digest`

These values identify the producer execution to which the test evidence is being related. They are claims until compared against the independently resolved SourceExecutionEvidence.

### 4.3 test_workflow_declaration

Exact fields:
- `repository_full_name`
- `workflow_path`
- `workflow_id`
- `run_id`
- `run_attempt`
- `event`
- `source_ref`
- `tested_commit_sha`
- `test_target_id`
- `command_id`

`test_target_id` and `command_id` are stable identifiers from a versioned allowlist. Arbitrary shell command strings supplied by the package are not accepted as proof of what ran.

### 4.4 github_observations

Exact fields:
- `repository`
- `workflow`
- `run`
- `attempt`
- `test_artifact`

The same resource-observation envelope and API provenance rules in §3.2 apply. The run observation must establish exact repository, workflow, run ID, attempt, event, ref, tested commit, status and conclusion. The test artifact observation must establish exact artifact ID, workflow run ID, expiry state and digest where GitHub exposes it.

### 4.5 test_result

Exact fields:
- `conclusion`: observed workflow conclusion, not a producer-selected status;
- `declared_test_count`: nonnegative integer or null;
- `observed_test_count`: nonnegative integer or null;
- `failure_count`: nonnegative integer or null;
- `error_count`: nonnegative integer or null;
- `test_artifact_id`;
- `test_artifact_digest`;
- `source_execution_comparison`: `MATCHED`, `MISMATCHED`, `INCOMPLETE`, or `UNVERIFIABLE`.

A workflow conclusion of success without retrievable test output/artifact and a known target/command remains insufficient for a test-evidence PASS. Authored test count and executed test count must never be conflated.

### 4.6 resolver

Exact resolver schema as §3.4. The resolver is not trusted merely because it identifies itself.

## 5. Resolver algorithm — bounded read-only sequence

For each evidence class, the resolver MUST:

1. Validate the local package envelope and exact schema before any API lookup.
2. Treat all producer-supplied GitHub identifiers as lookup claims, not authority.
3. Resolve the repository by full name and record its immutable repository ID.
4. Resolve the workflow by repository and workflow ID/path; compare both.
5. Resolve the exact run and attempt; verify repository ID, workflow ID, event, ref, head SHA, status and conclusion.
6. Resolve the exact artifact by artifact ID within the exact run; verify its workflow-run binding, expiry and available digest/size metadata.
7. Download only that artifact through the authenticated GitHub API after the identity checks pass; never locate it by name alone.
8. Recompute the downloaded artifact digest using the algorithm defined by the applicable GitHub artifact API contract, and record both GitHub-reported and locally recomputed values separately.
9. Resolve the source commit and Git tree object. Compute a normalized source-tree digest only after a separate canonical algorithm and test vectors are approved.
10. Compare all resolved values with producer declarations and the package's design/capture identity.
11. Emit explicit `MATCHED`, `MISMATCHED`, `INCOMPLETE` or `UNVERIFIABLE` outcomes. Never coerce missing values to empty strings, zero counts or successful matches.

The resolver must use read-only repository/Actions access. It must not request `contents: write`, `actions: write`, `id-token: write` or `attestations: write`.

## 6. Fail-closed and adversarial requirements

At minimum reject or mark unverifiable:

- producer declaration disagrees with repository ID/full name;
- workflow ID and path resolve to different workflows;
- run belongs to another repository/workflow;
- run attempt differs from the requested attempt;
- disallowed event, fork, ref or source commit;
- run is not completed successfully where success is required;
- artifact ID does not belong to the exact run;
- artifact expired, unavailable, or digest differs;
- source commit differs from run head SHA;
- Git tree object SHA differs from the resolved commit tree;
- source-tree digest algorithm is unknown, ambiguous or not reproducible;
- test evidence points to a different producer run/attempt/commit/artifact;
- test target or command ID is absent from the versioned allowlist;
- only a workflow conclusion is available, without retrievable evidence of the declared test target/counts;
- duplicate JSON keys, extra/missing fields, malformed types, oversized payloads or archive path traversal;
- any attempt to treat a producer declaration as an independently observed value.

## 7. Explicit unresolved contract decisions

This gate deliberately does not invent the following details:

1. **Source-tree digest algorithm.** Git commit/tree object IDs are available identities, but Gate 178's additional `source tree digest` requires a canonical inclusion/exclusion policy, byte representation, ordering, symlink/submodule treatment and test vectors. Until frozen, `source_tree_digest_status=UNVERIFIABLE`.
2. **Artifact digest authority.** The exact GitHub API/CLI version and semantics for the reported artifact digest, including the algorithm and whether it covers the downloaded archive bytes, must be verified against the current API contract and test vectors. A local digest is recorded separately.
3. **Attempt resolution.** Confirm the API's attempt-specific endpoint and response semantics; if unavailable, record the limitation and do not imply a distinct attempt resource.
4. **Runtime identity.** Close its exact field schema from the producer runtime contract; it is not an authentication input.
5. **Dependency-lock digest.** Bind the exact lockfile path, bytes and algorithm from the package's dependency contract.
6. **Test target/command allowlist.** Freeze identifiers and mapping to workflow YAML and observed test output; do not treat a free-form command string as trusted evidence.
7. **Resolver authentication.** This read-only adapter cannot authenticate itself. A future Gate 163 trusted attestor, governed on `main`, must authenticate the resolver workflow identity under a separately authorized policy.

Until these decisions are closed, the schemas are proposed and the resolver must return a non-success status for the affected checks.

## 8. Relationship to Gate 159 and package verifier

The adapter produces independently observed evidence. It does not replace the deterministic Gate159 reconciliation algorithm.

The verifier must continue to derive:
- `REJECTED` when a required comparison fails;
- `NOT_RECONCILED` when required evidence is missing or unverifiable;
- `RECONCILED` only when every required check is present and passes.

External authentication remains a separate state. `RECONCILED` is not `AUTHENTICATED`.

The package verifier must not import the writer, producer, harness, or adapter implementation as its trust source. A later independent verifier integration must consume the versioned evidence schema and recompute all comparisons from materialized evidence.

## 9. Acceptance criteria for this gate

- [ ] Field-level schema for SourceExecutionEvidence is reviewed against Gate 178 §8 and Gate 163.
- [ ] Field-level schema for TechnicalTestEvidence is reviewed against Gate 178 §8 and Gate 163.
- [ ] All GitHub API resources/fields and attempt semantics are verified against the supported API contract.
- [ ] Artifact digest algorithm and byte coverage are verified with test vectors.
- [ ] Source-tree digest algorithm and test vectors are frozen.
- [ ] Runtime identity and dependency-lock binding are closed.
- [ ] Test target/command allowlist is frozen and tied to the actual workflow.
- [ ] Adversarial fixtures cover missing, contradictory, stale, cross-run and forged declarations.
- [ ] The resolver remains read-only and never executes producer content.
- [ ] No trusted workflow, OIDC signing permission, attestation, producer, calibration or scientific execution is introduced by this gate.

## 10. Disposition

**Gate 195: CONDITIONAL — PROPOSED SCHEMA CONTRACT / NOT FROZEN.**

The proposed envelopes provide a concrete field-level starting point grounded in Gate 178's minimum members and Gate 163's trust boundary. They do not yet authorize implementation of a resolver that can return a positive provenance or test-evidence status. The unresolved decisions in §7 must be closed first.

**Next operation:** perform a focused GitHub API contract audit for repository/workflow/run/attempt/artifact resources and verify artifact digest semantics; separately define and test the canonical source-tree digest. Only then may the schema be frozen and the read-only adapter implemented in research.

No changes to `main`, scientific components, estimands, DGPs, seed generation, calibration, producer execution, Monte Carlo execution or attestation permissions are authorized by this draft.
