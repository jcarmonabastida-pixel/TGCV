# TGCV — Evidence-to-Claim Matrix — Current v1.18

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT  
**Date:** 2026-09-18  
**Predecessor:** v1.17  
**Incremental governance update:** Corrects the VSL Synthetic Minimum routing: the experiment adds bounded methodological evidence to C16 only; it does not add evidence to C10. The complete GL-07 material expediente is retained. No claim-level upgrade; C09, Core and RMA remain unchanged.

**C05 material-evidence update:** The C05 frozen runner, runtime execution, post-execution audit and evidence-to-claim propagation are incorporated as a bounded synthetic application-fit record. The result is propagated only to C02, C07, C08 and C16 within the explicitly stated methodological limits. The synthetic baseline is not independent evidence, and NC2 does not constitute a trajectory-policy sensitivity test because the frozen trajectory implementation does not consume the added `selection_tiebreak` field.

## Matrix preservation rule
This matrix is cumulative. Every new version MUST preserve the full evidentiary content and schema of its predecessor and add, qualify, bound, supersede, or explicitly retire information. A version MUST NOT silently reduce the number of claim-matrix columns, remove material evidence descriptions, collapse evidence basis into summary-only fields, or replace detailed evidence records with a short status table.

`EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` is a stable alias of the complete versioned current matrix; it MUST NOT be a simplified derivative.

## Material evidence propagation rule
A material experimental result is propagated to this matrix when it adds, removes, qualifies, bounds, or otherwise changes the evidentiary basis or interpretation of a claim, even when no claim status/level changes. Claim upgrade is a separate decision and is never inferred merely from evidence propagation.

**Operational rule:** Evidence propagation does not imply claim upgrade. A claim-level upgrade requires an explicit claim-level consolidation record.

**Material-section completeness rule:** Every material evidence item propagated into one or more claim rows MUST have a corresponding enriched `Material ... evidence` section in the same matrix version. The claim table is the routing/index layer; the material-evidence section is the developed evidentiary record. Table-only references are insufficient. This rule applies equally to foundational/base experiments that originally established claims and to later experiments. Where a foundational material result was previously represented only by a compressed table reference, the result MUST be restored cumulatively with its quantitative findings, provenance, operational scope, reproducibility boundary, interpretation limits and claim propagation. The integrity check is bidirectional: `material evidence item in claim table ↔ corresponding enriched material-evidence section`.

## Current claim matrix

