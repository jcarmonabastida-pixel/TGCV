# C10-S V_cont — Gate 158: Monte Carlo report provenance audit

**Status:** AUDITED — CONDITIONAL / PROVENANCE BINDING NOT IMPLEMENTED  
**Branch:** research/c10-s-consolidation-draft  
**Audit basis:** static inspection at HEAD 2b8008104efeb646fa7330ef58a1638d02641750  
**Scientific execution:** NOT AUTHORIZED  
**Calibration / evaluation seed-bank generation:** NOT EXECUTED

## 1. Audit question and verdict

Does the Monte Carlo report prove that the declared seed-bank fingerprint, executable commit and configuration fingerprint are the identities actually used to generate the runs and calculate the report?

**Verdict: NO.** The report is internally fingerprinted and the metadata fields are syntactically validated, but the three declared provenance identities are not cryptographically or structurally bound to the actual execution inputs. They remain caller-supplied assertions.

This is a static implementation audit. It is not a live seed-bank audit, benchmark execution or scientific result.

## 2. Evidence inspected

| Artifact | Branch blob SHA | Relevant implementation |
|---|---|---|
| 03_EXPERIMENTS/C10-S/harness/vcont_benchmark_protocol.py | 8511f289224a885bdc69b2b494f4e6dd345fa8b8 | SeedAssignment, build_seed_bank(), validate_seed_banks(), seed_bank_fingerprint(), MonteCarloBenchmarkDesign, validate_monte_carlo_benchmark_design() |
| 03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py | 88c6c7bd6f82353e64a4f12edbe2e2abc2cec002 | RunManifest, TruthBundle, ScenarioConfig, Evaluator.evaluate_monte_carlo_benchmark() |
| 03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py | inspected at audit HEAD | benchmark aggregation and classification regression fixtures |

Governing implementation record: C10_S_VCONT_MONTE_CARLO_BENCHMARK_AGGREGATION_IMPLEMENTATION_GATE_157_DRAFT_001.md.

## 3. Findings

### F158-01 — seed-bank fingerprint is not recomputed from evaluated assignments

**Status: FAIL — binding absent.**

- seed_bank_fingerprint(assignments) can calculate a canonical digest over bank, scenario/version, N, M identity, assignment role/index and world/Z/G seeds.
- validate_monte_carlo_benchmark_design() checks only that design.seed_bank_fingerprint is a 64-character hexadecimal string.
- Evaluator.evaluate_monte_carlo_benchmark() copies that supplied string into the report manifest. It does not receive the canonical SeedAssignment collection, recompute the digest, or compare the supplied value with the temporal manifest's actual seed rows.
- The temporal manifest contains seed values but is not reconciled against a canonical seed-bank manifest/fingerprint.

Therefore a syntactically valid but unrelated fingerprint can be reported as the bank identity.

### F158-02 — executable commit is format-checked, not execution-attested

**Status: FAIL — binding absent.**

- validate_monte_carlo_benchmark_design() checks that executable_commit is a 40- or 64-character hexadecimal string.
- The Evaluator does not compare it with the Git commit actually checked out by the execution environment, the source archive used for replay, or an execution attestation tied to the produced runs.
- The report fingerprint includes the supplied commit string, but hashing a claim does not establish that the claim identifies the code that ran.

Therefore an arbitrary well-formed commit hash can be recorded without proving that it generated the Analyzer outputs.

### F158-03 — configuration fingerprint is format-checked, not recomputed

**Status: FAIL — binding absent.**

- validate_monte_carlo_benchmark_design() checks only the length and hexadecimal syntax of configuration_fingerprint.
- The aggregator does not reconstruct a canonical configuration payload from the scenario configurations/contracts used for the runs and compare its digest with this value.
- The tuple's contract objects are not used to establish this fingerprint.

Therefore the report does not prove that the declared configuration is the configuration actually used by Generator and Analyzer.

### F158-04 — temporal manifest is not fully reconciled with M/R identity

**Status: PARTIAL — local checks exist; end-to-end checks are incomplete.**

The aggregator checks the number of rows per M, exactly one RUN role, contiguous R indices, scenario version and N, and uniqueness of temporal-manifest keys.

