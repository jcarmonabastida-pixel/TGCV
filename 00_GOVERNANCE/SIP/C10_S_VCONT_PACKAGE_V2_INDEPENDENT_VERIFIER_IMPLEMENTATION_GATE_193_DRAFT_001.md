# C10-S V_cont — Gate 193: independent package-v2 verifier implementation

**Status:** INDEPENDENT STRUCTURAL VERIFIER PARTIALLY IMPLEMENTED — STATIC REVIEW CONDITIONAL — NO TESTS EXECUTED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 192 — partial pure package-v2 writer  
**Normative predecessors:** Gates 164, 174, 178, 179, 181, 182, 188, 190, 191 and 192  
**Scope:** audit/correction of writer identity projections; independent archive, JSON/JCS, manifest, report, matrix and registered uint64 structural verification  
**Execution:** GitHub source/document inspection and source edits only. No imports, compilation, tests, workflow dispatch, package construction, producer invocation, seed generation, calibration or scientific execution.

## 1. Gate 193 audit findings against Gate 192

Static comparison of `vcont_package_v2.py` with the normative `derive_capture_identity` implementation and MatrixCapture construction found two defects in the Gate 192 writer boundary:

1. The writer converted `metric_targets` using `[list(row) for row in ...]`, which is not the complete source-safe conversion specified by the canonical identity algorithm. It now implements the same recursive source-domain rules independently: dataclasses, enums, string-key mappings, tuples/lists, finite floats and bounded integers. This preserves exact source types and rejects unsupported values rather than coercing them.
2. The writer compared MatrixCapture's compact `design_identity` to the full capture design identity. Those are different declared projections. It now checks the exact MatrixCapture projection: scenario versions, N, M, R and legacy matrix fingerprint.

A further digest-order defect was identified during report review: the historical Evaluator fingerprint is defined over source-domain integer values before uint64 wrapping. The writer now decodes the registered report wrappers in the legacy manifest projection before recomputing that fingerprint, while retaining the JCS snapshot digest over the wrapped v2.1.0 envelope.

These are source corrections only. They have not been compiled or executed. The report projection itself and Gate 181/188 frozen contracts have not been changed.

## 2. Independent verifier implementation

New module: `03_EXPERIMENTS/C10-S/harness/vcont_package_v2_verify.py`.

Public API:
`verify_package_v2(archive_bytes, *, expected_profile=None, trust_policy=None) -> PackageVerificationResult`.

The verifier does not import or call `vcont_package_v2` or any writer helper. It contains separate implementations for:
- exact package/report/matrix schema identity constants and 14-path inventory;
- strict UTF-8 JSON parsing, duplicate-key rejection, BOM rejection, non-finite constant rejection and exact one-trailing-LF enforcement;
- independent RFC 8785 canonical-byte comparison;
- strict TAR member/path/type/metadata checks, lexical order and exact inventory;
- independent deterministic USTAR reconstruction and byte-for-byte archive comparison;
- manifest exact field allowlist, profile/version/dependency checks, per-file byte lengths and SHA-256 recomputation;
- non-circular package ID derivation from package schema identity and manifest digest;
- FrozenReportSnapshot v2.1.0 envelope, historical report fingerprint, root/nested duplicate-view equality, 13-scenario and 52-pair coverage, M/R and temporal cardinalities;
- MatrixCapture v1.0.0 field allowlist, 52-row cardinality and full-matrix digest;
- all Gate 181 registered uint64 locations plus the four Gate 188 scenario-report pointers;
- exact wrapper grammar, canonical ASCII unsigned decimal and uint64 range;
- rejection of unregistered wrappers and direct seed fields outside the frozen pointer registry.

The verifier returns separate integrity, schema, completeness, identity, source-execution, technical-test and external-authentication statuses. It does not trust a producer-declared PASS or package status. A supplied `trust_policy` is rejected because no trust-policy/attestation verifier is implemented.

## 3. Critical semantic boundary — verifier remains partial

The current verifier does **not** claim full package conformance. These requirements remain open:
- decoding opaque legacy FrozenSnapshot payloads under the separately registered snapshot decoder and checking their type/schema identities and byte digests;
- exact RUN/R assignment ↔ ScenarioConfig ↔ RunManifest ↔ TruthProjection ↔ OuterWorldEvidenceBundle joins, including all run IDs and source seed equalities;
- calibration/evaluation seed disjointness from the actual calibration manifest;
- recomputation of Gate159 check results and `derived_status` from underlying rows/counts;
- exact field-level schema and semantic joins for every companion payload;
- recomputation of effective DGP/Generator/Analyzer configuration fingerprints from included payloads;
- independent resolution of source-execution claims against GitHub workflow/run/artifact metadata;
- binding technical-test evidence to a trusted workflow run, exact commit, commands and artifacts;
- cryptographic attestation verification under a separately governed signer/trust policy.