| ID | Claim | Status | Current evidence / basis | Evidence impact / interpretation | Next requirement |
|---|---|---|---|---|---|
| C01 | TGCV represents system state/context/conditions and constraints/resources | E0 | Formal architecture + bounded cross-domain traces + IT-G1 bounded industrial case + C10C-004 + MT4| IT-G1 adds material bounded evidence for reconstruction of internal state and external enabling conditions. C10C-004 adds bounded methodological evidence that an empirical construct can be traced from instrument semantics through physical variables to an executable derived outcome, without establishing TGCV state representation. No claim-level upgrade. MT4 adds bounded methodological evidence for identifying and preserving a technical constraint/state layer in a heterogeneous electricity-system domain. No claim-level upgrade.| Further independent operational confirmation |
| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Formalization + Rust + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 + IT-G1 + C10C-002 + C10C-001 + C10C-003 + C10C-004 + MT4 TSTC v004| SWIM provides bounded accessibility operationalization; IT-G1 adds bounded evidence that end-to-end accessibility/function can depend on conditions external to the internal remediation target; C10C-002 adds an independent real-world bounded reconstruction of `T_acc*` from six structural infrastructure dimensions using pre-outcome structural predicates across 342 polygons and two observed rounds. C10C-001 independently demonstrates in a distinct non-software case that structural state reconstruction and observed configuration changes do not identify `Pτ`/`T_acc` without an explicit admissibility predicate. C10C-003 adds a distinct randomized non-software boundary case in which rich longitudinal structural data and treatment/take-up variables do not identify a non-circular accessibility predicate within the bounded operational search. General `T_acc` remains unclosed. C10C-004 adds no direct positive accessibility evidence: its women's-empowerment construct is not an independently defined TGCV admissibility predicate and must not be relabeled as `T_acc`. No claim-level upgrade is implied. MT4 adds a bounded methodological qualification through the partially formalized CORE6 candidate layer with 92.58% complete coverage; full `P_tau` remains undetermined. No claim-level upgrade. TSTC v004 adds bounded synthetic application-fit evidence for explicit transformation, admissibility/accessibility and `T_acc` representation; methodological only, no claim upgrade. C05 adds bounded synthetic application-fit evidence for explicit candidate transformations, admissibility/accessibility and `T_acc`, including the T3 `T_acc` reduction from 8 to 6; baseline equivalence is not independent evidence and no claim-level upgrade is inferred.| Independent operationalization across a distinct exemplar |
| C03 | T_acc is analytically distinct from downstream Reach in bounded Rust | E1 | Rust RUST-DYN-2 / EXEC-1A; ND-1 = 159,921 and ND-2 = 278,282 adjacent temporal pairs with `Delta T_acc != 0`, distinguishing zero-change and nonzero-change bounded potential Reach outcomes | The enriched RUST-DYN-2 record makes the bounded structural distinction quantitatively explicit. SWIM does not alter the bounded Rust claim level; IT-G1 does not test the Rust-specific Reach separation; C10C-002 does not operationalize downstream Reach identity; C10C-003 does not test Reach identity. No claim-level upgrade.| Independent replication |
| C04 | ΔT_acc can occur without ΔReach¹_pot | E1 | Rust RUST-DYN-2 / EXEC-1A ND-1 = **159,921 adjacent temporal pairs** with `Delta T_acc != 0` and `Delta Reach^1_pot = 0` | Direct bounded empirical evidence in the frozen Rust representation that transformation-space change can occur without a change in bounded H=1 potential Reach. No direct test by SWIM, IT-G1, C10C-002 or C10C-003. No claim-level upgrade.| Independent replication |
| C05 | ΔT_acc can occur with ΔReach¹_pot change | E1 | Rust RUST-DYN-2 / EXEC-1A ND-2 = **278,282 adjacent temporal pairs** with `Delta T_acc != 0` and `Delta Reach^1_pot != 0` | Direct bounded empirical evidence in the frozen Rust representation that transformation-space change can coincide with a change in bounded H=1 potential Reach. No direct test by SWIM, IT-G1, C10C-002 or C10C-003. No claim-level upgrade.| Independent replication |
| C06 | Reach identity is not characterized by cardinality alone | E1 | Rust RUST-DYN-2 / EXEC-1A ND-4 = **266,201 adjacent pairs** with equal Reach cardinality but different Reach membership | Direct bounded structural evidence that equal cardinality does not imply Reach identity. C10C-002 uses a scalar net cardinality outcome only for its frozen bounded causal test and does not establish Reach identity; C10C-003 does not test Reach identity. No claim-level upgrade.| Independent replication |
| C07 | Accessible transformation spaces change over time in Rust | E1 | Rust RUST-DYN-2 / EXEC-1A: **438,203 non-persistent of 516,061 adjacent pairs (~84.91%)**, with PERSISTENCE 77,858, EXPANSION 8,295, CONTRACTION 3,786 and RECONFIGURATION 426,122 | The enriched Rust record supplies the quantitative temporal evidence underlying the bounded claim. SWIM provides bounded non-Rust evidence that accessible transformation spaces can change across observed state transitions; IT-G1 adds a bounded industrial state-transformation sequence; C10C-002 adds independent real-world longitudinal evidence from 342 polygons in which a bounded universe of 12 elementary structural transformations yields non-empty `ΔT_acc*` in 238 polygons, including 104 openings and 171 closures. C10C-001 adds a distinct non-software boundary case in which observed structural changes are reconstructible but `T_acc` and `ΔT_acc` are not identified. C10C-003 adds a second distinct non-software boundary case in which observed longitudinal configuration changes are available but `T_acc` and `ΔT_acc` remain unidentified within the bounded operational search. These cases qualify the distinction between observed structural change and accessible transformation-space change and are not evidence of `ΔT_acc`. C10C-004 is an endline operationalisation audit and does not reconstruct `U_tau`, `P_tau` or `ΔT_acc`. MT4 adds a bounded boundary qualification separating candidate technical constraints from realized technology changes; it does not establish a complete `T_acc` or positive `Delta T_acc` result. No claim-level upgrade. C05 adds bounded synthetic evidence of `Delta T_acc != 0` under T3 (8→6, with `accept_B` and `redirect_A_to_B` closed) and no accessibility delta under T1/T2/T4/T5/T6/NC1/NC2; this is synthetic methodological evidence only.| Independent closed operationalization / replication |
| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded Rust H=1 + SWIM trajectory-linkage reconstruction + IT-G1 bounded state/trajectory observation + C10C-001 + C10C-003 + MT4 TSTC v004| SWIM adds bounded reconstructability of ordered subsequent transformations and state transitions; IT-G1 provides a bounded industrial state/trajectory observation. KGFS supplies the causal layer now reflected in C09. C10C-002 does not add a trajectory outcome. C10C-001 and C10C-003 add complementary empirical boundary qualifications: structural change, realized intervention and conventional longitudinal outcomes cannot substitute for identified accessibility and reachable-trajectory evidence. No trajectory causal estimand is established by either case. No claim-level upgrade is implied. MT4 adds bounded methodological separation among candidate constraints, realized transformations and state/trajectory variables, but does not establish a trajectory causal estimand. No claim-level upgrade. TSTC v004 adds bounded synthetic representation of transition and subsequent trajectory fields; no causal trajectory estimand or claim upgrade. C05 adds bounded synthetic transition/trajectory representation; NC2 is not a trajectory-policy sensitivity test because `trajectory()` does not consume `selection_tiebreak`; no causal trajectory estimand is established.| Independent valid trajectory test with explicit trajectory criterion beyond bounded exemplars |
| C09 | Accessibility changes causally affect subsequent trajectories | **PASS — BOUNDED EMPIRICAL CAUSAL SUPPORT** | SWIM trajectory-linkage reconstruction + RUST-DYN-2 bounded structural evidence + KGFS randomized structural accessibility intervention with D5-A identified contribution + KGFS exact 74/74 trajectory-variable reproducibility audit + C09 Bundle 003 Executor-2 reconstruction + FOS methodological/reference evidence + MT4| Claim-level consolidation establishes bounded empirical causal support. KGFS provides the decisive real-world causal layer: randomized early expansion of KGFS banking infrastructure, reconstructable structural accessibility change, D5.2-S applicability, D5-A identified contribution, and reproducible longitudinal trajectory variables. SWIM and RUST-DYN-2 provide complementary bounded structural/trajectory-linkage support. Bundle 003 remains synthetic causal-operationalization evidence and FOS remains non-reportable under its frozen estimator. C10C-002 is deliberately excluded from positive C09 support because its estimand tests the intervention effect on `ΔT_acc*`, not the effect of `ΔT_acc*` on subsequent trajectories. C10C-003 adds no positive causal support because `ΔT_acc` is not identified. MT4 provides no positive causal evidence for `Delta T_acc -> subsequent trajectory`; the existing bounded causal status remains unchanged.| Independent real-world replication across a distinct domain; broader generality; no automatic value claim |
| C10 | Accessibility changes generate/predict value | H | No Value evidence + MT4| SWIM, RUST-DYN-2, KGFS, IT-G1, C10C-002 and C10C-003 do not establish causal `ΔT_acc → ΔV` or predictive value. C10C-002 explicitly did not execute a value regression. C10C-003 does not identify the TGCV accessibility layer required for a value pathway. No value claim is established. MT4-8 isolates `Inv`, `Fixed_OM_annual` and `Variable_OM` from the CORE6 candidate accessibility rule, but does not establish a downstream TGCV value endpoint or `Delta T_acc -> Delta V`. C10 remains open.| Value-linked test |
| C11 | TGCV is domain-independent / transversal | H | C-01 A-C + I-01 Gate C + bounded cross-domain evidence + C10C-002 + C10C-001 + C10C-003 + MT4 TSTC v004| SWIM is a bounded self-adaptive software exemplar, IT-G1 a bounded industrial AWS exemplar, KGFS a bounded real-world rural-finance intervention, C10C-002 a bounded urban-infrastructure/real-estate empirical case, C10C-001 a non-software export experiment and C10C-003 a randomized rural-energy-access experiment. C10C-001 and C10C-003 both add boundary evidence showing that structural state/change can be recovered while accessibility remains unidentified unless an explicit admissibility predicate is available. This strengthens documented heterogeneity and boundary evidence only; it does not establish transversal validity or justify a claim upgrade. MT4 adds bounded methodological cross-domain evidence from a heterogeneous electricity-system domain and strengthens documented transfer/boundary evidence only; it does not establish transversal validity or justify a claim upgrade. TSTC v004 adds bounded synthetic heterogeneity and domain-specific baseline comparison; no real-world transversal validity or claim upgrade.| Independent operationalization across broader domains |
| C12 | TGCV provides superior explanatory representation | H | Comparative evidence absent | IUT M1 provides bounded decision-performance evidence but U2-NULL; SWIM, IT-G1, KGFS, C10C-002 and C10C-003 are non-comparative for explanatory superiority. | Controlled differentiated comparison |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21 | No material impact. | Comparative coverage |
| C14 | T_acc is an ontological primitive independent of S | F | TR-131 | No impact; SWIM, IT-G1, KGFS, C09 Bundle 003, C10C-002 and C10C-003 treat accessibility as derived/conditioned rather than restoring the rejected primitive. | No restoration without contrary evidence |
| C15 | Rust demonstrates observed Cargo/runtime reachability | F | Rust evidence boundary | No impact. | Separate governed runtime test |
| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22/23 + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 + SWIM trajectory-linkage reconstruction + IT-G1 + C09 Bundle 003 + C10C-002 + C10C-001 + C10C-003 + C10C-004 + MT4 TSTC v004 + VSL Synthetic Minimum v0.1| SWIM supports bounded state/context → accessibility → `T_acc` → `ΔT_acc` and bounded trajectory linkage. IT-G1 adds bounded industrial evidence preserving distinctions among internal state transformation, external enabling condition and end-to-end outcome. C09 Bundle 003 adds bounded executable causal-operationalization evidence while preserving the distinction between intervention/accessibility and downstream outcome. C10C-002 adds a reproducible real-world bounded chain `Z → ΔS → T_acc* → ΔT_acc* → frozen causal estimand`, with structural-only predicates, explicit treatment/state separation, endpoint separation, and a negative result retained without post-hoc rescue. C10C-001 adds a complementary non-software boundary case preserving distinctions among structural state, candidate transformations, accessibility and realized transformations while preventing temporal leakage. C10C-003 adds a second randomized non-software boundary case preserving the same distinctions and explicitly qualifying the bounded scope of accessibility operationalization. C10C-004 adds a worked non-software translation example preserving the distinction among instrument semantics, raw variables, derived outcomes and TGCV constructs. It does not close downstream value boundaries or establish transversal validity. MT4 adds bounded methodological evidence preserving separation among state, candidate transformations, accessibility, realized transformations, trajectory and economic/value-related variables. No claim-level upgrade. TSTC v004 provides primary bounded methodological evidence for application-fit of the translation protocol across heterogeneous synthetic fixtures, including cross-domain paths and negative controls; no causal, value, superiority, generality or industrial-validation claim upgrade. C05 adds bounded synthetic application-fit evidence preserving the distinctions among candidate transformations, admissibility, `T_acc`, transition, bounded trajectory fields, negative controls and explicit non-claims; no causal, value, superiority, generality or deployment claim is inferred.| Closed independent-domain operationalization / downstream test |

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

