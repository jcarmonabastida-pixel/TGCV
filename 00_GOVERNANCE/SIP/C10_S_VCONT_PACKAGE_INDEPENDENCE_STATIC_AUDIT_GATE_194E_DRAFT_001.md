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


## 10. Gate 194-E continuation — companion identity and effective structural configuration

### 10.1 Historical crosswalk reused

The exact eleven-companion inventory and source-authority crosswalk were recovered from the existing Gate 194-A artifact. No replacement crosswalk was created. Gate 194-A explicitly classifies companion completeness as partial and identifies the remaining field-level/source-resolution gaps; that historical disposition remains in force.

The writer source was inspected for every occurrence of `benchmark_export_id`. Under the current Gate 191/Gate 192 writer contract, the field is declared only in:
- `runs/run_records.json`;
- `validation/reconciliation_results.json`.

The verifier now validates the RUN export ID and requires the Gate159 companion to declare the exact same ID under its frozen schema/version. It does not add the field to the other nine companions. This is a declared-field join, not an independent derivation of capture_id.

### 10.2 EffectiveScenarioConfigProjection v2.0.0

Gate 181 §3 provides an exact row-level projection contract. The verifier now implements the following source-level checks:
- schema ID/version are exactly `TGCV-C10S-VCONT-EFFECTIVE-SCENARIO-CONFIG-PROJECTION@2.0.0`;
- exactly 13 rows in authoritative scenario order, with exact scenario/version/N keys from the report design;
- exact row field allowlist: scenario_id, scenario_version, n_units, generator_version, seed_policy and config;
- exact 26-field structural ScenarioConfig allowlist from Gate 181;
- exact explicit-stream seed policy, including forbidden fallback and the v3 seed algorithm;
- no direct seed or RUN/R identity fields in the structural config projection;
- exact equality of every structural projection with every decoded RUN/R ScenarioConfig snapshot for that scenario;
- generator_version equality with every corresponding RunManifest snapshot;
- exact consumption of M×(1+R) RUN/R snapshots per scenario, with no duplicate logical key.

The production verifier performs the independent snapshot decode and passes the decoded source objects into the pure row reconciler. The row helper is directly fixture-tested. This binds the structural companion to all per-run opaque config snapshots rather than merely comparing a declared digest.

**Deliberate limitation:** Gate 181 defines the projection schema ID/version and exact row schema, but does not state a complete root-object field allowlist. The implementation therefore does not invent one. It validates the required root declarations and exact row contract; exact root-envelope closure remains open and is not represented as complete companion schema conformance.

### 10.3 AnalysisContract companion remains open

The existing RUN/R verifier already decodes every AnalysisContract snapshot, validates the exact source type field registry, checks its retained snapshot digest, and reconciles semantic identity against RunManifest and AnalyzerResult. It correctly does not invent an `AnalysisContract.run_id`.

That does **not** close `design/analysis_contracts.json`. Gate 181 specifies an effective AnalysisContract projection and per-scenario/run-family source mapping, while Gate 194-A explicitly records that the exact package-level schema remains open. No guessed root schema, deduplication key or projection envelope has been added. This companion remains a distinct open item.

### 10.4 Fixtures and status

New unexecuted effective-config fixtures cover:
1. positive 13-row projection consumed by every RUN/R snapshot;
2. structural parameter drift in one source snapshot;
3. forbidden direct seed in the projection;
4. forbidden legacy seed fallback policy;
5. Generator.version divergence;
6. wrong row order;
7. duplicate row identity;
8. missing RUN/R consumption.

The benchmark-export identity fixtures from the preceding continuation remain unexecuted.

Source commits:
- benchmark export ID verifier: `16a0d4c4c67950e8c6159acfd3f2e73aaf7c0020`
- benchmark export ID fixtures: `fca7edd9b301e0a1fe5701d7dc6b509e12da5a8a`
- effective config verifier: `334915ad2309e248fe64d86b9669b490d5832104`
- effective config fixtures: `f273ac1b22de35122e60281e173bc714fd8022ea`

Latest reviewed blob identities:
- verifier: `73e05aa1da7c3f9609f1590b4d78c06c1ec080e8`
- test module: `529cc257558bc27e80cf646c5a7bfea20bf65b17`

Static text inspection found no imports from the writer, capture/export, integrated harness or benchmark-protocol modules in the verifier, and no temporary `and False`, empty-comprehension, TODO/FIXME or NotImplemented scaffolding in the verifier/test files. This is not a syntax check or execution.

