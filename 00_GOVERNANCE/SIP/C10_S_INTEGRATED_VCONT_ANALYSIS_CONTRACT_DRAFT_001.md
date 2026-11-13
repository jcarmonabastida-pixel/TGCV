# C10-S Integrated V_cont Analysis Contract — DRAFT 001

**ID:** C10S-VCONT-ANALYSIS-CONTRACT-001  
**Date:** 2026-11-13  
**Status:** CONTRACT CLOSED FOR IMPLEMENTATION IN RESEARCH BRANCH / DRAFT / NOT DESIGN-FROZEN  
**Branch:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Scope:** integrated synthetic V_cont benchmark: assignment estimands ITT-Z and ITT-G, their truth/provenance correspondence, identification/abstention, and evaluator acceptance.  
**Does not authorize:** code changes, test execution, CI execution, Monte Carlo benchmark, scientific execution, C10-S global Design Freeze, or promotion to `main`.

---

## 1. Purpose and precedence

This contract consolidates the decisions required to implement the existing integrated V_cont harness without reopening its scientific architecture.

It applies to:
- `03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py`;
- `03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py`;
- the contracts and run artifacts directly consumed by those components.

It does **not** redefine C1 for the full D2 experimental programme. The D2 C1 documents concern assignment to material policies and retain open population, unit/interference, outcome/value and horizon decisions. The present harness is a separate synthetic benchmark with:
- `Z`: randomized package assignment;
- `G`: randomized synthetic intervention on the full focal accessibility-change vector (g_A);
- `V_cont`: the synthetic outcome used by this benchmark.

Consequently, `ITT_Z` here is not to be relabelled as the complete D2 C1 estimand, and `ITT_G` is not `theta_A`. The harness may test whether an analyzer recovers known assignment contrasts; it does not establish the real-world causal contribution of `ΔT_acc*` to Value.

Precedence within this scope:
1. this contract for the integrated V_cont harness;
2. accepted estimand-separation decision `DEC-C10S-D2-ESTIMAND-SEPARATION-001`;
3. the existing harness implementation and tests, only where consistent with this contract.

The broader plan `C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_004.md` remains governing for C10-S global closure and is not superseded.

## 2. Contractual estimands

Let (i=1,ldots,N) index the fixed synthetic units. Let (Y_i(z,g)) denote the unit's potential `V_cont` outcome under package assignment (z) and synthetic focal intervention (g), with the current harness's common-exogenous construction and no-interference restriction where applicable.

### 2.1 Primary benchmark target: marginal ITT-Z under reference G policy

The primary target is the finite-population marginal assignment effect under the declared reference distribution (q_i(g)):

[
	au_Z(q)=rac{1}{N}sum_{i=1}^{N}sum_{gin{0,1}}q_i(g)
\{Y_i(1,g)-Y_i(0,g)\}.
]

For the ordinary benchmark regime:
[
q_i(1)=q_i(0)=0.5 quad orall i.
]

The reference regime is part of the estimand identity, not an implicit default. It must be explicitly versioned in the analysis contract and linked to the run's assignment mechanism.

### 2.2 Run-conditional ITT-Z under the realized G vector

For a particular run with realized assignments (mathbf G=(G_1,ldots,G_N)), define:

[
	au_Z(\mathbf G)=rac{1}{N}sum_i
\{Y_i(1,G_i)-Y_i(0,G_i)\}.
]

With complete randomized Z assignment independent of G, the difference in observed mean outcomes between Z arms is the randomization estimator for this run-conditional target (under consistency, complete outcome observation and no interference).

It is **not** in general equal to (	au_Z(q)) in a single run. Under the declared G assignment mechanism:

[
E_{\mathcal D_G}[\tau_Z(\mathbf G)]=\tau_Z(q),
]

where (q_i(g)=P(G_i=g\mid X_i,\mathcal D_G)) is the actual unit/stratum-specific assignment probability induced by that mechanism.

Therefore:
- the per-run Analyzer estimate is interpreted against (	au_Z(\mathbf G));
- the primary marginal target (	au_Z(q)) is evaluated across repeated G assignments over the same fixed synthetic world;
- a single run must not be declared to have recovered the marginal target merely because its estimate is numerically close to it.

### 2.3 ITT-G under Z=0

