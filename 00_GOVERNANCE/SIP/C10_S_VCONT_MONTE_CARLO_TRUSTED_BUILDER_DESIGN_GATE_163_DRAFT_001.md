# C10-S V_cont — Gate 163: dedicated trusted-builder design and threat model

**Status:** DESIGN DEFINED / WORKFLOW IMPLEMENTATION OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Scientific execution:** NOT AUTHORIZED  
**Calibration / seed-bank generation / Monte Carlo:** NOT AUTHORIZED  
**Workflow implementation and CI:** NOT PERFORMED IN THIS GATE

## 1. Decision and security boundary

Adopt a two-workflow separation:

1. **Unprivileged producer/test workflow** — existing `c10-s-focal-harness-tests.yml` remains a test workflow with `contents: read`; it may execute research-branch code and produce test captures, but receives no OIDC signing or attestation permissions.
2. **Dedicated trusted attestor workflow** — a new workflow, governed and stored on canonical `main`, is the only workflow permitted to create the final Artifact Attestation. It runs in a separate `workflow_run` or manually approved dispatch context, never checks out or executes the producer's source tree, and never runs Python, shell scripts, notebooks, or binaries from the producer artifact.

The attestor is not a scientific runner and must not regenerate, calibrate, replay, or evaluate the Monte Carlo study. It accepts a completed report package, performs only bounded structural/digest checks and source-run metadata verification, then attests the exact immutable package digest.

**Important semantic limit:** an attestation proves that the identified trusted workflow attested the subject under the verified workflow identity. It does not prove that the scientific contents are true, that the producer code was scientifically valid, or that a causal estimand was identified.

## 2. Trust roots and immutable identity

The trusted workflow must be committed to `main` and invoked from an immutable full commit SHA. Its workflow file and every third-party action must be pinned to full commit SHAs. The verifier policy must pin:
- repository full name `jcarmonabastida-pixel/TGCV`;
- repository ID `1348691577` as a governance identity check (not automatically treated as cryptographically bound unless verifier evidence supports that);
- trusted attestor workflow path and immutable workflow revision;
- OIDC issuer `https://token.actions.githubusercontent.com`;
- expected predicate type `https://slsa.dev/provenance/v1`;
- permitted event and source-ref policy;
- exact source commit and source-tree/archive digest recorded in the package.

No trusted identity may be derived from a workflow path or SHA supplied only by the producer artifact. The verifier must inspect the verified attestation certificate identity and workflow provenance returned by GitHub verification tooling.

## 3. Producer artifact hand-off

The producer workflow may upload a report package as an ordinary workflow artifact. The attestor must resolve the exact producer run through GitHub's workflow-run metadata, not trust arbitrary artifact JSON.

Before download/attestation, verify:
1. producer repository identity is TGCV;
2. producer workflow ID/path is the approved unprivileged producer workflow;
3. run conclusion is success and run ID/attempt are exact;
4. source ref is the allowed research ref or an explicitly approved immutable source commit;
5. event type is permitted (never accept an untrusted fork pull request);
6. artifact name and artifact ID belong to that exact run/attempt;
7. artifact has not expired and is downloaded from that run only;
8. package digest and internal manifest are recomputed after download;
9. manifest's source commit, code digest, seed/configuration fingerprints and M/R ledger reconcile with the run metadata and approved schemas.

The attestor must not use an artifact name alone as an identity. It must bind the GitHub run ID, run attempt, artifact ID, artifact digest and source commit. If GitHub's artifact API does not expose a required field or immutable binding, the workflow must fail closed or record the field as unverifiable; it must not infer it.

## 4. Critical workflow_run threat model

GitHub documents that `workflow_run` workflows can receive elevated permissions and can be exposed to untrusted artifacts produced by the triggering workflow. Treat all downloaded artifacts, filenames, JSON fields, archives and embedded paths as attacker-controlled.

Mitigations:
- no checkout of producer commit or artifact content;
- no execution of files from artifact;
- no `source`/import/eval/deserialization of executable payloads;
- safe archive extraction: reject absolute paths, traversal, symlinks, hardlinks, devices, duplicate paths and unexpected files; enforce size/count limits;
- parse JSON with strict schemas, bounded lengths and no polymorphic object deserialization;
- use a fresh isolated runner and least-privilege token;
- set `persist-credentials: false` for any checkout (prefer no checkout at all);
- do not interpolate artifact fields into shell commands;
- pass values through environment variables or structured files and quote all shell expansions;
- do not expose secrets to producer jobs;
- do not let producer-controlled data choose signer workflow, action revision, permissions, repository, OIDC audience, or policy;
- restrict accepted producer refs/events and reject forks and unapproved workflow definitions;
- pin all actions by full SHA and review updates as governance changes.

If any artifact content influences a privileged decision beyond the allowlisted metadata/digest checks, the attestor must reject it.

## 5. Permissions and job separation

The signing job's permissions must be minimal and explicit. Candidate minimums for `actions/attest` include:
- `id-token: write`;
- `attestations: write`;
- `artifact-metadata: write`.