**Disposition:** benchmark_export_id declared-field equality is IMPLEMENTED IN SOURCE / FIXTURES WRITTEN / NOT EXECUTED. Effective structural config row reconciliation is IMPLEMENTED IN SOURCE / FIXTURES WRITTEN / ROOT ENVELOPE PARTIAL / NOT EXECUTED. AnalysisContract companion schema remains OPEN. The five historical companion gaps are not all closed.


### 10.5 Fail-closed hardening

A follow-up static pass added strict integer validation for an optional `row_count`, nonempty string/integer validation for effective-config row identities, and a fail-closed exception boundary around the companion identity/config reconciliation calls. Unexpected decoding or shape errors are now surfaced as `PackageVerificationError` rather than leaking an unrelated exception type.

Verifier commit: `fd42afe16e9a82c1cb3bcec99ba03e6bc537a689`. Latest verifier blob: `73e05aa1da7c3f9609f1590b4d78c06c1ec080e8`. No test or compilation was performed.


## 11. Gate 194-E source audit — AnalysisContract companion boundary

A static source comparison was completed before attempting any `design/analysis_contracts.json` verifier implementation.

### 11.1 Facts established by existing source

- The registered source type is `vcont_integrated_harness.AnalysisContract`.
- Its frozen dataclass registry contains exactly 37 fields in the current inspected source.
- It has **no `run_id` field**. A verifier must not invent one.
- `RunEvidenceBundle.capture` validates the source AnalysisContract, checks its estimand, target/outcome, transportability and mechanism/reference-regime fields against AnalyzerResult and RunManifest, and computes `analysis_contract_sha256` using the historical tagged FrozenSnapshot source encoding.
- The per-run `analysis_contract` FrozenSnapshot is retained in `runs/run_records.json`. The run record's `analysis_contract_sha256` must equal the snapshot reference SHA-256; the independent decoder recomputes that SHA over the exact retained bytes.
- The current verifier already checks the AnalysisContract/AnalyzerResult estimand and target/outcome fields, transportability fields, and mechanism/reference-regime identity against RunManifest. These are per-run snapshot joins, not validation of the separate design companion.

### 11.2 What is not defined

The historical Gate 181 crosswalk describes `design/analysis_contracts.json` as an exact effective AnalysisContract projection with per-scenario/run-family identity and source mapping. Gate 194-A explicitly says the package-level schema remains open.

The inspected normative artifacts do not establish:
- the companion root schema ID/version and exact root field allowlist;
- the exact row schema and whether it contains source fields, a typed projection, or both;
- the canonical digest algorithm and its input domain for each companion row;
- the exact applicability key that maps a contract to a scenario/version/N and RUN/R family;
- whether identical contracts are deduplicated by snapshot digest or retained once per applicability key;
- how one companion row is consumed exactly once by the per-run snapshots without fabricating `AnalysisContract.run_id`.

The writer currently accepts this companion as a materialized object but does not validate its field-level schema. That is not a source contract.

### 11.3 Gate decision

No AnalysisContract companion schema or verifier code has been invented. The existing per-run AnalysisContract snapshot and semantic checks are retained; the independent companion remains OPEN.

The next bounded operation is to define and reconcile the companion's source-to-wire projection and applicability relation from the frozen Gate 181/191 requirements and current `AnalysisContract` source. If those documents do not determine a unique mapping, record the missing design decision explicitly before implementation. Do not treat a matching snapshot digest alone as proof that the companion is complete.

This preserves the distinction between:
- **per-run AnalysisContract snapshot identity:** implemented and checked by the RUN/R verifier;
- **design/analysis_contracts.json companion completeness and one-to-one applicability:** not yet specified or verified.


## 12. Gate 194-E continuation — AnalysisContract source and applicability audit

### 12.1 Exact source object established

The current registered `vcont_integrated_harness.AnalysisContract` dataclass contains exactly 37 fields. The independent verifier's closed source-field registry matches those 37 names. The object has no:
- `run_id`;
- `outer_replicate_id`;
- `assignment_role`;
- `assignment_index`;
- scenario ID/version or N fields.

The source factory `contract_for(cfg)` constructs the AnalysisContract from `ScenarioConfig`. Its current implementation reads structural/configuration properties (randomization, positivity, interference, measurement, focal-path and mechanism/regime declarations); it does not receive a SeedAssignment, RunManifest, run ID, outer-world ID or assignment role/index. It therefore does not create a run-scoped identity.

### 12.2 Source-to-snapshot digest is already defined