The second assignment estimand is:

[
	au_G^{Z=0}=rac{1}{N}sum_i
\{Y_i(0,1)-Y_i(0,0)\}.
]

It is a population-wide total effect of assignment to G within Z=0. It is not the isolated effect of accessibility unless the intervention and exclusion conditions separately justify that interpretation. It is not `theta_A`.

Common support for G=0 and G=1 is required to identify this population-wide contrast nonparametrically under the current analysis contract. If support fails in any target stratum, the Analyzer abstains for this estimand; it must not silently replace the target population with the supported subset.

### 2.4 theta_A remains separate and unmaterialized

`theta_a_truth` remains `None`. No Analyzer output, ITT-G contrast, first-stage contrast or evaluator field may be relabelled as `theta_A`. A future `theta_A` contract requires the approved joint intervention policies, target distribution and independent identification/measurement specification.

## 3. Assignment mechanisms and target regimes

### 3.1 Z assignment

The current benchmark requires randomized, balanced Z assignment at the unit level, generated independently of G assignment. The run record must identify:
- assignment mechanism ID and version;
- assignment unit and allocation level;
- allocation rule and target ratio;
- randomization algorithm and seed/provenance;
- any strata, blocks or clusters;
- realized assignment vector hash.

A boolean `randomized_z` alone is not a complete provenance record.

### 3.2 G assignment

The current benchmark requires a separately randomized G assignment mechanism. The run record must identify:
- `g_assignment_mechanism_id`;
- `g_assignment_mechanism_version`;
- `g_assignment_mechanism_parameters`;
- `g_assignment_mechanism_hash`;
- assignment unit, strata and allocation rule;
- conditional probabilities (q_i(g)), or a deterministic/versioned rule from which they are reproducibly derived;
- randomization algorithm, seed/provenance and realized assignment vector hash.

For the ordinary regime, the current implementation uses a balanced binary assignment vector generated independently of Z. Its per-unit marginal assignment probability is 0.5; it is not an assertion of independent Bernoulli draws.

For `R0_SUPPORT_FAILURE`, the current implementation first creates a balanced G vector and then forces G=0 for units with baseline stratum HIGH. Its induced marginal probabilities are:
[
q_i(1)=
\begin{cases}
0.5 & X_i\text{ in LOW},\\
0 & X_i\text{ in HIGH}.
\end{cases}
]
The contract must represent this actual mechanism, not merely a `positivity=False` flag.

### 3.3 No implicit regime substitution

The following are distinct and must not be conflated:
- reference target regime (q^{ref}), e.g. 50/50 for every unit;
- actual run assignment mechanism (q^{run});
- realized assignment vector (mathbf G);
- run-conditional truth (	au_Z(mathbf G));
- marginal mechanism truth (	au_Z(q^{run}));
- reference target truth (	au_Z(q^{ref})).

The Evaluator must reject a comparison if the result and TruthBundle do not declare the same estimand identity/version and the same target regime identity/version. It must not compare a run-conditional estimate to a marginal truth as if they were the same run-level target.

## 4. Identification and transportability for ITT-Z

### 4.1 Identification with common support

If Z is randomized independently of G and has positive assignment probability in the target units, the Z contrast identifies the run-conditional effect (	au_Z(mathbf G)), subject to:
- consistency and version consistency;
- no interference under the unit-level estimand;
- complete and valid outcome measurement;
- no post-assignment selection or denominator changes;
- correct assignment-unit and randomization records.

A marginal target under a randomized G mechanism is identified by the design in expectation over that G mechanism. Per-run estimation variability remains and is evaluated using repeated assignments, not by pretending each run equals the marginal expectation.

### 4.2 Structural G support failure

When G=1 is unavailable in a target stratum, the observed Z contrast in that stratum identifies the Z effect under G=0, not automatically the counterfactual Z effect under G=1.

To identify the 50/50 reference target in that unsupported stratum, the contract requires a declared and justified transportability restriction on the **total Z effect**:

[
Y_i(1,1)-Y_i(0,1)
=
Y_i(1,0)-Y_i(0,0).
]

The restriction must identify:
- a stable ID and version;
- outcome ID/version;
- target scope (units/strata);
- structural basis in the DGP specification;
- evidence status;
- explicit falsifiers and boundary conditions.

