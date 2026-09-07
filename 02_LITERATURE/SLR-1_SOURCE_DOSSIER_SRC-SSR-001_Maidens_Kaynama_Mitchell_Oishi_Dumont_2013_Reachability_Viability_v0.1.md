# SLR-1 Source Dossier — SRC-SSR-001

**Source:** Maidens, J. N.; Kaynama, S.; Mitchell, I. M.; Oishi, M. M. K.; Dumont, G. A. (2013), *Lagrangian methods for approximating the viability kernel in high-dimensional systems*. Automatica 49(9), 2803–2810. DOI: `10.1016/j.automatica.2013.03.020`.

## Retrieval / family

**Family:** State-space and reachability approaches  
**Candidate:** SRC-SSR-001  
**Status:** INCLUDED — substantive comparison

## Analytical construction found

The source explicitly treats **reachability** and **viability** as set-valued analyses of constrained dynamical systems. It establishes a connection by which a viability kernel can be computed using reachable sets, including nonlinear dynamics and general state constraints. The paper therefore provides strong prior art for:

- state-space representation;
- admissible inputs and state constraints;
- sets of states reachable under admissible evolution;
- trajectory-level reasoning;
- viable future evolution under constraints;
- formal connection between reachable sets and longer-horizon viable futures.

## TGCV mapping

| TGCV element | Source correspondence | Assessment |
|---|---|---|
| `S` / system state | dynamical state space | Strong |
| admissibility conditions | input/state constraints | Strong |
| transformation `τ` | control input / admissible evolution | Partial; not an explicit domain-independent transformation object |
| accessibility predicate | existence of admissible input/trajectory reaching a state | Strong analogue |
| `T_acc` | reachable/viable state sets | Strong structural analogue, but different analytical object |
| `ΔT_acc` | not central; reachable/viable sets are computed for a fixed model/constraint structure | Not established |
| `ΔReach` | reachability over time/horizon | Established |
| trajectory | explicit | Established |
| outcome/value | safety/viability objectives, not general value construction | Partial |
| mechanism/interactions | dynamics/control/constraints | Partial |

## Absorption classification

**AC2 — VERY STRONG / DIRECT STRUCTURAL ANTECEDENT**  
**AC3 — NOT ESTABLISHED**

The source materially absorbs the general claim that system state, admissible evolution and constraints determine sets of future-reachable states and viable trajectories. It does **not** establish TGCV's distinctive architecture in which transformations themselves constitute an explicit accessible space whose structure changes across system states/contexts and where `ΔT_acc` is the central analytical object.

## Rationale

Classical reachability theory starts from a state and admissible inputs/dynamics and asks which states can be reached. TGCV asks a prior-level question: which **transformations** are accessible now, and how does that transformation-accessibility structure change? Reachability is therefore downstream in the TGCV architecture rather than a substitute for `T_acc`.

## Decision

This source is retained as strong prior art and as a boundary condition for the state-space/reachability family. It does not trigger Core modification or falsify TGCV architectural originality.

- TGCV Core: unchanged.
- TR-130–TR-140: not reopened.
- EXT-1.1: not used.
