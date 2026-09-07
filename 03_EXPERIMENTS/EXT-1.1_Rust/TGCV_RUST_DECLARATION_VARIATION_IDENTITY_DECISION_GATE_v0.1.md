# TGCV — Rust Declaration Variation / Transformation Identity Decision Gate v0.1

**Status:** CONDITIONAL PASS — DECLARATION VARIATION CONFIRMED; FIXED-IDENTITY ACCESSIBILITY EFFECT REQUIRES DEDICATED SHADOW AUDIT

## 1. Purpose

Assess the result of the Focal Declaration Temporal Variation / Transformation Identity Audit v0.1 and decide whether declaration-level temporal variation is a scientifically legitimate route for the next Rust structural audit under Option A.

This Gate does not compute `T_acc`, `Delta T_acc`, outcome, model or value, and does not freeze a revised accessibility predicate.

## 2. Executed evidence

Dataset:
`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

Runtime audit status:
`RUNTIME_AUDIT_OK: True`

Report canonical SHA-256:
`dcf8022aef684f088e36c7335027d1893792993faf0eb1096971c675b33fac3e`

Observed:

- `607,498` focal package versions indexed;
- `91,437` packages represented;
- `3,618,523` dependency rows scanned;
- `516,061` successive focal-version transitions;
- `0` temporal-order violations;
- `232,159` transitions with declaration changes;
- `283,902` unchanged transitions;
- `23,505` added-only transitions;
- `7,699` removed-only transitions;
- `200,955` transitions with both additions and removals;
- `193,447` transitions with same-target SemVer variation;
- `74,011` transitions with target-package-set variation;
- `691,807` declaration additions;
- `631,661` declaration removals;
- `570,747` same-target SemVer changes.

The examples include exact-version changes, caret requirement changes, range changes, target additions and target removals.

## 3. Identity assessment

The audit reports:

- `FOCAL_IDENTITY_IS_TIME_INDEPENDENT: True`;
- `CANDIDATE_IDENTITY_NOT_DEFINED_BY_DECLARATION: True`;
- `DECLARATION_VARIATION_OBSERVED: True`.

This establishes that the focal package-version identity can remain fixed while its dependency declarations change between successive versions.

However, the audit deliberately did **not** demonstrate that a fixed candidate transformation identity `(origin_version_id,target_package_id,target_version_id)` changes accessibility as a consequence of declaration variation. It also did not construct a fixed `U_tau` and did not evaluate the revised `P_tau`.

Therefore identity preservation is supported, but accessibility-effect validity remains open.

## 4. Why this matters

The observed pattern is materially different from the previous target-release-only construction.

Under target-release-only accessibility, later time can only add target versions. Here, the focal package itself changes its dependency declarations between releases. A fixed candidate transformation can therefore potentially move from accessible to inaccessible, or inaccessible to accessible, because the present focal declaration governing that transformation changes.

This provides a legitimate endogenous mechanism for possible non-monotonic accessibility **if and only if** the candidate universe is fixed independently of those declarations and the declaration-to-transformation mapping is non-circular.

The existence of declaration variation is therefore evidence for feasibility of the route, not proof that the route is already a valid TGCV accessibility predicate.

## 5. Important semantic constraint

The next implementation must not define transformation identity as:

`tau = (focal_version, target_package, semver_declaration)`

if that makes changes in declaration mechanically create changes in transformation identity.

The frozen identity must remain independent of accessibility and declaration content. The declaration is a present-state condition used by `P_tau`, not the identity of `tau` itself.

The preferred candidate identity remains:

`tau_id = (origin_version_id, target_package_id, target_version_id)`

with declaration semantics evaluated against the focal package-version's present dependency declaration.

## 6. Decision on candidate route

**T2 — focal declaration temporal variation: ACCEPTED FOR SHADOW AUDIT.**

It is not yet accepted for confirmatory structural execution.

The next audit must establish whether, for a fixed candidate `tau`, declaration changes can alter `P_tau` while:

1. `U_tau` remains fixed;
2. `tau_id` remains fixed;
3. R* v0.2 remains unchanged;
4. unsupported declarations remain explicitly unsupported;
5. no target-release timestamp is used to redefine candidate existence;
6. accessibility is evaluated from present focal declaration/state;
7. execution and later outcome are excluded;
8. no future information leaks into earlier accessibility.

## 7. Falsification conditions for the next audit

The T2 route must be rejected if any of the following is demonstrated:

- declaration changes cannot be mapped to fixed candidate transformations;
- candidate-universe membership changes when declarations change;
- the only possible mapping makes declaration content part of transformation identity;
- accessibility classification requires later execution or outcome;
- the route collapses back to target-release availability and remains monotone;
- R* v0.2 cannot be applied without silent semantic extension;
- unresolved/unsupported declarations cannot be preserved without distortion.

## 8. Gate criteria

| Criterion | Result |
|---|---|
| DV-G1 focal temporal ordering | PASS |
| DV-G2 declaration variation observed | PASS |
| DV-G3 declaration removals observed | PASS |
| DV-G4 same-target SemVer changes observed | PASS |
| DV-G5 focal identity time-independent | PASS |
| DV-G6 declaration independent of candidate identity | PASS |
| DV-G7 fixed `U_tau` demonstrated | OPEN |
| DV-G8 declaration-driven fixed-identity `P_tau` demonstrated | OPEN |
| DV-G9 non-circular accessibility demonstrated | OPEN |
| DV-G10 non-monotonic `T_acc` demonstrated | OPEN / NOT COMPUTED |
| DV-G11 outcome/model/value exclusion | PASS |
| DV-G12 R* v0.2 unchanged | PASS |

## 9. Decision

**CONDITIONAL PASS — T2 IS A LEGITIMATE CANDIDATE ROUTE FOR FURTHER STRUCTURAL VALIDATION.**

The declaration-variation evidence is strong enough to justify a dedicated shadow audit, but not strong enough to freeze a new accessibility predicate or authorize a confirmatory `T_acc/Delta T_acc` run.

No outcome or predictive analysis is authorized.

## 10. Next controlled operation

**TGCV Rust Fixed-Candidate Declaration-Driven Accessibility Shadow Audit v0.1**

That audit must construct a fixed candidate universe independently of declaration variation and test, for concrete fixed candidate identities, whether the successive focal declarations would change accessibility under frozen R* v0.2 semantics.

Only if that shadow audit passes may a new predicate freeze Gate be opened.
