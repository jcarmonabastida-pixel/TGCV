# C10-S V_cont — Gate 161: artifact-attestation availability and trusted-builder preflight

**Status:** AVAILABILITY CONFIRMED / TRUSTED BUILDER NOT YET IDENTIFIED  
**Branch:** `research/c10-s-consolidation-draft`  
**Repository:** `jcarmonabastida-pixel/TGCV`  
**Scientific execution:** NOT AUTHORIZED  
**Workflow/code modification:** NOT PERFORMED

## 1. Bootstrap and historical recovery

The operational entry point `00_GOVERNANCE/README.md` was read from `main` (blob SHA `f4871301c70e98a0b1b91d2253d0e937768c75d8`). The bootstrap and canonical state were also read from main. The canonical state declares RMA v3.38 and Evidence→Claim Matrix v1.47. Historical Gate 158–160 records and the calibration/seed-bank protocol were recovered from the research branch before this preflight.

No local validator was executed; this is a GitHub-side read-only preflight.

## 2. Repository visibility and feature availability

GitHub repository metadata was retrieved for `jcarmonabastida-pixel/TGCV`:
- immutable GitHub repository ID: `1348691577`;
- visibility: `public`;
- default branch: `main`;
- repository permissions for the connected identity include admin/push.

The public visibility satisfies the documented repository-visibility condition for Artifact Attestations on current GitHub plans. This preflight therefore closes the **visibility/plan-class availability condition** for the selected architecture. It does not prove that a future workflow has been enabled, correctly permissioned, or successfully executed.

Official references:
- GitHub Artifact Attestations overview: https://docs.github.com/en/actions/concepts/security/artifact-attestations
- Generation and availability requirements: https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations
- `actions/attest` usage and permissions: https://github.com/actions/attest
- GitHub CLI verification policy: https://cli.github.com/manual/gh_attestation_verify

## 3. Workflow discovery result

A read-only fetch was attempted for the previously assumed path:
`.github/workflows/c10-s-vcont-benchmark.yml`.

GitHub returned NOT_FOUND. This means that exact path is not present at the research branch ref inspected; it does not prove that no other C10-S workflow exists.

The available repository connector in this preflight did not expose a complete workflow-directory listing or repository tree listing. No alternate workflow path, reusable workflow, signer workflow identity, or immutable workflow revision has therefore been established. No workflow file was created or modified.

**Decision:** do not invent or pin a signer workflow path. The trusted-builder portion of Gate 161 remains OPEN until the actual workflow inventory is recovered from the repository tree and the selected workflow is inspected at an immutable commit.

## 4. Required trusted-builder contract

Before any attestation workflow is implemented, identify and freeze:
1. exact signer workflow path and immutable revision (full commit SHA);
2. whether it is a reusable workflow; if so, pin and verify the reusable workflow identity as the signer;
3. exact repository identity, including numeric repository ID `1348691577` as an additional policy input;
4. OIDC issuer `https://token.actions.githubusercontent.com`;
5. expected signer certificate identity / SAN and predicate type `https://slsa.dev/provenance/v1`;
6. allowed triggering events and source refs; untrusted pull-request code must not control the signing job;
7. least-privilege permissions.

For `actions/attest@v4`, the action's current README documents:
- `id-token: write`;
- `attestations: write`;
- `artifact-metadata: write`.

The GitHub documentation's basic example also includes `contents: read`. The eventual workflow must use the exact minimum permissions required by the pinned action version and repository API behavior; this permission set must be verified against the pinned action revision rather than copied uncritically from a moving tag.

Third-party actions in the signer workflow must be pinned to full commit SHAs. The verifier must use `gh attestation verify` with repository and signer-workflow constraints, and inspect structured verification output. A reusable workflow changes the signer identity: the reusable workflow, not merely its caller, must be constrained.

## 5. Verifier contract

The verifier accepts:
- finalized report-package path;
- expected repository full name and numeric repository ID policy value;
- expected signer workflow path/revision;
- expected OIDC issuer and predicate type;
- expected source commit/ref and report package digest;
- structured `gh attestation verify --format json` output.

It returns one of:
- `PROVENANCE_AUTHENTICATED`: cryptographic verification succeeds and every governed signer/repository/source/predicate/subject policy check passes;
- `PROVENANCE_RECONCILED`: deterministic input reconciliation succeeds but external attestation is absent or unavailable;
- `PROVENANCE_REJECTED`: signature, subject digest, signer identity, repository, source identity, predicate, or policy check fails.

It must never elevate status based on caller-provided `attested=true`, environment variables, unsigned JSON, or a declared SHA alone. The verifier must not claim that the attestation establishes scientific validity or causal truth.

Important identity limitation: the GitHub CLI's documented repository verification checks certificate repository/owner identity and signer workflow. The numeric repository ID is an additional governance control and must not be described as cryptographically verified unless the selected verifier/API provides a cryptographically bound, independently checked repository-ID field. A repository rename/reuse concern must be explicitly handled in the verifier policy and evidence record.

## 6. Gate 161 status

- Repository visibility: CONFIRMED PUBLIC.
- Artifact Attestations visibility/plan-class availability: CONFIRMED for current public-repository plan eligibility.
- Actual account entitlement beyond public-repository eligibility: no separate billing-plan assertion made.
- Exact signer workflow path: OPEN.
- Immutable trusted-builder revision: OPEN.
- OIDC/certificate identity policy: DEFINED AT CONTRACT LEVEL; exact identity OPEN.
- Verifier contract: DEFINED; implementation OPEN.
- Workflow/code changes: NOT PERFORMED.
- CI or attestation generation: NOT EXECUTED.
- Calibration, seed-bank generation, N/R/M sizing, Monte Carlo benchmark and scientific execution: NOT AUTHORIZED / NOT EXECUTED.
- `main`: unchanged; PR #116 remains Draft on its existing base.

## 7. Next operation

Recover the complete workflow inventory and historical workflow provenance from the Git tree / workflow API. Select an existing trusted workflow only if its security boundary is adequate; otherwise draft a dedicated reusable signer workflow under a separate governance decision. Do not generate attestations until the signer workflow identity and policy are frozen.
