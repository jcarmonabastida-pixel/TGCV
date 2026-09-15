# TGCV — Evidence-to-Claim Matrix — Current v1.9

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT  
**Date:** 2026-09-15  
**Predecessor:** v1.8  
**Incremental governance update:** v1.9 preserves the complete material evidentiary content and schema of v1.8; no evidence is deleted, collapsed, or downgraded. C10C-001 is propagated as material bounded empirical evidence to C02, C07, C08, C11 and C16. No claim-level status is upgraded by this propagation.

**Current update:** C10C-001 Egypt structural reconstruction. The controlled reconstruction establishes `S0`, `S1` and observed `ΔS` for the identified sample, but no independently defined accessibility predicate `Pτ` is identified; therefore `Uτ`, `T_acc,0`, `T_acc,1` and `ΔT_acc` are not reconstructible from the frozen evidence. This is a material non-software empirical boundary qualification, not positive accessibility or trajectory/value causal evidence. No claim-level status is upgraded.

## Matrix preservation rule
This matrix is cumulative. Every new version MUST preserve the full evidentiary content and schema of its predecessor and add, qualify, bound, supersede, or explicitly retire information. A version MUST NOT silently reduce the number of claim-matrix columns, remove material evidence descriptions, collapse evidence basis into summary-only fields, or replace detailed evidence records with a short status table.

`EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` is a stable alias of the complete versioned current matrix; it MUST NOT be a simplified derivative.

## Material evidence propagation rule
A material experimental result is propagated to this matrix when it adds, removes, qualifies, bounds, or otherwise changes the evidentiary basis or interpretation of a claim, even when no claim status/level changes. Claim upgrade is a separate decision and is never inferred merely from evidence propagation.

**Operational rule:** Evidence propagation does not imply claim upgrade. A claim-level upgrade requires an explicit claim-level consolidation record.

## Current claim matrix

