# TGCV — C09 King County Free Transit TR-132 Operational Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** King County free-transit randomized controlled trial
**Parent:** `TGCV_C09_RETROSPECTIVE_TR132_CANDIDATE_REVIEW_001.md`
**Execution authorization:** `NONE`

## 1. Candidate definition

The King County study randomized 1,797 low-income participants. Treatment participants received an ORCA LIFT card with up to six months of fully subsidized transit; controls received the standard reduced-fare card preloaded with $10. The trial was conducted through King County benefit offices. citeturn0search0turn0search10

A public OpenICPSR replication package exists and identifies the project as an RCT using administrative records, aggregate data, census data and experimental data. citeturn0search6turn0search12

## 2. Proposed bounded C09 representation

`U* = transit-use transformations available to an enrolled participant during the frozen subsidy window under the treatment and control fare regimes.`

The causal intervention is the randomized fare subsidy, not realized transit use.

## 3. Operational gates

### P1 — Randomized intervention

**PASS.**

Treatment/control assignment is explicitly randomized, with free-transit treatment versus reduced-fare control. citeturn0search0turn0search10

### P2 — Decision-time unit and baseline state

**PASS — DESIGN LEVEL.**

Participants enrolled through DSHS offices and completed an intake questionnaire describing baseline transit habits. citeturn0search10

### P3 — Accessibility intervention

**CONDITIONAL PASS.**

The fare subsidy directly changes the economic admissibility of transit-use transformations: treatment makes eligible transit rides free during the subsidy period, whereas control retains a reduced fare. This is a substantially cleaner intervention-to-accessibility mapping than the housing voucher candidates. citeturn0search0turn0search1

However, TGCV requires a bounded transformation-space representation, not merely a price/treatment indicator. The operational definition must specify the frozen transit universe, fare rules, temporal horizon and admissibility predicate.

### P4 — Unit-level `T_acc,0/T_acc,1`

**FAIL — PUBLIC REPRODUCIBILITY.**

The experimental intervention is identifiable, but the public replication package does not establish a unit-level representation of each participant's accessible transit transformation space under treatment and control. The underlying study uses administrative transit-card taps and additional administrative/proprietary sources. citeturn0search1turn0search24turn0search12

The public package therefore supports replication of reported analyses but does not establish that `T_acc,0` and `T_acc,1` can be reconstructed for each randomized unit within the declared `U*` without importing restricted/proprietary source data.

### P5 — Independent trajectory endpoint

**PASS — DESIGN LEVEL / DATA SOURCE RESTRICTION REMAINS.**

The study measures travel behavior and downstream outcomes including employment, benefits, health, residential mobility, criminal justice and well-being. The published work explicitly describes linkage to rich administrative and proprietary data for downstream outcomes. citeturn0search24turn0search23

The endpoint therefore exists scientifically, but its unrestricted unit-level reproducibility is not established by the public package.

### P6 — Public reproducibility

**FAIL.**

The existence of an OpenICPSR replication package is insufficient by itself: the deposited project metadata explicitly classifies the underlying project as including administrative-record and experimental data, while the published research describes administrative transit-card records and proprietary residential/consumer data. citeturn0search6turn0search12turn0search24

### P7 — TR-132 omitted-path sufficiency

**NOT ADMITTED.**

Because unit-level `T_acc,0/T_acc,1` cannot be reconstructed from the admissible public package, the sufficiency argument cannot be completed operationally. A fare-treatment indicator cannot be substituted for the transformation-space representation.

## 4. Decision

**KING COUNTY FREE TRANSIT = PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED.**

The candidate is methodologically strong and, conceptually, the randomized fare intervention is unusually close to an accessibility intervention. Nevertheless, the public reproducibility gate fails at the unit-level transformation-space representation.

No inference from treatment assignment to `T_acc`.
No substitution of realized card use for accessibility.
No use of proprietary residential/consumer data.
No restricted-data request.
No causal execution.
No matrix upgrade.
No Core change.
No execution authorization.

## 5. Candidate disposition

Retain King County as a **strong methodological reference** for the causal design of accessibility interventions. Do not reopen the candidate unless a legitimately accessible unit-level data package establishes the bounded `T_acc,0/T_acc,1` representation required by TR-132.

**Next operation:** evaluate the next-ranked candidate, **Naturalization Fee Voucher**, under the same controlled TR-132 operational-preflight gate.
