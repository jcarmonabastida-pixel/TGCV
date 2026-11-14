# C10-S V_cont — Gate 185: capture primitives implementation

**Status:** IMPLEMENTED — STATIC REVIEW ONLY; TECHNICAL TESTS NOT EXECUTED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 184 CI execution-boundary split  
**Scope:** MatrixCapture v1.0.0, FrozenReportSnapshot v2.0.0, capture identity v2.0.0 and pure fixture test source  
**Execution:** GitHub source edits and read-back only. No imports, compilation, tests, CI dispatch, dependency installation, Generator/Sealer/Analyzer/Evaluator invocation, seed generation, calibration, package creation or scientific execution.

## 1. Implementation slice

Gate 185 implements the first source-capture slice required by Gate 182. It does not implement the package writer, companion assembler, deterministic TAR or independent verifier.

Updated:
- `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`
- `03_EXPERIMENTS/C10-S/harness/test_vcont_capture_v2.py` (new)

The implementation remains confined to the capture/export boundary. No Generator, Sealer, Analyzer, Evaluator, DGP, assignment mechanism, estimand or Monte Carlo aggregation behavior was changed.

## 2. MatrixCapture v1.0.0

Implemented:
- exact 52-row positional validation using source-defined `SCENARIO_IDS` then `ESTIMAND_SPECS` order;
- exact row projection, including explicit nulls, `tolerance_id`, temporal classes and four-part key;
- authoritative scenario/version order and N/M/R design identity;
- independent recomputation of the historical `scenario_matrix_fingerprint()`, without changing its algorithm;
- full-matrix digest over RFC 8785 JCS of `schema_id`, `schema_version`, `row_count` and the exact ordered rows;
- immutable internal nested representation and retained canonical bytes.

The full digest does not include the design identity or capture IDs, matching Gate 178 §2.4. Permuted rows fail before digest acceptance. A tolerance-only change remains invisible to the historical fingerprint but changes the full-matrix digest.

## 3. FrozenReportSnapshot v2.0.0

Implemented:
- exact v2 envelope identity and payload type;
- source report projection with all seven required top-level report members;
- typed uint64 wrappers at Gate 181's report paths: root temporal manifest, nested legacy temporal manifest, root pair-ledger contributions and nested legacy pair-ledger contributions;
- validation of exact root/nested temporal and pair-ledger equality after typed projection;
- strict uint64 domain and rejection of booleans, negatives and values above 2^64−1;
- JCS canonical bytes and independent SHA-256;
- preservation of the original source report dictionary as the compatibility view. Snapshot bytes are captured independently and do not change when that dictionary is subsequently mutated.

The existing historical report fingerprint is not recomputed with JCS. Gate 181 requires an algorithm identifier but the Gate 164/178 text froze the source algorithm without assigning a stable identifier. Gate 185 assigns the explicit identifier:

`TGCV-C10S-VCONT-LEGACY-REPORT-PYTHON-JSON-SHA256-1`

It denotes the unchanged source operation: normalize the manifest payload through `json.dumps(..., default=asdict, sort_keys=True)` then `json.loads`; apply the existing `_hash` operation using sorted keys, compact separators, `allow_nan=False`, UTF-8 and SHA-256. This names the existing algorithm; it does not change the fingerprint bytes.

The v2 report envelope is schema-versioned 2.0.0 and keeps the Gate 181 exact field set: schema ID/version, payload type, legacy report fingerprint, legacy fingerprint algorithm and complete report projection. Its digest is SHA-256 over the exact JCS envelope bytes.

## 4. Capture identity v2.0.0

Implemented `derive_capture_identity()` using the Gate 178/181 content-only identity boundary:

- exact declared design identity projection;
- MatrixCapture full digest;
- JCS digest of ordered evaluation SeedAssignment projections with typed uint64 seed fields;
- ordered scenario/M outer-world bundle digests, each committing to the outer key, ordered RUN/R snapshot type IDs and SHA-256 values, and repeated-assignment report snapshot;
- FrozenReportSnapshot digest;
- exact ordered evidence_index.

The ID payload excludes its own `capture_id` / `benchmark_export_id`, companion artifacts, timestamps, random IDs, mutable paths and externally supplied provenance. `benchmark_export_id` is exposed as an alias of `capture_id`. Outer-world key coverage, uniqueness, M ordering and evidence-index equality are checked before deriving the ID.

The producer now captures MatrixCapture and FrozenReportSnapshot and derives capture_id immediately after Evaluator returns, then populates three trailing optional fields on CapturedBenchmark. The first three fields, order and meanings are unchanged; three-argument legacy construction remains valid and leaves the new fields absent.

## 5. Pure fixture tests and CI boundary

New `test_vcont_capture_v2.py` contains source for:
- exact matrix size/digest;
- positional permutation rejection;
- tolerance-only digest sensitivity while retaining the historical fingerprint;
- uint64 wrapper and report snapshot immutability;
- root/nested manifest disagreement;
- invalid uint64 and unknown report root field rejection;
- RFC 8785 canonicalization vectors and rejection vectors;
- three-positional-argument CapturedBenchmark compatibility.

