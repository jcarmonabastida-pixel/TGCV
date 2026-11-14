# C10-S V_cont — Calibration and Seed-Bank Protocol

**Status:** IMPLEMENTED PROTOCOL SCAFFOLD — NUMERIC PRECISION TARGETS OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** Phase A synthetic V_cont benchmark only  
**Scientific execution:** NOT AUTHORIZED

## 1. Purpose and boundary

This protocol defines how calibration outputs may select candidate sample size N and assignment-replicate count R before an independent evaluation bank is opened.

It does not change the C1 estimands, DGP scenario definitions, Analyzer identification rules, or the distinction between ITT-Z, ITT-G and theta_A. It does not establish real-world causal identification or the TGCV `ΔT_acc → ΔValue` claim.

## 2. Two disjoint banks

### Calibration bank

Used only to:
- estimate scenario- and estimand-specific dispersion at candidate N values;
- calculate the calibration SD used for R dimensioning;
- select the smallest candidate N meeting all predeclared Monte Carlo precision targets;
- identify numerical instability and feasibility constraints.

### Evaluation bank

Used only after N, R, estimands, metrics and acceptance rules are frozen. It must not be used to tune N, R, tolerances, scenarios or analysis choices.

The banks use deterministic, domain-separated seed derivation with distinct bank labels. Within each scenario/N:
- the world seed is fixed across assignment replicates;
- Z assignment seeds vary by replicate;
- G assignment seeds vary independently by replicate;
- world, Z and G streams are distinct within each run;
- calibration and evaluation seed sets must be disjoint.

The implementation is in `vcont_benchmark_protocol.py`: `build_seed_bank` and `validate_seed_banks`.

## 3. Candidate N selection

The N grid is an explicit protocol input, not silently inferred from the harness default. Each candidate must satisfy the Generator constraints (N >= 16 and divisible by four).

For every candidate N, calibration must report precision separately for each predeclared scenario and estimand. The selection rule is the smallest N for which every required scenario-specific MCSE is no greater than its predeclared target:

`N* = min{N : MCSE_cal(s, e, N) <= target_MCSE(s, e) for every required (s,e)}`.

If no candidate qualifies, the result is `NO_CANDIDATE_N_MEETS_ALL_PREDECLARED_MCSE_TARGETS`; no extrapolation beyond the tested grid is permitted without a protocol amendment.

Implementation: `select_minimum_n`.

## 4. Assignment replicate count R

For each selected scenario/N/estimand, calibration estimates the across-assignment-replicate SD, `SD_cal`. The minimum R is:

`R = max(2, ceil((SD_cal / target_MCSE)^2))`.

Implementation: `required_replicates`.

This formula controls Monte Carlo precision of the simulated mean estimate, not sampling uncertainty of a real-world causal estimand. If the calibration SD is estimated imprecisely, the protocol must conservatively account for that uncertainty before freezing R; a plug-in point estimate alone is not an automatic guarantee.

## 5. Required calibration outputs

For each scenario and estimand:
- number of calibration assignment replicates;
- fixed world identity and scenario/N configuration hash;
- SD across assignment replicates;
- resulting MCSE for the planned R;
- selected N and R, with the exact target used;
- counts of identified, not-identified and indeterminate Analyzer results;
- abstention and invalid-run counts;
- seed-bank fingerprint and code/configuration hashes.

Do not pool scenarios to conceal a scenario-specific precision failure. Do not discard abstentions from denominators; report rates and denominators explicitly.

## 6. Metrics and inference boundary

Continuous recovery metrics: bias, MAE, RMSE, SD and MCSE.  
Adjudication metrics: identification, non-identification, indeterminacy and abstention rates.

Coverage, type-I error and power remain `NOT_EVALUATED` unless an inferential procedure with valid per-replicate interval/test outputs has been separately specified and implemented. The current Analyzer standard errors do not establish those properties. Wilson intervals in the protocol module quantify Monte Carlo uncertainty in simulated binary rates; they are not confidence intervals for causal effects.

## 7. Numeric decisions deliberately left open

The following values cannot be responsibly inferred from software defaults or unit-test fixtures and must be explicitly approved before the calibration bank is run:

1. Candidate N grid.
2. Minimum scientifically relevant effect / precision scale for each primary estimand, or an independently justified absolute target MCSE.
3. Target MCSE by scenario and estimand.
4. Calibration replicate budget or adaptive stopping rule for estimating `SD_cal` with adequate precision.
5. The required scenario/estimand set for N and R selection.
6. Any scientific recovery tolerance. The existing test tolerance 0.10 is not promoted to a scientific criterion.

If a target is expressed relative to a minimum relevant effect `δ_min`, its ratio must also be approved explicitly; no ratio is assumed by this protocol.

## 8. Freeze and authorization sequence

1. Approve the numeric decisions in §7.
2. Freeze the N grid, targets, scenario/estimand set and calibration stopping rule.
3. Generate calibration bank only; persist its manifest and outputs.
4. Select N and R using the predeclared rules; record all failures and feasibility limits.
5. Freeze the evaluation-bank seed plan, N, R, metrics and acceptance criteria.
6. Conduct a separate authorization gate before generating the evaluation bank.

This document and its software are protocol preparation only. No calibration run, benchmark execution, or scientific execution is authorized by this record.


## 9. Gate 143–144 pair-keyed implementation alignment

The executable pair identity is (scenario_id, scenario_version, estimand_id, estimand_version). The protocol provides a 52-record coverage matrix for four V_cont assignment estimands across 13 benchmark scenarios, pair-specific summaries and R sizing, and a fail-closed pair-keyed N selector. Candidate N is eligible only when all predeclared coverage keys are present and every numeric EVALUABLE key has a finite MCSE within its own predeclared target. STATUS_ONLY and NOT_IDENTIFIABLE keys remain mandatory coverage records but do not receive numeric MCSE or recovery scoring. Numeric targets and the final required subset remain OPEN.

The legacy scenario-only selector is retained for historical result compatibility; it is not the conforming selector for new pair-keyed calibration. SeedAssignment now carries scenario_version, includes it in deterministic seed derivation and bank fingerprints, and groups fixed-world checks by scenario ID, scenario version and N. The default UNVERSIONED value is retained only for legacy callers; new governed banks must supply explicit scenario versions. No calibration or evaluation seed bank was generated by this source change.


## 10. Gates 149–152 — temporal aggregation and joint design contract (2026-11-13)

**Status:** DOCUMENTED DESIGN CONTRACT — IMPLEMENTATION GAP REMAINS OPEN  
**Execution:** no calibration, Monte Carlo, benchmark or scientific execution is authorized or recorded by this addendum.

This addendum reconciles the temporal aggregation gates with the existing pair-keyed matrix, Evaluator adapter and calibration/seed-bank scaffold. It does not change the four assignment estimands, the 52 required scenario–estimand coverage records, DGP truths, identification assumptions or numeric acceptance thresholds.

### 10.1 Gate 149 — aggregation identity and temporal levels

Every aggregation record is keyed by:

`K* = (scenario_id, scenario_version, estimand_id, estimand_version, temporal_level)`.

The supported temporal levels are:

- `RUN`: one generated dataset and one Analyzer/Evaluator run.
- `REPEATED_ASSIGNMENT`: aggregation over repeated joint Z×G assignments within one fixed generated synthetic world and one fixed scenario/DGP parameterization.
- `MONTE_CARLO`: aggregation over independent outer benchmark replications. This level is introduced by this design contract and is not yet implemented by the current harness.

The matrix remains authoritative for whether a pair is numerically scoreable or status-only at each level. The 52 scenario–estimand coverage obligations are retained; coverage does not imply that every pair has a numeric truth or estimate.

### 10.2 Gate 150 — metric-to-level mapping

| Estimand/pair class | RUN | REPEATED_ASSIGNMENT | MONTE_CARLO |
|---|---|---|---|
| ITT-Z run-conditional | Numeric error/recovery against run-conditional truth | Not a substitute for run-level truth | Aggregate distribution of run-level performance |
| ITT-Z mechanism-marginal | No numeric marginal recovery from one run | Numeric marginal recovery against mechanism-marginal truth | Aggregate performance across independent outer replications |
| ITT-Z reference-regime | Identification/status only; no comparison of a single run estimate to marginal reference truth | Numeric reference recovery only when identified and truth-comparable | Aggregate performance and identification rates |
| ITT-G, Z=0 | Numeric error/recovery against the declared run truth | Not applicable to the run-level assignment contrast unless a distinct repeated target is declared | Aggregate run-level performance |
| STATUS_ONLY / NOT_IDENTIFIABLE | Status adjudication | Status aggregation only if declared by the matrix | Status rates; never numeric error or recovery |

For all levels:
- report coverage counts and denominators;
- report bias, MAE, RMSE and recovery only for eligible numeric records;
- report identification, non-identification, indeterminacy, abstention and invalid-output rates with explicit denominators;
- do not count missing records as abstentions;
- do not coerce null or NOT_EVALUABLE to zero;
- do not pool scenario/version/estimand/temporal-level identities;
- preserve non-numeric pairs in coverage even when they are excluded from numeric summaries.

### 10.3 Gate 151 — hierarchy and meaning of N, R and M

The design hierarchy is:

`scenario/version/estimand → outer replicate m (1…M) → joint assignment r (1…R) → units i (1…N)`.

- `N`: units in each generated dataset/run. It governs within-run information and estimator precision.
- `R`: repeated joint Z×G assignments within the same fixed synthetic world. It governs precision of assignment-marginal aggregates, including mechanism-marginal and reference-regime targets where the matrix permits them.
- `M`: independent outer Monte Carlo replications of the benchmark procedure. Each outer replicate uses a newly generated synthetic world/sample under the same fixed scenario version and DGP parameterization; within each outer replicate, the world is held fixed across its R assignment repetitions. M quantifies uncertainty in benchmark performance summaries across independent outer replications.

The current seed scaffold fixes one world seed across assignment replicates within scenario/version/N. This is consistent with the R level but does not yet represent M independent outer replications. The implementation currently has no explicit outer-replicate identity/dimension. Consequently, MONTE_CARLO summaries across M are a specified requirement, not an implemented capability.

A draw of DGP parameters from a distribution is not silently folded into M. The present contract is conditional on the declared scenario version and fixed DGP parameterization. If a future target averages over parameter configurations, that requires an explicit world/parameter sampling distribution, target definition, versioned identity and separate analysis; it is not authorized by this addendum.

For a scalar benchmark metric `psi_m` computed once per independent outer replicate:

`MCSE(mean(psi)) = SD(psi_1,…,psi_M) / sqrt(M)`.

For a binary metric (e.g. recovery, identification or correct abstention), the Monte Carlo standard error of its estimated rate is:

`MCSE(p_hat) = sqrt(p_hat * (1-p_hat) / M)`.

A candidate M may be planned using `M >= ceil((SD_cal / target_MCSE)^2)`, or the corresponding conservative binary-rate bound, using a separate calibration source and predeclared target. Calibration and confirmatory evaluation seeds must be disjoint. The empirical plug-in SD is not an automatic precision guarantee; uncertainty in the calibration SD must be addressed conservatively before M is frozen.

**Important reconciliation with the existing implementation:** `required_replicates(calibration_sd, target_mcse)` currently sizes the assignment-replicate dimension R. It must not be reinterpreted as sizing M. A separate M-sizing rule and explicit outer-replicate identity are required before MONTE_CARLO summaries can be implemented.

### 10.4 Gate 152 — joint design specification and sufficiency states

Each design configuration is keyed by scenario/version, estimand/version and temporal level, and must declare:
- N, R and M values or an explicit `NOT_APPLICABLE` for dimensions not required by that estimand/level;
- precision targets and the metric/denominator to which each target applies;
- truth source, truth identity/version and comparability rule;
- assignment support and identification requirements;
- seed protocol and calibration/evaluation bank fingerprints;
- required coverage keys and any predeclared exclusions;
- design configuration identity/version and status.

Sufficiency is multidimensional and must not be collapsed into one unqualified PASS:

- `DESIGN_SUFFICIENT`: every applicable design dimension, truth/support prerequisite and precision target passes.
- `DESIGN_INSUFFICIENT_N`: within-run sample-size requirement fails.
- `DESIGN_INSUFFICIENT_R`: repeated-assignment precision requirement fails.
- `DESIGN_INSUFFICIENT_M`: outer Monte Carlo precision requirement fails.
- `DESIGN_SUPPORT_FAILURE`: the declared assignment support cannot identify the target under the approved contract.
- `DESIGN_TRUTH_MISMATCH`: truth and evaluated estimand/regime are not comparable.
- `DESIGN_SPECIFICATION_INCOMPLETE`: a required design parameter, target, provenance field or rule is absent.

Multiple failure reasons may coexist. `NOT_APPLICABLE` is not a precision PASS. Design sufficiency only permits the relevant evaluation; it does not guarantee Analyzer recovery or causal identification.

The order of design preparation is: freeze estimand/truth/support and target population; dimension N for within-run estimation; dimension R for repeated-assignment targets; dimension M for benchmark performance summaries; then validate full pair coverage and all design identities before opening the confirmatory evaluation bank.

The current code's pair-keyed N selector and R-sizing helper remain scaffolding. This addendum does not certify that their calibration inputs already implement all three dimensions or the full sufficiency state machine. In particular, no numerical N/R/M values, MCSE tolerances, recovery tolerances, required confirmatory subset or calibration stopping rule are approved here.

### 10.5 Implementation and verification obligations

Before the MONTE_CARLO level can be marked IMPLEMENTED, the harness must:
1. add an explicit outer-replicate identity to seed assignments, manifests, TruthBundle/outputs and aggregation keys;
2. generate independent world seeds across M while holding each world fixed across its within-world R assignment repetitions;
3. preserve disjoint calibration/evaluation banks across all world, Z and G seed streams;
4. compute one correctly defined metric contribution per outer replicate and aggregate only across independent M units;
5. keep R-level marginal-target recovery separate from M-level uncertainty in benchmark performance;
6. preserve the 52-pair coverage matrix and temporal-level eligibility rules;
7. reject duplicate, missing, cross-version, cross-world or non-independent replicate identities as specified;
8. expose separate N-, R- and M-sufficiency outcomes and retain all failure reasons;
9. test null/missing/invalid/status-only cases without denominator loss or numeric coercion.

