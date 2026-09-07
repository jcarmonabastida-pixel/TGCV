# TGCV — Domain Instantiation Selection Gate v0.1

**Status:** RECONSTRUCTED / WORKING  
**Date:** 2026-09-07  
**Phase:** Architecture development and empirical validation preparation

## 1. Purpose

Select the first concrete empirical domain in which the frozen TGCV representation contract can be instantiated without importing TGCV assumptions, redefining accessibility retrospectively, or confusing a native domain construct with `T_acc`.

This Gate selects a **domain for operational validation**, not a preferred empirical result. No outcome or predictive model is selected by this Gate.

## 2. Locked inputs

This Gate inherits:

- `Core_ontological = S`;
- `T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`;
- `ΔT_acc` as the primary differentiated candidate;
- `Reach` and `Trajectory` as distinct downstream objects;
- `Outcome` and `Value` as downstream layers;
- `I` as explanatory mechanism;
- SLR-1 closed;
- TR-130–TR-140 closed;
- Operational Representation Specification Gate closed;
- EXT-1.1 Rust retained only as a prior empirical precedent, not as automatic methodological template.

## 3. Selection principle

The first domain should maximize **identifiability and falsifiability**, not apparent theoretical fit.

A domain is eligible only if its data can support, with explicit bounded coverage:

`U_τ → P_τ → T_acc,t → ΔT_acc(t,t+1)`

and can preserve the distinction:

`accessibility ≠ execution ≠ outcome`.

## 4. Candidate domains

The candidate pool is restricted initially to domains already encountered in the SLR-1 and EXT-1.1 program, avoiding ad hoc expansion of the search space.

### D1 — Rust software ecosystem

Strengths:
- large longitudinal package/version/dependency data;
- transformations can be specified around package/version dependency changes;
- EXT-1.1 already demonstrated that a frozen accessibility-like representation can be reconstructed at scale;
- extensive prior audit infrastructure exists.

Risks:
- the previous `TAcc_repr=(A_rel,A_count)` is domain/protocol-specific;
- dependency admissibility may represent a narrow transformation class rather than a generic transformation universe;
- previous outcome experiment was negative descriptively, creating risk of methodological anchoring;
- a new instantiation must be designed independently.

### D2 — Model-driven engineering / model transformation systems

Strengths:
- explicit transformation rules/operators;
- applicability conditions;
- explicit transformation search spaces;
- reachable model states and trajectories.

Risks:
- very high local prior-art overlap;
- datasets may encode transformations and applicability directly, making non-redundancy harder to demonstrate;
- event histories may be less naturally census-like at scale.

### D3 — Self-adaptive / self-evolving software

Strengths:
- explicit adaptation spaces;
- temporal drift in available adaptation options;
- strong direct precedent for changing accessible options.

Risks:
- native `adaptation space` is extremely close to `T_acc`;
- risk that TGCV becomes a relabeling unless a genuine cross-domain analytical remainder is demonstrated;
- datasets may be experimental rather than longitudinal at ecosystem scale.

### D4 — Organizational capability / opportunity systems

Strengths:
- capability space and opportunity space evolve;
- explicit potential versus realized possibilities;
- strong relevance to value and downstream trajectories.

Risks:
- transformation identity may require substantial reconstruction;
- accessibility can become conceptually normative or evaluative;
- observational datasets may not expose sufficient temporal granularity.

### D5 — State-space / reachability systems

Strengths:
- precise state, transition and reachability semantics;
- strong mathematical identifiability;
- counterfactual reasoning is natural.

Risks:
- accessible transformations may be encoded directly in transition relations;
- high risk of proving only a representational restatement;
- empirical datasets may be simulation-generated rather than naturally observed.

### D6 — Generativity / adjacent-possible systems

Strengths:
- explicit evolving possibility spaces;
- generative transformation processes;
- direct relevance to expansion of future possibilities.

Risks:
- `possibility` is not automatically a transformation;
- outcome/value connection can become theory-dependent;
- operational candidate universes may be difficult to reconstruct independently.

## 5. Mandatory selection criteria

Each candidate is scored qualitatively against the following criteria before selection:

| Criterion | Requirement |
|---|---|
| DS-1 | Stable unit of analysis |
| DS-2 | Longitudinal observation |
| DS-3 | Independently constructible `U_τ` |
| DS-4 | Explicit non-circular `P_τ` |
| DS-5 | Reconstructable `T_acc` |
| DS-6 | Reconstructable `ΔT_acc` |
| DS-7 | Accessibility observable before execution |
| DS-8 | Empty/unresolved cases representable |
| DS-9 | Reach/Trajectory distinguishable |
| DS-10 | Outcome separable from accessibility |
| DS-11 | Sufficient provenance/reproducibility |
| DS-12 | Low dependence on ad hoc TGCV assumptions |
| DS-13 | Falsifiable substantive non-redundancy |
| DS-14 | Feasible execution with available tooling/data |