## Material empirical evidence — C10C-003 India Static Inspection

**Case:** `C10C-003 — Does basic energy access generate socioeconomic benefits? A field experiment with off-grid solar power in India`  
**Status:** `CLOSED — DATA-LEVEL STATIC INSPECTION; STRUCTURAL READINESS LIMITATION CONFIRMED`  
**Source freeze:** `00_GOVERNANCE/SIP/TGCV_C10C003_SOURCE_VERSION_FREEZE_003.md`  
**Inspection request:** `00_GOVERNANCE/SIP/TGCV_C10C003_STATIC_INSPECTION_REQUEST_001.md`  
**Result:** `00_GOVERNANCE/SIP/TGCV_C10C003_STATIC_INSPECTION_RESULT_001.md`  
**Propagation:** `00_GOVERNANCE/SIP/TGCV_C10C003_EVIDENCE_TO_CLAIM_PROPAGATION_001.md`

The frozen Harvard Dataverse replication package provides rich longitudinal household data, treatment/installation/adoption variables, structural electricity and lighting variables and conventional causal-analysis code. Static inspection established only partial TGCV-specific state reconstruction: `S0` and `S1` remain `PARTIAL`; `U_tau` and `P_tau(S,C,L)` are `NOT_IDENTIFIED`; and `T_acc,0`, `T_acc,1` and `Delta T_acc` are `NOT_TESTABLE_FROM_PACKAGE`.

### Scope qualification

The inspection was **bounded by design**. It did not attempt exhaustive enumeration of the complete universe of transformations potentially conceivable for the experiment. It searched instead for a finite, prospectively defensible operational transformation space derivable from the frozen replication package and capable of supporting an independent pair `(U_tau, P_tau(S,C,L))` without using treatment realization, installation, subscription/take-up or downstream outcomes.

Failure to close `U_tau` and `P_tau` therefore **must not** be interpreted as proof that the complete transformation universe is intrinsically unbounded, intractable or incompatible with TGCV. The result establishes only that the frozen package did not provide enough information to close the required TGCV operationalization within the bounded search space justified by the available evidence.

### Material evidence

The package distinguishes treatment offer, installation and adoption/take-up and contains longitudinal observations of electricity status, primary lighting source, electricity hours, charging access, kerosene expenditure, savings, expenses, business, study, work time and household characteristics. These observations support structural-state inspection but do not define accessibility. In particular, `tvitt` is treatment assignment, `tvinstalled` is realized installation, `tvadopted` is take-up, and observed `lighttype`, electricity status or electricity hours are state observations rather than a prospective accessibility predicate.

Conventional ITT/LATE, spillover, waiting-list, exclusion, second-order and placebo procedures strengthen the original experiment's conventional causal identification but do not construct TGCV accessibility. No positive `Delta T_acc` evidence, trajectory causal estimand or value pathway is established.

### Evidence-to-claim propagation

- **C02:** Material bounded qualification. Rich longitudinal structural data and treatment/take-up variables do not identify a non-circular `P_tau(S,C,L)` within the bounded operational search. No upgrade.
- **C07:** Material boundary qualification. Observed longitudinal configuration changes do not establish `T_acc` or `Delta T_acc`; no positive accessibility-space-change evidence is propagated. No upgrade.
- **C08:** Material boundary qualification. Conventional longitudinal outcomes cannot substitute for identified accessibility and reachable-trajectory evidence; no trajectory causal estimand is established. No upgrade.
- **C11:** Material bounded cross-domain qualification. C10C-003 adds a randomized non-software rural-energy-access case showing that the state/accessibility distinction remains operationally relevant while also exposing a concrete identification boundary. No transversal-validity upgrade.
- **C16:** Material methodological evidence. The case reinforces the distinction among structural state, candidate transformation, accessibility, realized intervention and downstream outcome, including the prohibition against using treatment realization, take-up or later observed configurations to define accessibility retrospectively.

No positive propagation is made to C01, C03, C04, C05, C06, C09, C10, C12, C13, C14 or C15. No claim-level status is changed and no Core/RMA modification is implied.

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

## Material methodological evidence — C10C-004 Morocco Gate G4

**Case:** `C10C-004 — Morocco microcredit / women's empowerment`  
**Gate:** `G4`  
**Status:** `CLOSED — OPERATIONAL RECONSTRUCTION VERIFIED`  
**Result artifact:** `00_GOVERNANCE/SIP/TGCV_C10C004_MOROCCO_G4_WOMENS_EMPOWERMENT_RECONSTRUCTION_RESULT_001.md`  
**Propagation record:** `00_GOVERNANCE/SIP/TGCV_C10C004_MOROCCO_G4_EVIDENCE_TO_CLAIM_PROPAGATION_001.md`

C10C-004 provides a closed independent reconstruction of the historical endline women's-empowerment construct from `Microcredit_EL_mini_anonym.dta` (N=5,551). The reconstruction linked questionnaire semantics, physical variables, observed coding, the historical Stata construction block and an independent Python implementation. J1-J9 were reconstructed across the F1-F11 household slots; J9b was reconstructed separately as `women_10`; J10-J13 were reconstructed under the documented 3/4 rule as `women_11`-`women_14`. Standardisation and the historical `women_index` row-total specification were reproduced, including the duplicate `outcome2` and omission of `outcome3`, without post-hoc correction.

The reconstructed `women_index` had N=5,551, mean 0, sample SD 8.218129454, minimum -5.965017097, maximum 53.466739700 and zero missing values. J1-J9 showed no observed nonmissing coding outside `{1,2,-99}`. The result is bounded to operational reconstruction; it is not a TGCV accessibility, trajectory or value result.

### Evidence-to-claim propagation

- **C01:** Material methodological evidence, bounded. The case demonstrates explicit tracing from instrument semantics through physical variables to an executable derived outcome, but does not establish TGCV state representation. No upgrade.
- **C02:** No direct positive evidence; bounded methodological relevance only. The empowerment construct is not an independently defined TGCV admissibility predicate `P_tau(S,C,L)` and must not be promoted to `T_acc`. No upgrade.
- **C07:** No direct evidence. The case does not reconstruct a TGCV transformation universe, admissibility predicate or `Delta T_acc`. No upgrade.
- **C08:** No direct evidence. The empowerment index is not a TGCV reachable-trajectory variable and no trajectory causal estimand is established. No upgrade.
- **C09:** No evidence contribution. No TGCV causal estimate is produced.
- **C10:** No evidence contribution. No `Delta T_acc → Delta V` causal or predictive pathway is tested.
- **C11:** Bounded methodological contribution. The case adds a distinct non-software empirical domain for explicit construct translation, but does not establish transversal validity. No upgrade.
- **C16:** Material methodological evidence. The reconstruction preserves distinctions among instrument semantics, raw variables, derived outcomes and TGCV constructs, and preserves a historical code anomaly rather than silently correcting it. No upgrade.

C10C-004 does not modify TGCV Core, RMA, the accessibility definition, the causal chain or any claim-level status.

## Claim boundary