This is a sufficient invariance condition, not a claim that it is the only possible mathematical identification route. A weaker aggregate restriction may only be introduced through a separate, explicit contract with its own truth and falsification tests.

The absence of a direct Z path is not sufficient. The absence of a focal direct path is not sufficient. A zero observed estimate is not evidence of invariance. Invariance must cover the total effect of Z on the declared outcome, including all modeled pathways and interactions.

### 4.3 Adjudication states

The Analyzer returns one of:
- `IDENTIFIED`: the declared design and restrictions identify the specified estimand;
- `NOT_IDENTIFIED`: a required design/positivity condition fails and no accepted identifying restriction repairs it;
- `INDETERMINATE`: evidence, measurement, provenance or scope is insufficient to adjudicate.

`IDENTIFIED` does not mean the numeric estimate is correct or within tolerance. Estimation, recovery and abstention correctness are separate evaluator outcomes.

For a support-failure run:
- `ITT_G^{Z=0}` is `NOT_IDENTIFIED` under the population-wide target;
- ITT-Z reference 50/50 is `IDENTIFIED` only if transportability is declared, valid for the unsupported stratum and independently supported by the DGP specification;
- without that restriction, ITT-Z reference 50/50 is `NOT_IDENTIFIED` (or `INDETERMINATE` if the status/evidence of the restriction itself cannot be adjudicated).

### 4.4 R0_SUPPORT_FAILURE adjudication

The current R0 support-failure DGP has, by configuration, zero package direct effect, zero collateral effect, zero heterogeneity and no interference; its shared exogenous variables are reused across potential regimes. The contract-level expectation is that the total Z effect is invariant across G in this scenario.

That expectation must be established from the complete implemented potential-outcome construction and scenario configuration, not inferred by the Analyzer from the observed outcome. The Generator/TruthBundle may carry the DGP's transportability truth and scope for post-analysis evaluation; the Analyzer receives only the approved restriction declaration and observable evidence, never potential outcomes or TruthBundle.

Until the implementation and tests explicitly encode this declaration and its falsifiers, the existing `package_status=IDENTIFIED` in R0 support failure is a legacy behavior, not proof that transportability has been implemented.

## 5. Interference, measurement and version conditions

- Any nonzero interference mechanism invalidates the current unit-level no-interference estimand. The Analyzer abstains as `INDETERMINATE` until a cluster/exposure estimand and matching design are specified.
- Missingness or measurement error not corrected by an approved model/bounds contract leads to `INDETERMINATE`; no complete-case silent substitution.
- Version inconsistency leads to `INDETERMINATE` or contract rejection, according to whether the mismatch is an evidence gap or a hard identity mismatch.
- The current point-identification restriction (perfect, complete S3 measurement) remains unchanged until a validated correction or partial-identification method is specified.
- The present contract does not approve Welch standard errors as design-valid uncertainty estimates, nor confidence intervals, type-I error, power or calibration claims.

## 6. Truth, evidence and firewall

### 6.1 Generator outputs

The Generator creates:
1. `RunManifest`: run/scenario identity, version, assignment mechanisms, target regime, seed/provenance, assignment hashes and DGP version;
2. `TruthBundle`: potential outcomes and separately identified truths for (	au_Z(\mathbf G)), (	au_Z(q^{run})), (	au_Z(q^{ref})) where defined, and (	au_G^{Z=0}); transportability truth/status/scope; `theta_a_truth=None`;
3. `EvidenceCandidate`: only observed outcomes/measurements, baseline variables, assignment indicators and permitted observable metadata.

Truths must be calculated using the exact assignment probabilities and target regimes declared in the manifest. No implicit hard-coded 0.5 averaging when the actual or reference regime differs.

### 6.2 Sealer

The Sealer accepts only `EvidenceCandidate`. It:
- validates a closed allowlist of observable fields;
- rejects truth, potential outcomes, DGP parameters, generator-only metadata and unauthorized fields;
- binds evidence to run ID and schema/version;
- seals the manifest and rows with a deterministic hash.

The Sealer does not accept or inspect `TruthBundle` or the full `RunManifest`.

### 6.3 Analyzer

The Analyzer receives only:
- sealed observable evidence;
- the versioned `AnalysisContract`.

