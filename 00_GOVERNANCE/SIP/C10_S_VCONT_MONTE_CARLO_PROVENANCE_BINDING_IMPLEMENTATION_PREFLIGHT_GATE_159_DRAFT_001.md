# C10-S V_cont — Gate 159: Monte Carlo provenance-binding implementation preflight

**Status:** IMPLEMENTATION PREFLIGHT COMPLETED / CODE CHANGE REQUIRED  
**Branch:** `research/c10-s-consolidation-draft`  
**Governing audit:** `C10_S_VCONT_MONTE_CARLO_PROVENANCE_AUDIT_GATE_158_DRAFT_001.md`  
**Scientific execution:** NOT AUTHORIZED  
**Calibration / evaluation seed-bank generation:** NOT AUTHORIZED / NOT EXECUTED

## 1. Purpose and historical reconciliation

Gate 158 established that the report digest protects internal payload integrity but does not authenticate the provenance labels supplied by the caller. Gate 159 must close F158-01 through F158-04 without weakening Gate 157's 52-pair ledger, M/R hierarchy, temporal classifications, or the targeted TRUTH_MISSING / INVALID_OUTPUT regression.

The existing helpers are reusable:
- `seed_bank_fingerprint(assignments)` computes a canonical digest over materialized SeedAssignment rows.
- `validate_seed_banks(calibration, evaluation)` checks bank labels, seed-stream disjointness, fixed world seed within M, distinct world seeds across M, RUN uniqueness and R-index uniqueness.
- Gate 157 already validates much of the per-run M/R temporal structure and fingerprints the report payload.

The gap is the absence of a single acceptance path that joins those helpers to the exact runs being aggregated.

## 2. Verified implementation gaps

The current benchmark Evaluator accepts `scenario_outer_runs` and `MonteCarloBenchmarkDesign`, but no canonical calibration/evaluation SeedAssignment manifests or runtime execution attestation. It therefore cannot independently recompute the evaluation-bank fingerprint, enforce bank separation against the actual calibration bank, or establish the source commit that produced Analyzer outputs.

The current RunManifest carries run, scenario, N, M/R role/index and world/Z/G seeds. It does not carry the bank identity or a cryptographically bound SeedAssignment-row identity. The benchmark aggregation path checks M/R identities and temporal consistency but does not join every RunManifest to exactly one canonical SeedAssignment row.

Configuration provenance is also not reconstructible from the current design's caller-supplied fingerprint alone. The effective scenario/DGP and Analyzer contracts must be canonicalized from the exact objects used for the evaluated runs.

## 3. Gate 159 design decisions

### 3.1 Canonical provenance bundle

Introduce one immutable provenance bundle supplied to the benchmark Evaluator, containing:
- the materialized evaluation SeedAssignment rows used to generate the runs;
- the materialized calibration SeedAssignment rows used to establish separation (or a separately verifiable calibration-bank manifest and digest);
- the execution attestation produced by the execution boundary;
- the canonical effective configuration payload, or the exact versioned objects from which it can be reconstructed;
- declared expected fingerprints and schema/version identifiers.

The Evaluator must validate the bundle before computing any pair summary.

### 3.2 Seed-bank binding

1. Validate calibration and evaluation banks together using the existing `validate_seed_banks()`.
2. Recompute the evaluation fingerprint from the exact evaluation rows supplied in the bundle.
3. Require equality with the design's declared evaluation-bank fingerprint.
4. Reject duplicate rows, missing rows, unexpected rows, wrong bank labels, duplicate assignment identities and any seed collision.
5. Reconcile every evaluated RunManifest to exactly one evaluation SeedAssignment using the full identity key:
   `(bank, scenario_id, scenario_version, N, outer_replicate_id, assignment_role, assignment_index)`.
6. Require exact equality of world, Z and G seeds. Reject zero matches and multiple matches.

A fingerprint is calculated over a canonical deterministic ordering of rows. Canonical sorting must be part of the schema; caller input order must not change the digest.

### 3.3 M/R/world reconciliation

For each scenario/version/N:
- the outer dictionary key must equal each row's `outer_replicate_id`;
- exactly one RUN with index -1 must exist per M;
- repeated assignments must be exactly indices 0…R-1;
- RUN and R rows within an M must share exactly one world_id and world_seed;
- distinct M identities must have distinct world IDs and world seeds;
- every evaluated run must map to one and only one canonical seed-bank row;
- the set of evaluated rows must equal the declared evaluation rows for the design scope, not merely be a subset.

The independent bank validator remains authoritative for calibration/evaluation seed-stream disjointness and is invoked by the report acceptance path rather than left as an optional utility.

### 3.4 Executable identity and attestation boundary

