# C10-S — Static delta reconciliation: direct theta_A pipeline against Gates 129–131

**Date:** 2026-11-28  
**Status:** STATIC SOURCE REVIEW UPDATED AGAINST CURRENT CONTRACT SET / DIRECT theta_A PATH IMPLEMENTED IN RESEARCH BRANCH / MATERIAL ESTIMAND CONFORMANCE NOT ESTABLISHED / PREFLIGHT NOT AUTHORIZED / NO SCIENTIFIC EXECUTION  
**Branch reviewed:** `research/c10s-m1-engine12-source-only-20261127`  
**Historical governance branch:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Scope:** Compare the newer direct-`g_A` DGP/Analyzer/Evaluator path with the already completed Gate 129–133 historical work and the canonical methodological boundaries of Gates 130–131.  
**Method:** GitHub source/document inspection only. No imports, tests, validators, seed generation, workflow dispatch, simulation, calibration or estimation.

## 1. Executive finding

The current research branch contains a **genuine direct theta_A pipeline**, which is materially different from the older integrated ITT-Z/ITT-G Analyzer reviewed by Gates 129–133:

- it constructs explicit `g_A0/g_A1` joint policies by history;
- randomizes directly between those policies, not through Z or legacy G;
- seals realized interval-level S3 observations with assignment/policy/`q_X`/`r_common` provenance;
- estimates the direct history-standardized theta_A contrast in the Analyzer; and
- compares it with a separately reserved `theta_a_truth` in the Evaluator.

This is a real implementation advance over Gate 129's historical finding that the then-current Analyzer did not estimate theta_A and over Gates 132–135's historical `theta_a_truth=None` state.

**It does not, by source presence alone, close Gate 129/130 or validate S3.** The current DGP materializes a particular synthetic `q_X`, a particular direct policy pair and `r_common` certificates. Their correspondence to the accepted DEC-C10-103 target and the no-substitution constraints in Gate 130 has not been established by an accepted decision or an independent semantic audit. The interval S3 route is explicitly an ideal/perfect-complete benchmark path; imperfect-measurement correction remains open. The truth path uses strict EventHistory interval adjudication over complete deterministic histories and emits 1/0. Under the later Gate 206 rule this is conformant for the current DGP scope: functional UNKNOWN is not generated unless an intrinsic truth indeterminacy is explicitly stipulated and accepted. Observation missingness remains separate.

**Disposition:** the direct pipeline is IMPLEMENTED IN THIS RESEARCH BRANCH at source level; the intended estimand's semantic/materialization conformance remains PARTIAL/OPEN; the technical preflight must not be interpreted as closing those questions.

## 2. Historical work reused — no duplicate Gate 132

The following prior artifacts were recovered and reused:

| Historical artifact | Existing conclusion retained |
|---|---|
| Gate 129 — `C10_S_THETA_A_IDENTIFICATION_AND_ANALYZER_RECOVERY_AUDIT_GATE_129_DRAFT_001.md` | DEC-C10-103 selects theta_A, but the then-current integrated harness had no materialized `q_X*`, approved `g_A0/g_A1`, certified `r_common`, or direct theta_A Analyzer. |
| Gate 130 — `C10_S_QX_GA_RCOMMON_EXISTING_CONTRACT_RECONCILIATION_GATE_130_DRAFT_001.md` | Contracts already define the required forms; no operational policy pair or approved target roster/masses were selected/materialized. Equal fingerprints/labels are not sufficient evidence of invariant non-focal mechanisms. |
| Gate 130 corrigendum — `C10_S_GATE_130_G_ASSIGNMENT_AND_GA_SEMANTICS_CORRIGENDUM_DRAFT_001.md` | Legacy `ITT-G^{Z=0}` is not theta_A. G's vector intervention does not establish correspondence to accepted `g_A0/g_A1`, target `q_X*`, `r_common` and valid outcome measurement. |
| Gate 131 — `C10_S_VCONT_S3_MEASUREMENT_IDENTIFICATION_SUFFICIENCY_AUDIT_GATE_131_DRAFT_001.md` | S3 measurement model is not validated; point identification is currently restricted to perfect and complete measurement; error/missingness correction is open. |
| Gate 132 — `C10_S_VCONT_S3_OBSERVATION_TO_TRUTH_CROSSWALK_GATE_132_DRAFT_001.md` | Earlier integrated harness had an ideal S3 route and an adverse abstention route, but no validated error correction; interval-grid limits remained. |
| Gates 133–135 | Ideal baseline is retainable only as a bounded methodological benchmark; accepted V_cont semantics require tri-valued truth, strict continuity and UNKNOWN bounds; earlier harness did not fully conform. |

