# TGCV — C09 MTO TR-132 Sufficiency Audit 001

**Status:** `COMPLETED — TR-132 CONDITIONAL PASS / C09 EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** Moving to Opportunity (MTO)
**Parent:** `TGCV_C09_TR132_SUFFICIENCY_GATE_001.md`
**Historical audit:** `D-OPS-27_MTO_RANDOMIZED_HOUSING_ACCESSIBILITY_C09_INTERVENTION_AUDIT_v0.1.md`
**Execution authorization:** `NONE`

## 1. Objective

Determine whether MTO can satisfy TR-132 using a bounded residential transformation profile rather than complete system-wide reconstruction of `T_acc`.

## 2. Frozen candidate profile

Proposed bounded transformation universe:

`U* = {voucher-supported residential move from baseline dwelling to a dwelling in a declared census-tract class during the first MTO move window}`

The profile is deliberately narrower than the complete housing transformation space.

Proposed accessibility predicates:

- `P_tau,LPV`: candidate residential move is admissible under the LPV rule, including the low-poverty census-tract restriction.
- `P_tau,TRV`: candidate residential move is admissible under the unrestricted traditional Section 8 voucher rule.

The MTO public documentation establishes random assignment to LPV, TRV and control; LPV vouchers were restricted to census tracts with 1990 poverty below 10%, while TRV vouchers were geographically unrestricted. citeturn0search0turn0search5

## 3. TR-132 assessment

### T1 — Frozen bounded U*

**PASS — DESIGN LEVEL.**

A bounded first-move residential profile is operationally definable without enumerating every possible housing transformation. The boundary can be frozen before outcome inspection.

### T2 — Ex-ante P_tau

**PASS — DESIGN LEVEL.**

The LPV geographic restriction is an ex-ante programme rule, not a predicate inferred from realized moves. The public documentation explicitly describes the restriction. citeturn0search0

### T3 — T_acc,0 versus T_acc,1 identifiable

**CONDITIONAL PASS.**

Within `U*`, LPV and TRV imply different admissibility predicates for residential transformations. This is a genuine accessibility contrast rather than a ranking, information or incentive-only contrast.

The remaining condition is unit-level reconstruction of the candidate transformation profile from admissible pre-treatment/public variables without importing realized addresses.

### T4 — Independent intervention

**PASS.**

MTO used random assignment among eligible volunteer families to LPV, TRV and control. citeturn0search0turn0search8

### T5 — Counterfactual

**PASS.**

Random assignment provides a credible treatment/control contrast. For the specific accessibility mechanism, TRV is a particularly useful comparator because it provides voucher access without the LPV geographic restriction. citeturn0search0

### T6 — Independent trajectory endpoint

**CONDITIONAL PASS.**

Longitudinal MTO outcomes and neighborhood measures are publicly documented, and public-use long-term files contain outcomes and baseline measures. Families were followed from 1994–1998 through 2008–2010. citeturn0search0turn0search1

However, detailed quarterly residential histories were constructed from HUD administrative data and MTO surveys; the published residential-history research relies on that richer longitudinal linkage. citeturn0search5

Therefore the causal trajectory endpoint must be frozen to an outcome/trajectory observable actually available in the admissible public-use package, unless independent access to the richer history is established.

### T7 — Omitted-transformation sufficiency

**OPEN — CRITICAL.**

TR-132 does not require complete housing-space enumeration, but it requires a defensible argument that transformations omitted from `U*` cannot alter the declared causal conclusion.

This is not yet demonstrated. In particular, unrestricted moves after the first relocation, alternative housing-assistance pathways, and subsequent residential transformations could matter depending on the chosen trajectory endpoint.

The bounded profile therefore needs a sharper causal estimand and horizon before execution.

### T8 — No post-treatment leakage

**PASS — DESIGNABLE.**

`P_tau` can be frozen from assignment, baseline eligibility and the published LPV/TRV programme rules. Realized addresses, later neighborhood measures and downstream outcomes must remain excluded from accessibility classification.

### T9 — Public reproducibility

**CONDITIONAL PASS.**

ICPSR provides public-use MTO files accessible without institutional affiliation, but NBER documents that individual-level restricted-access datasets also exist. citeturn0search0turn0search1

Consequently, public reproducibility is sufficient only for a bounded outcome/trajectory definition that does not require the restricted residential-history variables.

## 4. Critical finding

The previous MTO rejection cannot be maintained merely because complete unit-level `T_acc` is unavailable.

Under TR-132, MTO has a **credible bounded accessibility mechanism**:

`random assignment → LPV/TRV rule → bounded residential transformation accessibility → subsequent independently measured outcome/trajectory`

But TR-132 is **not yet fully passed**, because omitted-path sufficiency and the exact publicly reproducible trajectory endpoint remain unresolved.

## 5. Required finalization before any C09 preflight

A second, narrower MTO design audit must freeze:

1. the exact residential transformation profile `U*`;
2. the exact decision-time unit and baseline state;
3. the exact LPV/TRV accessibility predicates;
4. the trajectory endpoint `Y` available in public-use data;
5. the observation horizon;
6. a proof/argument that omitted residential transformations cannot change the declared causal estimand;
7. the treatment contrast (preferably LPV vs TRV for isolating the locational accessibility restriction);
8. the information firewall excluding realized residential histories from `P_tau`.

## 6. Decision

**TR-132 = CONDITIONAL PASS for MTO.**

MTO is promoted from `methodological reference` to **active C09 candidate under controlled TR-132 finalization**.

It is **not** yet admitted for C09 execution.

No claim-matrix upgrade.
No causal result.
No data acquisition.
No model fitting.
No AWS/Rust/SWIM execution.

**Next operation:** finalize the bounded MTO `U*`/trajectory pair and perform the TR-132 omitted-path sufficiency check before any C09 operational preflight.