Add `actions: read` / `contents: read` only if the exact pinned implementation needs them to resolve the producer run/artifact or source metadata. Verify permissions against the pinned action revision and GitHub API behavior before implementation. Do not grant broad `contents: write`, `pull-requests: write`, or repository administration.

Separate jobs:
- **resolve-and-validate**: read-only metadata/artifact download, no OIDC signing permission;
- **attest**: receives only a validated package digest/path and the minimum permissions needed to attest; does not execute producer content;
- **verify**: independently verifies the produced attestation and policy before reporting success. Where practical, keep verification separate from signing permissions.

Use a protected environment or required reviewer only if governance explicitly chooses it; do not claim a human approval gate exists unless configured and tested.

## 6. Artifact package contract

The subject is one finalized package (e.g. `c10s-monte-carlo-report-package.tar.zst`) with deterministic contents and a canonical manifest. It must include:
- report payload and report fingerprint;
- report schema/version;
- exact 52-pair temporal coverage ledger and status denominators;
- evaluation seed-bank manifest and recomputed fingerprint;
- calibration seed-bank manifest/fingerprint and disjointness proof;
- all M/R/RunManifest-to-SeedAssignment joins;
- effective Generator/DGP/Analyzer configuration payloads and recomputed fingerprint;
- tested source commit, source-tree/archive digest and producer run ID/attempt;
- test/validation record references and software versions.

Canonical serialization, file ordering, timestamp normalization and archive format must be specified by the report packager contract before relying on reproducible package digests. Exclude secrets, credentials and private runner paths.

The attestor signs the final package digest only after it has been finalized. Any mutation requires a new digest and new attestation.

## 7. Verifier acceptance contract

The verifier consumes:
- exact package path and independently computed digest;
- producer run ID/attempt and artifact ID;
- expected repository name and governed repository ID;
- expected attestor workflow path/revision and OIDC issuer;
- expected predicate type;
- expected source commit/ref and source-tree digest;
- structured output from `gh attestation verify`.

It emits:
- `PROVENANCE_AUTHENTICATED`: cryptographic verification succeeds and subject, repository, signer workflow, issuer, predicate and source policy all pass;
- `PROVENANCE_RECONCILED`: deterministic manifest/seed/config/run reconciliation passes but no acceptable attestation is present;
- `PROVENANCE_REJECTED`: signature, subject, signer, repository, source, schema or policy fails.

Missing or unverifiable required fields must never be silently treated as a pass. A mismatch is REJECTED; a genuinely absent attestation may remain RECONCILED only where the report is explicitly marked unauthenticated and cannot be used as authenticated evidence.

The verifier must rely on GitHub CLI/Sigstore verification for cryptographic validation, not implement signature verification itself. It must check structured verified output, not parse human-readable success strings.

## 8. Adversarial acceptance tests

Before the workflow can be accepted, tests must show rejection of:
- artifact from another repository, run, attempt or workflow;
- artifact from fork pull request or disallowed event/ref;
- artifact ID/name mismatch and expired artifact;
- path traversal, symlink, duplicate entry, oversized archive and malformed JSON;
- producer-controlled signer path, action SHA, repository, issuer, predicate or source commit;
- changed package after attestation;
- valid attestation from wrong workflow revision or wrong repository;
- wrong source commit/tree digest or report schema;
- missing attestation and forged `attested=true`;
- replay of an attestation from a previous report package;
- any manifest row that does not map one-to-one to a canonical SeedAssignment / RunManifest pair;
- any calibration/evaluation seed overlap;
- all existing Gate 157 52-pair, `TRUTH_MISSING` and `INVALID_OUTPUT` regressions.

A valid signature from the trusted workflow must not bypass deterministic Gate 159 reconciliation.

## 9. Implementation sequence and authorization boundary

Implementation must be split into controlled steps:
1. finalize deterministic report-package schema and canonical packager;
2. implement Gate 159 seed/configuration/manifest reconciliation and adversarial tests;
3. inventory and pin exact action commit SHAs and trusted workflow revision;
4. implement a no-execution attestor workflow on `main`, after a separate explicit workflow-change authorization;
5. implement independent verifier adapter and policy tests;
6. run only deterministic technical tests after explicit technical-verification authorization;
7. only later, under separate authorization, produce an attestation for a real authorized report package.

This Gate 163 document defines the architecture and threat model. It does **not** itself authorize workflow/code edits, signing permissions, CI dispatch, attestation generation, calibration, seed-bank generation, N/R/M sizing, Monte Carlo execution or scientific execution.

## 10. Status

- Dedicated trusted-builder architecture: DEFINED.
- Existing producer/test workflow: remains unprivileged.
- Attestor workflow location: canonical `main`, immutable revision required.
- Producer artifact hand-off contract: DEFINED.
- Threat model and mitigations: DEFINED.
- Report package schema/canonical packager: OPEN.
- Gate 159 deterministic reconciliation implementation: OPEN.
- Attestor workflow implementation: OPEN; separate explicit authorization required.
- Verifier adapter: OPEN.
- Adversarial tests: OPEN.
- Attestation generation: NOT EXECUTED.
- Scientific execution: NOT AUTHORIZED.
- `main`: unchanged by this gate; PR #116 remains Draft on its existing base.
