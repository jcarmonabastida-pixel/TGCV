# D-OPS-6 — Cross-Domain Discovery Search II v0.1

**Status:** CLOSED — POWER-GRID DOMAIN RETAINED AS BEST CANDIDATE, NOT SELECTED
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Purpose

Search for an external empirical domain in which the accessibility predicate can be derived from an independently governed rule/constraint system rather than from observed behaviour, fitness, outcomes or future states.

## 2. Discovery results

### A — Power-grid topology / reconfiguration

Public datasets provide unusually strong structural ingredients. RTE's French transmission-grid structural dataset contains 5-minute snapshots from 2021–2023 and represents the complete grid in node-breaker topology, with structural and parameter information but without injections or power flows. citeturn0search11

Other public power-system datasets explicitly contain contingency configurations, topology and operating states. citeturn0search0turn0search9 Dynamic reconfiguration datasets also represent temporal graph evolution under grid failure/reconfiguration scenarios. citeturn0search6

Potential TGCV mapping:
- `S`: grid topology/configuration at time t;
- `Uτ`: admissible topology reconfiguration actions, e.g. switching/opening/closing defined network elements;
- `Pτ`: independently specified electrical/topological safety and operating constraints;
- `T_acc`: reconfigurations satisfying those constraints before execution;
- `Reach`: resulting successor grid configurations;
- `ΔT_acc`: change in admissible reconfiguration space between frozen grid states.

Strength: the rule layer can be defined independently of observed reconfiguration outcomes. The physical/engineering constraints are not themselves observations of whether a particular action was subsequently taken.

Main blocker: the currently identified public datasets differ substantially in whether they expose a longitudinal sequence of *decision states* and an independently frozen admissibility model. Some provide snapshots; others provide simulated contingency scenarios. This requires a dedicated identifiability audit before selection.

**Disposition: RETAIN as primary candidate for D-OPS-7.**

### B — Electricity market / grid operational states

The Western/Northeastern U.S. power-grid dataset provides hourly prices plus network topology and MATPOWER cases. citeturn0search2

However, market prices and operating values introduce outcome/economic variables that are not necessary for accessibility. The dataset is therefore secondary to the structural RTE topology candidate.

**Disposition: RETAIN only as supporting source, not primary candidate.**

### C — Synthetic power-grid benchmark families

PFΔ contains 859,800 solved power-flow instances across multiple topologies and N/N-1/N-2 contingencies, with public data and generation code. citeturn0academia48turn0search10

Its strength is explicit, rule-governed topology variation; its weakness is that it is a benchmark ensemble rather than naturally observed longitudinal evolution. It could support a controlled structural experiment but would not provide independent empirical temporal evolution comparable to Rust.

**Disposition: secondary methodological candidate.**

### D — Rail timetable data

Renfe publishes public timetable datasets for high-speed, long-distance and medium-distance services. citeturn0search12

The dataset is useful for observing service configurations, but the currently identified resource does not establish a versioned longitudinal rule system sufficient to define independent `Pτ` and `ΔT_acc` without further reconstruction.

**Disposition: not selected.**

## 3. Comparative result

| Candidate | Independent rules/constraints | Longitudinal structural data | Independent Uτ/Pτ | Reach separable | Current decision |
|---|---:|---:|---:|---:|---|
| RTE power-grid topology | PASS/CONDITIONAL | PASS | CONDITIONAL | PASS/CONDITIONAL | **RETAIN** |
| US power-grid operational data | CONDITIONAL | PASS | CONDITIONAL | CONDITIONAL | Secondary |
| PFΔ synthetic grid | PASS | FAIL for natural longitudinal evolution | PASS | PASS | Secondary |
| Renfe timetable | CONDITIONAL | CONDITIONAL | FAIL/CONDITIONAL | CONDITIONAL | Reject |

## 4. D-OPS-6 decision

**A power-grid topology/reconfiguration domain is the strongest candidate identified so far, but it is NOT selected for execution.**

The decisive remaining question is whether a specific public grid dataset can support a frozen, independently defined `Pτ` and a longitudinal state population without importing observed switching decisions, contingency outcomes, market results or post-state information.

This is sufficiently concrete to justify a focused next gate, rather than another broad discovery search.

## 5. Next controlled operation

Open **D-OPS-7 — Power-Grid Topology/Reconfiguration Admissibility & Identifiability Audit**.

The audit must select one concrete public dataset and test, without downloading or executing it:

1. exact state unit and temporal boundary;
2. independently defined transformation universe `Uτ`;
3. canonical transformation identity;
4. independent pre-execution `Pτ` based only on frozen engineering/topological rules;
5. construction of `T_acc` without observed switching/outcome leakage;
6. distinct successor configuration and `Reach` semantics;
7. longitudinal comparability of `ΔT_acc`;
8. reproducibility and exact provenance;
9. information gain relative to Rust;
10. explicit falsifiers.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
