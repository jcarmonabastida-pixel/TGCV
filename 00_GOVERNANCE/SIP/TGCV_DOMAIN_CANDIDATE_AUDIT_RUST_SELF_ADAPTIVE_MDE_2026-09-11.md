# TGCV — Domain Candidate Audit: Rust vs Self-Adaptive Software vs MDE

**Date:** 2026-09-11  
**Status:** `CLOSED — BOUNDED CANDIDATE AUDIT`  
**Phase:** SIP-L2 / Architecture development and empirical validation preparation  
**Decision type:** domain-instantiation screening only

## 1. Purpose

Audit the three leading domain candidates identified by the existing TGCV Domain Instantiation Selection Gate — Rust software ecosystem, self-adaptive/self-evolving software, and model-driven engineering (MDE) — against the frozen representation contract for `U_τ`, `P_τ`, `T_acc` and `ΔT_acc`.

This audit does not select an outcome, predictive model, value hypothesis or confirmatory experiment.

It does not reopen EXT-1.1 or any closed scientific gate.

## 2. Mandatory reuse inputs

The audit reuses, without treating them as confirmatory evidence:

- Scientific Asset Registry v0.1;
- Operational Representation Specification Gate;
- Domain Instantiation Selection Gate;
- historical EXT-1.1 Rust dataset audit and selection decision;
- current Rust execution/reproducibility infrastructure.

The Scientific Asset Registry explicitly requires consultation of prior scientific assets before a new domain-selection operation and prohibits from-scratch treatment where relevant prior work exists.

## 3. Frozen screening criteria

The candidate must support, at least in principle and with bounded coverage:

`U_τ → P_τ → T_acc,t → ΔT_acc(t,t+1)`

while preserving:

`accessibility ≠ execution ≠ outcome`.

The primary screening criteria are:

- DS-3 independent candidate universe;
- DS-4 non-circular accessibility predicate;
- DS-5 reconstructable `T_acc`;
- DS-6 reconstructable `ΔT_acc`;
- DS-7 accessibility observable before execution;
- DS-8 unresolved/empty cases representable;
- DS-10 outcome separability;
- DS-11 provenance/reproducibility;
- DS-12 low dependence on ad hoc TGCV assumptions;
- DS-13 falsifiable substantive non-redundancy.

## 4. Candidate D1 — Rust software ecosystem

### Strengths

- Existing longitudinal package/version/dependency infrastructure.
- Stable package/version semantics are available in the established Rust research surface.
- Transformation candidates can be represented through dependency/version transitions rather than inferred from outcomes.
- Existing SemVer normalization, dependency-constraint representation, temporal pairing and identity-audit infrastructure can be reused as generic data-engineering components.
- Existing work has demonstrated executable reconstruction of accessibility-like structures at scale and reproducible frozen execution contexts.
- Current programme governance contains substantial provenance, freeze and reproducibility infrastructure for Rust.

### Critical limitation

The historical EXT-1.1 dataset-selection record explicitly closed Rust/Schueller for confirmatory execution because the historical `version_id → (crate, version)` identity join required for the original 2022-09-07 download series could not be established from the publicly recoverable artifacts then available.

Therefore existing Rust infrastructure establishes **operational readiness**, but it does not automatically establish a fresh confirmatory dataset identity for the present study.

### Screening assessment

| Criterion | D1 Rust |
|---|---|
| DS-3 `U_τ` | `PASS — strong candidate` |
| DS-4 `P_τ` | `PASS — strong candidate` |
| DS-5 `T_acc` | `PASS — reconstructable in bounded representations` |
| DS-6 `ΔT_acc` | `PASS — temporal comparison infrastructure exists` |
| DS-7 pre-outcome accessibility | `PASS — representable` |
| DS-8 unresolved/empty cases | `PASS — governed representation possible` |
| DS-10 outcome separation | `PASS — architecture supports separation` |
| DS-11 provenance/reproducibility | `PASS — strongest current programme support` |
| DS-12 low ad hoc dependence | `PASS WITH SAFEGUARD — fresh protocol required` |
| DS-13 non-redundancy | `OPEN / REQUIRES FRESH DOMAIN-SPECIFIC TEST` |

**D1 conclusion:** strongest current candidate for the first controlled instantiation, but **not yet selected for confirmatory execution**.

## 5. Candidate D3 — Self-adaptive / self-evolving software

### Strengths

- Native adaptation spaces provide a clear conceptual analogue for changing accessible options.
- Temporal changes in available adaptations are potentially observable before execution.
- Strong semantic fit for accessibility and dynamic change.

### Risks / current programme evidence

- The native adaptation-space construct is very close to `T_acc`, creating high local redundancy risk.
- The current TGCV repository does not contain a governed empirical dataset/infrastructure comparable to the Rust execution surface for a fresh domain instantiation.
- A new study would therefore require acquisition and independent reconstruction of `U_τ`, `P_τ`, temporal identity and unresolved cases before any meaningful comparison.
- Selecting D3 now would expand the empirical acquisition burden without current evidence that it improves identifiability relative to D1.

