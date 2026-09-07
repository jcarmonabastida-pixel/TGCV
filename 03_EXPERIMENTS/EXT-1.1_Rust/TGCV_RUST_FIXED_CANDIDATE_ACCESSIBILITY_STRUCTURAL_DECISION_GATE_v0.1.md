# TGCV — Rust Fixed-Candidate Accessibility Structural Decision Gate v0.1

**Status:** PASS — BOUNDED STRUCTURAL ADEQUACY ESTABLISHED; COVERAGE LIMITATION FROZEN; FULL T_acc/ΔT_acc AUDIT AUTHORIZED SUBJECT TO FINAL PROTOCOL

## 1. Purpose

This gate evaluates the successful Fixed-Candidate Declaration-Driven Accessibility Shadow Audit v0.1 and decides whether its construction is adequate as a bounded structural realization of the Rust accessibility predicate `P_τ` for subsequent reconstruction of `T_acc,t` and `ΔT_acc`.

This gate is outcome-blind. It does not authorize outcome modelling, value analysis, predictive testing, or causal inference.

## 2. Locked starting architecture

The gate starts from the previously frozen TGCV architecture:

- `Core_ontological = S`
- `T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`
- `ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`
- `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`
- `I` remains an explanatory mechanism and is not a Core primitive.

Rust uses a fixed candidate identity and declaration-driven present accessibility. This is an operational instantiation, not a universal TGCV representation.

## 3. Evidence reviewed

The successful shadow execution reported:

- 607,498 focal package versions;
- 91,437 packages;
- 3,618,523 dependency rows;
- 516,061 successive focal-version pairs;
- 0 malformed rows;
- 0 duplicate dependency keys;
- 752,721 focal-target pairs with declaration variation;
- 60,914 removal-only declaration changes;
- 121,060 addition-only declaration changes;
- 570,747 declaration changes involving replacement/modification;
- 39,238,220 fixed candidates tested;
- 1,266,151 unsupported target-version exclusions under frozen R* v0.2;
- 1,475,648 `1 → 0` accessibility changes;
- 827,361 `0 → 1` accessibility changes;
- 2,303,009 total fixed-candidate accessibility changes.

The canonical report SHA was:

`622e6e20f4ad8147e0b8fbe13bf4f8fddefe8e82743255e5bd18996c4fb9d32a`

## 4. Decision on fixed-candidate structural adequacy

### 4.1 Candidate identity

**PASS.** Candidate identity is independent of the declaration being evaluated. The declaration therefore does not redefine the transformation itself.

The operational identity remains:

`τ_id = (origin_version_id, target_package_id, target_version_id)`

### 4.2 Fixed candidate universe

**PASS — bounded.** The shadow audit evaluates target-version candidates independently of the focal declaration and excludes target releases that do not yet exist at the initial comparison time. Therefore the observed accessibility switch cannot be attributed to the target version becoming available between the paired observations.

The shadow audit establishes the intended firewall against the monotonicity defect of the earlier construction.

### 4.3 Declaration-driven accessibility

**PASS.** Observed declaration changes generate both accessibility directions for fixed candidates:

`P_τ(t0)=1, P_τ(t1)=0`

and

`P_τ(t0)=0, P_τ(t1)=1`.

This is sufficient to reject the restricted claim that fixed candidate identity necessarily implies invariant accessibility in this Rust instantiation.

### 4.4 Accessibility versus execution

**PASS.** The shadow audit does not inspect execution, resolution outcome, subsequent activity, or later focal outcomes. The tested relation is therefore structurally prior to execution.

### 4.5 Outcome/value separation

**PASS.** No outcome, model, value, future activity, or predictive feature was used.

## 5. R* v0.2 coverage limitation

**FROZEN LIMITATION — NO SILENT RECODING.**

The shadow execution excluded 1,266,151 target-version evaluations because the target version string was outside the frozen R* v0.2 version grammar. R* v0.2 accepts only the explicitly frozen restricted syntax and raises `UNSUPPORTED_VERSION` otherwise.

This limitation has two distinct meanings that must not be conflated:

1. those target versions are unsupported by the present analytical grammar;
2. that does **not** establish that those versions were semantically inaccessible in historical Rust dependency resolution.

Accordingly:

- R* v0.2 remains frozen;
- unsupported cases remain explicitly excluded/unresolved for this analytical construction;
- no coercion is permitted;
- no coverage claim may silently treat unsupported cases as inaccessible;
- changing the grammar requires a separate ex-ante grammar gate.

## 6. What this gate establishes

The gate establishes the following bounded proposition:

> In the Rust dataset, under the frozen R* v0.2 grammar and the fixed-candidate declaration-driven construction, accessibility can change in both directions for transformation candidates whose identity remains fixed, independently of target-release availability and without using execution, outcome, value, or future activity.

This is a structural property of the operationalization and is valid evidence for continued testing of the `P_τ` / `ΔT_acc` construction.

## 7. What this gate does not establish

It does not establish:

- that the restricted R* v0.2 grammar is a complete historical model of Rust dependency semantics;
- universal Rust coverage;
- universal TGCV validity;
- that every declaration-driven accessibility switch should be interpreted as a complete transformation-space change without further aggregation/identity rules;
- empirical causal effects on Reach, Trajectory, Outcome or Value;
- predictive superiority;
- value creation;
- universal novelty or ontological irreducibility.

## 8. Structural conditions for the next full audit

The next full structural audit must preserve all of the following:

1. fixed candidate identity;
2. candidate universe independent of declaration membership;
3. target-version availability not used as the temporal change driver;
4. present-state declaration evaluation at each time;
5. frozen R* v0.2;
6. explicit unsupported/unresolved categories;
7. membership-level `T_acc` representation;
8. explicit empty sets;
9. deterministic canonicalization;
10. temporal pairing fixed independently of any outcome;
11. no execution information;
12. no outcome/value information;
13. no model features or predictions;
14. complete provenance and reproducibility;
15. explicit `Add`, `Rem`, persistence, expansion, contraction and reconfiguration classification.

## 9. Full-audit authorization boundary

**AUTHORIZED:** a new outcome-blind full structural audit reconstructing:

`U_τ → P_τ(t0), P_τ(t1) → T_acc,t0, T_acc,t1 → ΔT_acc`

using the frozen fixed-candidate/declaration-driven semantics.

**NOT AUTHORIZED:** any outcome, predictive model, value variable, causal estimate, or confirmatory hypothesis until the full structural audit has been separately reviewed and accepted.

## 10. Gate criteria

| Criterion | Decision |
|---|---|
| FA-G1 fixed transformation identity | PASS |
| FA-G2 declaration independent of candidate identity | PASS |
| FA-G3 fixed candidate universe | PASS — bounded shadow evidence |
| FA-G4 target availability isolated as change driver | PASS |
| FA-G5 declaration-driven accessibility switch | PASS |
| FA-G6 both `1→0` and `0→1` directions | PASS |
| FA-G7 accessibility/execution separation | PASS |
| FA-G8 outcome/value leakage exclusion | PASS |
| FA-G9 R* v0.2 unchanged | PASS |
| FA-G10 unsupported coverage explicitly represented | PASS |
| FA-G11 complete T_acc reconstruction | NOT YET — next audit |
| FA-G12 complete ΔT_acc reconstruction | NOT YET — next audit |
| FA-G13 semantic completeness of R* v0.2 | NOT ESTABLISHED |
| FA-G14 causal/predictive validity | OUT OF SCOPE |
| FA-G15 universal validity/novelty | NOT CLAIMED |

## 11. Gate decision

**PASS — BOUNDED STRUCTURAL ADEQUACY ESTABLISHED; FULL T_acc/ΔT_acc AUDIT AUTHORIZED SUBJECT TO FINAL PROTOCOL.**

The shadow audit has demonstrated the essential structural behavior needed to proceed: fixed transformation identity does not force fixed accessibility, and the change can be driven by observed changes in the focal system's dependency declarations rather than by target-release availability.

The next scientific task is therefore no longer to determine whether such accessibility switching is structurally possible. It is to construct and audit the complete temporal `T_acc` membership relation and its `ΔT_acc` classification under the same frozen semantics.

## 12. Integrity lock

- Core remains `S`.
- `T_acc` remains a derived analytical object.
- `ΔT_acc` remains the primary differentiated candidate.
- `I` remains explanatory.
- SLR-1 remains closed.
- TR-130–TR-140 remain closed.
- EXT-1.1 predictive results remain excluded.
- R* v0.2 remains frozen.
- No outcome/model/value execution is authorized yet.
- No post-hoc semantic redesign is authorized.

## 13. Next controlled operation

**TGCV Rust Full Temporal T_acc / ΔT_acc Structural Audit Protocol & Implementation Gate v0.1**

This next gate must specify the complete aggregation of fixed-candidate accessibility into `T_acc,t`, the temporal comparison operator, unresolved/unsupported handling, deterministic canonicalization, and the final structural audit before any outcome/model layer is introduced.
