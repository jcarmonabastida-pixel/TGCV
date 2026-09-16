# TGCV MT4-5 — Pτ Sufficiency Decision Note 001

**Status:** ANALYTICAL DECISION NOTE — NOT GOVERNANCE-NORMATIVE  
**Date:** 2026-09-16

## 1. Question

Determine whether the MT4 source permits a defensible ex-ante technical admissibility representation `Pτ` from the inspected evidence, without defining accessibility retrospectively from realization, adoption, outcome, or value.

## 2. Established evidence

- CORE6 = `Fuel_efficiency + LF_min + LF_max + Peak_contr + Ramp_rate + Resource`.
- Complete CORE6 coverage: 12,331 / 13,320 country-technology-year cells = 92.58%.
- Missingness is structured: 900 Storage cells lack Ramp_rate; 89 Swiss cells lack Fuel_efficiency. The latter includes public-distribution/source restrictions; neither pattern is recoded as N/A or imputed.
- CORE6 has substantial variation and discrimination: 930/930 country-year groups with >=2 complete technologies also have >=2 distinct CORE6 signatures; 5,945 unique signatures globally.
- The sole duplicate CORE6 signature occurs in Estonia 1990, HydroRoR vs HydroDam.
- In that collision, `Potential_annual` differs: HydroRoR 1746.027163 GWh vs HydroDam 589.783628 GWh.
- Both `Potential_annual` records cite the same source (Hoes et al. 2017, Section 6.6) and the targeted temporal review found no textual future/retrospective flag.

## 3. Decision

The evidence supports the following bounded conclusion:

> A technically meaningful candidate admissibility layer can be represented by CORE6 for a large majority of country-technology-year cells, while `Potential_annual` provides demonstrated additional discriminative information in the sole observed CORE6 collision. However, the available evidence does not establish that CORE6 alone, or CORE6 plus `Potential_annual`, is a sufficient and generally valid representation of full `Pτ`.

Therefore:

- `P_TAU_TECHNICAL = PARTIALLY_FORMALIZED`
- `P_TAU_FULL = UNDETERMINED`
- `MT4-5 = OPEN / BOUNDED`

## 4. Why no sufficiency claim is made

Coverage and discrimination demonstrate information content, not semantic completeness. The source contains additional technical, economic, planning/legal, resource and potential variables with heterogeneous temporal provenance. In particular, `Potential_annual` cannot be promoted merely because it resolves a collision; its general role as an independent ex-ante admissibility constraint remains unproven.

Observed variables such as `Actual_capacity`, `Actual_generation`, `Actual_new_capacity`, and `Actual_retired_capacity` remain realization/transition variables and are excluded from admissibility construction.

## 5. Consequence for MT4

MT4-5 should not be forced to PASS or FAIL. The appropriate result is a **bounded transfer result**: the dataset supports a substantial, auditable technical admissibility representation, but does not permit a claim of complete `Pτ` reconstruction from the currently demonstrated evidence.

The next informative operation is therefore not another collision search. It is a prospective domain-transfer test using the bounded technical rule while explicitly recording unresolved components of full admissibility.
