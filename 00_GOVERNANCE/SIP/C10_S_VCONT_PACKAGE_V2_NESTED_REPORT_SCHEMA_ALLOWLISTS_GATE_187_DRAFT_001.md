# C10-S V_cont — Gate 187: nested report schema allowlists and cardinality

**Status:** CONDITIONAL — NESTED SOURCE ALLOWLISTS IMPLEMENTED; GATE 181 UINT64 REGISTRY OMISSION BLOCKS FULL CONFORMANCE  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 186 capture source audit  
**Scope:** exact nested report schemas and cardinality checks for FrozenReportSnapshot v2.0.0  
**Execution:** GitHub source inspection and source/test/document edits only. No imports, compilation, tests, CI dispatch, dependency installation, producer invocation, seed generation, calibration, package generation or scientific execution.

## 1. Historical and source basis

Gate 187 followed the mandatory canonical recovery path:
- `00_GOVERNANCE/README.md`, `CHATGPT_BOOTSTRAP.md`, `CANONICAL_STATE.json` and `STATUS.md` from `main`;
- canonical RMA v3.38, Evidence→Claim Matrix v1.47, RMA traceability v3.38 and Governance Operating Principles v0.1;
- historical reconstruction and technical execution workflows;
- Gates 178, 181, 182, 184, 185 and 186 on the research branch;
- actual source construction in `vcont_integrated_harness.py`, summary dataclasses in `vcont_benchmark_protocol.py`, and capture projection/tests in `vcont_evidence_export.py` and `test_vcont_capture_v2.py`.

The canonical pointers and declared versions agree at the source level. The local read-only validators were not run because no local execution environment was used; no validator PASS is claimed. The canonical TGCV Core, RMA and Evidence→Claim Matrix were not changed.

## 2. Nested allowlists implemented

The prior projection checked the report root and design/legacy manifest but recursively preserved unknown nested objects. Gate 187 adds exact field allowlists derived from the current Evaluator return construction and source dataclass declarations.

### 2.1 Temporal manifest

Every row must contain exactly:
`scenario_id`, `scenario_version`, `N`, `outer_replicate_id`, `assignment_role`, `assignment_index`, `run_id`, `world_id`, `world_seed`, `z_assignment_seed`, `g_assignment_seed`.

The projection now enforces exactly `13 × M × (1+R)` rows in authoritative scenario order, numeric M order, RUN first, then contiguous R indices. Root and nested legacy-manifest copies must match exactly after the registered uint64 projection.

### 2.2 Pair ledger

Every one of the 52 rows must contain exactly:
- identity: `key`;
- class/truth: `evaluation_class`, `truth_status`;
- denominators: `expected_M`, `observed_M`, `numeric_denominator`, `status_denominator`;
- counts: `missing_contribution_count`, `truth_missing_count`, `invalid_output_count`, `abstention_count`, `identification_correct_count`, `abstention_correct_count`;
- summaries: `identification_rates`, `run_identification_rates`, `metrics`;
- disposition: `precision_status`;
- ordered `contributions`.

The exact five-part key is checked against all 13 scenario IDs, their declared versions, all four registered estimands in matrix order, estimand version `001`, and metric scope `MONTE_CARLO`. Counts must be nonnegative exact integers (booleans rejected); denominators must reconcile to M; precision/class/truth values are allowlisted. Each row must contain exactly M contributions in numeric M order.

Each contribution has an exact 21-field allowlist derived from Evaluator construction. The registered `world_seed` is projected to the Gate 181 typed uint64 representation. Temporal source, contribution state and boolean fields are validated. Identification-rate blocks, binary summaries and bias/MAE/RMSE summary schemas are exact.

### 2.3 Scenario reports

The report must contain exactly the 13 registered scenario keys in authoritative order. Each scenario report has an exact root allowlist:
`scenario_id`, `scenario_version`, `n_units`, `outer_replicate_count`, `coverage`, `run_conditional`, `g_assignment_z0`, `mechanism_marginal`, `reference_regime`, `per_outer_replicate`.

Scenario identity/version/N/M are reconciled to design. Coverage and all four metric blocks have exact allowlists; continuous Monte Carlo, RMSE and binary-rate summary shapes are separately validated. Exactly M per-outer records are required in numeric order. Each per-outer record has exactly `outer_replicate_id`, `run`, `run_report`, `repeated_report`. The `run` projection must contain exactly four source objects in Evaluator tuple order: TruthBundle, AnalyzerResult, AnalysisContract and RunManifest, each checked against its source dataclass field set. EvaluationReport and RepeatedAssignmentReport shapes are also exact, with exactly R nested per-run reports.