The v1.10 update preserves the full evidence/claim structure of v1.9 and adds the C10C-003 empirical/methodological evidence record plus bounded propagation to C02, C07, C08, C11 and C16. The complete C10C-002 and C10C-001 evidence records and prior bounded propagations remain preserved. No C01–C16 status is upgraded by C10C-003. C09 and C10 are not positively supported by C10C-003. The TGCV Core remains unchanged.

## Gate state

- G1 Independent replication: OPEN at general scientific level; bounded fixture/event closures remain separately recorded.
- G2 Cross-domain generalisation: BOUNDED / PARTIAL.
- G3 Trajectory sufficiency: OPEN; bounded trajectory-linkage and IT-G1 state-transition observations do not close the general gate; C10C-002 and C10C-003 do not establish trajectory causality.
- G4 Causal identification: **BOUNDED PASS at C09 claim level** through KGFS D5-A; C10C-002 provides a separate negative bounded causal test of intervention → `ΔT_acc*` and does not extend C09; C10C-003 adds no positive causal identification.
- G5 Value linkage: OPEN; C10C-002 value pathway not executed and C10C-003 does not identify the accessibility layer required for a value pathway.
- G6 Originality/comparative architecture: BOUNDED / PARTIAL.
- G7 Transversal translation protocol: BOUNDED operational support; C10C-002 and C10C-003 add distinct non-software domains but general/transversal closure remains OPEN.

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
- C10C-003 India: `CLOSED — DATA-LEVEL STATIC INSPECTION; STRUCTURAL READINESS LIMITATION CONFIRMED`; no causal execution under the current closure; any future revisit requires a separately justified bounded operationalization space and independent admission decision.
- IT-METH-I FAA AMOC: `CLOSED — INCONCLUSIVE`.
- Utility scoring and new industrial execution: `NOT AUTHORIZED`.

## Current scientific position

The evidence base includes bounded comparative methodological evidence from IUT-A-01 U2, bounded downstream-separation/reconstructability evidence from IT-NOSD-010, bounded accessibility-closure boundary evidence from EXT-UPD-4.8, Class-II AWS fixture evidence, bounded self-adaptive software operationalization from SWIM Reactive-0 and Reactive2, bounded SWIM trajectory-linkage reconstruction, the closed IT-G1 industrial case, FOS C09 methodological/reference evidence, the closed C09 Bundle 003 Executor-2 independent reconstruction, the closed KGFS real-world causal architecture, the closed C10C-002 urban-infrastructure bounded causal experiment, and the closed C10C-003 India static inspection. These are cumulative material evidence records. The only claim-level change in the cumulative matrix remains the prior C09 consolidation; v1.8 added C10C-002 evidence propagation, v1.9 added C10C-001 evidence propagation, v1.10 added C10C-003 bounded evidence propagation, and v1.11 adds C10C-004 bounded methodological evidence propagation, while v1.12 adds MT4 bounded methodological domain-transfer evidence propagation and restores/enriches the foundational RUST-DYN-2 material evidence record. None of these C10-C/MT4/Rust propagations changes any claim status. The scientific Core remains unchanged.

## Material empirical evidence — RUST-DYN-2 / EXEC-1A foundational Rust structural experiment

