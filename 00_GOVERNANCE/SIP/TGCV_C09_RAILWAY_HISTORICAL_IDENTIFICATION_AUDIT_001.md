# TGCV — C09 Historical Railway Identification Audit 001

**Status:** `COMPLETED — CANDIDATE NOT ADMITTED FOR CAUSAL EXECUTION`
**Date:** 2026-09-12
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Gate:** `TGCV_C09_DOMAIN_IDENTIFICATION_GATE_001.md`
**Preceding audit:** `TGCV_C09_HISTORICAL_LONGITUDINAL_FEASIBILITY_AUDIT_001.md`

## 1. Objective

Audit the historical railway domain as a concrete C09 candidate. The question is whether a historical railway intervention can be represented as an independently determined change in accessibility, with pre-treatment `T_acc`, a credible counterfactual, and an independently observed subsequent trajectory, while preserving the C09 information firewall.

This is an identification audit only. No dataset acquisition, model fitting, causal estimation or execution authorization follows from this record.

## 2. Discovery evidence

### 2.1 Sweden, 1860–1917

Lindgren, Pettersson-Lidbom and Tyrefors use annual panel data for approximately 2,400 Swedish rural geographical areas/local governments over 1860–1917, with up to 1,340 local railway openings and a staggered event-study design. The study reports long pre-treatment histories and treatment/control trend diagnostics. This establishes that a historical railway domain can provide fine-grained temporal treatment assignment and independently measured post-treatment outcomes.

The source does not itself operationalize TGCV `T_acc`; its treatment is access to railways and its outcomes are economic activity measures. Therefore it is evidence of identification feasibility, not C09 evidence.

### 2.2 Portugal, 1971–2021

Melo et al. report a newly constructed longitudinal spatial database of Portuguese railway infrastructure and services for 1971–2021, including station operation, line extension, service frequencies and travel times. The study documents line closures, service restructuring and selective modernization as changes in rail accessibility across municipalities.

The associated TASSEL Railway Database explicitly contains station-level and municipality-level infrastructure/service variables and origin-destination travel times. This is strong evidence that historical railway accessibility can be reconstructed longitudinally.

However, the documented changes are institutionally selected and may be jointly determined with expected economic trajectories. Therefore intervention independence remains unresolved.

## 3. C09 identification audit

| Requirement | Finding | Disposition |
|---|---|---|
| Stable unit identity | Historical local governments/municipalities provide identifiable longitudinal units | **PASS — bounded** |
| Reconstructible `S0,C0` | Annual/panel infrastructure and socioeconomic histories permit pre-treatment reconstruction | **PASS — candidate** |
| Bounded transformation universe `U_tau` | Destinations/connections/services can define an operational candidate universe | **PASS — designable** |
| Frozen accessibility rule `L` | Railway network/service data can define pre-treatment accessibility | **PASS — designable** |
| Pre-treatment `T_acc,0` | Network/service state exists before treatment | **PASS — candidate** |
| Independent accessibility intervention | Railway openings/closures are externally dated interventions, but assignment may reflect anticipated demand/policy/economic factors | **OPEN — CRITICAL** |
| Intervention changes `T_acc` without directly encoding trajectory | Plausible for physical/service opening or closure, but not demonstrated at the exact unit/intervention level | **OPEN — CRITICAL** |
| Credible counterfactual | Swedish staggered event-study provides strong methodological precedent; candidate-specific admissibility still requires raw-data/provenance audit | **PASS — precedent / NOT YET ADMITTED** |
| Independent post-treatment trajectory | Income, population, employment and other outcomes are independently measurable | **PASS — bounded** |
| Temporal separation | Annual panel structure is sufficient in principle | **PASS — bounded** |
| No future/outcome leakage in `T_acc` | Feasible in principle if only pre-treatment network/service information is used | **PASS — design condition / NOT YET VERIFIED** |
| Provenance/reproducibility | Public scholarly/database provenance exists for identified sources | **PASS — preliminary** |

## 4. Critical identification issue

The central unresolved issue is not whether rail accessibility changes exist. They do.

