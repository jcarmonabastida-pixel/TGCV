# TGCV — Rust Fixed-Candidate Declaration-Driven Accessibility Shadow Audit v0.1 — Result Review

**Status:** CONDITIONAL PASS — DECLARATION-DRIVEN FIXED-CANDIDATE ACCESSIBILITY CHANGE DEMONSTRATED; FINAL STRUCTURAL ACCEPTANCE REMAINS GATED

## 1. Purpose

This review records the successful outcome-blind shadow execution of the redesigned Rust accessibility construction. The execution tests whether a fixed transformation identity can change accessibility between successive focal package versions as a consequence of declaration variation, without using target-release availability, execution, outcome, value, or future activity.

This is a structural shadow audit. It does not compute `T_acc`, `Delta T_acc`, outcomes, models, or value.

## 2. Runtime result

The execution completed successfully with `RUNTIME_AUDIT_OK: True`.

Key observations:

- FOCAL_VERSION_COUNT: 607,498
- PACKAGE_COUNT: 91,437
- SUCCESSIVE_FOCAL_PAIRS_TOTAL: 516,061
- SUCCESSIVE_FOCAL_PAIRS_INSPECTED: 516,061
- DEPENDENCY_ROWS_SCANNED: 3,618,523
- MALFORMED_ROWS: 0
- DUPLICATE_ROWS: 0
- DECLARATION_CHANGED_FOCAL_TARGET_PAIRS: 752,721
- DECLARATION_REMOVED_TARGET_PAIRS: 60,914
- DECLARATION_ADDED_TARGET_PAIRS: 121,060
- DECLARATION_CHANGED_TARGET_PAIRS: 570,747
- FIXED_CANDIDATES_TESTED: 39,238,220
- UNSUPPORTED_TARGET_VERSIONS_EXCLUDED: 1,266,151
- ACCESSIBILITY_1_TO_0: 1,475,648
- ACCESSIBILITY_0_TO_1: 827,361
- ACCESSIBILITY_PERSISTENT_1: 106,528
- ACCESSIBILITY_PERSISTENT_0: 36,828,683
- DECLARATION_DRIVEN_ACCESSIBILITY_CHANGES: 2,303,009

## 3. Scientific interpretation

The shadow construction successfully demonstrates a non-trivial declaration-driven change in accessibility for transformation candidates whose identity is held fixed.

This is materially different from the earlier paired construction, where the candidate universe itself was effectively time-indexed by target-release availability and therefore induced monotonicity. In the present shadow construction, target-release availability is explicitly prevented from being the change driver.

The result therefore establishes a concrete structural counterexample to the proposition that, in this Rust instantiation, accessibility of a fixed candidate must remain invariant whenever the candidate identity is fixed.

Both directions are observed:

- `1 -> 0`: a previously accessible fixed candidate becomes inaccessible after focal declaration change.
- `0 -> 1`: a previously inaccessible fixed candidate becomes accessible after focal declaration change.

This is the relevant structural property required for a non-monotonic accessibility relation and for a future empirical reconstruction of `Delta T_acc`.

## 4. Important semantic qualification

The result does **not** yet establish the full TGCV dynamic claim.

In particular, it does not by itself establish:

- that the resulting complete `T_acc,t` representation is scientifically sufficient;
- that `Delta T_acc` has downstream consequences for `Reach`;
- that those consequences alter `Trajectory`;
- that any downstream change affects outcome or value;
- causal sufficiency;
- predictive superiority;
- universal cross-domain validity;
- universal ontological irreducibility or universal novelty.

The execution remains a shadow structural demonstration.

## 5. R* coverage issue

`R* v0.2` remains frozen. Unsupported target versions were excluded rather than coerced.

The execution reports 1,266,151 unsupported target-version exclusions. This is a material coverage limitation and must remain explicitly documented. It is not evidence that those candidates are inaccessible under Rust generally; it is evidence that they are outside the frozen analytical grammar and therefore unavailable to this particular shadow predicate.

No grammar change is authorized by this result.

## 6. Leakage / integrity result

The execution confirms:

- candidate identity does not include declaration;
- candidate-universe membership is not declaration-driven;
- target-release cutoff is not used as the change driver;
- unsupported versions are not silently coerced;
- execution is not used;
- outcome is not used;
- value is not used;
- future activity is not used;
- R* is not modified;
- `T_acc` is not computed;
- `Delta T_acc` is not computed;
- no model is fitted.

## 7. Example structural cases

The execution contains direct examples of both accessibility directions. For example:

- focal version `6 -> 562825`, target package `3772`, fixed target version `0.101.2`: `1 -> 0`, with requirement changing from `=0.101.2` to `=0.101.3`;
- focal version `8 -> 67434`, target package `81974`, fixed target version `0.3.1`: `1 -> 0`, with requirement changing from `^0.3.1` to `^0.3.2`;
- focal version `13 -> 464347`, target package `84251`, fixed target version `0.5.0`: `0 -> 1`, with requirement changing from `>=0.5.0, <0.6.0` to `^0.5.0` under the frozen R* contract;
- focal version `13 -> 464347`, target package `88385`, fixed target version `0.6.1`: `0 -> 1`, where the declaration is newly added.

These examples are structurally sufficient to show that the effect is not merely a consequence of the target version first appearing after the temporal boundary.

## 8. Gate decision

**CONDITIONAL PASS — FIXED-CANDIDATE DECLARATION-DRIVEN ACCESSIBILITY CHANGE DEMONSTRATED.**

The shadow audit has passed the specific structural question for which it was designed: a fixed candidate transformation can switch accessibility in both directions under observed focal declaration changes, while maintaining candidate identity independently of the declaration and without using execution/outcome/value information.

The final acceptance of this construction as the Rust operational realization of TGCV `P_tau` remains subject to a dedicated structural decision gate covering semantic adequacy, coverage, canonicalization, complete `U_tau`, and reconstruction integrity.

## 9. Integrity lock

- Core remains `S`.
- `T_acc` remains a derived analytical object.
- `Delta T_acc` remains the primary differentiated candidate.
- `I` remains explanatory, not a Core primitive.
- SLR-1 remains closed.
- TR-130–TR-140 remain closed.
- EXT-1.1 predictive outcome/model results are not used as validation.
- No outcome/model/value execution is authorized from this result alone.
- R* v0.2 remains frozen.

## 10. Next controlled operation

**TGCV Rust Fixed-Candidate Accessibility Structural Decision Gate v0.1**

That gate must decide whether the shadow construction is semantically adequate for formal Rust `P_tau` instantiation, identify the coverage limitation represented by unsupported versions, and determine the minimal conditions for a full structural `T_acc,t / Delta T_acc` audit.

**Report canonical SHA:** `622e6e20f4ad8147e0b8fbe13bf4f8fddefe8e82743255e5bd18996c4fb9d32a`
