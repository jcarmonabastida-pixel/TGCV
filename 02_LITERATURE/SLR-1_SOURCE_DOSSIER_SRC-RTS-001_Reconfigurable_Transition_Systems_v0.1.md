# SLR-1 Source Dossier — SRC-RTS-001

**Status:** RECONSTRUCTED / WORKING
**Source cluster:** Reconfigurable Transition Systems (ReacTS 2024) and associated formal-literature lineage.
**Classification:** **AC2 — NEAR-DIRECT STRUCTURAL EQUIVALENCE; AC3 NOT ESTABLISHED**

## Why this source cluster matters

This is the closest formal antecedent found so far to the remaining TGCV boundary. Reconfigurable Transition Systems are explicitly defined as **dynamic relational structures whose accessibility relation itself can change during execution**, together with their nodes or labels. citeturn1view0

The source therefore goes beyond merely changing an action catalogue or possibility space: it explicitly models a changing **accessibility relation**.

## Key evidence

The ReacTS 2024 workshop defines RTSs as dynamic graphs that evolve during execution because their accessibility relation, node set, or labelling can change when edges are crossed. It positions RTSs as a formalism for reactive and reconfigurable behaviour and gives examples spanning autonomous vehicles, software components, and biological mutation. citeturn1view0

The 2026 ReacTS call independently repeats the same architectural definition: RTSs are dynamic relational structures whose underlying graph evolves during execution, including changes to the accessibility relation. citeturn0search1turn0search4

A complementary dynamic-Petri-net line explicitly represents configuration change as:

`DPN1(P,T,A,M) → DPN2(P',T',A',M')`

and allows the set of active/enabled places and transitions to change between configurations. citeturn0search47

Adaptive Petri-net work further describes runtime mechanisms that enable/disable transitions and thereby change control flow, including dynamic feature updates and transition occurrences under configuration conditions. citeturn0search2

Finally, formal reconfiguration work represents configurations as states of transition structures and treats runtime reconfiguration as dynamic evolution between configurations. citeturn0search48

## TGCV mapping

| TGCV element | RTS / dynamic-Petri analogue | Assessment |
|---|---|---|
| `S` | current graph/configuration/system state | strong |
| `C` | current configuration / structural context | strong |
| `T_acc` | enabled/accessibility relation from current configuration | **near-direct analogue** |
| accessibility predicate | edge/enabled-transition relation | **explicit** |
| `ΔT_acc` | change of accessibility relation after graph/configuration evolution | **explicit at structural level** |
| `Reach` | reachability graph / reachable configurations | **explicit** |
| `Trajectory` | execution paths through evolving relational structures | **explicit** |
| `Outcome` | reached state/configuration/behaviour | explicit |
| `Value` | not part of the formalism | absent / domain-specific |
| mechanism | reconfiguration/event/edge crossing causing relational change | explicit but not TGCV-generalized |

## AC2 assessment

**AC2 — NEAR-DIRECT STRUCTURAL EQUIVALENCE CONFIRMED.**

This cluster establishes that prior literature already contains a formal object with the following structure:

`current configuration → current accessibility relation → reachable states/paths`

and that execution can modify the accessibility relation itself.

This is a substantially stronger antecedent than the previously screened dynamic-action-set and phase-aware operation-set sources.

Consequently TGCV cannot claim novelty for the following broad propositions:

- accessibility relations can be dynamic;
- reconfiguration can modify which transitions/relations are available;
- a changing accessibility relation can be formally represented;
- reachability can be analysed over an evolving transition structure.

## AC3 assessment

**AC3 — NOT ESTABLISHED.**

This cluster comes very close, but the full TGCV architecture is still not demonstrated.

### 1. Accessibility relation ≠ general accessible transformation space

RTS literature represents an evolving relational graph. TGCV's target is a transversal **space of transformations**, potentially crossing domains and formalisms, with transformations treated as analytically identifiable objects.

### 2. The predicate is formal but not TGCV-generalized

RTSs provide an explicit accessibility relation, but the screened material does not establish a general construction:

`τ ∈ T_acc ⇔ P_τ(S,C,L)=1`.

### 3. `ΔT_acc` is present, but not elevated to TGCV's central explanatory variable

The relation changes, but the literature is concerned with semantics, verification and reconfiguration rather than making the change in the accessible-transformation space the central transversal phenomenon.

### 4. Reachability and trajectories are present

This is already prior art and must not be claimed as novel by TGCV. Dynamic Petri-net work explicitly uses reachability structures, and RTSs explicitly represent evolving relational paths. citeturn0search7turn1view0

### 5. Value construction is absent

The screened RTS/dynamic-Petri literature does not establish the downstream relation:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

where value is understood as a general value-construction phenomenon rather than verification, reward, fitness or reliability.

## SLR-1 significance

This source cluster is the strongest falsification result so far. It means that TGCV's originality **cannot** reside simply in:

> “the accessible relation of a system can change and this affects what can subsequently be reached.”

That proposition is already represented formally in reconfigurable transition systems.

The remaining candidate novelty is now extremely narrow:

> **A domain-independent analytical abstraction that treats transformations themselves as the elements of a dynamically changing accessible space, separates the mechanism producing that change from the space, and systematically connects `ΔT_acc` to downstream reachability/trajectory/outcome/value construction.**

Even this statement must remain provisional until the ReacTS and dynamic-Petri literature has been mined at the individual-paper level rather than only at the workshop/cluster level.

## Decision

- `AC2`: **NEAR-DIRECT / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Broad novelty of dynamic accessibility/reachability is **absorbed**.
- Broad novelty of reconfiguration changing enabled transitions is **absorbed**.
- TGCV Core: unchanged.
- EXT-1.1: not used.

## Next controlled operation

Do not broaden the search further. Perform **individual-paper screening within the ReacTS/dynamic-Petri cluster** and test whether any one formalism already contains the complete TGCV-like architecture, especially:

1. explicit transformation/action elements;
2. a state/configuration-conditioned accessibility predicate;
3. an explicit changing accessibility/transformation space;
4. propagation to reachability and trajectories;
5. an explanatory mechanism separated from the relational structure;
6. downstream outcome/value semantics.

If no source satisfies all six, the SLR-1 conclusion should shift from “search for a changing accessible relation” to a much narrower **architectural-difference analysis** against the strongest formal antecedents.