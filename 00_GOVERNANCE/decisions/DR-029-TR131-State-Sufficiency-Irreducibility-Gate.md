# DR-029 — TR-131 State Sufficiency / Transformational-Space Irreducibility Gate v0.2

**Status:** ACCEPTED — EX-ANTE DESIGN / NO EXECUTION AUTHORIZED  
**Accepted:** 2026-09-07  
**Supersedes:** v0.1 proposal in this file  
**Scope:** EXT-1.1 Rust / TGCV Core integrity  
**Predecessors:** TR-130; DR-018; DR-025A; DR-026A; DR-028

## 1. Purpose

Determine whether the accessible transformation space `T_acc` contains information not recoverable from a frozen conventional state representation, independently of predictive superiority.

DR-029 is a structural theoretical test gate. It does not constitute predictive validation and does not authorize any reuse of the closed DR-027 confirmatory analysis.

## 2. Discriminating question

Can two admissible Rust origin states that are equivalent under the frozen conventional representation `B` nevertheless have different accessible transformation spaces `T_acc`?

Formally, the constructive evidence target is:

`B(S_a) = B(S_b)  AND  T_acc(S_a) != T_acc(S_b)`.

If such a pair exists, `B` is insufficient to determine `T_acc`, providing support for TR-131 for the tested representation. If exhaustive admissible evaluation finds no such difference, the result is non-support for irreducibility relative to `B` only; it is not a universal refutation of TGCV.

## 3. Exact candidate state representation — FROZEN

The conventional state representation is the already accepted and frozen EXT-1.1 baseline representation from DR-025A:

`B(v_o) = (V_o, H_o, A_o, D_o)`

with:

- `V_o` = observed `version_str`, treated as nominal categorical release-state information;
- `H_o` = `prior_release_count_o`, the number of earlier same-package releases with `created_at < created_at(v_o)`;
- `A_o` = `package_age_days_o`, elapsed time from the earliest observed same-package release to `created_at(v_o)`;
- `D_o` = number of raw dependency declaration rows attached to the origin release.

For TR-131, `B` is treated as a **conventional state representation**, not as the ontological definition of `S` in the EXT-1.1 operational specification. This distinction is essential: the test asks whether `T_acc` adds structural information beyond this accepted conventional representation, not whether the full Rust historical structural state mechanically determines `T_acc`.

The predictive encoding `B_num` is irrelevant to TR-131 and must not be used for state equivalence. In particular, no learned encoding, target encoding, package identity feature, or model-derived representation is permitted.

## 4. Why `B` is the correct frozen candidate

`B` is the strongest currently available conventional comparator because it was accepted independently of the observed DR-027 result, is explicitly outcome-independent, contains only origin-state/historical information, and deliberately excludes resolved `T_acc`, `R*`, outcome, and post-origin information.

Using `B` also avoids circularity: the equivalence relation does not contain the object whose irreducibility is being tested.

The test therefore has a clear interpretation:

- `B` sufficient for `T_acc` → no evidence that `T_acc` is irreducible relative to this conventional state representation;
- `B` insufficient for `T_acc` → constructive evidence that the accessible transformation space contains information not captured by `B`.

This is a representation-relative result and must not be generalized to every possible state representation.

## 5. Exact Rust transformation identity

The transformation family is the accepted EXT-1.1 dependency-resolution family governed by DR-020 and DR-021.

A candidate transformation is represented as a resolved relation from an origin release to a selected target release:

`(v_o, p_d, v_d*)`

where `v_d*` is the greatest eligible target version satisfying the dependency requirement under the frozen restricted `R*` semantics and the historical temporal cutoff.

The accepted `T_acc` representation is the canonical resolved-pair relation `A_rel(v_o)`; its cardinality `A_count(v_o)` is derived and is not a substitute for membership comparison.

The normative `T_acc` construction must remain the DR-021 / DR-026A construction. No alternative resolver or post-hoc transformation definition is permitted.

## 6. Origin-state and information firewall

State equivalence and `T_acc` construction must use only information admissible at the origin state and the frozen historical structural snapshot.

The following are prohibited from equivalence construction, pair selection, or interpretation:

