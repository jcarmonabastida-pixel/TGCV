# TGCV — Application Fit WP2-C05 EV–Grid Minimum Demonstrator Specification 001

**Status:** FROZEN SPECIFICATION — EXECUTION NOT AUTHORIZED
**Date:** 2026-09-17
**Parent synthesis:** `TGCV_APPLICATION_FIT_WP2_CROSS_CASE_DISCRIMINATION_MATRIX_001.md`
**Candidate screen:** `TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_DEEP_SCREEN_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.14 / RMA traceability v3.35

## 1. Purpose and boundary

This artifact specifies a bounded synthetic minimum demonstrator for the C05 EV–Grid application-fit case. It is an **applicability/discrimination demonstrator**, not a scientific validation experiment and not a value evaluation.

The demonstrator tests whether an explicit TGCV-style representation of evolving accessible transformations can be reconstructed and compared with a conventional constrained-feasibility/optimisation representation.

No execution is authorized by this specification alone.

## 2. Frozen system

The demonstrator contains:

- two charging sites: A and B;
- one simplified distribution-grid capacity constraint shared by the sites;
- a finite set of EVs;
- finite charging states;
- mobility/departure requirements;
- optional V1G/V2G capability represented as a transformation attribute;
- no stochastic external inputs during a run.

The system is intentionally small enough that the complete candidate transformation universe can be enumerated and audited.

## 3. Decision boundary

The decision boundary is the charging-management decision immediately before a concrete charging action is accepted, deferred, throttled, redirected or rejected.

All state/context information used by admissibility predicates must be available at that boundary and frozen before evaluation.

## 4. State and context

### 4.1 State

`S_t = {site_assignment, charging_state, grid_capacity_state, active_power, EV_energy_state}`

### 4.2 Context

`C_t = {departure_requirement, mobility_requirement, site_capacity, grid_limit, charging_policy, V1G_V2G_capability}`

### 4.3 Admissibility rules

`L = {grid safety constraints, site charging constraints, EV state constraints, mobility/departure constraints, charging policy constraints}`

The demonstrator must keep legal/operational admissibility rules distinct from outcome variables.

## 5. Transformation universe Uτ

The finite universe is:

1. `accept_A`
2. `accept_B`
3. `defer`
4. `reduce_power`
5. `shift_window`
6. `redirect_A_to_B`
7. `redirect_B_to_A`
8. `reserve_capacity`
9. `release_capacity`
10. `v1g_discharge`
11. `v2g_discharge`
12. `reject`

A transformation is included in `Uτ` even when inadmissible in a particular state. Accessibility is determined by `Pτ`, not by deleting actions from the universe.

Transformations requiring unavailable capability are retained in `Uτ` and become inadmissible through the corresponding predicate.

## 6. Outcome-independent admissibility predicate

For each transformation `τ`:

`Pτ(S_t,C_t,L) ∈ {0,1}`

The predicate may depend only on frozen system state, context and admissibility rules. It must not depend on downstream performance, economic outcome, observed trajectory after the decision, or any variable generated after the accessibility decision.

Then:

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`

and:

`ΔT_acc(t0,t1) = T_acc,t1 \ T_acc,t0` together with the corresponding closures/reorderings.

## 7. Frozen baseline state S0/C0

The canonical baseline is:

- Site A capacity: available;
- Site B capacity: available;
- shared grid capacity: **high**;
- EV demand: **low**;
- departure requirements: **relaxed**;
- V1G/V2G capability: available only where explicitly assigned;
- no site failure;
- no policy change;
- no hidden capacity constraint.

The exact numerical capacities and EV energy values must be fixed in the execution manifest before execution. This specification intentionally defines the qualitative baseline while requiring the numerical fixture to be frozen separately.

## 8. Controlled transition matrix

Each transition is applied independently first, with all other variables held constant.

| ID | Transition | Domain/state affected | Intended accessibility consequence |
|---|---|---|---|
| T1 | grid capacity high → constrained | energy/grid | closes or restricts power-intensive actions |
| T2 | EV demand low → high | mobility/charging | closes or restricts actions exceeding available capacity |
| T3 | Site B available → unavailable | charging infrastructure | closes B-dependent actions |
| T4 | departure relaxed → tight | mobility | closes actions incompatible with deadline |
| T5 | V1G/V2G unavailable → available | vehicle capability | opens V1G/V2G transformations |
| T6 | combined T1 + T4 | energy + mobility | tests cross-domain interaction of constraints |

The execution must preserve the distinction between single-factor transitions and the combined transition.

## 9. Required reconstruction outputs