However, the inspected benchmark aggregation path does not establish all of the following before accepting the report:

1. The dictionary key outer_id equals every row's manifest.outer_replicate_id.
2. All RUN/R rows within one M share exactly one world_id and one world_seed.
3. Different M values within a scenario/version/N have distinct world IDs and world seeds.
4. The seed values in evaluated RunManifests exactly match corresponding canonical SeedAssignment rows, including bank, role and stream identity.

The separate validate_seed_banks() helper checks fixed world seed within M, distinct world seeds across M, one RUN per M, unique R indices and calibration/evaluation seed disjointness. But the benchmark Evaluator does not receive or invoke that canonical bank validation as part of its own acceptance path, nor bind the resulting bank digest to evaluated run records.

### F158-05 — report fingerprint is an integrity digest, not provenance authentication

**Status: PASS for internal integrity; NOT SUFFICIENT for provenance.**

The report SHA-256 covers declared design fields, temporal manifest and pair ledger. This can detect subsequent alteration if the expected digest is trusted. It does not authenticate the origin of the supplied seed-bank, executable or configuration identities.

The deterministic test fixture supplies placeholder values a×64, c×40 and b×64 for seed-bank, executable and configuration identities, and checks only that the report fingerprint has length 64. This is a structural fixture, not a provenance-binding test.

## 4. Overall audit matrix

| Provenance element | Current control | Audit result |
|---|---|---|
| Seed-bank identity | 64-hex syntax; helper exists to fingerprint SeedAssignment rows | **NOT BOUND** to evaluated rows |
| Executable identity | 40/64-hex syntax | **NOT ATTESTED** against actual runtime/source commit |
| Configuration identity | 64-hex syntax | **NOT RECOMPUTED** from actual run configuration |
| M/R temporal structure | Count, role and contiguous-index checks; separate bank validator | **PARTIAL**; missing cross-binding checks |
| Report payload | SHA-256 over design + manifest + ledger | **PASS as internal integrity digest only** |
| Calibration/evaluation separation | Separate validator exists | **NOT ENFORCED** by report acceptance path |

## 5. Required correction before provenance can be accepted

Implement a provenance-binding layer with one canonical execution provenance object. At minimum:

1. Accept the actual materialized SeedAssignment manifest used to generate the evaluated runs.
2. Validate complete calibration/evaluation bank separation and M/R constraints on that exact manifest.
3. Recompute its canonical fingerprint and require equality with the declared evaluation-bank fingerprint.
4. Require a runtime/source attestation containing the actual checked-out commit and bind it to every run/report; reject a caller-supplied commit that differs.
5. Canonicalize the actual scenario/DGP/Analyzer configuration used by each run, compute its fingerprint, and compare it with the declared configuration identity.
6. Reconcile each RunManifest to exactly one SeedAssignment by bank/scenario/version/N/M/role/R and require equality of all seeds and identities.
7. Enforce equality of outer-replicate keys and manifest identities, fixed world ID/seed within M, and distinct world ID/seed across M.
8. Include the validated provenance object and its validation result in the report fingerprint. Compute the digest only after validation; it must not turn unverified claims into verified provenance.
9. Add adversarial tests showing that altered bank seeds, mismatched commit, modified configuration, swapped M identity, cross-world assignment and calibration/evaluation seed collision all fail closed.

Do not conflate provenance authenticity with report integrity. Both are required and answer different questions.

## 6. Gate 158 conclusion and authorization boundary

**Gate 158 is AUDITED, but the provenance contract is NOT SATISFIED.** The current implementation can record caller-supplied provenance labels and produce a self-consistent report digest; it cannot yet claim those labels have been independently verified against the actual execution.

The next implementation gate should close F158-01 through F158-04 with explicit adversarial regression coverage. Retain the current report fingerprint as the final integrity layer after provenance binding is implemented.

No code or tests were changed as part of this static audit. No seed bank was generated, no calibration or benchmark was run, no N/R/M sizing was performed, and no scientific execution was authorized. main remains unchanged; PR #116 remains Draft on its existing base.