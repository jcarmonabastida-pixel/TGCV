# SLR-1 — ReacTS / Reactive Graphs Architectural Comparison v0.1

**Status:** RECONSTRUCTED / WORKING
**Purpose:** compare the strongest identified formal antecedents against the TGCV architecture and test whether any source establishes AC3 (architectural absorption).

## Scope

This matrix compares four sources already screened individually:

- `SRC-RTS-001` — Reconfigurable Transition Systems
- `SRC-PRG-001` — Paraconsistent Reactive Graphs
- `SRC-BER-001` — Behavioural Equivalences over Reconfigurable Systems
- `SRC-DGG-001` — Logics for Dynamic Graph Games

The ReacTS literature explicitly defines RTSs as dynamic relational structures whose accessibility relation, node set or labelling may change during execution. The 2024 proceedings place Behavioural Equivalences and Logics for Dynamic Graph Games in the same ReacTS cluster, alongside Paraconsistent Reactive Graphs. citeturn1search18turn2view0

## Architectural matrix

| Criterion | SRC-RTS-001 | SRC-PRG-001 | SRC-BER-001 | SRC-DGG-001 | TGCV target |
|---|---|---|---|---|---|
| Explicit system state/configuration | YES | YES | YES | YES | YES |
| Explicit transition/action elements | YES | YES | YES | YES | YES |
| State/configuration-conditioned availability | YES | YES | YES | YES | YES |
| Explicit accessibility relation | YES | YES | STRUCTURAL | YES | YES |
| Accessibility can change during evolution | YES | YES | YES | YES | YES |
| Explicit mechanism causing relation change | YES | YES | YES | YES | YES |
| Change in future available operations is represented | YES | YES | YES | YES | YES |
| Reachability / reachable configurations | YES | YES | YES | YES | YES |
| Trajectories / executions | YES | YES | YES | YES | YES |
| Domain-independent transformation abstraction | NO | NO | NO | NO | **YES** |
| General `T_acc = F(S,C,L)` formulation | NO | NO | NO | NO | **YES** |
| `ΔT_acc` as independent analytical object | NO | NO | NO | NO | **YES** |
| Mechanism separated from `T_acc` as explanatory layer | PARTIAL | PARTIAL | NO | PARTIAL | **YES** |
| General chain `ΔT_acc → ΔReach → ΔTrajectory` | PARTIAL | PARTIAL | PARTIAL | PARTIAL | **YES** |
| Outcome → Value construction | NO | NO | NO | NO | **YES** |
| Transversal value-construction theory | NO | NO | NO | NO | **YES** |

## Evidence interpretation

### 1. The cluster absorbs the broad phenomenon

The convergence is now strong. ReacTS explicitly treats evolving accessibility relations as the defining feature of a class of dynamic relational systems. citeturn1search18turn1search9

Paraconsistent Reactive Graphs gives a particularly explicit mechanism: hyper-edges activate or deactivate other edges, so traversal can modify which transitions are active. The formal definition includes a state set, action-labelled ground edges, activating edges and deactivating edges. citeturn2view1

Behavioural Equivalences extends bisimulation reasoning to reconfigurable systems; the available bibliographic evidence explicitly places it in the ReacTS cluster and describes an extension of bisimilarity for reactive/reconfigurable process systems. citeturn3search0turn2view0

Logics for Dynamic Graph Games treats sabotage games as a running example of graphs that change during play and develops logics for such reactive systems. citeturn1search2turn1search1

### 2. AC3 is still not demonstrated

No source identified in this cluster establishes the full TGCV architecture.

The decisive differences are:

1. **Object level.** The sources model graphs, transitions, actions, edges, games or process configurations. TGCV abstracts the *transformations themselves* into a transversal analytical space.
2. **Accessibility function.** None of the four sources has been shown to formulate the general cross-domain object `T_acc = F(S,C,L)` with an explicit accessibility predicate over arbitrary transformations.
3. **Centrality of change.** In these sources, changing accessibility is a semantic/runtime feature of the formalism. TGCV makes `ΔT_acc` the central analytical phenomenon.
4. **Mechanism separation.** Reactive mechanisms exist in the antecedents, but they are generally internal constructs of the formalism rather than a separate explanatory variable whose effect on `T_acc` is analysed across domains.
5. **Downstream analytical chain.** Reachability and trajectories are present, but no source has been shown to formulate the general relation `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.
6. **Value.** The sources target semantics, verification, equivalence, logical expressiveness or game winning conditions. None establishes a transversal theory connecting transformation-space change to value construction.

## Architectural verdict

**AC2: CONFIRMED — CONVERGENT PRIOR ART.**

The ReacTS / reactive-graph cluster is sufficient to falsify any broad TGCV novelty claim of the form:

> “Systems can evolve so that the set/relation of future accessible transitions changes.”

It is also sufficient to falsify the weaker claim that such changes can be caused by explicit mechanisms during execution.

**AC3: NOT ESTABLISHED.**

The remaining candidate contribution is therefore narrower and more defensible:

> A domain-independent analytical abstraction that represents transformations as members of a state/context-conditioned accessible transformation space, isolates the mechanism producing changes in that space, treats `ΔT_acc` as the central analytical object, and relates that change systematically to downstream reachability, trajectories, outcomes and value construction.

## Decision gate

**Decision:** Do NOT modify TGCV Core.

**SLR-1 status for this cluster:** AC2 convergence / AC3 unresolved but narrowed.

**Next operation:** do not continue indefinitely within ReacTS. Perform one final adjacent-literature falsification pass targeting the exact remaining combination: `transformation-space + accessibility predicate + change of that space + mechanism separation + downstream value/outcome relation`. If no AC3 source appears, freeze this cluster as prior-art boundary and move to the next predefined SLR-1 family.

## Traceability

Source dossiers:

- `SRC-RTS-001`
- `SRC-PRG-001`
- `SRC-BER-001`
- `SRC-DGG-001`

No EXT-1.1 result is used as evidence for architectural originality. No post-hoc change to EXT-1.1 is authorized by this matrix.
