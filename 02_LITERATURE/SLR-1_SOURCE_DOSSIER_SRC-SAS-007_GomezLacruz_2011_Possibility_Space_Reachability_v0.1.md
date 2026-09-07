# SLR-1 Source Dossier — SRC-SAS-007

**Status:** RECONSTRUCTED / WORKING  
**Source:** María Gómez Lacruz (2011), *Designing Self-Adaptive Systems*, Technical Master Thesis, Universitat Politècnica de València. citeturn3search12turn2search15  
**Classification:** **AC2 — DIRECT STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Why this source matters

This source is unusually close to the final subtest because it explicitly defines a **Possibility Space** from a variability specification as a state-machine representation containing all feasible configurations reachable through execution and the reconfigurations among them. It then performs explicit **reconfiguration analysis** and a dedicated **safe-reconfiguration/reachability refinement**. citeturn3search12turn2search14

The source therefore directly links:

`variability specification → possibility space → feasible configurations/reconfigurations → reachability → trajectory/path consequences`.

It is not merely an adaptation-space metaphor.

## TGCV mapping

- `S`: current self-adaptive software configuration/model.
- `C`: variability specification and design properties.
- candidate transformations: reconfigurations.
- `T_acc`: feasible reconfigurations represented by the possibility space.
- accessibility: feasibility plus reachability through execution.
- `Reach`: explicit and formally analysed.
- `Trajectory`: paths through the possibility-space state machine.
- mechanism: reconfiguration refinement that removes unsafe transitions/configurations while preserving safe reachability.
- outcome: preservation of design properties and reconfiguration capability.

## AC2 assessment

AC2 is **DIRECT / VERY STRONG** because the source explicitly establishes:

1. a possibility space derived from variability;
2. feasible configurations reachable through execution;
3. reconfigurations among those configurations;
4. explicit reconfiguration analysis;
5. explicit reachability guarantees;
6. the fact that removing transitions can make configurations unreachable, requiring refinement to preserve capability. citeturn3search12turn2search14

This closes the remaining empirical/conceptual subfamily for self-adaptive software: prior art explicitly connects variability/possibility-space structure to reachability and the preservation/loss of future reconfiguration capability.

## AC3 assessment

AC3 is **NOT ESTABLISHED**.

The source remains software/self-adaptation specific and does not establish:

1. a domain-independent transformation object `τ`;
2. a general accessibility predicate `P_τ(S,C,L)`;
3. `ΔT_acc` as a transversal explanatory variable;
4. a mechanism-independent architecture linking `ΔT_acc` to reachability and trajectories across domains;
5. a general `Outcome → Value` construction layer.

The source therefore substantially absorbs the **reachability consequence** part of the TGCV candidate but does not absorb the complete transversal architecture.

## Decision

- `AC2`: **DIRECT / VERY STRONG / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Self-adaptive-family broad novelty claim: **FURTHER ABSORBED**.
- TGCV Core: **UNCHANGED**.
- EXT-1.1: **NOT USED**.
