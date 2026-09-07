# TGCV — D-OPS-1 Rust Domain Operational Specification v0.1

**Status:** PASS — DOMAIN SELECTED / OPERATIONAL SPECIFICATION FROZEN FOR DESIGN
**Date:** 2026-09-08
**Domain:** Rust package ecosystem
**Role:** First domain instantiation of the TGCV operational architecture
**Scope:** specification and ex-ante design only; no new execution authorized by this document

## 1. Decision

**Rust is selected as the first D-OPS-1 domain.**

Selection is based on identifiability, reproducibility, existing frozen structural data, explicit transformation semantics and prior executable infrastructure — not on expected empirical confirmation.

The selection does not imply that Rust is theoretically privileged or representative of all domains.

## 2. Selection rationale

Rust is currently the strongest candidate because the project already possesses:

- a frozen real structural snapshot (`rust_repos_2022_09_07.zip`);
- a deterministic restricted resolver `R* v0.2`;
- a canonical transformation representation used in TR-131;
- a frozen executor with an explicit information firewall;
- completed TR-131 primary execution, replay and scientific integration;
- a documented bounded empirical result showing that the tested B representation does not uniquely determine canonical T_acc membership.

These assets make the domain unusually identifiable without requiring retrospective redesign.

The existing executor explicitly excludes outcome, Reach, sampling, predictive metrics and post-origin analysis, which makes it suitable as a structural foundation rather than as a source of outcome leakage.

## 3. Unit of analysis

The primary observational unit is a **package-version origin** represented by:

`o = (version_id, package_id, version_str, created_at)`.

Each origin is evaluated against the dependency declarations attached to that package version.

The temporal unit is the package-version creation/order relation already encoded in the frozen snapshot. No future outcome window is required for accessibility classification.

## 4. System representation S

For D-OPS-1, the system representation at an origin is the package-version configuration relevant to its dependency transformation possibilities.

The operational representation used by the existing executor includes the package version identity and dependency declarations required to reconstruct candidate transformations. This representation is domain-specific and must not be promoted to TGCV ontology.

For cross-time comparison, the relevant system/context record is indexed to the origin's creation time.

## 5. Context C

The accessibility context contains only information legitimately available at the origin time and needed by the restricted resolution semantics, including:

- dependency requirement declared by the origin;
- target package version history available at or before the origin time;
- target version identity/version string;
- origin creation time;
- package-local release ordering used for prior-release count and age calculations where those variables are used in an auxiliary representation.

Future release activity, later downloads/adoption/popularity/success and outcome variables are excluded from accessibility.

## 6. Analytical level L

`L` is the frozen restricted dependency-resolution semantics `R* v0.2`.

It is deliberately **not** claimed to be the historical Cargo resolver. Unsupported requirement/version syntax fails closed by exclusion from the admissible candidate set.

The current implementation supports exact requirements and caret-compatible requirements under the frozen parser/resolver rules. Candidate versions must satisfy the requirement and must have `created_at <= origin_created_at`; the maximum eligible version under the frozen ordering is selected.

The exact implementation is the GitHub-frozen `rstar_v02.py` artifact.

## 7. Candidate transformation universe U_tau

For each dependency declaration of origin `o`, the candidate transformation universe consists of dependency-resolution transformations of the form:

`τ = (origin_version_id, target_package_id, target_version_id, target_version_str)`.

`U_tau(o)` is generated from structurally available target package versions in the frozen snapshot, subject to the declared candidate construction, but **before** applying accessibility membership.

The universe must not be generated from observed successful execution or later outcomes.

## 8. Canonical transformation identity

Transformation identity is the exact tuple:

`(origin_version_id, target_package_id, target_version_id, target_version_str)`.

Canonical ordering is lexicographic on the tuple components. Duplicate canonical transformations are an integrity failure and must fail closed.

The canonical representation is therefore reproducible and supports exact membership comparison.

## 9. Accessibility predicate P_tau

For a candidate transformation `τ`,

`P_tau(S,C,L) = 1`

iff all frozen admissibility conditions of `R* v0.2` are satisfied, including:

1. the dependency requirement is supported by the frozen requirement grammar;
2. the target version is structurally present;
3. target version identity is unique;
4. target version creation time is not later than the origin creation time;
5. the target version satisfies the frozen requirement semantics;
6. the candidate is selected by the frozen maximum-eligible-version rule where selection is part of the transformation definition.

Otherwise the candidate is excluded or the relevant edge is classified by the frozen exclusion rule; unsupported syntax does not become accessible merely because a later execution succeeded.

The predicate is pre-execution and contains no outcome, success, adoption or future activity variable.

## 10. Accessible transformation space

For each origin:

`T_acc(o) = {τ ∈ U_tau(o) | P_tau(S_o,C_o,L)=1}`.

The canonical set is the sorted set of unique transformation tuples under the fail-closed duplicate rule.

An origin may have an empty `T_acc`; this is valid structural evidence and is not treated as missing data.

## 11. ΔT_acc operationalization

For two comparable observations under the same analytical level and canonical identity rule:

`ΔT_acc ≠ 0` iff their canonical membership sets differ.

The comparison preserves membership identity rather than cardinality alone.

