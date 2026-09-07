# SLR-1 Source Dossier — SRC-DAF-001

**Status:** RECONSTRUCTED / WORKING
**Source:** Xu, D., Mandlekar, A., Martín-Martín, R., Zhu, Y., Savarese, S., & Fei-Fei, L. (2021), *Deep Affordance Foresight: Planning Through What Can Be Done in the Future*, IEEE ICRA 2021, pp. 6206–6213. DOI: 10.1109/ICRA48506.2021.9560841; arXiv:2011.08424.
**Classification:** **AC2 — STRONG STRUCTURAL EQUIVALENCE; AC3 NOT ESTABLISHED**

## Bibliographic identity

The primary arXiv record identifies the six authors and the November 2020 preprint; IEEE Xplore records the peer-reviewed ICRA 2021 publication and DOI 10.1109/ICRA48506.2021.9560841. citeturn2view0turn1search0

## Why this source is relevant to the SLR-1 falsification question

This source belongs to the new search front deliberately selected after closing the MDE transformation cluster: **accessibility/changeability/future possibilities as an analytical object** rather than merely transformation-rule execution.

It is unusually close to TGCV because it explicitly models both:

1. what actions are feasible at a current state; and
2. what actions would become feasible if a current action were executed.

The authors introduce this recursive structure specifically to reason about long-horizon consequences. citeturn2view0

## Evidence extraction

### E1 — explicit accessibility object

The paper formally defines an affordance for a parameterized skill `(π,θ)` as the set of states in which that skill is feasible:

`A_(π,θ) = { s ∈ S | (π,θ) is feasible at s }`.

The corresponding indicator determines whether a given state affords the skill. This is a mathematically explicit accessibility relation between states and actions/skills. citeturn2view0

### E2 — accessibility is state-dependent

The paper emphasizes that only a small subset of skills can be successfully executed at a given state, making it crucial for planning to focus on executable skills in that state. Feasibility can be checked using kinematic constraints or collision checks. citeturn2view0

### E3 — current action can alter future accessibility

This is the most important evidence. The authors explicitly propose representing “future actions that would become feasible if a certain action is executed at the current state”. They give the recursive example that a grasp can enable a hook action, which in turn can make a final grasp feasible. citeturn2view0

Thus the paper contains an explicit operational relation of the form:

`current action → future state/conditions → future feasible actions`.

### E4 — recursive future-affordance structure

The authors define affordance feasibility at the current state and represent the effect of an action through expected affordances at future states. They explicitly state that this recursive structure allows chains of affordances to be composed for long-horizon planning. citeturn2view0

### E5 — reachability / trajectories

A plan is a sequence of parameterized skills. The paper recursively propagates a state distribution through the transition dynamics while gating each step by the corresponding affordance. Plan completion is then the probability that every skill in the sequence can be executed. citeturn2view0

### E6 — outcome / objective relation

The planning problem searches for the plan maximizing plan-completion probability among goal-directed plans. DAF then learns latent dynamics and affordance models and uses model-predictive control to select plans. citeturn2view0

### E7 — task-agnostic representation

A significant architectural feature is that the affordance representation is intended to be independent of a final task goal and reusable across different tasks. This gives the representation some cross-task generality, although it remains within robotic skill planning. citeturn2view0

## TGCV mapping

| TGCV element | DAF analogue | Assessment |
|---|---|---|
| `S` | robot/environment state space | explicit |
| `T_acc` | skills/actions afforded by a state | **very strong analogue** |
| accessibility predicate | `A_(π,θ)(s)` feasibility indicator | **explicit mathematical predicate** |
| `ΔT_acc` | future skills becoming feasible after action-induced state change | **operationally present; not isolated as a delta object** |
| `Reach` | recursively reachable/future state distributions | explicit |
| `Trajectory` | parameterized skill sequence | explicit |
| `Outcome` | goal-state / plan completion | explicit |
| `Value` | plan-completion probability / task success | partial analogue |
| mechanism | executed skill + learned dynamics causing future state changes | present, but domain-specific |

## AC2 assessment

**AC2 — STRONG STRUCTURAL EQUIVALENCE CONFIRMED.**

DAF substantially overlaps the TGCV analytical chain:

`state → feasible actions → action execution → future state → future feasible actions → reachable skill chains → goal-directed outcome`.

More importantly, unlike the MDE cluster, DAF explicitly treats **future feasibility of actions** as a planning object and recursively represents how actions can enable future actions. citeturn2view0

This makes DAF a substantially stronger falsification candidate than the preceding MDE sources.

## AC3 assessment

**AC3 — NOT ESTABLISHED.**

The source nevertheless stops short of the full TGCV architecture.

### 1. Accessibility is action/skill-specific, not a transversal `T_acc` change object

DAF defines an affordance set `A_(π,θ)` for each parameterized skill. It does not formulate a general object representing the entire accessible transformation/action space and its change:

`T_acc,t → T_acc,t+1`.

The future-affordance recursion is operationally equivalent to querying future members of an accessibility relation, but the **change of the relation itself is not elevated to the analytical object**.

### 2. No general mechanism/context decomposition

DAF has explicit state `S`, transition dynamics `T`, skill parameters and feasibility predicates. However, it does not introduce a domain-transversal mechanism variable corresponding to TGCV's explanatory `I`, nor does it formulate the mechanism → changed conditions → changed accessibility relation as an independent analytical chain.

### 3. No transversal outcome/value-construction architecture

DAF optimizes plan completion probability for robotic task goals. It does not connect accessibility-space change to a general theory of outcome/value construction across domains.

### 4. Domain dependence remains material

Although the affordance representation is reusable across different robotic tasks, it remains a robotics/skill-planning construction involving parameterized motor skills and learned environment dynamics. citeturn2view0

## Falsification significance

This source **does falsify any broad TGCV originality claim** that says prior literature does not already represent:

- state-dependent action accessibility;
- actions becoming feasible after previous actions;
- recursive future possibilities;
- reachability through feasible action chains;
- downstream task success.

It does **not** falsify the narrower TGCV proposition that these phenomena can be abstracted into a transversal analytical object `ΔT_acc`, independently of a domain-specific affordance formalism, and related systematically to future reachability, trajectories, outcomes and value.

## Decision boundary

- `AC2`: strong / high-confidence structural equivalence.
- `AC3`: not established.
- TGCV Core: unchanged.
- EXT-1.1 empirical result: not used.
- No historical artifact modified.

## Next controlled implication

`SRC-DAF-001` should now trigger **citation-chain mining around affordance theory and sequential decision-making**, especially the cited work on formal affordances in reinforcement learning and future action possibilities. The next search should test whether another source explicitly represents the *whole available-action relation* as an object whose change is itself measured or theorized, rather than merely predicting future feasible actions.

## Integrity note

This dossier is a current reconstructed research record, not a recovered historical dossier. Source evidence and architectural interpretation are kept separate.