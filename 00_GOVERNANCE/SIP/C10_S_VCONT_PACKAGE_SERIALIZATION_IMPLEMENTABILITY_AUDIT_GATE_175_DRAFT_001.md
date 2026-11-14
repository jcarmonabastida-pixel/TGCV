# C10-S V_cont — Gate 175: static implementability audit of package serialization

**Status:** STATIC AUDIT COMPLETED — CONDITIONAL / SERIALIZER NOT READY  
**Branch:** `research/c10-s-consolidation-draft`  
**Audited contract:** Gate 174 serialization and independent verifier  
**Source files:** `vcont_evidence_export.py`, `vcont_integrated_harness.py`, `vcont_benchmark_protocol.py`  
**Execution:** source inspection only; no imports, compilation, tests, CI, package generation, seed generation, calibration, benchmark or scientific execution

## 1. Executive verdict

Gate 174 is only partially implementable against the current source API. The core RUN/R evidence snapshots, per-world aggregate and benchmark report are available in memory. However, the current capture return type does not retain the exact matrix object consumed by the evaluator, does not carry calibration-bank evidence or independent source/test provenance, and the existing matrix fingerprint omits a declared matrix field.

**Do not implement the confirmatory Gate 164 packager against the current `CapturedBenchmark` interface yet.** A data-only serializer can be implemented only after the capture envelope is extended or supplied with separately retained, identity-bound companion inputs. No scientific object or estimator needs redesign.

## 2. Source/API inventory

| Required object | Actual source/API | Gate 175 finding |
|---|---|---|
| `MonteCarloBenchmarkDesign` | `CapturedBenchmark.report["design"]`; also input to producer | AVAILABLE in report; typed data-only projection still required |
| Exact 52-row `ScenarioEstimandSpec` matrix | Local `specs` in `produce_and_capture_benchmark()`; validated and passed to evaluator | **NOT RETAINED** in `CapturedBenchmark` or report |
| Matrix fingerprint | `design.matrix_fingerprint`, validated with `scenario_matrix_fingerprint()` | Declared fingerprint is not a complete commitment to all matrix fields; see §3 |
| Evaluation SeedAssignments | Each exact assignment is snapshotted in its owning RunEvidenceBundle | AVAILABLE across the 13×M×(1+R) snapshots; original bank order is not separately retained |
| Structural/per-run ScenarioConfig | Per-run config snapshot and structural digest in RunEvidenceBundle | Per-run available; structural registry requires explicit deterministic projection/deduplication |
| AnalysisContract | Per-run snapshots and digest | AVAILABLE; registry deduplication can be deterministic by complete canonical bytes |
| RunManifest, TruthProjection, EvidenceCandidate, SealedEvidence, AnalyzerResult, EvaluationReport | Per-run snapshots | AVAILABLE in memory; SealedEvidence rows+manifest are included in snapshot |
| RepeatedAssignmentReport | One snapshot in each OuterWorldEvidenceBundle | AVAILABLE once per scenario/M |
| Temporal manifest | `report["temporal_manifest"]` | AVAILABLE as reduced projection; joins to full snapshots are checked in producer |
| 52-pair ledger | `report["pair_ledger"]` | AVAILABLE, including M contributions, denominators and classifications |
| Calibration assignments/manifest | Not an input to `produce_and_capture_benchmark()`; producer accepts evaluation assignments only | **ABSENT — CONFIRMATORY BLOCKER** |
| Gate 159 reconciliation result | No input/output field or independent verifier API in the inspected harness | **ABSENT — CONFIRMATORY BLOCKER** |
| GitHub workflow/run/artifact resolution | Design contains declared `executable_commit`; no GitHub resolution interface in harness | EXTERNAL; must be injected from independent retrieval, not producer claims |
| Test execution evidence | No workflow-run/test-artifact input to CapturedBenchmark | EXTERNAL / ABSENT from capture |
| JCS serializer, TAR writer, package manifest verifier | No implementation found in the inspected three source modules | NOT IMPLEMENTED |

## 3. Exact matrix retention and fingerprint defect