Technical tests and CI may verify implementation conformance when separately authorized. Calibration, seed-bank generation, Monte Carlo sizing runs, benchmark execution and scientific execution remain outside this contract and require their own explicit authorization.

### 10.6 Gate status

- Gate 149: aggregation identity and temporal levels — DEFINED.
- Gate 150: metric-to-level mapping — DEFINED.
- Gate 151: N/R/M hierarchy and Monte Carlo precision — DEFINED; M implementation OPEN.
- Gate 152: joint design and sufficiency contract — DEFINED; numeric design choices OPEN.
- Existing calibration protocol scaffold: IMPLEMENTED as previously recorded; it does not yet implement M.
- This addendum: DOCUMENTARY PERSISTENCE ONLY; no code, tests, CI or scientific execution changed or ran.


## 11. Gate 154 — outer Monte Carlo replication contract

The explicit outer-replication identity, world-seed variation across M, designated RUN assignment, within-world R repeated assignments, stream roles, manifest provenance and two-stage aggregation contract are governed by:

`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_OUTER_REPLICATION_CONTRACT_DRAFT_001.md`.

This contract supersedes any ambiguous interpretation of the legacy `SeedAssignment.replicate`: that field represents assignment repetition R only and is not an outer Monte Carlo replicate. The current implementation remains without explicit M and must not be described as providing independent outer-world replication.

The existing `required_replicates(calibration_sd, target_mcse)` continues to size R only. M requires its own predeclared sizing and calibration-uncertainty procedure. No numerical M, new seed bank, calibration, Monte Carlo or scientific execution is authorized by this cross-reference.

**Gate 154 status:** DEFINED and cross-referenced; implementation OPEN.


## 12. Gate 155 — outer M implementation

**Implementation record:** `00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_OUTER_REPLICATION_IMPLEMENTATION_GATE_155_DRAFT_001.md`.

The seed-bank and harness implementation now carries `outer_replicate_id` and `assignment_role`, preserves one designated RUN and R repeated assignments within each outer world, derives distinct world seeds across M, and provides a two-stage Evaluator aggregation over within-world R followed by across-world M. Bias, MAE, RMSE (delta-method MCSE), recovery and identification metrics are aggregated only when the authoritative matrix marks the corresponding temporal pair EVALUABLE.

The legacy `replicate` remains the R assignment index; `replicate=-1` plus `assignment_role=RUN` denotes the designated run. Seed-bank fingerprints include M identity and role. The existing `required_replicates` continues to size R only; no numeric M sizing rule or target is inferred here.

**Gate 155:** IMPLEMENTED and TECHNICALLY VERIFIED — commit `3159ab10566e61eff97cb6d0a10bfc3801a6291b`, workflow run `43490700407` (compile PASS; primary 94/94 PASS; clean replay 94/94 PASS). Full implementation record: `C10_S_VCONT_MONTE_CARLO_OUTER_REPLICATION_IMPLEMENTATION_GATE_155_DRAFT_001.md`. No calibration or evaluation seed bank was generated. No Monte Carlo sizing, benchmark or scientific execution is authorized or recorded.


## 13. Gate 156 — MONTE_CARLO matrix coverage and temporal manifest

**Status:** DEFINED / PERSISTED — IMPLEMENTATION OPEN.

The Gate 155 Evaluator currently aggregates the four estimand pairs for one scenario/version at a time. Gate 156 defines the remaining benchmark-level integration: compose the 13 scenario blocks into the authoritative 52-pair ledger, enforce declared M and R completeness, retain one per-M contribution for every pair at its matrix-authorized temporal level, adjudicate statuses and denominators against the matrix, and preserve reconstruction fingerprints.

Canonical contract:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_MATRIX_COVERAGE_CONTRACT_GATE_156_DRAFT_001.md`.

This is a contract/persistence update only. Gate 156 implementation is OPEN. No seed bank has been generated; no calibration, Monte Carlo sizing, benchmark or scientific execution has been performed or authorized. Numeric N/R/M and MCSE targets remain OPEN.


## 14. Gate 157 — implementation preflight

**Status:** PREFLIGHT COMPLETED / PERSISTED — CODE IMPLEMENTATION OPEN.

The Gate 157 preflight confirms that Gate 155's per-scenario M evaluator is reusable, but the full 52-pair benchmark aggregator, declared design object, pair-keyed metric targets, exact R completeness and reconstructable per-M ledger remain unimplemented. It also identifies a typed R-index propagation gap: `SeedAssignment.replicate` exists, but the runtime chain does not yet carry a dedicated assignment index through ScenarioConfig, RunManifest, TruthBundle and AnalyzerResult.

Canonical preflight record:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_GATE_157_IMPLEMENTATION_PREFLIGHT_DRAFT_001.md`.

No code/test change, seed-bank generation, calibration, Monte Carlo sizing, benchmark or scientific execution was performed in this preflight.


## 15. Gate 157 — benchmark-level MONTE_CARLO aggregation

**Status:** IMPLEMENTED / TECHNICALLY VERIFIED.

