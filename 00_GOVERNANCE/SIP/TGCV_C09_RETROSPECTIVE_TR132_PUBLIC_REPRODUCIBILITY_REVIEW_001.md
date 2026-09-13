# TGCV — C09 Retrospective TR-132 Public-Reproducibility Review 001

**Status:** `COMPLETED — NO CANDIDATE CURRENTLY ADMITTED FOR C09 EXECUTION`
**Date:** 2026-09-13
**Scope:** Remaining retrospective C09 candidates after controlled operational preflights
**Execution authorization:** `NONE`

## 1. Purpose

Determine whether any remaining retrospective candidate can satisfy the C09 operational gate using an admissible, reproducible unit-level representation of bounded `T_acc,0/T_acc,1` without dependence on restricted or proprietary records.

This is a screening/disposition operation only. It does not reopen closed candidate audits and does not authorize execution.

## 2. Reviewed candidates

The controlled sequence has now screened:

- MTO — TR-132 PASS, operational preflight blocked by public-use inability to reconstruct unit-level `T_acc,0/T_acc,1`.
- Chicago Voucher Lottery — operationally blocked by provenance/restricted administrative records.
- NYCHANS — operationally blocked by absence of an established public-use household-level randomized package.
- King County Free Transit — operationally blocked by unit-level accessibility-space reconstruction.
- Naturalization Fee Voucher — operationally blocked by unit-level randomized longitudinal package availability.
- OHIE — public-use data exist, but the required unit-level bounded accessibility representation is not established.
- Charlotte-Mecklenburg School Choice — randomized admission mechanism is strong, but the required unit-level administrative accessibility representation is not publicly reproducible.

## 3. Public-reproducibility conclusion

**No candidate currently satisfies all operational conditions simultaneously.**

The recurring blocker is not randomization or causal identification. The blocker is the TGCV-specific requirement to reconstruct, for the randomized unit, a bounded transformation universe `U*` and distinguish `T_acc,0` from `T_acc,1` independently of realized outcomes, while retaining an independently defined trajectory endpoint.

Public replication code, published treatment effects, lottery assignment, voucher receipt, realized movement/use, or aggregate accessibility measures cannot substitute for that representation.

## 4. Important methodological result

The review therefore identifies a useful separation between two properties:

1. **Causal-design strength:** several candidates have strong randomized interventions.
2. **TGCV operational identifiability/reproducibility:** none of the screened candidates currently supplies the complete admissible unit-level accessibility representation needed for C09 execution.

This is a legitimate screening result and does not constitute evidence against C09 itself. It establishes that the present retrospective candidate pool does not yet provide an execution-ready public package.

## 5. Candidate status after review

| Candidate | Causal design | TR-132 | Public unit-level `T_acc` | C09 execution |
|---|---|---|---|---|
| MTO | Strong | PASS | Insufficient | NOT ADMITTED |
| Chicago Voucher | Strong | Screening blocked | Insufficient | NOT ADMITTED |
| NYCHANS | Strong | Promising | Insufficient | NOT ADMITTED |
| King County | Strong | Promising | Insufficient | NOT ADMITTED |
| Naturalization Voucher | Strong | Promising | Insufficient | NOT ADMITTED |
| OHIE | Strong | Conditional | Insufficient | NOT ADMITTED |
| Charlotte-Mecklenburg | Strong | Conditional | Insufficient | NOT ADMITTED |

## 6. Decision

**C09 RETROSPECTIVE SCREENING = CLOSED FOR CURRENT PUBLIC-PACKAGE EXECUTION.**

No candidate is promoted to causal execution.

No matrix upgrade.
No Core change.
No causal claim.
No restricted-data acquisition request.
No execution authorization.

The screening should not continue by repeatedly testing equivalent candidates solely to overcome the same public-reproducibility blocker.

## 7. Strategic next gate

The next scientific operation should therefore change the search criterion rather than repeat the same retrospective lottery pattern: identify a domain in which the accessibility intervention and bounded `T_acc,0/T_acc,1` representation are directly observable or reconstructible from an admissible public operational dataset, while preserving randomized or otherwise credible causal identification.

Candidate discovery remains subordinate to the Scientific Asset Registry and the C09 causal-design/TR-132 gates.
