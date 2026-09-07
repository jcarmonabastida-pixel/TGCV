# SLR-1 Source Dossier — SRC-DSPL-001

**Status:** RECONSTRUCTED / WORKING  
**Source:** Inmaculada Ayala, Alessandro V. Papadopoulos, Mercedes Amor & Lidia Fuentes (2021), *ProDSPL: Proactive self-adaptation based on Dynamic Software Product Lines*, Journal of Systems and Software 175, 110909. DOI 10.1016/j.jss.2021.110909. citeturn0search0turn0search2  
**Classification:** **AC2 — VERY STRONG STRUCTURAL ANTECEDENT; AC3 NOT ESTABLISHED**

## Why this source matters

ProDSPL combines Dynamic Software Product Lines with proactive control. DSPL models dynamic variability and alternative runtime adaptations; ProDSPL generates valid configurations at runtime and optimizes them over a prediction horizon. Valid extended-feature-model configurations are encoded as linear constraints, while an automatically learned system model anticipates future variations and their impact on quality requirements. citeturn0search0turn0search3

This makes the source particularly relevant to the SLR-1 question because it combines an explicit configuration space, an accessibility/validity constraint, runtime recomputation, anticipation of future conditions, and downstream quality consequences.

## TGCV mapping

- `S`: current software system plus relevant environment/context.
- `C`: runtime context, requirements and feature-model state.
- `T_acc`: valid DSPL configurations / possible adaptations — strong domain-specific analogue.
- accessibility predicate: feature-model constraints defining valid configurations.
- execution vs accessibility: valid configurations are generated as possibilities; the controller subsequently selects/reconfigures the running system.
- `ΔT_acc`: possible configuration set can vary as context/feature constraints and learned system conditions evolve; however, this delta is not isolated as an independent analytical object.
- `Reach`: configurations available over the prediction horizon and adaptation sequences.
- `Trajectory`: proactive reconfiguration sequence selected by the controller.
- `Outcome`: system quality and stability under anticipated future variations.
- `Value`: quality requirements/utility of configurations, not a general value-construction theory.
- mechanism: proactive control + DSPL variability management + learned predictive model.

## AC2 assessment

AC2 is **VERY STRONG / CONFIRMED**. The source absorbs prior-art claims that TGCV might otherwise make about:

1. representing future adaptation possibilities through a constrained configuration space;
2. separating valid/possible configurations from the configuration actually selected;
3. recomputing/optimizing runtime alternatives under changing context;
4. linking alternative-space selection to future trajectories and quality outcomes;
5. using explicit structural constraints to define the accessible configuration space. citeturn0search0

The broader SPL literature also establishes that variability management and product-line evolution are longstanding areas, including binding time, evolution and dynamic software product lines. citeturn0search1turn0search5

## AC3 assessment

AC3 is **NOT ESTABLISHED** because:

1. the transformation candidates are software configurations/adaptations, not domain-independent transformations `τ`;
2. the accessibility predicate is a DSPL feature-model constraint system rather than a transversal predicate `P_τ(S,C,L)`;
3. changing accessibility is not promoted to the general explanatory variable `ΔT_acc`;
4. mechanism and accessible-transformation object are not separated in a domain-independent ontology;
5. the downstream relation is a proactive-control/quality-optimization architecture, not the general TGCV chain `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`;
6. value is represented through quality requirements/utility, not through a transversal theory of value construction.

## Decision

- `AC2`: **VERY STRONG / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Novelty of dynamic variability/configuration spaces and runtime recomputation in DSPLs: **absorbed**.
- Novelty of proactive optimization over a changing configuration space: **absorbed** as domain-specific prior art.
- TGCV Core: **UNCHANGED**.
- EXT-1.1: **NOT USED**.
