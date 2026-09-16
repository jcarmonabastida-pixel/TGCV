# TGCV — Transversal Methodology Matrix — Candidate 001

**Status:** ANALYSIS ARTIFACT — CANDIDATE METHODOLOGY, NOT GOVERNANCE-NORMATIVE  
**Date:** 2026-09-16  
**Purpose:** Consolidate the currently supported methodological elements into an auditable matrix without upgrading claims, modifying TGCV Core/RMA, or declaring a closed TGCV methodology.

## 1. Governance boundary

This artifact operationalizes the previously authorized analytical question: whether a transversal methodology can be extracted from the accumulated cross-domain evidence without importing unsupported concepts.

It is deliberately **not** named `TGCV Methodology v1.0`. It does not modify the Evidence-to-Claim Matrix, RMA, Core, claim levels, or causal conclusions.

The matrix uses the following status vocabulary:

- **SUPPORTED:** repeatedly demonstrated or directly supported by existing evidence, subject to stated boundaries.
- **PARTIALLY SUPPORTED:** material evidence exists, but closure requires an additional test, replication, or domain transfer.
- **OPEN:** the methodological element has not yet been demonstrated sufficiently.
- **BOUNDARY / CONTROL:** evidence is principally useful for preventing an invalid substitution or overclaim.

## 2. Candidate transversal methodology matrix

| ID | Methodological element | Proposed rule / operation | Evidence | Gate / test | Boundary | Status |
|---|---|---|---|---|---|---|
| M-01 | State identification | Identify `S_t` from domain-observable structural, contextual and/or enabling-condition variables before defining downstream constructs. | SWIM; IT-G1; C10C-001; C10C-002; C10C-003; C10C-004 | State reconstruction / semantic audit | Domain-specific state variables do not automatically constitute TGCV Core state; external conditions must remain distinguishable from internal state. | SUPPORTED, bounded |
| M-02 | Candidate transformation universe | Define an explicit candidate universe `Uτ` independently of outcome/value variables. | C10C-002 provides the clearest bounded implementation; SWIM and other cases provide complementary transformation specifications. | Operationalization gate; pre-outcome specification | `Uτ` may remain unidentifiable in a frozen empirical package, as shown by C10C-001/C10C-003. Failure to identify it is a boundary result, not refutation. | PARTIALLY SUPPORTED |
| M-03 | Independent admissibility | Define executable `Pτ(S,C,L)` before outcome inspection and derive `T_acc={τ∈Uτ:Pτ=1}`. | SWIM bounded operationalization; C10C-002 structural-only predicates; C09/KGFS causal layer. C10C-001/C10C-003 show consequences when predicate is unavailable. | MT-1 identity; MT-3 non-circularity | Accessibility cannot be inferred from realization, treatment, adoption, take-up, configuration or outcome. | SUPPORTED, bounded |
| M-04 | Accessibility/realization separation | Keep accessible transformations distinct from transformations actually realized/executed/adopted. | C10C-001; C10C-002; C10C-003; SWIM; IT-G1 | Layer-identity audit; temporal ordering | Similar empirical labels do not justify semantic substitution. | SUPPORTED |
| M-05 | Transformation-space change | Compute `ΔT_acc` from independently reconstructed `T_acc,0` and `T_acc,1`; preserve the underlying transformation identities, not only cardinality. | Rust bounded evidence; C10C-002 reproducible `T_acc*` transition; SWIM | MT-1; bounded structural reconstruction; Rust identity tests | C10C-002's `T_acc*` is a bounded domain-specific universe; it does not close general `T_acc`. Cardinality alone is insufficient for Reach identity. | PARTIALLY SUPPORTED |
| M-06 | Execution / realization layer | Record whether candidate transformations are actually executed and distinguish this from accessibility and from subsequent trajectory. | SWIM; IT-G1; C10C-002; C10C-004 | Execution/reconstruction audit | Execution does not imply accessibility and does not by itself establish a trajectory effect. | SUPPORTED, bounded |
| M-07 | Subsequent trajectory | Define temporal ordering so that post-change transformations/states form a trajectory distinct from the transformation-space change itself. | SWIM trajectory-linkage reconstruction; KGFS/C09; IT-G1; C10C-001/C10C-003 boundary evidence | MT-1; trajectory criterion; C09 causal layer | C09 provides bounded causal evidence only for accessibility → subsequent trajectories; generality remains open. | PARTIALLY SUPPORTED |
| M-08 | Outcome separation | Define Outcome independently after the trajectory layer; do not use outcome identity to retroactively define accessibility. | SWIM; IT-G1; C10C-002; C10C-003; C10C-004 | Outcome-definition audit; temporal/non-circularity check | An observed outcome is not automatically TGCV Value and does not establish `T_acc`. | SUPPORTED |
| M-09 | Value separation | Introduce Value/`ΔV` only after accessibility, transformation and trajectory layers are independently defined; never construct `T_acc` from Value. | C10C-002 explicitly excludes value endpoints from `T_acc*`; cross-domain map; C10C-004 boundary | MT-3 non-circularity; downstream-value gate | `ΔT_acc → Value` is currently open; no end-to-end causal value pathway established. | SUPPORTED AS SAFEGUARD; VALUE LINK OPEN |
| M-10 | Reproducible translation | A second independent reconstruction from the same frozen material should recover the same operational objects/rules within the stated scope. | C10C-004 strong worked reconstruction; C10C-002 reproducibility; C09/KGFS reproducibility audit | MT-2 independent reconstruction | Existing evidence is distributed across cases; a formal cross-domain independent reconstruction of the complete protocol remains outstanding. | PARTIALLY SUPPORTED |
| M-11 | Non-circularity | Downstream information (Outcome/Value and later states) must not determine the earlier definition of `Uτ`, `Pτ` or `T_acc`. | C10C-002; C10C-001; C10C-003; C10C-004; C09 protocol boundaries | MT-3 | Non-circularity is demonstrated in bounded cases, not yet as a universally validated methodology. | SUPPORTED, bounded |
| M-12 | Domain transfer | Apply the same methodological distinctions across heterogeneous domains while retaining domain-specific semantics. | Software SWIM/Rust; industrial IT-G1; infrastructure C10C-002; Egypt C10C-001; India C10C-003; Morocco C10C-004; KGFS/C09 | MT-4 domain-transfer test | Heterogeneity of examples is not equivalent to formal transversal validity. C10C-004 supports translation/reconstruction but not TGCV `T_acc`. | PARTIALLY SUPPORTED |
| M-13 | Boundary preservation | Explicitly record when a domain supports state/change/outcome reconstruction but does not identify TGCV accessibility. | C10C-001; C10C-003; C10C-004 | Boundary gate | Negative/boundary evidence must not be converted into positive accessibility evidence. | SUPPORTED |
| M-14 | Causal-link discipline | Treat each causal link as a separate empirical question rather than infer a complete chain from adjacent associations. | C09; C10C-002; cross-domain map | Causal estimand gate | C10C-002 tests `Z → ΔT_acc*`, not `ΔT_acc* → trajectory`; C09 tests the latter boundedly; neither closes Value. | SUPPORTED, bounded |