| ID | Claim | Status | Current evidence / basis | Evidence impact / interpretation | Next requirement |
|---|---|---|---|---|---|
| C01 | TGCV represents system state/context/conditions and constraints/resources | E0 | Formal architecture + bounded cross-domain traces + IT-G1 bounded industrial case | IT-G1 adds material bounded evidence for reconstruction of internal state and external enabling conditions; no claim-level upgrade. | Further independent operational confirmation |
| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Formalization + Rust + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 + IT-G1 + C10C-002 + C10C-001 | SWIM provides bounded accessibility operationalization; IT-G1 adds bounded evidence that end-to-end accessibility/function can depend on conditions external to the internal remediation target; C10C-002 adds an independent real-world bounded reconstruction of `T_acc*` from six structural infrastructure dimensions using pre-outcome structural predicates across 342 polygons and two observed rounds. C10C-001 independently demonstrates in a distinct non-software case that structural state reconstruction and observed configuration changes do not identify `Pτ`/`T_acc` without an explicit admissibility predicate. General `T_acc` remains unclosed and no claim-level upgrade is implied. | Independent operationalization across a distinct exemplar |
| C03 | T_acc is analytically distinct from downstream Reach in bounded Rust | E1 | Rust evidence | SWIM does not alter the bounded Rust claim level; IT-G1 does not test the Rust-specific Reach separation; C10C-002 does not operationalize downstream Reach identity. | Independent replication |
| C04 | ΔT_acc can occur without ΔReach¹_pot | E1 | Rust ND-1 | No direct test by SWIM, IT-G1 or C10C-002. | Independent replication |
| C05 | ΔT_acc can occur with ΔReach¹_pot change | E1 | Rust ND-2 | No direct test by SWIM, IT-G1 or C10C-002. | Independent replication |
| C06 | Reach identity is not characterized by cardinality alone | E1 | Rust ND-4 | No material impact; C10C-002 uses a scalar net cardinality outcome only for its frozen bounded causal test and does not establish Reach identity. | Independent replication |
| C07 | Accessible transformation spaces change over time in Rust | E1 | Rust non-persistent pairs + bounded SWIM operationalization + C10C-002 + C10C-001 | SWIM provides bounded non-Rust evidence that accessible transformation spaces can change across observed state transitions; IT-G1 adds a bounded industrial state-transformation sequence; C10C-002 adds independent real-world longitudinal evidence from 342 polygons in which a bounded universe of 12 elementary structural transformations yields non-empty `ΔT_acc*` in 238 polygons, including 104 openings and 171 closures. C10C-001 adds a distinct non-software boundary case in which observed structural changes are reconstructible but `T_acc` and `ΔT_acc` are not identified; it therefore qualifies the distinction between observed structural change and accessible transformation-space change and is not evidence of `ΔT_acc`. This does not upgrade the Rust-specific claim level. | Independent closed operationalization / replication |
| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded Rust H=1 + SWIM trajectory-linkage reconstruction + IT-G1 bounded state/trajectory observation + C10C-001 | SWIM adds bounded reconstructability of ordered subsequent transformations and state transitions; IT-G1 provides a bounded industrial state/trajectory observation. KGFS supplies the causal layer now reflected in C09. C10C-002 does not add a trajectory outcome and therefore does not establish modification of reachable future trajectories. C10C-001 adds a material empirical boundary qualification: structural change and realized transformation cannot substitute for reachable-trajectory evidence because accessibility was not identified and no trajectory causal estimand was estimated. No claim-level upgrade is implied. | Independent valid trajectory test with explicit trajectory criterion beyond bounded exemplars |
| C09 | Accessibility changes causally affect subsequent trajectories | **PASS — BOUNDED EMPIRICAL CAUSAL SUPPORT** | SWIM trajectory-linkage reconstruction + RUST-DYN-2 bounded structural evidence + KGFS randomized structural accessibility intervention with D5-A identified contribution + KGFS exact 74/74 trajectory-variable reproducibility audit + C09 Bundle 003 Executor-2 reconstruction + FOS methodological/reference evidence | Claim-level consolidation establishes bounded empirical causal support. KGFS provides the decisive real-world causal layer: randomized early expansion of KGFS banking infrastructure, reconstructable structural accessibility change, D5.2-S applicability, D5-A identified contribution, and reproducible longitudinal trajectory variables. SWIM and RUST-DYN-2 provide complementary bounded structural/trajectory-linkage support. Bundle 003 remains synthetic causal-operationalization evidence and FOS remains non-reportable under its frozen estimator. C10C-002 is deliberately excluded from positive C09 support because its estimand tests the intervention effect on `ΔT_acc*`, not the effect of `ΔT_acc*` on subsequent trajectories. | Independent real-world replication across a distinct domain; broader generality; no automatic value claim |
| C10 | Accessibility changes generate/predict value | H | No Value evidence | SWIM, RUST-DYN-2, KGFS, IT-G1 and C10C-002 do not establish causal `ΔT_acc → ΔV` or predictive value. C10C-002 explicitly did not execute a value regression and its value endpoint was kept outside `Pτ` and the bounded causal outcome. No value claim is established. | Value-linked test |
| C11 | TGCV is domain-independent / transversal | H | C-01 A-C + I-01 Gate C + bounded cross-domain evidence + C10C-002 + C10C-001 | SWIM is a bounded self-adaptive software exemplar, IT-G1 a bounded industrial AWS exemplar, KGFS a bounded real-world rural-finance intervention, and C10C-002 a bounded urban-infrastructure/real-estate empirical case. C10C-001 adds a distinct non-software empirical reconstruction boundary, showing that structural state/change can be recovered while accessibility remains unidentified unless an explicit admissibility predicate is available. This strengthens the documented heterogeneity and boundary evidence only; it does not establish transversal validity or justify a claim upgrade. | Independent operationalization across broader domains |
| C12 | TGCV provides superior explanatory representation | H | Comparative evidence absent | IUT M1 provides bounded decision-performance evidence but U2-NULL; SWIM, IT-G1, KGFS and C10C-002 are non-comparative for explanatory superiority. | Controlled differentiated comparison |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21 | No material impact. | Comparative coverage |
| C14 | T_acc is an ontological primitive independent of S | F | TR-131 | No impact; SWIM, IT-G1, KGFS, C09 Bundle 003 and C10C-002 treat accessibility as derived/conditioned rather than restoring the rejected primitive. | No restoration without contrary evidence |
| C15 | Rust demonstrates observed Cargo/runtime reachability | F | Rust evidence boundary | No impact. | Separate governed runtime test |
| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22/23 + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 + SWIM trajectory-linkage reconstruction + IT-G1 + C09 Bundle 003 + C10C-002 + C10C-001 | SWIM supports bounded state/context → accessibility → `T_acc` → `ΔT_acc` and bounded trajectory linkage. IT-G1 adds bounded industrial evidence preserving distinctions among internal state transformation, external enabling condition and end-to-end outcome. C09 Bundle 003 adds bounded executable causal-operationalization evidence while preserving the distinction between intervention/accessibility and downstream outcome. C10C-002 adds a reproducible real-world bounded chain `Z → ΔS → T_acc* → ΔT_acc* → frozen causal estimand`, with structural-only predicates, explicit treatment/state separation, endpoint separation, and a negative result retained without post-hoc rescue. C10C-001 adds a complementary non-software boundary case preserving the distinction among structural state, candidate transformations, accessibility and realized transformations, while explicitly preventing temporal leakage. It does not close downstream value boundaries or establish transversal validity. | Closed independent-domain operationalization / downstream test |

## Material empirical evidence — C10C-001 Structural Reconstruction

**Case:** `C10C-001 — Egypt`  
**Status:** `PARTIAL — STRUCTURAL STATE RECONSTRUCTIBLE, ACCESSIBILITY PREDICATE NOT IDENTIFIED`  
**Result artifact:** `00_GOVERNANCE/SIP/TGCV_C10C001_STRUCTURAL_RECONSTRUCTION_RESULT_001.md`  
**Protocol:** `00_GOVERNANCE/SIP/TGCV_C10C001_STRUCTURAL_RECONSTRUCTION_PROTOCOL_001.md`  
**Source freeze:** `00_GOVERNANCE/SIP/TGCV_C10C001_SOURCE_VERSION_FREEZE_001.md`  
**Propagation record:** `00_GOVERNANCE/SIP/TGCV_C10C001_EVIDENCE_TO_CLAIM_PROPAGATION_001.md`

