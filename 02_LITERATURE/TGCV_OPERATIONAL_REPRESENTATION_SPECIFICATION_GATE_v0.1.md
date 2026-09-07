# TGCV — Operational Representation Specification Gate v0.1

**Status:** RECONSTRUCTED / WORKING  
**Date:** 2026-09-07  
**Phase:** Architecture development and operationalization  

## 1. Purpose

Freeze the methodological specification that any future empirical instantiation must satisfy before selecting a domain-specific representation of `T_acc` and `ΔT_acc`.

This Gate does **not** select a new dataset, outcome, model, or confirmatory experiment. It defines the representation contract that those later protocols must satisfy.

## 2. Locked architectural starting point

The representation contract inherits the current stabilized architecture:

`Core_ontological = S`

`T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`

`ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`

`mechanism → (S_t,C_t) → T_acc,t → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

`I` remains an explanatory mechanism, not a Core primitive.

SLR-1 and TR-130–TR-140 remain closed. EXT-1.1 remains a separate empirical precedent and does not determine this methodological specification.

## 3. Representation contract

### OR-1 — Unit of analysis

Every instantiation must identify an explicit analytical unit `e` and its temporal identity. The unit must be stable enough to compare its accessible transformation space across the observation window.

### OR-2 — Transformation identity

Each candidate transformation `τ` must have an independently specified identity:

`τ = transformation(source_state, target_state, operation, or equivalent domain-defined transition specification)`.

The exact encoding is domain-specific, but identity must be defined independently of accessibility and outcome.

### OR-3 — Candidate universe

Construct an independently defined candidate universe `U_τ` before determining accessibility.

`U_τ` may be complete or explicitly bounded. Any bounded universe must document its coverage rule and exclusions.

### OR-4 — Accessibility predicate

Define:

`P_τ(S_t,C_t,L) ∈ {0,1}`.

The predicate must be computable or reconstructable from present information and must not require:

- future observations;
- execution of `τ`;
- success of `τ`;
- downstream outcome;
- value evaluation.

### OR-5 — Accessible transformation representation

Construct:

`T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`.

The preferred representation is relational/set-based where the domain permits it. A cardinality or other summary statistic may be derived, but cannot replace the underlying representation when membership information is scientifically required.

### OR-6 — Empty and unresolved cases

Empty accessible sets must be valid observations. Unresolved candidate relations must be explicitly represented as unresolved/missing rather than silently classified as inaccessible or accessible.

### OR-7 — Temporal representation

For successive observation points `t` and `t+1`, retain sufficient information to reconstruct both `T_acc,t` and `T_acc,t+1` under the same frozen representation rules.

### OR-8 — Change operator

The comparison operator must be frozen before confirmatory analysis. At minimum it must distinguish:

- expansion: `T_acc,t+1 \ T_acc,t ≠ ∅`;
- contraction: `T_acc,t \ T_acc,t+1 ≠ ∅`;
- persistence: equal membership;
- reconfiguration/substitution: membership changes without simple monotonic expansion/contraction.

The exact operational encoding may be domain-specific, but the semantics cannot change after observing results.

## 4. Required separation from execution

The representation must support the sequence:

`τ exists → τ is accessible → τ may or may not be selected → τ may or may not execute → execution produces an outcome → outcome is evaluated`.

An executed transformation is not automatically the complete set of accessible transformations.

Likewise, a successful transformation cannot be used retrospectively as evidence that it was accessible unless accessibility was independently defined.

## 5. Required separation from Reach and Trajectory

The representation must preserve:

- `T_acc`: what transformations are accessible now;
- `Reach`: what futures/states/configurations can be reached through admissible sequences;
- `Trajectory`: which temporal/path structures are admissible.

A representation that collapses these into a single object must be rejected or explicitly justified as a domain-specific loss of information.

## 6. Representation levels

Each empirical study must explicitly classify the representation as:

**R0 — Direct:** accessible transformations are directly reconstructable as members of `T_acc`.

**R1 — Reconstructed:** membership is deterministically reconstructed from observable/specifiable domain data.

**R2 — Partial:** only a justified subset of `T_acc` is observable/reconstructable, with explicit coverage limitations.

**R3 — Proxy:** a native variable is used as an approximation to `T_acc`; it cannot be treated as direct evidence for transformation-level accessibility without additional validation.

R3 is insufficient for a primary confirmatory test of the TGCV representation unless a separate Gate establishes proxy validity.

## 7. Domain translation requirements

For domain `D`, document:

`S_D, C_D, L_D, U_τ,D, P_τ,D, T_acc,D, ΔT_acc,D, Reach_D, Trajectory_D, Outcome_D, Value_D`.

For every mapping, record:

1. native domain meaning;
2. TGCV role;
3. direct/partial/proxy status;
4. information lost;
5. assumptions introduced;
6. independent observability;
7. temporal availability;
8. provenance.

No TGCV variable may be inserted into the domain merely because it makes the mapping work.

## 8. Minimal data dictionary

| Field | Required definition |
|---|---|
| unit_id | stable analytical identity |
| time | observation time / ordering rule |
| S | system representation |
| C | present conditions/context |
| L | frozen analytical level |
| tau_id | independent transformation identity |
| U_tau_membership | candidate-universe membership |
| P_tau | accessibility determination |
| T_acc_membership | accessible-set membership |
| delta_T_acc | fixed comparison result |
| Reach | reachable-future representation |
| Trajectory | admissible path representation |
| execution | post-access selection/execution record |
| Outcome | realized consequence |
| Value | downstream evaluation |
| provenance | source and reconstruction trace |

## 9. Integrity requirements

A representation specification is valid only if it provides:

- deterministic or explicitly stochastic rules fixed ex ante;
- reproducible serialization where machine representation is used;
- canonical ordering where set equality is serialized;
- versioned definitions of all predicates;
- provenance from observations to derived membership;
- explicit treatment of missing and unresolved data;
- temporal consistency;
- no outcome leakage;
- no post-hoc feature creation.

## 10. Mandatory pre-confirmatory audit

Before any confirmatory model fit or hypothesis test, the operational representation must pass an audit covering:

1. candidate-universe independence;
2. accessibility non-circularity;
3. temporal validity;
4. empty-set validity;
5. unresolved-case handling;
6. deterministic/reproducible construction;
7. `T_acc` membership integrity;
8. `ΔT_acc` comparison integrity;
9. separation from execution;
10. separation from outcome/value;
11. separation from Reach/Trajectory;
12. provenance completeness.

A failed structural audit blocks confirmatory execution.

## 11. Falsifiers

**OR-F1 — Candidate dependence:** `U_τ` can only be constructed after observing accessibility or outcome.

**OR-F2 — Circular predicate:** `P_τ` depends on execution, success, outcome or value.

**OR-F3 — Temporal insufficiency:** `T_acc,t` and `T_acc,t+1` cannot be reconstructed under identical rules.

**OR-F4 — Proxy collapse:** the proposed representation is merely an existing native variable and loses transformation membership information essential to the claim.

**OR-F5 — Change collapse:** `ΔT_acc` cannot be distinguished from changes in the chosen state/native representation under the domain's correct semantics.

**OR-F6 — Downstream collapse:** Reach or Trajectory cannot be independently represented from `T_acc`.

**OR-F7 — Outcome leakage:** downstream information enters present accessibility.

**OR-F8 — Coverage failure:** the observed representation is too incomplete to support the intended claim and no bounded interpretation is possible.

## 12. Gate criteria

| Criterion | Result |
|---|---|
| OR-G1 | Unit of analysis specified — PASS |
| OR-G2 | Transformation identity independently defined — PASS |
| OR-G3 | Independent candidate universe required — PASS |
| OR-G4 | Non-circular accessibility predicate required — PASS |
| OR-G5 | `T_acc` representation contract specified — PASS |
| OR-G6 | Empty/unresolved cases explicitly handled — PASS |
| OR-G7 | Temporal reconstruction contract specified — PASS |
| OR-G8 | `ΔT_acc` operator contract specified — PASS |
| OR-G9 | Execution/outcome/value separation preserved — PASS |
| OR-G10 | Reach/Trajectory distinction preserved — PASS |
| OR-G11 | Cross-domain translation contract specified — PASS |
| OR-G12 | Pre-confirmatory audit specified — PASS |
| OR-G13 | Specific empirical instantiation selected — NOT YET / OUT OF SCOPE |
| OR-G14 | Confirmatory validation completed — NOT YET |

## 13. Gate decision

**PASS — REPRESENTATION CONTRACT SPECIFIED FOR DOMAIN-SPECIFIC OPERATIONALIZATION.**

The TGCV architecture now has a frozen methodological contract for constructing and auditing `T_acc` and `ΔT_acc` before any new confirmatory empirical study.

This Gate establishes representational readiness only. It does not establish empirical validity, causal efficacy, predictive superiority, universal applicability or universal originality.

## 14. Immediate next controlled operation

The next operation is the **TGCV Domain Instantiation Selection Gate**.

That Gate must select one concrete domain and determine whether its native data permit a valid R0/R1/R2 representation of `T_acc` and `ΔT_acc`. The selection must be made before specifying a confirmatory outcome/model protocol.

EXT-1.1 Rust may be considered as a candidate domain only through a fresh domain-instantiation decision; its previous representation remains specific to its frozen experimental protocol.

## 15. Integrity lock

No future empirical study may silently alter the definitions of:

`S`, `C`, `L`, `U_τ`, `P_τ`, `T_acc`, `ΔT_acc`, `Reach`, `Trajectory`, `Outcome`, or `Value`.

Any substantive alteration requires a new versioned ex-ante Gate.
