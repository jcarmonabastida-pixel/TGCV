# TGCV — C10C-002 Interference / Saturation Gap Resolution 001

**Status:** DESIGN-LEVEL GAP RESOLVED; DATA-PROVENANCE GAP REMAINS
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Purpose

Resolve the remaining C10-C admission gap concerning municipal saturation and interference without reopening the completed bounded causal experiment and without treating undocumented deposited variables as if their meaning were known.

## 2. Documentary finding

The published methodological record establishes that the experiment used a **randomized saturation design** and explicitly studied municipal-level spillovers. The 2014 McIntosh et al. paper states that the saturation design was used to study how municipal-level spillovers could undermine causal inference. citeturn0search0turn0search24

The same methodological paper explicitly formulates the spillover problem as a possible violation of SUTVA and reports that the randomized saturation design provided evidence that spillovers did not occur at a level sufficient to undermine the study's internal validity. citeturn0search2

This is **published study-level evidence about the interference question**. It is not treated as a substitute for variable-level provenance in the deposited replication data.

## 3. Controlled-data finding

The admitted V1 reconstruction contains 60 municipalities, with treatment variation within municipalities. The deposited analysis script uses municipal identifiers (`cve_mun`) and treatment/saturation-related fields (`treat`, `treat_r2`, `r2`, and related variables), confirming that municipal-level treatment intensity was part of the empirical design.

However, the controlled inspection also established that the precise provenance/definition of deposited `sat`, `sat_treat`, `r2` and related fields is not sufficiently documented in the deposited script itself. Those variables therefore cannot be silently interpreted or substituted into a causal estimand.

## 4. Resolution

The gap is split into two distinct questions:

### 4.1 Design-level interference question — RESOLVED

The published methodological record establishes that:

- treatment was implemented under a randomized saturation design;
- municipal-level spillovers were an explicit identification concern;
- the study explicitly analyzed the possibility of spillovers rather than assuming universal SUTVA;
- the published analysis reports evidence consistent with spillovers not occurring at a magnitude sufficient to undermine the principal causal interpretation.

Thus, the existence, methodological relevance, and published empirical treatment of interference/saturation are established.

### 4.2 Variable-level provenance question — UNRESOLVED

The exact meaning and construction of the deposited saturation variables cannot be established solely from the admitted V1 script/data documentation without relying on inference.

Therefore the programme must **not** use `sat`, `sat_treat`, `r2` or related undocumented fields as analysis variables merely because they exist in the replication data.

## 5. Permitted causal-design consequence

The published spillover analysis may be used as documentary evidence that interference was explicitly addressed by the original study. It does **not** authorize importing the authors' analytical choices into the TGCV execution specification without an ex-ante governance decision.

A future execution specification may proceed without the deposited `sat` variable only if it formally documents why the primary estimand is identifiable without conditioning on that undocumented field and freezes the corresponding interference robustness rule before estimation.

A deterministic observed municipal treatment share computed directly from admitted `treat` values remains conceptually distinct from the deposited `sat` variable and may be considered only if its construction is frozen ex ante and its relationship to the randomized assignment mechanism is documented sufficiently for the intended estimand.

No such substitution is authorized by this record.

## 6. Current admission decision

**C10C-002 remains PROMISING / EVIDENCE GAP REMAINS.**

The remaining gap is now narrowly defined as the **provenance and admissible operationalization of the saturation variable, or a formally justified ex-ante decision to proceed without the undocumented deposited saturation fields**.

The published study-level evidence on interference does not by itself close this data-level governance condition.

## 7. Execution boundary

Causal estimation remains **NOT AUTHORIZED**.

Before execution, the candidate-specific causal specification must freeze:

1. the exact estimand;
2. whether saturation is part of the estimand or an identification condition;
3. the exact saturation variable and source definition, or a documented decision to proceed without the undocumented deposited saturation variables;
4. the counterfactual under the randomized saturation design;
5. treatment/state/accessibility separation;
6. value endpoint and linkage;
7. uncertainty/cluster structure;
8. independent reproducibility procedure.

## 8. Non-reopening rule

This record does not reopen C10C-002's prior bounded causal experiment and does not alter its negative result. It records a separate methodological value-linkage admission finding.

## 9. Sources

- McIntosh, Alegría, Ordóñez & Zenteno, *Infrastructure Upgrading and Budgeting Spillovers: Mexico's Hábitat Experiment* (2014), eScholarship/UC Berkeley.
- McIntosh, Alegría, Ordóñez & Zenteno, *The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico* (2018), American Economic Journal: Applied Economics.
- OpenICPSR 113705 V1 replication deposit and its deposited scripts/data.
