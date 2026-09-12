# TGCV — Evidence-to-Claim Matrix — Current v1.3

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT  
**Date:** 2026-09-12  
**Predecessor:** v1.2  
**Current update:** Material evidence propagation for closed IT-G1 `AWSSupport-ExecuteEC2Rescue`. No scientific claim status/level upgrade.

## Matrix preservation rule
This matrix is cumulative. Every new version MUST preserve the full evidentiary content and schema of its predecessor and add, qualify, bound, supersede, or explicitly retire information. A version MUST NOT silently reduce the number of claim-matrix columns, remove material evidence descriptions, collapse evidence basis into summary-only fields, or replace detailed evidence records with a short status table.

`EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` is a stable alias of the complete versioned current matrix; it MUST NOT be a simplified derivative.

## Material evidence propagation rule
A material experimental result is propagated to this matrix when it adds, removes, qualifies, bounds, or otherwise changes the evidentiary basis or interpretation of a claim, even when no claim status/level changes. Claim upgrade is a separate decision and is never inferred merely from evidence propagation.

**Operational rule:** Evidence propagation does not imply claim upgrade.

## Current claim matrix

| ID | Claim | Status | Current evidence / basis | Evidence impact / interpretation | Next requirement |
|---|---|---|---|---|---|
| C01 | TGCV represents system state/context/conditions and constraints/resources | E0 | Formal architecture + bounded cross-domain traces + IT-G1 bounded industrial case | IT-G1 adds material bounded evidence for reconstruction of internal state and external enabling conditions; no claim-level upgrade. | Further independent operational confirmation |
| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Formalization + Rust + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 + IT-G1 | SWIM provides bounded accessibility operationalization; IT-G1 adds bounded evidence that end-to-end accessibility/function can depend on conditions external to the internal remediation target. General `T_acc` remains unclosed. | Independent operationalization across a distinct exemplar |
| C03 | T_acc is analytically distinct from downstream Reach in bounded Rust | E1 | Rust evidence | SWIM does not alter the bounded Rust claim level; IT-G1 does not test the Rust-specific Reach separation. | Independent replication |
| C04 | ΔT_acc can occur without ΔReach¹_pot | E1 | Rust ND-1 | No direct test by SWIM or IT-G1. | Independent replication |
| C05 | ΔT_acc can occur with ΔReach¹_pot change | E1 | Rust ND-2 | No direct test by SWIM or IT-G1. | Independent replication |
| C06 | Reach identity is not characterized by cardinality alone | E1 | Rust ND-4 | No material impact. | Independent replication |
| C07 | Accessible transformation spaces change over time in Rust | E1 | Rust non-persistent pairs + bounded SWIM operationalization | SWIM provides bounded non-Rust evidence that accessible transformation spaces can change across observed state transitions; IT-G1 adds a bounded industrial state-transformation sequence but does not upgrade the Rust-specific claim. | Independent closed operationalization / replication |
| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded Rust H=1 + SWIM trajectory-linkage reconstruction + IT-G1 bounded state/trajectory observation | SWIM adds bounded reconstructability of ordered subsequent transformations and state transitions; IT-G1 provides a bounded industrial state/trajectory observation. Neither establishes causal trajectory modification or a general trajectory claim. | Independent valid trajectory test with explicit trajectory criterion beyond bounded exemplars |
| C09 | Accessibility changes causally affect subsequent trajectories | H | No causal identification | Neither SWIM nor IT-G1 establishes causality. IT-G1 explicitly preserves the distinction between internal remediation, external enabling condition and end-to-end outcome. | Causal design |
| C10 | Accessibility changes generate/predict value | H | No Value evidence | SWIM and IT-G1 are methodological/reconstructive evidence only; no value realization or predictive-value claim is established. | Value-linked test |
| C11 | TGCV is domain-independent / transversal | H | C-01 A-C + I-01 Gate C + bounded cross-domain evidence | SWIM is a bounded self-adaptive software exemplar and IT-G1 a bounded industrial AWS exemplar; transversal validity remains unestablished. | Independent operationalization across broader domains |
| C12 | TGCV provides superior explanatory representation | H | Comparative evidence absent | IUT M1 provides bounded decision-performance evidence but U2-NULL; SWIM and IT-G1 are non-comparative for explanatory superiority. | Controlled differentiated comparison |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21 | No material impact. | Comparative coverage |
| C14 | T_acc is an ontological primitive independent of S | F | TR-131 | No impact; SWIM and IT-G1 treat accessibility as derived/conditioned rather than restoring the rejected primitive. | No restoration without contrary evidence |
| C15 | Rust demonstrates observed Cargo/runtime reachability | F | Rust evidence boundary | No impact. | Separate governed runtime test |
| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22/23 + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 + SWIM trajectory-linkage reconstruction + IT-G1 | SWIM supports bounded state/context → accessibility → `T_acc` → `ΔT_acc` and bounded trajectory linkage. IT-G1 adds bounded industrial evidence preserving distinctions among internal state transformation, external enabling condition and end-to-end outcome. It does not close downstream value boundaries or establish transversal validity. | Closed independent-domain operationalization / downstream test |

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