Allowed structural forms are:

- expansion;
- contraction;
- reconfiguration/substitution;
- equal cardinality with different membership.

The latter is especially important because cardinality equality does not imply transformational equivalence.

## 12. Reach and Trajectory — reserved downstream layer

D-OPS-1 does **not** infer Reach or Trajectory from the TR-131 structural result.

For a future downstream gate, Reach must be defined from explicit sequences of accessible transformations under frozen transition semantics, and Trajectory from ordered paths/continuations.

No execution/outcome data may be fed backward into `P_tau`.

## 13. Outcome and Value — reserved layers

Outcome and Value remain downstream and are outside the present structural D-OPS-1 freeze.

Any future outcome/value test requires a separate ex-ante specification defining:

- outcome horizon;
- outcome variable;
- value criterion;
- selection/execution semantics;
- confounder handling;
- information firewall;
- prospective evaluation protocol.

No positive-value implication is assumed.

## 14. Primary hypotheses for the Rust instantiation

### H-R1 — Non-trivial accessibility change

There exist comparable Rust package-version observations for which the canonical accessible transformation membership differs.

### H-R2 — State-reduction residual

For a declared observational representation B, there exist B-equivalent observations with different canonical T_acc membership.

This has already received bounded empirical support under TR-131 and DR-032; it is not a new claim here.

### H-R3 — Downstream structural link

Under a separately frozen transition semantics, some non-trivial `ΔT_acc` events correspond to differences in Reach and/or Trajectory.

This remains untested by D-OPS-1.

### H-R4 — Counterfactual preservation

`T_acc` records accessible-but-unexecuted alternatives that cannot be reconstructed from realized execution alone.

This remains a future test.

## 15. Information firewall

The structural accessibility layer MUST NOT read or derive from:

- later release activity;
- downloads, adoption, popularity or success;
- future outcome windows;
- predictive targets or metrics;
- Reach or Trajectory when classifying present accessibility;
- post-origin metadata not frozen as part of `C`;
- package identity as an extra B-equivalence feature beyond the frozen specification.

## 16. Reproducibility requirements

Any execution based on D-OPS-1 must record:

- dataset filename and integrity hash;
- exact executor commit/blob SHA;
- exact `R*` implementation SHA;
- runtime version;
- exact command;
- execution timestamp;
- complete stdout/stderr;
- canonicalization rule;
- all integrity/firewall flags;
- deterministic replay result.

No manual alteration of raw execution output is permitted.

## 17. Existing evidence boundary

The following are already established and are not to be re-proven by D-OPS-1:

- TR-131 primary integrity PASS;
- deterministic replay PASS;
- execution-result closure PASS;
- DR-032 scientific integration accepted;
- bounded empirical support for retaining explicit T_acc under the tested B representation.

D-OPS-1 does not reopen any of those records.

## 18. Falsifiers

The Rust operationalization must be rejected or redesigned if:

1. `U_tau` cannot be independently enumerated;
2. `P_tau` requires future outcome/execution information;
3. transformation identity is non-reproducible;
4. canonical membership depends on arbitrary ordering or hidden labels;
5. unsupported syntax is silently treated as accessible;
6. duplicate transformations are silently collapsed;
7. `T_acc` is merely a relabelled existing sufficient native variable with no residual analytical function;
8. downstream tests require retroactive modification of the frozen structural definitions.

## 19. D-OPS-1 gate criteria

| Criterion | Requirement | Result |
|---|---|---|
| DOPS-G1 | Domain identifiable | PASS |
| DOPS-G2 | Observation unit frozen | PASS |
| DOPS-G3 | S/C/L roles separable | PASS |
| DOPS-G4 | U_tau independently specified | PASS — bounded structural universe |
| DOPS-G5 | Canonical tau identity | PASS |
| DOPS-G6 | Non-circular P_tau | PASS |
| DOPS-G7 | T_acc reproducible | PASS — existing executor infrastructure |
| DOPS-G8 | ΔT_acc exact comparison | PASS |
| DOPS-G9 | Accessibility/execution separation | PASS |
| DOPS-G10 | Outcome/value separation | PASS |
| DOPS-G11 | Reach/Trajectory operationalized | NOT YET — separate downstream gate |
| DOPS-G12 | New empirical result produced | NO — not the purpose of this gate |

## 20. Decision

**D-OPS-1 = PASS — RUST DOMAIN SELECTED AND STRUCTURAL OPERATIONAL SPECIFICATION FROZEN.**

This authorizes construction of the next Rust-specific downstream gate. It does not itself authorize a new dataset execution.

## 21. Integrity consequence

- TGCV Core remains `S`.
- `T_acc` remains derived analytical object.
- `ΔT_acc` remains primary differentiated candidate.
- Existing TR-131 evidence remains frozen.
- No outcome/value information is admitted into accessibility.
- No retrospective redesign is authorized.

## 22. Next controlled operation

The next gate is **RUST-DYN-1 — Dynamic ΔT_acc / Reach-Trajectory Operational Gate**.

Its purpose is to freeze, before execution, the temporal comparison and downstream semantics needed to test H-R1/H-R3/H-R4 without outcome leakage.