**Case:** `RUST-DYN-2 / EXEC-1A`  
**Status:** `CLOSED — BOUNDED STRUCTURAL EMPIRICAL TEST`  
**Operational horizon:** `H=1`  
**Frozen temporal rule:** `DR-035-v0.1-ADJACENT-CREATED-AT`  
**Frozen dataset SHA-256:** `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

### Purpose and operational scope

RUST-DYN-2 / EXEC-1A is the foundational empirical Rust experiment underlying the bounded C03–C07 evidence layer. It tests structural distinguishability between changes in the accessible transformation space `T_acc` and changes in bounded one-step potential Reach, while also characterizing temporal change in the frozen Rust package ecosystem. The operational Reach object is `Reach¹_pot`; the experiment does **not** execute Cargo or runtime behavior and therefore does not establish observed runtime reachability.

The frozen temporal population contains **516,061 adjacent package-version pairs** under `DR-035-v0.1-ADJACENT-CREATED-AT`, with `H=1`. The transition classification is:

- `PERSISTENCE`: **77,858**
- `EXPANSION`: **8,295**
- `CONTRACTION`: **3,786**
- `RECONFIGURATION`: **426,122**
- `NON-PERSISTENCE`: **438,203 / 516,061 ≈ 84.91%**

These counts are the bounded empirical population used for the Rust temporal claims and are not a sample-based estimate of a broader software ecosystem.

### ND-1 — transformation-space change without bounded Reach change

`ND-1 = 159,921` adjacent temporal pairs satisfy:

`Delta T_acc != 0` and `Delta Reach^1_pot = 0`.

This is the direct quantitative basis for **C04**. It establishes, within the frozen Rust representation and H=1 operationalization, that a change in accessible transformation space can occur without a change in the bounded potential Reach cardinal/identity outcome used by this test.

### ND-2 — transformation-space change with bounded Reach change

`ND-2 = 278,282` adjacent temporal pairs satisfy:

`Delta T_acc != 0` and `Delta Reach^1_pot != 0`.

This is the direct quantitative basis for **C05**. It establishes, within the frozen Rust representation and H=1 operationalization, that transformation-space change can also coincide with a change in bounded potential Reach.

### ND-4 — Reach identity is not reducible to cardinality

`ND-4 = 266,201` adjacent pairs have **equal Reach cardinality but different Reach membership**.

This is the direct quantitative basis for **C06**. Equal cardinality therefore does not establish identity of the reachable transformation set in the frozen representation. This is a structural identity result, not a claim about observed runtime execution.

### Temporal change and non-persistence

The **438,203 non-persistent pairs (84.91%)** provide the direct quantitative basis for **C07** within the frozen Rust operationalization. The classification shows that adjacent package-version transitions are dominated by reconfiguration in this historical technical ecosystem, with additional persistence, expansion and contraction classes. The result establishes bounded temporal change of the represented accessible transformation space; it does not by itself identify a causal mechanism for each change.

### Reproducibility and execution firewall

Primary and replay structured outputs were field-identical under the governed closure. The closure does **not** claim byte-level raw-file equality because independent raw JSON artifacts were not supplied during coordination. The experiment firewall reports no sampling, downstream outcome/value, future/predictive, Cargo-runtime or lockfile access. `Reach¹_pot` is a frozen analytical potential-Reach object, not an observed execution result.

The earlier immutable Rust source snapshots used in the foundational programme remain governed separately, including the 2018-09-26 snapshot `9110daee6752e903379f3af955506d6116315273` and the 2021-05-05 snapshot `a5dcd8438da2d8f99e3661a1956afbfb8f026fa0`, with the documented snapshot scale of 79,053 files / 449,893,157 bytes. These source snapshots are provenance for the broader Rust experimental lineage; the quantitative C03–C07 results above are specifically the closed RUST-DYN-2 / EXEC-1A evidence.

### Scientific interpretation

The strongest empirical result supported by RUST-DYN-2 is **bounded structural distinguishability between `Delta T_acc` and `Delta Reach^1_pot` in the frozen Rust representation**, together with bounded temporal change in the represented accessibility space. The experiment supports C03–C07 only within its stated operational scope.

The result must **not** be rewritten as evidence for:

- causality;
- predictive superiority;
- positive value creation;
- universal domain independence;
- complete prior-art absence;
- observed Cargo/runtime reachability;
- H>1 trajectory sufficiency.

In particular, C08 remains a hypothesis, C09's causal support comes from its separately governed evidence layer, C10 remains open, and C15 remains falsified for the observed-runtime interpretation.

### Evidence-to-claim propagation

- **C03:** Material quantitative support. ND-1 and ND-2 provide the bounded structural distinguishability evidence separating `T_acc` change from downstream H=1 potential Reach behavior. No upgrade beyond E1.
- **C04:** Material direct support. ND-1 = 159,921 pairs with `Delta T_acc != 0` and `Delta Reach^1_pot = 0`. No upgrade beyond E1.
- **C05:** Material direct support. ND-2 = 278,282 pairs with `Delta T_acc != 0` and `Delta Reach^1_pot != 0`. No upgrade beyond E1.
- **C06:** Material direct support. ND-4 = 266,201 pairs with equal Reach cardinality but different membership. No upgrade beyond E1.
- **C07:** Material direct support. 438,203 of 516,061 adjacent pairs are non-persistent (~84.91%), with the complete transition classification preserved above. No upgrade beyond E1.
- **C08:** Bounded structural antecedent only. The experiment uses H=1 potential Reach and does not establish H>1 trajectory sufficiency or a causal accessibility-to-trajectory effect. No upgrade.
- **C09:** Complementary bounded structural evidence only. RUST-DYN-2 is not a causal intervention and does not independently establish C09. The existing C09 bounded causal status is unchanged.
- **C10:** No value evidence. Outcome/value variables are excluded by the experiment firewall; no `Delta T_acc -> Delta V` result is available.
- **C15:** Boundary confirmation. The experiment uses `Reach^1_pot`, not observed Cargo/runtime execution; C15 remains F.

No positive propagation is made to C01, C02, C11, C12, C13, C14 or C16 beyond the bounded evidentiary basis already recorded. No claim-level status is changed and no TGCV Core/RMA modification is implied.

## Material methodological evidence — MT4 Domain Transfer

**Case:** `MT4 — Historical national electricity-system transitions / energy-system technology change`  
**Status:** `BOUNDED PASS — METHODOLOGICAL TRANSFER DEMONSTRATED WITH EXPLICIT LIMITS`  
**Primary frozen source:** Jaxa-Rozen, Wen & Trutnevyte, historic national electricity-system transitions dataset, Zenodo 6696776 v2.  
**Source SHA256:** `691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`

### MT4 objective and domain transfer

MT4 tests whether the candidate transversal analytical methodology can be transferred to a genuinely heterogeneous electricity-system domain without collapsing TGCV distinctions or importing downstream/value information into the accessibility layer. The frozen source covers national electricity-system transitions in Europe across 31 countries and 1990–2019.

### Gate summary and meaning

- **MT4-1 — Domain novelty: PASS.** The case provides a genuinely heterogeneous domain relative to the previously used exemplars.
- **MT4-2 — Frozen evidence: PASS.** The source package, version and hash were frozen before methodological interpretation.
- **MT4-3 — Structural inspection: PASS.** Country, technology, resource and technical/economic parameter structures were reproducibly identified.
- **MT4-4 — Semantic non-substitution: PASS — BOUNDED.** Candidate technical constraints were kept separate from realized transformations, state/trajectory variables and economic/value-related variables; observed realization was not relabeled as `T_acc`.
- **MT4-5 — `P_tau` technical formalization: OPEN / BOUNDED.** CORE6 provides a partially formalized technical candidate layer with 92.58% complete coverage, but full `P_tau` sufficiency remains undetermined.
- **MT4-6 — Independent reproducibility: PASS.** The frozen structural representation, coverage, missingness and discrimination results were independently reproduced.
- **MT4-7 — Downstream separation: BOUNDED PASS.** Candidate constraints, realized technology changes and state/trajectory variables were structurally separated; no trajectory causal estimand was established.
- **MT4-8 — Value isolation: BOUNDED PASS.** `Inv`, `Fixed_OM_annual` and `Variable_OM` were isolated from the CORE6 candidate accessibility rule; no downstream TGCV value endpoint was established.

### Consolidated methodological finding

The candidate TGCV analytical methodology can be transferred to a heterogeneous electricity-system domain while preserving explicit separation between candidate technical constraints, admissibility/accessibility, realized transformations, state/trajectory variables and economic/value-related variables. CORE6 provides a partially formalized technical admissibility candidate with 92.58% complete country-technology-year coverage, while full `P_tau` remains undetermined. Economic variables are structurally isolated from CORE6, but no independently established downstream TGCV `Delta V` endpoint has been demonstrated.

### MT4 material contribution to the claim matrix

- **C01 — bounded methodological support:** identifies and preserves a technical constraint/state layer in a heterogeneous electricity-system domain; no claim-level upgrade.
- **C02 — bounded qualification:** provides a partially formalized candidate admissibility layer through CORE6; full `P_tau` remains undetermined; no upgrade.
- **C07 — boundary qualification:** separates candidate technical constraints from realized technology changes and does not establish positive `Delta T_acc`; no upgrade.
- **C08 — bounded methodological support:** separates candidate constraints, realized transformations and state/trajectory variables, without establishing a trajectory causal estimand; no upgrade.
- **C09 — no positive causal propagation:** MT4 does not estimate `Delta T_acc -> subsequent trajectory`; the existing bounded causal status is unchanged.
- **C10 — material boundary qualification:** MT4-8 isolates economic parameters from CORE6 but does not establish `Delta T_acc -> Delta V`; C10 remains open.
- **C11 — bounded cross-domain evidence:** adds a heterogeneous electricity-system domain and strengthens documented methodological transfer/boundary evidence, but does not establish transversal validity.
- **C16 — bounded methodological evidence:** preserves the separation among state, candidate transformations, accessibility, realized transformations, trajectory and economic/value-related variables; no upgrade.

### Boundaries and research disposition

MT4 does not establish transversal causal validity, full `P_tau` sufficiency, `Delta T_acc -> Delta V`, or a general causal value mechanism. It does not promote observed adoption, installed capacity, generation, investment cost or operating-cost parameters into accessibility or value constructs by semantic substitution. MT4 is closed as a bounded methodological domain-transfer result; further work should target full `P_tau` formalization where feasible and a genuinely downstream, independently defined outcome/value endpoint.

# TGCV MT4 — Domain Transfer Result 001

## Status
**BOUNDED PASS — METHODOLOGICAL TRANSFER DEMONSTRATED WITH EXPLICIT LIMITS**

## Frozen source
Jaxa-Rozen, Wen & Trutnevyte, historic national electricity-system transitions dataset, Zenodo 6696776 v2.

SHA256:
`691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`

## Gate reconciliation
- MT4-1 Domain novelty: PASS
- MT4-2 Frozen evidence: PASS
- MT4-3 Structural inspection: PASS
- MT4-4 Semantic non-substitution: PASS — BOUNDED
- MT4-5 P_tau technical formalization: OPEN / BOUNDED
- MT4-6 Independent reproducibility: PASS
- MT4-7 Downstream separation: BOUNDED PASS
- MT4-8 Value isolation: BOUNDED PASS

## Consolidated finding
The candidate TGCV analytical methodology can be transferred to a genuinely heterogeneous electricity-system domain while preserving explicit separation between candidate technical constraints, realized transformations, state/trajectory variables, and economic/value-related variables.

The transfer is reproducible for the frozen structural representation. CORE6 provides a partially formalized technical admissibility candidate with 92.58 percent complete country-technology-year coverage, but full P_tau remains undetermined. Economic variables are structurally disjoint from CORE6, but no independently established downstream TGCV Delta V endpoint has been demonstrated.

## Boundaries
This result does not establish transversal causal validity, full P_tau sufficiency, Delta T_acc -> Delta V, or a general causal value mechanism. It does not promote observed adoption, installed capacity, generation, investment cost, or operating-cost parameters into accessibility or value constructs by semantic substitution.

## Research disposition
MT4 is closed as a **bounded methodological domain-transfer result**. Further work should target the unresolved analytical bottlenecks rather than repeat the completed MT4 gates: (1) independent formalization of full P_tau where feasible, and (2) a genuinely downstream, independently defined value/outcome endpoint capable of testing the accessibility-to-value layer.

## Material methodological evidence — TSTC v004 Application-Fit Demonstrator

**Case:** `TSTC — Synthetic Fixture-003 / Freeze-003`  
**Status:** `CLOSED — BOUNDED METHODOLOGICAL EVIDENCE REGISTERED`  
**Execution mode:** `TSTC_SYNTHETIC_EXECUTION_V004`  
**Fixture version:** `003`  
**Execution artifact:** `03_EXPERIMENTS/TSTC/tstc_execution_v004.py`  
**Post-execution audit:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_TSTC_POST_EXECUTION_AUDIT_002.md`  
**Evidence-to-claim propagation:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_TSTC_EVIDENCE_TO_CLAIM_PROPAGATION_001.md`  
**Execution source commit:** `bdb8477089b3b141ebf8231a9ad678cca9cbdce8`  
**Fixture manifest SHA-256:** `1ac8e7ca8c8a3e7afdc125a1d5021b386206205ec486664b362be0136e90bced`  
**Ruleset SHA-256:** `9a0c757ee8e166e991f60d898018a4ee424fae0e0e9c955458252ce7f56221c2`  
**Transformation-universe SHA-256:** `c6d4dfec24877318f466f7736f587557111d8524170f76b71e9596fe42868d3c`  
**Configuration SHA-256:** `ce274a9bc723989451b0ae2a5318efa92ccca86cf30c4403267a1c1123afaa84`  
**Output SHA-256:** `6afaffa091984b9b2e7823194b9170cfcdbef98f337d38d6f143f8c3e887bb38`  
**Environment:** Windows `10.0.26200`; Python `3.8.10`  
**Random seed:** `null`

### 1. Purpose and frozen scope
TSTC v004 is the executed form of the frozen **TGCV Application Fit — WP2 TSTC Minimum Demonstrator Specification 001**, using **Synthetic Fixtures Freeze-003** and **Execution Authorization Gate 003**. Its purpose is methodological application-fit: instantiate the TGCV translation representation reproducibly across heterogeneous synthetic domains while explicitly representing state/context, candidate transformations, admissibility, `T_acc`, transition, `Delta_T_acc` and bounded subsequent trajectory.

The demonstrator is not a scientific validation experiment, causal identification study, explanatory-superiority comparison, value/ROI test, industrial validation or deployment-readiness test. It covers **FX-C01 technical orchestration**, **FX-C03 agent/tool/permission**, and **FX-C05 resource/constraint**.

The frozen output contract requires explicit `fixture_id`, `fixture_version`, `connector_id`, `intervention_id`, `S0`, `C0`, `L_version`, `U_tau`, `T_acc_0`, transition, `S1`, `C1`, `T_acc_1`, `Delta_T_acc`, trajectory, baseline model, baseline representation, baseline reconstruction, comparison observations, limitations, non-claims and execution metadata.

### 2. Execution integrity and comparison contract
The result is `TSTC_EXECUTION_COMPLETE` under `TSTC_SYNTHETIC_EXECUTION_V004`, fixture version `003`, with the provenance hashes recorded above. The v004 execution corrected the earlier v003 output-contract deficiency. The post-execution audit PASS covers schema completeness, execution metadata, independent baseline reconstruction, all eight comparison dimensions, negative controls, controlled cross-domain propagation and trajectory/boundary checks.

The eight comparison dimensions are **(1)** transformation identities, **(2)** admissibility conditions, **(3)** state/context dependencies, **(4)** transition causing accessibility change, **(5)** cross-domain dependency, **(6)** trajectory consequence, **(7)** assumptions, and **(8)** information omitted. The conventional baseline is independently reconstructed; the three local comparisons are `EQUIVALENT_REPRESENTATION` within the frozen synthetic universes. This is representational agreement, not explanatory or predictive superiority.

### 3. Fixture-level results
**FX-C01 — technical orchestration.** Baseline: finite-state/orchestration rule model. Intervention: `trust_B: trusted → untrusted`. Result: `c01.deploy_B` closes; `c01.deploy_A` and `c01.restrict_security` remain admissible. `T_acc_1` changes through an explicit state/context-dependent admissibility rule and the bounded post-transition trajectory is restricted accordingly. Independent baseline reconstruction matches the feasible set.

**FX-C03 — agent/tool/permission.** Baseline: capability/access-control matrix plus workflow model. Intervention: `permission_repo: granted → denied`. Result: `c03.inspect_repo`, `c03.open_pr` and `c03.modify_repo` close; `c03.query_db` and `c03.complete_task` remain admissible. The record separates enabling condition, accessibility-space change and subsequent trajectory. Baseline reconstruction matches.

**FX-C05 — resource/constraint.** Baseline: finite constrained-resource feasibility model. Intervention: `grid_capacity: high → low`. Result: `c05.start_A` and `c05.start_B` close. The transition is represented as a bounded accessibility change without equating it with a downstream outcome. Baseline reconstruction matches.

### 4. Negative controls
`N-C01`, `N-C03` and `N-C05` all pass with empty `Delta_T_acc` and no opened, closed or changed transformations. `N-C01` changes `routing` while accessibility remains unchanged. Thus a context/state change is not automatically classified as an accessibility change; the admissibility predicate must change the feasible transformation set.

### 5. Controlled cross-domain paths
**C01 → C03:** the declared synthetic rule `security = restricted → permission_repo = denied` propagates the source condition into C03 and closes `c03.modify_repo`.  
**C03 → C05:** the C03 transition `c03.modify_repo` changes `repo` to `changed`; the declared rule propagates to `mobility_requirement_A = urgent` in C05 and closes `c05.redirect_A_to_B`.

Both are synthetic rule propagation, not empirical causal estimates or evidence of a universal mechanism.

### 6. Trajectory and representation checks
Each local record keeps transition, post-transition state/context, `T_acc_1` and bounded subsequent trajectory separate. Trajectories contain only transformations admissible under the post-transition space. The baseline independently reconstructs the same feasible transformation sets. `EQUIVALENT_REPRESENTATION` therefore means agreement under frozen synthetic rules; no explanatory, predictive, computational or downstream-performance superiority metric was executed.

### 7. Evidence-to-claim routing
**Primary: C16.** The experiment provides bounded methodological evidence that one frozen contract can be instantiated across three heterogeneous synthetic connector types while preserving distinctions among state/context, `U_tau`, admissibility/accessibility, `T_acc`, intervention, `Delta_T_acc`, trajectory, baseline reconstruction, cross-domain dependency, omitted information and non-claims.

**C02:** bounded qualification only; deterministic synthetic admissibility predicates and `T_acc` are explicitly represented, but general empirical accessibility is not validated.  
**C08:** bounded qualification only; accessibility change and bounded trajectory are represented, but no causal trajectory estimand is identified.  
**C11:** bounded qualification only; synthetic heterogeneity and two cross-domain paths are covered, but no transversal empirical validity is established.

Claim statuses remain **C02 = E0, C08 = H, C11 = H, C16 = H**. No TGCV Core primitive, relation, threshold or falsification criterion changes.

### 8. Scientific and interpretive boundaries
TSTC v004 does **not** establish scientific validity; empirical causality; a causal `Delta_T_acc → trajectory` estimand; `Delta_T_acc → Delta_V`; value creation; ROI; explanatory superiority; predictive superiority; real-world generality; industrial validation; or deployment readiness. Predicates and transformation universes are rule-defined and frozen; trajectories are generated within the demonstrator; cross-domain links are declared synthetic propagation rules. Negative controls validate only the frozen implementation logic, not external-world accessibility predicates.

### 9. Reproducibility and closure
The provenance fields and hashes identify the exact execution inputs, ruleset, transformation universe, configuration and output. The post-execution audit closes the execution as conformant, and the propagation record closes registration as **`CLOSED — BOUNDED METHODOLOGICAL CONTRIBUTION`**. This is closed methodological/application-fit evidence and **not authorization to reopen or repeat TSTC**.

### 10. Canonical governance effect
This v1.14 change corrects documentation completeness only. The v1.13 cumulative evidence is preserved, the TSTC material record is made autocontained, and no experiment is rerun. Canonical claim statuses, TGCV Core and RMA remain unchanged.

## Material empirical evidence — C05 EV–Grid Minimum Demonstrator v001

**Case:** `C05_EV_GRID_SYNTHETIC_MINIMUM_DEMONSTRATOR_V001`  
**Status:** `EXECUTION COMPLETE — PASS WITH METHODOLOGICAL LIMITATIONS`  
**Evidence class:** bounded synthetic application-fit / methodological evidence; not empirical causal evidence.  
**Runner:** `03_EXPERIMENTS/TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_MINIMUM_DEMONSTRATOR_V001.py`  
**Runner commit:** `e8e55f50f82b9bdf69eeca4d48deb9d23799672e`  
**SPEC_COMMIT:** `5aa2c7e20ea3f5775b2d6e60797f9be9efe10e05`  
**FIXTURE_COMMIT:** `9dd6e9b6bb8d0b7a7e686c4dc61926fc627fa8b6`  
**Execution:** `C05_EXECUTION_COMPLETE`  
**Python:** `3.8.10`  
**Platform:** `Windows-10-10.0.26200-SP0`  
**Output SHA-256:** `27025e638c05458e19a125c00d9d86d89906bc418eec5670eddec14c89e96880`  
**Preflight:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_RUNNER_PREFLIGHT_001.md`  
**Post-execution audit:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_POST_EXECUTION_AUDIT_001.md`

## 1. Purpose, research role and frozen scope

C05 is the executed EV–Grid Minimum Demonstrator for TGCV application-fit. Its purpose is to instantiate the TGCV translation chain in a compact synthetic domain while preserving the distinction among system/context state, candidate transformations, admissibility, accessible transformation space (`T_acc`), transition, post-transition state/context and bounded subsequent trajectory.

Its evidentiary role is methodological and application-fit oriented. It is not a real-world EV-grid study, causal identification experiment, value/ROI test, explanatory- or predictive-superiority comparison, generality test, industrial validation, or deployment-readiness assessment. No claim-level validation is inferred from execution completion. The synthetic nature of the domain, transformation universe, admissibility predicates, transitions and trajectory generation is part of the evidence boundary.

## 2. Frozen transformation universe and operational contract

The frozen candidate transformation universe `U_tau` contains exactly:

`accept_A`, `accept_B`, `defer`, `reduce_power`, `shift_window`, `redirect_A_to_B`, `redirect_B_to_A`, `reserve_capacity`, `release_capacity`, `v1g_discharge`, `v2g_discharge`, `reject`.

For each frozen scenario, candidate transformations are evaluated through an explicit admissibility rule and `T_acc` is the admissible subset of `U_tau`. The execution contract records initial state/context, candidate transformation universe, admissibility/accessibility results, transition identifier, post-transition state/context, `T_acc_1`, `Delta T_acc`, bounded trajectory fields, baseline fields, controls and explicit non-claims.

The analytical separation tested by the demonstrator is therefore:

`state/context → admissibility → T_acc → transition → post-transition state/context → bounded trajectory fields`.

The experiment does not treat downstream outcome or value as a substitute for accessibility.

## 3. Provenance and execution integrity

The frozen runner executed to `C05_EXECUTION_COMPLETE` under Python `3.8.10` on `Windows-10-10.0.26200-SP0`. Runner, specification and fixture provenance are pinned by the commits above. The execution output is identified by SHA-256 `27025e638c05458e19a125c00d9d86d89906bc418eec5670eddec14c89e96880`.

The preflight and post-execution audit record execution-integrity PASS, runtime-contract PASS, transition-coverage PASS, negative-control PASS and observed-accessibility-delta PASS. These are execution/audit classifications within the frozen demonstrator and do not constitute broader scientific validity.

## 4. Scenario coverage and quantitative findings

The frozen execution contains scenarios `T1`–`T6` plus negative controls `NC1` and `NC2`. The material positive result is concentrated in T3.

Under **T3**:

- `|T_acc,0| = 8`;
- `|T_acc,1| = 6`;
- `Delta |T_acc| = -2`;
- closed transformations: `accept_B` and `redirect_A_to_B`.

Under **T1, T2, T4, T5 and T6**, the frozen execution reports no accessibility delta. The same absence of an accessibility delta is reported for **NC1 and NC2**.

Thus the demonstrator does not classify every represented state/context change as an accessibility-space change. The observed delta depends on the frozen admissibility structure.

## 5. Interpretation of the result

The T3 result concerns the identity and cardinality of the accessible candidate-transformation space, not downstream operational outcomes. Closing `accept_B` and `redirect_A_to_B` is evidence of a bounded synthetic `T_acc` change. It is not evidence that an EV-grid intervention caused a real-world reliability, mobility, energy, economic or value outcome.

The principal methodological contribution is the executable preservation of distinctions among `U_tau`, admissibility, `T_acc`, transition, post-transition state/context and bounded trajectory fields.

## 6. Baseline reconstruction limitation

The frozen implementation defines `baseline(s,c,l)` by returning `admissible(s,c,l)`. Consequently `baseline_equivalent=true` is an implementation identity, not an independently constructed baseline model.

It cannot be counted as independent baseline evidence and cannot support independent validation, explanatory superiority, predictive superiority or comparative advantage. The baseline comparison establishes consistency with the same admissibility implementation rather than an independent comparator.

## 7. Negative controls and trajectory-policy limitation

`NC1` and `NC2` show no accessibility delta in the frozen execution. `NC2` specifies `selection_tiebreak=reverse_lexical`, but the frozen `trajectory()` implementation does **not consume that field**.

Consequently NC2 is **not** a valid trajectory-policy sensitivity test. It is only a negative-control execution under the frozen implementation. C05 therefore does not establish trajectory-policy robustness, sensitivity of trajectory conclusions to selection policy, a causal `Delta T_acc -> trajectory` estimand, or any downstream causal trajectory effect.

## 8. Evidence-to-claim propagation

**C02 — bounded qualification.** C05 supplies synthetic application-fit evidence that explicit candidate transformations, admissibility/accessibility and `T_acc` can be represented and executed, including the T3 reduction from 8 to 6. It does not establish general empirical accessibility or an independently validated admissibility predicate.

**C07 — bounded qualification.** C05 supplies synthetic evidence that `T_acc` can change between frozen states/contexts, specifically 8→6 under T3, with `accept_B` and `redirect_A_to_B` closing. It does not establish temporal change of accessible transformation spaces in real systems.

**C08 — bounded qualification.** C05 represents transition, post-transition accessibility and bounded trajectory fields. Because the demonstrator is synthetic and NC2 is not a genuine trajectory-policy sensitivity test, it does not establish a causal `Delta T_acc -> trajectory` estimand.

**C16 — bounded methodological contribution.** C05 preserves an executable distinction among candidate transformations, admissibility, `T_acc`, transition, bounded trajectory, controls and explicit non-claims in an EV-grid application-fit domain. It strengthens the translation-protocol evidence without establishing transversal validity.

No propagation is made to C01, C03, C04, C05, C06, C09, C10, C11, C12, C13, C14 or C15. No claim-level status or level is changed.

## 9. Scientific boundaries and explicit non-claims

C05 does **not** establish empirical causality, generality, transversal validity, value creation, ROI, downstream operational performance, explanatory superiority, predictive superiority, real-world EV-grid validity, industrial validation, deployment readiness, or a causal `Delta T_acc -> Delta V` pathway.

It does not independently validate the baseline because the baseline implementation is identical to the admissibility function. It does not establish trajectory-policy robustness because `selection_tiebreak` is not consumed by `trajectory()`. It does not establish that the synthetic admissibility predicates correspond to an independently identified real-world EV-grid mechanism.

## 10. Governance disposition and closure

C05 is closed as **bounded synthetic methodological/application-fit evidence**. Its material result is retained because it qualifies the evidentiary basis of C02, C07, C08 and C16 without warranting a claim-level upgrade. No completed C05 gate is reopened by this enrichment, and no Core/RMA modification follows.

**Claim routing:** `C02`, `C07`, `C08`, `C16` only.

## 11. GL-07 disposition

This file is the developed material expediente for C05 and is intended to support restoration of the full autocontained C05 section in the cumulative Evidence-to-Claim Matrix. The matrix section itself remains the canonical routing/index layer and must contain the developed evidence, not merely a reference to this file, under persistent GL-07.


## Material methodological evidence — VSL Synthetic Minimum v0.1

**Case:** `VSL_SYNTHETIC_MIN_v0.1`  
**Status:** `CLOSED — BOUNDED METHODOLOGICAL EVIDENCE`  
**Evidence class:** synthetic methodological / implementation evidence; not empirical causal evidence.  
**Specification:** `00_GOVERNANCE/SIP/TGCV_VSL_SYNTHETIC_MIN_v0.1_SPECIFICATION.md`  
**Outcome definition:** `00_GOVERNANCE/SIP/TGCV_VSL_SYNTHETIC_MIN_OUTCOME_DEFINITION_v0.1.md`  
**Freeze record:** `00_GOVERNANCE/SIP/TGCV_VSL_SYNTHETIC_MIN_v0.1_FREEZE_RECORD_001.md`  
**Fixture:** `03_EXPERIMENTS/VSL_SYNTHETIC_MIN_V001/vsl_synthetic_min_fixture_v01.py`  
**Runner:** `03_EXPERIMENTS/VSL_SYNTHETIC_MIN_V001/vsl_synthetic_min_runner_v01.py`  
**Runner commit:** `617646497518dba30c0ba721d4bdd24823c0e2ea`  
**Runner blob:** `eebade9075aa286f22249015443397fb83d069bf`  
**Fixture runtime audit:** `TGCV_VSL_SYNTHETIC_MIN_FIXTURE_RUNTIME_AUDIT_001.md`  
**Runner runtime audit:** `TGCV_VSL_SYNTHETIC_MIN_RUNNER_RUNTIME_AUDIT_001.md`  
**Source/runtime integrity audit:** `TGCV_VSL_SYNTHETIC_MIN_RUNNER_SOURCE_RUNTIME_INTEGRITY_AUDIT_001.md`  

### 1. Purpose and frozen scope
The experiment is a deliberately artificial minimum demonstration of an external Value Specification Layer (VSL). Its purpose is to test whether an outcome-to-Value mapping can be frozen and executed without allowing the valuation functions to inspect accessibility, treatment, selected transformation or transformation identity. It is not a real-world valuation study and does not establish a universal definition of Value.

The frozen architecture is:

`C → T_acc → selection → τ → S' → O → V*`

