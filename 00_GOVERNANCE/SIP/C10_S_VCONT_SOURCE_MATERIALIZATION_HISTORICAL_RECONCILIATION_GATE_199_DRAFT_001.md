# C10-S V_cont — Gate 199: historical source-materialization contract reconciliation

**Status:** HISTORICAL REUSE AUDIT PASS; EXECUTION-SOURCE CLOSURE NOT ESTABLISHED; NEW MANIFEST SCHEMA NOT YET AUTHORIZED  
**Branch:** research/c10-s-consolidation-draft  
**Parent:** Gate 198 — canonical Git source-tree identity  
**Scope:** read-only reconciliation of existing C10-S package/source contracts, source code, workflow definitions, dependency locks and analogous TGCV materialization records. No source code, workflow, tests, package builder, producer, calibration or scientific execution was run.

## 1. Purpose

Gate 198 separated the committed Git tree identity from the bytes actually consumed by a runtime. Before creating a new materialization manifest, this gate checks whether the existing C10-S contracts already provide that identity and whether analogous TGCV manifests can be reused.

**Finding:** C10-S already has strong and increasingly complete package-content, configuration, snapshot and producer-evidence boundaries. It does not yet have a single independently verifiable declaration of the exact source/runtime input closure consumed by each execution. The missing layer is not another package archive digest or configuration fingerprint.

## 2. Historical C10-S contracts recovered

The following existing contracts were inspected on `research/c10-s-consolidation-draft`:

| Existing artifact | Reusable content | Boundary not covered |
|---|---|---|
| Gate 167 — evidence-export source boundary | Construction-point map; capture requirements; independent GitHub producer metadata boundary; no reconstruction of discarded source objects | Exact source/runtime file closure and environment identity |
| Gate 164 — package/report contract | Package inventory and required evidence roles | Source-tree/materialized-runtime manifest |
| Gate 178 — serialization and companion schema | Canonical JSON/JCS and exact-byte snapshot serialization boundaries | Actual checkout/materialization inputs |
| Gate 179 — uint64 wire-format decision | Typed source-seed transport | Source code and runtime closure |
| Gates 180–181 — source-schema crosswalk and source-to-wire projection | Exact source fields, projections, seed exclusions and package boundaries | Runtime source materialization |
| Gate 184 — CI execution boundary | Separation of pure package operations from producer/scientific execution | Immutable runner/action/runtime identity |
| Gate 186–190 — capture/source reconciliation | Source object joins, snapshots, exact RUN/R identity, report reconciliation | Full source/runtime dependency closure |
| Gate 194-G — configuration/source crosswalk | Effective 26-field ScenarioConfig projection, AnalysisContract and configuration-fingerprint crosswalk | Source-tree digest or materialized source digest |
| Gate 194-I — companion writer/verifier implementation | 28 configuration components, historical seed fingerprint, independent reconstruction and package-file integrity | Semantic verification of source-execution and technical-test provenance; source materialization |

The existing package-v2 inventory remains exactly 14 files. Its `provenance/source_execution.json` and `validation/test_evidence.json` are distinct companion boundaries. The writer accepts these as independently materialized companions; it does not establish that the contents accurately bind a GitHub run, attempt, artifact, source tree or runtime. Gates 195–197 address those external-evidence contracts. Gate 198 addresses Git tree identity. Neither should be folded into the 28-component configuration fingerprint.

## 3. What the current hashes actually identify

The current C10-S design contains several valid but non-interchangeable identities:

| Identity/digest | What it identifies | What it does not identify |
|---|---|---|
| Git commit SHA | Commit object and parent/history metadata | Runtime materialization by itself |
| Git root tree SHA-1 | Committed recursive Git tree graph | LFS payload bytes, submodule contents, checkout-filter output, generated/untracked inputs |
| Git blob SHA-1 | One committed blob object | Post-checkout transformed file bytes |
| FrozenSnapshot SHA-256 | Exact retained snapshot bytes | Executable source tree |
| MatrixCapture JCS/SHA-256 | Frozen matrix digest domain | Source code or runtime |
| 28 configuration components / aggregate fingerprint | Declared DGP/Generator, Analyzer, MatrixCapture and evaluation-assignment configuration components | Source file identity, dependencies, OS image or runner actions |
| Package manifest/archive SHA-256 | Exact package file inventory and archive bytes | Source that produced the package, unless independently joined |
| GitHub artifact metadata/digest | GitHub artifact resource and its archive digest semantics | Artifact-to-attempt foreign-key binding or semantic correctness of contents |
| Output SHA-256 | Exact output/capture bytes | Which source/runtime generated them |

**Decision:** retain each identity in its own evidence domain. Do not rename a configuration fingerprint or package digest to `source_digest`, and do not use the Gate 198 tree SHA-1 as a substitute for a SHA-256 materialization manifest.

## 4. Existing execution paths and observed materialization gaps

