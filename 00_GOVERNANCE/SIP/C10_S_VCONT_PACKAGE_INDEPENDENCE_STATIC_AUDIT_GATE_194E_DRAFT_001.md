# C10-S V_cont — Gate 194-E: static independence and contract audit (partial)

**Status:** STATIC AUDIT PARTIAL — FINDINGS CORRECTED IN SOURCE — REMAINING COMPANION AUDIT OPEN — NOT EXECUTED  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope reviewed:** independent FrozenSnapshot decoder, RUN/R semantic joins, report/MatrixCapture reconciliation, source provenance binding and imports/dependencies of the verifier  
**Normative comparison sources:** Gates 174, 181 and 188 contracts; current capture/export source inspected only as a comparison target, not imported or called by the verifier  
**Execution:** source retrieval and static inspection only. No imports, compilation, tests, CI, workflows, package construction, producers, seed generation, calibration or scientific execution.

## 1. Audit conclusion

The verifier remains structurally independent at the Python import boundary: the verifier source imports no writer, capture, harness or benchmark-protocol module. The FrozenSnapshot decoder uses its own closed registry and tagged-grammar validation, and the archive is reconstructed independently rather than through the package writer.

The audit was not sufficient to declare the entire package verifier independently complete. It found and corrected three classes of semantic gaps:
1. internally valid SealedEvidence provenance was not fully bound to the exact RUN/R source identity or AnalyzerResult provenance digest;
2. the report design view was not explicitly required to equal the legacy manifest design view;
3. the 52 MatrixCapture/pair-ledger identities were not tied to the frozen authoritative 13-scenario × 4-estimand universe.

The corrected source remains uncompiled and unexecuted. Gate 194-E is therefore partial.

## 2. Finding E-01 — SealedEvidence provenance not bound to the RUN/R source

**Severity:** material semantic reconciliation gap  
**Disposition:** corrected in verifier source; fixtures authored, not executed

Before correction, the verifier:
- compared EvidenceCandidate rows/provenance to SealedEvidence rows/provenance;
- recomputed SealedEvidence provenance_sha256;
- checked the SealedEvidence legacy digest and AnalyzerResult.input_sha256.

It did not explicitly require the provenance fields to equal the decoded SeedAssignment, ScenarioConfig and RunManifest identity, nor require AnalyzerResult.provenance_sha256 to equal the recomputed provenance digest.

This permitted a self-consistent provenance object to be attached to a different RUN/world while retaining its own valid digest.

Correction: `_assert_sealed_provenance_identity` now binds run_id, scenario/version, world/version, replicate identity, assignment role/index, G/Z mechanism identities and hashes, reference regime, assignment-vector hashes, provenance digest and AnalyzerResult.provenance_sha256.

Fixtures added: positive binding, cross-world/run divergence and AnalyzerResult digest divergence.

## 3. Finding E-02 — report design and legacy manifest views lacked an exact join

**Severity:** material identity ambiguity  
**Disposition:** corrected in verifier source; package-level fixture remains open

The report contains both a design projection and a legacy manifest. The RUN/R reconciler previously derived scenario versions and N/M/R from the design projection, while report validation independently used manifest values. The two views were not explicitly required to agree on the complete design identity.

Correction: the verifier now requires equality of:
- ordered scenario/version registry;
- N, M and R;
- matrix fingerprint.

It also validates the design scenario registry against the frozen authoritative scenario order before constructing RUN/R keys.

## 4. Finding E-03 — MatrixCapture and pair ledger could agree on a non-authoritative universe

**Severity:** material semantic coverage gap  
**Disposition:** corrected in verifier source; adversarial fixtures authored, not executed

The initial Gate 194-D join compared MatrixCapture rows to pair-ledger rows, but only required 52 unique identities. A mutually consistent but non-authoritative scenario/estimand universe could therefore pass that helper.

Correction: the verifier now carries an explicit frozen registry, independent of producer imports:
- 13 authoritative scenario IDs in their frozen order;
- 4 authoritative estimand IDs in their frozen order;
- estimand version `001`;
- exact 52-row Cartesian sequence.

The report manifest and design registry must match the frozen scenario order. MatrixCapture rows must match the exact 13×4 identity sequence. Each pair-ledger key must equal the corresponding MatrixCapture key plus `MONTE_CARLO`, and the evaluation/truth classifications must agree.

## 5. Independence review

Static source inspection confirms:
- no imports from `vcont_package_v2`;
- no imports from `vcont_evidence_export`;
- no imports from `vcont_integrated_harness`;
- no imports from `vcont_benchmark_protocol`;
- FrozenSnapshot bytes are hashed before parsing and retained unchanged;
- historical snapshot bytes are validated using the historical serialization, not JCS;
- JCS is used for the package's own matrix/package digest contracts, not to rewrite snapshot bytes;
- no temporary `and False` guards or empty-comprehension scaffolding were found in the reviewed verifier and test modules.

The test module's import of `vcont_package_v2_verify` is expected: it is the module under test.

This review does not establish runtime independence, dependency closure, Python import behavior, syntax correctness or successful tests. Those require execution, which remains outside the current authorization boundary.

## 6. Remaining audit and implementation gaps

The following remain explicitly open and prevent a complete Gate 194-E disposition:

