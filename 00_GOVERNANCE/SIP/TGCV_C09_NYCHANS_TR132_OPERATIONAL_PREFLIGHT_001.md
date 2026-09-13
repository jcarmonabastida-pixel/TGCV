# TGCV — C09 NYCHANS TR-132 Operational Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** New York City Housing and Neighborhood Study (NYCHANS)
**Parent:** `TGCV_C09_RETROSPECTIVE_TR132_CANDIDATE_REVIEW_001.md`
**Execution authorization:** `NONE`

## 1. Candidate definition

NYCHANS is a randomized housing study in which approximately 2,600 near-poor households were assigned either an offer of an affordable unit at one of thirteen developments or to remain in private-market housing without assistance. Follow-up interviews occurred four to seven years after random assignment. citeturn2search0turn0search13

## 2. Proposed bounded C09 representation

`U* = assignment-supported residential transformation from the applicant's pre-assignment housing state to the newly constructed affordable unit offered through the randomized housing lottery.`

The causal intervention is the randomized offer, not actual take-up or subsequent residential moves.

## 3. Operational gates

### P1 — Randomized assignment

**PASS.**

The study is explicitly an RCT using the city's housing lottery, with treatment defined by being offered an affordable housing unit and control by eligibility without an offer. citeturn0search13turn2search0

### P2 — Decision-time unit and assignment data

**PASS — DESIGN / SOURCE DOCUMENTED.**

The study documentation reports that original housing application and screening files contain household composition, income, voucher status, originating address, offer/acceptance information, and group assignment; assignment data were available for the full sample. citeturn0search12

### P3 — Intervention accessibility rule

**CONDITIONAL PASS.**

Unlike MTO/Chicago, the treatment is a concrete offer of a unit at one of thirteen identified developments. The offered destination is therefore much closer to a directly enumerated bounded transformation than a general voucher geography. However, the underlying application/screening records are researcher/agency data rather than an established public-use household microdata release. citeturn0search12

### P4 — Unit-level `T_acc,0/T_acc,1`

**CONDITIONAL / CRITICAL.**

The documentation establishes originating address, offered unit, acceptance, and baseline/follow-up residential addresses as study variables. It also states that census data were merged to residential addresses at baseline and follow-up. citeturn0search12

But this establishes existence in the NYCHANS research data infrastructure, not public reproducibility of the household-level accessibility representation.

### P5 — Independent trajectory endpoint

**PASS — DESIGN LEVEL.**

Follow-up outcomes include housing and neighborhood quality, financial stability, neighborhood safety, social context, physical and mental health, and health behaviors, measured four to seven years after intervention. citeturn2search0

For C09, one endpoint must be frozen before execution and must be independently reconstructible from an admissible data package.

### P6 — Public reproducibility

**FAIL / NOT ESTABLISHED.**

The NYCHANS documentation explicitly describes application/screening files, administrative records, baseline survey data, follow-up interviews, and census merges. It does not identify a public-use NYCHANS household-level dataset containing the randomized assignment, offered destination, baseline state, and selected follow-up endpoint needed for a TGCV reconstruction. citeturn0search12

The existence of public NYCHVS microdata does not solve this problem: NYCHVS is a separate representative housing survey, not the NYCHANS randomized sample. citeturn1search0turn2search2

## 4. TR-132 assessment

Conceptually, NYCHANS is highly compatible with TR-132 because the randomized offer is tied to a concrete affordable-housing transformation and the destination developments are bounded and identifiable.

Operationally, however, the candidate fails the current public-use reproducibility gate because the household-level assignment/application/follow-up linkage required to reconstruct the causal unit is not established as publicly downloadable.

Therefore:

`TR-132 conceptual sufficiency = promising`

but

`C09 operational reproducibility = NOT ESTABLISHED`

## 5. No-go substitutions

Rejected:

- treating public Housing Connect lottery statistics as the randomized NYCHANS sample;
- using aggregate development-level lottery data as household-level `T_acc`;
- substituting NYCHVS microdata for NYCHANS participants;
- replacing randomized offer with actual acceptance/move;
- reconstructing household-level treatment from published effect estimates;
- requesting or using restricted administrative data without a new governed access pathway.

## 6. Decision

**NYCHANS = PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED.**

The candidate remains a **strong methodological reference** and is conceptually stronger than the voucher-geography candidates because the intervention is a concrete housing-unit offer. Nevertheless, no causal execution is admitted without an accessible reproducibility package containing the necessary unit-level randomized assignment, bounded accessibility representation, and independently defined outcome.

No data acquisition.
No restricted-data request.
No model fitting.
No causal result.
No matrix upgrade.
No Core change.
No execution authorization.

**Next operation:** evaluate the next-ranked candidate, **King County Free Transit**, under the same controlled TR-132 operational-preflight gate.
