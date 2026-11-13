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
