# SLR-1 Source Dossier — SRC-DGG-001

**Source:** Johan van Benthem, *Logics for Dynamic Graph Games*, SEFM 2024 Collocated Workshops / ReacTS 2024, pp. 22–35, DOI 10.1007/978-3-031-94748-3_2.

**Classification:** **AC2 — STRONG STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Evidence basis

The paper is explicitly part of ReacTS 2024. Its abstract describes sabotage games on graphs that change during play as a running example and discusses logics for reactive systems whose underlying graphs are dynamically modified. citeturn0search0turn0search15

Bibliographic records identify the work as a 2024 SEFM workshop contribution, with an open-access electronic edition listed by DBLP. citeturn0search2turn0search6

## TGCV mapping

| TGCV element | Source analogue | Assessment |
|---|---|---|
| `S` | current graph/game position | strong |
| `C` | current graph configuration and game state | strong |
| `T_acc` | currently available graph moves / edges/actions | strong structural analogue |
| accessibility predicate | modal/game move relation | explicit |
| `ΔT_acc` | graph update/removal changes future moves | **explicit structural analogue** |
| `Reach` | game positions reachable under changing graph | explicit |
| `Trajectory` | play histories through successive graph updates | explicit |
| `Outcome` | resulting game/graph position | explicit |
| `Value` | strategic/game-theoretic evaluation | domain-specific, not TGCV value construction |
| mechanism | sabotage/update move modifying the graph | explicit |

## AC2 assessment

**AC2 — STRONG STRUCTURAL ANTECEDENT CONFIRMED.**

This work independently reinforces the strongest prior-art finding from ReacTS and reactive graphs: a system can contain an explicit relational structure governing available moves, and actions during execution can modify that structure, thereby changing the set of future moves and the reachable behavioural space. citeturn0search15turn0search0

Thus TGCV cannot claim novelty for the generic proposition that a system's future possibilities are changed by graph/relational updates during execution.

## AC3 blockers

The paper nevertheless does not establish the full TGCV architecture:

1. The changing object is a graph/game relation, not a general domain-independent space of transformations.
2. No general `T_acc = F(S,C,L)` predicate covering arbitrary technical transformations is established.
3. The change of the available-move relation is a semantic feature of the game model, not the transversal explanatory object of the research programme.
4. Reachability and trajectories are analysed inside the game formalism, but the explicit TGCV chain `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value` is not established as a general analytical architecture.
5. Strategic/game-theoretic value is not the TGCV notion of value construction.

## Decision

- AC2: **STRONG / CONFIRMED**.
- AC3: **NOT ESTABLISHED**.
- Broad novelty of dynamically changing future possibilities under graph updates: **absorbed**.
- TGCV Core: unchanged.
- EXT-1.1: not used.

## Cluster implication

Together with SRC-RTS-001 and SRC-PRG-001, this source makes the following boundary increasingly robust:

> Dynamic accessibility, reconfiguration of transition relations, and consequent changes in future reachability are established prior art.

The remaining candidate contribution is therefore narrower: **a domain-independent analytical construction in which transformations themselves are elements of an accessible space, the space is explicitly represented as `T_acc = F(S,C,L)`, its change `ΔT_acc` is isolated as the central phenomenon, and that change is systematically connected to downstream reachability, trajectories, outcomes and value construction.**

## Next controlled operation

The ReacTS subcluster now contains multiple independent AC2 antecedents. The next step should therefore be a **cluster-level architectural comparison matrix** across SRC-RTS-001, SRC-PRG-001, SRC-BER-001 and SRC-DGG-001, followed only if necessary by one additional search for a source explicitly combining `T_acc`-like transformation spaces with value/outcome semantics.