`produce_and_capture_benchmark()` accepts `matrix=None`. It materializes either the supplied matrix or `build_scenario_estimand_matrix(versions)` into local `specs`, validates the design against it, passes it to `evaluate_monte_carlo_benchmark()`, and then returns:

- `report`;
- `outer_world_bundles`;
- `evidence_index`.

The exact `specs` object is not included in the returned `CapturedBenchmark`. The report retains `design.matrix_fingerprint` and the resulting 52-pair ledger, but neither is a lossless representation of all 52 matrix definitions. Rebuilding the default matrix later is not proof that it is the exact object passed at capture time, especially when a caller supplied a custom matrix.

A second defect is in `scenario_matrix_fingerprint()`: its tuple includes scenario/version, estimand/version, evaluation/run/repeated classes, truth status/field, analyzer output, aggregation field, identification expectation, abstention expectation and reason, but **omits `tolerance_id`**, which is a declared field of `ScenarioEstimandSpec`. Two matrices differing only in `tolerance_id` can therefore share the existing fingerprint.

Required resolution:
1. Retain the exact ordered 52 typed matrix rows in the capture envelope (or a companion immutable object bound by capture-time digest and exact design identity).
2. Preserve the legacy `matrix_fingerprint` for historical compatibility; do not silently change its semantics.
3. Add a separately versioned full-matrix digest covering every declared `ScenarioEstimandSpec` and nested `EvaluationKey` field, including `tolerance_id`, with an explicit canonical ordering.
4. Verify both legacy fingerprint and full-matrix digest independently. The full digest, not the legacy fingerprint alone, commits to the exact matrix.

## 4. Snapshot type registry and round-trip limits

The current `_SNAPSHOT_TYPES` registry includes SeedAssignment, AnalysisContract, AnalyzerResult, EvaluationReport, EvidenceCandidate, RepeatedAssignmentReport, RunManifest, ScenarioConfig, SealedEvidence, TruthBundle and MatrixTruthProjection. It does not include ScenarioEstimandSpec/EvaluationKey; those are not snapshotted today.

The generic encoder supports dataclasses, enums, tuples, lists, string-keyed dictionaries, null, strings, booleans, integers and finite floats. It rejects arbitrary bytes and non-string mapping keys. The decoder:
- returns an enum's decoded underlying value and does not restore the enum type;
- accepts generic untagged dictionaries;
- relies on dataclass constructor behavior rather than explicit exact field-set/version validation;
- uses ordinary `json.loads`, with no duplicate-key rejection;
- has no explicit per-type schema version or migration registry.

**Qualification:** the enum defect is a real generic decoder limitation, but the inspected current snapshot dataclass field definitions use string/Literal-style status fields; no enum-valued field was identified in the currently registered snapshot payload types. Therefore it is a latent compatibility/security gap, not proof that current RUN/R snapshots already lose an enum value. The package verifier must nevertheless reject unsupported enum-bearing payloads until a typed enum registry exists.

The current `FrozenSnapshot.restore()` is a source convenience method, not a sufficient independent package decoder. A package verifier needs strict UTF-8, duplicate-key rejection, exact top-level/nested type allowlists, exact field-set checks, schema-version checks and explicit construction rules. Arbitrary bytes must remain rejected unless a versioned lossless encoding is added.

## 5. Data that can be derived without scientific reconstruction

The per-run ScenarioConfig snapshots contain full effective configurations. The capture code computes a structural projection by removing `seed`, `world_seed`, `z_assignment_seed`, `g_assignment_seed`, `replicate_id`, `outer_replicate_id`, `assignment_role` and `assignment_index`. The projection can be deterministically regenerated from the retained snapshot under that exact named rule, and compared with the stored structural digest. This is a technical serialization projection, not a DGP reconstruction.

AnalysisContract snapshots can similarly be deduplicated by complete canonical snapshot bytes while retaining per-run references. Do not infer a registry entry from the AnalyzerResult alone.

The report contains the typed design, temporal manifest, pair ledger, manifest payload, scenario reports, coverage and legacy report fingerprint. It does not contain the exact matrix specs. Its design and report structures require explicit data-only adapters; `dataclasses.asdict` or generic JSON default hooks are not a complete schema contract.

