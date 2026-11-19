# C10-S V_cont — Gate 162: workflow inventory and trusted-builder suitability audit

**Status:** INVENTORY RECOVERED / EXISTING WORKFLOWS NOT SUITABLE AS TRUSTED SIGNER AS-IS  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** GitHub Actions workflow inventory, C10-S workflow history and attestation trust boundary  
**Scientific execution:** NOT AUTHORIZED  
**Workflow modification / attestation generation:** NOT PERFORMED

## 1. Canonical bootstrap

Read `00_GOVERNANCE/README.md` from `main`; blob SHA:
`f4871301c70e98a0b1b91d2253d0e937768c75d8`.

The README confirms:
- `main` is the canonical source of truth;
- research-branch changes must not be silently promoted;
- historical reconstruction precedes new work;
- execution authorization, provenance and state labels must remain explicit.

The repository bootstrap and canonical-state pointers were previously recovered in this continuation. No local validator or scientific execution was performed in this gate.

## 2. Complete workflow-directory inventory and branch delta

The GitHub Contents API returned the complete `.github/workflows/` directory for both refs:
- `main`: 50 workflow files;
- `research/c10-s-consolidation-draft`: 55 workflow files.

The research branch contains exactly five additional files; no workflow present on main is missing from the research branch, and no same-named workflow has a different blob SHA between these two refs.

The five branch-only workflow files are:
1. `c10-s-analyzer-mc-performance-diagnostic.yml`
2. `c10-s-analyzer-mc-replay.yml`
3. `c10-s-analyzer-monte-carlo.yml`
4. `c10-s-analyzer-t-cache-probe.yml`
5. `c10-s-focal-harness-tests.yml`

This is an exact directory-level comparison, not an assumption based on filename search. It establishes that the C10-S-specific workflow additions are confined to the research branch at the inspected refs.

## 3. C10-S workflow inventory and immutable blob identities

| Workflow | Blob SHA | Role |
|---|---|---|
| `c10-s-analyzer-mc-performance-diagnostic.yml` | `ab43b805cb127fbbdd0caa9d61ba14d20729d839` | bounded performance/repeatability diagnostic |
| `c10-s-analyzer-mc-replay.yml` | `d1cff873374d5691638bbba1a579ff39152935b5` | replay of an existing P178 artifact |
| `c10-s-analyzer-monte-carlo.yml` | `54eccca47a1dd5628dafabcba70a0e1c872a44a1` | legacy P178 27-cell Monte Carlo and replay |
| `c10-s-analyzer-t-cache-probe.yml` | `0bf4550e0bcba016213ceec6c260ae0180001c9c` | bounded exact-cache probe |
| `c10-s-focal-harness-tests.yml` | `129c74e101910c2eaa877ef82da4c699247d199e` | C10-S harness compile and deterministic tests |

The assumed `.github/workflows/c10-s-vcont-benchmark.yml` path does not exist at the inspected research ref. The earlier NOT_FOUND result was correct but did not mean there were no C10-S workflows; this inventory now resolves that gap.

## 4. Historical recovery of the relevant workflows

GitHub path-specific commit history was recovered:

### 4.1 P178 Analyzer Monte Carlo
- `e592de8f1aa8a40f84571ca7304d205b24ac24bc` — 2026-11-11 19:03:18Z, “Add bounded GitHub Actions workflow for P178 Analyzer Monte Carlo”.
- `689c8f0164e0625ca536a20b1805e555cd63d5fd` — 2026-11-11 19:03:50Z, “Fix GitHub Actions expression interpolation”.

### 4.2 P178 clean replay
- `4b2236727bf24889e3f071f22c53dc8312ed78b5` — 2026-11-11 19:55:07Z, “Add isolated clean replay for completed P178 Analyzer Monte Carlo”.
- `fc0839f53d3d09ae2764909bbf13a6ef896042a1` — 2026-11-11 23:30:12Z, “Trigger exact P178 Analyzer clean replay”.

### 4.3 P178 performance diagnostic
- `3bd61ac1520be23fd248fd17de7755ad0140dca7` — 2026-11-11 23:14:57Z, “Add bounded P178 replay performance diagnostic”.