It must not receive:
- TruthBundle;
- potential outcomes;
- generator-only DGP parameters;
- hidden assignment probabilities unless explicitly declared as part of the analysis design contract available to the analyst;
- post-analysis evaluator metadata.

The Analyzer validates the evidence seal and the declared estimand/assignment/transportability contract before estimating. It records the target estimand ID/version and regime ID/version in its output seal.

### 6.4 Evaluator

The Evaluator receives TruthBundle, RunManifest, AnalyzerResult and AnalysisContract only after Analyzer completion. Before computing any error it validates:
- run ID;
- scenario and DGP version;
- estimand ID/version;
- target regime ID/version;
- assignment mechanism IDs/versions/hashes;
- outcome ID/version;
- transportability restriction ID/version/scope/status;
- evidence input hash and Analyzer output hash.

A mismatch is a contract failure, not an estimate error. The Evaluator separately scores:
- per-run recovery of (	au_Z(\mathbf G));
- repeated-assignment recovery of (	au_Z(q^{run})) and, where specified, (	au_Z(q^{ref}));
- ITT-G recovery when identified;
- correct non-recovery/abstention when not identified or indeterminate;
- falsifier detection and rejection of incompatible metadata.

## 7. Repeated-assignment validation

The primary validation of marginal ITT-Z recovery uses a fixed synthetic world and repeated randomized assignment vectors.

Required separation:
- world seed: fixes baseline units, exogenous variables and potential outcomes;
- Z assignment seed/stream: generates randomized Z vectors;
- G assignment seed/stream: generates randomized G vectors under the declared mechanism;
- replicate ID: identifies each assignment replicate.

For each replicate (r), retain:
- (hat	au_{Z,r});
- (	au_Z(mathbf G_r));
- the mechanism-level target (	au_Z(q^{run}));
- assignment mechanism identities and seeds/hashes.

Acceptance is not “every replicate equals the marginal truth.” It requires:
1. per-run estimates assessed against their matching run-conditional truths;
2. replicate-average estimates assessed against the marginal mechanism truth;
3. where the target is the reference 50/50 regime but actual support is incomplete, transportability validated for every unsupported target stratum;
4. repeated-run bias and dispersion reported descriptively until a design-valid inferential procedure is separately approved.

The current single-seed `Generator.generate()` does not implement this separation. It is an implementation requirement, not an existing capability.

## 8. Scenario roster and required adversarial contrast

Retain the existing twelve scenario IDs. Do not silently alter their DGP parameters or interpretation.

Add one adversarial candidate scenario:
`R2_SUPPORT_FAILURE_ZG_INTERACTION`.

It must:
- remove G=1 support in at least one target stratum;
- create a nonzero difference between the total Z effect under G=1 and G=0 in that unsupported stratum;
- preserve randomized Z independent of G;
- keep potential outcomes and interaction truth inaccessible to the Analyzer;
- carry no accepted transportability restriction for the affected scope;
- expect ITT-Z reference 50/50 `NOT_IDENTIFIED` and ITT-G population-wide `NOT_IDENTIFIED`.

The scenario must be generated from an explicit, finite DGP parameterization. It must not be implemented by injecting truth into evidence or by post hoc editing of observed outcomes.

## 9. Contract fields and component responsibilities

### 9.1 Required identities

The implementation must provide stable IDs/versions for:
- `estimand_id`, `estimand_version`;
- `outcome_id`, `outcome_version`;
- `g_reference_regime_id`, `g_reference_regime_version`;
- `g_assignment_mechanism_id`, `g_assignment_mechanism_version`, `g_assignment_mechanism_parameters`, `g_assignment_mechanism_hash`;
- Z assignment mechanism ID/version/hash;
- `z_effect_transportability_id`, `z_effect_transportability_version`, `z_effect_invariant_across_g`, `transportability_scope`, `transportability_outcome_id`, `transportability_basis`, `transportability_evidence_status`;
- `world_id`, `world_version`, `replicate_id`, and separate randomization stream identities.

### 9.2 Responsibilities