A Python Evaluator cannot prove its own source commit by inspecting a caller-supplied SHA string. The execution boundary must create an attestation from trusted runtime context (for GitHub Actions, the workflow commit identity and checkout identity), then bind that attestation to each generated run and the final report.

The attestation schema must include at least:
- repository identity;
- actual checked-out commit SHA;
- workflow/run identity where available;
- source-tree or source-archive digest used by the process;
- attestation schema/version;
- execution identity shared by all runs in the report.

The Evaluator must reject absent, malformed, inconsistent or caller/design-mismatched attestations. It must not infer the commit from the report's own declared field. A local execution without a trusted runtime attestation must be explicitly marked UNATTESTED and cannot receive a provenance-verified report status.

### 3.5 Configuration binding

Define a canonical configuration payload from the effective objects actually passed through Generator and Analyzer, including:
- scenario ID/version and all DGP parameters;
- N and temporal design;
- assignment mechanism identities, versions, hashes and support settings;
- analysis/estimand contract identities and versions;
- Analyzer configuration and relevant software/schema versions.

Canonicalize with stable key ordering, explicit numeric serialization, and rejection of NaN/infinity and unsupported values. Recompute the digest from the effective run objects and require equality with the declared configuration fingerprint. Do not accept a free-standing 64-hex string as proof.

### 3.6 Report acceptance and fingerprint order

The acceptance order is fail-closed:

1. validate provenance-bundle schema and completeness;
2. validate both banks and their disjointness;
3. recompute and compare evaluation-bank fingerprint;
4. validate execution attestation and compare commit/runtime identity;
5. reconstruct and compare effective configuration fingerprint;
6. reconcile all RunManifests to canonical SeedAssignment rows;
7. validate complete M/R/world structure and exact design-scope coverage;
8. only then evaluate/aggregate the 52 matrix pairs;
9. include the validated provenance bundle, attestation and validation outcomes in the report payload fingerprint.

The report's existing SHA-256 remains an integrity digest. It is not to be described as an external signature or proof against a malicious actor able to rewrite both report and digest. Any stronger authenticity claim would require a separately governed signing/key-management mechanism.

## 4. Required adversarial tests

The implementation must add deterministic tests proving rejection of:
1. one altered world/Z/G seed after the bank fingerprint is declared;
2. a missing or additional SeedAssignment row;
3. a duplicate canonical assignment row;
4. calibration/evaluation seed collision;
5. a RunManifest with no matching SeedAssignment;
6. a RunManifest matching more than one row;
7. swapped outer-replicate identity;
8. within-M world ID or world-seed inconsistency;
9. duplicate world ID or world seed across M;
10. RUN/R role-index mismatch or incomplete R indices;
11. mismatched actual execution commit versus declared executable commit;
12. absent or inconsistent execution attestation;
13. modified effective DGP/Analyzer configuration with unchanged declared fingerprint;
14. report fingerprint mutation after successful provenance validation.

Tests must also preserve the existing Gate 157 targeted classification regression and all 52-pair denominator/status semantics.

## 5. Compatibility and migration constraints

- Do not change the meaning of legacy `SeedAssignment.replicate`: it remains R; -1 remains the designated RUN.
- Do not redefine M, N, the four estimands, matrix classes, truths or temporal levels.
- Do not convert provenance failures into Analyzer abstentions, NOT_IDENTIFIED, TRUTH_MISSING or INVALID_OUTPUT. They are integrity/contract failures and must reject report acceptance.
- Preserve deterministic report reconstruction for identical validated inputs.
- Any compatibility path accepting legacy caller-supplied provenance labels must be explicitly marked UNVERIFIED and must not be eligible for a provenance-verified report.

## 6. Technical verification boundary

After code and tests are implemented, run compilation, the complete deterministic test suite and clean source-archive replay against the exact tested commit. The technical verification must include the adversarial tests above.

This gate does not authorize:
- calibration or evaluation seed-bank generation;
- N/R/M sizing or pilot runs;
- Monte Carlo benchmark execution;
- scientific execution or interpretation.

## 7. Gate 159 status

- Gate 158: AUDITED — CONDITIONAL; provenance binding absent.
- Gate 159 preflight: COMPLETED / PERSISTED.
- Gate 159 code implementation: OPEN.
- Gate 159 adversarial regression: OPEN.
- Scientific execution: NOT AUTHORIZED.
- Calibration / seed-bank generation: NOT AUTHORIZED / NOT EXECUTED.
- `main`: unchanged; PR #116 remains Draft on its existing base branch.


## 8. Implementation blocker found during Gate 159 continuation

A further integrity boundary must be resolved before implementing a provenance-verified acceptance status.

A Python process cannot authenticate its own source commit merely by receiving `GITHUB_SHA`, `GITHUB_RUN_ID`, a repository string, a source digest, or an `attested=true` field. Those values are process inputs and can be caller-supplied or modified. Comparing them with another caller-supplied design field only proves internal consistency, not origin authenticity.

