# TGCV — C09 MTO Endpoint / Public-Package Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / C09 EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** Moving to Opportunity (MTO)
**Parent:** `TGCV_C09_MTO_TR132_OMITTED_PATH_FINALIZATION_001.md`
**Execution authorization:** `NONE`

## 1. Objective

Determine whether the bounded MTO C09 design has a trajectory endpoint that is independently reconstructible from the admissible public-use package, without importing restricted residential-history data or changing the causal unit.

## 2. Public-package evidence

The ICPSR MTO public-use collections provide long-term outcomes, mediators and baseline measures for the 2008–2010 evaluation. ICPSR describes the public-use collection as individual observations, but the associated replication package is explicitly limited to variables needed to roughly replicate the published findings. The MTO public-use dissemination also includes cell-level and pseudo-individual representations; NBER explicitly warns that these are not actual individual-level data and are useful for site/treatment-group comparisons rather than other individual-level analyses.

The richer individual-level final-evaluation dataset is restricted-access. NBER and ICPSR identify residential-history information and other richer longitudinal linkage as part of restricted data resources.

## 3. Endpoint candidates screened

### E1 — Long-term adult subjective well-being / health endpoint

**CONDITIONALLY OBSERVABLE, NOT SUFFICIENT FOR CURRENT C09 REPRESENTATION.**

The endpoint is publicly documented and downstream of random assignment, but it is an outcome rather than a reconstructible transformation trajectory. It therefore cannot by itself repair the missing unit-level representation needed to establish the bounded first-move accessibility contrast.

### E2 — Long-term neighborhood outcome

**NOT ADMITTED.**

The public package contains neighborhood-related outcomes/mediators, but using the realized downstream neighborhood classification to define or reconstruct accessibility would violate the frozen information firewall. The endpoint can be an outcome only if the treatment-side accessibility contrast is independently reconstructed at the same admissible unit level.

### E3 — First residential relocation / subsequent residential trajectory

**BLOCKED BY PUBLIC-PACKAGE PROVENANCE.**

The required detailed residential-history reconstruction is not established in the unrestricted public-use package. The richer longitudinal residential-history linkage is associated with restricted data. Importing it would violate the current no-restricted-data boundary.

## 4. Unit-consistency test

The decisive failure is not absence of a downstream MTO outcome. Such outcomes exist publicly.

The failure is that the current admissible public package does not establish, for the same randomized unit, both:

`T_acc,LPV(U*)` and `T_acc,TRV(U*)`

and an independently reconstructible post-decision trajectory while preserving the frozen pre-treatment information boundary.

Cell-level or pseudo-individual public-use representations cannot be promoted to individual causal reconstruction merely because they contain 3,273 rows; NBER explicitly states that these representations are not actual individual-level data.

## 5. TR-132 operational decision

| Criterion | Result |
|---|---|
| Frozen bounded U* | PASS |
| Ex-ante LPV/TRV predicates | PASS |
| Randomized counterfactual | PASS |
| Public downstream outcomes | PASS |
| Unit-level public `T_acc,0/T_acc,1` reconstruction | FAIL |
| Independent public first-move trajectory reconstruction | FAIL |
| Information-firewall integrity | PASS |
| Public-only operational reproducibility | FAIL |
| C09 execution admissibility | **BLOCKED** |

## 6. Decision

**MTO is not admitted for C09 execution under the current public-only evidence boundary.**

This result does not falsify C09 and does not invalidate the TR-132 bounded-design result. It establishes that MTO's strong randomized intervention and public outcome availability are insufficient when the TGCV-specific accessibility representation must remain independently reconstructible at the causal unit level.

The restricted MTO final-evaluation datasets are explicitly excluded from this programme stage. No restricted-data request is authorized.

## 7. Governance consequence

MTO is downgraded from `ACTIVE C09 CANDIDATE` to `METHODOLOGICAL REFERENCE — PUBLIC-ONLY PREFLIGHT BLOCKED`.

No claim-matrix upgrade.
No causal result.
No data acquisition.
No restricted-data request.
No model fitting.
No execution authorization.
No AWS/Rust/SWIM execution.

## 8. Next operation

Return to the reconciled TR-132 candidate ranking and perform the **Chicago voucher lottery dedicated TR-132 operational sufficiency audit**, unless a higher-quality admissible candidate is identified by an independent candidate-class gate.
