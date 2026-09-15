# TGCV — C10C-002 Pre-Execution Readiness Gap Register 001

**Status:** FROZEN — READINESS REGISTER; EMPIRICAL EXECUTION NOT AUTHORIZED
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Purpose

Consolidate the remaining conditions that must be satisfied before any C10-C empirical execution can be authorized, after resolution of the design-level saturation question.

This register is a governance/status artifact only. It does not alter the frozen causal design and does not reopen T17.

## 2. Conditions already resolved for readiness purposes

### R1 — Bounded structural universe
**Status: RESOLVED AT THE TRANSFORMATION-DEFINITION LEVEL; POLYGON-LEVEL STATE RECONSTRUCTION NOT RESOLVED.**

The admissible structural universe contains six elemental infrastructure dimensions and 12 opening/closure transformations. The transformation definitions are frozen. However, the independent B4 reproduction has established that the admitted V1 evidence does not yet prove a deterministic household-to-polygon mapping capable of producing reproducible binary structural states for all 342 polygons at both rounds. Therefore `T_acc,0`, `T_acc,1`, and `ΔT_acc` are **not currently reproducible at the required polygon level**.

### R2 — Treatment/state separation
**Status: RESOLVED.**

`treat` remains the assignment variable. The six `Disp_*` infrastructure variables are structurally distinct from treatment and value variables. However, the polygon-level structural state required by the frozen causal pathway remains subject to the B4 household-to-polygon provenance limitation.

### R3 — Design-level saturation/interference identification concern
**Status: RESOLVED AS A DESIGN QUESTION.**

The published study establishes randomized saturation and explicit municipal spillover analysis. The undocumented deposited fields `sat`, `sat_treat` and `r2` remain excluded from the primary estimand.

The formal disposition is to proceed conceptually without those undocumented fields, while retaining interference as an identification/robustness issue.

## 3. Conditions closed or formally disposed

### B1 — Endpoint upstream construction provenance
**Status: CLOSED AS IRRECOVERABLE PROVENANCE LIMITATION.**

The deposited endpoint variable `precios_diferencia_usd` is identified and directly used by the authors' replication script, but the script does not construct it. The exact upstream construction of `precios_diferencia` and its USD representation is not recoverable from the admitted V1 script/metadata without inference.

The direct check also establishes that `precios_diferencia` is not equal to `valor_co_12 - valor_co_09`.

No inferred formula is admissible. The limitation is formally recorded in `TGCV_C10C002_ENDPOINT_PROVENANCE_IRRECOVERABLE_LIMITATION_001.md`.

### B2 — Endpoint field/unit/time/aggregation freeze
**Status: CLOSED AT DOCUMENTED EVIDENCE LEVEL; PROVENANCE LIMITATION RETAINED.**

The primary deposited field is `precios_diferencia_usd`, documented as change in professional real-estate price/value per square meter in real 2012 USD, at polygon level, over the baseline/follow-up valuation period. The endpoint is observed for 138 of 342 polygons.

The exact upstream construction remains unavailable and is governed by the B1 limitation record. No imputation or inferred transformation is authorized.

### B3 — Interference robustness rule
**Status: CLOSED — SPECIFICATION FROZEN.**

The primary ITT estimand will not condition on undocumented `sat`, `sat_treat`, `r2`, `treat_r2` or related fields. Interference is not assumed absent. Primary inference is municipality-clustered using `cve_mun`; any additional sensitivity analysis must be frozen ex ante using only provenance-established variables.

The full rule is recorded in `TGCV_C10C002_B3_INTERFERENCE_ROBUSTNESS_RULE_FREEZE_001.md`.

## 4. Remaining blockers

### B4 — Independent reproduction package
**Status: OPEN — MATERIAL BLOCKER.**

The controlled B4 execution verified all eight frozen V1 input hashes, 342/342 polygon linkage, treatment/state separation, endpoint linkage and exclusion of undocumented saturation fields. However, the bounded structural reconstruction failed because the admitted V1 evidence does not establish a deterministic household-to-polygon mapping for the six `Disp_*` dimensions.

The previous verifier unanimity rule has been withdrawn. No alternative aggregation rule (majority, mean/threshold, presence, median, treatment-informed or outcome-informed classification) is admissible without independent V1 provenance or a separately frozen methodological rule.

This material limitation is formally recorded in:

- `TGCV_C10C002_B4_STRUCTURAL_LEVEL_MISMATCH_DIAGNOSTIC_001.md`
- `TGCV_C10C002_B4_HOUSEHOLD_TO_POLYGON_STATE_PROVENANCE_LIMITATION_001.md`

Accordingly, B4 cannot close as a successful independent reproduction of the polygon-level TGCV structural pathway on the currently admitted evidence.

### B5 — Final analysis script/specification hash
**Status: OPEN.**

The final execution script/specification has not yet been frozen and hashed. No empirical result may be generated before this condition is satisfied.

## 5. Authorization threshold

Empirical execution may be authorized only when all material blockers are closed or explicitly accepted as irrecoverable limitations under a documented governance decision that preserves reproducibility and falsifiability.

At minimum, authorization requires:

- endpoint limitation explicitly governed;
- exact endpoint field and documented unit frozen;
- endpoint time/aggregation/missingness rules frozen to the extent supported by admitted evidence;
- interference robustness rule frozen;
- final script/specification hash frozen;
- independent executor package and reproduction test completed; and
- a reproducible polygon-level structural state mapping established, or its absence explicitly accepted as an irrecoverable limitation with the causal design correspondingly not executed.

## 6. Current decision

**C10C-002: PROMISING / EVIDENCE GAP REMAINS.**

**EMPIRICAL CAUSAL EXECUTION: NOT AUTHORIZED.**

The candidate is not rejected. The remaining work is now a finite readiness problem centered on B4, with B5 dependent on a valid execution-ready design.

## 7. Non-reopening rule

This register does not reopen:

- the completed C10C-002 bounded causal experiment;
- T17;
- T10–T16-B;
- the frozen C10-C causal design.

It does not introduce a new estimand and does not authorize any causal regression.
