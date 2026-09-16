# TGCV MT4-8 — Value Isolation Protocol 001

## Status
**ANALYSIS PROTOCOL — NOT GOVERNANCE-NORMATIVE**

## Objective
Test whether value-related/economic variables in the frozen electricity-system dataset can be isolated downstream from the construction of candidate admissibility/accessibility, while preserving temporal order and avoiding circular use of outcomes or value to define `P_tau` or `T_acc`.

## Frozen source
Jaxa-Rozen, Wen & Trutnevyte, Historic data of national electricity-system transitions in Europe, Zenodo 6696776 v2.
Source SHA256:
`691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`

## Frozen candidate accessibility rule
The MT4 transfer retains the bounded technical candidate representation:
`CORE6 = Fuel_efficiency, LF_min, LF_max, Peak_contr, Ramp_rate, Resource`.

The following are prohibited from entering `P_tau` solely because they are economically meaningful or correlated with realized outcomes:
`Inv`, `Fixed_OM_annual`, `Variable_OM`.

`Potential_annual`, `Potential_installed`, `Buildrates`, and all `Actual_*` variables remain outside the minimum candidate rule unless independently justified by prior MT4 evidence.

## Value-isolation audit questions
1. Are economic/value-related variables structurally disjoint from CORE6?
2. Can economic/value-related variables be located in time relative to realized transformations without using them to define accessibility?
3. Are there candidate economic variables that are themselves inputs/constraints rather than downstream value outcomes?
4. Is there any variable that can be interpreted as a downstream economic outcome without being part of the accessibility rule?
5. Can a value-related change be represented as a downstream quantity without silently equating an economic parameter with TGCV `Delta V`?
6. Does the dataset provide enough temporal information for a non-circular value test, or must the result remain bounded?

## Decision rules
- **PASS**: value-related variables are demonstrably isolated from the accessibility rule, temporal ordering is auditable, and at least one downstream value-related endpoint can be identified without circularity.
- **BOUNDED PASS**: isolation and temporal discipline are reproducible, but no sufficiently clean downstream value endpoint is established.
- **FAIL**: value/economic variables are required to define accessibility or cannot be separated without circularity.
- **INVALID/REJECTED**: source integrity or required temporal information is unavailable.

## Prohibited inference
This protocol does not permit interpreting `Inv`, `Fixed_OM_annual`, or `Variable_OM` as `Delta V` merely because they are economic variables. A value endpoint requires an independently defined temporal contrast or outcome interpretation. No causal effect is inferred by this protocol.

## Execution discipline
The audit must run locally against the frozen ZIP and return a compact summary. No full dataset is to be transported into the conversation. The result must be reconciled before any MT4 status is changed.