The controlled reconstruction was conducted on the frozen C10C-001 Egypt source. The baseline and identified longitudinal subset permit reconstruction of structural state and observed state changes, but the source does not expose an independently defined accessibility predicate `Pτ(S,C,τ)`. The audited variables identified as treatment/assignment, realized take-up/adoption, observed configuration identity, orders/production, or implementation detail cannot be promoted to an accessibility predicate without an additional admissibility rule.

The reconstruction therefore establishes a bounded non-software empirical boundary: `S0`, `S1` and observed `ΔS` are reconstructible for the identified sample, while `Uτ` cannot be defined as a cross-temporal union, `Pτ` is not identified, and consequently `T_acc,0`, `T_acc,1` and `ΔT_acc` are not reconstructible from the frozen evidence. Observed realization is not treated as accessibility; treatment assignment is not treated as availability; take-up/adoption is not treated as availability; observed configuration identity is not treated as the accessible transformation universe; and later-observed configurations are not used to define earlier accessibility because of temporal leakage.

This is material empirical evidence because it independently qualifies the boundary between structural-state reconstruction and accessibility-space reconstruction in a non-software domain. It does **not** establish positive evidence of `ΔT_acc`, a trajectory effect, a value pathway, causal effect on subsequent trajectories, transversal validity, or a Core modification. No claim-level upgrade follows from this propagation.

### Evidence-to-claim propagation

- **C02:** Material qualification. Structural reconstruction and observed configuration changes do not identify `Pτ`/`T_acc`; an explicit admissibility predicate remains required. No upgrade.
- **C07:** Bounded negative/limiting qualification. The case does not identify `ΔT_acc`; observed structural changes are not substituted for accessible transformation-space changes. No upgrade.
- **C08:** Material boundary qualification. Structural change/realized transformation cannot substitute for reachable trajectory evidence, and no trajectory causal estimand is established. No upgrade.
- **C11:** Material methodological qualification. The case is a distinct non-software empirical reconstruction boundary, strengthening the documented cross-domain evidence base only by showing where accessibility reconstruction fails. No transversal-validity upgrade.
- **C16:** Material methodological evidence. The case reinforces preservation of the distinctions among state, candidate transformations, accessibility, realized transformations and temporal leakage controls. No upgrade.

No positive propagation is made to C01, C03, C04, C05, C06, C09, C10, C12, C13, C14 or C15. The Core/RMA status is unchanged.

## Material methodological evidence — IUT-A-01 U2 FULL_PILOT 001

**Case:** `IUT-A-01`  
**Status:** `CLOSED — U2-NULL`  
**Evidence artifact:** `03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_FULL_PILOT_RESULT_001.json`  
**Closure audit:** `03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_FULL_PILOT_CLOSURE_AUDIT_001.md`

The frozen FULL_PILOT completed with execution integrity `PASS`. M1 decision correctness was `60.0%` control versus `100.0%` TGCV, a `+40.0` percentage-point difference, with the predeclared M1 gate passing. M2 used the declared single-invocation microbenchmark and failed its predeclared improvement threshold: control median `0.00155 ms`, TGCV median `0.00485 ms`. The overall classification is `U2-NULL`.

This is material comparative methodological evidence bounded to Fixture 002 and the executed criteria. It does not upgrade C12 or any other claim.

## Material methodological evidence — IT-NOSD-010

**Case:** `IT-NOSD-010 — ETSI TS 23.502 / 3GPP 5GS`  
**Status:** `IT-G0 CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`; `IT-G1 CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`; `IT-G2 CLOSED — BOUNDED DOWNSTREAM-SEPARATION PASS`.

The independent G1 and G2 executions reproduced the frozen event, provenance, bounded pre-state, transformation identity, temporal boundary and downstream separation. Accessibility was not reused as outcome evidence, outcome was not used to define post-state, and complete ex-ante enumeration of `T_acc(S_t)` was not required under TR-132-MOD-1.

This is material bounded methodological evidence for reconstruction and separation of accessibility from downstream evidence in one frozen 5G event. It does not establish complete `T_acc`, normative 3GPP admissibility, utility, causal effect, value effect, comparative superiority, transversal validity or scientific validation.

## Material methodological evidence — EXT-UPD-4.8 O3 accessibility closure reassessment

**Case:** `IUT-A-01`  
**Option:** `O3`  
**Status:** `CLOSED — INDETERMINATE / H-B — HS-AC01`  
**Execution artifact:** `03_EXPERIMENTS/IUT-A-01/IUT_A01_O3_ACCESSIBILITY_CLOSURE_RESULT_001.json`  
**Governance closure:** `00_GOVERNANCE/D-OPS-24_EXT-UPD-4.8_STAGE_B_ACCESSIBILITY_CLOSURE_REASSESSMENT_EXECUTION_RESULT_v0.1.md`

The bounded corrective assessment executed with integrity `PASS`. RF-AC01 through RF-AC04 all passed. O3 was confirmed as a native candidate alternative from frozen Stage-A evidence, but two material decision-time conditions remained unresolved: availability/accessibility of alternative tooling T-C and ability to perform the required additional setup within the decision-time boundary. The available rule that partial setup plus an explicit alternative-tool requirement implies accessibility was classified as `ANALYST-INTERPRETATION`, so the hard stop `HS-AC01` was correctly triggered.

