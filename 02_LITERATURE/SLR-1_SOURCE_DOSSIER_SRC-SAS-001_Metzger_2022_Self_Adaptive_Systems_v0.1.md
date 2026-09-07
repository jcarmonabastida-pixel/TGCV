# SLR-1 Source Dossier — SRC-SAS-001

**Status:** RECONSTRUCTED / WORKING  
**Source:** Andreas Metzger, Clément Quinton, Zoltán Ádám Mann, Luciano Baresi, Klaus Pohl et al. (2022/2024), *Realizing self-adaptive systems via online reinforcement learning and feature-model-guided exploration*, Computing 106, 1251–1272. DOI: 10.1007/s00607-022-01052-x.  
**Classification:** **AC2 — VERY STRONG STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Reason for inclusion

This source is a direct test of the remaining TGCV boundary because it explicitly defines a self-adaptive system's **adaptation space** as a set of possible runtime configurations/actions and then analyzes how system evolution changes that space. It distinguishes adaptation from evolution and computes added and removed adaptation actions through feature-model differences. citeturn1search0turn1search1

## Core evidence

The paper formalizes an adaptation space in which each adaptation action is represented by a valid feature combination specifying a target runtime configuration. It then compares feature models before and after an evolution step and derives:

- added configurations: `M' \ M`;
- removed configurations: `M \ M'`.

Added adaptation actions are explored first; removed actions are no longer executed and corresponding learned knowledge can be pruned. citeturn1search1

This is unusually close to the TGCV concept of an explicitly represented changing accessible repertoire.

## TGCV mapping

| TGCV element | Source analogue | Assessment |
|---|---|---|
| `S` | monitored system/environment state | explicit |
| `C` | feature-model/system configuration | explicit |
| `T_acc` | adaptation space / valid runtime configurations | **very strong analogue** |
| accessibility predicate | feature-model constraints defining valid configurations | **explicit** |
| execution vs accessibility | possible adaptation actions vs selected/executed action | **explicit** |
| `ΔT_acc` | added/removed configurations between `M` and `M'` | **explicit** |
| `Reach` | configurations explored by the adaptation policy | partial/explicit operationally |
| `Trajectory` | sequence of adaptation decisions over time | operationally present |
| `Outcome` | system/environment state and quality response | explicit |
| `Value` | reward / quality requirements / learning performance | explicit but domain-specific |
| mechanism | system evolution / feature-model change | explicit |

## AC2 assessment

**AC2 — VERY STRONG STRUCTURAL ANTECEDENT CONFIRMED.**

The source establishes prior art for all of the following subclaims:

1. a system can possess an explicit space of possible adaptations;
2. that space is constrained by a formal representation;
3. possible adaptations are distinct from the action actually executed;
4. system evolution can add and remove members of the adaptation space;
5. those changes affect subsequent exploration and learning performance.

The paper therefore materially absorbs the broad novelty claim that TGCV is the first framework to make a state/configuration-conditioned repertoire of future actions explicit and to analyze its evolution. citeturn1search1

## AC3 assessment

**AC3 — NOT ESTABLISHED.**

Despite its strength, the source does not establish the full TGCV architecture:

1. **Adaptation-action scope:** the repertoire consists of adaptation actions/configurations for self-adaptive software, not a domain-independent space of arbitrary transformations of a system.
2. **No transversal transformation predicate:** feature-model validity is a domain-specific constraint formalism rather than a general `P_τ(S,C,L)` definition for arbitrary transformations.
3. **Mechanism scope:** evolution changes the adaptation space, but the paper does not abstract the mechanism as a domain-independent explanatory variable separated from the accessible transformation object.
4. **No independent `ΔT_acc` construct:** set difference is operationally computed, but change in accessible transformations is not elevated as the central cross-domain analytical object.
5. **Downstream chain differs:** the paper connects adaptation-space change to exploration and learning performance, but does not establish the general `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value` architecture.

## Falsification significance

This source substantially narrows the remaining TGCV originality claim. In particular, TGCV cannot claim novelty for:

> explicitly representing a condition-constrained set of future actions/adaptations and measuring additions/removals in that set after system evolution.

The remaining candidate contribution is narrower:

> a domain-independent analytical abstraction in which **transformations themselves** are the members of an accessible transformation space, accessibility is represented by a general predicate over system/context/level, the change of that space (`ΔT_acc`) is the central analytical object, and that change is systematically related to downstream reachability, trajectories, outcomes and value construction, with the mechanism producing the change represented separately.

## Decision

- `AC2`: **VERY STRONG / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Broad novelty of changing adaptation/action spaces: **absorbed**.
- TGCV Core: **UNCHANGED**.
- EXT-1.1: not used.
- This source should become a principal member of the **self-adaptive systems / runtime adaptation cluster** for subsequent comparative screening.
