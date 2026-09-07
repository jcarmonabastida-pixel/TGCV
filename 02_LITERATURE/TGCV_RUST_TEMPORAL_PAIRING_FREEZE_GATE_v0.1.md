# TGCV — Rust Temporal Pairing Freeze Gate v0.1

**Status:** RECONSTRUCTED / WORKING  
**Date:** 2026-09-07  
**Phase:** Rust domain instantiation — outcome-blind structural validation

## 1. Purpose

Freeze, ex ante, the temporal observation rule used to compare accessible transformation spaces for the same Rust package-version unit.

This Gate resolves the only temporal indeterminacy left by the Rust Accessibility Semantics Freeze Gate: the exact definition of the paired observations used to construct `T_acc,t` and `T_acc,t+1`.

No outcome, predictive model, value criterion, or post-hoc performance information may influence the pairing rule.

## 2. Locked starting architecture

`Core_ontological = S`

`T_acc,t = {τ ∈ U_τ | P_τ(S_t,C_t,L)=1}`

`ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

`I` remains explanatory, not primitive.

The following are already frozen and are not reopened here:

- Rust unit: `e = package@version`;
- transformation identity `τ_id = (origin_version_id,target_package_id,target_version_id)`;
- independent candidate universe;
- R* v0.2 requirement semantics;
- accessibility/execution separation;
- membership-level `T_acc`;
- `Add`, `Rem` and `ΔT_acc` operator.

## 3. Temporal unit of observation

The primary temporal observation unit is a **single focal package-version `e_o` evaluated at two historical information boundaries**.

For each focal origin:

- `t_0 = created_at(e_o)` — origin boundary;
- `t_1` — the first subsequent observation boundary at which the same focal package-version remains analytically observable under the frozen temporal rule.

The comparison is therefore within the same focal identity, not between different package versions.

## 4. Frozen rule for `t_0`

`t_0` is exactly the canonical publication timestamp of the focal origin package-version.

The candidate universe at `t_0` is:

`U_τ(e_o,t_0) = {(e_o,p_d,v_d) | created_at(v_d) <= t_0}`.

No release occurring after `t_0` may enter the baseline candidate universe.

## 5. Frozen rule for `t_1`

`t_1` is defined as the **next release timestamp of the same focal package** after `t_0`, when such a release exists in the frozen dataset.

Thus, if `e_o = p@v_i` and the same package has a next version `v_{i+1}` with timestamp `t_1`, then:

`pair(e_o) = (e_o,t_0,t_1)`.

If no subsequent release of the same focal package exists in the available dataset, the focal unit has **no valid temporal pair** and is excluded from the paired temporal audit, while remaining present in the structural census.

This exclusion is based solely on temporal observability and is independent of outcome.

## 6. Why the next focal release is used

The next focal release provides a deterministic, package-local temporal boundary without selecting a horizon according to later outcome behaviour.

It also preserves the distinction between:

`origin state → changed present conditions → changed accessibility space`

and avoids importing the previous EXT-1.1 outcome window.

The rule is not intended to claim that one-release intervals are theoretically privileged; it is the frozen first operational temporal interval for this validation.

## 7. Candidate universe at `t_1`

At `t_1`, the candidate universe is reconstructed under the **same candidate identity and temporal rule**, but with the new information boundary:

`U_τ(e_o,t_1) = {(e_o,p_d,v_d) | created_at(v_d) <= t_1}`.

The transformation identity remains anchored to the same focal origin package-version.

No candidate is created merely because it was observed in an executed dependency graph.

## 8. Frozen accessibility comparison

For each candidate in the common canonical universe:

`P_τ(t_0)` and `P_τ(t_1)` are evaluated independently under exactly the same R* grammar and admissibility rules.

The resulting spaces are:

`T_acc,t0 = {τ | P_τ(t_0)=1}`

`T_acc,t1 = {τ | P_τ(t_1)=1}`.

No outcome or execution information is used in either construction.

## 9. Comparison universe and additions/removals

Because `U_τ(t_1)` may contain candidates that did not exist at `t_0`, the paired comparison uses the union of the two canonical candidate universes:

`U_pair = U_τ(t_0) ∪ U_τ(t_1)`.

A candidate not yet existing at `t_0` is inaccessible at `t_0` by the frozen temporal rule and may become accessible at `t_1` if the frozen admissibility predicate is satisfied.

Define:

`Add = T_acc,t1 \ T_acc,t0`

`Rem = T_acc,t0 \ T_acc,t1`.

The membership-level operator therefore captures transformations newly accessible or no longer accessible at the second boundary.

## 10. Classification

For every valid pair:

- **persistence:** `Add=∅` and `Rem=∅`;
- **expansion:** `Add≠∅` and `Rem=∅`;
- **contraction:** `Add=∅` and `Rem≠∅`;
- **reconfiguration/substitution:** `Add≠∅` and `Rem≠∅`.

`ΔT_acc ≠ 0` iff `Add ≠ ∅` or `Rem ≠ ∅`.

Cardinality change alone is not sufficient for classification.

## 11. Temporal ordering constraints

The audit must enforce:

`created_at(e_o) = t_0 < t_1`.

For every candidate represented as accessible at either boundary, its target release must satisfy the relevant boundary rule.

No information whose first appearance is after the boundary may be used to classify accessibility at that boundary.

## 12. Same-unit requirement

A pair is valid only if:

1. the focal package identity is identical;
2. the origin version identity is fixed;
3. `t_0` is the origin version's publication timestamp;
4. `t_1` is the next release timestamp of the same package;
5. transformation identity is unchanged;
6. R* semantics are unchanged;
7. canonicalization is unchanged.

Cross-package and non-local temporal pairing is prohibited.

## 13. Missing and terminal cases

The audit must distinguish:

- **paired:** valid `t_0 → t_1` exists;
- **terminal:** no later focal release exists;
- **invalid timestamp:** temporal ordering cannot be established;
- **unresolved:** required identifiers or dependency semantics cannot be resolved.

Terminal units are not treated as evidence of persistence, contraction or expansion.

Invalid/unresolved units are not silently classified as inaccessible.

## 14. Coverage accounting

The audit must report at minimum:

- total focal package-versions in the census;
- paired focal package-versions;
- terminal focal package-versions;
- invalid temporal cases;
- unresolved temporal cases;
- candidate counts at `t_0` and `t_1`;
- empty `T_acc,t0` counts;
- empty `T_acc,t1` counts;
- valid paired observations;
- expansion, contraction, persistence and reconfiguration counts;
- unresolved candidate counts at each boundary.

Coverage is descriptive and must not be optimized for any later outcome.

## 15. Determinism requirements

The temporal pairing procedure must be deterministic and row-order invariant.

If multiple records could qualify as the next focal release, the canonical version identity and timestamp ordering must provide a deterministic choice. If ties cannot be resolved from frozen identifiers, the pair is marked unresolved rather than selected post hoc.

Repeated execution over identical frozen inputs must produce identical pair identities and identical `T_acc` membership sets.

## 16. Relationship to EXT-1.1

The following are explicitly **not inherited**:

- the EXT-1.1 180-day outcome window;
- its train/test temporal boundary;
- its outcome definition;
- its predictive model;
- its feature construction;
- any pairing chosen to maximize predictive or outcome contrast.

Only generic temporal indexing/integrity infrastructure may be reused.

## 17. Outcome-blindness firewall

The following are prohibited before temporal pairing and `ΔT_acc` classification:

- subsequent release activity as an outcome;
- future package activity beyond the two frozen observation boundaries;
- model-derived variables;
- value evaluations;
- outcome prevalence;
- effect-size calculations;
- predictive discrimination.

The audit is strictly structural.

## 18. Falsifiers

**TPF-1:** the next focal release cannot be determined reproducibly.

**TPF-2:** valid pairs cannot preserve identical focal identity.

**TPF-3:** `t_0 < t_1` cannot be established reliably.

**TPF-4:** accessibility at either boundary requires post-boundary information.

**TPF-5:** `T_acc,t0` or `T_acc,t1` cannot be reconstructed at membership level.

**TPF-6:** `Add` and `Rem` cannot be computed deterministically.

**TPF-7:** terminal/missing/unresolved cases cannot be separated from valid temporal pairs.

**TPF-8:** pairing requires knowledge of the eventual outcome or model.

**TPF-9:** repeated execution is not deterministic.

## 19. Gate criteria

| Criterion | Result |
|---|---|
| TPF-G1 | Origin boundary `t_0` frozen — PASS |
| TPF-G2 | Next-release rule for `t_1` frozen — PASS |
| TPF-G3 | Same-package/same-unit pairing frozen — PASS |
| TPF-G4 | Candidate universe at both boundaries frozen — PASS |
| TPF-G5 | Union comparison universe frozen — PASS |
| TPF-G6 | `Add`/`Rem`/`ΔT_acc` classification frozen — PASS |
| TPF-G7 | Terminal/invalid/unresolved treatment frozen — PASS |
| TPF-G8 | Coverage accounting frozen — PASS |
| TPF-G9 | Determinism requirements frozen — PASS |
| TPF-G10 | Outcome/model firewall frozen — PASS |
| TPF-G11 | Temporal pairing audit executed — NOT YET |

## 20. Gate decision

**PASS — TEMPORAL PAIRING CONTRACT FROZEN FOR OUTCOME-BLIND STRUCTURAL AUDIT.**

The temporal boundary is now fixed independently of outcomes. The next audit may therefore reconstruct paired `T_acc` spaces and `ΔT_acc` without making a temporal choice after inspecting results.

## 21. Immediate next controlled operation

**TGCV Rust Paired Temporal T_acc / ΔT_acc Structural Audit v0.1**.

The audit must execute this contract on the frozen Rust dataset and report structural feasibility and temporal change classes only.

No outcome, predictive model or value hypothesis may be introduced until the structural audit is reviewed and accepted.

## 22. Integrity lock

Any modification to the origin boundary, next-release pairing rule, candidate temporal rule, comparison universe, or `ΔT_acc` operator requires a new ex-ante versioned Gate.
