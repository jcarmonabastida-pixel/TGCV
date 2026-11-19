# DEC-C10-094 — AB integrated material design resolutions

**Date:** 2026-11-09  
**Status:** ACCEPTED WORKING DESIGN RESOLUTIONS — NOT DESIGN FREEZE  
**Scope:** C10-S package AB-01…AB-09  
**Branch:** research/c10-s-consolidation-draft

## 1. Decision

Following the integrated proposal in master §219 and explicit user acceptance, the following material design resolutions are accepted as the working specification for AB. They specialize DEC-C10-093 without reopening its accepted conceptual baseline.

### 1.1 Instance, inventory and representation

1. Retain the DEC-C10-069 contract, instance and CMP anchor without modification.
2. Retain the constitutive logical inventory: one CMP, PAR-SVC-ENABLED and PAR-SVC-PROFILE, one REQUIRE rule, and two semantically mandatory typed operand bindings. POL remains outside the minimal confirmatory nucleus; MET remains mandatory.
3. The two operand bindings must be represented exactly once. The physical encoding must be either two typed REF objects or two typed AST links, as dictated by the canonical grammar. REF and AST must not duplicate the same relation. The semantic decision is accepted; physical encoding, canonical serialization and byte-level canonicalization remain OPEN pending verification against the governing grammar.
4. Retain the synthetic source/destination/mapping namespaces and the total, injective PROFILE mapping STD→STANDARD, RO→READ_ONLY, OFF→DISABLED. ENABLED remains BOOL without coercion. Undefined conversions fail explicitly; no silent defaults or collapse of ABSENT/NULL/DEFAULT/VALUE.
5. IAM is an applicability matrix indexed by role, action, object, stage, route and snapshot. Applicability classes are REQUIRED, CONDITIONAL and NOT_APPLICABLE; UNKNOWN is evidence status, not a design class. NOT_APPLICABLE must be justified ex ante. Coverage is unknown unless its applicable denominator is closed.
6. Keep functional authorization, technical credentials/ACLs and agent knowledge as separate constructs. API acceptance or agent knowledge does not establish AUTH_f*.

### 1.2 Routes, functional criterion and temporal frame

7. Retain F1→F2 as focal route and A1→A2 as alternative route, evaluated against the same destination contract, roster, mapping, IAM, C0/G/H and common non-compensatory F*.
8. Retain A_f* as the conjunction of its specified necessary predicates and three-valued propagation 1/0/?. DEP_f* remains focal-route dependency and cannot be used to rule out the alternative route.
9. FP-05 is specialized as no secrets in artifacts/snapshots, no silent privilege expansion over pre-Z baseline, least privilege and no relaxation of security controls. Any elevation, exposure or relaxation is a non-compensable failure. Required permissions must be declared in C0/IAM before assignment; a new requirement is treated as a potential direct/collateral path, not silently introduced by B.
10. FP-08 remains a separate evidentiary gate and does not alter F*.
11. G is the complete logical service unit and its constitutive roster. Host/runtime/resource boundaries are recorded in C0 and the surface map, not added to the constitutive roster merely for convenience.
12. C0 is the immutable baseline snapshot before Z and before any B programming. It includes configuration/versions, runtime and host, functional and technical permissions, resources, baseline F/A states and known background routes, unit/cluster, clock/window, M/IAM/oracle versions and eligibility. Post-Z variables cannot redefine C0.
13. H is common to F and A, uses one pre-specified common temporal anchor, and cannot stop selectively at route-specific success. The anchor may be Z or another protocol-defined common start fixed before Z. H* must receive an explicit value and unit before DGP freeze; neither is inferred here. Post-H events are recorded as carryover/residual.

### 1.3 D2, joint technical mechanism and collateral paths

14. D2 remains the primary candidate policy; D1 remains secondary. Record separately assignment, programming, receipt, compliance, attempt, actor, artifact/version, timing, installation, retries, partial failure, rollback, background provision, crossover and deviations.
15. Z=1 does not imply receipt, attempt or installation; Z=0 does not imply absence of background provision. Control is defined by absence of focal programming/attempt under the policy, with background access observed and classified.
16. C_dep* remains the conjunction of installation, integrity, compatibility and operability. Its DGP is represented by a conditional joint distribution (e.g. a 16-cell table per relevant stratum or a validated equivalent), not by an independence assumption or marginal probabilities alone. The distribution must be normalized and all probabilities bounded [0,1]. No numerical probabilities, s=.80 or historical .20/.80 rates are approved by this decision.
17. ARCH-B1 remains a candidate architecture, not a confirmed implementation. MD-C1 and MD-C4 require material manifests and evidence; until demonstrated, no exclusive focal-path intervention or A1/A2 non-affectation may be claimed. Unknown surfaces remain UNKNOWN, not invariant.

### 1.4 Population, truth and causal handoff

18. Eligibility is determined by a reproducible algorithm using C0 variables only, before Z and B programming. Post-assignment receipt, installation, F*, success or outcomes cannot determine eligibility or exclusions.
19. P*_τ2, P*_F and q_X* remain distinct. q_X* is fixed and versioned pre-Z. Standardization is restricted to documented common support and positivity; unsupported cells are not silently extrapolated.
20. Assignment unit, analysis unit and interference unit are distinct fields. Shared host, adapter, permissions, resources or state require cluster assignment or an explicit exposure/interference model. The actual cluster topology remains a material evidence/design input; no individual-level independence is assumed.
21. Reuse R0–R3 and existing EXC/PM/IV controls. Keep DGP truth, observed data, measurement status, coverage and adjudication references separate. Reach=0 requires exhaustive coverage of a closed universe; otherwise use ?. Generator, Analyzer and Evaluator remain separated; Analyzer cannot access truth, hidden assignment or scenario labels.
22. The independent oracle must be route- and outcome-independent, versioned before fixture generation, with documented adjudication and blinding where feasible. Independence, blinding and adjudication are evidence gates, not assumed satisfied.
23. Transfer to package C the population and q_X*, support, joint D2 distribution, unit/interference, timing, measurement and adversarial scenarios as inputs. ITT-Z-D2, package effect, LATE_f, θ_Af(q_X*) and θ_A(q) remain distinct estimands. This decision makes no identification, power, sample-size or Value claim.

## 2. Explicitly unresolved gates

The following remain OPEN and must not be filled with invented defaults: physical REF/AST encoding and canonical serialization; numerical value/unit of H* and final anchor choice; material MD-C1/MD-C4 manifests and evidence; numerical joint D2 probabilities and sensitivity; material eligibility roster/algorithm, q_X* and support; actual assignment/cluster/interference topology; oracle validation, blinding feasibility and adjudication evidence; any remaining instrument-level reconciliation of C0/G/IAM against source decisions.

These are bounded material gates, not grounds to reopen the accepted conceptual architecture. Their resolution must be coordinated across AB and the downstream C interface.

## 3. Status and authorization

AB has accepted working design resolutions for the documentary choices above. **AB is not DONE, not Design Frozen and not implementable.** No executable fixture, code, parser, validator, simulation or experiment is authorized. No scientific execution or execution authorization is granted.

`scientific_execution=false`; `execution_authorized=false`.

Work remains on the research branch. No change to `main` and no promotion of PR #116 is authorized.

## 4. Traceability

- Baseline acceptance: DEC-C10-093.
- Integrated proposal: C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md §219.
- Master propagation: §220.
- Closure plan propagation: §16.98.
- Closure control propagation: §116.