with the VSL restricted to the downstream path `S' → O → V*` and external to the TGCV transformational core.

### 2. Operational valuation contract
The synthetic state is `S=(q,r)`, with baseline `S0=(10,10)`. The frozen outcome is `O(S)=q+0.5r`, so `O0=15`. Value is defined as `V*=O`, hence `Delta V*=Delta O`. The outcome function receives only the final state; the Value function receives only the outcome.

The valuation objective, direction, reference frame and mapping are artificial, versioned and frozen before execution. The construct is explicitly domain-bounded to the synthetic system.

### 3. Fixture and runner controls
The fixture runtime validated T1, T2, T3, T4, NC1 and NC2. The corrected runner preflight passed after T4 was changed to generate its final state through `apply_exogenous_factor(S0, 2)` rather than a parallel hard-coded final state. The runner then executed successfully with all six cases and no assertion failure.

### 4. Quantitative runtime findings

| Case | Accessibility changed | Selected transform | Final state | ΔO | ΔV* | Exogenous factor |
|---|---:|---|---|---:|---:|---:|
| T1 | False | A | (10,10) | 0 | 0 | 0 |
| T2 | True | A | (10,10) | 0 | 0 | 0 |
| T3 | True | B | (14,10) | +4 | +4 | 0 |
| T4 | False | A | (12,10) | +2 | +2 | 2 |
| NC1 | False | A | (10,10) | 0 | 0 | 0 |
| NC2 | True | A | (10,10) | 0 | 0 | 0 |