| Component | Contract responsibility |
|---|---|
| ScenarioConfig | Versioned DGP, target regime, assignment mechanisms, support and structural interaction/transportability declaration |
| Generator | Generate fixed-world potential outcomes, randomized assignments, exact truths and RunManifest |
| RunManifest | Preserve run/world/replicate identity, assignment mechanism and regime provenance, hashes |
| TruthBundle | Keep run-conditional, mechanism-marginal and reference-regime truths separate; preserve theta_A=None |
| EvidenceCandidate | Observable-only data and permitted assignment/baseline fields |
| Sealer | Closed allowlist, schema, run binding and integrity hash |
| AnalysisContract | Estimand, outcome, target regime, assignment assumptions, support and accepted transportability scope |
| Analyzer | Estimate and adjudicate without truth access; report status and abstention reasons |
| AnalyzerResult | Bind result to run, estimand, regime, mechanism and evidence hash |
| Evaluator | Reject mismatches first; then score matching truths, recovery and abstention separately |

The current single `AnalysisContract.estimand_id="ITT_D2_AND_THETA_A_VCONT"` is not sufficiently discriminating. Replace it with explicit estimand IDs or an explicit multi-estimand contract that declares each estimand separately. Do not imply theta_A is analyzed merely because it appears in a combined label.

## 10. Acceptance tests

The following tests are required. IDs are contractual labels; they are not claims that tests already exist or have passed.

| ID | Required assertion |
|---|---|
| AC-01 | Ordinary G mechanism declares q=0.5 per unit and correct mechanism hash |
| AC-02 | Support-failure mechanism declares q=0.5 LOW and q=0 HIGH; no implicit global 0.5 |
| AC-03 | Generator computes run-conditional, mechanism-marginal and reference-regime ITT-Z truths separately |
| AC-04 | Analyzer per-run ITT-Z output is evaluated against (	au_Z(\mathbf G)), not silently against marginal truth |
| AC-05 | Repeated G assignments on a fixed world recover (	au_Z(q^{run})) in expectation/replicate average |
| AC-06 | Reference 50/50 target under support failure is identified only with valid transportability in unsupported strata |
| AC-07 | R0 support-failure structural invariance is explicitly declared, scoped and checked against the complete DGP |
| AC-08 | Adversarial support failure plus Z×G interaction causes ITT-Z reference 50/50 abstention |
| AC-09 | ITT-G population-wide target abstains under G support failure; no LOW-only substitution |
| AC-10 | Analyzer firewall rejects TruthBundle/potential outcomes/hidden DGP truth |
| AC-11 | Evaluator rejects run, estimand, regime, assignment mechanism, outcome or transportability mismatch |
| AC-12 | Direct G path is not relabelled theta_A; theta_A remains unmaterialized |
| AC-13 | Interference, measurement adversity, missingness and version mismatch produce the specified abstention/rejection |
| AC-14 | Per-run recovery, marginal recovery, identification and abstention are reported as separate metrics |
| AC-15 | Fixed-world seed and Z/G assignment streams are independently reproducible |
| AC-16 | A zero observed effect or absence of direct Z path cannot itself satisfy transportability |

Existing tests may be retained where they meet these assertions. Their current PASS history remains historical evidence for the prior test set only; it does not imply these new acceptance tests exist or pass.

## 11. Implementation sequence

Implement as one coordinated change set in the research branch:

1. Add explicit estimand and regime identities; correct the multi-estimand label.
2. Separate fixed-world generation from Z/G assignment streams and add replicate identity.
3. Make Generator compute the three distinct ITT-Z truths and ITT-G truth under declared mechanisms.
4. Extend RunManifest with assignment mechanism, regime and provenance identities/hashes.
5. Extend AnalysisContract with explicit target, support, transportability declaration/scope and observable design assumptions.
6. Update Analyzer to distinguish run-conditional estimation from marginal-target identification and to abstain when required restrictions fail.
7. Update AnalyzerResult to seal estimand/regime/mechanism identity and separate status/estimate fields.
8. Update Evaluator to validate all correspondence before scoring and to evaluate repeated-assignment recovery.
9. Add the adversarial support-failure × Z×G interaction scenario.
10. Implement AC-01…AC-16 tests and reconcile the existing suite without weakening prior assertions.
11. Perform static review of the complete diff and test coverage before requesting a separate authorization for technical suite execution.

No partial merge of mismatched Generator/Analyzer/Evaluator contracts is acceptable.

