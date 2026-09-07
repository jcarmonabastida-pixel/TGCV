# SLR-1 Source Dossier — SRC-PRG-001

**Status:** RECONSTRUCTED / WORKING
**Source:** Cunha, J., Madeira, A., & Barbosa, L. S. (2024), *Paraconsistent Reactive Graphs*, SEFM 2024 Collocated Workshops, pp. 105–111, DOI 10.1007/978-3-031-94748-3_9.
**Classification:** **AC2 — DIRECT STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Evidence basis

A full-text version is openly accessible through the authors' institutional repository. The paper states that reactive graphs have an accessibility relation that can be modified by prior transitions. This is achieved through higher-order/hyper-edges that update the accessibility relation when traversed; hyper-edges can activate or deactivate connected ground edges. citeturn3search42turn3search1

The paper further defines an `(A,Act)`-Paraconsistent transition system with states `W`, initial state `w0`, and a transition relation `R ⊆ W × Act × A² × W`, explicitly making actions part of the transition structure. It then extends the model with reactive hyper-edges that change which ground transitions are active. citeturn3search1

## TGCV mapping

| TGCV element | Source analogue | Assessment |
|---|---|---|
| `S` | current reactive graph/state | strong |
| `C` | current activation/information configuration | strong analogue |
| `T_acc` | currently active/available ground transitions | **direct analogue** |
| accessibility predicate | active-edge / transition relation | explicit |
| `ΔT_acc` | activation/deactivation of edges following traversal | **explicit operational analogue** |
| `Reach` | states reachable through active transitions | explicit in transition-system semantics |
| `Trajectory` | sequences of traversed transitions | explicit/implicit in reactive graph execution |
| `Outcome` | resulting graph/state | explicit |
| `Value` | absent as a general value-construction layer | absent |
| mechanism | hyper-edge/switch that activates/deactivates another edge | **explicit mechanism** |

## AC2 assessment

**AC2 — DIRECT STRUCTURAL ANTECEDENT CONFIRMED.**

The source provides a particularly important combination that earlier candidates often separated:

`transition/action → mechanism (hyper-edge) → changed accessibility relation → changed available transitions → subsequent behaviour`.

This is very close to the TGCV idea of a mechanism changing future accessibility conditions. It therefore absorbs any broad claim that no formal system represents an explicit mechanism which changes the accessibility relation governing future transitions.

## AC3 assessment

**AC3 — NOT ESTABLISHED.**

The source still does not demonstrate the full TGCV architecture.

### 1. The object is an accessibility relation over transitions, not a transversal transformation space

The reactive graph formalism operates on a graph-specific transition structure. TGCV seeks an abstraction whose elements are transformations/operations across arbitrary technical or generative systems.

### 2. No general `T_acc = F(S,C,L)` formulation

The accessibility relation is explicit, but the source does not formulate a domain-independent predicate identifying arbitrary transformations as members of an accessible transformation space.

### 3. `ΔT_acc` is operational, not elevated to the central research object

Activation/deactivation of edges directly changes the relation, but the source's objective is formal semantics for reactive/paraconsistent graphs, not a transversal theory of change in accessible transformation spaces.

### 4. Reachability/trajectory are formal consequences, not the proposed explanatory chain

The formalism naturally supports subsequent transitions and states, but it does not establish the general chain:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.

### 5. Value construction remains absent

There is no general value-construction layer analogous to TGCV's downstream analytical objective.

## Falsification significance

This is one of the strongest individual-paper results in the SLR-1 pass. It demonstrates that prior literature can already combine:

- an explicit transition/action relation;
- an explicit accessibility relation;
- a mechanism that changes that relation;
- activation/deactivation of future transitions;
- dynamic downstream behaviour.

Therefore TGCV must **not** claim novelty for that combination alone.

The remaining candidate contribution is the abstraction of this pattern into a **domain-independent analytical construction of accessible transformations**, with `ΔT_acc` explicitly separated as the phenomenon of interest and systematically related to future reachability, trajectories, outcomes and value construction.

## Decision

- `AC2`: **DIRECT / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Broad novelty of mechanism-mediated accessibility-relation change: **absorbed**.
- Broad novelty of activation/deactivation changing future transitions: **absorbed**.
- TGCV Core: unchanged.
- EXT-1.1: not used.

## Next controlled operation

Screen the strongest ReacTS papers individually, especially **Behavioural Equivalences over Reconfigurable Systems** and **Logics for Dynamic Graph Games**, and test whether their formal semantics already supplies the missing abstraction from an evolving accessibility relation to a general transformation-space object plus downstream value semantics. citeturn2view0turn3search2turn3search5
