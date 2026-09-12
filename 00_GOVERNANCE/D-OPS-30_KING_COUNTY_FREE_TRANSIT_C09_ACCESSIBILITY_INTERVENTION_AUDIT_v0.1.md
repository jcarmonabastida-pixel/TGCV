# D-OPS-30 — King County Free Transit C09 Accessibility Intervention Audit v0.1

**Status:** `CLOSED — PROMISING METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Execution:** `NOT AUTHORIZED`
**Candidate:** King County, Washington randomized free-transit subsidy experiment

## 1. Purpose

Apply the strengthened C09 filter to a randomized intervention that directly changes the monetary accessibility of public-transport transformations.

## 2. Candidate evidence

The King County experiment randomly assigned low-income residents to receive either a transit-pass providing up to six months of free transportation or a regular reduced-fare card with a small preloaded balance. The registered design identifies individual-level random assignment and longitudinal outcomes. citeturn1search5

Published results use administrative transit-card tap records and follow-up surveys and find that free fares sharply increase transit-card use, while persistence after the subsidy is limited. citeturn1search7

A public OpenICPSR replication package exists and contains code plus some data, but explicitly states that some data are not included because of legal limitations on data sharing. citeturn1search8turn1search10

## 3. C09 gate assessment

| Gate | Result | Finding |
|---|---|---|
| Stable unit | PASS | Individual participant/randomization unit. |
| Transformation universe `U_tau` | CONDITIONAL PASS | A bounded universe of transit journeys can be frozen from the service/network schedule and decision window. |
| Pre-execution `P_tau` | PASS — bounded | Fare/payment eligibility can be defined before observed travel. |
| Independent intervention | PASS | Individual random assignment of free-transit access. citeturn1search5 |
| `Z → ΔT_acc` | **PASS — strong design candidate** | Free fare changes the pre-decision affordability/access predicate for otherwise available transit journeys, without defining accessibility from realized taps. |
| Counterfactual | PASS | Randomized reduced-fare comparator. |
| Independent trajectory | PASS — bounded | Subsequent travel behavior is independently observed over the trial window. citeturn1search7 |
| Transition environment | PASS — bounded | The intervention changes fare/access conditions, not the underlying transit network. |
| Public reconstruction of unit-level `T_acc` | **FAIL / NOT DEMONSTRATED** | The replication deposit does not contain all underlying data; the published administrative tap data are not established here as a complete public unit-level package. citeturn1search8 |
| Public reproducibility | **FAIL** | Some replication data are legally unavailable. |

## 4. TGCV interpretation boundary

This candidate is materially different from OHIE and eBay.

The intervention is not merely information, ranking, incentive messaging, or realized participation. It directly changes the ex-ante condition under which a concrete class of transit transformations is economically accessible:

`Z → fare constraint → T_acc(Z)`

The transformation universe must nevertheless be frozen independently of observed trips. Realized transit-card taps cannot be used to define the transformation universe or accessibility set.

## 5. Why execution is still blocked

The decisive failure is reproducibility, not causal assignment.

The published experiment and registration establish randomization and longitudinal measurement, while the OpenICPSR deposit confirms that code and some data are available but some data are legally excluded. citeturn1search5turn1search8

Therefore an execution claiming to reconstruct unit-level `T_acc,0` and `T_acc,1` from the public package would risk silently substituting researcher-generated network/trip constructs for an independently reproducible state representation.

## 6. Decision

**D-OPS-30 = CLOSED — PROMISING METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED.**

Strengths:
- randomized individual intervention;
- direct accessibility change;
- stable transport transformation class;
- credible counterfactual;
- longitudinal trajectory;
- transition environment largely held fixed.

Blocker:
- incomplete public unit-level data needed for independently reproducible `T_acc` reconstruction.

No C09 claim upgrade.
No data acquisition.
No model fitting.
No execution authorization.
No AWS/Rust/SWIM action.

**Updated discovery criterion:** prioritize candidates where the intervention directly changes a formally frozen accessibility predicate **and** the complete unit-level inputs required to compute both treatment and control `T_acc` are public and reproducible.