Static inspection of the test source confirms it does not call Generator, Sealer, Analyzer, Evaluator or either producer.

**Tests have not been run.** Gate 182 requires separate technical execution authorization. To prevent a push from silently executing tests before that authorization, Gate 184's pure workflow is temporarily narrowed to a manual-only capture-test workflow. It installs the pinned JCS dependency, compiles only the capture module/test and runs only `test_vcont_capture_v2` when manually dispatched. No workflow dispatch has occurred. The workflow can be expanded to the remaining v2 modules as those slices are implemented and execution is authorized.

## 6. Static review limits and known boundaries

- No Python import, syntax compilation or test result is claimed.
- RFC 8785 behavior is specified and test vectors are authored, but JCS conformance is NOT VERIFIED until the tests execute and pass.
- The report source projection is intentionally fail-closed on root schema, legacy manifest schema, missing registered seed fields and root/nested duplication mismatch.
- The independent verifier must independently validate the report envelope and typed uint64 registry; it must not trust these capture helper outputs.
- CalibrationBankManifest and Gate159 companions remain unimplemented and external to capture_id.
- The package writer/verifier, 14-file package inventory, deterministic TAR and external provenance reconciliation remain open.

## 7. Gate 185 result

| Item | State |
|---|---|
| MatrixCapture source implementation | IMPLEMENTED |
| FrozenReportSnapshot v2 source implementation | IMPLEMENTED |
| Capture identity v2 source implementation | IMPLEMENTED |
| CapturedBenchmark additive API | IMPLEMENTED |
| Pure fixture test source | IMPLEMENTED — NOT EXECUTED |
| CI workflow | MANUAL ONLY — NOT DISPATCHED |
| JCS conformance | NOT VERIFIED |
| Package writer / independent verifier | NOT IMPLEMENTED |
| Calibration / Gate159 companions | NOT IMPLEMENTED |
| Synthetic producer execution | NOT AUTHORIZED / NOT EXECUTED |
| Scientific execution | NOT AUTHORIZED / NOT EXECUTED |

**Overall:** `IMPLEMENTED — STATIC REVIEW ONLY; TECHNICAL TESTS AND JCS CONFORMANCE OPEN`.

## 8. Next operation — Gate 186

Gate 186 should statically audit the capture implementation against the exact source report schema and capture-identity contract, close any code-level discrepancies, and then add the pure serialization/uint64 projection module. Do not run the pure tests or dispatch the workflow until separate technical execution authorization is explicit. Do not invoke the benchmark producer.

## 9. Corrective execution record — push-triggered preflight runs

The first Gate 185 source/test commits landed while the previous Gate 184 pure workflow still had its push trigger and its full future-module compile list. GitHub therefore ran that workflow on three commits:

- `3bf7cb56a8bf0da305e9802c7555eb52c3163b3b` — run `43542215502`;
- `f3fc6dd51d6e4bcb87611595c1e69cbf11731545` — run `43542249750`;
- `0fedd28ed20ced1ae3f6e1da1d630d0083e2cbd3` — run `43542308263`.

Each run installed the hash-pinned `rfc8785==0.1.4` dependency, then attempted the previous workflow's compile list and failed at the first not-yet-created module, `vcont_package_v2.py`. The test step was skipped in all three runs. The capture module appeared before the missing module in the compile command and its compilation completed without a reported syntax error. No test method, Generator, Sealer, Analyzer, Evaluator, producer, seed generation, calibration or scientific operation ran.

This was an unintended technical workflow execution caused by the still-active push trigger. It is recorded as a governance/configuration deviation, not a PASS. The workflow was then changed to manual-only and narrowed to the capture module plus its fixture test. The current workflow has not been dispatched. This correction supersedes §1/§5/§7 statements that implied no dependency installation or compilation occurred.

## 10. Gate 185 capture audit refinement

The report snapshot implementation now recomputes the legacy report fingerprint from the original source-typed `manifest` before any uint64 wrapper projection, using the exact Evaluator JSON round-trip and unchanged compact `_hash` sequence. A mismatch fails closed. The fixture source now computes a valid legacy fingerprint and includes a negative tampering case. This is source/test authoring only; the test remains unexecuted.

## 11. Gate 186 correction and conformance limitation

Gate 186 corrected the legacy report fingerprint algorithm identifier to the exact Gate 181 value: `TGCV-C10S-VCONT-LEGACY-REPORT-FINGERPRINT-PYJSON-SORTKEYS-COMPACT-SHA256-1`. It also strengthened capture identity validation so every outer-world bundle's scenario version and N must match the declared design identity. The corresponding identifier assertion was added to the pure fixture source; no tests were run.

Gate 186 found that nested `scenario_reports`, `coverage`, pair-ledger rows/contributions and nested metric/status structures are preserved recursively but do not yet have complete exact field allowlists. Unknown nested fields are not dropped, but schema drift is not rejected as Gate 181 requires. Therefore Gate 185's report projection is not yet a strict schema decoder and full Gate 181 conformance remains CONDITIONAL. Gate 187 is assigned to close these allowlists/cardinality checks from actual Evaluator source. See Gate 186.
