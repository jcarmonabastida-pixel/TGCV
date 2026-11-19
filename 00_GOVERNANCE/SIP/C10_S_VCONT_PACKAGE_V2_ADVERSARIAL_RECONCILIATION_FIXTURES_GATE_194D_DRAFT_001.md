# C10-S V_cont — Gate 194-D: adversarial RUN/R and MatrixCapture reconciliation fixtures

**Status:** ADVERSARIAL FIXTURES IMPLEMENTED IN SOURCE — STATIC REVIEW CONDITIONAL — NOT EXECUTED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 194-C — independent RUN/R semantic reconciliation  
**Scope:** complete the directly testable verifier subcontracts for MatrixCapture↔pair-ledger identity, outer-world RUN/R reference resolution, duplicate logical-key registration and report-to-snapshot provenance  
**Execution boundary:** GitHub source inspection and source/document edits only. No imports, compilation, test execution, CI, workflow, package construction, producers, seed generation, calibration or scientific execution.

## 1. Gate decision

Gate 194-D adds pure positive and adversarial fixtures around extracted verifier subcontracts. The extraction is not a second implementation: the same helpers are invoked by the production verifier's RUN/R reconciliation path.

The work does not claim that a complete 13×M×(1+R) package fixture has been built or exercised. The tests added here isolate identity joins at the narrowest independently testable boundary. Full archive-to-report integration fixtures remain open.

## 2. MatrixCapture ↔ pair-ledger identity

The previous verifier checked MatrixCapture schema, cardinality, full JCS digest and design identity, and separately reconciled pair-ledger contributions to outer-world RUNs. It did not yet join each of the 52 pair-ledger keys and classifications to the corresponding MatrixCapture row.

A new independent helper, `_reconcile_matrix_pair_ledger`, now enforces:
- exactly 52 MatrixCapture rows and 52 pair-ledger rows;
- exact MatrixCapture row and four-field key allowlists;
- nonempty string scenario/version/estimand/version identity values;
- unique MatrixCapture scenario/estimand identities;
- allowed evaluation and truth classifications;
- exact ordered pair key `[scenario_id, scenario_version, estimand_id, estimand_version, "MONTE_CARLO"]`;
- no duplicate pair identity;
- equality of pair-ledger `evaluation_class` and `truth_status` with the corresponding MatrixCapture row.

The helper is called by the package verifier after MatrixCapture digest and design-identity checks.

Fixtures added:
1. positive 52-row MatrixCapture/pair-ledger join;
2. wrong scenario identity;
3. wrong estimand identity;
4. wrong estimand version;
5. reordered pair rows;
6. classification drift;
7. duplicate MatrixCapture identity.

## 3. Outer-world RUN/R reference resolution

The former inline logic has been factored into `_resolve_outer_world_run_reference`, now used for both designated RUN and repeated-assignment references. It requires:
- exact seven-field logical key parsing;
- exact scenario/version/N/outer-replicate base;
- expected assignment role and index;
- reference existence in the independently reconstructed run map;
- equality between key `run_id` and decoded RunManifest `run_id`;
- exact equality of `(world_id, world_version, world_seed)` to the owning outer-world key.

Fixtures added:
1. positive designated RUN resolution;
2. positive repeated-assignment resolution;
3. cross-world reference rejection;
4. RunManifest/run-key `run_id` divergence rejection;
5. repeated assignment incorrectly mapped to the designated RUN rejection;
6. orphaned reference rejection.

The resolver is not allowed to infer identity from array position or from a partial match.

## 4. Duplicate keys and report provenance

Two additional helpers centralize checks already required by the reconciliation path:

- `_register_unique_run_record` rejects a second insertion of the same complete logical RUN/R key and is now used at the production run-map insertion point.
- `_assert_report_snapshot_projection` compares a report object with the source-safe projection of the independently decoded snapshot and is now used for AnalyzerResult, AnalysisContract, RunManifest, EvaluationReport and RepeatedAssignmentReport report views.

Fixtures added:
- duplicate complete logical RUN/R key rejected at registration;
- positive report projection accepted when tuple-valued source fields are represented as JSON arrays;
- structurally valid but semantically false report projection rejected when its `run_id` differs from the captured snapshot.

These tests target semantic provenance, not merely report JSON shape.

## 5. Source independence and static checks