Top-level coverage must equal the complete 52-pair / 13-scenario declaration. Root/nested temporal and pair-ledger equality remains enforced. Unknown nested fields now fail closed rather than being carried forward under the existing payload version.

## 3. Newly discovered blocker — Gate 181 uint64 registry is incomplete

The source inspection exposed an omission not recorded in Gate 181's direct uint64 pointer registry.

The Evaluator's `scenario_reports[*].per_outer_replicate[*].run` retains the original four-object RUN tuple. In that tuple:
- `run[0]` is a `TruthBundle`, whose `seed` is the world seed;
- `run[3]` is a `RunManifest`, whose `world_seed`, `z_assignment_seed` and `g_assignment_seed` are all uint64 seed values.

These source fields are present in the complete report projection required by Gate 181 §4.3, but the Gate 181 direct uint64 registry does not include the corresponding JSON Pointer paths:
- `/scenario_reports/*/per_outer_replicate/*/run/0/seed`;
- `/scenario_reports/*/per_outer_replicate/*/run/3/world_seed`;
- `/scenario_reports/*/per_outer_replicate/*/run/3/z_assignment_seed`;
- `/scenario_reports/*/per_outer_replicate/*/run/3/g_assignment_seed`.

This is a contract omission, not merely a test gap. The current projection wraps the registered root temporal and pair-ledger seed fields but does not transform these additional source occurrences. If any such value exceeds the exact JCS integer domain, canonicalization rejects it; even for smaller values, emitting the field as an ordinary JSON number would not satisfy a typed uint64 registry for the source semantic type.

Gate 187 adds a negative fixture vector for unsafe values in the omitted nested locations. The source is expected to fail closed; that vector has not been executed.

**No silent fix is applied.** Gate 181 freezes both the complete report projection and the direct uint64 registry. Changing the registry requires an explicit versioned contract amendment (candidate: FrozenReportSnapshot v2.1.0 with the four pointers above) or an explicit decision to change the complete-report projection requirement. Gate 188 must resolve that contract-level choice before any code begins wrapping these additional paths. Gate 187 does not change Gate 181 or relabel v2.0.0.

## 4. Source and test changes

- `vcont_evidence_export.py`: exact nested field allowlists; exact pair identity/order; temporal, pair-ledger, scenario/M/R cardinality; nested summary and source-object validation; registered uint64 projection retained.
- `test_vcont_capture_v2.py`: complete structural report fixture with 13 scenario reports, 52 pair rows, 13×M×(1+R) temporal rows and nested source-object structures; adversarial cases for nested unknown fields, pair contribution drift, temporal/pair cardinality and unsafe unregistered scenario-report seed values.

These are source/test authoring results only. No test, import, compilation or workflow was run. The fixture is structural and does not constitute a synthetic benchmark execution.

## 5. Conformance disposition

| Property | Gate 187 disposition |
|---|---|
| Exact nested field allowlists | IMPLEMENTED — SOURCE REVIEW ONLY |
| Temporal 13×M×(1+R) cardinality/order | IMPLEMENTED — SOURCE REVIEW ONLY |
| Pair ledger 52 rows, exact key/order, M contributions | IMPLEMENTED — SOURCE REVIEW ONLY |
| Scenario reports 13 keys, M outer reports and R nested reports | IMPLEMENTED — SOURCE REVIEW ONLY |
| Root/nested manifest equality | IMPLEMENTED — SOURCE REVIEW ONLY |
| Test fixture/adversarial vectors | WRITTEN — NOT EXECUTED |
| Gate 181 uint64 registry coverage of scenario_reports RUN tuple | OPEN — CONTRACT AMENDMENT REQUIRED |
| FrozenReportSnapshot v2.0.0 full JCS conformance | CONDITIONAL / NOT ESTABLISHED |
| Package writer/verifier and deterministic TAR | NOT IMPLEMENTED |
| Calibration/Gate159 companion assembly | NOT IMPLEMENTED |
| CI/tests | NOT EXECUTED |
| Scientific execution | NOT AUTHORIZED / NOT EXECUTED |

**Overall:** `CONDITIONAL — NESTED SCHEMA VALIDATION IMPLEMENTED; REPORT UINT64 REGISTRY INCOMPLETE`.

## 6. Next operation — Gate 188

Resolve the Gate 181 registry omission explicitly. The minimum successor contract must decide whether to:
1. retain the complete Evaluator report and version FrozenReportSnapshot to v2.1.0, adding the four exact scenario-report seed pointers and their equality/reconciliation rules; or
2. change the report projection requirement through an explicit, versioned decision, preserving the required source evidence elsewhere without silent omission.

Do not change the current v2.0.0 wire shape by implication. After the contract decision, implement the exact additional typed projections and adversarial vectors. Tests and CI remain unexecuted until separately authorized.
