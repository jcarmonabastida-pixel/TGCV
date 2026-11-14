# C10-S V_cont — Gate 194-I: configuration companion assembly and independent verification

**Status:** IMPLEMENTED — PURE TEST SUITE PASS; REAL PACKAGE NOT BUILT OR VERIFIED  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** the two Gate 194-H frozen companions, their independent semantic verification, and adversarial test authoring.  
**Authorization:** user approval to proceed with the bounded implementation, 2026-11-14.

## 1. Scope and non-goals

Gate 194-I implements only the Gate 194-H configuration-companion contract:

- assemble `design/analysis_contracts.json` from captured RUN/R AnalysisContract snapshots;
- assemble `provenance/configuration_fingerprints.json` from the effective-config projection, source AnalysisContracts, MatrixCapture and ordered evaluation SeedAssignments;
- independently reconstruct and verify both companions from package contents;
- add positive/adversarial tests to the existing allowlisted pure-verifier test module.

No Generator, Sealer, Analyzer, Evaluator, DGP, estimand, seed derivation, scientific interpretation, package profile, package inventory, or historical snapshot serialization code was modified. The writer imports the existing `AnalysisContract`, `Analyzer.version` and `RunManifest` definitions only to materialize the companion from already captured source evidence; it does not instantiate or invoke these components.

No package was generated. Pure compilation and regression tests were subsequently executed through the bounded GitHub Actions workflow recorded in §9.2. No calibration or scientific execution was performed.

## 2. Pre-implementation correction: independent AnalysisContract source

The Gate 194-H §12.8 Analyzer `source_ref` originally pointed into `design/analysis_contracts.json` itself. That would make the declared source row authenticate itself.

Gate 194-F §12.11 corrects this before implementation. Each of the 13 Analyzer component records now points to the representative RUN snapshot:

`runs/run_records.json#/run_evidence_records/<j>/snapshot_refs/analysis_contract`

The index is derived from canonical scenario/M/R order; the pointed record is checked against the complete logical RUN key and run_id. All other RUN and REPEATED_ASSIGNMENT snapshots are also decoded and reconciled to the same scenario-level source payload. The companion source row is a declaration, never its own evidence source.

## 3. Writer implementation

Updated `03_EXPERIMENTS/C10-S/harness/vcont_package_v2.py`.

### 3.1 Generated companions

The caller-supplied `VContPackageCompanionsV2` inventory now excludes exactly the two generated paths:

- `design/analysis_contracts.json`;
- `provenance/configuration_fingerprints.json`.

The writer creates both from already materialized inputs and captured snapshots. The package remains the same exact 14-file Gate 181 inventory; no fifteenth file or package-version change is introduced.

### 3.2 AnalysisContract companion

The writer:

1. orders captured outer-world bundles by the frozen 13-scenario registry and numeric M;
2. validates each scenario/M RUN and repeated assignment key;
3. restores the retained AnalysisContract snapshots without rewriting their historical bytes;
4. requires the 37-field contract to be identical across all RUN/R snapshots for that scenario;
5. checks each snapshot reference in `run_records.json` against the captured type ID, serialization ID and exact-byte SHA-256;
6. emits one source row per scenario, including the current `Analyzer.version` and semantic JCS digest;
7. emits exactly two applicability rows per scenario, RUN and REPEATED_ASSIGNMENT.

### 3.3 Configuration fingerprints

The writer assembles 28 component rows in frozen order:

- 13 DGP/Generator rows from the exact nested Gate 181 effective-config rows;
- 13 Analyzer rows from the semantic source-contract digests and independently derived RUN snapshot references;
- one MatrixCapture component using its four-field digest domain;
- one evaluation assignment component using `SHA256(JCS({"rows": ordered_assignment_wire_rows}))`.

Separately, it decodes the three typed uint64 streams back to source integers and recomputes the historical Gate 179 `seed_bank_fingerprint` over the exact ten source SeedAssignment fields and original row order. It compares that value with both the source design object and `design/benchmark_design.json`. This historical fingerprint is not substituted for the evaluation wire-manifest component and is not added as a 29th component.

It then computes the exact versioned seven-field aggregate projection and checks that the result equals both the source `MonteCarloBenchmarkDesign.configuration_fingerprint` and the `design/benchmark_design.json` declaration. A mismatch fails closed; the writer does not overwrite or normalize the declaration.

## 4. Independent verifier implementation

Updated `03_EXPERIMENTS/C10-S/harness/vcont_package_v2_verify.py`. The verifier does not import the package writer.

The new independent reconciliation layer:

- validates exact companion root and row allowlists;
- validates the 37 AnalysisContract fields and their source type partition (nine booleans, five nullable strings, remaining fields non-null strings);
- independently recomputes the semantic AnalysisContract JCS digest;
- validates 13 unique source rows and 26 complete applicability rows in canonical order;
- decodes every RUN/R AnalysisContract FrozenSnapshot using the historical decoder, preserving and hashing original bytes;
- checks type ID, serialization ID, base64 canonicality, exact-byte SHA-256, full scenario/version/N and RUN/R family mapping;
- enforces canonical `run_evidence_records` order and exact consumption of every scenario contract by all RUN/R records;
- derives the 13 representative source references from the canonical RUN rows and rejects the former self-referential locator;
- independently recomputes the historical source-typed Gate 179 `seed_bank_fingerprint` separately from the typed evaluation-manifest digest;
- independently recomputes all 28 components and the aggregate from package sources;
- checks both companion roots against the same `benchmark_export_id` and compares the aggregate to the source design declaration.

The verifier result now reports identity reconciliation as `RECONCILED` only after this configuration layer succeeds. Overall schema status remains partial, completeness remains structural-only, source-execution provenance remains unverified, and external authentication remains `NOT_AUTHENTICATED`.

## 5. Tests authored and execution scope

Added 18 positive/adversarial cases to the existing allowlisted file:

`03_EXPERIMENTS/C10-S/harness/test_vcont_package_v2_verifier.py`

Coverage includes:

- positive 13/26/28 reconciliation;
- writer assembly of the 13/26 AnalysisContract companion from captured RUN/R snapshots;
- writer assembly of all 28 configuration components and the aggregate fingerprint;
- generated-companion boundary;
- 12 source rows and 25 applicability rows;
- RUN snapshot crossed to another scenario;
- Analyzer version drift;
- MatrixCapture digest drift;
- self-referential/wrong Analyzer `source_ref`;
- RUN and REPEATED_ASSIGNMENT semantic snapshot divergence despite recomputed valid byte digests;
- DGP component digest drift;
- aggregate source-declaration mismatch.

The existing workflow `.github/workflows/c10-s-vcont-package-v2-pure-tests.yml` includes this test module. Its permanent trigger remains `workflow_dispatch`; a narrowly scoped temporary `push` trigger was used and then removed to run the tests from the mobile-constrained session. The exact execution and restoration are recorded in §9.2.

## 6. Static review findings and remaining conditions

**Implementation state:** code written and committed on the research branch.  
**Execution state:** PURE TESTS EXECUTED — PASS (92/92).  
**Test disposition:** PASS — execution-backed regression suite passed. **Overall Gate disposition:** CONDITIONAL — no real captured package has yet been assembled and independently verified.

The following are deliberately not claimed:

- that the writer successfully assembles a real captured benchmark;
- that the verifier passes a real package;
- that a real captured benchmark can be assembled;
- that the aggregate declaration in any extant design fixture equals the newly frozen aggregate;
- that Gate159, calibration/evaluation disjointness, source-execution provenance, technical-test provenance or external authentication are verified.

The writer's aggregate-declaration equality is a fail-closed precondition. Its compatibility with a real source design remains unverified until a separately authorized pure fixture/package operation is performed.

## 7. Governance and scientific boundary

- `main` is unchanged.
- PR #116 remains open and Draft.
- No scientific execution authorization was inferred or used.
- No claim, estimand, DGP truth, causal assumption, TGCV Core element, claim status or Evidence→Claim Matrix entry changed.
- Implementation and package integrity are not scientific evidence for `ΔT_acc → ΔV`.

**Gate 194-I disposition: IMPLEMENTED / CONDITIONAL — PURE TEST SUITE PASS; REAL PACKAGE NOT BUILT OR VERIFIED.**

**Next operation:** proceed to a separately bounded source/package fixture operation only after its own authorization. A passing pure-test suite does not authorize package generation or scientific execution.

## 8. Gate 194-I.1 — historical seed-bank fingerprint closure

A final crosswalk against the source function `seed_bank_fingerprint(assignments)` in `vcont_benchmark_protocol.py` found that the initial Gate 194-I implementation recomputed the typed evaluation-manifest digest but had not yet added the separate historical source-typed fingerprint check.

That gap is now closed in both writer and independent verifier:

- typed uint64 wire values are decoded to exact source integers;
- the historical payload is reconstructed using exactly the ten Gate 179 SeedAssignment fields and original row order;
- SHA-256 is recomputed over the original `json.dumps(sort_keys=True, separators=(",", ":"))` representation;
- the result is compared with `seed_bank_fingerprint_legacy` in the evaluation assignment envelope, the historical `seed_bank_fingerprint` in the source design object, and the corresponding `design/benchmark_design.json` declaration;
- calibration remains separate and is not mixed into the evaluation bank or the 28-component aggregate.

Three additional tests were added for writer parity, historical fingerprint mismatch and reordered evaluation rows. The Gate 194-I companion test set contains **18 authored tests**, all included in the passing 92-test pure suite.

**Updated disposition:** IMPLEMENTED / CONDITIONAL — pure test suite PASS (92/92); no real package generated or verified. This closes the historical seed-bank digest check at source-code level and provides regression evidence for the pure writer/verifier path.