Accordingly, the result model intentionally reports:
- integrity: `PASS` only after archive/file/digest checks actually run;
- schema: `PARTIAL`, because the full companion schemas and semantic contracts are not yet verified;
- completeness: `STRUCTURAL_ONLY`;
- identity reconciliation: `NOT_VERIFIED`;
- source-execution provenance: `NOT_VERIFIED`;
- technical-test evidence: `NOT_VERIFIED`;
- external authentication: `NOT_AUTHENTICATED`.

The module has not yet been executed, so no actual package has received even this structural result. A static source review is not a verification result.

## 4. Pure verifier regressions

New module: `03_EXPERIMENTS/C10-S/harness/test_vcont_package_v2_verifier.py`.

Twelve methods cover:
1. exact 14-path uniqueness;
2. canonical JSON acceptance;
3. duplicate JSON key rejection;
4. whitespace/noncanonical and missing-LF rejection;
5. BOM and non-finite rejection;
6. uint64 boundary round-trips at 0, 2^53−1, 2^53 and 2^64−1;
7. bool/float/negative/overflow/malformed decimal rejection;
8. unsafe archive path rejection;
9. positive report fingerprint and duplicate-view structure;
10. divergent root/nested report view rejection;
11. registered uint64 pointer wrapper and row-count coverage;
12. unregistered wrapper/direct seed rejection.

These tests are written, not executed. They are deterministic pure tests and do not invoke any producer or seed-generation function.

## 5. Pure workflow scope

The existing `.github/workflows/c10-s-vcont-package-v2-pure-tests.yml` remains:
- `workflow_dispatch` only;
- `contents: read`;
- exact checkout of the dispatched commit;
- fail-fast restriction to `refs/heads/research/c10-s-consolidation-draft`;
- hash-locked `rfc8785==0.1.4`;
- explicit compilation and unittest module allowlists only.

Gate 193 adds `vcont_package_v2_verify.py` and `test_vcont_package_v2_verifier.py` to those allowlists. It does not add push/PR/schedule triggers, unittest discovery, integrated harness tests or producer execution. The workflow was not dispatched.

## 6. Version and compatibility

- Gate 164 package v1.0.0 remains frozen.
- Package profile remains `TGCV-C10S-VCONT-MC-PACKAGE@2.0.0`.
- RUN export envelope remains v2.0.0.
- Report dependency remains FrozenReportSnapshot v2.1.0.
- MatrixCapture remains v1.0.0.
- Gate 181 and Gate 188 remain frozen; no historical schema or fingerprint algorithm is rewritten.
- Historical report fingerprint, report snapshot JCS digest, capture_id/benchmark_export_id, package ID and archive SHA-256 remain distinct.

## 7. Current disposition

| Item | State |
|---|---|
| Canonical bootstrap from main | READ; RMA v3.38 and Evidence→Claim Matrix v1.47 resolved |
| Gate 192 capture identity source projection | Corrected in writer source; unexecuted |
| MatrixCapture design identity crosswalk | Corrected in writer source; unexecuted |
| Historical report fingerprint source-domain recomputation | Added in writer source; unexecuted |
| Independent archive/TAR verifier | Implemented partially |
| Strict duplicate-key/JCS parser | Implemented in source |
| Exact 14-file and manifest integrity checks | Implemented in source |
| Gate 181/188 uint64 registry structural checks | Implemented in source |
| Report 13-scenario/52-pair/M/R structural checks | Implemented in source |
| MatrixCapture full digest check | Implemented in source |
| Companion semantic schemas and joins | OPEN |
| Opaque FrozenSnapshot decoding/source joins | OPEN |
| Gate159 and calibration disjointness derivation | OPEN |
| GitHub source-execution/test evidence reconciliation | OPEN |
| External attestation verification | NOT IMPLEMENTED |
| Verifier tests | 12 written, NOT EXECUTED |
| Writer tests | 7 written, NOT EXECUTED |
| Capture tests | 27 written, NOT EXECUTED |
| Compilation / CI / workflow | NOT EXECUTED |
| Package generation | NOT EXECUTED |
| Producers, seeds, calibration, scientific execution | NOT AUTHORIZED / NOT EXECUTED |
| main / canonical governance | UNCHANGED |
| PR #116 | OPEN / DRAFT / ORIGINAL BASE RETAINED |

**Gate 193 verdict:** `PARTIAL INDEPENDENT STRUCTURAL VERIFIER IMPLEMENTED — STATIC REVIEW CONDITIONAL — NO TECHNICAL OR SCIENTIFIC EXECUTION.`

## 8. Next operation — Gate 194

Complete the companion crosswalk and independent semantic joins. Prioritize the RUN evidence envelope and exact snapshot reference/type/byte-digest decoder contract, then reconcile each report scenario/M RUN against assignment, ScenarioConfig, RunManifest, TruthProjection and outer-world key. Do not mark identity reconciliation PASS until those joins are independently recomputed. Continue to keep calibration/Gate159, external GitHub provenance, technical-test evidence and attestation as separate layers. No tests or workflow execution without separate technical authorization; no producers or scientific execution.
