# C10-S V_cont — Gate 194-I: configuration companion assembly and independent verification

**Status:** IMPLEMENTED — STATIC REVIEW ONLY; NOT EXECUTED  
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

No package was generated. No tests, compilation, CI, workflow, calibration or scientific execution was performed.

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

## 5. Tests authored — not executed

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

The existing manual-only workflow `.github/workflows/c10-s-vcont-package-v2-pure-tests.yml` already includes this test module. Its trigger is `workflow_dispatch`; it was not dispatched. No workflow file was modified.

## 6. Static review findings and remaining conditions

**Implementation state:** code written and committed on the research branch.  
**Execution state:** NOT EXECUTED.  
**Static disposition:** CONDITIONAL — implementation has not yet received an execution-backed regression result.

The following are deliberately not claimed:

- that the writer successfully assembles a real captured benchmark;
- that the verifier passes a real package;
- that the new tests pass;
- that the aggregate declaration in any extant design fixture equals the newly frozen aggregate;
- that Gate159, calibration/evaluation disjointness, source-execution provenance, technical-test provenance or external authentication are verified.

The writer's aggregate-declaration equality is a fail-closed precondition. Its compatibility with a real source design remains unverified until a separately authorized pure fixture/package operation is performed.

## 7. Governance and scientific boundary

- `main` is unchanged.
- PR #116 remains open and Draft.
- No scientific execution authorization was inferred or used.
- No claim, estimand, DGP truth, causal assumption, TGCV Core element, claim status or Evidence→Claim Matrix entry changed.
- Implementation and package integrity are not scientific evidence for `ΔT_acc → ΔV`.

**Gate 194-I disposition: IMPLEMENTED / CONDITIONAL — STATIC REVIEW ONLY; TESTS NOT EXECUTED.**

**Next operation:** complete a source-level consistency audit of the writer/verifier pair and the new test fixtures. Only after that audit should a separate explicit authorization be sought to dispatch the existing manual pure-test workflow. No package generation or scientific execution is implied.

## 8. Gate 194-I.1 — historical seed-bank fingerprint closure

A final crosswalk against the source function `seed_bank_fingerprint(assignments)` in `vcont_benchmark_protocol.py` found that the initial Gate 194-I implementation recomputed the typed evaluation-manifest digest but had not yet added the separate historical source-typed fingerprint check.

That gap is now closed in both writer and independent verifier:

- typed uint64 wire values are decoded to exact source integers;
- the historical payload is reconstructed using exactly the ten Gate 179 SeedAssignment fields and original row order;
- SHA-256 is recomputed over the original `json.dumps(sort_keys=True, separators=(",", ":"))` representation;
- the result is compared with `seed_bank_fingerprint_legacy` in the evaluation assignment envelope, the historical `seed_bank_fingerprint` in the source design object, and the corresponding `design/benchmark_design.json` declaration;
- calibration remains separate and is not mixed into the evaluation bank or the 28-component aggregate.

Three additional tests were added for writer parity, historical fingerprint mismatch and reordered evaluation rows. The Gate 194-I companion test set now contains **18 authored tests**, all still unexecuted.

**Updated disposition:** IMPLEMENTED / CONDITIONAL — STATIC REVIEW ONLY; TESTS NOT EXECUTED. This closes the missing historical seed-bank digest check at source-code level; it does not establish that the implementation passes the tests or a real package.