These artifacts are historical research-branch drafts, not silently promoted canonical main decisions. Their findings remain applicable wherever the newer source has not demonstrably superseded them.

## 3. Direct theta_A implementation — what is now materially different

### 3.1 Direct intervention and assignment

The current DGP creates per-history `JointPolicyHistory` entries for both policies and passes them to `materialize_c10s_complete_world_from_dgp()`. `generate_theta_a_policy_assignments()` explicitly randomizes the joint `g_A` policy and its vector, with its own assignment probabilities and salt; its source docstring expressly excludes Z and legacy G.

The Analyzer contract binds:
- target `q_X` masses and fingerprint;
- assignment bundle;
- `g_A0` and `g_A1` fingerprints;
- `r_common` fingerprint;
- history-specific assignment probabilities;
- optional structural support contract.

The Evaluator independently checks the reserved theta_A truth's estimand identity, `q_X`, `g_A0/g_A1` fingerprints, sealed evidence, actual direct assignment records, common-regime binding and EventHistory manifest. It does not derive theta_A by relabelling ITT-G.

**Finding:** the old Gate 130 G-versus-`g_A` conflation is avoided in the new source path. This is an implementation-level resolution of that specific distinction.

### 3.2 The remaining Gate 130 question: are these the accepted target and policies?

The current DGP's positive fixture declares:
- `q_x_mass_by_unit=(1/N,…,1/N)` in the synthetic world configuration;
- one generated baseline history per synthetic unit;
- `g_A0=(0,0,0,0)` and `g_A1=(1,0,0,0)` for each history;
- an assignment probability of 0.5 for `g_A1`;
- a feasible-vector roster containing those two vectors; and
- per-history `r_common` certificates whose fingerprints are set equal and whose status is `COMMON_FIXED`.

The alternative-path fixture holds its second coordinate at 1 in both arms while varying the first coordinate. These are explicit synthetic DGP stipulations, not estimates inferred from observed outcomes. The source therefore does more than the old harness.

However, Gate 130 specifically says that `q_X*` is not the number of units or a simulation frequency, that the candidate extreme policy pair was not approved, and that no substitute pair may be selected merely to obtain positivity. It also requires evidence that non-focal structural functions/versions are invariant; a shared fingerprint or `COMMON_FIXED` label alone is not that evidence.

The current source demonstrates internal consistency and fingerprints for its chosen fixture. It does **not yet demonstrate**:
1. that its synthetic unit/history roster is the accepted target population `P*_{τ2}` operationalization for DEC-C10-103, rather than a convenient calibration population;
2. that the chosen per-history `g_A0/g_A1` pair is the accepted/authorized intervention pair under the full-vector policy contract, rather than a new candidate;
3. that structural feasibility and Generator counterfactual evaluability are independently justified, rather than declared through the DGP's feasible-vector/support inputs; or
4. that `r_common` invariance is demonstrated across all non-focal structural mechanisms, not only represented by equal fingerprints and shared labels.

The support contract is useful: it distinguishes source/target support and assignment positivity, and the Analyzer can return `NOT_IDENTIFIED` for unsupported target histories. But a validator accepting declared booleans does not independently establish the scientific truth of those declarations.

