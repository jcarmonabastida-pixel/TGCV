# D-OPS-27 — MTO Randomized Housing Accessibility C09 Intervention Audit v0.1

**Status:** `CLOSED — STRONG METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Execution:** `NOT AUTHORIZED`
**Candidate:** Moving to Opportunity (MTO), HUD randomized housing-mobility experiment

## 1. Purpose

Audit whether MTO satisfies the strengthened C09 requirement: randomized unit-level access intervention, independently defined transformation accessibility, credible counterfactual trajectory, longitudinal state reconstruction and reproducible evidence.

## 2. Candidate strength

MTO randomized eligible families into three conditions: low-poverty voucher (LPV), traditional voucher (TRV), and control. The LPV voucher could be used only in census tracts below the specified poverty threshold, while TRV vouchers were geographically unrestricted. Families were followed from 1994–1998 baseline through 2008–2010 long-term evaluation. ICPSR provides public-use files, while more detailed individual-level data are restricted. citeturn2search0turn2search1turn2search2

This is materially stronger for C09 than ranking/visibility interventions: the randomized treatment changes the set of housing moves that are permitted under the intervention rule, not merely their visibility or incentives.

## 3. Gate assessment

| Gate | Result | Finding |
|---|---|---|
| Stable unit/state | PASS — bounded | Randomized household/family unit and baseline condition are documented. |
| Formal rule layer | PASS — bounded | LPV/TRV/control conditions specify distinct voucher-use rules. |
| Independent intervention | PASS | Assignment to treatment condition was randomized. |
| Bounded `U_tau` | CONDITIONAL PASS | Candidate transformations can be bounded as eligible residential moves under a frozen baseline and voucher rule. |
| Pre-execution `P_tau` | PASS — bounded | Eligibility and voucher-use constraints are defined before subsequent residence/outcomes. |
| `Z → ΔT_acc` | **PASS — bounded design candidate** | LPV assignment changes the permitted geographic class of voucher-supported moves relative to TRV/control. This is a direct accessibility change, subject to freezing the transformation universe and eligibility predicate ex ante. |
| Counterfactual | PASS | Randomized LPV/TRV/control assignments provide credible counterfactual conditions. |
| Longitudinal trajectory | PASS — bounded | MTO follows families for 10–15 years; residential histories and downstream outcomes have been reconstructed in published analyses. citeturn2search4turn2search6 |
| Transition environment | CONDITIONAL PASS | The treatment rule is frozen at assignment; subsequent residential choice remains endogenous and must be represented as trajectory rather than treatment definition. |
| Public reproducibility | **FAIL for full C09 execution** | Public-use files exist, but detailed individual-level/restricted data and the granular residential-history information needed to reconstruct `T_acc` are not fully public. ICPSR documents restricted-access individual-level data. citeturn2search2 |

## 4. Critical mapping

A defensible bounded TGCV mapping is:

`S_0,C_0 → U_tau → P_tau(Z) → T_acc(Z) → S_1,C_1 → trajectory`

For the LPV treatment, the intervention can be represented as changing an ex-ante admissibility predicate over residential transformations by imposing the low-poverty-tract constraint. TRV provides a useful comparator because it preserves voucher access without that geographic restriction.

The critical firewall is to define `U_tau` and `P_tau` **before** observing realized moves, neighborhood trajectories or outcomes. The realized residential address must not be used to define the accessibility space retrospectively.

## 5. Reproducibility blocker

The candidate does not currently satisfy the execution-level public-reproducibility requirement. ICPSR's public-use MTO files are available, but the public files are aggregated/pseudo-individual products for the long-term adult analyses; the detailed individual-level dataset is restricted. citeturn2search0turn2search1

Consequently, a full C09 reconstruction of unit-level `U_tau`, `P_tau`, `T_acc,0`, `T_acc,1` and subsequent trajectory cannot presently be guaranteed from the public package alone.

## 6. Decision

**D-OPS-27 = CLOSED — STRONG METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED.**

MTO is the strongest candidate identified in the present discovery sequence because it simultaneously provides:

1. randomized unit-level assignment;
2. an intervention that plausibly changes transformation accessibility itself;
3. an explicit formal access constraint;
4. a credible randomized counterfactual;
5. long-horizon trajectory evidence; and
6. public documentation and partial public-use data.

The remaining blocker is **data granularity/provenance for reconstructing the TGCV accessibility space**, not causal assignment.

No C09 claim upgrade follows.

## 7. Discovery implication

MTO establishes the next useful search criterion more sharply:

`randomized access rule that directly changes admissible transformations + public unit-level longitudinal state sufficient to reconstruct T_acc before outcome observation`.

This criterion should govern the next discovery pass. Domains that satisfy randomization but only alter information, incentives, ranking or take-up remain excluded. Domains with the correct causal mechanism but restricted state needed to reconstruct `T_acc` remain methodological references until public or independently reproducible state evidence is demonstrated.

No data acquisition, model fitting, execution, AWS mutation, Rust rerun or SWIM rerun is authorized.
