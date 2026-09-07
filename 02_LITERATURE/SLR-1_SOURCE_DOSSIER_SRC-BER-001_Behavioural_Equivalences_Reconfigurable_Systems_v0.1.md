# SLR-1 Source Dossier — SRC-BER-001

**Source:** Bogdan Aman & Gabriel Ciobanu, *Behavioural Equivalences over Reconfigurable Systems*, SEFM 2024 Collocated Workshops, pp. 7–21. DOI: 10.1007/978-3-031-94748-3_1.

**Classification:** **AC2 — STRONG STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Evidence basis

The paper is part of the ReacTS 2024 cluster on reconfigurable transition systems. Its stated contribution is behavioural equivalence for reconfigurable systems, building on process-calculus formalisms for systems whose organization and communication structure can change. The workshop programme and proceedings identify the paper explicitly within the ReacTS cluster. citeturn0search0turn1search14turn1search6

Available bibliographic material indicates that the approach extends bisimilarity to account for communicated values and instantiated variables in reactive/reconfigurable systems. Related work by the same authors describes dynamic adjustment of spatial organization and communication structure. citeturn1search1turn1search17

## TGCV mapping

| TGCV element | Source analogue | Assessment |
|---|---|---|
| `S` | reconfigurable process/system configuration | strong |
| `C` | current process/network organization | strong |
| `T_acc` | actions/transitions available in current configuration | strong structural analogue |
| accessibility predicate | enabled/process-calculus transition semantics | implicit/explicit at formal level |
| `ΔT_acc` | reconfiguration altering future behaviour/available actions | structurally present |
| `Reach` | transition-system behaviour/reachable configurations | explicit |
| `Trajectory` | execution behaviour/traces | explicit |
| `Outcome` | resulting system behaviour/configuration | explicit |
| `Value` | behavioural equivalence / verification criterion | not TGCV value construction |
| mechanism | reconfiguration/migration/communication dynamics | explicit domain mechanism |

## AC2 assessment

The paper materially weakens any novelty claim that dynamic reconfiguration can alter the future transition possibilities of a system and that this can be analysed through transition-system semantics and behavioural equivalence.

However, the available evidence does **not** establish AC3 because the contribution remains a formal equivalence theory for a class of reconfigurable process systems. It does not appear to abstract the accessible transformations themselves into a domain-independent analytical object whose change is the primary explanatory variable.

## AC3 blockers

1. No demonstrated transversal `T_acc = F(S,C,L)` abstraction.
2. No explicit research object corresponding to `ΔT_acc` independently of the formal transition semantics.
3. Reconfiguration is model-specific rather than separated as a general explanatory mechanism.
4. Reachability and behaviour are analysed, but not through the TGCV chain `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.
5. Behavioural equivalence is not a general value-construction theory.

## Decision

- AC2: **STRONG / CONFIRMED**.
- AC3: **NOT ESTABLISHED**.
- Broad novelty claim around reconfiguration changing future behaviours/actions: **absorbed**.
- TGCV Core: unchanged.
- EXT-1.1: not used.

## Next use

Keep this source as a strong formal antecedent in the narrow architectural-difference analysis. It should be compared directly with SRC-RTS-001 and SRC-PRG-001 rather than treated as an isolated candidate.