The result is `INDETERMINATE / H-B`: a bounded deeper operationalization boundary persists. It is material methodological evidence because it qualifies the evidence boundary for accessibility closure. It does not establish complete `T_acc`, industrial utility, superiority, causality, value, transversal validity or any Core modification. No additional constructive attempt or comparative IUT is authorized by this closure.

## Material methodological evidence — Class-II AWS-PatchAsgInstance

**Fixture:** `IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE`  
**Phase-A status:** `CLOSED — PREDECISION RECONSTRUCTION REPRODUCIBILITY PASS`  
**B0 accessibility preflight:** `CLOSED — NO ADMISSIBLE RESOLVED ACCESSIBILITY DIFFERENCE IDENTIFIED`  
**B0 permissions audit:** `CLOSED — PARTIAL / EFFECTIVE CANDIDATE PERMISSION UNRESOLVED`

The primary Phase-A predecision freeze and independently executed R002 reconstruction recovered the same governed target/ASG identity and exactly the same 21 compared reconstruction fields. The subsequent B0 read-only accessibility preflight found no admissible resolved predicate difference; the permissions audit left effective candidate permission unresolved.

This evidence remains Class-II fixture-level methodological evidence and is not an observed industrial-case result.

## Material methodological evidence — SWIM Reactive-0

**Case:** `SWIM Reactive-0`  
**Run:** `Reactive-0-20260911-17:49:20-1`  
**Status:** `CLOSED — BOUNDED TGCV OPERATIONALIZATION RESULT`  
**Disposition:** `00_GOVERNANCE/SIP/TGCV_SWIM_REACTIVE0_OPERATIONALIZATION_DISPOSITION_001.md`

The frozen SWIM Reactive-0 execution completed successfully with a reproducible `.sca/.vec` result bundle. Existing run evidence and deterministic source semantics were used to reconstruct candidate transformation identities, pre-outcome accessibility predicates, multiple accessible-transformation snapshots and observed changes in that space.

Bounded candidate universe: `Uτ = {AddServer, RemoveServer, SetDimmer(k)}` with only observed dimmer targets represented in the bounded reconstruction.

The reconstruction yielded multiple `T_acc,t` snapshots and non-empty `ΔT_acc` transitions, including: `t=600 → 660` AddServer enters `T_acc`; `t=660 → 3960` RemoveServer leaves `T_acc`; `t=3960 → 4680` RemoveServer re-enters `T_acc`; `t=4680 → 4740` AddServer leaves `T_acc` at `maxServers=3`.

This is material evidence because it operationalizes the bounded chain `S_t,C_t → Pτ(S_t,C_t) → T_acc,t → ΔT_acc` without using downstream outcome to define accessibility.

### Interpretation boundary

The result supports bounded operational reconstructability of accessible transformation space and its change over time in this SWIM exemplar. It does **not** establish transversal novelty, causal effects on trajectories, value creation or prediction, explanatory superiority, general validity across self-adaptive systems, or industrial utility/production benefit.

## Material methodological evidence — SWIM trajectory linkage

**Case:** `SWIM Reactive-0 — bounded trajectory-linkage reconstruction`  
**Status:** `CLOSED — BOUNDED TRAJECTORY-LINKAGE RECONSTRUCTION`  
**Disposition:** `00_GOVERNANCE/SIP/TGCV_SWIM_TRAJECTORY_LINKAGE_DISPOSITION_001.md`  
**Matrix reconciliation:** `00_GOVERNANCE/SIP/TGCV_SWIM_TRAJECTORY_LINKAGE_MATRIX_RECONCILIATION_001.md`

Existing Reactive-0 evidence was further reconstructed without new execution to test whether already established accessibility-space changes could be followed by distinguishable bounded trajectories of selected transformations and system-state transitions.

The result establishes the bounded analytical linkage `S_t,C_t → Pτ(S_t,C_t) → T_acc,t → ΔT_acc,t → selected τ_t → S_{t+1},C_{t+1} → bounded subsequent trajectory`. At the recorded accessibility transitions, the evidence permits reconstruction of ordered subsequent selected transformations and state transitions.

This result is an observed association/reconstructability result. It does **not** establish that `ΔT_acc` causes the subsequent trajectory, general modification of all reachable future trajectories, counterfactual trajectory differences, value creation or prediction, explanatory superiority, transversal validity, or industrial utility.

## Material methodological evidence — SWIM Reactive2

**Case:** `SWIM Reactive2`  
**Run:** `Reactive2-0`  
**Status:** `CLOSED — BOUNDED METHODOLOGICAL EVIDENCE; A8 NOT_COMPARABLE`  
**Disposition:** `00_GOVERNANCE/SIP/TGCV_SWIM_REACTIVE2_POLICY_INDEPENDENCE_GATE_DISPOSITION_001.md`  
**Matrix reconciliation:** `00_GOVERNANCE/SIP/TGCV_SWIM_REACTIVE2_MATRIX_RECONCILIATION_001.md`