## 12. Explicit non-goals and open boundaries

This contract does not:
- close C10-S globally or freeze D2 population `P*_{τ2}`;
- operationalize the full D2 C1 population, policy receipt, Outcome A or Value B;
- identify the real-world causal effect of accessibility on Value;
- implement or estimate `theta_A`;
- validate a real migration system;
- approve confidence intervals, p-values, type-I error, power or inferential calibration;
- establish absence of interference beyond the declared synthetic DGP;
- authorize any scientific or Monte Carlo execution;
- promote the research branch or PR #116 to `main`.

The D2 policy C1 and the integrated V_cont assignment benchmark remain distinct research objects. Results from this harness may support methodological benchmark claims about recovery under specified synthetic DGPs only.

## 13. Closure statement

The integrated V_cont analysis contract is **closed for coordinated implementation** at the specification level in the research branch. Its core decisions are fixed for this implementation:
- ITT-Z reference marginal regime is explicit (50/50 in the ordinary target);
- per-run realized-G target and marginal mechanism target are distinct;
- support failure requires scope-specific total-effect transportability to recover a different reference regime;
- ITT-G remains a population-wide assignment contrast and abstains without common support;
- theta_A remains separate and unmaterialized;
- Analyzer/TruthBundle firewall is mandatory;
- per-run and repeated-assignment recovery are separately evaluated;
- inferential calibration remains outside this implementation.

This closure is not a claim that the contract is implemented, tested, scientifically validated or accepted as a C10-S Design Freeze. Implementation, static audit and separately authorized technical execution remain pending.

**Execution flags:** `scientific_execution=false`; `execution_authorized=false`.

## 14. Implementation alignment record — 2026-11-13

The coordinated implementation pass has begun in the research branch. The following changes are present in the current harness and test source; they have **not** been executed.

### 14.1 Implemented in source (static presence only)

- ScenarioConfig now separates world, Z-assignment and G-assignment seeds and carries a replicate ID plus a finite zg_interaction_effect parameter.
- Generator uses independent random streams for the fixed synthetic world and the two assignment vectors.
- TruthBundle distinguishes run-conditional ITT-Z, mechanism-marginal ITT-Z and reference-regime ITT-Z; legacy itt_z_truth remains an alias for the 50/50 reference truth. theta_a_truth remains None.
- RunManifest records world/replicate identity, assignment mechanism IDs/versions/hashes, realized assignment-vector hashes, reference-regime identity and stratum-level G assignment probabilities.
- Analyzer reports run-conditional ITT-Z separately from reference-regime identification. Lack of G support does not by itself invalidate the run-conditional target; the 50/50 reference target is separately NOT_IDENTIFIED unless the total-Z-effect transportability declaration covers the unsupported HIGH stratum.
- Evaluator checks estimand, target-regime, outcome and assignment-mechanism hash correspondence before scoring. Run-level ITT-Z is compared with its matching run-conditional truth, not the marginal reference truth.
- The scenario roster now contains R2_SUPPORT_FAILURE_ZG_INTERACTION, with a structural G support failure and a nonzero Z×G interaction parameter.
- Existing and new tests cover separated truths, independent random streams, support/transportability adjudication, mechanism provenance, firewall rejection and evaluator mismatch rejection.

### 14.2 Test coverage status

The existing suite has been retained and nineteen additional tests have been added (35 test definitions in total). The coverage mapping is partial:
- Source-level assertions now cover AC-01…AC-16, including RunManifest scenario/world/vector mismatches, estimand and mechanism version mismatches, transportability scope/outcome checks, provenance injection, sparse realized-arm abstention, and explicit repeated-assignment marginal scoring.
- This is a static coverage mapping only. It does not establish that the tests pass or that all boundary combinations are exhaustively enumerated.

These are test definitions only. No test has been run in this implementation pass, so no PASS, CI success, benchmark recovery or scientific validation is claimed.

### 14.3 Remaining static work before execution authorization

1. Complete AC-11 mismatch coverage and AC-13 version-consistency coverage.
2. Audit the exact DGP-derived transportability declaration against every potential-outcome pathway and its scope.
3. Verify that repeated-assignment tests assess mechanism-level recovery without implying confirmatory inference.
4. Reconcile code/test schemas and this record against the current branch diff.
5. Preserve the execution gate: no test suite, CI, Monte Carlo benchmark or scientific execution until separately authorized.