Accordingly, Gate 159 must distinguish three levels:
- **PROVENANCE_DECLARED:** caller-provided metadata is syntactically valid.
- **PROVENANCE_RECONCILED:** seed rows, RunManifests, effective configuration and report inputs have been deterministically recomputed and matched.
- **PROVENANCE_AUTHENTICATED:** execution identity is supported by a trust mechanism external to the evaluated Python process, with a verifiable binding to repository, immutable commit/source digest, workflow run and produced report.

The current repository evidence inspected for this continuation does not establish an existing signed execution-attestation trust root or verifier. Therefore, a Python-only attestation dataclass or environment-variable comparison would be insufficient and must not be implemented or reported as authentication.

**Required architecture decision before code can claim authenticated provenance:**
1. Select and govern the external attestation mechanism and trust root (for example, GitHub artifact attestations with a pinned/verified issuer and repository/workflow identity, or an explicitly governed signing key and verification procedure).
2. Define the signed subject: source archive/tree digest and final report artifact digest, bound to repository, commit, workflow/run identity and attestation schema.
3. Define the verifier and fail-closed behavior for absent, invalid, expired/revoked or mismatched attestations.
4. Decide whether local/unattested technical runs may produce only `PROVENANCE_DECLARED` or `PROVENANCE_RECONCILED` reports, never `PROVENANCE_AUTHENTICATED`.
5. Only then implement the external verification adapter and adversarial tests.

This does not block deterministic implementation of seed-bank fingerprint recomputation, calibration/evaluation bank separation, canonical SeedAssignment-to-RunManifest one-to-one joins, or effective configuration fingerprint reconstruction. Those can be implemented as **reconciliation**, but must not be conflated with authentication.

### Gate 159 status update

- Seed/configuration/manifest reconciliation: implementation OPEN.
- External execution-attestation trust mechanism: ARCHITECTURE DECISION REQUIRED / BLOCKED.
- Provenance-authenticated report status: BLOCKED until the trust root and verifier are governed.
- Gate 159 as a whole: OPEN; no authenticated provenance claim is permitted.
- No code, tests, CI, seed-bank generation, calibration, N/R/M sizing, Monte Carlo benchmark or scientific execution was performed in this continuation.

## 9. Gate 159 continuation crosswalk against package-v2 implementation (2026-11-14)

This update reconciles the original Gate 159 obligations with the later Gates 166–194-I. It prevents both reimplementing work already present in the package verifier and incorrectly treating partial v2 coverage as closure of Gate 159.

### 9.1 Deterministic elements already implemented in later source

| Gate 159 obligation | Later implementation evidence | Current classification |
|---|---|---|
| Evaluation SeedAssignment ↔ RunManifest one-to-one identity and exact seed equality | Gate 194-C RUN/R semantic reconciliation in `vcont_package_v2_verify.py` | IMPLEMENTED IN SOURCE; covered by the Gate 194-I pure suite, but not validated against a real package |
| RUN/R role/index, M/world identity, temporal rows and report contribution joins | Gate 194-C/D verifier reconciliation | IMPLEMENTED IN SOURCE; pure fixture suite passed; real-package validation absent |
| Effective structural DGP/Generator configuration reconstruction | Gate 181 projection plus Gate 194-I configuration companion | IMPLEMENTED IN SOURCE; independent verifier recomputes the registered configuration components |
| AnalysisContract and Analyzer-version binding | Gate 194-I 13 source contracts / 26 applicability rows, 37 fields, 28 component aggregate | IMPLEMENTED IN SOURCE; pure fixture suite passed |
| Evaluation assignment seed derivation from declared descriptor | Gate 194-I.4 writer/verifier recomputation of every evaluation world/Z/G seed | IMPLEMENTED IN SOURCE; 94 pure tests passed |
| Matrix and report coverage linkage | Gates 176/178/181 and 194-C/D/E | IMPLEMENTED IN SOURCE; structural/semantic package checks exist |

These are source and fixture-level implementation results. They do not establish a successful real-package round trip or runtime execution provenance.

### 9.2 Gate 159 obligations still not implemented

The current `vcont_package_v2.py` checks only the calibration companion's envelope schema/version/bank label/row-count and the Gate159 companion's schema/version/`benchmark_export_id`. It does not derive the Gate159 status from the actual check rows.

The independent verifier's final status vector explicitly records the following limitations:

- calibration/evaluation seed disjointness is not implemented in the package verifier;
- Gate159 derived-status recomputation is not implemented;
- source-execution metadata is not independently resolved against GitHub;
- technical-test evidence is not independently bound to a trusted workflow run/artifact;
- external attestation/signature verification is absent and the package remains NOT_AUTHENTICATED.

