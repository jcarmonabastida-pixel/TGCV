# TGCV — Rust Temporal Accessibility Condition Selection Gate v0.1

**Status:** RECONSTRUCTED / WORKING — DECISION GATE OPEN

## 1. Purpose

Determine, ex ante and outcome-blind, whether the retained Rust dataset contains an observable temporal condition that can legitimately enrich the present-state accessibility predicate `P_tau(e_o,t)` while preserving the frozen identity of `tau`, the fixed-candidate-universe architecture selected under Option A, and the distinction between accessibility and execution.

This gate follows the accepted Dataset Temporal Semantics Audit v0.1 and does not execute `T_acc`, `Delta T_acc`, outcome, model or value.

## 2. Locked starting point

The following remain frozen:

- `Core_ontological = S`;
- `T_acc,t = {tau in U_tau | P_tau(S_t,C_t,L)=1}`;
- `Delta T_acc(t,t+1) = T_acc,t+1 not equivalent to T_acc,t`;
- Option A: fixed candidate universe + time-varying present accessibility;
- R* v0.2 is frozen;
- unsupported R* requirements are not silently recoded;
- accessibility is distinct from execution, outcome and value;
- SLR-1 is closed;
- TR-130–TR-140 are closed;
- EXT-1.1 outcome/model findings cannot define the new predicate.

## 3. Dataset evidence available

The audit established the following retained fields:

### packages.csv

`id, source_id, insource_id, name, url_id, repo_id, created_at`

### package_versions.csv

`id, package_id, version_str, created_at`

### package_dependencies.csv

`depending_version, depending_on_package, semver_str`

Genuine temporal fields identified:

- `packages.created_at`;
- `package_versions.created_at`.

No explicit retained field was identified for historical yank, deletion, availability state, validity interval, active/inactive dependency state, or equivalent status transition.

## 4. Candidate temporal constructions

### Option T1 — Target release availability

Use target-version `created_at <= t` as a present accessibility condition.

**Assessment:** OBSERVABLE but MONOTONE.

For fixed `U_tau`, if all other predicate terms remain unchanged:

`P_tau(t0)=1 => P_tau(t1)=1` for `t1 >= t0`.

Therefore this condition cannot generate removals and cannot by itself empirically discriminate contraction or reconfiguration.

**Decision:** RETAIN AS A VALID TEMPORAL CONDITION, BUT NOT SUFFICIENT FOR FULL DYNAMIC VALIDATION.

### Option T2 — Focal package release / dependency-declaration variation

Use the dependency declaration associated with successive versions of the focal package as a time-varying present condition.

This option requires a precise semantic distinction:

- candidate transformation identity must remain fixed independently of the declaration;
- the declaration applicable at time `t` may change as the focal package evolves;
- accessibility may then change because the present focal package state/conditions change, not because a later target version is newly released;
- the transformation identity cannot be redefined as “whatever dependency declaration is observed at t” if that would make membership define identity circularly.

The retained dependency table contains `depending_version`, `depending_on_package`, and `semver_str`, which can potentially be joined to focal package-version state. However, the dataset audit did not yet establish the exact row-level correspondence and whether successive focal declarations can be mapped without ambiguity to the frozen `tau` identity.

**Decision:** CANDIDATE — REQUIRES A DEDICATED EX-ANTE IDENTITY / DECLARATION VARIATION AUDIT BEFORE USE.

### Option T3 — Package creation time as a state condition

Use `packages.created_at` as a condition on the focal system.

**Assessment:** temporal but essentially fixed for a package across its versions. It does not by itself represent a changing accessibility condition between successive focal releases.

**Decision:** NOT SUFFICIENT AS A DYNAMIC ACCESSIBILITY CONDITION.

### Option T4 — Package-version creation time as a focal state condition

Use `package_versions.created_at` to define focal state transitions.

**Assessment:** establishes the temporal ordering of focal releases and can identify `t0/t1`, but it does not itself provide a non-monotone accessibility condition. It is a temporal index/state boundary, not sufficient accessibility semantics.

**Decision:** RETAIN FOR TEMPORAL STATE INDEXING, NOT AS AN INDEPENDENT ACCESSIBILITY CONDITION.

### Option T5 — External Cargo/Rust status information

Import yank/deletion/availability/status semantics from external sources.

