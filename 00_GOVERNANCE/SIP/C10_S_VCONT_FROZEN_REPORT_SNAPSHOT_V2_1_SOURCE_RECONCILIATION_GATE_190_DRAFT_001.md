# C10-S V_cont — Gate 190: source-bundle reconciliation and package-profile boundary

**Status:** IMPLEMENTED IN RESEARCH BRANCH — STATIC SOURCE AUDIT CONDITIONAL / TESTS NOT EXECUTED  
**Parent:** Gate 189 — FrozenReportSnapshot v2.1.0 capture implementation  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** exact RUN/R source-bundle reconciliation for the four v2.1 nested report seed paths; pure adversarial fixture authoring; package writer/verifier existence audit  
**Execution:** GitHub source inspection and source/document edits only. No imports, compilation, tests, workflow dispatch, producer invocation, seed generation, package generation, calibration or scientific execution.

## 1. Historical reconstruction and source findings

Gate 188 defines the v2.1.0 successor without changing Gate 181 or FrozenReportSnapshot v2.0.0. Gate 189 added the four nested uint64 projections and a source reconciliation helper, but its own record explicitly left a material gap: the helper had no successful/failed full source-bundle fixtures.

The actual source shape was re-read:
- Evaluator report is a dictionary with typed `MonteCarloBenchmarkDesign`;
- each scenario report is a dictionary;
- `per_outer_replicate` is a tuple of row dictionaries;
- each row's `run` is the exact four-object tuple `(TruthBundle, AnalyzerResult, AnalysisContract, RunManifest)`;
- `RunEvidenceBundle` retains snapshots of SeedAssignment, ScenarioConfig, RunManifest, MatrixTruthProjection, AnalyzerResult, AnalysisContract and EvaluationReport;
- `OuterWorldEvidenceBundle` retains one RUN bundle, ordered repeated bundles and a repeated-assignment report.

This is the join shape consumed by Gate 190. The source is not a JSON-projected tuple at reconciliation time.

## 2. Reconciliation implementation

The helper `_reconcile_report_seed_sources` in `vcont_evidence_export.py` now validates:

1. Immutable outer-bundle tuple, exact design scenario/version registry, N/M/R cardinalities, exact scenario coverage and one-to-one scenario/M keys.
2. Exact outer/run evidence schema identifiers and versions.
3. The seven-part RUN/R logical key:
   `(scenario_id, scenario_version, n_units, outer_replicate_id, assignment_role, assignment_index, run_id)`,
   plus the separate `evaluation` bank.
4. Source dataclass identities across SeedAssignment, ScenarioConfig, RunManifest, MatrixTruthProjection, AnalyzerResult, AnalysisContract and EvaluationReport.
5. Exact uint64 type/range at the source for TruthBundle/config/truth-projection seeds, all three SeedAssignment streams, all three RunManifest streams, effective ScenarioConfig streams and OuterWorldEvidenceBundle.world_seed.
6. Source-specific seed equality:
   - `TruthBundle.seed == ScenarioConfig.seed == MatrixTruthProjection.seed`;
   - RunManifest world/Z/G streams equal their matching SeedAssignment and effective ScenarioConfig streams;
   - outer-world world seed equals RUN assignment and RUN manifest.
7. Effective stream fallback semantics used by `RunEvidenceBundle.capture`: when a ScenarioConfig stream field is `None`, world uses `config.seed`, Z uses `config.seed + 100003`, and G uses `config.seed + 200003`. The helper does not incorrectly compare a defaulted stream to a literal `None`.
8. Exact RUN report tuple equality for AnalyzerResult, AnalysisContract and RunManifest, and equality of the report TruthBundle's retained matrix projection to the immutable MatrixTruthProjection snapshot.
9. Exact R repeated-bundle count, indices 0..R-1, logical keys, world identity/seed, unique run IDs and unique Z/G streams within the M group.
10. RepeatedAssignmentReport identity/count and exact ordered EvaluationReport correspondence to the repeated RunEvidenceBundles.

The implementation deliberately does not compare TruthBundle.seed to world_seed. The four report pointers retain the distinct source semantics specified by Gate 188.

## 3. Pure fixtures authored

`test_vcont_capture_v2.py` now contains **25 test methods**. Eight Gate 190 tests construct typed source objects and immutable FrozenSnapshots without calling Generator, Sealer, Analyzer, Evaluator or any producer:
- positive exact RUN + R source-bundle reconciliation;
- report RunManifest seed divergence;
- repeated SeedAssignment stream divergence;
- duplicate/missing outer-world groups;
- TruthBundle.seed / MatrixTruthProjection mismatch;
- explicit ScenarioConfig stream mismatch;
- OuterWorldEvidenceBundle world-seed mismatch;
- missing repeated assignment.

The fixture uses deterministic inline values and the pure `benchmark_scenarios` configuration constructor only. It does not build a seed bank or invoke a producer.

These tests are **written, not executed**. No import, compile, unit test or workflow run has occurred. The tests are not technical PASS evidence.

## 4. Package-profile integration audit

The research harness directory was enumerated at the current branch:
- present: `vcont_evidence_export.py`, `test_vcont_capture_v2.py`;
- absent: `vcont_package_v2.py`, `vcont_package_v2_verify.py`, package serialization/verifier test modules.

The only package-v2 workflow is `.github/workflows/c10-s-vcont-package-v2-pure-tests.yml`. It is `workflow_dispatch` only, read-only, and explicitly compiles/runs the capture module and its pure test file. The legacy integrated synthetic workflow is also `workflow_dispatch` only and requires an explicit boolean confirmation on the research branch.

Therefore the package profile cannot yet enforce the v2.1 report sub-schema: there is no writer/verifier implementation or package profile code to update. Gate 182's normative contract and Gate 188's schema decision remain controlling. Package-level v2.1 conformance remains OPEN. Gate 190 does not create a partial writer/verifier or change the 14-file package inventory.

## 5. Scope and non-execution

No changes were made to Generator, Sealer, Analyzer, Evaluator, ScenarioConfig semantics, estimands, DGPs, seed generation, calibration or scientific execution. Gate 181, FrozenReportSnapshot v2.0.0, Gate 164 package v1.0.0 and `main` remain untouched.

The pure workflow was inspected but not dispatched. No tests, compilation, CI, producers, package generation, calibration or scientific experiment was executed.

## 6. Disposition

**Gate 190: SOURCE RECONCILIATION IMPLEMENTED — CONDITIONAL.**

The helper now covers the source equality and logical joins for RUN and R bundles, and pure positive/adversarial fixtures have been authored. Static source review remains conditional until tests are executed under separate technical authorization. Package-level v2.1 integration is blocked by the absence of writer/verifier modules and remains a subsequent implementation task.

### Next operation — Gate 191

Perform a read-only source audit of the complete helper and fixtures, correct any source-level defects found, then define the bounded implementation contract for the v2 package writer and independent verifier with an explicit `report_snapshot.schema_version = 2.1.0` dependency. Do not run tests or the workflow without separate execution authorization.

## 7. Final Evaluator-row join refinement

A further read of `Evaluator.evaluate_monte_carlo` established that the per-outer row also carries `outer_replicate_id`, `run_report` and `repeated_report`, while the scenario report carries `scenario_id` and `scenario_version`. Gate 190 now checks those labels against the ordered scenario/M key and checks both summary report objects against the exact captured RUN and repeated EvaluationReport sources. This prevents a correctly seeded RUN tuple from being attached to a mislabeled M row or a divergent evaluation summary.

The typed pure fixture was extended to include those exact Evaluator fields. This is a static source-level strengthening; the test suite remains unexecuted.