### Screening assessment

| Criterion | D3 Self-adaptive |
|---|---|
| DS-3 `U_τ` | `OPEN — dataset-specific` |
| DS-4 `P_τ` | `PASS IN PRINCIPLE` |
| DS-5 `T_acc` | `OPEN — dataset-specific` |
| DS-6 `ΔT_acc` | `OPEN — dataset-specific` |
| DS-7 pre-outcome accessibility | `PASS IN PRINCIPLE` |
| DS-8 unresolved/empty cases | `OPEN — dataset-specific` |
| DS-10 outcome separation | `OPEN — dataset-specific` |
| DS-11 provenance/reproducibility | `OPEN` |
| DS-12 low ad hoc dependence | `RISK — high native overlap` |
| DS-13 non-redundancy | `HIGH-RISK / OPEN` |

**D3 conclusion:** retain as a later cross-domain candidate; do not select as first empirical instantiation.

## 6. Candidate D2 — Model-driven engineering / model transformation systems

### Strengths

- Transformation rules/operators and applicability conditions are explicit.
- Transformation identity can often be specified directly.
- Reachability and trajectory semantics are naturally expressible.

### Risks / current programme evidence

- Native transformation-rule applicability is extremely close to the proposed `T_acc` representation.
- This creates the highest immediate risk of representational restatement rather than substantive analytical remainder.
- No current TGCV empirical execution surface equivalent to Rust has been frozen for a fresh domain instantiation.
- A new MDE dataset or benchmark would require a separate provenance and reproducibility construction before it could satisfy the representation contract.

### Screening assessment

| Criterion | D2 MDE |
|---|---|
| DS-3 `U_τ` | `PASS IN PRINCIPLE` |
| DS-4 `P_τ` | `PASS IN PRINCIPLE` |
| DS-5 `T_acc` | `PASS IN PRINCIPLE` |
| DS-6 `ΔT_acc` | `PASS IN PRINCIPLE` |
| DS-7 pre-outcome accessibility | `PASS IN PRINCIPLE` |
| DS-8 unresolved/empty cases | `OPEN — dataset-specific` |
| DS-10 outcome separation | `OPEN — dataset-specific` |
| DS-11 provenance/reproducibility | `OPEN` |
| DS-12 low ad hoc dependence | `HIGH-RISK — native overlap` |
| DS-13 non-redundancy | `HIGH-RISK / OPEN` |

**D2 conclusion:** retain as a prior-art pressure domain and later cross-domain validation candidate; do not select as first empirical instantiation.

## 7. Comparative decision

At the current bounded programme state:

**D1 Rust > D3 Self-adaptive > D2 MDE** for immediate operational readiness.

The ordering is not a claim of theoretical superiority. It reflects the combination of:

1. existing empirical infrastructure;
2. temporal data availability;
3. reproducibility controls;
4. ability to separate accessibility from execution/outcome;
5. lower immediate acquisition burden;
6. ability to run a bounded fresh identifiability test without expanding the candidate pool.

D2 and D3 remain scientifically useful precisely because their native constructs create strong redundancy pressure; they should not be discarded as irrelevant.

## 8. Selection status

**DOMAIN SELECTION STATUS: D1 RUST — PREFERRED CANDIDATE, NOT YET FROZEN.**

The audit does not authorize confirmatory execution.

A fresh small-slice domain-instantiation gate remains mandatory before freezing D1 as the empirical domain. The gate must independently establish:

- stable historical identity;
- independent `U_τ`;
- non-circular `P_τ`;
- reconstructable `T_acc,t`;
- reconstructable `ΔT_acc`;
- explicit pre-outcome accessibility;
- unresolved/empty-case handling;
- provenance and reproducibility.

The previous EXT-1.1 Rust outcome is not to be used to choose the new representation, hypotheses, features, windows or model class.

## 9. Immediate next controlled operation

The next operation is therefore **not confirmatory execution**.

It is the **Rust Domain Instantiation Small-Slice Identifiability Gate**, designed ex ante around the frozen Operational Representation Specification contract.

Only after that gate passes may a concrete empirical protocol be frozen.

## 10. Scientific boundary

This audit establishes only a bounded programme-management and methodological selection result:

> Rust currently offers the strongest controlled path to a fresh empirical instantiation of `T_acc` and `ΔT_acc`, subject to an independent small-slice identifiability gate.

It does not establish:

- empirical validity of TGCV;
- superiority of Rust as a domain;
- causal efficacy of `ΔT_acc`;
- predictive superiority;
- industrial utility;
- value creation;
- universal applicability or originality.

## 11. Closure

`DOMAIN CANDIDATE AUDIT = PASS — BOUNDED.`

`D1 RUST = PREFERRED / CONDITIONAL.`

`D2 MDE = RETAINED / HIGH REDUNDANCY PRESSURE.`

`D3 SELF-ADAPTIVE = RETAINED / HIGH REDUNDANCY PRESSURE.`

No confirmatory execution is authorized by this audit.
