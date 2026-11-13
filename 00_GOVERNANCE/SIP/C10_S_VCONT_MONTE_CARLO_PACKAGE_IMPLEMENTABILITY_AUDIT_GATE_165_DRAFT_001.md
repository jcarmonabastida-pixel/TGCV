# C10-S V_cont — Gate 165: implementability audit of Monte Carlo package v1.0.0

**Status:** STATIC AUDIT COMPLETED / CONDITIONAL — PACKAGE CONTRACT NOT YET IMPLEMENTABLE AS WRITTEN  
**Branch:** research/c10-s-consolidation-draft  
**Scope:** read-only comparison of Gate 164 package requirements with current harness/protocol structures and return values  
**Execution:** no code execution, tests, CI, calibration, seed generation, N/R/M sizing or scientific benchmark execution

## 1. Audit basis

Read-only inspection of:
- 03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py
- 03_EXPERIMENTS/C10-S/harness/vcont_benchmark_protocol.py
- 03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py
- Gate 164 package schema v1.0.0
- main governance bootstrap and canonical state, per README operating procedure.

Observed source blob identities at audit time:
- vcont_integrated_harness.py: 88c6c7bd6f82353e64a4f12edbe2e2abc2cec002
- vcont_benchmark_protocol.py: 8511f289224a885bdc69b2b494f4e6dd345fa8b8
- test_vcont_integrated_harness.py: 8d9102c37f36f8fad14731797fb9796b11615097
- Gate 164 schema: 3be6a76e75fd8643c2e954e403d3e143bafe0b51

This is a static implementability audit, not a runtime verification or independent source-execution attestation.

## 2. Executive finding

Gate 164's package layout and data requirements are materially broader than the current integrated Evaluator return object. A subset is available or deterministically derivable from existing report structures. Several essential payloads are only partially represented, and several are absent from the current aggregation boundary. The current report is therefore not sufficient input to a compliant Gate 164 packager.

**Decision:** do not implement the packager against the current report dictionary by guessing or synthesizing missing provenance. First add an explicit, typed evidence-export boundary that carries the canonical source records into a package builder. This is a contract/interface extension, not permission to change code.

## 3. Field-by-field implementability matrix

Legend:
- **AVAILABLE** — present in current returned object or passed typed input.
- **DERIVABLE** — deterministically reconstructable from available data without inventing source facts.
- **PARTIAL** — some required fields exist, but the package requirement is not fully met.
- **ABSENT** — not carried by the current aggregation return boundary.
- **EXTERNAL** — must be resolved from GitHub/workflow metadata or a separately governed record.

