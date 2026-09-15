# TGCV C10C-002 — B4 Household-to-Polygon State Provenance Limitation 001

## Status

`FROZEN — MATERIAL STRUCTURAL PROVENANCE LIMITATION; B4 NOT CLOSED; EMPIRICAL CAUSAL EXECUTION NOT AUTHORIZED`

## Finding

The admitted V1 replication script establishes the six infrastructure variables as household-level analytical variables. It does not establish a documented deterministic transformation from household observations to one binary infrastructure state per `N_POLIGONO × round`.

The script defines the infrastructure family as `Disp_Agua`, `Disp_Drenaje`, `Disp_Luz`, `Alumbrado_Siempre_Enc`, `Disp_Guarniciones`, `Disp_Banquetas`, and `Disp_Pavimento`. fileciteturn201file0L27-L36

It then analyses these variables directly with household observations, using `m_Factor_C` and clustering at `N_POLIGONO`; for example, `Disp_Agua` is regressed directly and the six-dimensional variables are subsequently used through the corresponding `d_Disp_*` change variables. fileciteturn201file0L108-L129

The deposited `b_Disp_*` and `d_Disp_*` variables are themselves household-level baseline/change constructs used in regressions. The script explicitly uses `d_Disp_Agua`, `b_Disp_Agua`, `d_Disp_Drenaje`, and `b_Disp_Drenaje` in this manner. fileciteturn199file1L48-L55 fileciteturn200file14L648-L665

The reviewed explicit `collapse` command concerns construction variables and does not provide the missing six-dimensional household-to-polygon rule. fileciteturn197file4L137-L146

## Consequence for TGCV reconstruction

A polygon-level `T_acc,0`, `T_acc,1`, and `ΔT_acc` cannot be reconstructed from the admitted V1 evidence without introducing an additional aggregation rule.

The following alternatives are therefore **not admissible unless independently documented and frozen**:

- unanimity;
- majority vote;
- weighted mean plus threshold;
- any-observation/presence rule;
- median or other quantile;
- outcome-informed threshold;
- treatment-informed classification;
- saturation-informed classification.

The current B4 verifier's unanimity rule is explicitly withdrawn by the preceding diagnostic.

## Methodological disposition

The evidence supports a household-level infrastructure state/change representation, but the current causal execution design requires linkage to an independent polygon-level value endpoint. A deterministic household-to-polygon state mapping is therefore a material missing operationalization condition for the proposed TGCV structural pathway.

No heuristic aggregation will be introduced merely to make B4 pass.

## Decision

`B4 MATERIAL BLOCKER — HOUSEHOLD-TO-POLYGON STRUCTURAL STATE MAPPING NOT PROVEN FROM ADMITTED V1 EVIDENCE`

B4 remains open. B5 remains separate. No causal estimation or claim upgrade is authorized.
