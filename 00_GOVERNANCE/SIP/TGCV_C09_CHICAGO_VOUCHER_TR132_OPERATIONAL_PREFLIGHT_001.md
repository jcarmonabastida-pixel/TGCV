# TGCV — C09 Chicago Voucher Lottery TR-132 Operational Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** Chicago Housing Voucher Lottery (CHAC, 1997)
**Parent:** `TGCV_C09_RETROSPECTIVE_TR132_CANDIDATE_REVIEW_001.md`
**Execution authorization:** `NONE`

## 1. Frozen causal question

Test whether randomized offer/access to a housing voucher changes a bounded subsequent trajectory/outcome through an accessibility intervention.

Preferred contrast:

`randomized voucher offer → voucher-supported housing accessibility → subsequent administrative trajectory`

The 1997 Chicago lottery involved 82,607 applicants; published research uses administrative records to track outcomes for up to 14 years. citeturn0search0turn0search12

## 2. TR-132 bounded representation

Proposed:

`U* = voucher-supported residential transformations available to an applicant under the CHAC voucher programme during the declared first-offer/lease-up window.`

The intervention is the randomized wait-list offer/position, not the realized move.

The trajectory endpoint must be independently defined from post-randomization administrative records, with treatment assignment and accessibility predicates frozen before outcome inspection.

## 3. Preflight gates

### P1 — Randomized treatment assignment

**PASS.**

The Chicago programme used a randomized housing-voucher wait-list lottery. The published evidence explicitly treats the lottery as the source of experimental identification. citeturn0search0turn0search8

### P2 — Longitudinal outcome data

**PASS — STRONG.**

Published work uses longitudinal administrative data on schooling, arrests and health and follows children for up to 14 years. Other work uses UI earnings, social-programme participation and criminal-record data. citeturn0search0turn0search12

### P3 — Voucher accessibility rule

**CONDITIONAL PASS.**

Voucher offer clearly changes access to the housing-assistance programme and substantially increases voucher utilization. The experimental evidence reports roughly a 40-percentage-point increase in lease-up from a favorable lottery position. citeturn0search14

However, TGCV requires a rule-level transformation-space mapping, not merely voucher utilization. The exact public unit-level representation of the set of feasible residential transformations remains to be established.

### P4 — Unit-level `T_acc,0/T_acc,1`

**OPEN — CRITICAL.**

The underlying research uses HUD 50058 records and several methods to track residential locations, linking those locations to census-tract data. citeturn0search12

This is promising because it indicates that the required accessibility/trajectory variables existed in the research infrastructure. It does **not** establish that the required household-level pre-treatment accessibility representation is publicly reproducible.

### P5 — No post-treatment leakage

**PASS — DESIGNABLE.**

The lottery assignment is pre-outcome. Published work states that administrative-data matching used only pre-randomization sources for the matching process to preserve experimental identification. citeturn0search12

The TGCV accessibility predicate must nevertheless be frozen independently of realized voucher utilization and residential destinations.

### P6 — Counterfactual

**PASS.**

Randomized lottery assignment provides the counterfactual contrast.

### P7 — Endpoint reproducibility

**CONDITIONAL PASS.**

The outcome infrastructure is exceptionally strong, but the relevant administrative microdata are not established here as a public-use package. The existence of published analyses is not equivalent to current reproducibility access.

## 4. Key distinction from MTO

Chicago is materially stronger than MTO on the **longitudinal outcome side**: the literature documents multiple administrative outcome streams extending many years after randomization. citeturn0search0turn0search12

But the same operational issue remains on the TGCV side: the published research's residential-location reconstruction does not by itself establish a public, unit-level, pre-treatment `T_acc` representation.

## 5. Decision

**PRE-FLIGHT = BLOCKED.**

The candidate is retained as a **strong C09 methodological reference**, but is not admitted to causal execution until a governed public-use/accessibility reconstruction package is demonstrated.

No inference of `T_acc` from voucher offer alone.
No substitution of realized moves for ex-ante accessibility.
No restricted-data acquisition.
No model fitting.
No causal claim.
No matrix upgrade.

**Next operation:** perform a controlled Chicago accessibility-data provenance audit to determine whether the required household-level bounded `U*` and `T_acc,0/T_acc,1` can be reconstructed from legitimately accessible public/replication materials. If not, close Chicago operationally and move to NYCHANS.
