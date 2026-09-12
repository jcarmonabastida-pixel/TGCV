# D-OPS-29 — Chicago Voucher Lottery C09 Accessibility Intervention Audit v0.1

**Status:** `CLOSED — STRONG METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Execution:** `NOT AUTHORIZED`
**Candidate:** Chicago Housing Authority Corporation (CHAC) 1997 Section 8 voucher lottery

## 1. Purpose

Apply the strengthened C09 filter to the Chicago voucher lottery without reopening prior MTO work.

## 2. Candidate evidence

In July 1997 CHAC received 82,607 income-eligible applications and randomly assigned lottery positions. The first 35,000 were placed on an active waitlist; households outside that range were told they would not receive a voucher within three years. Voucher offers continued over several years, with an interruption caused by a lawsuit. citeturn1search8turn1search20

The experiment has strong longitudinal follow-up and randomized allocation. Published work uses voucher utilization, residential histories and administrative outcomes. citeturn1search23turn1search10

## 3. C09 gate assessment

| Gate | Result | Finding |
|---|---|---|
| Stable unit | PASS | Individual/household lottery applicant is identifiable. |
| Formal access/allocation rule | PASS — bounded | Lottery position and voucher-offer rule define a concrete housing-access allocation mechanism. |
| Independent intervention | PASS | Lottery position was randomized. |
| `Z → ΔT_acc` | PASS — strong design candidate | Voucher offer changes the set of housing-transition actions that can be initiated with voucher support; this is materially closer to TGCV accessibility than ranking/incentive-only interventions. |
| Counterfactual | PASS | Lottery non-offer group supplies a randomized comparison. |
| Longitudinal trajectory | PASS — bounded | Residential, labor-market and benefit outcomes were tracked for years. |
| Public unit-level state sufficient for execution | **FAIL** | The published analyses rely on administrative and tracking sources, including HUD 50058 and address-tracking data; these are not established here as a fully public unit-level reconstruction package. citeturn1search23 |
| Public reproducibility of `T_acc` | **FAIL** | Public CHA data currently expose aggregate/property/waitlist information, not the historical 1997 applicant-level lottery state required for C09 reconstruction. citeturn1search2turn1search3 |
| Stable transition environment | CONDITIONAL | Historical waitlist service was interrupted and later resumed; a frozen cohort would be required. citeturn1search20 |

## 4. Critical TGCV distinction

This candidate passes the substantive intervention test more strongly than eBay, EDR and OHIE: the randomized treatment changes access to a concrete housing transformation under a formal voucher programme.

However, C09 requires **reconstructible unit-level `T_acc` before observing realized moves**. The currently public CHA portal provides contemporary aggregate/property/waitlist datasets, not the historical applicant-level state required to reconstruct the 1997 lottery cohort. citeturn1search2turn1search5

The published research therefore cannot be treated as a ready-made public C09 dataset merely because the causal experiment exists.

## 5. Decision

**D-OPS-29 = CLOSED — STRONG METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED.**

The Chicago voucher lottery is retained as a strong methodological reference because it combines:

- randomized unit-level allocation;
- a formal housing-access rule;
- direct change in a concrete transformation opportunity;
- randomized counterfactual;
- long-horizon trajectories.

It fails the current execution gate because the historical unit-level public data necessary to reconstruct `T_acc` are not demonstrated as publicly reproducible.

No C09 claim upgrade.
No data acquisition.
No model fitting.
No execution authorization.
No AWS/Rust/SWIM action.

**Consequence:** the search criterion is now narrowed further to candidates where the randomized accessibility intervention and the unit-level pre-treatment state needed to compute `T_acc` are both publicly reconstructible, not merely documented in published research.
