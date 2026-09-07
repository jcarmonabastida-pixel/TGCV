# SLR-1 Source Dossier — SRC-DAS-001

**Status:** RECONSTRUCTED / WORKING
**Sources:** Chandak, Y., Theocharous, G., Kostas, J., & Thomas, P. (2018), *Reinforcement Learning with a Dynamic Action Set*, NeurIPS 2018 Continual Learning Workshop; and Chandak, Y., Theocharous, G., Nota, C., & Thomas, P. S. (2019), *Lifelong Learning with a Changing Action Set*, arXiv:1906.01770.
**Classification:** **AC2 — DIRECT STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Why this source is decisive

This is the first screened candidate in the current search front that explicitly treats the **action set itself as a changing object**. The authors state that many sequential decision problems have a set of possible actions that changes over time and develop methods that adapt to a dynamic/changing action set.

## Key evidence

The 2018 source states that reinforcement learning traditionally assumes a fixed set of possible actions, whereas real-world settings can have a set of possible actions that changes over time. The method therefore adapts to a dynamic action set. citeturn1search0

The 2019 version explicitly frames the problem as lifelong learning with a changing action set: the number of available actions can vary over time, and the action-set change is treated as a distinct problem from changing transition dynamics or rewards. citeturn1academia42

## TGCV mapping

| TGCV element | Dynamic-action-set analogue | Assessment |
|---|---|---|
| `S` | decision/environment state | strong analogue |
| `T_acc` | currently available action set | **direct analogue at the action level** |
| accessibility predicate | membership in the current action set | explicit operational analogue |
| `ΔT_acc` | addition/removal/change of available actions over time | **explicitly represented** |
| `Reach` | consequences of choosing available actions | partial |
| `Trajectory` | sequential decision process | explicit |
| `Outcome` | task/environment outcome | explicit in RL setting |
| `Value` | reward / policy performance | partial, not TGCV value construction |
| mechanism | environmental/task change causing action-set change | present, but not generalized as a transversal mechanism variable |

## AC2 assessment

**AC2 — DIRECT STRUCTURAL ANTECEDENT CONFIRMED.**

The source establishes the following architecture explicitly:

`changing environment/problem → changing available action set → policy adaptation → sequential outcomes`.

This is extremely close to the empirical core of the TGCV intuition that the set of currently accessible operations can change over time.

The source therefore **absorbs the broad originality claim that a changing set of available actions can itself be a first-class analytical object**.

## AC3 assessment

**AC3 — NOT ESTABLISHED.**

The source does not yet establish full TGCV architectural absorption.

### 1. Action sets are not a general transformation space

The action set is the available decision set of an RL agent. TGCV seeks a domain-transversal object of accessible transformations of a system, including transformations that need not be agent decisions.

### 2. No explicit state-conditioned accessibility predicate of TGCV scope

The literature has `A_t` / available-action sets, but the present source does not formulate a general relation:

`τ ∈ T_acc ⇔ P_τ(S,C,L)=1`.

### 3. Change of action set is treated as a learning/environmental problem

The source asks how an agent can adapt to an externally changing action set. It does not generalize the phenomenon as a structural relation between system conditions and the transformation possibilities of the system itself.

### 4. No general mechanism → `ΔT_acc` → downstream architecture

There is no transversal mechanism variable equivalent to TGCV's explanatory `I`, nor a demonstrated architecture:

`mechanism → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.

### 5. Value is reward optimization

Reward and policy performance are not equivalent to TGCV's broader value-construction layer.

## Falsification significance

This source is highly consequential for SLR-1. TGCV **cannot claim novelty** for:

- changing action sets;
- treating action-set change as analytically relevant;
- adapting a policy to additions/removals in available actions;
- distinguishing action-set change from changes in transition/reward functions.

The unresolved proposition is narrower: whether a **domain-independent accessible-transformation space** can be explicitly defined from system conditions, independently of an agent's decision problem, and whether its change can be propagated to reachability, trajectories, outcomes and value.

## Decision

- `AC2`: **DIRECT / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Critical prior-art anchor for `ΔT_acc`.
- TGCV Core: unchanged.
- EXT-1.1 result: not used.
- No historical artifact modified.

## Next controlled operation

The next search should target **dynamic/reconfigurable systems in which the changing action set is endogenous to the system configuration**, rather than an external learning environment. The key test is whether the literature explicitly models:

`S_t → A_t → S_{t+1}`

with

`A_t = F(S_t,C_t)`

and treats changes in `A_t` as consequences of system transformation/reconfiguration itself.

That is the sharpest remaining bridge from dynamic action sets to TGCV's general `T_acc` construction.