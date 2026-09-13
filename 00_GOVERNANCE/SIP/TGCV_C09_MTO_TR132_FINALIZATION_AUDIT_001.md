# TGCV — C09 MTO TR-132 Finalization Audit 001

**Status:** `COMPLETED — TR-132 PASS WITH BOUNDED ENDPOINT / C09 EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** Moving to Opportunity (MTO)
**Parent:** `TGCV_C09_MTO_TR132_SUFFICIENCY_AUDIT_001.md`
**Execution authorization:** `NONE`

## 1. Decision-time unit

Unit = one randomized MTO household at baseline, represented only by pre-randomization state/context `S0,C0` and assignment `Z`.

The causal contrast is restricted to LPV versus TRV, because both are voucher-assignment arms while differing in the relevant geographic accessibility rule. MTO documentation states that LPV vouchers were usable only in census tracts below the 10% 1990-poverty threshold, whereas TRV vouchers were usable anywhere. citeturn0search1turn0search2

## 2. Frozen bounded transformation universe U*

`U* = first voucher-supported residential transformation from the baseline housing state into a dwelling located in a census tract satisfying the applicable voucher rule.`

The transformation class is bounded to **first relocation under the initially assigned voucher regime**. Subsequent voluntary moves are outside `U*` and are not used to redefine accessibility.

This is a deliberate TR-132 bounded representation, not a claim that `U*` equals the complete residential transformation space.

## 3. Frozen accessibility predicates

`P_LPV(τ) = voucher-supported first residential transformation τ has destination census tract with 1990 poverty < 10%.`

`P_TRV(τ) = voucher-supported first residential transformation τ satisfies the ordinary Section 8 geographic rule, without the MTO low-poverty-tract restriction.`

These predicates are fixed from programme rules and assignment, not from realized destination, later neighborhood characteristics, or observed outcomes.

## 4. Frozen causal endpoint and horizon

The bounded endpoint is **long-term adult physical/mental health and subjective well-being measured in the MTO final evaluation (2008–2010)**, with baseline covariates fixed before assignment.

This endpoint is selected because the public-use final-evaluation files contain the analyzed adult outcomes and baseline measures, and the study is explicitly longitudinal from 1994–2010. citeturn0search1turn0search2

The causal horizon is therefore:

`baseline assignment → first-voucher accessibility contrast → long-term adult outcome at 2008–2010.`

No claim is made that every intermediate residential transition is observed or represented in `U*`.

## 5. Omitted-path sufficiency test

### O1 — Can omitted later moves alter the declared causal estimand?

**NO, under the declared endpoint and estimand.**

The estimand is the intent-to-treat effect of randomized LPV versus TRV assignment on the specified long-term adult outcome. Later moves are post-treatment mediating events, not omitted treatment definitions. Their existence does not invalidate the assignment contrast.

### O2 — Can omitted housing transformations create a second treatment assignment pathway?

**NO within the frozen treatment definition.**

The treatment is assignment to LPV versus TRV. The TGCV accessibility contrast is the rule-level difference in the initially assigned voucher's admissible first-move transformation class. Later voucher use or moves are explicitly outside the accessibility intervention definition.

### O3 — Does `P_tau` use post-treatment information?

**NO.**

`P_LPV` and `P_TRV` are programme rules known at assignment. Realized destination, subsequent neighborhood conditions, later moves and outcomes are excluded from the predicate.

### O4 — Does the endpoint require restricted residential-history data?

**NO for the selected endpoint.**

The public-use long-term MTO files contain the adult outcomes and baseline measures analyzed in the associated Science/AER work. ICPSR explicitly describes these as public-use data and identifies individual-level restricted datasets separately. citeturn0search0turn0search1

### O5 — Could omitted transformations change the LPV-vs-TRV assignment contrast itself?

**NO.**

The assignment contrast exists before any realized residential transformation. The omitted transformations are downstream of assignment and therefore cannot alter which arm a household was randomized into.

### O6 — Is the TGCV claim being overextended?

**NO.**

The resulting bounded proposition is only:

`within MTO, for randomized LPV-vs-TRV assignment, the ex-ante geographic accessibility rule for the first voucher-supported residential transformation is a well-defined bounded intervention whose downstream long-term adult outcomes can be compared under the randomized assignment.`

This does not establish that the accessibility rule caused every observed residential trajectory, does not identify mediation through actual moves, and does not establish universal C09 validity across domains.

## 6. TR-132 final disposition

| TR-132 requirement | Result |
|---|---|
| Relevant transformation profile defined pre-treatment | PASS |
| P_tau independent of realized trajectory/outcome | PASS |
| T_acc,0 vs T_acc,1 distinguishable within U* | PASS |
| Treatment/counterfactual identifiable | PASS |
| Endpoint independently reconstructible | PASS, bounded to public-use long-term outcomes |
| Causal estimand testable | PASS |
| Omitted transformations unable to alter declared causal conclusion | PASS, for the declared ITT estimand |
| No post-treatment leakage | PASS |
| Bounded claim boundary explicit | PASS |

## 7. Critical limitation

This TR-132 pass **does not** demonstrate that realized residential accessibility changed as experienced by every treated household, nor that the LPV rule mediated the long-term outcome through actual relocation.

It establishes only that the **rule-level accessibility intervention** is sufficiently represented for the declared randomized LPV-vs-TRV causal question.

Therefore, any later C09 execution must preserve the distinction between:

`assignment → accessibility-rule intervention → outcome`

and the stronger, currently untested mediation claim:

`assignment → realized ΔT_acc → realized trajectory → outcome`.

## 8. Decision

**TR-132 = PASS for the bounded MTO causal question.**

MTO is now an **admissible C09 candidate for operational preflight**, subject to the existing C09 design requirements.

This audit does **not** authorize execution, data acquisition, model fitting, or claim-matrix upgrade.

**Next operation:** C09 MTO operational preflight — verify the exact public-use variable mapping and reproducibility package before any causal execution is admitted.
