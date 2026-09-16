# TGCV MT4-8 — Value Isolation Result 001

## Status
**BOUNDED PASS — VALUE VARIABLES STRUCTURALLY ISOLATED; TGCV DELTA-V ENDPOINT NOT ESTABLISHED**

## Source integrity
Frozen source SHA256:
`691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`

## Audit result
- Technology parameter rows: 254,421
- CORE6 rows: 79,920
- `Inv` rows: 13,320
- `Fixed_OM_annual` rows: 13,320
- `Variable_OM` rows: 13,320
- `Actual_*` rows: 53,280
- CORE6/value overlap violations: 0
- All three economic/value-related variables span 1990-2019.

## Reconciliation
The audit confirms structural isolation of the predefined economic/value-related variables from the CORE6 candidate accessibility rule. None of `Inv`, `Fixed_OM_annual`, or `Variable_OM` enters the candidate technical representation.

The common 1990-2019 span does **not** establish downstream ordering relative to each realized transformation. These variables may function as techno-economic inputs or parameters rather than downstream value outcomes. The audit therefore does not promote them to TGCV `Delta V`.

## Decision
`MT4-8 = BOUNDED PASS`.

The value layer is protected from circular inclusion in accessibility/admissibility, but a clean downstream value endpoint has not been established. No causal value effect is inferred.

## Claim boundaries
This result does not establish:
- full sufficiency or general validity of `P_tau`;
- `Delta T_acc -> Delta V`;
- a causal effect on economic value;
- that `Inv`, `Fixed_OM_annual`, or `Variable_OM` are downstream outcomes;
- transversal causal validity of TGCV.

## MT4 disposition
MT4 has demonstrated bounded methodological transfer through reproducible structural, semantic, temporal, reproducibility, downstream-separation, and value-isolation controls. The principal unresolved boundary is the construction of a clean full `P_tau` and an independently defined downstream outcome/value endpoint.