### 4.1 P178 Analyzer Monte Carlo workflow

The current `.github/workflows/c10-s-analyzer-monte-carlo.yml`:
- checks out `github.sha`;
- uses `actions/checkout@v4` and `actions/setup-python@v5`;
- selects Python `3.12`;
- installs `numpy==2.3.5` and `scipy==1.17.0` without a hash-locked requirements file;
- compiles/runs the legacy P178 focal harness;
- runs the primary 27-cell / 10,000-replication job;
- constructs a clean replay source archive using `git archive` over an explicit path list;
- replays and compares CSV and manifest bytes;
- records tested commit, run ID, attempt, event, ref and output hashes.

This is a useful existing execution-provenance pattern, but its source identity remains commit/path-declaration based. It does not hash the exact extracted source files as a manifest, pin action implementations by immutable commit SHA, identify the `ubuntu-latest` image revision, or record the full resolved Python environment. The replay archive path list is explicit, but no independently hashed archive/source-input manifest is emitted.

The workflow and README identify this as the earlier P178 focal harness, distinct from the integrated V_cont harness. Its evidence must not be relabelled as validation of the integrated C10-S estimand or package-v2 implementation.

### 4.2 Integrated synthetic harness workflow

The current `.github/workflows/c10-s-focal-harness-tests.yml`:
- is manual-only;
- requires an explicit boolean confirmation;
- is restricted to the research branch;
- checks out the exact event commit;
- uses Python 3.12 and direct NumPy/SciPy version pins;
- compiles and runs the integrated synthetic test suite;
- records commit/run/attempt/event/ref and a confirmation flag;
- uploads captures and manifest.

It does not hash the source files or resolved runtime. Its explicit confirmation and branch guards are execution-control properties, not source-materialization evidence.

### 4.3 Package-v2 pure workflow

The current `.github/workflows/c10-s-vcont-package-v2-pure-tests.yml`:
- is manual-only and read-only;
- enforces the exact research branch;
- checks out `github.sha`;
- uses Python 3.12;
- installs `rfc8785==0.1.4` using `requirements-vcont-v2.lock` and `pip --require-hashes --only-binary=:all:`;
- compiles and runs only the allowlisted pure capture/writer/verifier tests.

The lockfile pins the RFC 8785 wheel SHA-256. This is a stronger dependency-input control than the P178 direct version pins. It is still not a complete runtime lock: Python patch/build, pip version, transitive/runtime environment, OS image and GitHub Action implementation identities are not fully frozen. The workflow does not run the producer or create a real package.

### 4.4 Source-tree scope and replay

The clean replay uses `git archive` over a declared path list. That is an execution-specific source subset, not the complete repository tree. It is useful because it excludes unrelated repository content, but the path list alone does not prove which imported/transitive files were actually required. It also does not automatically include submodule contents or materialized LFS payloads.

For package-v2 pure tests, the relevant source closure includes at least the allowlisted test modules, capture/writer/verifier modules, their imported C10-S source modules and the pinned JCS dependency. The exact import/dependency closure must be derived from the selected workflow and commit, not copied from the broader repository tree.

## 5. Reusable TGCV precedent — and limits

Two analogous patterns were inspected:

1. **D-OPS Freeze Package 002 Materialization Audit 003:** hashes exact UTF-8 bytes of all declared package inputs and executable components, excludes the manifest from its own hash set, and recomputes hashes from GitHub-served content. This is a reusable exact-byte inventory principle, not a complete runtime materialization schema.
2. **VIATRA V002 fixture byte manifest/audits:** preserve SHA-256 and byte lengths for exact materialized fixture files and distinguish fixture-byte identity from runtime-equivalence evidence. The historical audit is explicitly superseded by a later canonical fixture manifest; it must not be copied as current VIATRA state.

These precedents support a separate file-inventory digest with exact byte lengths and SHA-256. They do not supply C10-S's workflow-specific source closure, checkout/filter rules, resolved dependencies, action/runtime identity or proof that a particular execution consumed those exact bytes.

The C10-S adapter provision/dependency graph is also not a substitute: it describes the experimental microdomain's provisioned dependencies and possible causal collateral paths, not the build/test runtime used by GitHub Actions.

## 6. Reconciliation: reuse versus genuinely open requirements

### Reuse without redesign

- Gate 198's Git commit/root-tree identity fields.
- Gate 167's separation of producer declarations from independent GitHub observations.
- Gate 181/178's canonical serialization and exact-byte snapshot principles.
- Gate 194-I's independent writer/verifier separation and fail-closed source references.
- The 14-file package inventory and existing `source_execution.json` companion role.
- The D-OPS exact-byte manifest pattern, adapted only after C10-S-specific scope is established.
- Existing workflow commit/run/attempt and output-hash records, retained as observations rather than treated as complete source attestation.

### Genuinely open