T2 provides the required accessibility-change/zero-Value contrast. T3 realizes the specified synthetic accessibility/selection/value pathway. T4 provides a non-accessibility exogenous outcome/value change. NC1 and NC2 remain zero-effect controls.

### 5. Source/runtime separation
Source inspection confirms that `outcome(state)` receives only `State(q,r)`, while `value(outcome_value)` receives only the outcome. Neither function receives accessibility, treatment, case identifier, selected transformation, exogenous factor or transformation identity. Accessibility, selection and state transition are generated upstream. The source/runtime audit confirms correspondence between this source structure and the supplied runtime output.

### 6. Interpretation
The result demonstrates a bounded implementation property: a synthetic VSL can be specified and executed as an external downstream valuation layer without direct computational access to the accessibility/transformation variables. This is methodological evidence about separation and operational reproducibility.

The T3 result is **not** an independent causal estimate of accessibility on Value. The synthetic runner deliberately encodes the transformation/accessibility pathway, so the execution cannot establish empirical causal validity.

### 7. Evidence-to-claim routing
**C16 — bounded methodological contribution.** The result extends the translation protocol to preserve an explicit downstream Outcome/Value distinction and an external VSL interface. It demonstrates implementation-level separation without establishing transversal empirical validity or a causal value pathway.

No routing is added to C02, C07, C08, C09 or C10. The experiment does not test accessibility, Reach or trajectory causality as its primary endpoint. No TGCV Core primitive or relation changes.

### 8. Reproducibility and boundaries
The specification, outcome definition, freeze record, fixture, runner and audits are versioned in the canonical repository. Runtime evidence is the supplied controlled local execution under the corrected runner. The result is synthetic and domain-bounded. No real-world population, empirical valuation objective, monetary interpretation, ROI or cross-domain Value comparability is claimed.

### 9. Governance disposition
The VSL Synthetic Minimum v0.1 is closed as **bounded methodological evidence**. Its propagation to C10 and C16 changes the evidentiary basis by adding an implementation-level demonstration of external valuation-layer separation, but **does not change claim status or level**. C09, TGCV Core and RMA remain unchanged.

### 10. GL-07 completeness
This section is the autocontained material expediente for the VSL Synthetic Minimum result. It contains identity/status, purpose and frozen scope, provenance, operational contract, methods and controls, quantitative findings, interpretation, observation-versus-inference boundaries, evidence-to-claim routing and governance disposition. External artifacts supplement rather than replace this record.