**Disposition:** direct `q_X/g_A/r_common` objects are IMPLEMENTED in the synthetic DGP; their conformance to the accepted DEC-C10-103/Gate-130 semantic target remains OPEN. Do not silently call Gate 130 closed.

## 4. Gate 131 measurement boundary — the exact route exercised

The current DGP has two distinct measurement paths:

**A. Default interval path (`point_s3=False`)**
- Uses `IntervalMonitorConfig` with `coverage_mode="CONTINUOUS_EVENT_COVERAGE"` and `missing_probability=0.0`.
- Projects each realized EventHistory over the common interval grid.
- The Analyzer requires contiguous interval coverage and returns a point estimate only when target histories, both realized arms and every interval are observed.
- This is the **ideal, perfect-and-complete measurement benchmark** contemplated by Gate 131, not a validated model of real or imperfect passive S3.

**B. Point-sample path (`point_s3=True`)**
- Uses a separate point-sampled S3 configuration.
- The Analyzer explicitly returns partial identification / abstention because point samples do not reveal strict interval continuity.
- It does not fabricate a point estimate from point observations.

For the technical preflight workflow already prepared, `run_pipeline()` is called without `point_s3=True`; therefore it exercises path A, the ideal interval route. The workflow's one-fixture result can measure the computational cost of that route only.

The interval projector reads the generated EventHistory to construct an observed compliance signal, but emits only the interval observation and permitted identity/timing/provenance fields to the Sealer/Analyzer. This is a synthetic measurement mechanism, not independent validation of a passive production S3 source. The `missing_probability=0` fixture and `CONTINUOUS_EVENT_COVERAGE` declaration are ideal-path assumptions.

No calibrated sensitivity/specificity correction for interval S3 is implemented in this path. Missing interval records cause abstention/indeterminate output; they are not corrected into a point estimate. Thus Gate 131's measurement-validity and imperfect-S3 boundary remains open.

## 5. Temporal semantics delta since Gates 133–135

The newer direct path is stronger than the earlier slot-binary harness in one important respect:

- Generator creates versioned `EventHistory` objects with dated transitions.
- `adjudicate_intervals()` scans transitions inside each interval and applies strict continuity: a confirmed non-compliant state in any part of the interval makes that interval 0.
- The grid is common across histories and the interval S3 route is tied to the same support.

This is a material source-level advance toward the strict-continuity requirement identified in Gates 134–135.

Correction under the later accepted logical scope: `EventHistory.validate(require_complete=True)` and `adjudicate_intervals()` emitting 1/0 are consistent with Gate 206 for complete, deterministic histories. Gate 206 explicitly limits functional `?` to an intrinsic truth indeterminacy explicitly stipulated by the DGP; omissions, S3 missingness, timestamps, harness defects or observation limits must not create functional `?`. No such intrinsic-UNKNOWN scenario is currently approved in this path. Consequently, the absence of a functional-UNKNOWN fixture is **not** a present conformance defect. If a future DGP explicitly introduces intrinsic UNKNOWN, the corresponding V_cont bounds must be implemented under its own accepted specification. S3 missingness remains a separate observation state and must lead to analytical abstention/indeterminacy where identification is insufficient.

The fixture's two-interval grid is a software/DGP fixture choice, not a scientifically selected K, horizon or temporal resolution.

## 6. Conformance disposition