## 6. Provenance and calibration boundaries

The producer accepts only evaluation-bank SeedAssignment rows and rejects other bank labels. The exact evaluation assignments are retained through per-run snapshots. Calibration rows are not passed to this capture API, and no calibration manifest or bank-separation proof is returned. The Gate 164 calibration file cannot be populated from evaluation records or inferred from the declared seed-bank fingerprint.

The design's `seed_bank_fingerprint`, `configuration_fingerprint` and `executable_commit` are declarations validated for shape, not independently recomputed or resolved by the capture API. Gate 159 reconciliation, GitHub workflow/run/attempt/artifact resolution, tested-source identity and technical-test workflow evidence remain outside this harness. The independent package builder/verifier must receive those as separately sourced inputs and mark them UNAVAILABLE/NOT_RECONCILED until actually verified.

## 7. Implementability matrix and required source changes

| Requirement | Current state | Minimum resolution |
|---|---|---|
| Serialize RUN/R snapshots | AVAILABLE | Versioned strict decoder + data-only adapters |
| Serialize M bundles and repeated report | AVAILABLE | Stable key/reference adapter |
| Serialize exact report and pair ledger | AVAILABLE | Explicit report schema/version and strict adapter |
| Export exact matrix used | BLOCKED | Retain exact matrix in CapturedBenchmark or immutable capture companion |
| Commit to every matrix field | BLOCKED | Add versioned full-matrix digest including tolerance_id |
| Export structural config registry | DERIVABLE | Freeze projection algorithm and verify against stored digest |
| Export AnalysisContract registry | DERIVABLE | Deduplicate by full snapshot bytes, preserve per-run refs |
| Export evaluation seed manifest | AVAILABLE IN RUN SNAPSHOTS | Materialize exact rows and verify complete cardinality/order |
| Export calibration seed manifest | ABSENT | Supply actual calibration manifest and independently verify disjointness |
| Gate 159 reconciliation | ABSENT | Separate deterministic reconciliation artifact/tool |
| External source/test provenance | EXTERNAL | Independently resolved GitHub workflow and artifact metadata |
| JCS/TAR and independent verifier | ABSENT | Implement only after above source gaps are closed |

## 8. Gate 175 disposition

- Gate 174 conceptual serialization contract: **DEFINED, QUALIFIED**.
- RUN/R snapshots and M-level bundles: **AVAILABLE IN SOURCE; runtime unverified**.
- Report and 52-pair ledger: **AVAILABLE IN SOURCE; runtime unverified**.
- Exact matrix payload: **NOT RETAINED; BLOCKER**.
- Existing matrix fingerprint: **INCOMPLETE COMMITMENT because tolerance_id is omitted**.
- Snapshot enum restoration: **GENERIC GAP; no current enum-valued registered snapshot field identified**.
- Strict independent decoder: **NOT IMPLEMENTED**.
- Calibration manifest and Gate 159: **ABSENT; CONFIRMATORY BLOCKERS**.
- External source/test provenance: **NOT PROVIDED BY CAPTURE API**.
- JCS/TAR packager and independent verifier: **NOT IMPLEMENTED**.
- Tests, CI, package generation and benchmark: **NOT EXECUTED**.

## 9. Next operation — Gate 176

Resolve the source-level blockers without implementing the serializer yet:
1. Define the exact matrix capture field and compatibility treatment for existing CapturedBenchmark consumers.
2. Define a versioned full-matrix fingerprint that includes every ScenarioEstimandSpec field, including tolerance_id, while retaining the legacy fingerprint.
3. Define the immutable calibration-manifest and Gate 159 reconciliation inputs as external, independently verified companion artifacts.
4. Freeze the strict snapshot decoder/type registry requirements and explicit current-field inventory.
5. Update Gate 174/164/166/172 cross-references as one integrated contract correction.

Only after Gate 176 should implementation readiness be reassessed. No benchmark, seed generation, calibration, test execution or scientific execution is authorized by this audit.
