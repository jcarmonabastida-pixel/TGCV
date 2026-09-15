# TGCV C10C-002 — B4 Structural-Level Mismatch Diagnostic 001

## Status

`FROZEN — B4 DIAGNOSTIC; INDEPENDENT REPRODUCTION NOT CLOSED; EMPIRICAL CAUSAL EXECUTION NOT AUTHORIZED`

## Purpose

Record the result of the controlled review of the V1 household replication script after B4 verifier run `B4_RESULT_002.json` failed the bounded structural reconstruction check because the verifier imposed an unsupported polygon-round unanimity rule.

This diagnostic does **not** authorize a new aggregation rule and does **not** alter the frozen causal design.

## Finding

The V1 household replication script treats the six infrastructure variables as household-level analytical variables. The script repeatedly estimates `Disp_Agua`, `Disp_Drenaje`, `Disp_Luz`, `Disp_Guarniciones`, `Disp_Banquetas`, and `Disp_Pavimento` directly with household observations and polygon-clustered inference. It also contains baseline/change variables such as `b_Disp_Agua` and `d_Disp_Agua`, but the reviewed V1 material does not establish a deterministic rule converting these household-level variables into one binary structural state per `N_POLIGONO × round`.

The script evidence therefore does **not** justify the verifier's previous rule:

`polygon × round → retain value only if all non-missing household observations agree`.

That rule is a verifier heuristic and is withdrawn.

## Evidence

The V1 script defines the six variables in the infrastructure analytical family. fileciteturn195file0L23-L39

The script directly regresses `Disp_Agua` and the infrastructure family using household records, with polygon clustering, rather than first establishing a polygon-level binary transformation state. fileciteturn195file0L143-L168

The script also directly uses the baseline/change variables `b_Disp_*` and `d_Disp_*` in household-level regressions, again with `N_POLIGONO` as the clustering level. fileciteturn196file0L173-L189 fileciteturn196file0L195-L226

The V1 code does contain an explicit `collapse` command, but the reviewed occurrence collapses construction variables such as `constr_agua_alt`, `constr_drenaje_alt`, and `constr_pavimen_alt`; it does **not** establish the required six-dimensional `Disp_*` polygon state. fileciteturn196file0L163-L171

## Consequence for B4

The `B4_RESULT_002.json` result is correctly interpreted as:

- input hashes: PASS;
- 342/342 panel linkage: PASS;
- treatment/state separation: PASS;
- endpoint linkage: PASS;
- undocumented saturation exclusion: PASS;
- bounded structural reconstruction: **REVIEW / NOT ESTABLISHED**;
- causal estimation: NOT PERFORMED.

The 331 conflicts are therefore **not evidence that the dataset is defective**. They demonstrate that the verifier attempted to impose a polygon-level state representation that has not yet been justified from the admitted V1 evidence.

## Methodological disposition

1. Withdraw the unanimity aggregation rule from the B4 verifier as an admissible reconstruction rule.
2. Do not replace it with mean, majority, any-observation, threshold, or other aggregation without explicit V1 provenance or a separately frozen TGCV operational rule.
3. Do not infer a polygon state from treatment assignment, value outcomes, saturation variables, or post-treatment results.
4. Do not reopen the closed T17 causal result.
5. Keep B4 OPEN and keep B5 separate.
6. The next admissible task is to establish whether a reproducible polygon-level structural state can be reconstructed from admitted V1 evidence at all. If not, the correct outcome is an evidence-gap limitation rather than a heuristic repair.

## Decision

`B4 REMAINS OPEN — STRUCTURAL-LEVEL OPERATIONALIZATION NOT YET ESTABLISHED`

No empirical causal execution is authorized.