## 9. Gate 194-I.2 — source-level consistency audit

The writer, verifier and adversarial fixtures were reviewed against the single normative definitions in Gate 194-F §§4–5 and 11–12, the Gate 181 source projection and capture identity, and the Gate 179 SeedAssignment source fingerprint.

The audit confirms at source level:

- writer-generated companion paths are exactly the two frozen paths and are excluded from caller-supplied companions;
- the Analyzer component points to the canonical representative RUN snapshot, not to its own companion declaration;
- the verifier independently enforces canonical scenario/M/R record order and consumes every RUN/R AnalysisContract snapshot;
- all 37 fields and the nine-boolean/five-nullable-string type partition are checked;
- the historical Gate 179 seed fingerprint is independently reconstructed from decoded source integers and compared with the evaluation manifest's `seed_bank_fingerprint_legacy`, the design object's `seed_bank_fingerprint`, and the benchmark-design declaration;
- the typed evaluation assignment-manifest digest remains a separate component;
- the 28 component records, exact source references, component order and aggregate digest are independently reconstructed;
- the test runner guard remains after all 18 added test methods, and the tests are in the existing manual-workflow allowlist.

**Static disposition: PASS_STATIC for the source-to-wire companion contract and its independent reconstruction.**  
**Overall Gate 194-I disposition: CONDITIONAL — pure test suite PASS; no real package assembled or verified.**

The current comparison reports the research branch as diverged from `main` (32 commits behind). No merge, rebase, cherry-pick or promotion was performed. PR #116 remains open and Draft. All Gate 194-I changes remain isolated to the research branch.

The pure-test workflow is restored to manual-only (`workflow_dispatch`). The bounded test run did not execute package generation, calibration or scientific execution.

**Next operation requiring separate authorization:** any real-package construction and independent verification. The pure-test workflow has already passed; that result does not authorize package generation or scientific execution.

### 9.1 Residual seed-derivation metadata boundary

Gate 181's evaluation-assignment envelope also declares a `seed_derivation` descriptor (algorithm, hash, output rule and namespace). Gate 194-I now verifies the exact assignment rows, their typed uint64 representation, the typed manifest digest and the legacy source-typed fingerprint declaration. It does **not** independently authenticate the declared namespace against the seed-generation call or recompute every seed from that namespace. The current `MonteCarloBenchmarkDesign` source type does not retain a namespace field, and the manifest descriptor alone is not independent provenance.

Accordingly, the assignment manifest's seed-derivation descriptor remains declared metadata, not independently authenticated derivation provenance. This limitation stays within `source_execution_provenance_status=NOT_VERIFIED`; no seed-generation or calibration operation is authorized by Gate 194-I.

### 9.2 Gate 194-I.3 — regression correction and pure-test execution

The first bounded run (workflow run [43633198109](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/43633198109), commit `8a640ec847419812f38cd1119562d60fc1bc0baa`) executed 92 tests and exposed five fixture/code failures. The failures were corrected without changing the package schema, scientific components, estimands, DGPs or verifier acceptance rules:

- `vcont_package_v2.py`: added the missing standard-library `json` import required by the historical seed-bank fingerprint reconstruction.
- `test_vcont_package_v2_verifier.py`: changed positive report fixtures to use the frozen 13-ID authoritative scenario registry, including the registered uint64-pointer fixture. The verifier's 13-scenario invariant was not weakened.
- `test_vcont_capture_v2.py`: made the uint64 boundary test actually supply `2**64 - 1` and `2**53 + 1` in both duplicate temporal views and recomputed the fixture's historical report fingerprint accordingly. The assertion was retained.

The corrected pure suite then completed successfully: **92 tests, 0 failures, 0 errors**. Run: [43633578902](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/43633578902). The workflow checked out exact commit `f58d2701cf9e1a98f22ff5ea7211f0f8c60c641d`; Python 3.12 setup, hash-locked JCS installation, allowlisted module compilation and the unittest step all passed.

To accommodate the absence of an available workflow-dispatch action, the workflow YAML received a temporary branch-and-path-scoped `push` trigger, then was restored to its original manual-only `workflow_dispatch` configuration. Restoration commit: `9f9f67be7a0af9348bf036df72a223cc322688dc`. The current workflow file was re-read and confirmed to contain only `workflow_dispatch`.

This is execution-backed technical regression evidence for the pure test suite only. It is not evidence that a real V_cont package has been assembled or independently verified, and it does not establish source-execution provenance, external authentication, calibration/evaluation separation, or any scientific claim about `ΔT_acc → ΔV`.

**Gate 194-I.3 disposition: PURE TEST SUITE PASS (92/92); OVERALL GATE REMAINS CONDITIONAL PENDING REAL-PACKAGE VALIDATION AND RESIDUAL PROVENANCE WORK.**
