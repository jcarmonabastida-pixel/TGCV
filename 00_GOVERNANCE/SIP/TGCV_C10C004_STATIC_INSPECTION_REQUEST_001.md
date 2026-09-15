# TGCV C10-C — C10C-004 Morocco Static Inspection Request 001

## Status

`AUTHORIZED — STATIC INSPECTION ONLY`

## Frozen source

C10C-004 Morocco, openICPSR Project 116333, Version V1, DOI `10.3886/E116333V1`, released 2019-12-07. Byte-level local acquisition is frozen in `TGCV_C10C004_SOURCE_VERSION_FREEZE_001.md`.

Frozen input package:
- `Microcredit_BL_mini_anonym.dta`
- `Microcredit_EL_mini_anonym.dta`
- `Microcredit_MS_anonym.dta`

The V1 repository also contains documented DoFiles and survey instruments; these may be inspected only as static documentation if acquired into the authorized inspection workspace. The official source lists five DoFiles: `Analysis_Oct2014.do`, `Graphs_Oct2014.do`, `MASTER_Alamana_Oct2014.do`, `OutcomeConstruction_baseline_Oct2014.do`, and `OutcomeConstruction_endline_Oct2014.do`.

## Objective

Inspect the frozen replication package without executing replication code, to determine whether the data and documented construction permit an independent, non-circular operationalization of:

`S0, S1, U_tau, P_tau(S,C,L), T_acc,0, T_acc,1, Delta T_acc`.

The inspection is deliberately bounded. It must seek a finite, operationally defensible transformation space derivable prospectively from the package and documentation, without defining accessibility from treatment realization, take-up or downstream outcomes.

## Authorized inspection

1. Inspect the three frozen Stata datasets at metadata/data-structure level only.
2. Inspect the five V1 DoFiles as text only, if locally available/acquired for this inspection.
3. Inspect survey instruments and README documentation as static source material, if locally available/acquired.
4. Identify longitudinal/household/village identifiers, timing variables, treatment assignment, treatment realization/take-up variables, and candidate state variables.
5. Record transformation-relevant variables and their timing/provenance.
6. Determine whether a finite candidate `U_tau` can be justified prospectively from the package.
7. Determine whether `P_tau(S,C,L)` can be defined independently of treatment assignment, treatment realization, take-up and downstream outcomes.
8. Determine whether `T_acc,0`, `T_acc,1` and `Delta T_acc` are reconstructible from the frozen package under that bounded operationalization.
9. Explicitly distinguish observed state transitions, treatment assignment, treatment realization and take-up from prospective accessibility.
10. Record any finite blocker that prevents closure of the TGCV objects.

## Prohibited

- Executing any `.do` file or other replication code.
- Reproducing published causal estimates as a scientific result.
- Selecting variables using treatment effects or downstream outcomes.
- Defining `U_tau` from observed post-treatment configurations.
- Treating treatment assignment as `T_acc`.
- Treating loan realization, take-up or borrowing as accessibility.
- Treating observed outcomes or conventional causal estimands as `Delta T_acc`.
- Any causal estimation or value inference.
- Modifying TGCV Core or reopening prior closed gates.

## Required output

A bounded static/data-structure audit reporting, for each target object, one of:

- `ESTABLISHED`
- `PARTIAL`
- `NOT_IDENTIFIED`
- `NOT_TESTABLE_FROM_PACKAGE`

with explicit evidence, provenance and any finite blocker.

The report must explicitly state whether the blocker is:

1. a package-level operationalization limitation;
2. a data-structure limitation; or
3. an unresolved identification issue within the bounded inspection scope.

It must not generalize a bounded blocker into a claim that the complete transformation universe is intrinsically intractable or incompatible with TGCV.

No empirical TGCV claim, claim-level upgrade, causal result or Core modification is authorized by this inspection alone.
