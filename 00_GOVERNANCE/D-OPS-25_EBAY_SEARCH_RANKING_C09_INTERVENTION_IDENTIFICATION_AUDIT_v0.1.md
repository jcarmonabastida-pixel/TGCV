# D-OPS-25 — eBay Search-Ranking C09 Intervention Identification Audit v0.1

**Status:** `CLOSED — CANDIDATE NOT ADMITTED FOR C09 CAUSAL EXECUTION`
**Date:** 2026-09-13
**Execution:** `NOT AUTHORIZED`
**Candidate:** eBay randomized search-ranking experiment (Nosko & Tadelis)

## 1. Purpose

Audit whether the eBay field experiment can satisfy the strengthened C09 requirement that an independently assigned intervention changes `T_acc` rather than merely changing visibility, ranking, information or incentives.

## 2. Evidence reviewed

The 2026 published version reports a randomized field experiment in which a randomly selected group of eBay buyers received search results giving greater prominence to higher-EPP sellers, while controls saw the standard ranking. The experiment ran from 14 December 2011 through 2 January 2012 and covered 10% of U.S. site traffic. The study reports subsequent purchasing effects. citeturn0search0turn1search1

The underlying longitudinal transaction data comprise 935,326 buyers and 15,384,439 transaction observations, but the publisher states explicitly that the data cannot currently be accessed because they resided at eBay and access became prohibited after the authors left. citeturn1search1turn1search23

## 3. Gate assessment

| Gate | Result | Finding |
|---|---|---|
| Stable unit | PASS | Buyer/browser GUID and linked user identity are documented. |
| Randomized intervention | PASS | Treatment/control ranking assignment was randomized at browser level. |
| Longitudinal outcome | PASS — bounded | Subsequent purchasing is observed in the original internal data. |
| Public reproducible state archive | FAIL | The underlying transaction data are not currently accessible. |
| Bounded `U_tau` | OPEN | Candidate purchase/listing actions can be bounded conceptually, but the published study does not provide a frozen exhaustive transformation universe for C09. |
| Ex-ante `P_tau` | FAIL for current C09 mapping | Ranking prominence is not a protocol-level admissibility predicate defining whether a transformation is permitted. |
| `Z → ΔT_acc` | **FAIL — CRITICAL** | Treatment changes ranking/order/prominence of listings. It does not demonstrably change the underlying set of purchasable/admissible transformations. |
| No direct trajectory encoding | PASS | Ranking assignment does not prescribe the subsequent purchase path. |
| Counterfactual | PASS | Randomized treatment/control supplies a strong experimental counterfactual. |
| Information firewall | PASS — designable | Assignment precedes subsequent purchases. |

## 4. Critical distinction

The experiment establishes a causal change in **exposure/order of information** and reports downstream purchase effects. It does not establish that the set/structure of transformations accessible to the buyer changed in the TGCV sense.

A representation such as:

`Z → ranking/visibility → consideration → purchase`

is supported by the experiment.

The required TGCV relation is stronger:

`Z → ΔT_acc → subsequent trajectory`

To equate ranking prominence with `ΔT_acc` would require redefining `T_acc` as a visibility-weighted consideration space after seeing the intervention. That would be an ad hoc operationalization and would violate the current C09 firewall against using the outcome/research result to define accessibility.

## 5. Reproducibility blocker

Even if the accessibility interpretation were defensible, the underlying experiment data are not publicly accessible. The 2026 published paper explicitly states that access is prohibited because the data remained at eBay. citeturn1search1

Therefore an independent reconstruction satisfying the current TGCV provenance requirement cannot presently be performed from public data.

## 6. Decision

**D-OPS-25 = CLOSED — NO C09 EXECUTION CANDIDATE ADMITTED.**

The eBay experiment is retained as a useful methodological reference for randomized manipulation of search exposure and downstream behavior, but it is not TGCV C09 evidence.

No C09 claim upgrade follows.

## 7. Discovery implication

The strengthened search criterion is now:

`randomized/quasi-exogenous intervention + independently defined accessibility predicate + demonstrable Z→ΔT_acc + reconstructible longitudinal state/trajectory + public or independently reproducible evidence`

Candidates where treatment changes only ranking, visibility, incentives or information remain methodological references unless an independent transformation-accessibility change can be demonstrated without redefining `T_acc` post hoc.

No data acquisition, model fitting, execution, AWS mutation, Rust rerun or SWIM rerun is authorized.