Accordingly, the remaining implementation work is not a general rewrite of RUN/R or configuration reconciliation. It is the narrowly scoped Gate159 companion layer:

1. Freeze/verify the exact calibration-manifest row schema and canonical ordering against Gate 178/179/181.
2. Recompute calibration and evaluation bank identities independently and invoke the existing bank-separation rule over the exact materialized rows. Check all required seed streams and report the exact denominator and collision set.
3. Define the exact Gate159 reconciliation artifact check registry, input references/digests, denominator/count/mismatch fields, allowed statuses and canonical ordering.
4. Recompute every check result from the package's actual calibration/evaluation assignments, RUN/R records, configuration components and report identity; do not accept caller-supplied PASS/status values.
5. Derive the aggregate Gate159 status fail-closed from the required check set, preserving UNAVAILABLE/UNVERIFIABLE separately from FAIL and never treating an empty check as success.
6. Add independent positive and adversarial fixtures for missing/extra/duplicate calibration rows, bank-label drift, every seed-stream collision class, wrong evaluation/calibration digest, altered check counts/status, omitted required checks, orphan/duplicate references and forged aggregate status.

### 9.3 Separate trust-boundary work — not part of deterministic reconciliation

Gate 163's dedicated attestor architecture remains a design, not an implemented trust service. The current five C10-S workflows inventoried by Gate 162 were not trusted signers. The package verifier deliberately does not infer authentication from caller fields or its `trust_policy` argument.

The following remain separate and must not be smuggled into the deterministic Gate159 result:

- independently resolving producer workflow ID/path, run ID/attempt, event, ref, commit, artifact ID and artifact digest from GitHub;
- binding the tested source tree/archive digest to the exact producer execution;
- independently resolving technical-test evidence;
- implementing and governing the trusted-builder workflow and its immutable action revisions;
- verifying the detached GitHub Artifact Attestation against the pinned repository/workflow/issuer/predicate policy.

Until that trust root and verifier exist, the maximum legitimate package status is deterministic RECONCILED with source/test provenance NOT_VERIFIED and external authentication NOT_AUTHENTICATED.

### 9.4 Current Gate 159 disposition

- Evaluation-side seed derivation, assignment joins, RUN/R structure and effective configuration: IMPLEMENTED IN SOURCE; pure tests PASS; real-package round trip NOT VERIFIED.
- Calibration/evaluation disjointness and Gate159 derived-status recomputation: OPEN.
- GitHub source/test provenance: OPEN / NOT VERIFIED.
- External authenticated provenance: BLOCKED pending trusted-builder implementation and verifier.
- Gate 159 overall: OPEN / CONDITIONAL; no authenticated provenance claim is permitted.
- Scientific execution, calibration/evaluation seed-bank generation and Monte Carlo execution: NOT AUTHORIZED / NOT EXECUTED.

**Next bounded operation:** perform a static schema-and-source crosswalk for the calibration manifest and Gate159 reconciliation artifact only, then freeze the exact check registry and derived-status algorithm before any implementation. Do not build a real package, invoke producers, generate seeds or execute calibration/Monte Carlo in that operation.

## 10. Gate 178 companion contract — exact Gate159 schema/source crosswalk (static, 2026-11-14)

The calibration and Gate159 companion schemas were recovered from Gate 178 §§6–8 and cross-checked against Gates 179/181 and the current package writer/verifier. This section records the normative requirements and the exact current implementation boundary.

### 10.1 CalibrationBankManifest v2.0.0

The v2 envelope retains the Gate 178 exact logical envelope and rows, versioned to v2.0.0 by Gate 179/181 with the typed uint64 wire projection:

- `schema_id = TGCV-C10S-VCONT-CALIBRATION-BANK-MANIFEST`;
- `schema_version = 2.0.0`;
- `bank = calibration`;
- non-empty `namespace`;
- exact `seed_derivation` descriptor: algorithm `TGCV-C10S-VCONT-SEED-v3`, hash `SHA-256`, output rule `first_8_digest_bytes_unsigned_big_endian`;
- calibration-specific `design` (ordered scenario IDs/version map, sorted N grid, M, R and declared purpose/targets);
- `row_count`, `rows`;
- `seed_bank_fingerprint_legacy`;
- versioned `manifest_sha256`;
- `execution_evidence_status` in `NOT_CAPTURED`, `AVAILABLE`, `UNVERIFIABLE`.

Each row's exact logical fields are: bank, scenario_id, scenario_version, n_units, replicate, outer_replicate_id, assignment_role, world_seed, z_assignment_seed and g_assignment_seed. The three seed fields use the exact Gate 179 uint64 object. `assignment_index` is not a second source field; it is the runtime alias of `replicate`.

