# SLR-1 Source Dossier — SRC-SAS-003

**Status:** RECONSTRUCTED / WORKING  
**Source:** Konstantinos Angelopoulos, Vítor E. Silva Souza & John Mylopoulos (2015), *Capturing Variability in Adaptation Spaces: A Three-Peaks Approach*, ER 2015, LNCS 9381, 384–398. DOI 10.1007/978-3-319-25264-3_28. citeturn1search0turn1search25  
**Classification:** **AC2 — VERY STRONG / NEAR-DIRECT STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Why this source matters

This source is one of the closest matches encountered in the self-adaptive-systems family. It explicitly defines an **adaptation space** as the space of alternative adaptations available to an adaptive system and models that space through three coupled dimensions: requirements/goals, architecture and behaviour. It also states that possible reconfigurations define the adaptation space and that its dimensions and size determine adaptivity. citeturn1search0turn1search25

## TGCV mapping

- `S`: adaptive software/system plus environment.
- `C`: current requirements, environmental parameters, behavioural and architectural control parameters.
- `T_acc`: alternative adaptations/reconfigurations represented by the three-peaks variability model — **near-direct analogue**.
- accessibility predicate: constraints and control parameters defining supported alternatives.
- execution vs accessibility: possible reconfigurations constitute the adaptation space; actual adaptation scenarios/executions are downstream.
- `ΔT_acc`: not formulated as a standalone delta operator, but changes in variability parameters alter the available adaptation options.
- `Reach`: alternative sequences for goal fulfilment and task execution.
- `Trajectory`: supported behavioural sequences and runtime adaptation paths.
- `Outcome`: requirement fulfilment / handling failures.
- `Value`: quality attributes and requirement satisfaction, not a general value-construction theory.
- mechanism: runtime adaptation/reconfiguration driven by failures, requirements and environmental variability.

## AC2 assessment

AC2 is **very strong and near-direct**. The paper absorbs several broad TGCV novelty claims:

1. adaptation alternatives can be represented as an explicit space;
2. that space can be multidimensional and structurally represented;
3. behaviour and architecture contribute jointly to the set of alternatives;
4. possible sequences/paths through the space can be represented;
5. the size/structure of the adaptation space is analytically meaningful for adaptivity. citeturn1search0turn1search25

This source should therefore be treated as a principal prior-art boundary, not merely an adjacent analogy.

## AC3 assessment

AC3 is **not established** because:

1. the adaptation space is explicitly a software-adaptation construct, not a domain-independent transformation space;
2. the paper does not define a general predicate `P_τ(S,C,L)` over arbitrary transformations;
3. change in the adaptation space is not isolated as the central analytical variable `ΔT_acc`;
4. the causal/explanatory mechanism producing the change is not separated from the analytical space in a transversal form;
5. the downstream chain is domain-specific and does not establish the general `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value` architecture;
6. value remains requirement/quality satisfaction rather than a general theory of value construction.

## Decision

- `AC2`: **VERY STRONG / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Broad claim that adaptive systems can explicitly model a multidimensional adaptation space: **absorbed**.
- TGCV Core: **UNCHANGED**.
- EXT-1.1: **NOT USED**.