## Claim boundary

The v1.3 update is additive. It preserves the full evidence/claim structure of v1.2 and adds IT-G1 as material bounded industrial evidence. No C01–C16 status is upgraded. Material evidence propagation remains distinct from scientific claim upgrade. The TGCV Core remains unchanged.

## Gate state

- G1 Independent replication: OPEN at general scientific level; bounded fixture/event closures remain separately recorded.
- G2 Cross-domain generalisation: BOUNDED / PARTIAL.
- G3 Trajectory sufficiency: OPEN; bounded trajectory-linkage and IT-G1 state-transition observations do not close the general gate.
- G4 Causal identification: OPEN.
- G5 Value linkage: OPEN.
- G6 Originality/comparative architecture: BOUNDED / PARTIAL.
- G7 Transversal translation protocol: BOUNDED operational support; general/transversal closure remains OPEN.

## Current methodological routing

- IUT-A-01 U2 FULL_PILOT 001: `CLOSED — U2-NULL`; no rerun.
- IT-NOSD-010: G0/G1/G2 closed for one bounded frozen event; industrial execution authorization `NONE`.
- EXT-UPD-4.8 O3 accessibility closure: `CLOSED — INDETERMINATE / H-B / HS-AC01`; no reopening or additional attempt under this closure.
- Class-II AWS-PatchAsgInstance: fixture-level closure as previously governed.
- SWIM Reactive-0: `CLOSED — BOUNDED TGCV OPERATIONALIZATION RESULT`; no repeat run for current claim.
- SWIM trajectory linkage: `CLOSED — BOUNDED TRAJECTORY-LINKAGE RECONSTRUCTION`; no repeat run for current bounded reconstruction.
- SWIM Reactive2: `CLOSED — BOUNDED METHODOLOGICAL EVIDENCE; A8 NOT_COMPARABLE`; no additional execution under current gate.
- IT-G1 `AWSSupport-ExecuteEC2Rescue`: `CLOSED — FUNCTIONAL RECOVERY DEMONSTRATED`; no rerun implied.
- IT-METH-I FAA AMOC: `CLOSED — INCONCLUSIVE`.
- Utility scoring and new industrial execution: `NOT AUTHORIZED`.

## Current scientific position

The evidence base includes bounded comparative methodological evidence from IUT-A-01 U2, bounded downstream-separation/reconstructability evidence from IT-NOSD-010, bounded accessibility-closure boundary evidence from EXT-UPD-4.8, Class-II AWS fixture evidence, bounded self-adaptive software operationalization from SWIM Reactive-0 and Reactive2, bounded SWIM trajectory-linkage reconstruction, and the closed IT-G1 industrial case. These are cumulative material evidence records, not claim upgrades. The scientific Core remains unchanged.