Calibration row count is derived from its own design: `scenario_count × n_grid_count × M × (1 + R)`. It is not copied from evaluation design. Canonical order is authoritative scenario order, ascending N, ascending M, RUN first (-1), then R indices 0…R-1.

Required semantic checks: exact one RUN and contiguous R per scenario/version/N/M; fixed world seed within M; distinct world seeds across M; unique Z seeds and unique G seeds within M; pairwise-distinct world/Z/G within each row; calibration/evaluation union disjointness across all three streams; source-typed legacy fingerprint recomputation; independent JCS manifest digest recomputation. Calibration rows are not joined to evaluation RunManifests. Calibration execution links are conditional and missing evidence is UNAVAILABLE/UNVERIFIABLE, not an empty PASS.

### 10.2 Gate159ReconciliationArtifact v1.0.0

The exact envelope is:
`schema_id`, `schema_version`, `benchmark_export_id`, `design_identity`, `verifier_identity`, `input_artifacts`, `required_check_ids`, `checks`, `derived_status`, `findings_digest`.

Each exact check row is:
`check_id`, `check_version`, `scope`, `applicability`, `join_key_profile`, `expected_count`, `observed_count`, `matched_count`, `mismatch_count`, `mismatches`, `input_digests`, `status`, `reason`.

Allowed applicability: `REQUIRED` / `CONDITIONAL`. Allowed statuses: `PASS`, `FAIL`, `UNAVAILABLE`, `UNVERIFIABLE`, `NOT_APPLICABLE`. Counts are nonnegative exact integers or null only where the contract permits. Mismatch rows are ordered, bounded and data-only; they identify key, field, expected/observed digest or value reference and reason, without disclosing secrets or raw seed values.

The exact required check IDs, in frozen order, are:

1. `EVALUATION_ASSIGNMENT_RUN_MANIFEST_ONE_TO_ONE`
2. `CALIBRATION_EVALUATION_SEED_DISJOINTNESS`
3. `EVALUATION_SEED_FINGERPRINT_RECOMPUTATION`
4. `CALIBRATION_SEED_FINGERPRINT_RECOMPUTATION`
5. `EFFECTIVE_CONFIGURATION_FINGERPRINT_RECOMPUTATION`
6. `MATRIX_LEGACY_AND_FULL_DIGEST_RECOMPUTATION`
7. `SOURCE_EXECUTION_GITHUB_BINDING`
8. `TECHNICAL_TEST_RUN_BINDING`

Conditional check: `CALIBRATION_ASSIGNMENT_EXECUTION_LINK`, required only when calibration run outputs or N/R sizing claims rely on executed calibration records; otherwise NOT_APPLICABLE requires a documented seed-manifest-only calibration scope.

Derived status is not caller-authored:
- REJECTED if any required check is FAIL;
- NOT_RECONCILED if no required check fails but a required check is missing, UNAVAILABLE or UNVERIFIABLE;
- RECONCILED only when all required checks are present and PASS, and each conditional check is PASS or validly NOT_APPLICABLE with a documented reason.

### 10.3 Exact current source comparison

| Contract element | Current writer/verifier behavior after increments 1–2 | Finding |
|---|---|---|
| Calibration envelope and exact rows | Writer enforces v2 root/design/row allowlists; verifier independently enforces them | IMPLEMENTED IN SOURCE |
| Calibration design cardinality and canonical order | Derived from declared scenario/version map, N grid, M and R; exact row order checked | IMPLEMENTED IN SOURCE |
| Calibration seed derivation | Every world/Z/G uint64 is independently recomputed from declared namespace and source algorithm | IMPLEMENTED IN SOURCE |
| Calibration legacy fingerprint | Recomputed from source-typed row projection using the frozen historical JSON/SHA-256 algorithm | IMPLEMENTED IN SOURCE |
| Calibration manifest JCS digest | Recomputed over exact v2 envelope excluding only manifest_sha256 | IMPLEMENTED IN SOURCE |
| Calibration/evaluation disjointness | Full three-stream union intersection independently checked | IMPLEMENTED IN SOURCE |
| Gate159 root/nested schemas and ordered check registry | Exact root, verifier identity, input artifacts, nine check rows and mismatch structures validated | IMPLEMENTED IN SOURCE |
| Gate159 derived status and findings digest | Independently derived and compared with declared status/digest | IMPLEMENTED IN SOURCE |
| GitHub source execution and technical-test binding | Cannot be authenticated from package declarations; PASS is rejected without independent resolution | EXTERNAL / OPEN |
| Cryptographic attestation | No trusted signer/verifier | NOT_AUTHENTICATED |

The existing `validate_seed_banks()` helper is useful source logic but is not by itself the package acceptance contract: it does not establish the exact package-level calibration design cardinality/order, source fingerprint/JCS manifest digest, Gate159 check-row evidence or derived aggregate status. The independent verifier must implement/reconcile these from the serialized v2 inputs without trusting producer-supplied status.