**Assessment:** would require new data acquisition and a new ex-ante data contract. It cannot be silently inferred from the retained dataset.

**Decision:** OUT OF CURRENT GATE / NOT AUTHORIZED.

### Option T6 — Outcome-derived or future-derived condition

Use subsequent activity, later success, future release counts, observed downstream behavior, model predictions, or value to determine present accessibility.

**Decision:** PROHIBITED — LEAKAGE / CIRCULARITY.

## 5. Primary methodological decision

The retained dataset supports a legitimate temporal index through package-version `created_at`, and it supports target-release availability as an observable condition. But target-release availability alone reproduces the monotonicity already diagnosed.

The only endogenous route that may provide a genuinely time-varying present condition without importing external status data is **variation in the focal package's dependency declarations across successive focal package versions**.

This route is not accepted yet. It requires a separate structural audit of declaration identity and temporal variation.

## 6. Required identity condition for T2

Before T2 can be accepted, the following must be demonstrated:

1. `tau_id` remains independently defined as `(origin_version_id,target_package_id,target_version_id)` or an explicitly justified equivalent fixed identity;
2. dependency declaration rows can be associated with the correct focal origin version;
3. the declaration's `semver_str` can vary across focal releases without redefining `tau`;
4. accessibility at `t0` and `t1` can be evaluated using only information available at each time;
5. candidate existence remains independent of accessibility;
6. accessibility remains independent of execution and outcome;
7. the same fixed candidate universe can be evaluated at both times;
8. removals, if observed, arise from a legitimate change in present conditions rather than from changing candidate-universe membership;
9. unsupported R* syntax remains explicitly unsupported;
10. no future information is used to classify present accessibility.

## 7. Falsifiers

### T2-F1 — Identity collapse

The declaration cannot be mapped to a fixed transformation identity without making identity depend on accessibility membership.

### T2-F2 — No temporal variation

Successive focal releases do not produce a semantically meaningful change in the relevant dependency declaration.

### T2-F3 — Circularity

The proposed declaration-based predicate uses T_acc membership itself to define the declaration or transformation.

### T2-F4 — Candidate-universe contamination

The declaration-based construction changes `U_tau` rather than only `P_tau`.

### T2-F5 — Leakage

Evaluation at `t0` requires information created after `t0`.

### T2-F6 — Unsupported semantics

A required distinction cannot be represented with R* v0.2 and the retained data without inventing or silently extending semantics.

### T2-F7 — No observable change

No legitimate declaration-level change can produce a change in accessibility under the fixed identity.

## 8. Gate criteria

| Criterion | Status |
|---|---|
| TG-G1 temporal fields identified | PASS |
| TG-G2 focal release temporal index available | PASS |
| TG-G3 target release temporal condition available | PASS |
| TG-G4 independent status/yank field available | NOT FOUND |
| TG-G5 target-release condition non-monotone | FAIL / structurally monotone |
| TG-G6 declaration-level temporal variation identifiable | OPEN |
| TG-G7 declaration variation preserves fixed tau identity | OPEN |
| TG-G8 fixed U_tau preserved | OPEN |
| TG-G9 non-circular P_tau preserved | OPEN |
| TG-G10 outcome-blind evaluation | PASS |
| TG-G11 R* v0.2 unchanged | PASS |
| TG-G12 full dynamic Delta T_acc validation currently authorized | NO |

## 9. Decision

**GATE STATUS: CONDITIONAL PASS — T2 DECLARATION-LEVEL TEMPORAL VARIATION IS THE ONLY CURRENTLY AUTHORIZED ENDOGENOUS CANDIDATE FOR FURTHER AUDIT.**

No revised accessibility predicate is frozen by this document.

No revised T_acc implementation is authorized by this document.

No outcome/model protocol is authorized.

## 10. Next controlled operation

**TGCV Rust Focal Declaration Temporal Variation / Transformation Identity Audit v0.1**

That audit must inspect the actual dependency rows and successive focal package versions to determine whether declaration-level variation can support a non-circular, fixed-identity, time-varying `P_tau` under Option A.

If the audit fails, the scientifically correct conclusion is that the retained Rust dataset cannot support the intended non-monotonic accessibility validation without a new data source or an explicitly approved new data contract.

If it passes, only then may a new predicate freeze gate be opened.