| Requirement | Source-level status | What this does not establish |
|---|---|---|
| Direct assignment to `g_A0/g_A1`, not G/ITT-G | IMPLEMENTED | That the selected policies are the accepted DEC-103 pair |
| History-standardized `q_X` target | IMPLEMENTED AS SYNTHETIC DGP INPUT | That equal unit masses represent the approved `P*_{τ2}` target |
| Per-history policy feasibility checks | IMPLEMENTED AS CONTRACT CHECKS | Independent semantic approval of the chosen policy support |
| Structural support and abstention | IMPLEMENTED | That declared support facts are externally/independently established |
| `r_common` identity/fingerprint checks | IMPLEMENTED | Invariance of all non-focal structural mechanisms |
| Independent reserved theta_A truth | IMPLEMENTED | Scientific validity of the DGP assumptions/policy pair |
| Independent Evaluator checks | IMPLEMENTED | Independent validation of source assumptions or external measurement validity |
| Strict interval continuity from EventHistory | IMPLEMENTED IN BINARY TRUTH | Functional UNKNOWN and corresponding truth bounds |
| Ideal complete interval S3 | IMPLEMENTED / GATE-131-COMPATIBLE BENCHMARK | Imperfect S3 validity or error correction |
| Point-sample abstention | IMPLEMENTED IN SOURCE | Calibration/validation of S3 missingness/error |
| Calibration protocol and metrics | IMPLEMENTED IN SOURCE | Empirical coverage, point recovery, MCSE or scientific conclusions (no calibration run) |

## 7. Decision and routing

1. **Do not recreate Gate 132 or its crosswalk.** Its historical work and Gate 133–135 temporal findings are reused.
2. **Do not describe Gate 129/130 as closed solely because the new code contains `theta_a_truth`, `q_X`, `g_A0/g_A1` and `r_common`.** The semantic identity of the target distribution, policy pair and common regime remains to be reconciled with the accepted DEC-C10-103 contract and Gate 130 constraints.
3. **The technical preflight, if later authorized, is valid only as an ideal interval-path runtime diagnostic.** It does not test imperfect S3, full V_cont truth semantics, or establish that the policy/population choices are scientifically admissible.
4. The minimum next design operation is a source-backed, decision-level reconciliation of the exact DGP fixture's `q_X`, `g_A0/g_A1`, feasibility/support and `r_common` against DEC-C10-103 and Gate 130. Reuse existing contracts; do not create another ledger, estimator, test family or measurement model.
5. Keep the tri-valued UNKNOWN/temporal-truth gap visible as a separate bounded limitation; do not expand this calibration workstream into a redesign of the complete V_cont measurement system.

No code, workflow, schema, DEC, test register, RMA, Evidence→Claim Matrix, STATUS or `main` was changed. No execution was performed or authorized by this review.

`scientific_execution=false`  
`execution_authorized=false`

## 8. Source identity register

### Canonical/historical governance sources
- `research/c10-s-consolidation-draft` — Gate 129 blob `601b03a08393a28e527930f11615a5b56bbf5b0e`.
- `research/c10-s-consolidation-draft` — Gate 130 q_X/g_A/r_common blob `bcf051ebd16dcb397ea2940d51b3db6204567f55`.
- `research/c10-s-consolidation-draft` — DEC-C10S-D2-ESTIMAND-SEPARATION-001 blob `f3556581d90a522d93805099380974b01f652287`.
- `main` — Gate 130 corrigendum blob `3c520d0d544ccbc4b91176aa244cf092b16c3d51`.
- `main` — Gate 131 S3 measurement audit blob `91b82ef71a081a46f3896693ed0783a787a088f2`.
- `research/c10-s-consolidation-draft` — Gate 132 blob `0236cc63ebad70d046dff9f5fc14fb3dd0a8b57b`.
- `research/c10-s-consolidation-draft` — Gate 133 blob `f396e20a9d08f4e0141e11d4d9ce870429bc7935`.
- `research/c10-s-consolidation-draft` — Gate 134 blob `4cd3f1beb8de0cb55e2d40ac0f344977f366f3de`.
- `research/c10-s-consolidation-draft` — Gate 135 blob `f029a0b90289085007f17e1124636ea8dd9c82bb`.

