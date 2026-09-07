# SLR-1 Source Dossier — SRC-HENSHIN-001

**Status:** RECONSTRUCTED / WORKING
**Source:** Strüber, D., Burdusel, A., John, S., & Zschaler, S. (2018), *Henshin: A Model Transformation Language and its Use for Search-Based Model Optimisation in MDEOptimiser*, Modellierung 2018, pp. 299–300.
**Classification:** **AC2 — STRUCTURAL EQUIVALENCE CONFIRMED; AC3 NOT ESTABLISHED**

## Bibliographic identity

The source is a peer-reviewed conference contribution in *Modellierung 2018*, pages 299–300. The authors and publication metadata are independently recorded by DBLP and King's College London. citeturn0search0turn0search1

## Source scope

The paper presents Henshin as a graph-transformation language and explains its use for search-based model optimisation in MDEOptimiser. The abstract explicitly states that Henshin is used to specify evolutionary operators for MDEOptimiser, whose goal is to find an optimal model under a fitness function. citeturn0search1

## Evidence extraction

### E1 — transformations are rule-based operators

Henshin is based on graph transformation and is rule-based. Its transformation rules specify modifications of model graphs. citeturn1view1

### E2 — applicability is structurally represented

The tutorial material describes rule application through graph matching and explicitly includes positive and negative application conditions. A rule application therefore depends on whether its left-hand-side pattern can be matched and its application conditions are satisfied. citeturn2view1

### E3 — state transition is explicit

Henshin describes rule application as a transition from an input graph to a modified graph, with deleted, preserved and created elements represented by the left- and right-hand sides of the rule. citeturn2view1

### E4 — state-space exploration is an explicit Henshin capability

The Henshin tutorial lists state-space exploration among its analysis capabilities. It also gives an example in which the full state space is computed, with states and transitions explicitly enumerated. citeturn2view4

### E5 — reachability/trajectory analogue

Because Henshin rules induce transitions between model states, repeated rule application defines reachable states and paths through the state space. The tutorial also demonstrates conflict/dependency analysis among rules and identifies situations where a rule is no longer applicable after another rule has changed the model. citeturn2view1turn2view4

### E6 — optimisation layer

In the MDEOptimiser application, Henshin evolutionary operators are combined with constraints and fitness functions in a multi-objective optimisation process. Candidate solution models are evaluated against objective functions and constraints. citeturn1view0

### E7 — the accessibility relation changes operationally, but is not isolated as the research object

The strongest relevant evidence is the conflict example: after a model transformation, another rule can become “Not applicable anymore”, producing a conflict. This demonstrates state-dependent accessibility of transformations in the operational semantics. citeturn2view4

However, neither the source nor the tutorial elevates the resulting change in the set of applicable transformations to an explicit transversal analytical variable comparable to TGCV `ΔT_acc`.

## TGCV mapping

| TGCV element | Henshin analogue | Assessment |
|---|---|---|
| `S` | current typed attributed graph/model | strong analogue |
| `T_acc` | currently applicable rule applications satisfying matching/application conditions | **very strong operational analogue** |
| accessibility predicate | graph matching + positive/negative application conditions | explicit |
| `ΔT_acc` | rules becoming applicable/inapplicable after model changes | **operationally present, analytically implicit** |
| `Reach` | state-space reachability under rule applications | explicit |
| `Trajectory` | ordered rule-application path | explicit/derived |
| `Outcome` | resulting model state | explicit |
| `Value` | fitness/objective functions in optimisation | partial analogue |
| mechanism modifying accessibility | rule application modifies the model and can change applicability of other rules | present operationally, not separated as transversal mechanism |

## AC2 assessment

**AC2 — STRUCTURAL EQUIVALENCE CONFIRMED.**

Henshin is stronger than a mere transformation-language example because its formalism makes the accessibility conditions of transformations operationally explicit: rule matching and positive/negative application conditions determine whether a transformation can be applied to a given model. Rule application changes the model state, and the resulting state can alter which rules remain applicable. State-space exploration and conflict/dependency analysis make the resulting transition structure explicit. citeturn2view1turn2view4

This is therefore clear prior art for the following structure:

`state/model → applicable transformations → state transition → changed future applicability → reachable state space → trajectory → evaluated outcome`.

## AC3 assessment

**AC3 — ARCHITECTURAL ABSORPTION NOT ESTABLISHED.**

The source does not establish the stronger TGCV architecture for three reasons.

1. **No explicit `ΔT_acc` object:** although transformations can become inapplicable after another transformation, the source does not define the change in the accessible transformation relation as an independent analytical object.
2. **No transversal mechanism layer:** the model transformation mechanism is formalized, but there is no general abstraction separating a mechanism that changes system conditions from the resulting change in accessibility and then from downstream trajectory/value effects.
3. **Domain/framework specificity:** the construction is embedded in graph transformation and search-based model optimisation, whereas TGCV seeks a transversal formulation independent of a particular transformation formalism, algorithm or optimisation task.

The evidence therefore strengthens the prior-art boundary but does not absorb the proposed TGCV higher-level architecture.

## Important methodological consequence

This source materially raises the originality threshold. It is no longer sufficient for TGCV to claim novelty merely because it makes accessibility of transformations explicit. Henshin already provides a formal operational mechanism for state-dependent transformation applicability and its effect on future transitions.

The potentially distinctive TGCV claim must therefore remain at the level of **analytical elevation and transversalization of changes in accessible transformation relations**, rather than the existence of such state-dependent applicability itself.

## Cluster conclusion

With `SRC-DSE-001`, `SRC-MOMOT-001`, `SRC-MDEO-001`, and now `SRC-HENSHIN-001`, the MDE/search-based transformation cluster provides convergent prior art for:

- transformation/search spaces;
- explicit transformation operators/rules;
- state-dependent applicability;
- changes in future applicability after state transitions;
- reachable states and state-space exploration;
- trajectories through transformation sequences;
- optimisation/objective evaluation.

The cluster does **not yet demonstrate AC3 absorption** of the stronger TGCV proposition concerning a transversal analytical object `ΔT_acc` and its general downstream relation to reachability, trajectories, outcomes and value.

## Decision boundary

- `AC2`: confirmed.
- `AC3`: not established.
- TGCV Core: unchanged.
- EXT-1.1 evidence: not used in classification.
- Historical records: not modified.

## Integrity note

This dossier is a current reconstructed research record, not a recovered historical dossier. It separates source evidence from TGCV architectural interpretation.