The verifier module was re-read after the changes. A static text scan found:
- no imports from `vcont_package_v2`, `vcont_evidence_export`, `vcont_integrated_harness` or `vcont_benchmark_protocol`;
- no temporary `and False` guards;
- no empty-comprehension scaffolding;
- no visible TODO/FIXME markers in the two reviewed modules.

The test module imports the verifier under test, which is expected. This text scan is not a syntax check, compilation or execution and does not prove complete semantic independence beyond the inspected source boundary.

## 6. Test inventory added in Gate 194-D

| Fixture family | Positive cases | Adversarial cases |
|---|---:|---:|
| MatrixCapture ↔ pair ledger | 1 | 7 |
| Outer-world reference resolution | 2 | 4 |
| Duplicate logical key registration | 0 | 1 |
| Report ↔ snapshot projection | 1 | 1 |

All fixtures are authored only. **None has been executed.**

Existing decoder and seed-domain tests remain unchanged and unexecuted.

## 7. Explicitly open work

Gate 194-D is partial, not an end-to-end closure. The following remain:
- full 13-scenario × M-world × (1+R)-assignment positive package fixture;
- package-level adversarial mutations that recompute all outer file hashes and archive bytes while preserving an invalid semantic join;
- complete companion crosswalk and schema validation for all 11 complements;
- `benchmark_export_id` equality across all relevant independent companions;
- exact effective structural-config registry and AnalysisContract companion joins;
- calibration/evaluation seed-bank disjointness;
- Gate159 derived-status recomputation;
- complete aggregate summary consistency, beyond exact captured report projections;
- source-execution, test-evidence and GitHub provenance reconciliation;
- external authentication, which remains `NOT_AUTHENTICATED`.

No test, compilation, CI, workflow, package construction or scientific operation was performed.

## 8. Source commits

All commits are on `research/c10-s-consolidation-draft`:
- MatrixCapture ↔ pair-ledger join: `733471ba586f8967654aa76710db5fd3ce5e1927`
- Matrix/pair adversarial fixtures: `e3dabf5f3d41d9b8e8f87add9229831975d488f4`
- shared outer-world reference resolver: `9adef7788d8d346c0721338b670da343af35a466`
- outer-world adversarial fixtures: `21861000c2409810881ff09943a3aa9b1b762ce9`
- shared report projection and unique-key assertions: `2e00b6f0939760721e939eb5dd4c8a46120ca244`
- duplicate-key and false-provenance fixtures: `dae3c1cd0b41f33f02cca0f0eca9d3103fc3a875`

Current reviewed blob identities:
- verifier `vcont_package_v2_verify.py`: `e55283bc305fbad31347bf8f77c1838c75086535`
- tests `test_vcont_package_v2_verifier.py`: `9becb82fd7a349f0e49e4f8e14dc9da6fe1151b9`

## 9. Gate disposition and next operation

**G194-D: PARTIAL IMPLEMENTATION / STATIC REVIEW CONDITIONAL / NOT EXECUTED.**

The next operation should be G194-D completion at package-fixture level only if the fixture can be built from frozen contracts without invoking producers or seed generation. Otherwise, proceed to G194-E static audit and record the remaining integration fixture as an explicit evidence limitation rather than manufacturing a synthetic end-to-end PASS.

PR #116 remains Draft. No changes to `main`, historical frozen contracts or scientific components. Scientific execution remains unauthorized.


## 10. Gate 194-E static-audit finding corrected during continuation

A source-to-source comparison against the historical `RunEvidenceBundle.capture` contract found that the verifier recomputed the SealedEvidence provenance digest but did not bind every provenance identity field to the decoded SeedAssignment, ScenarioConfig and RunManifest, nor require `AnalyzerResult.provenance_sha256` to equal that digest.

This allowed an internally self-consistent provenance object to be attached to the wrong RUN/world while retaining its own valid digest.

The verifier now uses `_assert_sealed_provenance_identity` to bind:
- run_id, scenario/version and replicate identity;
- world_id/world_version;
- outer replicate, role and assignment index;
- G/Z mechanism IDs, versions and hashes;
- reference-regime identity;
- Z/G assignment-vector hashes;
- recomputed provenance digest and AnalyzerResult.provenance_sha256.

Three additional unexecuted fixtures cover a positive join, cross-world/run identity divergence and AnalyzerResult digest divergence.

Source commits:
- verifier: `88b791cd8a4e35c0475e151fc175e73f18bc701a`
- fixtures: `45fb6389c6577224502ef2f40045c047c3916332`

The change is a verifier correction derived from the existing historical capture contract; no historical contract or producer was modified.
