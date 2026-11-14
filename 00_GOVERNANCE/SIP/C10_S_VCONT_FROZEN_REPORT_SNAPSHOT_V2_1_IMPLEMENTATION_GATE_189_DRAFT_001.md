# C10-S V_cont — Gate 189: FrozenReportSnapshot v2.1.0 implementation slice

**Status:** IMPLEMENTED IN RESEARCH BRANCH — SOURCE AUDIT PARTIAL / TESTS NOT EXECUTED  
**Parent:** Gate 188 — FrozenReportSnapshot v2.1.0 successor contract  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** v2.1 report uint64 projection and mandatory source-bundle seed reconciliation at the existing capture boundary  
**Execution:** GitHub source edits and readback only. No imports, compilation, tests, workflow dispatch, producer invocation, seed generation, package generation, calibration or scientific execution.

## 1. Changes persisted

### 1.1 `vcont_evidence_export.py`

- FrozenReportSnapshot schema version is now `2.1.0`; the existing envelope field set is unchanged.
- The complete Evaluator `scenario_reports` RUN tuple is retained.
- Exactly four nested values are converted to the typed uint64 wrapper:
  - `run[0].seed`;
  - `run[3].world_seed`;
  - `run[3].z_assignment_seed`;
  - `run[3].g_assignment_seed`.
- Conversion uses the existing strict `_uint64_wire` validator: exact integer only, booleans rejected, range `0..2^64-1`, canonical decimal string.
- The legacy report fingerprint is still recomputed over the source-typed Evaluator manifest before the JCS projection; the new snapshot digest is computed over the wrapped v2.1 envelope.
- `freeze_report_snapshot` now fails closed unless immutable `OuterWorldEvidenceBundle` sources are supplied. A private fixture-only escape hatch is used by isolated projection unit tests; it is not used by the producer.
- The production benchmark path supplies its captured outer-world bundles when freezing the report.

### 1.2 Source reconciliation

A new `_reconcile_report_seed_sources` check joins each scenario/M RUN report to exactly one captured evaluation-bank outer-world bundle and its RUN `RunEvidenceBundle`.

The check validates:
- exact scenario/version/N/M/RUN/-1/run_id logical key and `evaluation` bank;
- source report RUN tuple identity across TruthBundle, AnalyzerResult, AnalysisContract and RunManifest run IDs;
- `TruthBundle.seed == ScenarioConfig.seed == MatrixTruthProjection.seed`;
- each of the three RunManifest stream seeds equals its matching SeedAssignment, explicit ScenarioConfig field and RunManifest snapshot field;
- OuterWorldEvidenceBundle world seed equals both evaluation SeedAssignment.world_seed and RUN RunManifest.world_seed;
- all source seeds are exact uint64 values;
- one-to-one coverage of all declared scenario/M bundles and exact repeated-assignment cardinality.

The implementation deliberately does **not** equate `TruthBundle.seed` with `world_seed`. This matches the Generator construction and the pre-existing `RunEvidenceBundle.capture` check.

### 1.3 Regression fixtures

The capture test module now contains **17 test methods**. New/updated cases cover:
- schema version 2.1.0;
- all four nested report paths;
- boundary values (2^{53}-1), (2^{53}), (2^{64}-1), and zero;
- invalid negative, boolean, float, string and out-of-range source values;
- a positive case where TruthBundle.seed differs from RunManifest.world_seed;
- rejection when a production snapshot is requested without source-bundle reconciliation.

The 14 direct report-projection fixture calls explicitly opt into the private test-only bypass. They do not constitute source-reconciled acceptance tests.

## 2. Deliberate non-changes

- Generator, Sealer, Analyzer, Evaluator, ScenarioConfig semantics and seed generation are unchanged.
- Historical Gate 181 and FrozenReportSnapshot v2.0.0 are not edited or reinterpreted.
- Gate 164 package v1.0.0 remains frozen.
- No package writer or independent package verifier was modified in this Gate.
- No package profile has yet been updated to require report snapshot v2.1.0. Until that versioned cross-reference is implemented, package-level v2.1 conformance remains OPEN.
- No test, compilation, CI, producer, package, calibration or scientific execution was performed.

## 3. Audit limitations

The production call path now supplies source bundles, and the helper enforces source-specific equality. The isolated projection tests deliberately bypass source-bundle reconciliation and therefore cannot demonstrate that the helper accepts/rejects complete captured bundles correctly.

The next source audit must inspect the exact production join in context, confirm the report's RUN tuple is the same tuple previously checked against each `RunEvidenceBundle`, and add a pure source-bundle fixture that exercises positive and negative reconciliation. Do not dispatch the pure workflow or run tests without separate execution authorization.

The package writer/verifier and package profile cross-reference remain a separate implementation gap. A valid v2.1 FrozenReportSnapshot alone is not a conformant V_cont package.

## 4. Disposition

**Gate 189: IMPLEMENTED IN RESEARCH BRANCH — CONDITIONAL.**

The capture boundary can now produce a v2.1-shaped report snapshot only when source bundles are supplied by the production caller. The report projection and source reconciliation are implemented in code, but not executed. Source-bundle adversarial test coverage, package-profile integration, independent verification, trusted provenance and end-to-end package conformance remain open.

No scientific estimand, DGP, causal claim, or authorization to execute experiments is changed.
