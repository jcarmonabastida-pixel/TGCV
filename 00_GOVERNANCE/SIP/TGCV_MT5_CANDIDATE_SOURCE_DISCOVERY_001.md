# TGCV MT5-1 — Candidate Source Discovery 001

**Status:** MT5-1 COMPLETE — CANDIDATE IDENTIFIED FOR SOURCE-FREEZE REVIEW
**Date:** 2026-09-16
**Protocol:** `00_GOVERNANCE/SIP/TGCV_MT5_DOWNSTREAM_VALUE_ENDPOINT_PROTOCOL_001.md`

## 1. Discovery objective

Identify a genuinely new empirical source capable, in principle, of supporting the downstream chain:

`S_t → U_tau → P_tau → T_acc,t → ΔT_acc → subsequent transformation/trajectory → independently measured downstream value/outcome`

with temporal ordering and without using the downstream endpoint to define accessibility.

## 2. Selected candidate

**Gonzalez-Navarro & Quintana-Domeque — Paving Streets for the Poor: Experimental Analysis of Infrastructure Effects**

Published in *The Review of Economics and Statistics* (2016), 98(2), 254–267, DOI `10.1162/REST_a_00553`.

Study setting: Acayucan, Mexico.

Study period: 2006–2009.

AEA RCT registration: `AEARCTR-0001300`.

Replication deposit: Harvard Dataverse DOI `10.7910/DVN/6TC8RO`.

The author replication page reports a readme, replication files and a 552 KB compressed data/replication package. J-PAL reports 1,231 households and a randomized street-paving intervention. The study used random allocation of first-time asphalting of residential non-arterial streets among eligible candidate streets.

## 3. Why this candidate is informative for MT5

The candidate has an unusually direct potential downstream value endpoint: professional appraisals of residential property value were collected before and after the intervention. The published study reports that street paving increased property values and that the increase in property wealth was followed by changes in vehicle ownership, durable goods and home improvements.

The source therefore appears capable of providing all three critical layers that remained unresolved in MT4:

1. a pre-intervention structural state containing road/street configuration and candidate eligibility conditions;
2. a concrete structural transformation — first-time street paving — with randomized assignment among eligible candidate streets;
3. an independently measured downstream property-value endpoint collected after the intervention.

The candidate is analytically attractive because property valuation is not required to define the candidate transformation or its admissibility. This creates a prospective opportunity to freeze `P_tau` before inspecting the downstream value result.

## 4. Preliminary TGCV translation hypothesis — NOT YET FROZEN

This is a candidate translation only and must not be treated as the MT5 operational definition until MT5-2 source freeze and MT5-3/4 audits.

Potential bounded transformation universe:

`U_tau* = {Pave(street_segment)}`

Potential baseline state components:

- street paved/unpaved status;
- connectivity to the existing pavement grid;
- street/project eligibility conditions;
- relevant physical and municipal constraints documented in the frozen source.

Potential admissibility structure:

`P_tau(S,C,L)=1` only for transformations satisfying the source's pre-intervention candidate-street and physical/municipal feasibility conditions.

Potential downstream value endpoint:

`V_{t+k} = professional residential property appraisal / market-value measure` at follow-up, constructed only from frozen post-intervention observations and never fed back into `P_tau`.

This translation remains explicitly provisional.

## 5. Critical risks to audit in MT5-2/MT5-3

1. **Eligibility leakage:** candidate-street selection rules may include information determined after baseline.
2. **Treatment-realization substitution:** randomized assignment and actual paving must remain distinct from accessibility.
3. **Single-transformation triviality:** `U_tau*` may be too narrow to test a meaningful transformation space; this must be assessed rather than assumed away.
4. **Accessibility versus assignment:** assignment to paving is not itself an admissibility predicate.
5. **Property-value timing:** appraisal dates must be verified as downstream of the accessibility-changing intervention.
6. **Appraisal construction:** the exact raw variables and historical construction rule must be frozen before outcome interpretation.
7. **Interference/network effects:** neighboring street paving may affect accessibility/value of control properties; this must be audited rather than assumed absent.
8. **Post-treatment information:** no follow-up property, consumption or take-up variable may enter the baseline accessibility definition.

## 6. Candidate disposition

**MT5-1:** `PASS — CANDIDATE IDENTIFIED`

**MT5-2 authorization:** source-freeze/provenance audit is authorized for this candidate.

No causal or value conclusion is drawn at MT5-1. No claim-level status changes. No Core/RMA modification follows from candidate discovery.

## 7. Supporting public records

- J-PAL evaluation record: `Economic Returns to Street Paving in Mexico`, AEA RCT `AEARCTR-0001300`.
- Author replication-materials page: Harvard Dataverse DOI `10.7910/DVN/6TC8RO`.
- Published article: Gonzalez-Navarro & Quintana-Domeque (2016), DOI `10.1162/REST_a_00553`.
