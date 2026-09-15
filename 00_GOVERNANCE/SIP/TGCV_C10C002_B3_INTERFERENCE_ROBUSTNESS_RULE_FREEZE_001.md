# TGCV — C10C-002 B3 Interference Robustness Rule Freeze 001

**Status:** FROZEN — B3 SPECIFICATION CLOSED; EMPIRICAL EXECUTION NOT AUTHORIZED
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico

## 1. Purpose

Freeze the ex-ante treatment of municipal saturation/interference for the future C10-C value-linkage execution, without using undocumented deposited saturation variables and without reopening the completed bounded causal experiment.

## 2. Identification condition

The study used randomized municipal saturation and explicitly treated municipal spillovers as an identification concern. The controlled V1 reconstruction contains 60 municipalities with treatment variation within municipalities.

Therefore interference is **not assumed absent by construction**.

## 3. Primary estimand rule

The primary confirmatory estimand remains the ITT effect of randomized polygon-level assignment `treat` on the independent polygon-level change in professional real-estate value.

The primary estimand will **not condition on** `sat`, `sat_treat`, `r2`, `treat_r2`, or other undocumented saturation fields.

This preserves interpretability of the assignment contrast without relying on undocumented deposited variables.

## 4. Inference rule

The primary inference structure is municipality-clustered because treatment assignment and the interference concern operate at the municipal design level.

The exact implementation will be frozen in the final executable script before estimation and must use the same frozen municipality identifier `cve_mun`.

No alternative standard-error structure may be selected after observing the outcome.

## 5. Saturation robustness rule

The deposited undocumented saturation fields are excluded from causal adjustment.

A deterministic municipal treatment share computed solely from admitted `treat` assignments may be reported as a **design descriptor** if included in the final package, but it is not a causal covariate and may not be introduced to alter the primary ITT estimand after outcome inspection.

No post-treatment saturation measure, outcome-derived saturation classification, or undocumented field may enter the primary regression.

## 6. Interpretation rule

If the primary ITT estimate is obtained under this frozen design, its interpretation is conditional on the experiment's municipal saturation/interference structure. The result must not be described as a universal no-spillover effect.

The published study-level evidence that the original saturation design addressed spillovers may be cited as documentary support, but it does not eliminate the need to preserve the interference qualification in the TGCV execution record.

## 7. Sensitivity boundary

Any additional interference sensitivity analysis must be specified before execution and must use only variables whose provenance and construction are frozen.

No specification search across saturation definitions is permitted.

If the final independent reproduction cannot implement a proposed sensitivity analysis without undocumented assumptions, that sensitivity analysis is omitted rather than reconstructed post hoc.

## 8. B3 disposition

**B3 — CLOSED AS A SPECIFICATION BLOCKER.**

The remaining data-provenance uncertainty concerning deposited saturation fields is explicitly handled by exclusion from the primary estimand, not by guessing their definitions.

This does not constitute empirical evidence that interference is absent.

## 9. Remaining readiness conditions

After B3 closure, remaining conditions are:

- B4 — independent reproduction package;
- B5 — final analysis script/specification hash.

B1 is separately recorded as an irrecoverable endpoint-provenance limitation, and B2 has been frozen at the directly documented endpoint-definition level.

## 10. Governance boundary

This record:

- does not authorize causal estimation;
- does not reopen T17;
- does not repeat T10–T16-B;
- does not infer saturation-variable definitions;
- does not upgrade the candidate claim;
- does not modify the frozen TGCV causal target.

**Current candidate state: PROMISING / EVIDENCE GAP REMAINS.**
**Empirical causal execution: NOT AUTHORIZED.**
