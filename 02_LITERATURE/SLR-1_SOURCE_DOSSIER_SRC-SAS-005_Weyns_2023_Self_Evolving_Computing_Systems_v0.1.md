# SLR-1 Source Dossier — SRC-SAS-005

**Status:** RECONSTRUCTED / WORKING  
**Source:** Danny Weyns, Thomas Bäck, René Vidal, Xin Yao & Ahmed Nabil Belbachir (2023), *The Vision of Self-Evolving Computing Systems*, Journal of Integrated Design and Process Science 26(3–4), 351–367, DOI 10.3233/JID-220003. citeturn2search0turn2search4  
**Related source:** Danny Weyns & Jesper Andersson (2023), *From Self-Adaptation to Self-Evolution Leveraging the Operational Design Domain*, SEAMS 2023, DOI 10.1109/SEAMS59076.2023.00022. citeturn2academia24turn2search2  
**Classification:** **AC2 — VERY STRONG / NEAR-DIRECT STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Why this source matters

This is the first source in the current bounded pass that explicitly crosses from ordinary self-adaptation into **self-evolution**. It defines the target of self-evolution as changing the operational design domain itself, including unanticipated goals, constraints and anomalies, and proposes an evolutionary engine that runs online experiments, evolves the system architecture and can integrate new computing elements. citeturn2search0turn2academia24

The companion ODD paper makes the boundary explicit: self-adaptive capabilities are constrained by the initial operational design domain, while conditions outside that domain require evolution; the proposed direction is autonomous evolution to handle conditions not anticipated initially. citeturn2academia24turn2search2

## TGCV mapping

- `S`: runtime architectural/system representation.
- `C`: goals, constraints and environmental/context conditions.
- `T_acc`: implicitly, the set of architectural adaptations/evolution variants that can be generated and evaluated.
- accessibility predicate: constrained by the operational design domain, architectural feasibility and available auto-evolution-enabled computing elements.
- mechanism: evolutionary learning engine / evolutionary learning pipeline.
- state change: evolution replaces the running architecture with a novel architecture.
- reachability: candidate variants are generated and experimented with, but no general TGCV reachability object is defined.
- trajectory: evolutionary sequence of model variants is present, but not formalized as a domain-independent trajectory of accessible transformations.
- outcome/value: performance/goal satisfaction metrics guide optimization, but no general theory of value construction is proposed.

## AC2 assessment

AC2 is **VERY STRONG / NEAR-DIRECT**. The source establishes prior art for:

1. a system whose capabilities are bounded by an operational domain;
2. explicit distinction between anticipated adaptation and unanticipated change requiring evolution;
3. autonomous generation/evaluation of alternative system variants;
4. runtime architectural evolution;
5. integration of new system capabilities/elements;
6. online experimental selection of evolved variants;
7. expansion of the system's operational domain through self-evolution. citeturn2search0turn2academia24

This absorbs any broad novelty claim that systems can autonomously alter their future capability envelope or evolve their adaptation logic/domain.

## AC3 assessment

AC3 is **NOT ESTABLISHED** despite the unusually close architectural relationship.

The decisive blockers are:

1. the source does not define a domain-independent transformation `τ`;
2. it does not define `T_acc = {τ | P_τ(S,C,L)=1}` as an explicit transversal analytical object;
3. it does not isolate the mechanism as a variable distinct from the accessible transformation space;
4. `ΔT_acc` is not the central explanatory construct;
5. reachability and trajectory are present only implicitly/locally through generated variants and experiments, not as the explicit `ΔT_acc → ΔReach → ΔTrajectory` chain;
6. outcome assessment is tied to system goals/performance rather than a general `Outcome → Value` construction layer.

Therefore this source is a **major near-boundary antecedent**, but not an identified AC3 absorber.

## Important methodological consequence

This source changes the burden of proof for TGCV. It is no longer sufficient to argue that TGCV is novel because it concerns future possibilities that can change. Prior art already explicitly addresses autonomous evolution of the operational domain and autonomous generation of new capabilities. citeturn2search0turn2academia24

The remaining candidate must therefore be the **transversal analytical representation** and its explicit causal/structural chain, not the existence of self-evolution itself.

## Decision

- `AC2`: **VERY STRONG / NEAR-DIRECT / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Broad novelty of autonomous change to the future capability/operational domain: **absorbed**.
- TGCV Core: **UNCHANGED**.
- EXT-1.1: **NOT USED**.