Canonical implementation record:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_BENCHMARK_AGGREGATION_IMPLEMENTATION_GATE_157_DRAFT_001.md`.

Gate 157 completes the Gate 156 benchmark-level integration. The typed R assignment index now propagates through Generator, sealed provenance, TruthBundle, AnalyzerResult and Evaluator; each M requires one RUN with index -1 and exactly the declared contiguous R indices. The benchmark aggregator composes all 13 scenarios and 52 matrix pairs, emits the full temporal manifest and per-M contribution ledger, applies matrix-authoritative temporal/status classes, preserves separate denominators and emits a report fingerprint bound to design, targets, temporal manifest and ledger.

**Technical verification:** commit `0afb77fb45308a7d1573d0ab644a9d6f69e7302d`, workflow run `43494346461`; compile PASS, primary suite 99/99 PASS, clean source-archive replay 99/99 PASS. Artifact `14070228979`, SHA-256 `c9cb24f9d4504f609abbf8d7eaa8ce0ad839279cbc0b2ddc0c2768b8b1a556c7`.

This verification is deterministic software testing only. No calibration/evaluation seed bank was generated; no numeric N/R/M sizing, calibration, benchmark study or scientific execution was performed or authorized. The caller must supply canonical seed-bank, executable and configuration provenance; this implementation does not select those values.


## 16. Gate 157 targeted classification regression — CLOSED

The benchmark-level MONTE_CARLO implementation and targeted classification verification are recorded in:

`C10_S_VCONT_MONTE_CARLO_BENCHMARK_AGGREGATION_IMPLEMENTATION_GATE_157_DRAFT_001.md`.

The dedicated regression distinguishes `TRUTH_MISSING` from `INVALID_OUTPUT` and asserts their counters and denominators. Verified commit: `a399c5810fa988b31390e2957671f6bf134836b7`; GitHub Actions run `43496381997`; compile PASS, primary suite 100/100 PASS, clean source-archive replay 100/100 PASS. Artifact `14070369862`, SHA-256 `c9a3050c8081bb48099b57ad123cd2e955c31f88791529016c2943252b5f9ffd`.

This closes the narrow software regression only. No calibration, seed-bank generation, N/R/M sizing, benchmark study or scientific execution was performed or authorized.

## 17. Gate 158 — Monte Carlo report provenance audit

Gate 158 static audit is persisted in:

`C10_S_VCONT_MONTE_CARLO_PROVENANCE_AUDIT_GATE_158_DRAFT_001.md`.

Audit verdict: **AUDITED — CONDITIONAL / PROVENANCE BINDING NOT IMPLEMENTED**.

The report fingerprint currently binds the report payload internally, but the declared seed-bank fingerprint, executable commit and configuration fingerprint are only syntax-checked caller inputs. The Evaluator does not recompute or compare them against the actual SeedAssignment bank, runtime/source commit and canonical run configuration. The Evaluator also does not invoke the separate seed-bank validator or fully reconcile each RunManifest to its canonical SeedAssignment row.

Required next step: implement the Gate 158 provenance-binding layer and adversarial tests listed in the audit before claiming verified provenance. This is a technical integrity requirement; it does not authorize calibration, seed-bank generation, N/R/M sizing, benchmark execution or scientific execution.

## 18. Gate 159 — provenance-binding implementation preflight

Gate 159 implementation preflight is persisted in:

`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_PROVENANCE_BINDING_IMPLEMENTATION_PREFLIGHT_GATE_159_DRAFT_001.md`.

The preflight reuses the existing canonical seed-bank fingerprint and bank-separation validator, and defines the missing binding between the exact evaluation SeedAssignment manifest, calibration/evaluation separation, runtime execution attestation, effective Generator/Analyzer configuration, and each evaluated RunManifest. It requires fail-closed one-to-one reconciliation of every run to its canonical seed row before the 52-pair report is accepted.

The executable identity must be attested at the execution boundary; a caller-supplied SHA string or report self-fingerprint is not evidence of the source commit that actually ran. Configuration identity must be recomputed from the effective versioned DGP and Analyzer objects. Provenance failures are integrity/contract failures and must not be relabelled as Analyzer abstentions or estimand outcomes.

**Gate 159 status:** PREFLIGHT COMPLETED / PERSISTED; CODE IMPLEMENTATION OPEN; ADVERSARIAL REGRESSION OPEN.

This preflight authorizes no calibration/evaluation seed-bank generation, N/R/M sizing, Monte Carlo benchmark execution or scientific execution. `main` remains unchanged; PR #116 remains Draft on its existing base branch.


### Gate 159 continuation — authentication trust boundary

The Gate 159 preflight has been extended to distinguish declared provenance, deterministically reconciled provenance, and externally authenticated execution provenance. The current Python process cannot authenticate its own commit from caller-supplied fields or environment variables. An externally verifiable attestation mechanism and trust root must be governed before any report can receive an authenticated-provenance status.

Seed-bank, RunManifest and effective-configuration reconciliation may proceed independently, but those checks establish consistency only, not execution-origin authenticity.

**Current Gate 159 status:** seed/configuration/manifest reconciliation OPEN; external attestation trust mechanism ARCHITECTURE DECISION REQUIRED / BLOCKED; authenticated provenance status BLOCKED. No code, tests, CI, calibration, seed-bank generation, sizing or scientific execution is claimed by this addendum.


## 19. Gate 160 — external execution-attestation architecture

**Architecture decision:** select GitHub Artifact Attestations (`actions/attest@v4`, Sigstore/OIDC) for signing the finalized Monte Carlo report package, with verification through `gh attestation verify`, subject to a read-only repository visibility/plan availability preflight and a pinned trusted-builder workflow.

Canonical decision:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_ATTESTATION_ARCHITECTURE_DECISION_GATE_160_DRAFT_001.md`.

The attested subject is the final immutable report package digest. Its internal manifest binds the report, canonical seed manifests and fingerprints, effective configuration fingerprint, M/R/RunManifest reconciliation ledger, source identity and validation results. The verifier must pin repository identity, signer workflow/revision, OIDC issuer, predicate type and source identity. A caller-supplied environment variable, SHA string or `attested=true` cannot elevate provenance status.

**Availability condition:** artifact attestations are available for public repositories on current GitHub plans; private/internal repositories require GitHub Enterprise Cloud. Repository visibility and entitlement are not yet verified. If unavailable, stop and return to architecture decision; do not fall back to unsigned/self-asserted metadata.

Gate 160 selects architecture only. It does not authorize workflow/code changes, CI, calibration, seed-bank generation, N/R/M sizing, Monte Carlo benchmark or scientific execution. Gate 159 reconciliation and external-verifier implementation remain OPEN.


## 20. Gate 161 — attestation availability and trusted-builder preflight

Gate 161 preflight is persisted in:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_ATTESTATION_AVAILABILITY_AND_TRUSTED_BUILDER_PREFLIGHT_GATE_161_DRAFT_001.md`.

GitHub repository metadata confirms TGCV is public (repository ID `1348691577`). Public visibility satisfies the documented Artifact Attestations plan-class availability condition. The preflight does **not** establish that a trusted signer workflow already exists or is correctly configured.

The assumed path `.github/workflows/c10-s-vcont-benchmark.yml` returned NOT_FOUND. No complete workflow inventory or exact signer workflow identity has yet been established; no workflow path or revision is invented. Trusted-builder selection and immutable revision remain OPEN.

The verifier contract requires exact artifact digest, repository and signer-workflow identity, OIDC issuer, SLSA predicate, source identity and structured verification result. Numeric repository ID is an additional policy value and must not be called cryptographically verified unless the verifier exposes a cryptographically bound field for it. The pinned `actions/attest` revision's actual minimum permissions must be checked; its current README lists `id-token: write`, `attestations: write`, and `artifact-metadata: write`, while GitHub's basic documentation example also includes `contents: read`.

**Gate 161 status:** PUBLIC REPOSITORY AVAILABILITY CONFIRMED; TRUSTED WORKFLOW IDENTITY OPEN; VERIFIER IMPLEMENTATION OPEN. No workflow/code change, CI, attestation generation, calibration, seed-bank generation, N/R/M sizing, Monte Carlo benchmark or scientific execution was performed or authorized.


## 21. Gate 162 — workflow inventory and trusted-builder suitability audit

The complete `.github/workflows/` directory was recovered from GitHub at both `main` and `research/c10-s-consolidation-draft`: 50 files on main and 55 on the research branch. The research branch contains five additional C10-S workflows and no same-named workflow modifications relative to main. Their exact paths, blob SHAs, relevant path-specific commit history and security review are recorded in:

`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_TRUSTED_WORKFLOW_INVENTORY_AUDIT_GATE_162_DRAFT_001.md`.

The five C10-S workflows are the P178 performance diagnostic, clean replay, Monte Carlo runner, exact-cache probe and focal harness contract tests. The assumed `c10-s-vcont-benchmark.yml` path does not exist. The existing C10-S workflows grant only `contents: read`, do not create Artifact Attestations, do not declare OIDC/attestation permissions, and use mutable action tags. They are execution/replay/test workflows, not trusted signers.

The focal harness test workflow is the closest existing unprivileged test job: its history records explicit compilation of the Vcont integrated harness and benchmark protocol. It remains unsuitable as a signer. A dedicated trusted builder/attestor is required and must consume an already finalized report package; it must not rerun scientific or Monte Carlo work merely to sign.

**Gate 162 status:** INVENTORY RECOVERED; BRANCH DELTA AUDITED; EXISTING SIGNER CANDIDATES REJECTED AS-IS; DEDICATED TRUSTED BUILDER DESIGN OPEN. No workflow was modified, no signing permissions were added, and no CI, attestation generation, calibration, seed-bank generation, sizing or scientific execution was performed.


## 22. Gate 163 — dedicated trusted-builder design and threat model

Gate 163 architecture and threat model are persisted in:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_TRUSTED_BUILDER_DESIGN_GATE_163_DRAFT_001.md`.

