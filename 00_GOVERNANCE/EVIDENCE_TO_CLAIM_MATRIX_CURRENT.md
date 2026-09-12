# TGCV — Evidence-to-Claim Matrix — Current v1.2

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT  
**Date:** 2026-09-12  
**Predecessor:** v1.1  
**Current update:** Material evidence propagation for SWIM Reactive-0, Reactive2 and bounded SWIM trajectory-linkage reconstruction. No scientific claim status/level upgrade.

## Material evidence propagation rule
A material experimental result is propagated to this matrix when it adds, removes, qualifies, bounds, or otherwise changes the evidentiary basis or interpretation of a claim, even when no claim status/level changes. Claim upgrade is a separate decision and is never inferred merely from evidence propagation.

**Operational rule:** Evidence propagation does not imply claim upgrade.

| ID | Claim | Status | Current evidence / basis | Evidence impact / interpretation | Next requirement |
|---|---|---|---|---|---|
| C01 | TGCV represents system state/context/conditions and constraints/resources | E0 | Formal architecture + bounded cross-domain traces | SWIM Reactive-0 adds a bounded self-adaptive-system operationalization of state/context reconstruction; no claim-level upgrade. | Further independent operational confirmation |
| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Formalization + Rust + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 | SWIM Reactive-0 provides bounded reconstruction of `Pτ(S_t,C_t)` and `T_acc,t`; Reactive2 additionally provides bounded evidence that candidate identity and accessibility can remain analytically separated from native policy selection. This strengthens bounded operational support while general `T_acc` remains unclosed. | Independent operationalization across a distinct exemplar |
| C03 | T_acc is analytically distinct from downstream Reach in bounded Rust | E1 | Rust evidence | SWIM does not alter the bounded Rust claim level; it independently instantiates the accessibility object without establishing the Rust claim more generally. | Independent replication |
| C04 | ΔT_acc can occur without ΔReach¹_pot | E1 | Rust ND-1 | SWIM demonstrates bounded `ΔT_acc` but does not test the specific Reach-separation condition. | Independent replication |
| C05 | ΔT_acc can occur with ΔReach¹_pot change | E1 | Rust ND-2 | SWIM demonstrates bounded `ΔT_acc` but does not test the specific Reach-separation condition. | Independent replication |
| C06 | Reach identity is not characterized by cardinality alone | E1 | Rust ND-4 | No material impact. | Independent replication |
| C07 | Accessible transformation spaces change over time in Rust | E1 | Rust non-persistent pairs | SWIM provides bounded non-Rust operational evidence that accessible transformation spaces can change across observed state transitions. This does not upgrade the Rust-specific claim. | Independent closed operationalization / replication |
| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded Rust H=1 + SWIM Reactive-0 trajectory-linkage reconstruction | SWIM now adds material bounded evidence that reconstructed `ΔT_acc` can be followed by a distinguishable ordered sequence of selected transformations and state transitions. This is a bounded observed association/reconstructability result, not general trajectory modification proof and not causal identification. | Independent valid trajectory test with explicit trajectory criterion beyond the bounded exemplar |
| C09 | Accessibility changes causally affect subsequent trajectories | H | No causal identification | No causal evidence from SWIM Reactive-0, Reactive2 or trajectory-linkage reconstruction. The linkage result is explicitly non-causal. | Causal design |
| C10 | Accessibility changes generate/predict value | H | No Value evidence | SWIM is methodological/reconstructive evidence only; no value realization or predictive-value claim is established. | Value-linked test |
| C11 | TGCV is domain-independent / transversal | H | C-01 A-C + I-01 Gate C | SWIM is one bounded self-adaptive software exemplar and therefore strengthens cross-context evidence only at the methodological level; transversal validity remains unestablished. | Independent operationalization across broader domains |
| C12 | TGCV provides superior explanatory representation | H | Comparative evidence absent | SWIM Reactive-0/Reactive2 are non-comparative for explanatory superiority. | Controlled differentiated comparison |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21 | No material impact. | Comparative coverage |
| C14 | T_acc is an ontological primitive independent of S | F | TR-131 | No impact; SWIM treats `T_acc` as derived from state/context and admissibility. | No restoration without contrary evidence |
| C15 | Rust demonstrates observed Cargo/runtime reachability | F | Rust evidence boundary | No impact. | Separate governed runtime test |
| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22/23 + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 + SWIM Reactive-0 + SWIM Reactive2 + SWIM trajectory-linkage reconstruction | SWIM Reactive-0 adds a bounded operationalization of the state/context → accessibility → `T_acc` → `ΔT_acc` segment; the trajectory-linkage reconstruction additionally supports the bounded `ΔT_acc → selected transformation/state trajectory` segment. Reactive2 adds bounded methodological evidence that candidate identity, accessibility and native policy selection can be represented as distinct analytical layers. It does not close downstream value boundaries or establish transversal validity. | Closed independent-domain operationalization / downstream test |