For each transition, the execution record must contain:

1. `S0`
2. `C0`
3. `U_tau`
4. `P_tau` definition
5. `T_acc_0`
6. transition identifier
7. `S1`
8. `C1`
9. `T_acc_1`
10. `Delta_T_acc`
11. explicit opened transformations
12. explicit closed transformations
13. any reordered transformations, if ordering is part of the representation
14. downstream trajectory under the selected transformation policy
15. conventional baseline reconstruction
16. comparison observations
17. limitations
18. non-claims
19. execution metadata and hashes.

## 10. Conventional baseline

The baseline must be a finite constrained-feasibility representation equivalent in information scope to the demonstrator:

- same state variables;
- same constraints;
- same transformation/action universe;
- same transition sequence;
- no access to future outcomes.

The baseline may be expressed as a constrained optimisation/feasibility model. It must reconstruct which actions are feasible under each state.

The comparison question is therefore not whether the baseline can calculate feasibility. It normally can. The question is whether the TGCV-style representation provides an additional reusable description of **how the future accessible transformation space changes across coupled domains and how that change relates to trajectory reconstruction**.

## 11. Trajectory policy

To prevent arbitrary post-hoc choices, the demonstrator must freeze a deterministic action-selection policy before execution. The policy may be lexicographic or otherwise explicitly specified, but cannot use future outcomes.

The trajectory record must show the sequence of selected transformations and the resulting bounded state changes.

Trajectory observation is descriptive. It does not establish empirical causality or value creation.

## 12. Required discrimination comparison

The execution must compare TGCV-style and conventional representations on:

1. reconstruction of the same feasible/accessibility set;
2. identification of the transition that changed accessibility;
3. identification of cross-domain dependency;
4. representation of opened/closed transformations;
5. trajectory reconstruction;
6. assumptions required;
7. information omitted;
8. reproducibility from the frozen specification.

No superiority metric is prescribed at this stage. If both representations encode the same information, that result must be recorded as such rather than interpreted as TGCV differentiation.

## 13. Negative controls

At least two negative controls are required:

- **NC1:** a state change that alters an irrelevant descriptive variable without changing any admissibility rule;
- **NC2:** a routing/scheduling change that leaves `T_acc` unchanged.

For each negative control:

`ΔT_acc = ∅`.

Negative controls are necessary to show that the mapper does not manufacture accessibility changes from arbitrary state differences.

## 14. Non-claims

The demonstrator must explicitly state that it does **not** establish:

- scientific validity of TGCV;
- causal validity in the empirical world;
- generality across EV–grid systems;
- superiority over optimisation/control methods;
- predictive accuracy;
- value creation or ROI;
- industrial readiness;
- deployment readiness;
- real-world policy effectiveness;
- a unique explanation of EV–grid coordination.

## 15. Execution gates

Before execution, the following must all pass:

**G1 — Specification integrity:** this frozen specification is unchanged.

**G2 — Fixture completeness:** all numerical capacities, EV states, transformation parameters and policy rules are frozen.

**G3 — Universe completeness:** every candidate transformation is explicitly listed in `Uτ`.

**G4 — Predicate independence:** no `Pτ` rule references downstream outcome or future trajectory.

**G5 — Baseline equivalence:** conventional baseline uses the same information scope and action universe.

**G6 — Negative-control completeness:** NC1 and NC2 are fully specified.

**G7 — Reproducibility:** execution environment, seed policy if applicable, hashes and output schema are fixed.

**G8 — Authorization:** a separate execution authorization artifact explicitly permits the run.

No run should begin merely because this specification exists.

## 16. Expected evidentiary disposition

Possible outcomes are intentionally non-ranked:

- **RECONSTRUCTION-EQUIVALENT:** TGCV-style and conventional representations encode substantially the same information for the bounded case;
- **ADDITIONAL-STRUCTURAL-INFORMATION:** TGCV-style representation exposes a reproducible cross-domain relation not equivalently represented by the baseline;
- **NON-DISCRIMINATING:** the comparison cannot distinguish the representations under the bounded protocol;
- **BLOCKED:** one or more execution gates fail.

None of these outcomes, by itself, constitutes scientific validation of TGCV.

## 17. Governance boundaries

This specification does not modify:

- TGCV Core;
- RMA;
- Evidence→Claim Matrix;
- STATUS;
- C09;
- previous scientific evidence.

It does not authorize reopening TSTC or TR-132.

## 18. Next controlled step

The next controlled operation is **fixture construction and preflight only**. Execution remains prohibited until G1–G8 are satisfied and a separate execution authorization gate is recorded.