| Gate 164 payload | Current evidence | Classification | Finding / required action |
|---|---|---|---|
| report/report.json | Evaluator returns coverage, 52-pair ledger, scenario reports, temporal manifest, manifest and report fingerprint | PARTIAL | The top-level report is available, but complete immutable source records and provenance are not included |
| 52-row scenario_estimand_matrix | Matrix is supplied to Evaluator or built from scenario versions; matrix fingerprint is declared in design | DERIVABLE, conditional | Serialize the exact matrix object used; recompute fingerprint. Do not reconstruct from report labels alone |
| benchmark_design | MonteCarloBenchmarkDesign carries scenario versions, N/M/R, matrix fingerprint, metric targets, seed-bank label/fingerprint, executable commit and configuration fingerprint | AVAILABLE, partial trust | Values are present as claims; they are not independently reconciled source provenance |
| effective_scenario_configs | ScenarioConfig objects are used by Generator but are not retained in the benchmark report return | ABSENT at report boundary | Must preserve exact effective config per scenario/version/N, including seed fields and all DGP parameters, before generation |
| analysis_contracts | AnalysisContract is passed per run in scenario_outer_runs tuples | PARTIAL | It is available transiently at evaluator input, but not serialized into temporal_manifest, pair_ledger or final return. Need canonical per-run/per-family capture |
| evaluation_seed_assignments | SeedAssignment schema/builder exists; RunManifest contains world/Z/G seeds, outer ID, role and assignment index | PARTIAL | Evaluator temporal_manifest carries only a reduced projection; no bank, namespace, typed SeedAssignment identity or canonical row fingerprint. Exact original SeedAssignment rows are not passed to Evaluator |
| calibration_seed_manifest | No calibration bank input in benchmark aggregation API/report | ABSENT | Requires actual calibration rows or immutable retrievable manifest, not just fingerprint |
| temporal_manifest | Evaluator emits one row per run with scenario/version/N/M/role/index/run/world and three seeds | PARTIAL | It omits RunManifest fields including replicate_id, world_version, interval/time fields, generator_version, assignment mechanism IDs/versions/hashes, assignment-vector hashes and probability-by-stratum; it is not a complete RunManifest |
| run_records | Evaluator input tuple includes TruthBundle, AnalyzerResult, AnalysisContract, RunManifest; SealedEvidence and EvaluationReport exist upstream in execute flow | PARTIAL/ABSENT | Aggregator input omits SealedEvidence and EvaluationReport is not in the tuple; returned scenario_reports retain only selected aggregate outputs. Full per-run truth/analyzer/contract records are not exported |
| source_execution | Design carries executable_commit claim | EXTERNAL + PARTIAL | No workflow run ID/attempt, repository/event/ref, source tree digest, producer artifact identity/digest or independently resolved GitHub metadata in report |
| configuration_fingerprints | Design carries configuration_fingerprint and seed_bank_fingerprint; matrix fingerprint also present | PARTIAL | No included effective config payloads, no independent recomputation record, and current seed fingerprint uses legacy JSON serialization rather than Gate 164 JCS |
| reconciliation_results | Gate 159 findings identify missing integrated validation; no reconciliation record in Evaluator return | ABSENT | Must be produced by an independently implemented validator from actual source rows and external metadata; producer-supplied PASS is insufficient |
| test_evidence | Historical workflow run details may exist in GitHub, but not in benchmark report | EXTERNAL | Must be resolved from exact workflow run/commit/artifact metadata; do not infer from source test files |
| manifest file inventory/digests | No package manifest or package builder currently exists | ABSENT | Deterministically construct only after all payloads are present and validated |
| package digest / attestation | No package builder, verifier or attestor currently exists | ABSENT | Later gates, not part of current report |

## 4. Concrete structural observations

### 4.1 Report aggregation boundary

The current Evaluator method `evaluate_monte_carlo_benchmark(scenario_outer_runs, design, tolerance, matrix)` receives scenario blocks whose run tuples contain `(TruthBundle, AnalyzerResult, AnalysisContract, RunManifest)`. It constructs:
- a reduced temporal manifest;
- a per-scenario Monte Carlo report;
- 52 pair-ledger rows with M-level contributions and status/numeric denominators;
- a report manifest and internal report fingerprint.

The return value does not preserve all input tuples as a complete run-record ledger. A package builder that consumes only this return value cannot recover omitted values.

### 4.2 Missing run-level objects

The upstream `execute_world` test helper demonstrates the actual execution chain: Generator -> Sealer -> Analyzer -> Evaluator. SealedEvidence and EvaluationReport are real typed objects, but the benchmark aggregation tuple does not include them. Gate 164 asks for sealed input/output digests and per-run evaluation records. They cannot be reconstructed from the reduced report without changing the evidence-export contract.

TruthBundle is also broader than the four scalar truths used by the pair ledger. Preserve the fields actually needed by the frozen matrix and audit; do not dump unrelated potential-outcome arrays by default if the data-minimization contract can specify the required subset.

### 4.3 Seed identity

SeedAssignment includes bank, scenario/version, N, legacy replicate (R index), world seed, Z seed, G seed, outer ID and assignment role. Its property `assignment_index` aliases `replicate`. The current Evaluator manifest instead projects RunManifest fields and does not include bank or namespace. RunManifest's `replicate_id` is not interchangeable with SeedAssignment's integer R index.

The package must join actual SeedAssignment rows to RunManifest by the full typed identity; deriving a seed assignment row from a RunManifest projection would be an unsupported reconstruction unless the derivation inputs and algorithm version are themselves retained and independently validated.

### 4.4 Fingerprint compatibility

- Current `seed_bank_fingerprint` hashes a JSON serialization using sorted keys and compact separators, preserving the input row order. It is not the Gate 164 JCS package serialization.
- Current report fingerprint uses the harness's internal `_hash` path over a JSON-normalized manifest payload. Gate 164 correctly treats this as a separate legacy report fingerprint.
- The package builder must compute new JCS payload and file digests independently; it must not relabel existing fingerprints as JCS or overwrite their semantics.