`RunEvidenceBundle.capture` stores `analysis_contract_sha256` as the historical tagged FrozenSnapshot digest of the AnalysisContract object. The independent verifier:
- strictly decodes each AnalysisContract snapshot under the closed 37-field type registry;
- recomputes the digest from the exact retained snapshot bytes through the independent decoder;
- requires the run record's `analysis_contract_sha256` to equal the snapshot reference digest;
- reconciles the contract's estimand/version, target regime, outcome, transportability declarations and mechanism/reference-regime identities against AnalyzerResult and RunManifest.

This is a per-RUN/R snapshot integrity and semantic join. It is not yet a check of the separate `design/analysis_contracts.json` companion.

### 12.3 RUN/R applicability fact

The factory `contract_for(cfg)` does not branch on RUN versus REPEATED_ASSIGNMENT. The RUN/R role is introduced in the subsequent RunEvidenceBundle capture key and in the SeedAssignment/ScenarioConfig/RunManifest identity join. Therefore, a proposed companion mapping that treats the two run families as two different AnalysisContract source objects would not be supported by the inspected producer semantics.

The normative Gate 181 crosswalk nevertheless requires an exact per-scenario/run-family identity and source mapping. The intended distinction appears to be applicability/consumption by run family, not a different contract object per role. That interpretation is supported by source structure but is not a substitute for an explicit wire schema.

### 12.4 Remaining normative decisions — do not implement by guess

The following are still not fixed by Gate 181/Gate 191/Gate 194-A:
1. Companion root schema ID/version and exact root field allowlist.
2. Whether the 37-field source projection is stored once per scenario and referenced by two run-family applicability rows, or repeated in each family row.
3. Exact row key and controlled vocabulary for the run-family mapping.
4. Exact source-mapping representation: snapshot digest only, source projection plus digest, or another frozen mapping.
5. Whether the contract digest in the companion is the historical tagged FrozenSnapshot SHA-256 over the exact 37-field dataclass projection, or a separately declared JCS digest over a companion row. These are different digest domains and must not be conflated.
6. Exact cardinality and one-to-one consumption rule between companion mappings and the observed RUN/R snapshots.
7. Exact crosswalk from each companion row to the effective ScenarioConfig row and to `provenance/configuration_fingerprints.json`.

A plausible but **not approved** candidate is one source contract projection per scenario/version/N, with two explicit applicability mappings (RUN and REPEATED_ASSIGNMENT) that point to the same contract digest. This matches the current factory's role-independent construction, but must not be treated as a frozen schema until the mapping and digest domains are explicitly decided.

### 12.5 Disposition and next bounded operation

No `analysis_contracts.json` verifier code or tests have been added in this continuation. The correct next operation is a narrow contract-resolution step: retrieve the exact Gate 178/179 configuration-fingerprint schema and the Gate 191 companion obligations, then resolve the seven decisions above against the existing producer output and historical contracts. If the normative material still does not determine a unique row schema, record a decision request and obtain explicit design acceptance before implementation.

**Disposition:** per-run AnalysisContract snapshot identity/semantic reconciliation remains implemented in source; separate companion schema and applicability remain OPEN. No producer, scientific component, DGP, estimand, seed generation or execution behavior was changed.


## 13. Gate 194-E continuation — configuration-fingerprint dependency audit

### 13.1 What the historical package contract actually requires

Gate 164 §3/§6.3 and Gate 181 §6 require `provenance/configuration_fingerprints.json` to contain canonical configuration-payload digests and recomputation records for:
- effective DGP/Generator configuration;
- Analyzer configuration/version;
- the authoritative matrix;
- the evaluation seed bank.

Gate 164 also requires `design/analysis_contracts.json` to represent the effective AnalysisContract and Analyzer configuration/version per scenario/run family. Gate 181 narrows the required verifier relation to recomputed structural-config and effective-analysis-contract digests compared against declarations.

These are verification obligations, not an exact companion schema. The inspected Gate 164, 178, 179, 181 and 191 texts do not define the root schema ID/version, exact record allowlists, canonical ordering, composite fingerprint algorithm, or complete cross-file dependency graph for `configuration_fingerprints.json`.

### 13.2 Source facts relevant to the digest graph