### Current direct-pipeline source blobs
- `theta_a_calibration_dgp.py`: `e334ee62502a9bb012512305075a8b071fd8efed`.
- `theta_a_analyzer.py`: `432841e301850d6caf35db1f7fb6c3174fb7f098`.
- `theta_a_evaluator.py`: `43c6715219114eaf1e0ac9eeb7e304939c7ae99b`.
- `theta_a_interval_observation.py`: `3d6ee9a46adcc59e3b23957aae993719228d3f69`.
- `theta_a_observation_harness.py`: `e75629ecc6aca4ca61bbddec8cffe1bfb72e3c85`.
- `c10s_synthetic_components.py`: `876c406e99ee855b25bbe0e0b1cb53eb35f7ef3d`.
- `c10s_world_pipeline.py`: `192086604283d38930de75284cb8aedbf85515a8`.
- `theta_a_calibration_protocol.py`: `5076df64cb2c9a486d1855600699bcc1a824210e`.

## 9. Mandatory update against the latest recovered C10-S contracts — 2026-11-28

This section supersedes any earlier interpretation in this review that did not incorporate the later logical B1/V_cont decisions. The current canonical governance state was reloaded from main: RMA v3.38, Evidence→Claim Matrix v1.47 and STATUS 2026-11-06. C09 remains PASS at bounded empirical causal-support level; C10 remains OPEN; no C10 value claim or execution authorization is created.

### 9.1 Later B1/V_cont contracts — what the current source does conform to

The historical C10-S consolidation branch contains later accepted logical scope decisions after Gate 131:
- Gate 154 accepts the bounded temporal scope of A_B1/V_cont: effective admission/non-admission required by ENABLED; PROFILE remains declared configuration/contractual obligation but has no independent temporal truth trajectory in the current DGP.
- Gates 151–152 preserve that separation and require EventHistory to represent functional transitions, not process events or PROFILE exposure.
- Gate 206 specifies the composition A_B1 → EventHistory → IntervalAdjudication → V_cont. Complete, deterministic histories yield 1/0; functional ? is allowed only for explicitly accepted intrinsic DGP indeterminacy, never for missing S3 or defects.
- Gate 208 R208-A1…A6 is recorded as accepted logical design scope, not implementation/design-freeze authorization. It keeps runtime mechanisms only when explicitly declared/versioned and causally determinative of admission; a single standardized opportunity remains a discrete probe, not a continuous monitor.

The current source implements FunctionalState.compliant as admission matching ENABLED, retains PROFILE as declarative configuration, validates complete EventHistory, and applies strict interval adjudication. This is materially aligned with the later Gate 154/206 scope. The previous report's characterization of the missing functional-UNKNOWN state as a defect is withdrawn. The path does not validate PROFILE exposure, and must not claim that it does.

Sources: Gate 154; Gates 151–152; Gate 206; Gate 208 R208-A acceptance and integrated B1 audit.

### 9.2 The later contracts do not close the direct theta_A estimand

The direct-g_A code is still not materially conformant to the accepted theta_A(q_X*, r_common; V_cont) target. The precise mismatches are:

1. **Target population / q_X*.** The DGP sets q_x_mass_by_unit=(1/N,…,1/N) in SyntheticWorldConfig. Gate 130 defines q_X* = Law(X,H0,C_c | i ∈ P*_τ2) and explicitly prohibits treating unit count, harness roster or simulation frequency as q_X* or inferring its masses from them. The target-history rows must be derived from an approved, versioned pre-Z eligible population and its baseline histories. Gate 80/130 report that the approved B1/UE roster and corresponding baseline snapshots are absent; no authorization to materialize them was present in that cycle.

2. **Policy pair.** The current positive/null/negative fixture uses g_A0=(0,0,0,0) and g_A1=(1,0,0,0); the alternative fixture uses (0,1,0,0) and (1,1,0,0). Gate 130 requires two explicit, versioned, jointly feasible interventions over the complete vector ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*), conditional on each target history. Even the previously proposed extreme pair (0,0,0,0) versus (1,1,1,1) was explicitly not ratified; Gate 130 prohibits selecting a substitute pair or kernel merely to create positivity. The current pair is therefore a DGP fixture choice, not an accepted operational intervention pair.