A candidate must not be selected merely because it has the largest apparent theoretical similarity.

## 6. Preliminary bounded assessment

At the current evidence state:

- **D1 Rust:** strongest operational readiness because prior data engineering, temporal audit, candidate-universe construction and reproducibility controls already exist. However, this advantage must not contaminate the new representation or outcome protocol.
- **D2 MDE:** excellent semantic identifiability but substantial risk of local representational redundancy.
- **D3 Self-adaptive software:** excellent direct accessibility semantics but very high local construct overlap.
- **D4 Organizational:** theoretically valuable but transformation-level reconstruction is less direct.
- **D5 State-space:** mathematically clean but strongest risk of representational restatement.
- **D6 Generativity:** conceptually relevant but weakest current empirical identifiability of transformation-level accessibility.

## 7. Selection decision rule

The first empirical domain is selected when one candidate satisfies the following minimum condition:

`DS-3 ∧ DS-4 ∧ DS-5 ∧ DS-6 ∧ DS-7 ∧ DS-8 ∧ DS-10 ∧ DS-11 ∧ DS-13`

with no unresolved critical failure in `DS-1`, `DS-2` or `DS-12`.

If multiple domains satisfy the condition, prefer the one with:

1. strongest direct observability;
2. lowest circularity risk;
3. strongest temporal coverage;
4. clearest independent candidate universe;
5. lowest proxy dependence;
6. highest reproducibility.

## 8. Rust-specific independence safeguard

If Rust is selected, the new protocol must explicitly state that:

- `DR-026A TAcc_repr=(A_rel,A_count)` is not adopted as the canonical TGCV representation by inheritance;
- the prior EXT-1.1 outcome is not used to choose hypotheses, features, windows or model class;
- the new `U_τ`, `P_τ` and `ΔT_acc` are specified independently before examining the new outcome;
- prior Rust infrastructure may be reused only where it is generic data-engineering infrastructure and its reuse is documented;
- any domain-specific accessibility semantics are justified independently.

## 9. Exclusion rules

A domain must be rejected at this Gate if:

1. accessibility can only be inferred from future execution or outcome;
2. no independent candidate universe can be constructed;
3. `T_acc` can only be represented by an unvalidated proxy;
4. temporal comparison is impossible;
5. unresolved relations cannot be distinguished from inaccessible relations;
6. the proposed test would merely reproduce a native variable without analytical remainder;
7. the required data are unavailable or irreproducible;
8. selecting the domain requires changing the locked TGCV architecture.

## 10. Gate criteria

| Criterion | Result |
|---|---|
| DS-G1 | Candidate pool bounded to previously established domains — PASS |
| DS-G2 | Selection criteria defined ex ante — PASS |
| DS-G3 | Independent `U_τ` required — PASS |
| DS-G4 | Non-circular `P_τ` required — PASS |
| DS-G5 | `T_acc` reconstruction required — PASS |
| DS-G6 | `ΔT_acc` reconstruction required — PASS |
| DS-G7 | Accessibility/execution separation required — PASS |
| DS-G8 | Temporal and unresolved-case requirements explicit — PASS |
| DS-G9 | Outcome separated from accessibility — PASS |
| DS-G10 | Reproducibility/provenance required — PASS |
| DS-G11 | Domain selected for confirmatory study — NOT YET |

## 11. Gate decision

**PASS — DOMAIN SELECTION CONTRACT ESTABLISHED; CONCRETE DOMAIN SELECTION REMAINS OPEN UNTIL CANDIDATE AUDIT.**

This is intentionally not a forced domain-selection decision. The next operation must audit the leading candidate domains against the criteria above using their actual available data structures before selecting one.

## 12. Immediate next controlled operation

**TGCV Domain Candidate Audit — Rust vs Self-Adaptive Software vs MDE**.

The audit should be performed at the representation level only, without outcome/model selection. It must determine which candidate provides the cleanest independent construction of `U_τ`, `P_τ`, `T_acc` and `ΔT_acc`.

Only after that audit may the program freeze a concrete domain instantiation.

## 13. Integrity lock

No domain is considered selected merely because it is operationally convenient. Convenience is subordinate to identifiability, non-circularity, reproducibility and falsifiability.

No outcome, predictive model or value hypothesis may be optimized around the domain before the domain-selection decision is frozen.