- `ScenarioConfig` has a frozen 26-field structural projection in Gate 181 §3; stochastic seeds and RUN/R identity are explicitly excluded.
- `Generator.version` is declared as `c10s-vcont-generator-0.1`.
- `Analyzer.version` is declared as `c10s-vcont-analyzer-0.1`.
- `AnalysisContract` has 37 exact fields and a per-run historical tagged-snapshot digest retained in each RUN/R record.
- The authoritative matrix has its own legacy fingerprint and independent full MatrixCapture JCS digest.
- Evaluation SeedAssignment rows have a separate ordered-manifest digest in capture identity; calibration is a separately supplied bank and is not part of evaluation capture identity.
- `MonteCarloBenchmarkDesign.configuration_fingerprint` is currently only validated as a 64-character hexadecimal declaration by the design validator. The inspected source does not define its input payload or derivation algorithm.

The source exposes Generator and Analyzer version strings, but no separate typed Analyzer-configuration object. Treating the 37-field AnalysisContract as the entire Analyzer configuration would be an additional design interpretation, not a fact established by the source or frozen schema.

### 13.3 Digest domains that must remain separate

At least five identities are in play and must not be silently substituted:
1. per-RUN/R AnalysisContract FrozenSnapshot SHA-256 over historical tagged source bytes;
2. any companion-row canonical JCS digest used for package file integrity;
3. component configuration fingerprints (DGP/Generator/Analyzer/matrix/seed bank);
4. the aggregate `MonteCarloBenchmarkDesign.configuration_fingerprint` declaration;
5. package file SHA-256 / package ID.

A companion may expose more than one of these, but each must have a named algorithm, exact input domain, schema version and derivation rule. A package file SHA-256 only proves the bytes in the package; it does not independently establish that a declared configuration fingerprint was derived from the correct source payload.

### 13.4 Unresolved design decisions

Before implementing either companion, the governing contract must settle:
- whether the AnalysisContract projection is one source row per scenario/version/N plus two applicability mappings, or a different explicit cardinality;
- whether the AnalysisContract snapshot digest is the canonical contract identity used by the companion;
- whether Analyzer.version plus AnalysisContract constitutes the Analyzer configuration identity, or whether an additional frozen Analyzer config payload is required;
- the exact aggregate algorithm and ordered inputs for `MonteCarloBenchmarkDesign.configuration_fingerprint`;
- whether the matrix and evaluation seed-bank fingerprints are included in that aggregate or remain separate component declarations;
- exact `configuration_fingerprints.json` root/row schemas and source mapping;
- how every declared component digest is independently recomputed and consumed exactly once.

No code or tests have been added for these unresolved contracts. No guessed aggregate hash or synthetic Analyzer configuration has been introduced.

**Disposition:** source facts and digest-domain boundaries are now documented; both `design/analysis_contracts.json` and `provenance/configuration_fingerprints.json` remain OPEN at schema/derivation level. The next implementation-ready step is not to write another guessed verifier helper; it is to resolve the aggregate configuration-fingerprint contract and its exact mapping to the already defined effective-config and AnalysisContract projections.


## 14. Gate 194-E — resolution matrix for configuration fingerprints

A further historical/source pass resolves several points that were previously grouped together as unspecified. The distinction below is now explicit: some payloads and recomputation duties are frozen; the aggregate algorithm and companion wire schema are not.

### 14.1 Normative elements already frozen and reusable

**Effective DGP/Generator payload**
- Gate 181 §3.1–§3.3 freezes the exact EffectiveScenarioConfigProjection@2.0.0 row: scenario_id, scenario_version, n_units, generator_version, seed_policy and the exact 26-field structural config.
- The row key/order and all stochastic/run-identity exclusions are explicit.
- Gate 164 §6.3 requires the effective DGP/Generator configuration to be included and its fingerprint recomputed from that payload.
- Gate 181 §7.2 requires a structural-config digest to change when any structural field changes and remain invariant to assignment-seed-only changes.

**AnalysisContract payload**
- Gate 181 §6 requires an exact effective AnalysisContract projection and per-scenario/run-family identity/source mapping.
- The source dataclass has exactly 37 fields. contract_for(cfg) creates it from ScenarioConfig; neither its factory nor its 37 fields contain RUN/R identity.
- The current Analyzer class exposes only version = c10s-vcont-analyzer-0.1 and an analyze(evidence, contract) method. No separate Analyzer configuration dataclass/object or configurable instance state is present in the inspected source.
- Gate 164 §3 and §6.3 require effective AnalysisContract and Analyzer configuration/version to be represented and their fingerprints recomputed.