## Material methodological evidence — SWIM Reactive-0

**Case:** `SWIM Reactive-0`  
**Run:** `Reactive-0-20260911-17:49:20-1`  
**Status:** `CLOSED — BOUNDED TGCV OPERATIONALIZATION RESULT`  
**Disposition:** `00_GOVERNANCE/SIP/TGCV_SWIM_REACTIVE0_OPERATIONALIZATION_DISPOSITION_001.md`

The frozen SWIM Reactive-0 execution completed successfully with a reproducible `.sca/.vec` result bundle. Existing run evidence and deterministic source semantics were used to reconstruct candidate transformation identities, pre-outcome accessibility predicates, multiple accessible-transformation snapshots and observed changes in that space.

Bounded candidate universe:

`Uτ = {AddServer, RemoveServer, SetDimmer(k)}`

with only observed dimmer targets represented in the bounded reconstruction.

The reconstruction yielded multiple `T_acc,t` snapshots and non-empty `ΔT_acc` transitions, including:

- `t=600 → 660`: `AddServer` enters `T_acc`;
- `t=660 → 3960`: `RemoveServer` leaves `T_acc`;
- `t=3960 → 4680`: `RemoveServer` re-enters `T_acc`;
- `t=4680 → 4740`: `AddServer` leaves `T_acc` at `maxServers=3`.

This is material evidence because it operationalizes the bounded chain:

`S_t,C_t → Pτ(S_t,C_t) → T_acc,t → ΔT_acc`

without using downstream outcome to define accessibility.

### Interpretation boundary

The result supports bounded operational reconstructability of accessible transformation space and its change over time in this SWIM exemplar.

It does **not** establish:

- transversal novelty;
- causal effects on trajectories;
- value creation or prediction;
- explanatory superiority;
- general validity across self-adaptive systems;
- industrial utility or production benefit.

No additional Reactive-0 simulation is required for the present bounded operationalization claim.

## Material methodological evidence — SWIM trajectory linkage

**Case:** `SWIM Reactive-0 — bounded trajectory-linkage reconstruction`  
**Status:** `CLOSED — BOUNDED TRAJECTORY-LINKAGE RECONSTRUCTION`  
**Disposition:** `00_GOVERNANCE/SIP/TGCV_SWIM_TRAJECTORY_LINKAGE_DISPOSITION_001.md`  
**Matrix reconciliation:** `00_GOVERNANCE/SIP/TGCV_SWIM_TRAJECTORY_LINKAGE_MATRIX_RECONCILIATION_001.md`

Existing Reactive-0 evidence was further reconstructed without new execution to test whether already established accessibility-space changes could be followed by distinguishable bounded trajectories of selected transformations and system-state transitions.

The result establishes the bounded analytical linkage:

`S_t,C_t → Pτ(S_t,C_t) → T_acc,t → ΔT_acc,t → selected τ_t → S_{t+1},C_{t+1} → bounded subsequent trajectory`

At the recorded accessibility transitions, the evidence permits reconstruction of ordered subsequent selected transformations and state transitions. The result is therefore material bounded evidence for trajectory linkage/reconstructability.

### Interpretation boundary

This result is an observed association/reconstructability result. It does **not** establish:

- that `ΔT_acc` causes the subsequent trajectory;
- general modification of all reachable future trajectories;
- counterfactual trajectory differences;
- value creation or prediction;
- explanatory superiority;
- transversal validity;
- industrial utility.

No additional Reactive-0 simulation is required for this bounded reconstruction.

## Material methodological evidence — SWIM Reactive2

**Case:** `SWIM Reactive2`  
**Run:** `Reactive2-0`  
**Status:** `CLOSED — BOUNDED METHODOLOGICAL EVIDENCE; A8 NOT_COMPARABLE`  
**Disposition:** `00_GOVERNANCE/SIP/TGCV_SWIM_REACTIVE2_POLICY_INDEPENDENCE_GATE_DISPOSITION_001.md`  
**Matrix reconciliation:** `00_GOVERNANCE/SIP/TGCV_SWIM_REACTIVE2_MATRIX_RECONCILIATION_001.md`

