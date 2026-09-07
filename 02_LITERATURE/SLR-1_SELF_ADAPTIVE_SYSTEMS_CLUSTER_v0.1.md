# SLR-1 — Self-Adaptive Systems / Runtime Adaptation Cluster v0.1

**Status:** RECONSTRUCTED / WORKING

## Current bounded pass

The self-adaptive-systems family has now produced five convergent strong antecedents: `SRC-SAS-001` (Metzger et al.), `SRC-SAS-002` (Gheibi & Weyns, 2024), `SRC-SAS-003` (Angelopoulos, Souza & Mylopoulos, 2015), `SRC-DSPL-001` (Ayala et al., 2021), and `SRC-SAS-004` (Stevens & Bagheri, 2020).

### Cluster evidence

The cluster establishes prior art for:
- explicit adaptation spaces;
- constraint-defined possible configurations;
- possible vs executed adaptation;
- multidimensional representation of adaptation alternatives;
- evolution-induced additions/removals;
- adaptation-space drift;
- emergence/disappearance of options;
- dynamic variability and valid runtime configuration spaces;
- proactive recomputation/optimization over changing configuration spaces;
- formal reachability analysis over adaptation alternatives;
- bounded-horizon adaptation trajectories;
- explicit utility/value assessment of alternatives;
- adaptation-space reduction based on anticipated utility;
- adaptation-space structure as an analytical determinant of adaptivity;
- downstream adaptation/learning behaviour over the available alternatives.

### Architectural verdict

**AC2: VERY STRONG / CONVERGENT / NEAR-DIRECT.**

**AC3: NOT ESTABLISHED.**

The convergence means TGCV must no longer claim novelty for the existence, explicit representation, drift, expansion, contraction, multidimensional modelling, runtime recomputation/optimization, reachability analysis or utility-based selection of an adaptation/action/configuration space within adaptive software systems.

The remaining candidate contribution is narrower and transversal:

`T_acc = {τ | P_τ(S,C,L)=1}`

`ΔT_acc = T_acc,t+1 ⊖ T_acc,t`

`mechanism → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

where `τ` denotes a domain-independent transformation rather than a software adaptation/configuration option, and where the mechanism producing the change is analytically separated from the accessible transformation object.

## Next controlled operation

Continue the bounded pass within self-adaptive systems, now targeting specifically:

1. self-evolution changing future adaptation possibilities;
2. explicit reachability/trajectory consequences of adaptation-space drift;
3. formal links between changing variability spaces and reachable behavioural states.

Stop on the first plausible AC3 candidate and open a dedicated comparative architecture review. If none appears after the predefined subfamilies are screened, freeze this family as AC2 prior-art and proceed to the next SLR-1 family.

## Integrity boundary

No Core modification. No reopening of TR-130–TR-140. No modification of EXT-1.1.