State: source changes present; test definitions present; static review incomplete; execution not performed; scientific_execution=false; execution_authorized=false.

### 14.4 Gate 124 corrective alignment — 2026-11-13

The Gate 124 static audit identified a missing RunManifest handoff, incomplete estimand/mechanism version binding, absent aggregate marginal-recovery scoring, insufficient transportability-scope verification and an uncontrolled sparse-arm exception. The following corrective changes have now been persisted in the research branch:

1. **Evaluator / RunManifest:** Evaluator.evaluate now requires the RunManifest. It validates run, scenario, DGP version, world, replicate, reference regime, assignment mechanism IDs/versions/hashes and realized assignment-vector hashes before scoring.
2. **Evidence provenance:** EvidenceCandidate carries a restricted provenance envelope. Sealer enforces a closed key allowlist, verifies assignment-vector hashes against the observed assignment columns, and seals the provenance digest with the evidence. G stratum probabilities remain in RunManifest, outside the Analyzer-visible envelope; Evaluator validates them against the assignment mechanism hash. The envelope contains no TruthBundle, potential outcomes, hidden assignment probabilities or DGP truth.
3. **AnalyzerResult:** result output seal now includes estimand version, assignment mechanism IDs/versions, reference regime ID/version and evidence provenance digest.
4. **Transportability:** AnalysisContract requires a structural basis and matching outcome for a positive transportability declaration. Evaluator checks DGP truth status and scope against the declared scope and outcome.
5. **Repeated assignments:** Evaluator.evaluate_repeated_assignment now evaluates each run against its run-conditional truth and separately compares the replicate-average estimate with the mechanism-marginal truth, requiring a common fixed world and common mechanism truth.
6. **Sparse realized arms:** insufficient realized arm sizes return INDETERMINATE with explicit abstention reasons instead of raising an uncaught ContractError. First-stage summaries remain absent where the required observed arms are empty.
7. **Tests:** five additional tests have been added since the Gate 124 audit, bringing the suite to 35 test definitions (16 pre-existing + 19 added). They include manifest identity/vector mismatches, estimand/mechanism version mismatches, scope/outcome truth mismatch, provenance firewall and sparse-arm abstention. All AC-01…AC-16 have source-level test assertions.

**Important boundary:** these changes have not been executed. No test, CI, benchmark, Monte Carlo run or scientific execution has been started. Static source presence and contract alignment are not PASS evidence.

**Updated state:** Gate 124 corrective source changes persisted; static review of the final diff remains to be completed; test execution remains unauthorized (scientific_execution=false; execution_authorized=false).


### 14.5 Gate 125 — final static coverage correction — 2026-11-13

Following the 52/52 primary and clean-replay CI pass, the Gate 125 audit identified three remaining test-coverage gaps and one workflow omission. The following corrections are now persisted:

1. **AC-11 identity/version boundaries:** added evaluator rejection cases for transportability restriction ID/version, outcome ID, Z assignment mechanism version, reference-regime ID and scenario/DGP version.
2. **AC-13 version-consistency adjudication:** added an end-to-end Analyzer→Evaluator test requiring package, G-assignment and reference-regime statuses to be INDETERMINATE, expected abstention to be respected, and no false reference-regime mismatch.
3. **AC-15 independent reproducibility:** added a four-way seed test. Identical world/Z/G seeds reproduce both assignment vectors; changing only Z seed changes only Z; changing only G seed changes only G; potential V_cont and ΔT_acc truth remain invariant across assignment-seed changes.
4. **Workflow compilation:** explicit `py_compile` now includes `vcont_integrated_harness.py` and `test_vcont_integrated_harness.py` in addition to the pre-existing focal/P178 modules.

The integrated harness test module now contains 38 test definitions (35 prior + 3 added in Gate 125). These are source-level additions only until the next Actions run completes.

**Execution boundary:** this correction does not authorize or start Monte Carlo, benchmark or scientific execution. The next authorized technical check is the C10-S focal harness GitHub Actions workflow on this research-branch push. `main` remains unchanged; PR #116 remains Draft.