Reactive2 completed under the authorized Run-0 scope using the same frozen SWIM infrastructure and inputs. The evidence supports a bounded separation between:

`candidate identity → pre-outcome accessibility → T_acc → native policy selection → execution`

for the observed candidate families `{AddServer, RemoveServer, SetDimmer(k)}`.

The result is material because it adds a methodological qualification not established by Reactive-0 alone: the native adaptation-manager policy can change the selected action sequence while the candidate/accessibility representation remains analytically separable from that downstream policy-selection step at the inspected points.

### Comparability boundary

Criterion A8 is `NOT_COMPARABLE`. Timestamp coincidence and partial vector-state coincidence are insufficient to establish identical predecision `(S_t,C_t)` because zero-latency/event-ordering effects and differing preceding adaptation histories can make same-timestamp observations represent different transition positions.

Therefore Reactive2 does **not** establish policy-independent accessibility under an identical matched state/context with Reactive-0.

### Interpretation boundary

Reactive2 provides bounded methodological support for the analytical separation of accessibility from native policy selection. It does **not** establish:

- general policy-independent accessibility across self-adaptive systems;
- identical accessibility predicates across Reactive-0 and Reactive2 at matched state/context;
- downstream trajectory effects;
- causal effects;
- value creation or prediction;
- explanatory superiority;
- transversal validity;
- industrial utility or production benefit.

No additional Reactive2 execution is required under the closed gate. A future comparative test would require a new falsifiable question and explicit control of predecision state/context equivalence rather than timestamp matching.

## Claim boundary

No C01–C16 status is upgraded by the material evidence recorded in v1.2. The SWIM results strengthen the bounded evidentiary basis for C01, C02, C07 and C16; Reactive2 specifically adds bounded methodological evidence relevant to C02 and C16. The trajectory-linkage reconstruction adds material bounded evidence relevant to C08 and the `ΔT_acc → trajectory` segment of C16. These are material evidence records, not claim upgrades. The scientific Core remains unchanged.

## Gate state

- G1 Independent replication: OPEN at general scientific level; bounded fixture/event closures remain separately recorded.
- G2 Cross-domain generalisation: BOUNDED / PARTIAL.
- G3 Trajectory sufficiency: OPEN; bounded trajectory-linkage reconstruction is recorded but does not close the general gate.
- G4 Causal identification: OPEN.
- G5 Value linkage: OPEN.
- G6 Originality/comparative architecture: BOUNDED / PARTIAL.
- G7 Transversal translation protocol: BOUNDED operational support strengthened by SWIM, including bounded trajectory linkage; general/transversal closure remains OPEN.

## Current methodological routing

- IUT-A-01 U2 FULL_PILOT 001: `CLOSED — U2-NULL`; no rerun.
- IT-NOSD-010: G0/G1/G2 closed for one bounded frozen event; industrial execution authorization `NONE`.
- EXT-UPD-4.8 O3 accessibility closure: `CLOSED — INDETERMINATE / H-B / HS-AC01`; no reopening or additional attempt under this closure.
- AWS Phase-A/B0 work remains fixture-level; no candidate/comparator transformation is authorized.
- SWIM Reactive-0: `CLOSED — BOUNDED TGCV OPERATIONALIZATION RESULT`; no repeat run for the current claim.
- SWIM trajectory linkage: `CLOSED — BOUNDED TRAJECTORY-LINKAGE RECONSTRUCTION`; no repeat run for the current bounded reconstruction.
- SWIM Reactive2: `CLOSED — BOUNDED METHODOLOGICAL EVIDENCE; A8 NOT_COMPARABLE`; no additional execution under the current gate.
- Utility scoring and industrial case admission: `NOT AUTHORIZED`.

## Current scientific position

The evidence base now includes bounded comparative methodological evidence from IUT-A-01 U2, bounded downstream-separation/reconstructability evidence from IT-NOSD-010, bounded accessibility-closure boundary evidence from EXT-UPD-4.8, Class-II AWS fixture evidence, bounded self-adaptive software operationalization from SWIM Reactive-0 and Reactive2, and bounded SWIM trajectory-linkage reconstruction. These are material evidence records, not claim upgrades. The scientific Core remains unchanged.
