# TGCV — C09 MTO Operational Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** Moving to Opportunity (MTO)
**Parent:** `TGCV_C09_MTO_TR132_FINALIZATION_AUDIT_001.md`
**Execution authorization:** `NONE`

## 1. Objective

Verify whether the public-use MTO package is sufficient to operationalize the frozen C09 causal question without restricted residential-history data or post-treatment leakage.

## 2. Frozen causal specification

- Unit: randomized MTO household / sampled adult linked to baseline assignment.
- Contrast: LPV vs TRV.
- Accessibility rule: LPV low-poverty-tract restriction vs TRV unrestricted voucher geography.
- Bounded transformation profile: first voucher-supported residential transformation.
- Outcome horizon: long-term adult outcomes, 2008–2010.
- Estimand: ITT effect of randomized LPV assignment relative to randomized TRV assignment.

ICPSR confirms that the long-term MTO data cover the 2008–2010 evaluation, contain adult outcomes and baseline measures, and derive from the randomized MTO sample. citeturn0search0turn0search5

## 3. Public-use package feasibility

### P1 — Assignment variable

**PASS.**

Treatment-group assignment is part of the MTO experimental structure and is represented in the public-use research package/documentation. citeturn0search0turn0search6

### P2 — Baseline covariates

**PASS.**

Public-use documentation identifies baseline demographic and other measures used in the final-impact analyses. citeturn0search0turn0search5

### P3 — Long-term endpoint

**PASS.**

The public-use final-evaluation package contains adult long-term outcome variables used for the associated Science analysis; the package is specifically limited to variables needed to roughly reproduce the published findings. citeturn0search0turn0search6

### P4 — LPV/TRV rule mapping

**PASS — DOCUMENTARY.**

LPV is restricted to census tracts with 1990 poverty below 10%; TRV vouchers can be used anywhere. citeturn0search0

### P5 — Unit-level `T_acc,0/T_acc,1` reconstruction

**FAIL — PUBLIC-USE OPERATIONALIZATION.**

The public-use package is intentionally limited and the published long-term dataset is not a complete individual-level representation of every feasible residential transformation. ICPSR states that the distributed public-use datasets are limited to data needed to roughly replicate the associated article findings. citeturn0search6

The relevant individual-level restricted dataset exists separately. NBER explicitly distinguishes the public-use files from restricted individual-level data used to approximate replication of the Science results. citeturn0search3

Therefore the frozen TGCV `T_acc,0/T_acc,1` contrast cannot currently be reconstructed at the household level from the public-use package alone without importing variables or realized residential information not established as public.

### P6 — Independence from realized residential history

**PASS for rule definition / FAIL for household-level accessibility realization.**

The rule itself is ex ante and independent. However, mapping the rule to each household's complete candidate residential transformation profile requires geographic/residential information not established as available in the public-use package.

### P7 — Reproducible C09 execution

**FAIL.**

The public package is adequate for reproducing published outcome-level ITT analyses, but not for the stronger TGCV operationalization that requires a household-level bounded accessibility contrast.

## 4. Decision logic

TR-132 remains valid. The preflight failure is **not** a failure of the sufficiency principle; it is a failure of the currently available public-use operational package to instantiate the frozen TGCV accessibility variable at the required unit level.

This distinction is essential:

`TR-132 PASS` ≠ `public-use execution readiness`.

## 5. No workaround permitted

The following are explicitly rejected:

- inferring household-level `T_acc` from treatment assignment alone;
- substituting realized moves for ex-ante accessibility;
- using published aggregate tract statistics as a fabricated unit-level accessibility variable;
- redefining `T_acc` as “received voucher” merely because voucher receipt is public;
- importing restricted residential histories without a new governed access authorization;
- changing the endpoint or estimand post hoc to rescue execution.

## 6. Final preflight disposition

**PRE-FLIGHT = BLOCKED.**

MTO remains an admissible methodological C09 candidate under TR-132, but **is not executable under the current public-use evidence package**.

No data acquisition.
No restricted-data request.
No model fitting.
No causal result.
No claim-matrix upgrade.
No execution authorization.

## 7. Strategic implication

MTO has now passed the conceptual/sufficiency gates but failed the operational reproducibility gate. It should therefore be retained as a strong methodological reference rather than forced into execution.

**Next operation:** evaluate the next highest-ranked TR-132 candidate, **Chicago Voucher Lottery**, under the same controlled operational-preflight discipline.