1. **Eleven companion files:** exact schema/crosswalk validation and semantic joins have not been completed for all companion payloads.
2. **benchmark_export_id:** equality across RUN export and all applicable companions remains unverified.
3. **Effective scenario configurations:** exact registry/cardinality/identity reconciliation against design and snapshots remains open.
4. **AnalysisContract companions:** exact one-to-one companion-to-snapshot identity and digest joins remain open.
5. **Calibration/evaluation separation:** disjoint seed-bank and assignment reconciliation remains unimplemented.
6. **Gate159:** derived status recomputation remains unimplemented and independent.
7. **Aggregates:** repeated and scenario aggregate statistics are compared to captured report projections, but their numerical summaries are not independently recomputed from primitive contributions.
8. **Source execution and test provenance:** GitHub commit/workflow/artifact bindings remain unverified.
9. **External authentication:** no governed signature/attestation verifier or trusted signer configuration is present; status remains `NOT_AUTHENTICATED`.
10. **Package-level adversarial fixtures:** no end-to-end fixture has yet mutated a package, recomputed every external digest/archive byte, and demonstrated rejection solely on a false semantic relation.

The last item is not to be simulated by claiming a helper-level fixture is a complete package-level proof.

## 7. Source commits in this continuation

All changes are confined to `research/c10-s-consolidation-draft`:
- Gate 194-D MatrixCapture/pair-ledger join: `733471ba586f8967654aa76710db5fd3ce5e1927`
- Gate 194-D matrix adversarial fixtures: `e3dabf5f3d41d9b8e8f87add9229831975d488f4`
- outer-world reference resolver: `9adef7788d8d346c0721338b670da343af35a466`
- outer-world adversarial fixtures: `21861000c2409810881ff09943a3aa9b1b762ce9`
- report projection and unique-key assertions: `2e00b6f0939760721e939eb5dd4c8a46120ca244`
- duplicate-key and false-report fixtures: `dae3c1cd0b41f33f02cca0f0eca9d3103fc3a875`
- SealedEvidence provenance identity correction: `88b791cd8a4e35c0475e151fc175e73f18bc701a`
- SealedEvidence provenance fixtures: `45fb6389c6577224502ef2f40045c047c3916332`
- frozen scenario/estimand and report-design joins: `480f15985de1020bbaf98c2ade9367b287b95f3a`
- authoritative 13×4 matrix fixture update: `007d3a87784fc5c5f38621d8f9bae87709b30749`
- design identity in matrix fixture: `f5b8f0f0e3800284be3e94dfed91bdc8f33fb298`

Latest reviewed blob identities:
- verifier: `ec67fc389879c109da0592dbf19dae8ccb19184c`
- test module: `1ca5442cbc98848738e152dd9d38d3a67bc39f8b`

## 8. Gate disposition

**G194-D: PARTIAL IMPLEMENTATION / STATIC REVIEW CONDITIONAL / NOT EXECUTED.**  
**G194-E: PARTIAL STATIC AUDIT / THREE FINDINGS CORRECTED IN SOURCE / COMPANION AUDIT OPEN / NOT EXECUTED.**

The next operation should complete the companion crosswalk and semantic joins, beginning with exact `benchmark_export_id` linkage and the effective configuration/AnalysisContract registries. Package-level adversarial fixtures should follow only when they can be constructed from frozen inputs without invoking producers or generating seeds.

PR #116 remains Draft. No changes to `main`, historical frozen contracts or scientific components. Scientific execution remains unauthorized.


## 9. Gate 194-E continuation — exact benchmark_export_id crosswalk

A source-to-source crosswalk of the 11 non-capture companion paths was completed against the Gate 191 package-v2 writer contract. The important correction is that `benchmark_export_id` is **not** a universal field required in all 11 companions. The writer contract declares it only in the RUN export envelope and Gate159 reconciliation companion. Other companions carry their own domain identities and must not be forced to duplicate a capture identifier without a frozen contract requiring it.

| Companion path | Contractual benchmark_export_id field | Identity role |
|---|---:|---|
| `design/benchmark_design.json` | No | Frozen benchmark design |
| `design/effective_scenario_configs.json` | No | Effective scenario configuration registry |
| `design/analysis_contracts.json` | No | AnalysisContract registry |
| `seeds/evaluation_seed_assignments.json` | No | Evaluation-bank assignment rows |
| `seeds/calibration_seed_manifest.json` | No | Calibration-bank manifest |
| `runs/temporal_manifest.json` | No | RunManifest temporal projection |
| `runs/run_records.json` | **Yes** | RUN/R export envelope; ID must be a lowercase 64-hex SHA-256 string |
| `provenance/source_execution.json` | No | Source execution provenance |
| `provenance/configuration_fingerprints.json` | No | Configuration fingerprint registry |
| `validation/reconciliation_results.json` | **Yes** | Gate159 reconciliation; ID must equal RUN export ID |
| `validation/test_evidence.json` | No | Technical test evidence |

The independent verifier now calls `_reconcile_benchmark_export_identity` after RUN/R reconstruction. It requires both declared-ID companions, validates the RUN export ID's exact lowercase SHA-256 representation, checks the Gate159 schema/version, and rejects any mismatch between the two IDs. It does not infer identity from filenames or propagate an ID into companions whose frozen schema does not declare it.

Four unexecuted fixtures cover the positive cross-companion join, Gate159 divergence, malformed/missing identity and Gate159 schema-version drift.

Source commits:
- verifier: `16a0d4c4c67950e8c6159acfd3f2e73aaf7c0020`
- fixtures: `fca7edd9b301e0a1fe5701d7dc6b509e12da5a8a`

This closes the *declared-field crosswalk and equality check only*. It does not independently derive the capture identity from the complete set of snapshots and report/matrix digests, nor does it complete the semantic crosswalk of the other nine companion payloads.
