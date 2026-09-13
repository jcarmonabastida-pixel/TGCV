# D-OPS-29 — C09 TR-132 Capability/Permission Discovery 001

**Status:** `CLOSED — DISCOVERY RULE REFINED / MTO ADMITTED TO CONTROLLED PREFLIGHT`
**Date:** 2026-09-13
**Purpose:** use TR-132 compliance as a sufficient discovery filter for bounded C09 cases, rather than requiring a globally complete transformation universe at discovery time.

## 1. Correction to D-OPS-28 discovery rule

D-OPS-28 correctly rejected channel/interface interventions, but its final discovery criterion was unnecessarily strict if applied before TR-132.

The relevant sequence is:

`candidate → TR-132 state-sufficiency test → bounded U* / P_tau → causal accessibility test`

not:

`candidate → globally complete U_tau required before candidate admission`.

TR-132 permits a bounded operational transformation profile `U*` when the omitted transformations are proven unable to change the causal conclusion within the declared scope. Therefore, **compliance with TR-132 can be sufficient to admit a real-world case to C09 preflight**, even when the complete domain-wide transformation universe is not enumerable.

This does not weaken C09. It moves the completeness burden to the explicit TR-132 sufficiency test.

## 2. Revised discovery criterion

A candidate is eligible for controlled C09 preflight when it has:

1. stable decision-time unit/state;
2. exogenous or randomized intervention;
3. an intervention that changes a permission, eligibility, capability or resource feasibility condition;
4. a candidate bounded transformation profile `U*`;
5. an ex-ante accessibility predicate `P_tau`;
6. a subsequent longitudinal outcome independent of accessibility adjudication;
7. **TR-132 sufficiency:** omitted transformations cannot alter the causal estimand/conclusion within the declared scope;
8. reproducible provenance sufficient to test the above.

Global enumeration of all transformations is **not** an admission prerequisite when TR-132 supplies the required sufficiency proof.

## 3. Candidate D29-A — Moving to Opportunity (MTO)

The strongest candidate identified under the corrected rule is the randomized **Moving to Opportunity** housing-mobility experiment.

MTO randomly assigned eligible families to housing-voucher conditions or control. The experimental group received a voucher restricted to low-poverty census tracts, while the Section 8 group received an unrestricted voucher; controls received no new voucher offer. The programme therefore changes a concrete feasibility condition for a distinct transformation: relocating from the original public-housing state into a qualifying private-market residential state. Random assignment was used across five U.S. cities and long-term follow-up data exist. citeturn1search0turn1search3turn1search7

### Candidate TGCV mapping

`Z = randomized voucher offer`

`U* = {remain in origin housing state, relocate using qualifying voucher}`

`T_acc,0 = {remain in origin housing state}`

`T_acc,1 ⊇ {remain in origin housing state, relocate through the offered voucher}`

The crucial distinction from D27-A is that the treatment does not merely provide another interface for the same action. It changes the **resource/eligibility feasibility boundary for relocation**: without the voucher offer, the particular subsidized relocation transformation is not available under the experimental programme; with the offer, it becomes executable subject to the programme's eligibility and housing-quality rules. HUD and subsequent analyses explicitly describe the programme as randomly assigning housing assistance and expanding access to lower-poverty neighbourhoods. citeturn1search5turn1search7

## 4. TR-132 relevance

MTO does not require us to claim that `U*` is the universe of every possible residential move, housing change, neighbourhood interaction or household decision.

The controlled preflight can instead test whether the bounded transformation profile is **state-sufficient for the C09 estimand**:

`Y = subsequent trajectory over the declared post-assignment horizon`

and whether omitted residential transformations cannot change the treatment/control contrast for that estimand within the declared scope.

This is precisely the type of bounded sufficiency question for which TR-132 is useful.

A TR-132 PASS would therefore be sufficient to continue even if a larger transformation universe exists.

A TR-132 failure would close MTO without execution.

## 5. Evidence already available

MTO provides unusually strong causal infrastructure:

- randomized assignment;
- explicit voucher eligibility and redemption rules;
- multiple treatment arms and control;
- a concrete resource enabling a relocation transformation;
- administrative/residential-history follow-up;
- long-term trajectory/outcome records over 10–15 years. citeturn1search2turn1search3turn1search11

The experiment enrolled 4,610 eligible families across Baltimore, Boston, Chicago, Los Angeles and New York, with baseline, interim and final follow-up waves. citeturn1search3turn1search5

## 6. Remaining gates

D29-A is **not yet C09 evidence**. The following must be tested in the next controlled preflight:

- TR-132 state sufficiency for the proposed `U*`;
- exact decision-time state/context `S0,C0`;
- ex-ante voucher accessibility predicate `P_tau`;
- exact treatment contrast `Z`;
- distinction between voucher eligibility/access and actual voucher take-up;
- independent trajectory definition `Y`;
- direct-path exclusion;
- attrition and missingness;
- independent reconstruction/provenance;
- whether the relocation transformation itself is sufficiently distinct and causally downstream of the randomized access condition.

## 7. Secondary candidates retained

### D29-B — randomized public-school choice / centralized assignment

School-choice lottery systems are potentially strong because lottery assignment directly changes access to a school/programme while leaving later educational trajectories open. Chicago Public Schools, for example, uses randomized computerized lotteries for eligible choice programmes and documents eligibility, capacity and assignment rules. citeturn0search1turn0search3

This class remains secondary until a specific longitudinal randomized study is selected with sufficient post-assignment trajectory data.

### D29-C — randomized naturalization-access voucher

A recent New York randomized lottery offered naturalization fee vouchers to permanent residents. Voucher assignment increased naturalization substantially and was followed using administrative and financial records for up to five years. This is conceptually relevant because treatment changes access to the naturalization transformation, although the downstream trajectory and transformation-state representation require a careful TR-132 preflight. citeturn1search12

Disposition: secondary candidate; do not preflight before D29-A unless MTO fails.

## 8. Decision

`C09 = H — NO CAUSAL IDENTIFICATION`

`D29-A MTO = LEAD CANDIDATE — ADMIT TO CONTROLLED TR-132/C09 PREFLIGHT`

`D29-B SCHOOL CHOICE = SECONDARY`

`D29-C NATURALIZATION = SECONDARY`

`EXECUTION AUTHORIZATION = NONE`

`NEW DATASET ACQUISITION = NONE`

`CLAIM UPGRADE = NONE`

## 9. Next operation

**D-OPS-30 — MTO TR-132 State-Sufficiency / C09 Admissibility Preflight.**

The next operation must test whether a bounded relocation transformation profile is sufficient under TR-132 and whether the randomized voucher offer produces the required causal accessibility contrast without conditioning on take-up or post-treatment residential outcomes.
