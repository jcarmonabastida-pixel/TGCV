# TGCV TR-131 — Expanded-State Challenge Operational Specification v01

**Status:** BLOCKED — NO NON-TAUTOLOGICAL OPERATIONAL REPRESENTATION AVAILABLE FROM FROZEN SEMANTICS
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Gate determination

The expanded-state challenge cannot currently be operationalized from the frozen TR-131 construction without introducing new pre-realization semantics that are absent from the frozen package.

The decisive canonical input is `03_EXPERIMENTS/TR-131/scientific_policy_definitions.json`.

Its frozen policy definitions specify:

- `policy_A` selects `tau_accept`;
- `policy_B` selects `tau_defer`;
- `selection_source: X`;
- `post_hoc: false`.

Thus the only declared pre-realization determinant of selection is X itself.

## 2. Consequence for E1/E2

The challenge candidates were:

- E1: `S' = G(S,C,X)`
- E2: `C' = G(C,X)`

The non-tautology rule explicitly prohibits simply copying or renaming X into S' or C'.

Because the frozen policy semantics provide no independently defined semantic decomposition of X into another pre-existing state/context property, no reproducible G1 or G2 can presently be specified without inventing new semantics.

Likewise, a rule `T_real = F(S',C',T_acc)` cannot be fixed without either reconstructing the same selection encoded by X under another name, which is explicitly disallowed, or introducing an additional pre-realization semantic variable/rule not contained in the frozen construction.

The second option would constitute a new experimental construction and cannot be silently inserted into this candidate package.

## 3. Counterfactual consequence

The required counterfactual cannot be fixed non-tautologically from the current frozen semantics.

The existing construction permits the alternative:

- X = policy_A → tau_accept
- X = policy_B → tau_defer

but this is precisely the X distinction under test. A counterfactual that changes only X therefore does not demonstrate absorption into an independently defined expanded state/context.

## 4. Scientific disposition of this design gate

**BLOCKED — OPERATIONAL SPECIFICATION CANNOT BE CLOSED FROM THE FROZEN TR-131 SEMANTICS.**

This is a design limitation, not a scientific FAIL of the expanded-state challenge.

No PASS/FAIL/INCONCLUSIVE scientific outcome is assigned.

## 5. Required next gate

### Path A — Close using existing frozen semantics

Proceed only if an independently existing pre-realization semantic structure can be identified in the frozen package that is not X, not a renamed X, and not derived from T_real/H/outcome/value.

If such a structure exists, it must be cited explicitly and used to define G and F reproducibly.

### Path B — New challenge construction

If no such structure exists, define a new challenge construction introducing an independently justified pre-realization semantic variable. That construction must be separately audited and frozen; it must not modify the frozen TR-131 package.

## 6. Governance boundary

- Frozen TR-131 package: unchanged.
- Original TR-131 scientific result: unchanged.
- Scientific disposition: unchanged.
- TGCV Core/RMA/Evidence Matrix: unchanged.
- No package freeze for the expanded-state challenge.
- No scientific execution authorization.

## 7. Audit requirement

The prior expanded-state design audit cannot be treated as an operational specification audit. The correct current state is:

**DESIGN AUDIT: PASS**
**OPERATIONAL SPECIFICATION AUDIT: BLOCKED**

The next action is to inspect the remaining frozen TR-131 artifacts for any independently specified pre-realization semantic structure that can support G/F without relabelling X. If none exists, stop and construct a separate new challenge rather than manufacture one post hoc.