### 10.4 Bounded implementation contract for the next code gate

The next implementation should be limited to the pure package boundary:

1. Add an independent calibration-manifest verifier with exact root/row allowlists, design-derived cardinality, canonical order, exact RUN/R coverage, role/index types, per-row stream uniqueness, within-M/world and cross-M checks, seed derivation recomputation from the calibration descriptor, source-typed legacy fingerprint and JCS manifest digest.
2. Recompute calibration/evaluation disjointness over the complete three-stream seed unions. Report counts and bounded mismatch references without raw seed disclosure.
3. Add a strict Gate159 check-registry validator for the exact eight required IDs/order plus the conditional calibration-execution check, exact root/row allowlists, duplicate/missing/extra checks, count/null semantics, input digests, allowed statuses and bounded mismatch structures.
4. Recompute all checks whose evidence is internal to the package. For GitHub source-execution and technical-test checks, require independently resolved evidence; absent evidence is UNAVAILABLE/UNVERIFIABLE and forces NOT_RECONCILED, never PASS.
5. Independently derive Gate159 `derived_status` and `findings_digest`; reject any caller-declared mismatch.
6. Add adversarial pure fixtures for calibration schema/cardinality/order/seed/fingerprint/disjointness and forged/missing/duplicate/extra Gate159 check rows/statuses.
7. Keep the current external-authentication output NOT_AUTHENTICATED. Do not add OIDC/signing permissions or a trusted workflow in this code gate.

No Generator, Sealer, Analyzer, Evaluator, DGP, estimand or seed-generation source is to be modified. No producer, seed-bank generation, calibration, package construction, benchmark or scientific execution is included. A separate technical-test authorization is required before compiling or executing tests if not already granted for this new verifier layer.
## 11. Gate 159 implementation increment 1 — calibration row reconciliation (2026-11-14)

Following explicit user authorization, the package boundary received a first bounded implementation increment:

- Writer: exact CalibrationBankManifest v2.0.0 root and row allowlists, required envelope fields, execution-evidence enum, typed uint64 decoding and exact seed-derivation descriptor validation.
- Independent verifier: calibration namespace/descriptor binding; per-row world/Z/G seed recomputation; source-typed legacy fingerprint recomputation; RUN/R group invariants; within-row stream distinction; fixed world seed within M; distinct world seeds across M; unique Z/G values within M; and full three-stream calibration/evaluation union disjointness.
- Nine adversarial/positive pure tests are now authored for the calibration verifier. They remain NOT EXECUTED.

The initial implementation increment did not yet enforce the full calibration design contract. The following correction is now implemented in source, using Gate 178 §§6.1–6.3, Gate 179 §4, Gate 181 §2.3a, Gate 156 and the existing source structures for seed-bank generation and MonteCarloBenchmarkDesign.metric_targets:

1. Exact design object allowlist and source-mapped fields.
2. Authoritative ordered scenario/version subset, sorted supported N grid, positive M/R dimensions, declared calibration purpose and pair/metric-keyed positive MCSE targets.
3. Design-derived row cardinality and exact scenario/N/M/R row order.
4. Independent JCS manifest digest recomputation over the complete v2.0.0 envelope with only manifest_sha256 excluded.

The Gate 178 design description was therefore not absent: it specified the dimensions, ordering and cardinality rule. The remaining implementation work was to map that contract to an exact nested wire projection and enforce it. This update corrects the earlier overstatement that the design/cardinality contract itself was missing.

### 11.1 Remaining Gate 159 boundaries

- The Gate159 envelope and check-row fields, eight required check IDs, conditional calibration execution check and derived-status rules are already defined in Gate 178 §7. Gate159 does not need a new catalogue.
- Exact nested wire constraints for verifier_identity, input_artifacts, mismatches, input_digests and the canonical findings_digest input still need one explicit crosswalk/decision before implementation.
- Source-execution GitHub binding and technical-test run binding require independently resolved GitHub evidence; they cannot be inferred from producer declarations.
- External cryptographic attestation remains a separate trusted-builder/signature verification layer.

No tests, compilation, package construction, calibration, seed generation, producer, benchmark or scientific execution was performed in these increments. The nine calibration tests are AUTHORED / NOT EXECUTED.

**Increment 1 disposition:** calibration design cardinality/order, per-row seed derivation, source-typed legacy fingerprint, manifest JCS digest, RUN/R invariants and three-stream cross-bank disjointness are IMPLEMENTED IN SOURCE; tests AUTHORED / NOT EXECUTED. Gate159 artifact derivation and external provenance remain OPEN. Gate 159 overall remains CONDITIONAL / OPEN.
## 12. Gate 159 nested companion wire crosswalk — calibration and reconciliation v1 (2026-11-14)