Reactive2 completed under the authorized Run-0 scope using the same frozen SWIM infrastructure and inputs. The evidence supports a bounded separation between `candidate identity → pre-outcome accessibility → T_acc → native policy selection → execution` for the observed candidate families `{AddServer, RemoveServer, SetDimmer(k)}`.

The result is material because it adds a methodological qualification not established by Reactive-0 alone: native adaptation-manager policy can change the selected action sequence while candidate/accessibility representation remains analytically separable from downstream policy selection at inspected points.

### Comparability boundary

Criterion A8 is `NOT_COMPARABLE`. Timestamp coincidence and partial vector-state coincidence are insufficient to establish identical predecision `(S_t,C_t)` because zero-latency/event-ordering effects and differing preceding adaptation histories can make same-timestamp observations represent different transition positions. Therefore Reactive2 does **not** establish policy-independent accessibility under an identical matched state/context with Reactive-0.

### Interpretation boundary

Reactive2 provides bounded methodological support for analytical separation of accessibility from native policy selection. It does **not** establish general policy-independent accessibility, identical predicates at matched state/context, downstream trajectory effects, causal effects, value creation or prediction, explanatory superiority, transversal validity, or industrial utility/production benefit.

## Material industrial evidence — IT-G1 AWSSupport-ExecuteEC2Rescue

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`  
**Candidate:** `AWSSupport-ExecuteEC2Rescue`  
**Status:** `CLOSED — FUNCTIONAL RECOVERY DEMONSTRATED`  
**Canonical integration:** `00_GOVERNANCE/INDUSTRIAL_TRACK/execution/IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_FINAL_RESULT_INTEGRATION_001.md`

### Governed evidence sequence

`AWSSupport-ExecuteEC2Rescue SUCCESS → internal Windows/RDP state repaired → read-only diagnostic attribution to Security Group inbound policy → explicit narrow remediation authorization → TCP/3389 ingress rule applied → same-observation-point functional verification PASS`

### Evidence content

The authorized EC2Rescue execution repaired the internal Windows/RDP state of the target instance. The historical execution result recorded internal remediation success but did not demonstrate end-to-end functional recovery. A subsequent read-only diagnostic identified the primary observed blocker as the target Security Group inbound policy: `sg-05c212fdd50abc3fc` had no inbound rule, while the main route table provided an Internet gateway path, the NACL allowed IPv4 traffic, Windows `TermService` was running and TCP/3389 was listening, and Windows Firewall profiles had been disabled by the remediation.

A separate explicit remediation authorization then permitted only a narrow ingress rule on `sg-05c212fdd50abc3fc`: TCP port `3389`, source `113.203.180.202/32`. AWS created rule `sgr-0fbb978cecdef01e9`. No NACL, route, Windows RDP, firewall, root-volume, stop/start or EC2Rescue changes were included in that remediation.

Functional verification was performed from the same observation point. Before the narrow remediation, external TCP/3389 verification failed. After the rule was applied, `Test-NetConnection 18.100.134.191 -Port 3389` returned `TcpTestSucceeded : True`. The final case closure therefore records `FUNCTIONAL RECOVERY = PASS`.

### Material methodological significance

IT-G1 is material evidence because it preserves analytically distinct states and conditions across a governed sequence: (1) internal transformation/remediation of target state; (2) persistence of an external enabling-condition blocker; (3) read-only attribution of that blocker; (4) separately authorized interaction with the enabling condition; and (5) functional end-to-end outcome.

The case therefore strengthens the bounded distinction between transformation of internal system state and the conditions required for that transformation to become externally functional. It also provides a bounded industrial observation of a change in the effective conditions surrounding a target transformation.

### Interpretation boundary

IT-G1 is one governed industrial case and remains a bounded exemplar. It does **not** establish complete `T_acc`, general trajectory modification, causal identification, value creation, predictive value, explanatory superiority, transversal validity, or general industrial utility.

The historical execution-result artifact remains immutable. The later diagnostic, authorization, remediation and verification artifacts establish the subsequent governed state transition; they do not rewrite the earlier result.

No claim status/level is upgraded by IT-G1.

## Material methodological evidence — FOS C09

# FOS C09 — Evidence Disposition 001

**Status:** CLOSED — NOT REPORTABLE UNDER FROZEN ESTIMATOR

FOS provides material bounded evidence for reconstructing intervention availability, randomized SUB/UC assignment, linkage to the 37-month endpoint, and weighted ITT arithmetic. It does not provide a reportable C09 causal estimate under the currently frozen TGCV estimator because a design-consistent randomization variance could not be demonstrated from the public-use files and frozen design information.

Frozen disposition:
- retain FOS as methodological/reference evidence;
- do not report SE, CI, p-value, or final causal effect;
- do not impute the single determinately unresolved SUB/UC endpoint;
- preserve the reconstructed weighted ITT only as arithmetic reconstruction, not as a causal result;
- no C09 claim upgrade;
- no TGCV Core change;
- no execution authorization;
- resume C09 candidate screening.

### Interpretation boundary

FOS is material methodological/reference evidence for reconstruction and evaluation of a candidate causal-design pathway. Its closure is specifically an estimator/reportability boundary: it does not constitute a reportable causal estimate for C09 and must not be used to infer one. Evidence propagation does not imply claim upgrade.

## Material methodological evidence — C09 Bundle 003 + independent Executor-2 reconstruction

**Case:** `C09_OPERATIONAL_BUNDLE_003`  
**Status:** `CLOSED — EXECUTOR-2 RECONSTRUCTION PASS / CAUSAL CLAIM REMAINS OPEN`  
**Execution result:** `03_EXPERIMENTS/C09_EXECUTOR_2_RECONSTRUCTION_RESULT_001.md`  
**Closure audit:** `00_GOVERNANCE/SIP/TGCV_C09_EXECUTOR_2_RECONSTRUCTION_CLOSURE_AUDIT_001.md`  
**Evidence registration:** `00_GOVERNANCE/SIP/TGCV_C09_EXECUTOR_2_RECONSTRUCTION_EVIDENCE_REGISTRATION_001.md`  
**Propagation record:** `00_GOVERNANCE/SIP/TGCV_C09_EVIDENCE_MATRIX_PROPAGATION_RECORD_001.md`

The frozen Bundle 003 causal-operationalization test specifies the bounded intervention `Z → ΔT_acc → Y` at `H=1`, with `U={A,B,C}`, control accessibility `T_acc=[A,C]`, treatment accessibility `T_acc=[A,B,C]`, deterministic balanced assignment and a fixed transformation-selection policy independent of the treatment flag except through the accessibility predicate. Bundle 003 is frozen and immutable.

Executor-2 independently reconstructed the frozen design using the subsequently frozen exact randomization specification. The reconstruction completed with `PASS_RECONSTRUCTION`, `n_control=128`, `n_treatment=128`, `mean_control=5.671875`, `mean_treatment=7.3203125`, and `tau_hat=1.6484375`. The retained null observation was `null_tau_hat=-0.3515625`; Bundle 003 explicitly does not impose a zero-null gate, so this value is not a failure condition.

All 13 Executor-2 integrity checks returned `true`, including accessibility intervention, balanced assignment, baseline definition, bundle-hash integrity, canonical row schema, transition/policy integrity, null no-accessibility-change, randomization-specification presence, and confirmation that Executor-1 output was not used as an input.

### Material methodological significance

This is material evidence because C09 moves from causal-design specification plus prior estimator-boundary evidence to a frozen, executable bounded causal-operationalization with an independent reconstruction. The result demonstrates that the specified intervention can produce a measurable bounded contrast in the frozen synthetic system while preserving the information firewall between treatment assignment, accessibility, transition, policy, observation and outcome.

The result is therefore evidence of **bounded causal operationalization and independent reconstruction**, not evidence of real-world causal identification. The positive `tau_hat` is a result of the governed synthetic reconstruction and must not be generalized to empirical causal effectiveness. The nonzero null is retained as a control observation under the frozen specification and does not invalidate the execution.

### Interpretation boundary

The reconstruction does **not** close C09 scientifically. It does not establish an admissible real-world intervention, external validity, empirical causal effect, transversal validity, value creation, predictive value, explanatory superiority, or TGCV Core modification. It also does not supersede the FOS C09 estimator/reportability boundary; FOS remains methodological/reference evidence only.

## Material empirical causal evidence — KGFS Rural Banking

**Case:** `KGFS Rural Banking — Barboni, Field, Pande`  
**Status:** `CLOSED — D5-A IDENTIFIED CONTRIBUTION`  
**Operationalisation audit:** `00_GOVERNANCE/SIP/TGCV_C09_KGFS_TACC_OPERATIONALISATION_AUDIT_001.md`  
**D5-A closure:** `00_GOVERNANCE/SIP/TGCV_C09_KGFS_D5A_CLOSURE_RECORD_001.md`  
**Trajectory bridge:** `00_GOVERNANCE/SIP/TGCV_C09_KGFS_ACCESSIBILITY_TO_TRAJECTORY_BRIDGE_001.md`  
**Exact variable audit:** `00_GOVERNANCE/SIP/TGCV_C09_KGFS_TRAJECTORY_VARIABLE_AUDIT_001.md`  
**Download manifest:** `03_EXPERIMENTS/C09_KGFS_TRAJECTORY_AUDIT/output/KGFS_D178_DOWNLOAD_MANIFEST.json`  
**Source reconciliation:** `00_GOVERNANCE/SIP/TGCV_C09_KGFS_D178F70_SOURCE_INCONSISTENCY_AUDIT_001.md`

KGFS provides the decisive real-world causal layer for C09. The study uses randomized expansion of banking infrastructure at the service-area level, with treatment consisting of early opening of a KGFS branch. The intervention is a structural accessibility intervention under D5.2-S: it changes the local financial-access system itself rather than merely encouraging downstream use.

The TGCV reconstruction is:

`S0 = absence of KGFS branch/service system`  
`T_acc,0 = financial transformations structurally accessible pre-opening`  
`Z = randomized early branch assignment/opening`  
`S1 = branch/service system present`  
`T_acc,1 = T_acc,0 + structural financial-access capabilities introduced by KGFS`  
`ΔT_acc = T_acc,1 − T_acc,0`

The structural accessibility representation includes the introduced local branch access and associated formal financial capabilities: formal loans, formal savings, formal insurance and tailored financial advice/wealth-management services. Downstream take-up, investment, employment, income and poverty variables are not substituted for `T_acc`.

D5.0 and D5.1 are PASS. D5.2-S is PASS because assignment is randomized, the intervention implements a structural accessibility change, pre/post accessibility can be characterized independently of downstream outcomes, the estimand is the causal effect of the structural intervention, and downstream adoption is not used as the accessibility construct. D5.3 pathway audit is PASS and D5.4 classification is `D5-A IDENTIFIED CONTRIBUTION`.

The public longitudinal trajectory architecture was independently audited at exact variable level: `technical_status=PASS`, `files_audited=74`, `missing=[]`, `scientific_claim_status=NO_C09_UPGRADE` at the technical-audit stage. The 74 public `.dta` files were reconciled against the Yale D178 inventory; D178F70 retained a documented catalogue-size discrepancy while the current Dataverse object and checksum were verified. No fabricated padding or byte repair was used.

### Causal interpretation

KGFS therefore supplies an admissible real-world causal architecture in which a randomized structural change in accessibility is followed by observed downstream household/economic trajectories over the study's post-intervention period. This supports the bounded C09 proposition that accessibility changes causally affect subsequent trajectories in the studied setting.

The result is deliberately bounded. It does not establish universal causality across all generative systems, sole causation, universal effect magnitude, that every accessibility change changes a trajectory, or causal `ΔT_acc → ΔV`. It also does not by itself establish full transversal validation of TGCV Core.

## Material empirical causal evidence — C10C-002 Urban Mexico infrastructure

**Case:** `C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico`  
**Study:** McIntosh, Alegría, Ordóñez & Zenteno (2018), AEJ Applied Economics  
**Replication deposit:** `OpenICPSR 113705, V1`  
**Status:** `CLOSED — NEGATIVE BOUNDED CAUSAL RESULT`  
**Closure artifact:** `00_GOVERNANCE/SIP/C10C002_BOUNDED_CAUSAL_EXPERIMENT_CLOSURE_001.md`

C10C-002 is material empirical evidence for the bounded structural reconstruction of accessibility and for the methodological ability to execute a falsifiable causal test without post-hoc rescue after a negative result. It is propagated to C02, C07, C11 and C16, but it does **not** upgrade any claim level.

### Source and design boundary

The public V1 deposit was acquired and audited under the frozen C10-C controlled-acquisition authorization. The intervention was randomized at polygon level: 370 eligible polygons, 176 treatment and 194 control, with two-level municipality-saturation randomization. The study contains baseline 2009 and follow-up 2012 household/block data and separate professional valuations of the same 464 unbuilt lots at baseline/follow-up. The V1 replication deposit contains the eight governed files recorded in the closure artifact, with their acquisition sizes and SHA-256 hashes preserved there.

### Bounded structural reconstruction

The admitted bounded transformation universe is:

`U_τ* = {A+, A−, D+, D−, L+, L−, G+, G−, B+, B−, P+, P−}`

corresponding to opening/closing six structural infrastructure dimensions: piped water, sewerage, electricity, curbs/medians, sidewalks and paved streets. The aggregate infrastructure index and downstream outcomes were not used as elementary transformations, and value/rent/private-investment/social-capital/crime/satisfaction outcomes were excluded from `P_τ`.

For each dimension the minimal structural feasibility predicates were frozen as:

`P_{τ_j+}(S_t)=1 if S_{j,t}<1`  
`P_{τ_j−}(S_t)=1 if S_{j,t}>0`

This yields structural-only `T_acc,t*` snapshots and deterministic `ΔT_acc*` without fabricating ex-ante mechanistic accessibility. The bounded reconstruction covered all 342 `sample_panel` polygons observed in both rounds. There were 64 unique `T_acc,0*` signatures, 53 unique `T_acc,1*` signatures, 104 polygons with openings, 171 with closures, and 238 polygons with non-empty `ΔT_acc*`. Treatment was never used in the accessibility predicate and value variables were not used in `T_acc*` construction.

The T10–T15 gate chain established source identity, structural-variable recovery, temporal linkage, treatment/state separation, bounded transformation-universe construction, predicate integrity, endpoint separation, deterministic reconstruction, causal-unit linkage, positivity and a frozen polygon-level ITT specification. The scalar causal outcome was frozen as:

`ΔT_acc_net = |T_acc,1*| − |T_acc,0*|`

with N=342, range −3 to +4, mean −0.2368421053 and 217 polygons with nonzero net change.

### Causal execution and closure

The frozen treatment was polygon-level randomized treatment `treat`, with municipality-clustered ITT and no post-treatment covariates, saturation, value or downstream variables in the specification. The direct OLS estimate was:

`β_ITT = −0.031421139101862026`  
`cluster SE = 0.1645865990128021`  
`normal p = 0.848596526762317`  
`normal 95% CI = [−0.3540108731669541, 0.2911685949632301]`

The pre-specified Rademacher wild-cluster bootstrap with 9,999 draws produced:

`p = 0.8354`  
`critical 95% = 1.6846375446998223`  
`95% CI = [−0.3086899031532831, 0.24584762494955906]`

The scientific closure is therefore `C10C002_CLOSED_NEGATIVE_BOUNDED_CAUSAL_RESULT`: no statistically detectable treatment effect on the frozen net number of accessible transformations under the bounded operationalization. This is **not** evidence that the true effect is exactly zero, is **not** positive causal support for TGCV, and is **not** a refutation of TGCV. The experiment is closed and must not be repeated merely to seek a positive result.

### Methodological significance

C10C-002 demonstrates the bounded methodological progression `bounded universe → operationalizable real case → structural reconstruction → frozen causal estimand → causal execution → negative bounded result`, while preserving the separation between structural accessibility and downstream/value outcomes. It therefore materially supports the programme's methodological criterion that the minimum sufficient bounded transformation universe can be preferable to attempting to operationalize the maximum theoretically conceivable universe at the outset.

### Interpretation boundaries

The value pathway was not executed. Municipal treatment saturation/interference remains unresolved: all 60 municipalities contain mixed treatment/control and the available saturation variables could not be fully reconstructed from deposited code, so broader causal interpretation is conditional on this unresolved interference issue. C10C-002 does not establish trajectory modification, does not provide evidence for `ΔT_acc → ΔV`, does not establish transversal validity, and does not modify the TGCV Core.

## Claim boundary

The v1.8 update preserves the full evidence/claim structure of v1.7 and adds the C10C-002 empirical evidence record plus bounded propagation to C02, C07, C11 and C16. No C01–C16 status is upgraded. C08, C09 and C10 are explicitly not upgraded or positively supported by C10C-002. The TGCV Core remains unchanged.

## Gate state

- G1 Independent replication: OPEN at general scientific level; bounded fixture/event closures remain separately recorded.
- G2 Cross-domain generalisation: BOUNDED / PARTIAL.
- G3 Trajectory sufficiency: OPEN; bounded trajectory-linkage and IT-G1 state-transition observations do not close the general gate; C10C-002 does not measure trajectory outcomes.
- G4 Causal identification: **BOUNDED PASS at C09 claim level** through KGFS D5-A; C10C-002 provides a separate negative bounded causal test of intervention → `ΔT_acc*` and does not extend C09.
- G5 Value linkage: OPEN; C10C-002 value pathway not executed.
- G6 Originality/comparative architecture: BOUNDED / PARTIAL.
- G7 Transversal translation protocol: BOUNDED operational support; C10C-002 adds a distinct urban-infrastructure domain but general/transversal closure remains OPEN.

## Current methodological routing

- IUT-A-01 U2 FULL_PILOT 001: `CLOSED — U2-NULL`; no rerun.
- IT-NOSD-010: G0/G1/G2 closed for one bounded frozen event; industrial execution authorization `NONE`.
- EXT-UPD-4.8 O3 accessibility closure: `CLOSED — INDETERMINATE / H-B / HS-AC01`; no reopening or additional attempt under this closure.
- Class-II AWS-PatchAsgInstance: fixture-level closure as previously governed.
- SWIM Reactive-0: `CLOSED — BOUNDED TGCV OPERATIONALIZATION RESULT`; no repeat run for current claim.
- SWIM trajectory linkage: `CLOSED — BOUNDED TRAJECTORY-LINKAGE RECONSTRUCTION`; no repeat run for current bounded reconstruction.
- SWIM Reactive2: `CLOSED — BOUNDED METHODOLOGICAL EVIDENCE; A8 NOT_COMPARABLE`; no additional execution under current gate.
- IT-G1 `AWSSupport-ExecuteEC2Rescue`: `CLOSED — FUNCTIONAL RECOVERY DEMONSTRATED`; no rerun implied.
- C09 Bundle 003 Executor-2 reconstruction: `CLOSED — PASS`; no further Bundle 003 rerun justified.
- KGFS Rural Banking: `CLOSED — D5-A IDENTIFIED CONTRIBUTION`; no repeat of existing local reproducibility audit justified.
- C10C-002 Urban Mexico infrastructure: `CLOSED — NEGATIVE BOUNDED CAUSAL RESULT`; no rerun to seek a positive result; value pathway and unresolved interference remain boundaries.
- IT-METH-I FAA AMOC: `CLOSED — INCONCLUSIVE`.
- Utility scoring and new industrial execution: `NOT AUTHORIZED`.

## Current scientific position

The evidence base includes bounded comparative methodological evidence from IUT-A-01 U2, bounded downstream-separation/reconstructability evidence from IT-NOSD-010, bounded accessibility-closure boundary evidence from EXT-UPD-4.8, Class-II AWS fixture evidence, bounded self-adaptive software operationalization from SWIM Reactive-0 and Reactive2, bounded SWIM trajectory-linkage reconstruction, the closed IT-G1 industrial case, FOS C09 methodological/reference evidence, the closed C09 Bundle 003 Executor-2 independent reconstruction, the closed KGFS real-world causal architecture, and the closed C10C-002 urban-infrastructure bounded causal experiment. These are cumulative material evidence records. The only claim-level change in v1.7 remains C09; v1.8 adds evidence propagation only and makes no claim-level status upgrade. The scientific Core remains unchanged.