3. **Support.** The source declares feasibility through its own feasible_vectors_by_history fixture and builds support rows from the same synthetic histories. This checks internal contract consistency but does not independently establish that both policies are structurally feasible and counterfactually evaluable in the accepted target population. The three states remain separate: structural feasibility, Generator counterfactual evaluability, and Analyzer identification support.

4. **Common non-focal regime.** The DGP creates per-history RCommonPairCertificate rows by repeating the same fingerprint on both sides and labelling them COMMON_FIXED. Gate 130 explicitly says that equal fingerprints, labels or shared seeds do not prove invariance. It requires the non-focal structural functions and versions to be invariant under both potential interventions, or any differential path to be separately identified/unresolved. The source does not provide that independent invariance evidence.

5. **D2 and focal intervention are not reconciled.** The same fixture contains a D2 mechanism with programmed_probability_by_z=(0,1) and a D2 functional rule that changes admission when w_programmed=True, alongside a separately randomized direct-g_A policy. This is not automatically wrong as a synthetic world, but it means the non-focal D2 path must be shown to be held under the same r_common for the two g_A potential outcomes. A duplicated r_common digest does not demonstrate that. The current master C10-S Draft 004 and Gate 208 routing require D2, population, isolation, support and estimands to be reconciled together.

6. **Full ΔT_acc* versus focal projection.** C10-S Draft 004 §§32.1–32.3, consistent with DEC-C10S-D2-ESTIMAND-SEPARATION-001, distinguishes full ΔT_acc* from focal A_f*. A focal τ2 contrast must remain labelled θ_Af(q_X*) until its relation to the general θ_A(q) is justified. The direct DGP's first-coordinate intervention cannot be presented as a general test of all ΔT_acc* contributions.

### 9.3 Correct scientific disposition

- The direct Analyzer/Evaluator is a real software implementation advance over the historical integrated ITT-G Analyzer.
- The ideal interval S3 path is a legitimate best-case software benchmark within Gate 131's boundary.
- The EventHistory/strict-admission path is materially aligned with later Gate 154/206/208 logical scope; no extra UNKNOWN implementation should be invented now.
- **The present fixture is not yet a valid calibration instance for the accepted focal estimand.** Its q_X masses, policy pair and r_common invariance are not established under the governing contracts, and the D2-to-focal mapping remains unresolved.
- The technical preflight workflow, if run, would measure only the cost of this currently instantiated software path. It would not resolve the scientific mismatches and should not be used to authorize or tune scientific calibration.

### 9.4 Minimum next operation — one integrated design closure, not another instrumentation gate

Do not create another Analyzer, S3 model, test family, ledger or gate sequence. Reuse Gate 130, DEC-C10-103, DEC-C10S-D2-ESTIMAND-SEPARATION-001, the AB residual ledger, C10-S Draft 004 §§30–32 and Gate 208.

The single remaining design operation is to reconcile, as one connected decision package:
1. the approved pre-Z target population/UE roster and baseline-history basis for P*_τ2 and q_X*;
2. the exact versioned joint g_A0/g_A1 pair over the complete ΔT_acc* vector, with history-specific structural feasibility and Generator evaluability;
3. the non-focal regime r_common, including D2 policy/provisioning and all non-focal structural functions, with evidence of invariance rather than matching labels;
4. the distinction between the D2 assignment ITT/package effect, focal θ_Af(q_X*), and the general θ_A(q);
5. the V_cont measurement boundary: ideal perfect/complete interval S3 only for a best-case benchmark; imperfect S3 remains unvalidated and must not yield point identification.

This package must first establish whether the direct-g_A calibration is scientifically admissible as the intended estimand or only a software-method benchmark. It must not choose arbitrary policy vectors or infer q_X* from N. If the required population/policy decisions cannot be justified from existing accepted contracts, they must be presented together for explicit user decision before materialization or implementation.

**No tests, fixture generation, seed generation, workflow dispatch, calibration or scientific execution were performed.** No code or canonical main artifact was modified. scientific_execution=false, execution_authorized=false, and implementation_authorized=false remain in force.