The selected design separates the existing unprivileged producer/test workflow from a dedicated attestor stored on canonical `main`. The attestor must never check out or execute producer source/artifact content; it resolves the exact producer run/artifact through GitHub metadata, validates allowlisted metadata and recomputed package digests, and attests only the finalized immutable package. It must not rerun Monte Carlo or scientific work.

The threat model treats every producer artifact field and archive entry as attacker-controlled, including path traversal, symlinks, malformed/oversized archives, forged source metadata, replay and workflow-run privilege escalation. It requires strict schema/size/path checks, no executable deserialization, no shell interpolation of artifact fields, full-SHA action pins, least privilege, event/ref restrictions and fail-closed verification. A cryptographic attestation cannot replace Gate 159's deterministic seed/configuration/manifest reconciliation or establish scientific validity.

**Gate 163 status:** DESIGN DEFINED / PERSISTED; report package schema and canonical packager OPEN; Gate 159 reconciliation OPEN; attestor workflow implementation OPEN and requires separate explicit authorization; verifier and adversarial tests OPEN. No code/workflow change, CI, attestation generation, calibration, seed-bank generation, sizing or scientific execution was performed or authorized.


## 23. Gate 164 — Monte Carlo report-package schema and canonical packager

Gate 164 package schema v1.0.0 is persisted in:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_REPORT_PACKAGE_SCHEMA_AND_CANONICAL_PACKAGER_GATE_164_DRAFT_001.md`.

The schema defines one immutable attestation subject and an allowlisted package layout covering the complete report/52-pair ledger, benchmark design and matrix, effective scenario and analysis configurations, evaluation and calibration seed manifests, temporal/run records, source-execution provenance, configuration fingerprints, reconciliation results and technical test evidence.

Canonical serialization is RFC 8785 JCS; the archive profile is uncompressed deterministic POSIX tar with normalized metadata. The digest graph is non-circular: per-file SHA-256 values feed manifest.json; its digest determines package identity; the exact final archive SHA-256 is the external attestation subject and is not embedded inside the package. The existing report fingerprint remains a distinct report-level integrity value.

The package preserves M as independent outer worlds, R as within-world repeated assignments and the designated RUN separately. It requires 13 scenarios, 52 unique scenario-estimand pairs, one RUN plus R rows per scenario/M, complete one-to-one SeedAssignment/RunManifest reconciliation, explicit denominators and distinct TRUTH_MISSING / INVALID_OUTPUT classifications. Null is not zero; missing/invalid outputs are not abstentions. Marginal estimands are aggregated within M before any between-M summary.

**Implementation-relevant code boundary recovered:** the current Evaluator already returns design, temporal_manifest, pair_ledger, report manifest, scenario_reports, coverage and report_fingerprint. Its temporal_manifest currently carries the reduced scenario/version/N/M/role/R/run/world/seed fields; the package contract additionally requires the complete canonical RunManifest and run-level TruthBundle/AnalyzerResult/contract/evaluation records. The current report fingerprint uses the existing internal JSON hash path; it is not JCS and must remain a distinct legacy report digest unless a separately versioned report protocol changes it. The packager must create JCS canonical package files without silently redefining that existing fingerprint.

The current design carries declared seed-bank, executable-commit and configuration fingerprints; Gate 158/159 findings remain binding: these declarations cannot be promoted to reconciled provenance until actual seed rows, effective configuration payloads and source execution identity are independently bound. Calibration seed disjointness cannot be recomputed from a fingerprint alone; the actual calibration manifest or an immutable retrievable manifest is required.

**Gate 164 status:** PACKAGE CONTRACT DEFINED / PERSISTED; PACKAGER IMPLEMENTATION OPEN; report-schema alignment OPEN; Gate 159 reconciliation OPEN; calibration manifest availability OPEN; adversarial tests OPEN. No code/tests/workflows/CI were changed or executed. No calibration, seed-bank generation, N/R/M sizing, Monte Carlo benchmark or scientific execution was performed or authorized.


## 24. Gate 165 — implementability audit of the canonical Monte Carlo package

Gate 165 static audit is persisted in:
`00_GOVERNANCE/SIP/C10_S_VCONT_MONTE_CARLO_PACKAGE_IMPLEMENTABILITY_AUDIT_GATE_165_DRAFT_001.md`.

**Verdict: AUDITED — CONDITIONAL / NOT IMPLEMENTABLE AS WRITTEN FROM CURRENT AGGREGATOR OUTPUT.**

The current Evaluator can supply the 52-pair ledger, M-level contributions, coverage, denominators, reduced temporal manifest, benchmark design claims and existing report fingerprint. The exact matrix is derivable only if the same matrix object used by the Evaluator is retained.

The current aggregation boundary does not preserve the full evidence needed by Gate 164. ScenarioConfig is not returned; AnalysisContract is transient in the input tuple; exact SeedAssignment rows and bank/namespace identity are not passed; temporal_manifest is a reduced projection rather than a complete RunManifest; SealedEvidence and per-run EvaluationReport are absent from the aggregation tuple/return; calibration assignments are not an input; effective configuration payloads, Gate 159 reconciliation results and GitHub-resolved workflow/artifact metadata are absent. Existing seed/report fingerprints use their own legacy serialization and must not be relabelled as JCS.

The current code statically contains separate TRUTH_MISSING and INVALID_OUTPUT contribution classifications and counts. For Gate 165 these are classified **STATICALLY PRESENT / RUNTIME UNVERIFIED**; no tests were run.

Before the packager, freeze a typed immutable evidence-export boundary carrying exact per-run ScenarioConfig, SeedAssignment, RunManifest, matrix-relevant TruthBundle fields, SealedEvidence digest/manifest, AnalyzerResult, AnalysisContract and EvaluationReport; plus benchmark-level design, exact matrix, calibration manifest, source-execution reference and reconciliation/test evidence references. Do not reconstruct missing evidence from reduced report rows or promote producer assertions to authenticated provenance.

**Next:** Gate 166 — freeze typed evidence-export interface, cardinalities, join keys, data-minimization boundary and provenance split. No code/tests/workflows/CI changes or execution were performed.


## 25. Gate 166 — typed evidence-export contract

Gate 166 is persisted in:
`00_GOVERNANCE/SIP/C10_S_VCONT_TYPED_EVIDENCE_EXPORT_CONTRACT_GATE_166_DRAFT_001.md`.

Schema: `TGCV-C10S-VCONT-EVIDENCE-EXPORT` v1.0.0. It freezes the benchmark envelope and one immutable RunEvidenceRecord per scenario/version/N/M/role/R-index/run. For the current 13-scenario design at one N, the required count is exactly 13 × M × (1+R), with one RUN (-1) and R rows (0..R-1) per scenario/M. The exact 52-row matrix is retained.

Each record binds the exact SeedAssignment, complete RunManifest, full per-run ScenarioConfig, structural ScenarioConfig projection, AnalysisContract, matrix-relevant TruthBundle fields, SealedEvidence manifest/digest, AnalyzerResult and EvaluationReport. AnalysisContracts may be deduplicated by content digest, but every run must reference its exact contract. One RepeatedAssignmentReport is retained per M; the designated RUN EvaluationReport remains distinct.

The TruthBundle export is limited to the exact truth fields used by the current matrix; full potential-outcome arrays are excluded by default. `theta_a_truth` remains explicit null/value and is not made scoreable by inclusion. Raw SealedEvidence rows are excluded by default; digest recomputation is RECONCILED only if the canonical sealed representation is retrievable. A digest alone remains DECLARED/UNVERIFIABLE.

The contract distinguishes producer execution claims from GitHub-resolved metadata and technical test runs from scientific benchmark runs. Calibration/evaluation disjointness must be recomputed from actual materialized or immutably retrievable manifests; hashes alone are insufficient.

**Gate 166 status:** INTERFACE CONTRACT DEFINED / IMPLEMENTATION OPEN. No code/tests/workflows/CI changes or execution were performed. Next: Gate 167 source-boundary mapping and compatibility audit.


## 26. Gate 167 — evidence-export source-boundary audit

Gate 167's static audit is persisted in:
`00_GOVERNANCE/SIP/C10_S_VCONT_EVIDENCE_EXPORT_SOURCE_BOUNDARY_AUDIT_GATE_167_DRAFT_001.md`.

The audit confirms that Generator, Sealer, Analyzer and Evaluator construct the required source objects, but the current Monte Carlo aggregation interface transports only `(TruthBundle, AnalyzerResult, AnalysisContract, RunManifest)`. It omits ScenarioConfig, SeedAssignment and SealedEvidence. Gate 166 export must therefore capture a typed RunEvidenceBundle at the orchestration boundary before reduction; it cannot reconstruct omitted records from the aggregate Evaluator output.

SealedEvidence retains rows and manifest in memory, so its existing digest can be recomputed at capture. Independent later verification after raw-row minimization requires an immutable retrievable canonical evidence object; no such durable locator/store is currently implemented.

**Gate 167:** AUDITED — CONDITIONAL. **Gate 168:** freeze RunEvidenceBundle and sealed-evidence retention/retrieval contract. No code/tests/CI changes, runtime verification, calibration, seed generation or scientific execution were performed.

## 27. Gate 168 — RunEvidenceBundle and SealedEvidence retention

Gate 168 is persisted in:

`00_GOVERNANCE/SIP/C10_S_VCONT_RUN_EVIDENCE_BUNDLE_AND_SEALED_EVIDENCE_RETENTION_CONTRACT_GATE_168_DRAFT_001.md`.

The gate defines the immutable per-execution `RunEvidenceBundle` and the per-M `OuterWorldEvidenceBundle`, with exact Gate 166 join keys and cardinalities. Capture occurs in the orchestration boundary after Evaluator returns and before source objects leave scope; no source object is reconstructed from aggregate report output. Nested mutable payloads must be snapshotted into immutable canonical bytes or an equivalently deeply immutable representation.

**SealedEvidence retention decision:** for package schema v1.0.0, retain the complete canonical SealedEvidence manifest and rows inline. The current source has no independently retrievable immutable evidence store; excluding rows would make later digest recomputation impossible. Preserve the existing legacy Sealer digest algorithm and verify it from its exact canonical payload. RFC 8785 JCS package serialization remains a separate digest layer. This explicitly amends Gate 166's default raw-row exclusion for this implementation.

**Critical source correction required:** static reinspection found that Generator's current `world_spec` projection still includes `assignment_role` and `assignment_index`. Since both fields participate in the `world_id` hash, RUN and R assignments can receive different world IDs despite sharing the intended M/world seed. This contradicts Gate 154's fixed-world-within-M invariant and corrects Gate 167's earlier incomplete description. The versioned world-identity projection must exclude role/index while preserving those fields in run identity/manifests; deterministic regressions must prove shared world identity within M, distinct worlds across M and unique run IDs.

**Gate 168 status:** bundle/retention contract DEFINED and PERSISTED; world-identity source invariant BLOCKED pending correction; export implementation OPEN; tests NOT RUN. No code, tests, workflow or CI changes were made in this gate. No calibration, seed-bank generation, N/R/M sizing, Monte Carlo or scientific execution was authorized or performed. `main` remains unchanged; PR #116 remains Draft on its existing base.

**Next:** prepare and implement the minimal versioned world-identity correction with compatibility tests, then implement RunEvidenceBundle capture and export. Do not treat the Gate 155 historical PASS as proof that this newly identified identity invariant is satisfied by the current source.
## 28. Gate 169 — world identity invariance audit

Gate 169 is persisted in `00_GOVERNANCE/SIP/C10_S_VCONT_WORLD_IDENTITY_INVARIANCE_AUDIT_GATE_169_DRAFT_001.md`.

The Gate 168 source-level blocker is withdrawn: reinspection of the current `Generator.generate()` confirms that `assignment_role` and `assignment_index` are excluded from `world_spec` before `world_id` is computed. The current projection binds `world_seed`, `outer_replicate_id` and the remaining DGP-defining ScenarioConfig fields. The per-run identity separately binds the complete config, assignment role, world identity and assignment streams.

The existing RUN/R shared-world and cross-M separation test was strengthened to isolate role/index-only changes (same world ID, different run ID), DGP-parameter changes (different world ID), and different world seeds across M. The updated test source is persisted but has NOT been executed. No runtime PASS, CI result, independent-world guarantee from seed declarations alone, or Gate 159 provenance reconciliation is claimed.

**Disposition:** world-identity source contract STATICALLY CONSISTENT; regression STRENGTHENED / NOT EXECUTED; Gate 168 bundle contract remains DEFINED; RunEvidenceBundle implementation OPEN. No Generator source change, calibration, seed-bank generation, Monte Carlo, benchmark or scientific execution was performed. `main` remains unchanged and PR #116 remains Draft.

**Next:** Gate 170 — implement the Gate 168 capture boundary and deeply immutable RunEvidenceBundle snapshots, retaining full SealedEvidence rows and manifests.


## 29. Gate 170 — immutable RunEvidenceBundle capture implementation

Gate 170 is persisted in `00_GOVERNANCE/SIP/C10_S_VCONT_RUN_EVIDENCE_BUNDLE_CAPTURE_IMPLEMENTATION_GATE_170_DRAFT_001.md`.

The new module `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py` implements:

- canonical deeply immutable `FrozenSnapshot` payloads with type identity, SHA-256 and typed restoration;
- `RunEvidenceBundle.capture(...)` with exact SeedAssignment/ScenarioConfig/RunManifest joins, M/role/index checks, source run-ID joins, provenance digest recomputation, full SealedEvidence legacy digest recomputation, AnalysisContract/AnalyzerResult binding and exact EvaluationReport capture;
- a Gate 166 `MatrixTruthProjection` that retains matrix truth fields and explicit theta_A null/value without exporting potential-outcome arrays;
- `OuterWorldEvidenceBundle.capture(...)` enforcing one RUN, exactly R indices 0..R-1, shared world identity, common bank/design identity, unique run IDs and distinct Z/G assignment streams.

A regression source was added to the harness test module to verify source mutation after capture cannot mutate the bundle and that the truth projection excludes potential arrays. It has NOT been executed; no runtime PASS or CI evidence is claimed.

**Integration boundary:** the new API is not yet wired into the current benchmark producer/Monte Carlo path, which still consumes reduced tuples. No package writer, Gate 159 reconciliation, calibration manifest retrieval, trusted builder or attestor is implemented. Gate 170 is therefore IMPLEMENTED at the capture-primitive level; producer integration remains OPEN.

No Generator/Sealer/Analyzer/Evaluator scientific semantics were changed. No tests, CI, calibration, seed-bank generation, N/R/M sizing, Monte Carlo, benchmark or scientific execution was performed. `main` remains unchanged and PR #116 remains Draft.

**Next:** Gate 171 — integrate the capture API at the producer/orchestration boundary and construct one OuterWorldEvidenceBundle per M without reconstructing omitted source objects from aggregate outputs.


## 30. Gate 171 — M-level evidence producer/orchestration integration

Gate 171 adds `produce_and_capture_outer_world(...)` to `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`. The function consumes already-materialized evaluation-bank SeedAssignment rows; it does not derive or generate a seed bank. It accepts one structural ScenarioConfig template and exactly one RUN plus R repeated assignments for a single M.

The function applies the exact world/Z/G streams and assignment identity, calls the existing Generator → Sealer → Analyzer → Evaluator sequence, captures each RunEvidenceBundle before source objects are discarded, calculates one RepeatedAssignmentReport through the existing Evaluator method, and constructs one OuterWorldEvidenceBundle. It returns the unchanged legacy four-object tuples in RUN then R-index order, so existing MC aggregation interfaces and the 52-pair ledger semantics remain untouched.

Three regression tests were added: successful RUN+R capture, missing-R rejection and cross-M rejection. They have NOT been executed. The producer function itself was not called. No test PASS, CI, calibration, seed-bank generation, N/R/M sizing, Monte Carlo, benchmark or scientific execution is claimed.

**Boundary still open:** no benchmark-wide driver yet partitions all 13 scenario blocks and M groups, calls the producer for every M, and co-exports all OuterWorldEvidenceBundles with the existing 52-pair result. That is Gate 172. Gate 159 reconciliation, canonical JCS/tar packaging, trusted builder and attestation also remain OPEN.


## 31. Gate 172 — benchmark-wide evidence envelope implementation

Gate 172 adds `produce_and_capture_benchmark(...)` to `03_EXPERIMENTS/C10-S/harness/vcont_evidence_export.py`. It accepts the frozen `MonteCarloBenchmarkDesign`, exactly 13 matching structural `ScenarioConfig` templates and already-materialized evaluation-bank `SeedAssignment` rows. It validates 13×M×(1+R) assignment coverage, exact scenario/version/N/M/role/index joins, one RUN plus R repeated rows per M, shared world seed and unique Z/G assignment streams.

In deterministic scenario/M order, it calls the Gate 171 producer once per group, joins each legacy tuple to its exact RunEvidenceBundle snapshots, constructs the existing `scenario_outer_runs` input and calls the unchanged `evaluate_monte_carlo_benchmark()` exactly once. It returns the evaluator report and 13×M OuterWorldEvidenceBundles in one `CapturedBenchmark`, with an explicit scenario/M/world index.

The evaluator remains authoritative for the 52-pair ledger, report fingerprint, temporal manifest and aggregation calculations. Gate 172 does not change these semantics. Its positive complete-envelope test and two preflight rejection tests are persisted but NOT EXECUTED. The driver itself was NOT CALLED; no runtime PASS, CI, benchmark or scientific result is claimed.

The design's seed-bank/configuration fingerprints and executable commit are still only structurally/format-validated; Gate 172 does not independently recompute them from the effective assignment bank, configurations or running process. Gate 159 reconciliation, canonical JCS/tar package writer and trusted attestation remain OPEN.


### Gate 172 implementation qualification — report/evidence join

The Gate 172 driver compares the legacy TruthBundle against the deliberately bounded Gate 166 MatrixTruthProjection, not against omitted potential-outcome arrays. AnalyzerResult, AnalysisContract and RunManifest are restored and compared exactly. After the existing benchmark evaluator returns, the driver verifies one-to-one identity equality between captured RUN/R manifests and the temporal manifest; each of the 52×M pair contributions must join to the matching scenario/M world and designated RUN run_id. This remains source-level logic only and has NOT been executed.

## 32. Gate 173 — package readiness and canonicalization audit

Gate 173 statically confirms that the Gate 172 benchmark envelope contains the typed RUN/R source snapshots and M-level aggregate records needed to populate the Gate 164 `runs/run_records.json` payload. The exact Gate 164 path inventory can be retained; encode a versioned envelope in that existing file with 13×M×(1+R) run records, 13×M outer-world records, explicit evidence index and deterministic ordering. Keep the exact matrix used in the separate matrix package file.

Do not equate source snapshot digests with package JCS digests. FrozenSnapshot uses its tagged Python JSON serialization; SealedEvidence and report fingerprints retain legacy algorithms. A package adapter must losslessly restore the typed records, recompute the SealedEvidence digest from exact rows+manifest, and only then compute JCS file, manifest and archive digests as separate layers.

Gate 173 confirms that calibration assignments/manifest are not supplied to CapturedBenchmark; Gate 159 reconciliation and external GitHub-resolved producer/test metadata also remain absent. Therefore the source evidence envelope is available but package provenance cannot yet be RECONCILED. No package builder, verifier, tests, CI, calibration, seed-bank generation or benchmark was executed. See Gate 173.

## 33. Gate 174 — serialization and independent verifier contract

Gate 174 retains the exact Gate 164 v1.0.0 package inventory and freezes `runs/run_records.json` as a versioned envelope of RUN/R evidence records, one outer-world record per scenario/M, repeated aggregate report once per M, evidence index, cardinalities and join keys. Each FrozenSnapshot is transported as base64 of exact retained bytes with type ID, serialization ID and SHA-256. This snapshot integrity layer remains distinct from package JCS file/manifest/archive digests and from the legacy SealedEvidence/report fingerprints.

The current snapshot decoder does not restore enum types (it returns their underlying values), and the encoder rejects arbitrary bytes. A future versioned allowlisted decoder must reject unknown types/fields and prove exact restoration; no universal round-trip is assumed.

Gate 164 CONFIRMATORY v1.0.0 is fail-closed when calibration manifest, Gate 159 reconciliation, independent GitHub source/workflow resolution or required technical test evidence is missing. No placeholder or caller PASS is acceptable. Any diagnostic partial-transport format must use a distinct schema ID/version and cannot claim Gate 164 compliance or reconciled/authenticated provenance.

The independent verifier returns separate integrity, schema, completeness, reconciliation, source provenance, test and attestation statuses; producer validation flags are untrusted. Full contract: Gate 174. No serializer, package, tests, CI, calibration or scientific execution occurred. Next Gate 175 audits implementability against actual types and APIs.

## 34. Gate 175 — package serialization implementability audit

Gate 175 finds the RUN/R and M evidence source objects available in `CapturedBenchmark`, but the exact 52-row matrix is not retained: the producer validates and uses it locally, while the return object contains report, outer-world bundles and evidence index only. The report's design fingerprint and pair ledger do not reconstruct the exact matrix. The matrix must be retained as an immutable capture-time payload or bound companion.

The legacy `scenario_matrix_fingerprint()` omits `tolerance_id`; keep it unchanged for compatibility and add a full versioned matrix digest covering all declared fields. The generic snapshot decoder is not a strict independent decoder (enum values lose type identity, untagged dicts are accepted, exact field/version checks are absent); no enum-valued fields were identified in the current registered snapshot dataclasses, so that enum issue is latent for current records. Arbitrary bytes and non-string mapping keys remain unsupported.

The capture API receives only evaluation assignments. Actual calibration manifest, Gate 159 reconciliation and independent GitHub workflow/test evidence are absent from its return contract. Therefore Gate 164 confirmatory packager remains blocked. See Gate 175. No code, tests, calibration, seed generation, package or benchmark was executed.

## 35. Gate 176 — matrix capture and independent companion artifacts

Gate 176 defines the capture-time immutable MatrixCapture v1.0.0 for the exact 52 ScenarioEstimandSpec rows passed to the evaluator. It retains every declared field, including `tolerance_id`, in canonical order and adds a versioned full-matrix JCS SHA-256. The legacy matrix fingerprint remains unchanged.

The frozen CapturedBenchmark dataclass contains a mutable report dict; a separate immutable report snapshot/digest is required for package export. Calibration manifest, Gate 159 reconciliation, independent GitHub source-execution provenance and technical-test evidence are separate companion artifacts joined by benchmark_export_id. They cannot be inferred from the evaluation bank or declared design fingerprints. Missing companions block Gate 164 confirmatory acceptance. See Gate 176. No implementation or execution occurred.

## 36. Gate 177 — capture/export implementation-readiness audit

Gate 177 found that the producer retains the exact matrix tuple through validation and evaluator invocation, but the current validator does not enforce canonical SCENARIO_IDS × ESTIMAND_SPECS order. The legacy fingerprint sorts rows and omits `tolerance_id`; the new full digest requires strict row/value validation.

The report root is a mutable dict and cannot be passed to the current dataclass-only FrozenSnapshot.capture API. Its canonical serialization is Python JSON rather than RFC 8785 JCS. A separate typed FrozenReportSnapshot, pinned JCS implementation/version and strict decoder are required. Preserve existing CapturedBenchmark report/bundle/index shapes and use trailing optional new fields with fail-closed export validation.

Gate 176's two IDs require a non-circular content-derived rule; Gate 177 proposes `benchmark_export_id = capture_id`. Calibration and Gate 159 companion schemas still need exact row, cardinality, denominator and applicability rules. See Gate 177. No code/tests/execution occurred.

## 37. Gate 178 — capture/export serialization and companion schemas

Gate 178 freezes the exact MatrixCapture v1.0.0 row schema and SCENARIO_IDS × ESTIMAND_SPECS positional order; the versioned full-matrix JCS digest; FrozenReportSnapshot v1.0.0; deterministic non-circular `capture_id = benchmark_export_id`; CalibrationBankManifest v1.0.0; Gate159ReconciliationArtifact v1.0.0; SourceExecutionEvidence and TechnicalTestEvidence; strict decoder behavior; and the regression specification. The historical matrix/report/seed fingerprints remain distinct and unchanged.

The JCS Python implementation candidate is `rfc8785==0.1.4`, subject to later dependency pinning and independent conformance vectors. Gate 178 finds a Gate 164 v1.0.0 compatibility blocker: seed derivation yields uint64 integers, but ordinary JCS numeric representation cannot guarantee exactness above 2^53-1 and the frozen package contract disallows numeric-to-string coercion. A versioned exact uint64 wire representation must be approved before packager implementation. Gate 164 v1.0.0 is not silently modified.

Gate 178 is documentary only. No code, tests, CI, seed generation, calibration, package, benchmark or scientific execution occurred. Full contract: `C10_S_VCONT_CAPTURE_EXPORT_SERIALIZATION_AND_COMPANION_SCHEMAS_GATE_178_DRAFT_001.md`.

## 38. Gate 179 — uint64 package wire projection

The source seed derivation remains unchanged: `_derive_seed()` returns the unsigned integer represented by the first eight SHA-256 digest bytes. SeedAssignment continues to retain integer values; no seed is regenerated, transformed or relabelled by Gate 179.

For Gate 164 package v2.0.0 JCS payloads, each direct seed field is projected as the exact typed object `{"$type":"uint64","decimal":"<canonical unsigned decimal>"}`, range 0…18446744073709551615. The exact affected fields and five JSON paths are enumerated in Gate 179 §3. Historical seed-bank fingerprints are recomputed from the original typed SeedAssignment rows before projection. FrozenSnapshot canonical bytes remain opaque and byte-preserved.

Gate 164 v1.0.0 remains frozen; package v2.0.0 is the successor draft. No code, tests, seed generation, calibration, package, benchmark or scientific execution occurred. Full contract: `C10_S_VCONT_PACKAGE_UINT64_WIRE_FORMAT_DECISION_AND_V2_CROSSWALK_GATE_179_DRAFT_001.md`.

## 39. Gate 180 — source-schema audit of uint64 export coverage

Gate 180 confirms that the evaluator emits the three assignment stream seeds in each temporal-manifest row and emits `world_seed` again in each of the 52-pair ledger contributions. The pair ledger is duplicated at report root and within the legacy manifest payload. All these direct report JSON occurrences must use the Gate 179 typed uint64 representation and must be reconciled for equality before historical fingerprint recomputation.

The source ScenarioConfig also contains a base `seed` plus optional world/Z/G stream seeds. Their presence in the package's effective structural configuration projection has not been established. The exact projection must explicitly classify these fields before the v2 direct-seed registry can be considered complete. No seed algorithm or source SeedAssignment type is changed.

Gate 180 also confirms that MatrixCapture and FrozenReportSnapshot are not yet retained by CapturedBenchmark, and that calibration/Gate159/source/test companions are not producer outputs. See Gate 180. No code, tests, seed generation, calibration, package or scientific execution occurred.