### 4.4 C10-S focal harness tests
- `e8dd7f06ebd459a7e13f417c3b92961aadb8b586` — 2026-11-11 18:36:42Z, initial GitHub Actions execution for focal harness contract tests.
- `80fd9b06dd9b4c9fbfe57e6796de157d5ade29fa` — pinned numerical environment.
- `aba70f2c6ba6b033890e2c03ad62c097bf005dd1` — include P178 reference source in clean replay archive.
- `e34c6702bff74cb406451e31a198dfbc59546796` — include P178 reference CSV in clean replay archive.
- `88f89696bcf919774b39934ab36ee32107667982` — compile integrated Vcont harness and tests explicitly in Actions.
- `142821f3da8988738a102489a2631145e1abbf9f` — compile quantitative benchmark protocol in C10-S CI.

These histories show that the focal harness workflow was progressively extended to compile the Vcont integrated harness and benchmark protocol. They do not show a trusted artifact-signing workflow or an attestation trust boundary.

## 5. Security and suitability audit

All five C10-S workflow files were inspected. The four execution/test workflows and the cache probe share the following relevant properties:

- They grant `contents: read`; none declares `id-token: write`, `attestations: write` or `artifact-metadata: write`.
- They use mutable action tags such as `actions/checkout@v4`, `actions/setup-python@v5` and `actions/upload-artifact@v4`, not full commit-SHA pins.
- They upload ordinary workflow artifacts but do not create GitHub Artifact Attestations.
- The Monte Carlo, replay and test workflows run code from the research branch or a declared historical commit. Their existing role is execution/replay/testing, not a separately governed signing boundary.
- The performance diagnostic and cache probe pin a historical source commit; this is useful for reproducibility but does not authenticate a report package.
- The focal test workflow is triggered by pushes to the research branch and workflow_dispatch. It compiles and executes harness tests; it does not independently establish that its workflow definition and all code inputs are approved by a protected trusted-builder policy.

Therefore none of the five existing workflows is acceptable as a trusted signer **as-is**. Adding OIDC/signing permissions to one of these workflows without first isolating and governing the signing boundary would conflate code execution with authority to attest its own outputs.

This audit does not assert that mutable action tags have been exploited; it records that they are not immutable dependencies and do not satisfy the proposed trusted-builder policy.

## 6. Candidate and decision

The existing `c10-s-focal-harness-tests.yml` is the closest technical candidate for the deterministic code/test job because its history shows it compiles:
- `vcont_integrated_harness.py`;
- `test_vcont_integrated_harness.py`;
- `vcont_benchmark_protocol.py`;
- `test_vcont_benchmark_protocol.py`.

However, it is **not** selected as the signer. Its role may remain the unprivileged test job. A separate trusted builder/attestor should consume a finalized artifact only after:
1. the source commit is approved by the governed ref policy;
2. deterministic provenance reconciliation has passed;
3. the artifact is finalized and hashed;
4. the signing workflow definition is pinned and isolated from untrusted caller-controlled code;
5. the verifier checks the exact signer identity and subject digest.

The trusted builder must not rerun scientific or Monte Carlo work merely to sign a report. It should attest the exact finalized report package produced by an already authorized execution.

## 7. Gate 162 status

- Complete workflow inventory: RECOVERED.
- Research-vs-main workflow delta: AUDITED (50 main / 55 research; five C10-S additions).
- C10-S workflow histories: RECOVERED.
- Existing C10-S workflow as trusted signer: REJECTED AS-IS.
- Unprivileged focal harness workflow as technical test job: RETAINABLE, subject to ordinary code review.
- Dedicated trusted builder / attestor: REQUIRED; DESIGN OPEN.
- Verifier implementation: OPEN.
- Workflow changes or signing permissions: NOT PERFORMED.
- CI, attestation generation, calibration, seed-bank generation, N/R/M sizing, Monte Carlo benchmark and scientific execution: NOT EXECUTED / NOT AUTHORIZED.
- `main`: unchanged; PR #116 remains Draft on its existing base.

## 8. Next operation

Gate 163 should define the dedicated trusted-builder workflow and threat model: approved source refs, artifact hand-off, immutable action revisions, minimal permissions, signer identity, and the verifier's exact accepted claims. Keep the existing C10-S test workflow unprivileged. Do not create or run the signing workflow until its security policy is reviewed and explicitly authorized.
