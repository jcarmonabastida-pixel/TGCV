# SLR-1 Source Dossier — SRC-SAS-004

**Status:** RECONSTRUCTED / WORKING  
**Source:** Clay Stevens & Hamid Bagheri (2020), *Reducing Run-Time Adaptation Space via Analysis of Possible Utility Bounds*, ICSE 2020, pp. 1522–1534. DOI 10.1145/3377811.3380365. citeturn1search0turn1search25  
**Classification:** **AC2 — NEAR-DIRECT STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Why this source matters

This source is particularly strong for the current subtest because it treats the runtime **adaptation space** as the possible state transitions considered for an adaptation decision, uses formal structural modelling to determine which configurations are reachable from others, and computes bounded-horizon utility for candidate adaptations. It then trims the space to alternatives with the best potential utility. citeturn1search0turn1search25

## TGCV mapping

- `S`: current managed system configuration and environment.
- `C`: adaptation goals, monitored context and model parameters.
- `T_acc`: allowable runtime adaptation options / possible state transitions.
- accessibility predicate: allowable adaptation structure and runtime model constraints.
- execution vs accessibility: candidate adaptations are analysed before the planner selects and executes one.
- `Reach`: explicitly modelled reachability among configurations.
- `Trajectory`: bounded-horizon adaptation sequences.
- `Outcome`: possible utility/quality results.
- `Value`: explicit utility bounds and Pareto potential.
- mechanism: formal structural/behavioural analysis used to reduce the adaptation space.
- `ΔT_acc`: not formulated as a general state-to-state delta of the accessible transformation space; the contribution is reduction/pruning of the current adaptation space.

## AC2 assessment

AC2 is **NEAR-DIRECT / VERY STRONG**. The source establishes prior art for:

1. explicit runtime adaptation spaces;
2. adaptation space as possible transitions/configurations;
3. formal reachability analysis over that space;
4. downstream trajectory/horizon analysis;
5. explicit utility/value assessment of alternatives;
6. transformation of the candidate space based on anticipated utility. citeturn1search0turn1search25

This substantially narrows any novelty claim concerning runtime recomputation, pruning or evaluation of accessible alternatives.

## AC3 assessment

AC3 is **NOT ESTABLISHED** because:

1. the transformation candidates remain software adaptation transitions/configurations;
2. the accessibility predicate is domain-specific and not a general `P_τ(S,C,L)`;
3. the paper optimizes/reduces an existing adaptation space rather than treating `ΔT_acc` as the central transversal explanatory variable;
4. the mechanism is an analysis/optimization technique, not an abstract mechanism variable separated from the accessible transformation object;
5. reachability and trajectory are explicitly present, and utility is explicitly present, but the general cross-domain architecture `mechanism → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value` is not established;
6. no general theory of value construction is proposed.

## Decision

- `AC2`: **NEAR-DIRECT / VERY STRONG / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Novelty of runtime adaptation-space recomputation/reduction, reachability analysis and utility-based selection: **absorbed as domain-specific prior art**.
- TGCV Core: **UNCHANGED**.
- EXT-1.1: **NOT USED**.