## 3. Methodological sequence emerging from the matrix

The current evidence supports the following candidate sequence:

`S_t → Uτ → Pτ(S,C,L) → T_acc,t → ΔT_acc → realization/execution → subsequent state/trajectory → Outcome → Value`

The arrows are **procedural dependencies for analysis**, not assertions that every arrow has already been causally validated.

In particular:

1. `S_t` is identified before accessibility.
2. `Uτ` is explicitly bounded before admissibility is evaluated.
3. `Pτ` is specified independently of downstream outcomes.
4. `T_acc` is derived from `Uτ` and `Pτ`.
5. `ΔT_acc` is reconstructed before inspecting downstream consequences as explanatory evidence.
6. Realization/execution is recorded separately.
7. Subsequent trajectory is temporally separated from the transformation-space change.
8. Outcome is defined separately.
9. Value is introduced last and cannot redefine preceding layers.

## 4. What the matrix currently supports

### Strongest methodological result
The accumulated evidence supports a **transversal analytical translation-and-audit pattern**: heterogeneous empirical material can be inspected through ordered layers while explicitly preserving distinctions among state, candidate transformations, admissibility/accessibility, realization, trajectory, outcome and value.

### What remains incomplete
The matrix does not yet demonstrate:

- a fully closed methodology applicable to arbitrary domains;
- formal transversal validity;
- universal identifiability of `Uτ` or `Pτ`;
- a general causal law for `ΔT_acc → trajectory`;
- a causal or predictive `ΔT_acc → Value` relation;
- explanatory superiority over alternative representations.

## 5. Critical controls revealed by the matrix

Three controls are now central:

**Control A — semantic non-substitution:** observed structural change, treatment, adoption, take-up, realized configuration and conventional outcome must not be renamed accessibility without an independently defined predicate.

**Control B — temporal non-leakage:** later states, realized configurations, outcomes or value endpoints must not be used to define earlier accessibility.

**Control C — causal-link isolation:** evidence for one link in the chain must not be propagated as evidence for a different downstream link.

These controls are supported by both positive operational cases and negative/boundary cases.

## 6. Methodological maturity assessment

| Layer | Current assessment |
|---|---|
| Ontological layer | Stable at programme level; no change proposed |
| Translation layer | Strong candidate; repeatedly instantiated |
| Operationalization layer | Substantial bounded evidence; not universally closed |
| Audit layer | Relatively mature; non-circularity and boundary controls repeatedly demonstrated |
| Causal-validation layer | Partial; C09 closes one bounded causal link, not the chain |
| Domain-transfer layer | Promising but not formally closed |
| Value layer | Open downstream empirical target |

## 7. Decision

**Current disposition: RETAIN AS CANDIDATE ANALYTICAL METHODOLOGY.**

The matrix is sufficiently structured to guide the next scientific analysis, but insufficiently validated to become a normative TGCV methodology or to justify a C16 claim-level upgrade.

The next informative test is therefore not another generic reconstruction. It is a **methodological transfer test (MT-4)** in which the candidate sequence is applied prospectively to a new heterogeneous case with frozen pre-outcome information, independently defined `Uτ`/`Pτ`, explicit temporal ordering, and an auditable downstream outcome/value layer.

Until such a test is completed, this artifact must remain separate from normative governance artifacts.

## 8. Governance non-upgrade

No change is proposed to:

- TGCV Core;
- RMA v3.35;
- Evidence-to-Claim Matrix v1.11;
- C09 status;
- C10 status;
- C11 status;
- C12 status;
- C16 status;
- the open `ΔT_acc → Value` layer.

This artifact is an analytical consolidation only.