### 12.1 Calibration design projection v2.0.0

The exact nested `design` object in CalibrationBankManifest v2.0.0 is frozen for this package implementation as:

- `scenario_versions`: nonempty JSON array of exact two-element `[scenario_id, scenario_version]` arrays. Scenario IDs must form a unique ordered subsequence of `AUTHORITATIVE_SCENARIO_IDS`; versions are nonempty strings. An array is required because JCS canonicalizes object-member order and cannot preserve semantic scenario order in a JSON object.
- `n_grid`: nonempty ascending array of unique exact integers, each N >= 16 and divisible by four.
- `outer_replicates`: positive exact integer M.
- `repeated_assignments`: positive exact integer R.
- `calibration_purpose`: nonempty declared string. It identifies the purpose/scope but does not itself authorize calibration execution or imply that a numeric target has been accepted.
- `metric_targets`: nonempty array of exact objects `{scenario_id, scenario_version, estimand_id, estimand_version, metric, target_mcse}`. The scenario/version must be declared by `scenario_versions`; all identifiers are nonempty strings; `target_mcse` is finite and >0; the five-part metric identity is unique. The field mapping follows Gate 156/157's pair-keyed metric target contract and `MonteCarloBenchmarkDesign.metric_targets` source tuple.

Design-derived row count is `len(scenario_versions) × len(n_grid) × outer_replicates × (1 + repeated_assignments)`. Canonical rows are scenario order, ascending N, ascending M (`outer-000000`…), RUN (`replicate=-1`), then R (`0…R-1`). This is the wire-level realization of Gate 178 §6.3 and `build_seed_bank()`; it does not select or approve numeric N/M/R or MCSE targets.

### 12.2 Calibration manifest digest

Algorithm identifier: `TGCV-C10S-VCONT-CALIBRATION-MANIFEST-JCS-SHA256-1`.

Digest input is the complete CalibrationBankManifest v2.0.0 JSON object with only the `manifest_sha256` member removed. All other root fields, the complete exact design, row order, typed uint64 wrappers, legacy fingerprint and `execution_evidence_status` are included. Canonicalization is RFC 8785 JCS UTF-8; digest is lowercase SHA-256 hex. The digest is not self-included. This operationalizes Gate 178's versioned manifest JCS digest while preserving the Gate 179/181 typed uint64 projection.

### 12.3 Gate159ReconciliationArtifact v1.0.0 nested projection

Gate 178 §7 already freezes the root/check catalogue and derived-status semantics. The following nested constraints make that schema machine-verifiable without changing its root field inventory:

- `verifier_identity` is exactly `{name, version, source_commit, implementation_digest}`; name/version are nonempty strings, source_commit is a full 40-character lowercase Git commit SHA, and implementation_digest is a lowercase 64-character SHA-256 hex digest.
- `input_artifacts` is the exact ordered registry of ten package paths: `design/analysis_contracts.json`, `design/effective_scenario_configs.json`, `design/scenario_estimand_matrix.json`, `provenance/configuration_fingerprints.json`, `provenance/source_execution.json`, `runs/run_records.json`, `runs/temporal_manifest.json`, `seeds/calibration_seed_manifest.json`, `seeds/evaluation_seed_assignments.json`, `validation/test_evidence.json`. Each row is exactly `{artifact_id, sha256}`, ordered lexically by artifact_id; every digest is recomputed from the exact packaged bytes. Each check's `input_digests` must equal its frozen check-specific subset of this registry.
- `required_check_ids` is exactly the eight Gate 178 §7.3 required IDs, in their frozen order. `checks` contains those eight rows in the same order followed by exactly one conditional `CALIBRATION_ASSIGNMENT_EXECUTION_LINK` row.
- Every check row has the exact Gate 178 §7.2 field allowlist. `applicability` is REQUIRED for the eight mandatory rows and CONDITIONAL for the final calibration execution row. `scope`, `check_version`, `join_key_profile` and `reason` are nonempty strings.
- `input_digests` is a JSON object mapping nonempty artifact identifiers to lowercase SHA-256 hex digests. `mismatches` is an ordered array of at most 100 exact `{key, field, expected_ref, observed_ref, reason}` objects; all members are nonempty strings and raw seed values/secrets are prohibited.
- Counts are exact nonnegative integers (booleans rejected) or null under Gate 178 §7.2's availability rules. If observed_count, matched_count and mismatch_count are all integers, `matched_count + mismatch_count = observed_count`; mismatch_count equals the number of serialized mismatch records when that count is fully materialized. PASS requires zero mismatches and an empty mismatch list. FAIL requires at least one mismatch. NOT_APPLICABLE is valid only for the conditional check and requires an explicit seed-manifest-only scope reason. The verifier binds denominators as follows: check 1 counts evaluation assignment rows, temporal rows and RUN/R evidence records respectively; check 2 counts all three seed-field occurrences across both banks (not unique seed values); checks 3 and 4 each count one recomputed legacy fingerprint; check 5 counts the 28 effective-configuration fingerprint components; check 6 counts the 52 MatrixCapture rows; checks 7 and 8 each expect one external evidence binding but leave observed/matched/mismatch counts null until independent GitHub resolution; the conditional execution-link check expects the calibration row count when applicable and null counts only when validly NOT_APPLICABLE.

