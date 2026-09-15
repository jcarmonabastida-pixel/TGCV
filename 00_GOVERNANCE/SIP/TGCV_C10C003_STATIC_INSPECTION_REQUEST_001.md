# TGCV C10-C — C10C-003 India Static Inspection Request 001

## Status

`AUTHORIZED — STATIC INSPECTION ONLY`

## Frozen source

C10C-003 India, Harvard Dataverse DOI `10.7910/DVN/QXKPHH`, released dataset version `2`, dataset version ID `126497`. Byte-level local acquisition is frozen in `TGCV_C10C003_SOURCE_VERSION_FREEZE_003.md`.

## Objective

Inspect the frozen replication package without executing replication code, to determine whether the data and documented construction permit an independent, non-circular operationalization of:

`S0, S1, U_tau, P_tau(S,C,L), T_acc,0, T_acc,1, Delta T_acc`.

## Authorized inspection

1. Read `ReadMe.txt` as text.
2. Read the five `.do` files as text only.
3. Inspect Stata/tabular variable names, labels, coding and longitudinal identifiers as metadata/data inspection.
4. Record transformation-relevant variables and their timing/provenance.
5. Determine whether accessibility can be defined prospectively, independently of treatment realization, subscription/take-up and downstream outcomes.

## Prohibited

- Executing any `.do` file or other replication code.
- Reproducing published causal estimates as a scientific result.
- Selecting variables using treatment effects or downstream outcomes.
- Defining `U_tau` from observed post-treatment configurations.
- Treating treatment assignment as `T_acc`.
- Treating subscription/take-up as accessibility.
- Any causal estimation or value inference.
- Modification of TGCV Core or reopening prior closed gates.

## Required output

A bounded static/data-structure audit reporting, for each target object, one of:

- `ESTABLISHED`
- `PARTIAL`
- `NOT_IDENTIFIED`
- `NOT_TESTABLE_FROM_PACKAGE`

with explicit evidence and any finite blocker. No empirical TGCV claim is authorized by this inspection alone.
