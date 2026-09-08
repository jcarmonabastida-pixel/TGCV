# D-OPS-7 — Power-Grid Topology/Reconfiguration Admissibility & Identifiability Audit v0.1

**Status:** CLOSED — NO EXECUTION-READY OPERATIONALIZATION
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Concrete dataset audited

Primary candidate: **RTE7000 / D-GITT**, the French transmission-grid structural topology time series. RTE describes it as 5-minute snapshots covering 2021–2023, with approximately 7,000 nodes in node-breaker topology; injections and power-flow data are omitted. citeturn0search0turn0search1turn0search2

The dataset is public and reproducible, with the RTE GitHub repository and public dataset distribution identified. citeturn0search1turn0search2

## 2. TGCV identifiability assessment

| Criterion | Result | Assessment |
|---|---|---|
| D7-1 State unit S | PASS | A topology snapshot is a concrete structural state. |
| D7-2 Temporal boundary | PASS | 5-minute snapshots provide an explicit temporal index. |
| D7-3 Independent Uτ | CONDITIONAL | Switching/reconfiguration operations can be enumerated structurally, but the exact admissible operation universe must be frozen from an external engineering model. |
| D7-4 Canonical τ identity | PASS/CONDITIONAL | A switch/open-close operation can be canonically represented by component identity plus target state. Node-breaker topology provides component identities. |
| D7-5 Independent pre-execution Pτ | FAIL under current dataset alone | Topology alone does not establish electrical feasibility. RTE explicitly omits injections and power-flow quantities; these are needed for power-flow computation. citeturn0search0turn0search3 |
| D7-6 T_acc without outcome leakage | FAIL under current evidence | Without an independently frozen engineering constraint model, admissibility would either be trivial topological validity or be inferred from observed configurations/operations. |
| D7-7 Reach separability | CONDITIONAL | Successor topology can be structurally constructed, but meaningful Reach requires the same independent admissibility layer that is currently missing. |
| D7-8 Longitudinal ΔT_acc | FAIL under current operationalization | The dataset supplies longitudinal topology states, but changing observed topology is not equivalent to changing the set of transformations admissible from each state. |
| D7-9 Reproducibility | PASS | Public dataset and repository are identified. citeturn0search1turn0search2 |
| D7-10 Information gain beyond Rust | PASS | Electricity-grid reconfiguration is genuinely external to software package evolution. |
| D7-11 Firewall feasibility | PASS | The design can exclude switching observations, contingencies, flows, outcomes and market variables from Pτ. |
| D7-12 Falsifiability | PASS | A future independently frozen engineering model could fail the admissibility test or fail to distinguish ΔT_acc from downstream Reach. |

## 3. Decisive blocker

The RTE7000 dataset is exceptionally strong for **longitudinal structural state observation**, but that is not enough for TGCV.

The decisive missing element is an independently governed, versioned **engineering admissibility model** that maps `(S,C,L,τ)` to a pre-execution predicate `Pτ` without using observed switching decisions, future topology, contingency outcomes, power-flow results or market outcomes.

A trivial structural predicate such as “the resulting topology is syntactically valid” would be formally non-circular but scientifically insufficient: it would test graph/configuration mutation rather than engineering accessibility.

Conversely, defining admissibility from observed transitions or successful operating states would violate the TGCV firewall.

## 4. Why this is not a dataset failure

The finding is narrower than “power grids are unsuitable.” The domain remains conceptually compatible with TGCV. What is missing is a **jointly reproducible dataset + independent rule layer** suitable for empirical accessibility measurement.

Synthetic benchmark datasets can provide explicit engineering rules and simulated reconfiguration, but then the evidence would be primarily model-generated rather than an empirical longitudinal replication of the Rust result. Public contingency datasets likewise tend to provide scenario outcomes rather than an independently versioned accessibility space. citeturn0search13turn0search18

## 5. Decision

**D-OPS-7 = NO SELECTION.**

RTE7000 is retained as a high-quality structural-state resource, but it is not authorized for implementation or execution as a TGCV replication domain under the current architecture.

This reinforces the methodological constraint already observed in D-OPS-5: **longitudinal observations do not by themselves identify a changing accessibility space.**

## 6. Program consequence

The current empirical evidence remains:

- Rust: **E1 bounded structural/informational distinction** between `ΔT_acc` and `ΔReach¹_pot` under frozen operational semantics.
- Cross-domain generalisation: **H**.
- Causality: **H**.
- Predictive superiority: **H**.
- Value linkage: **H**.
- Universal validity: **H**.
- Originality/no equivalent architecture: **O**.

No scientific claim is upgraded by this audit.

## 7. Next controlled operation

Open **D-OPS-8 — Rule-Layer Discovery / Engineering-Constraint Search**.

The search should no longer start from a longitudinal dataset. It should start from an **independently published and reproducible rule system** capable of defining `Pτ`, and only then determine whether a longitudinal public dataset exists to instantiate it.

Priority characteristics:
1. explicit engineering rules or formal constraints;
2. public/versioned rule specification;
3. independently enumerable `Uτ`;
4. pre-execution admissibility;
5. downstream successor construction;
6. longitudinal states or repeated configurations;
7. no dependence on observed outcomes.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