- `Y_180` or any later outcome;
- future package activity;
- downloads, adoption, success, or popularity after origin;
- predictive performance, LogLoss, Brier, AUC, or model selection;
- `Reach` as a substitute for `T_acc` comparison;
- post-origin structural metadata;
- any learned or target-derived feature;
- any selection criterion introduced after inspection of DR-029 results;
- any decision conditioned on the negative DR-027 result.

Package identity is not part of `B` and therefore cannot be added to the equivalence relation merely to increase or decrease the availability of comparison pairs.

## 7. Required empirical construction

If execution is later authorized by a dedicated implementation gate, the executor shall:

1. reconstruct `B(v_o)` exactly according to DR-025A;
2. construct the canonical `T_acc(v_o)` exactly according to DR-021/DR-026A;
3. group origin states by exact equality of the frozen `B` tuple;
4. identify admissible equivalence classes containing at least two distinct origin observations;
5. compare the canonical `T_acc` membership sets within each class;
6. record whether any class contains unequal `T_acc` sets;
7. preserve canonical ordering and deterministic replay;
8. report counts of admissible equivalence classes, pairwise comparisons or equivalent class-level comparisons, classes with differing `T_acc`, and the constructive witness when present.

The primary comparison is set membership equality, not cardinality equality.

## 8. Exhaustiveness and decision logic

The preferred evidence mode is exhaustive census over all admissible origin observations, consistent with the already established feasibility of deterministic census in EXT-1.1.

Decision logic:

- **TR-131 support for `B`:** at least one valid state-equivalent class contains two origin states with demonstrably different `T_acc` membership sets.
- **TR-131 non-support for `B`:** exhaustive evaluation of all admissible `B` equivalence classes finds identical `T_acc` membership within every class.
- **Indeterminate:** equivalence classes or `T_acc` membership cannot be reconstructed without violating the frozen specifications or information firewall.

No p-value, confidence interval, predictive metric, or statistical significance threshold is required for this structural test.

## 9. Treatment of special states

- Empty `T_acc` is a valid set and must remain distinguishable from missing or failed reconstruction.
- Missing required origin identity or structural inputs must fail closed and be reported, not imputed.
- Terminal observations are retained when they are valid origin states; they are not discarded because they have no accessible transformations.
- Duplicate origin/version identifiers are an integrity failure and must not be silently collapsed.
- The equivalence relation is exact equality of the frozen `B` tuple; approximate matching, binning, nearest-neighbour matching, or learned similarity is prohibited.

## 10. Separation from Reach non-redundancy

DR-018 established a distinct structural property concerning Reach and successor configurations. It does not answer TR-131.

DR-029 therefore compares `T_acc` membership directly against equivalence under `B`; it must not replace `T_acc` by Reach, reachable cardinality, trajectory length, or another downstream construct.

## 11. Relationship to DR-027 and DR-028

DR-027C remains closed. DR-028 remains the governing scientific interpretation boundary.

The negative predictive result of DR-027 is neither an input nor a selection criterion for DR-029. DR-029 tests a different proposition and is intentionally independent of predictive performance.

## 12. Determinism and reproducibility requirements

Any later executor must use deterministic canonical ordering, deterministic serialization, and replay verification. The same frozen dataset, specifications, and implementation must produce the same equivalence classes and `T_acc` comparisons on repeated execution.

No sampling is permitted unless a separate accepted decision explicitly changes this gate; the default is exhaustive census.

## 13. Governance status

**DR-029 is ACCEPTED as an ex-ante structural design gate.**

Acceptance freezes the candidate state representation as `B` and freezes the structural comparison defined above.

Acceptance does **not** authorize execution. A separate implementation/pre-execution gate must verify that the executor faithfully implements this design, including the exact `B` equality relation, canonical `T_acc` construction, exhaustive census, information firewall, and replay requirements.

No TR-131 conclusion may be recorded before that execution gate passes and the authorized run is completed.

## 14. Next gate

The next work item is the **DR-029 implementation/pre-execution audit**, followed only if it passes by construction of the deterministic executor and its synthetic conformance tests.