Gate159 `findings_digest` algorithm identifier: `TGCV-C10S-VCONT-GATE159-FINDINGS-JCS-SHA256-1`. Its input is the exact Gate159 root object with only `findings_digest` removed; `derived_status`, all ordered check rows, verifier identity, input artifact IDs/digests and design identity are included. Canonicalization is RFC 8785 JCS UTF-8; digest is lowercase SHA-256 hex. This is a non-circular integrity digest, not an attestation.

Derived status is recomputed from the complete required and conditional check set. Any FAIL in a required check (or an applicable conditional check) yields REJECTED. Missing required rows or required UNAVAILABLE/UNVERIFIABLE rows yield NOT_RECONCILED. RECONCILED is allowed only when all eight required checks PASS and the conditional check PASSes or is validly NOT_APPLICABLE with a documented seed-manifest-only reason. The verifier must compare the declared `derived_status` and `findings_digest` with these independent recomputations.

### 12.4 Independent evidence boundary

The deterministic package verifier can establish the internal checks from package payloads only after their respective independent source validators have passed. It cannot manufacture SOURCE_EXECUTION_GITHUB_BINDING or TECHNICAL_TEST_RUN_BINDING from producer declarations. Until a separately resolved GitHub source/test evidence object is available, those checks must be UNAVAILABLE or UNVERIFIABLE; therefore the derived status cannot be RECONCILED. External Artifact Attestation remains outside this artifact and remains NOT_AUTHENTICATED until a trusted builder and signature verifier are implemented.



**Historical-plan note:** §10.3–10.4 records the pre-implementation boundary. Its OPEN items for calibration schema/cardinality/fingerprints/disjointness and deterministic Gate159 artifact reconstruction are superseded by implementation increments §§11–13. The remaining external source/test binding and attestation limitations are still current.
## 13. Gate 159 implementation increment 2 — Gate159 artifact reconstruction (2026-11-14)

Following the calibration increment, the independent verifier now also:

- validates the exact Gate159 root allowlist and benchmark_export_id binding;
- validates verifier_identity and ordered input_artifacts nested projections;
- enforces the eight required checks in Gate 178 order plus the conditional calibration-execution row;
- validates exact check/mismatch field sets, status/applicability, count types/arithmetic, bounded mismatch records and seed-manifest-only NOT_APPLICABLE conditions;
- requires checks 1–6 to be PASS only after the corresponding package-internal independent verifications have passed;
- rejects producer-declared PASS for GitHub source-execution, technical-test and calibration-execution bindings that this verifier has not independently resolved;
- independently derives REJECTED / NOT_RECONCILED / RECONCILED and recomputes findings_digest over the exact Gate159 root projection excluding only findings_digest.

Eight additional deterministic adversarial fixtures were authored: valid NOT_RECONCILED, forged aggregate status, findings-digest drift, self-asserted external PASS, check-order drift, unregistered input digest, packaged-byte digest drift and invalid conditional NOT_APPLICABLE. Together with the nine calibration fixtures, 17 test methods are now authored for these increments.

**No tests or compilation have been executed.** The source updates and fixtures are persisted only on the research branch. No package was built; no seed bank, calibration, producer, benchmark or scientific execution occurred.

### 13.1 Current Gate 159 disposition

- Calibration manifest v2.0.0: design/cardinality/order, seed derivation, historical fingerprint, JCS manifest digest, RUN/R invariants and bank disjointness IMPLEMENTED IN SOURCE.
- Gate159ReconciliationArtifact v1.0.0: exact nested schema, check registry, derived status and findings digest IMPLEMENTED IN SOURCE.
- Source-execution GitHub binding: UNAVAILABLE / UNVERIFIED until independently resolved GitHub evidence is supplied.
- Technical-test run binding: UNAVAILABLE / UNVERIFIED until independently resolved workflow/run/artifact evidence is supplied.
- External cryptographic attestation: NOT_AUTHENTICATED.
- Gate159 overall: implementation present, but any package without independently resolved source/test bindings must derive NOT_RECONCILED; no authenticated or scientific claim is implied.

**Next operation:** static review the complete diff for calibration and Gate159 invariants, then request separate authorization for the deterministic technical test workflow. Do not run it as part of this implementation operation.