**Matrix and seed-bank payloads**
- MatrixCapture v1.0.0 already supplies a full 52-row canonical matrix payload and its full JCS SHA-256, distinct from the historical matrix fingerprint.
- Evaluation SeedAssignment rows have a separately recomputable ordered-manifest digest, also used in capture identity. Calibration remains a separate manifest and disjointness check; it must not be silently merged into evaluation-bank identity.
- Gate 164 §6.2–§6.3 requires actual rows or immutable retrievable material to recompute seed-bank identity and disjointness.

### 14.2 Concrete source gap confirmed

MonteCarloBenchmarkDesign.configuration_fingerprint is only checked for 64-character hexadecimal syntax in validate_monte_carlo_benchmark_design. It is copied unchanged into the legacy report manifest and benchmark-design package projection. No source function in the inspected protocol defines its payload, component order, domain separation or derivation.

The package writer accepts design/analysis_contracts.json and provenance/configuration_fingerprints.json as caller-materialized mappings. It does not freeze their schemas or recompute their semantic fingerprints. This is consistent with Gate 191's boundary, but means the package currently has no source-of-truth algorithm for the aggregate declaration.

### 14.3 Candidate mapping that matches the producer (NOT FROZEN)

A source-compatible candidate for the AnalysisContract companion is:
- 13 scenario contract payloads, one per scenario/version/N, each containing the exact 37 source fields plus the Analyzer version;
- 26 explicit applicability rows keyed by (scenario_id, scenario_version, N, run_family), where run_family ∈ {RUN, REPEATED_ASSIGNMENT};
- each applicability row references the same scenario contract payload digest for both families;
- verifier consumes each applicability row against every corresponding RUN/R snapshot and verifies the exact historical snapshot digest separately.

This preserves the role-independent contract_for(cfg) source behavior while satisfying the Gate 181 per-scenario/run-family mapping. It is a candidate only: Gate 181 does not freeze the exact row/root schema, whether the 37 fields repeat in the 26 rows, or the companion digest domain.

### 14.4 Candidate non-circular fingerprint dependency graph (NOT FROZEN)

A possible versioned graph, to be explicitly accepted or amended before implementation, is:

1. **DGP/Generator component:** per-scenario digest over the exact Gate 181 effective-config row, including generator_version and seed_policy, using SHA-256 over RFC 8785 JCS bytes.
2. **Analyzer/contract component:** per-scenario digest over a versioned object containing the exact 37-field AnalysisContract projection and Analyzer.version, using a separately named SHA-256/JCS domain. The historical FrozenSnapshot SHA remains an independent byte-identity check, not a substitute.
3. **Matrix component:** reuse MatrixCapture's full JCS SHA-256; preserve the legacy matrix fingerprint as a separate compatibility declaration.
4. **Evaluation seed-bank component:** recompute the ordered evaluation assignment-manifest SHA-256 from exact materialized rows; keep calibration manifest digest/disjointness separate.
5. **Aggregate design fingerprint:** derive from a versioned, ordered component manifest containing the above component IDs, schema/algorithm IDs and digests. This aggregate would replace neither package ID nor capture_id.
6. **Configuration-fingerprints companion:** carry each component's source reference, algorithm/schema ID, declared digest and independently recomputable status; require exact consumption of every declared component.

The proposal intentionally does not specify a final schema ID, version, property names or byte-level object shape. Those are decision items, not facts recovered from the historical contracts.

### 14.5 Explicit decision required before code

The following questions must be answered in a bounded design decision:
- Approve or reject the 13-source-contract / 26-applicability-row mapping.
- Decide whether Analyzer.version plus AnalysisContract is the complete effective Analyzer configuration for this implementation, or whether the source must first expose a distinct Analyzer configuration payload. No such payload currently exists.
- Approve or replace the proposed per-component JCS digest domains.
- Define the ordered aggregate component set and exact MonteCarloBenchmarkDesign.configuration_fingerprint derivation.
- Decide whether the aggregate includes the evaluation seed-bank digest and MatrixCapture digest, and confirm that calibration remains separately declared.
- Freeze exact root/row schemas and exact-one-time consumption rules for both companion files.

**Disposition:** Gate 181 effective-config payload and recomputation obligations are DEFINED and already partly implemented in the verifier. Matrix and evaluation seed-manifest digest sources are DEFINED. The AnalysisContract source shape and Analyzer version are known, but its companion applicability schema remains OPEN. The aggregate configuration fingerprint and configuration_fingerprints.json schema remain OPEN. No implementation is added until the above design decision is explicitly accepted. No tests, compilation, workflow, producer, calibration or scientific execution was performed.
