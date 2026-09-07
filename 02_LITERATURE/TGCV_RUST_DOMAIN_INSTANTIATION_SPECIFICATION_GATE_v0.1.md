# TGCV — Rust Domain Instantiation Specification Gate v0.1

**Status:** RECONSTRUCTED / WORKING  
**Date:** 2026-09-07  
**Phase:** Domain instantiation and empirical validation preparation

## 1. Purpose

Specify, ex ante and independently of any new outcome or predictive model, how the frozen TGCV representation contract will be instantiated in the Rust software ecosystem.

This Gate does not authorize confirmatory model fitting. It freezes the domain-level semantics required for a subsequent structural audit.

## 2. Locked methodological architecture

`Core_ontological = S`

`T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`

`ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

`I` remains explanatory rather than primitive.

The following remain closed: SLR-1; TR-130–TR-140; the general Operational Representation Specification Gate; and the Domain Instantiation Selection Gate.

EXT-1.1 is treated as a prior empirical precedent only.

## 3. Domain unit

### RUST-1 — Unit of analysis

The primary unit is a **package version at a defined observation time**:

`e = package@version`.

The unit identity is determined by package and version identifiers and their canonical publication timestamp. A package version is not identified by its later dependency behaviour or outcome.

## 4. System representation

### RUST-2 — `S_Rust`

For the instantiation, `S_Rust,t` is the package-version system state represented by the package's observable ecosystem metadata at time `t`, including only fields frozen by the later data dictionary.

The system representation must not include downstream outcome variables or future information.

### RUST-3 — Context `C_Rust`

`C_Rust,t` contains present conditions relevant to transformation accessibility, such as registry/ecosystem constraints and dependency/environment information available at `t`.

Context variables must be frozen before confirmatory analysis and cannot be selected using the eventual outcome.

### RUST-4 — Analytical level `L_Rust`

`L_Rust` is fixed at the **package-version dependency ecosystem level**. It is not permitted to vary between observations to improve discrimination of `T_acc`.

## 5. Transformation identity

### RUST-5 — `τ`

A candidate transformation must describe an independently identifiable change that can be applied to the focal package-version system under the frozen analytical level.

The first candidate class for audit is:

`τ = dependency-transition(origin_package_version, target_package, target_version)`.

A candidate transformation is identified by the tuple:

`τ_id = (origin_version_id, target_package_id, target_version_id)`.

This identity is constructed independently of accessibility and outcome.

Importantly, this specification does **not** inherit the EXT-1.1 interpretation that every observed dependency relation is necessarily the definitive TGCV transformation object. The structural audit must establish whether this candidate class is adequate for the new instantiation.

## 6. Candidate universe `U_τ`

### RUST-6 — Independent construction

`U_τ` must be constructed from observed Rust ecosystem records and a frozen temporal rule, before accessibility is evaluated.

Minimum structural requirements:

1. candidate identity is unique;
2. origin and target identifiers resolve to canonical entities;
3. target information satisfies the ex-ante temporal boundary;
4. construction does not use `P_τ`, execution, outcome or value;
5. candidate generation is deterministic and row-order invariant.

The existing EXT-1.1 DR-020 audit provides evidence that this type of independent candidate-universe construction is technically feasible at scale, but it does not automatically validate the new TGCV semantics. fileciteturn221file0L2-L10

## 7. Accessibility predicate `P_τ`

### RUST-7 — Non-circular accessibility

For each candidate `τ`:

`P_τ(S_Rust,t,C_Rust,t,L_Rust) ∈ {0,1}`.

For the initial Rust instantiation, accessibility means that the target dependency transition is **permitted by the frozen dependency-resolution semantics at the origin observation time**, using only information available at that time.

The predicate must be evaluated without:

- executing the dependency transition;
- observing whether the target package is subsequently selected in reality;
- observing later package releases;
- using subsequent activity as a proxy for present accessibility;
- using any downstream outcome or value measure.

The exact dependency-resolution semantics, including version-range grammar and precedence, must be frozen in the subsequent structural protocol rather than inferred from the eventual results.

## 8. `T_acc` representation

### RUST-8 — Primary representation

The primary representation is the **membership relation**:

`T_acc,t = {(e,τ) | e=package@version and P_τ(e,t)=1}`.

For each focal package-version, the accessible transformations are the set of `τ_id` satisfying the predicate.

Derived summaries such as:

`|T_acc,t|`

may be retained, but are secondary and cannot replace membership information when membership-level comparison is required.

This deliberately differs from adopting `TAcc_repr=(A_rel,A_count)` as a universal representation. That representation remains specific to EXT-1.1.

## 9. `ΔT_acc` representation

### RUST-9 — Frozen comparison

For an origin observed at `t` and the corresponding next observation point `t+1`:

`ΔT_acc = T_acc,t+1 ≄ T_acc,t`.

The structural record must preserve set membership sufficiently to classify:

- **expansion:** `T_acc,t+1 \ T_acc,t ≠ ∅`;
- **contraction:** `T_acc,t \ T_acc,t+1 ≠ ∅`;
- **persistence:** membership equal;
- **reconfiguration/substitution:** both additions and removals occur.

The exact observation pairing and temporal window must be frozen before examining outcome data.

## 10. Empty and unresolved cases

### RUST-10

A package-version with:

`T_acc,t = ∅`

is a valid observation and must not be discarded merely because it has no accessible transformation.

An unresolved candidate relation must be represented as unresolved/missing and must not be silently converted into `P_τ=0`.

Coverage must be reported at both candidate and focal-unit levels.

## 11. Execution separation

The Rust instantiation must preserve:

`τ exists → P_τ=1 → selection/execution may occur or not → result occurs or not`.

Observed dependency usage after the origin time is therefore not the definition of accessibility.

The empirical audit must explicitly identify cases where a transformation is accessible but unexecuted whenever the available data permit this distinction.

## 12. Reach and trajectory

`Reach_Rust,t` must describe the futures/configurations reachable under admissible sequences of accessible transformations.

`Trajectory_Rust` must describe the temporal structure of such sequences.

Neither may be substituted for `T_acc` merely because the native Rust data make one easier to compute.

## 13. Reuse of EXT-1.1 infrastructure

Permitted reuse:

- generic parsing/indexing infrastructure;
- frozen dataset integrity checks where applicable;
- deterministic serialization utilities;
- generic audit machinery.

Not permitted by inheritance:

- the old outcome;
- the old model;
- the old feature encoding as a canonical TGCV representation;
- the old temporal window;
- the old hypothesis;
- the old predictive interpretation;
- any post-hoc choice motivated by the EXT-1.1 negative result.

Every reused component must be documented as **infrastructure reuse** or **semantic inheritance**, with semantic inheritance requiring an explicit justification.

## 14. Required structural audit before any outcome/model

The next audit must verify:

1. `unit_id` uniqueness;
2. transformation identity uniqueness;
3. independent `U_τ` construction;
4. temporal validity;
5. frozen dependency-resolution semantics;
6. non-circular `P_τ`;
7. `T_acc` membership reconstruction;
8. empty-set validity;
9. unresolved-case integrity;
10. temporal reconstruction of `T_acc,t` and `T_acc,t+1`;
11. exact `ΔT_acc` classification;
12. accessibility/execution separation;
13. outcome/value exclusion;
14. deterministic reproducibility;
15. provenance completeness.

Failure of any critical item blocks confirmatory outcome/model specification.

## 15. Falsifiers

**RF-1:** candidate transformation identity cannot be independently defined.

**RF-2:** `U_τ` depends on accessibility or future information.

**RF-3:** dependency-resolution semantics cannot be frozen without outcome information.

**RF-4:** `P_τ` is circular or requires execution.

**RF-5:** `T_acc` cannot be reconstructed at membership level.

**RF-6:** `ΔT_acc` cannot be reconstructed consistently across time.

**RF-7:** unresolved relations cannot be separated from inaccessible relations.

**RF-8:** the proposed representation collapses to the old EXT-1.1 proxy without substantive justification.

**RF-9:** the Rust data cannot preserve accessibility/execution/outcome separation.

**RF-10:** reproducibility or provenance fails.

## 16. Gate criteria

| Criterion | Result |
|---|---|
| RI-G1 | Rust domain unit specified — PASS |
| RI-G2 | `S_Rust`, `C_Rust`, `L_Rust` specified — PASS |
| RI-G3 | Independent transformation identity specified — PASS |
| RI-G4 | Independent `U_τ` contract specified — PASS |
| RI-G5 | Non-circular `P_τ` contract specified — PASS |
| RI-G6 | Membership-level `T_acc` specified — PASS |
| RI-G7 | `ΔT_acc` semantics specified — PASS |
| RI-G8 | Empty/unresolved treatment specified — PASS |
| RI-G9 | Execution/outcome/value separation specified — PASS |
| RI-G10 | Reach/Trajectory distinction preserved — PASS |
| RI-G11 | EXT-1.1 inheritance safeguards specified — PASS |
| RI-G12 | Pre-confirmatory structural audit specified — PASS |
| RI-G13 | Structural audit executed — NOT YET |
| RI-G14 | Outcome/model protocol selected — NOT YET / OUT OF SCOPE |

## 17. Gate decision

**PASS — RUST DOMAIN INSTANTIATION CONTRACT SPECIFIED; STRUCTURAL VALIDATION REMAINS OPEN.**

This Gate establishes the Rust-level semantic contract required for the next structural audit. It does not establish that the proposed Rust transformation class is empirically identifiable, complete, or superior to the native dependency representation. Those questions remain falsifiable in the next audit.

## 18. Immediate next controlled operation

**TGCV Rust Instantiation Structural Audit v0.1**.

The audit must be performed before selecting any new outcome or predictive model. Its purpose is to determine whether the specified Rust instantiation actually satisfies the frozen representation contract on the available data.

## 19. Integrity lock

No outcome, model, feature set, temporal window or value hypothesis may be selected using results from the future structural audit. The structural audit itself must remain outcome-blind.