The unresolved issue is whether a concrete railway intervention can be treated as an admissible C09 intervention rather than as an outcome-linked infrastructure investment.

Railway construction, service expansion, closure and modernization can be selected because of anticipated economic growth, political priorities, population trends, strategic planning or other factors that may also affect the subsequent trajectory. A conventional causal design may address some of these issues, but C09 additionally requires the treatment to be interpretable as a change in `T_acc` without encoding the target trajectory through the intervention itself.

Accordingly:

`railway treatment -> economic outcome`

is not yet equivalent to:

`accessibility intervention -> ΔT_acc -> subsequent trajectory`.

The latter mapping must be explicitly constructed and audited.

## 5. Candidate operationalization

A potentially admissible unit would be:

`u = municipality/local government × decision year`

with:

- `S0`: pre-treatment physical/service state;
- `C0`: pre-treatment institutional, geographic and service context;
- `U_tau`: bounded destination/service transformation universe;
- `L`: frozen accessibility rule based exclusively on information available at `t0`;
- `T_acc,0 = F(S0,C0,L)`;
- `Z`: externally dated railway opening/closure/service intervention;
- `T_acc,1 = F(S1,C1,L)`;
- `ΔT_acc = T_acc,1 ≄ T_acc,0`;
- `Y`: independently defined post-intervention trajectory over a fixed horizon.

A valid design would have to establish that `Z` changes accessibility without directly specifying `Y`, and that untreated/counterfactual units provide a credible estimate of the trajectory that would have occurred without the accessibility change.

## 6. Information-firewall test

### Admissible information for `T_acc,0`

- railway network and service state existing before `t0`;
- station/service availability before `t0`;
- travel times/connectivity calculated from pre-treatment information;
- stable geographic and institutional characteristics available before `t0`.

### Forbidden information for `T_acc,0`

- post-treatment population/income/employment;
- later railway outcomes;
- trajectory realizations;
- treatment-response estimates;
- outcome-selected accessibility definitions.

The firewall is technically designable but has not yet been demonstrated on a concrete frozen dataset.

## 7. Identification hierarchy assessment

The Swedish historical railway evidence demonstrates that staggered event-study identification with annual panel data can provide a credible treatment/control architecture and long pre-treatment trend checks. It therefore materially strengthens the feasibility assessment.

It does **not** automatically establish C09 because the published treatment is railway access itself, not a TGCV-defined accessibility intervention followed by an independently reconstructed `ΔT_acc`.

The Portuguese TASSEL database is particularly promising for direct `T_acc` reconstruction because it contains stations, line extensions, frequencies and travel times. However, the institutional causes of closures, restructuring and modernization require a separate treatment-assignment audit before they can be admitted as C09 interventions.

## 8. Decision

**C09 HISTORICAL RAILWAY IDENTIFICATION AUDIT = PASS AS FEASIBILITY / FAIL AS CURRENT EXECUTION ADMISSION**

The railway domain is now a **concrete high-priority C09 candidate**, not merely a generic historical domain class.

However:

**CONCRETE C09 EXECUTION CANDIDATE = NOT YET ADMITTED**

The remaining gate is a candidate-specific treatment-assignment and data-provenance audit. That audit must verify, on one selected historical railway dataset/episode, that:

1. treatment assignment is independently reconstructible;
2. pre-treatment `T_acc` can be frozen without leakage;
3. the intervention produces an observable `ΔT_acc`;
4. the counterfactual is reconstructible from the same pre-treatment information;
5. the post-treatment trajectory is independently defined;
6. direct treatment pathways and major confounding explanations are explicitly handled.

## 9. Execution boundary

`EXECUTION AUTHORIZATION = NONE`

No dataset acquisition, causal estimation, model fitting, external intervention, AWS mutation, Rust rerun or SWIM rerun is authorized.

## 10. Claim boundary

No C09 claim upgrade follows from this audit.

C09 remains `OPEN — UNTESTED CAUSAL CLAIM`.

The audit establishes only that historical railway infrastructure is a **credible and unusually promising candidate architecture for attempting C09 identification**, subject to the remaining candidate-specific treatment-assignment/data audit.
