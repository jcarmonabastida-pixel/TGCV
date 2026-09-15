# TGCV — C10C-002 Interference / Saturation Gap Resolution 001

**Status:** DESIGN-LEVEL GAP RESOLVED; DATA-PROVENANCE GAP REMAINS
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Purpose

Resolve the remaining C10-C admission gap concerning municipal saturation and interference without reopening the completed bounded causal experiment and without treating undocumented deposited variables as if their meaning were known.

## 2. Documentary finding

The published study documentation independently establishes that the experiment used a **randomized saturation design** and explicitly studied municipal-level spillovers. The published research therefore confirms that saturation/interference is not an accidental afterthought: it is a design feature relevant to causal identification. citeturn1search1turn1search13

The AEA publication describes the intervention as randomized across low-income urban neighborhoods in 60 municipalities and reports infrastructure and real-estate effects. citeturn0search0turn0search1

## 3. Controlled-data finding

The admitted V1 reconstruction contains 60 municipalities, with treatment variation within municipalities. The deposited analysis script uses municipal identifiers (`cve_mun`) and treatment/saturation-related fields (`treat`, `treat_r2`, `r2`, and related variables), confirming that municipal-level treatment intensity was part of the empirical design.

However, the controlled inspection also established that the precise provenance/definition of deposited `sat`, `sat_treat`, `r2` and related fields is not sufficiently documented in the deposited script itself. Those variables therefore cannot be silently interpreted or substituted into a causal estimand.

## 4. Resolution

The gap is split into two distinct questions:

### 4.1 Design-level interference question — RESOLVED

The study's published methodological record establishes that:

- treatment was implemented under a randomized saturation design;
- municipal-level spillovers were an explicit identification concern;
- the study was designed to permit analysis of treatment intensity/saturation rather than assuming universal SUTVA.

Thus, the existence and methodological relevance of interference/saturation are established rather than unknown.

### 4.2 Variable-level provenance question — UNRESOLVED

The exact meaning and construction of the deposited saturation variables cannot be established solely from the admitted V1 script/data documentation without relying on inference.

Therefore the programme must **not** use `sat`, `sat_treat`, `r2` or related undocumented fields as analysis variables merely because they exist in the replication data.

## 5. Permitted causal-design consequence

A future execution specification may treat municipal saturation/interference as an explicit design feature and may use only a saturation/intensity variable whose definition and construction are independently documented and frozen before estimation.

A deterministic observed municipal treatment share computed directly from admitted `treat` values is conceptually distinct from the deposited `sat` variable and may be considered only if its construction is frozen ex ante and its relationship to the randomized assignment mechanism is documented sufficiently for the intended estimand.

No such substitution is authorized by this record.

## 6. Current admission decision

**C10C-002 remains PROMISING / EVIDENCE GAP REMAINS.**

The remaining gap is narrower than previously stated: it is no longer “whether the experiment has a saturation/interference design”; it is the **provenance and admissible operationalization of the saturation variable required for the causal estimand**.

## 7. Execution boundary

Causal estimation remains **NOT AUTHORIZED**.

Before execution, a separate candidate-specific causal specification must freeze:

1. the exact estimand;
2. whether saturation is part of the estimand or an identification condition;
3. the exact saturation variable and source definition;
4. the counterfactual under the randomized saturation design;
5. treatment/state/accessibility separation;
6. value endpoint and linkage;
7. uncertainty/cluster structure;
8. independent reproducibility procedure.

## 8. Non-reopening rule

This record does not reopen C10C-002's prior bounded causal experiment and does not alter its negative result. It records a separate methodological value-linkage admission finding.

## 9. Sources

- AEA article: *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico*.
- McIntosh et al., *Infrastructure Upgrading and Budgeting Spillovers: Mexico's Hábitat Experiment*, documenting the randomized saturation design and municipal spillover problem.
- OpenICPSR 113705 V1 replication deposit and its deposited scripts/data.