1. **Execution source closure:** exact repository paths consumed by a specific workflow/job/step, including imported local modules and explicitly declared data/config inputs.
2. **Materialized file identity:** canonical path, entry type, Git mode where applicable, materialized mode, byte length and SHA-256 of actual bytes consumed.
3. **Checkout/materialization policy:** exact checkout action implementation, Git version/config, line-ending and clean/smudge filters, sparse/path selection, submodule policy, LFS policy and relevant environment variables.
4. **Dependency closure:** lockfile identity and exact resolved distributions/wheels; package name/version/platform/tag/hash; distinguish direct from transitive dependencies.
5. **Runtime identity:** Python implementation/version/build, OS/runner image identity, architecture, relevant toolchain versions and action implementation SHAs. Mutable labels such as `ubuntu-latest` or action tags alone are declarations, not immutable identities.
6. **Generated/untracked inputs:** explicit allowlist and capture rule for files generated before the target operation; reject undeclared inputs or mark the source closure incomplete.
7. **Execution binding:** bind the source-materialization observation to exact repository, commit, workflow/run/attempt, job, step and artifact/output observations. Preserve Gate 197's distinction between direct association and bounded temporal corroboration.
8. **Independent verification:** a verifier must reconstruct the manifest digest and validate each referenced file/dependency against the declared source boundary. A producer-generated manifest alone remains a declaration.

### Explicit non-goals

- Hashing every file in the repository when a smaller exact execution closure is known.
- Treating package-v2's 14 package files as the source code that generated them.
- Including transient stdout/stderr or result outputs in the source manifest; those remain separate output evidence.
- Requiring a complete machine image/container digest if the workflow does not use one and the environment can instead be represented by a sufficiently explicit, verifiable runtime inventory. Any unrepresented mutable environment dimension must remain a limitation.
- Claiming that source integrity proves scientific validity, causal identification or the correctness of the producer.

## 7. Gate 195 schema implications

Do not create a second generic `source_execution` object or expand the existing 28-component configuration fingerprint.

The eventual evidence envelope should keep at least these domains separate:
- `git_source_identity` — commit and root tree object observation from Gate 198;
- `source_materialization` — execution-specific exact source/input file inventory and canonical SHA-256 manifest;
- `runtime_environment` — resolved interpreter, OS/architecture, toolchain, actions and dependency inventory;
- `workflow_execution` — independent GitHub run/attempt/job/step observations from Gates 196–197;
- `artifact_output` — exact artifact metadata/download and output hashes;
- `association` — direct or bounded source/run/artifact association with explicit status.

The final schema must use the existing package's `provenance/source_execution.json` role if it is compatible, or version that companion through the existing package schema governance. It must not silently add a fifteenth file or alter the frozen 14-file inventory. Whether the materialization manifest belongs inside that companion or is an independently referenced content-addressed record remains a schema decision for the next gate.

## 8. Evidence disposition

| Question | Result |
|---|---|
| Does C10-S already have canonical package serialization and file/archive digests? | YES |
| Does Gate 194-I provide source/configuration fingerprint components? | YES — configuration identity, not source code |
| Does Gate 167 define the need for independent producer metadata? | YES |
| Does current source-execution companion have independent semantic verification? | NO — remains outside current verifier's verified scope |
| Does the P178 workflow capture commit/run/attempt and output hashes? | YES |
| Does P178 source replay hash the exact extracted source closure? | NO |
| Does package-v2 pure workflow hash-lock its direct JCS wheel? | YES |
| Is the complete runtime environment immutable and independently identified? | NO |
| Is there an existing C10-S materialized-source manifest covering all open dimensions? | NOT FOUND IN THE AUDITED CONTRACT/SOURCE SET |
| Can a compatible exact-byte manifest pattern be reused? | YES — D-OPS/VIATRA precedents, with C10-S-specific scope |
| Is the materialization schema ready to freeze? | NO — execution profile and source closure must be specified first |

## 9. Gate disposition and next step

**Gate 199: HISTORICAL REUSE AUDIT PASS / MATERIALIZATION CONTRACT OPEN.**

The historical reconstruction found no compatible existing C10-S manifest that binds exact materialized source/runtime inputs to an execution. It did find reusable package, configuration, snapshot, workflow-provenance and exact-byte manifest mechanisms. These must be composed without semantic duplication.

**Next operation:** define the C10-S execution-profile registry and source-closure rules before writing the canonical SHA-256 manifest algorithm. At minimum, distinguish:
- P178 legacy focal Monte Carlo;
- integrated synthetic harness tests;
- V_cont package-v2 pure tests;
- any future authorized confirmatory producer/package operation.

For each profile, specify the exact workflow, job/step boundary, path allowlist, local imports, external inputs, dependency lock, and environment dimensions. Then define one canonical materialization-manifest serialization over those resolved inputs and test vectors. Do not run workflows, package generation, producers, calibration or scientific execution as part of that design step.
