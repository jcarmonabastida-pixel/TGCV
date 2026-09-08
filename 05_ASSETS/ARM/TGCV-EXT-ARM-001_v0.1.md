# TGCV — Architectural Research Map (ARM) v0.1

**Asset ID:** TGCV-EXT-ARM-001  
**Status:** CURRENT-DRAFT / CONTROLLED  
**Canonical location:** `05_ASSETS/ARM/`  
**Date:** 2026-09-09  

## 1. Purpose

The Architectural Research Map (ARM) provides a controlled map of the TGCV scientific architecture, its analytical layers, evidence boundaries, dependencies and open research operations.

It is an architectural control artifact. It does not introduce a new scientific claim, empirical result, or ontological primitive.

## 2. Current scientific core

The current ontological Core is:

`Core_ontological = S`

where `S` denotes the system/domain state relevant to the transformations under analysis.

The accessible transformation space is an analytical representation derived from state and contextual conditions:

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`

The central dynamic quantity is the change in membership of this accessible space:

`ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`

The distinction is deliberate: `T_acc` is analytically indispensable for studying accessibility changes, while TR-131 established that it is not ontologically independent of `S`.

## 3. Role of mechanisms and interaction

Mechanisms explain how a system state and its contextual conditions change. Interaction `I` is therefore treated as an explanatory mechanism variable and not as a Core primitive.

The controlled analytical chain is:

`mechanism → (S,C) → (S’,C’) → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

The downstream elements are analytical layers, not automatically established causal consequences.

## 4. Architectural layers

### Layer A — Ontological state

- `S`: minimal ontological state.
- Current scientific decision: no independent primitive `I`.

### Layer B — Accessible transformations

- `T_acc`: transformations accessible under the relevant state/context/constraint conditions.
- `ΔT_acc`: change in accessible transformation membership.
- This is the primary analytical focus of TGCV.

### Layer C — Reach and trajectory

- `Reach`: transformations or states reachable through subsequent admissible transitions.
- `Trajectory`: ordered downstream development through time.
- These remain analytically downstream from accessibility change.

### Layer D — Outcome and value

- `Outcome`: observed subsequent result.
- `Value`: value attributable only under an appropriate additional analytical and evidentiary argument.
- No current evidence permits treating `ΔT_acc` as sufficient for value creation.

### Layer E — Cross-domain translation

The translation architecture asks whether the same minimal analytical distinction can be represented in another domain without importing domain-specific semantics into the TGCV Core.

D-OPS-21 identified high local redundancy and weakened broad novelty claims. D-OPS-22 established bounded translational non-redundancy, without proving superiority. D-OPS-23 froze the minimal transversal translation protocol.

## 5. Evidence architecture

### Established

- TGCV Core is currently represented minimally as `S`.
- `T_acc` is analytically central but ontologically state-dependent.
- Interaction `I` is explanatory rather than Core-primitive.
- TR-131 is closed.
- The current cross-domain translation protocol is frozen at D-OPS-23.

### Bounded empirical evidence

RUST-DYN-1 and RUST-DYN-2 provide bounded structural evidence from the Rust ecosystem concerning temporal non-persistence and changes in observed package-level structures. RUST-DYN-2 contains 516,061 adjacent temporal pairs, of which 438,203 are non-persistent (~84.91%).

This evidence does not by itself establish causal efficacy, prediction, value creation, universal validity, runtime Cargo reachability, or second-domain validation.

### Hypotheses / open questions

The remaining programme must test whether the analytical architecture is operationally identifiable, non-redundant and transferable beyond the currently bounded evidence surface, and whether downstream relations can be established without circularity.

## 6. Research/gate map

The current programme state is controlled by the RMA and associated decision/gate records. D-OPS-15 through D-OPS-23 are closed bounded discovery, rejection, bridge and translation operations. D-OPS-24 is the next controlled operation.

D-OPS-24 is **not authorized by the existence of this ARM**. Its own historical reconstruction, design, preflight and explicit authorization remain mandatory.

## 7. Claim boundary

ARM v0.1 must not be read as evidence for any of the following:

- causal efficacy of `ΔT_acc`;
- predictive validity;
- demonstrated value creation;
- universal domain independence;
- runtime reachability in Cargo;
- validation in a second independent domain;
- broad scientific originality or superiority.

No epistemic status is upgraded by publication of this document.

## 8. Governance dependencies

ARM v0.1 is subordinate to the current RMA. Any future substantive change to the Core, evidence status, gate status or external-asset architecture requires the mandatory propagation sequence:

`Decision/Gate/Closure → Impact analysis → RMA current master → current dependent assets → STATUS → Evidence-to-Claim Matrix → consistency audit → next gate`

Historical ARM states, if created in future, shall remain immutable.

## 9. Current position

ARM v0.1 is the first substantive canonical ARM artifact. It records the current architecture without claiming more than the present evidence supports.

**Next controlled operation:** propagation of ARM v0.1 through the RMA governance surfaces, followed by consistency closure. RII remains pending after ARM closure.