### 4.5 Invalid-output classification

The current pair-ledger code explicitly emits TRUTH_MISSING and INVALID_OUTPUT when a contribution is nonnumeric after the preceding status branches, and separately counts both states. This is a positive existing invariant. However, this audit did not execute the code or verify the latest regression suite; classification is **STATICALLY PRESENT, RUNTIME UNVERIFIED** for this gate. Preserve the classification and add package round-trip/adversarial tests later.

## 5. Minimal evidence-export contract required before packager implementation

The benchmark execution boundary must retain, per scenario/M/role/R:
1. exact ScenarioConfig effective payload and its canonical identity;
2. exact SeedAssignment row and bank/namespace identity;
3. complete RunManifest;
4. TruthBundle fields required by the 52-pair matrix;
5. SealedEvidence manifest and digest (or an explicit governed decision to omit sealed rows while retaining verifiable digests);
6. AnalyzerResult and exact AnalysisContract;
7. EvaluationReport or the exact per-run evaluation record used by the report;
8. scenario/M/R identity and source execution reference.

At benchmark level, retain:
- exact MonteCarloBenchmarkDesign and authoritative 52-row matrix;
- complete calibration manifest or immutable content reference resolvable by the verifier;
- producer workflow execution identity and artifact reference (resolved externally by the attestor, not trusted from producer claims);
- independently generated Gate 159 reconciliation result;
- technical test evidence references, each bound to exact workflow run and commit.

This export must be immutable, typed, complete and data-only. It must not execute additional simulation, generate seeds, infer absent records or upgrade provenance status.

## 6. Corrections to Gate 164 before implementation

1. **Separate package schema from evidence availability.** Keep Gate 164 as the target package contract, but label fields whose sources are external or absent; do not claim the current report can already satisfy the schema.
2. **Clarify `effective_scenario_configs.json`.** ScenarioConfig currently includes seed and assignment fields. Define a canonical DGP configuration projection that separates structural scenario parameters from per-assignment seed/identity metadata, while retaining both source objects and a deterministic link. Otherwise the same config file conflates DGP invariants with M/R-specific assignment state.
3. **Clarify `analysis_contracts.json` cardinality.** Contracts are passed per run and may vary by scenario; package schema must specify whether one canonical contract per scenario/version is sufficient or whether each run's exact contract identity is retained.
4. **Add an explicit `evidence_export_manifest` or typed `run_evidence_records` payload.** Current files do not identify a stable complete source record set.
5. **Do not require source execution claims to be authored by the producer as authoritative.** Store producer assertions separately from attestor-resolved GitHub metadata.
6. **Do not label test evidence as benchmark-run provenance.** Technical test runs and scientific benchmark runs are distinct execution classes.
7. **Do not require full TruthBundle arrays unless scientifically necessary.** Include the minimal matrix-relevant truth fields plus source digest/reference to avoid unnecessary sensitive/large payload.
8. **Add package validation outcome for each invalid/missing record.** A package must retain the failure rather than silently omit the offending run.

## 7. Gate 165 verdict

**AUDITED — CONDITIONAL / NOT IMPLEMENTABLE AS WRITTEN FROM CURRENT AGGREGATOR OUTPUT.**

Available/derivable: design identity fields, 52-row matrix (if exact matrix is retained), 52-pair report ledger, M-level contributions, coverage, status/numeric denominators, reduced temporal manifest, current report fingerprint.

Partial: effective configuration, AnalysisContract, SeedAssignment, RunManifest, run records, seed/config fingerprints, source-execution identity.

Absent or external: calibration manifest, SealedEvidence/EvaluationReport per-run export, Gate 159 reconciliation result, GitHub-resolved producer workflow/artifact identity, package manifest/archive/digest, test evidence binding.

**No code, tests, workflow or CI changes were made. No tests or compilation were run. No calibration, seed-bank generation, N/R/M sizing, Monte Carlo or scientific execution was performed or authorized. main remains untouched; PR #116 remains Draft on its existing base.**

## 8. Next gate

**Gate 166 — freeze the typed evidence-export interface and source-of-record cardinalities.** Specify the exact immutable per-run record, benchmark-level envelope, join keys, data-minimization boundary and provenance split required to make every Gate 164 package field available without reconstruction. Do this before implementing the packager or trusted attestor.
