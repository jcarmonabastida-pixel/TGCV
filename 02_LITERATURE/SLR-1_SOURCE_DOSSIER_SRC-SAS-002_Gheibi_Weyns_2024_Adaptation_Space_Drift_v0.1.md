# SLR-1 Source Dossier — SRC-SAS-002

**Status:** RECONSTRUCTED / WORKING  
**Source:** Omid Gheibi & Danny Weyns (2024), *Dealing with Drift of Adaptation Spaces in Learning-based Self-Adaptive Systems Using Lifelong Self-Adaptation*, ACM Transactions on Autonomous and Adaptive Systems 19(1), Article 5, DOI 10.1145/3636428. citeturn1search12turn1academia25  
**Classification:** **AC2 — VERY STRONG / NEAR-DIRECT STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Core evidence

The paper defines an **adaptation space** as the set of adaptation options a self-adaptive system can select at a given time. It explicitly studies **drift of adaptation spaces**: uncertainties can cause adaptation options to disappear or new options to emerge. The paper proposes a lifelong-self-adaptation architecture that detects such changes and updates the learning models accordingly. citeturn1search12turn1academia25

## TGCV mapping

- `S`: current self-adaptive system/environment/task state.
- `C`: current runtime models, tasks, adaptation goals and quality estimates.
- `T_acc`: adaptation space — set of currently selectable adaptation options.
- accessibility predicate: option is available/selectable under current adaptation conditions and goals.
- execution vs accessibility: explicit; the adaptation space is the set of options available for selection, not the set of actions already executed.
- `ΔT_acc`: drift of the adaptation space, including emergence of new options and disappearance/invalidation of existing ones.
- `Reach`: downstream configurations/tasks achievable through available adaptations.
- `Trajectory`: adaptation/learning evolution over time.
- `Outcome`: quality/goal satisfaction of the self-adaptive system.
- `Value`: quality properties and adaptation-goal satisfaction, not TGCV's general value construction.
- mechanism: environmental/system uncertainty and learning-model/lifelong-adaptation response.

## AC2 assessment

This source strongly absorbs the claim that a changing set of future adaptation options can itself be an explicit analytical problem. It also shows that the space may drift without requiring software evolution, because uncertainty can change which options remain useful or emerge. citeturn1search12turn1academia25

## AC3 assessment

AC3 is **not established**. The remaining blockers are:

1. the object is adaptation options in self-adaptive software, not arbitrary transformations across domains;
2. the accessibility predicate is architecture/domain-specific rather than a transversal `P_τ(S,C,L)`;
3. the paper does not elevate `ΔT_acc` as a domain-independent explanatory variable separate from the mechanisms producing drift;
4. the downstream relation is centered on learning/self-adaptation performance rather than a general `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value` architecture;
5. no general theory of value construction is supplied.

## Decision

- `AC2`: **VERY STRONG / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Broad novelty claim concerning drift/change of adaptation spaces: **absorbed**.
- TGCV Core: **UNCHANGED**.
- EXT-1.1: **NOT USED**.
