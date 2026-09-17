# TGCV — WP2-C05 Energy–Mobility / EV-Grid Deep-Screen 001

**Status:** PROVISIONAL — COUPLING-CANDIDATE / RECONSTRUCTION INCOMPLETE
**Date:** 2026-09-17
**Parent screen:** `TGCV_APPLICATION_FIT_WP2_DEEP_SCREENING_001.md`
**Candidate register:** `TGCV_APPLICATION_FIT_WP2_CANDIDATE_REGISTER_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.12 / RMA traceability v3.35

## 1. Evidence boundary

The energy–mobility interface is explicitly treated in current European policy work as an interoperability and data-exchange problem between energy and transport ecosystems. A 2026 European Commission joint report addresses demand-side flexibility, smart charging and bidirectional charging and identifies interoperability, governance and data exchange between the energy and mobility sectors as requirements for grid integration. citeturn0search8turn0search11

Recent research also explicitly models grid-aware EV charging under capacity constraints. A 2026 Energy and AI study integrates public and domestic charging demand, local grid-capacity constraints and cross-site redirection; its policy changes acceptance and redirects charging between sites. citeturn0search0turn0search1 A 2026 Applied Energy study models competition among charging service providers under shared transformer constraints and derives executable charging capacity allocations. citeturn0search3turn0search7 Current research also treats coupled power and transportation networks, including EV spatio-temporal V2G flexibility, as jointly constrained systems. citeturn0search12

These sources establish the cross-domain problem and concrete constraint/resource interactions. They do not establish TGCV constructs, causal evidence for TGCV, or differential value.

## 2. Why C05 is structurally different

C01: federated technical orchestration.

C03: agent/tool/permission action space.

C04: physical asset/digital-twin/maintenance coupling.

C05 introduces **resource coupling and constraint propagation** between two operational domains:

`mobility demand / charging state ↔ electrical network capacity / grid state`

The important feature is that a state change in one domain can alter which transformations are feasible in the other domain, while the reverse can also occur.

This creates a potentially bidirectional transformation-space coupling rather than a one-way dependency.

## 3. Decision-time boundary

A clean boundary is a charging-management decision point immediately before a charging acceptance, scheduling, throttling, redirection, V1G or V2G action is selected.

Frozen information should include:

- EV arrival/queue/session state;
- requested energy and departure constraints;
- charging-site state;
- local transformer/feeder capacity;
- current and forecast grid load;
- electricity/charging constraints and tariff state where relevant;
- available neighbouring charging sites;
- EV-to-grid capability where applicable;
- mobility constraints such as acceptable detour/time;
- network/operator policies.

This is compatible with current research representations that combine charging demand with local grid constraints and cross-site coordination. citeturn0search0turn0search3

## 4. Candidate state representation

A bounded screening representation is:

`S_t = {EV/charging configuration, site configuration, grid configuration}`

`C_t = {current/forecast demand, queue state, grid capacity, mobility requirements, tariffs/policies, available sites, V1G/V2G capability}`

`L = {grid safety limits, charging-service rules, mobility constraints, contractual/operator constraints}`

This is an analytical TGCV representation, not a claim about any specific EV charging platform's internal ontology.

## 5. Candidate transformations

A finite synthetic `Uτ` can contain:

- accept charging at site A;
- defer charging;
- reduce charging power;
- shift charging to another time window;
- redirect an EV to site B;
- redirect a subset of demand across sites;
- discharge to grid where V2G is available;
- charge from grid at a different rate;
- switch between charging modes;
- reserve/release charging capacity;
- reject a request under defined constraints.

The candidate space should remain deliberately finite. The objective is not to model every mobility or power-system action.

## 6. Accessibility hypothesis

C05 provides the clearest resource/constraint propagation hypothesis so far:

`grid state / mobility state / shared resource state`
→ `admissibility of charging/mobility transformations`
→ `T_acc`
→ `subsequent energy + mobility trajectory`.

Examples:

`transformer capacity becomes constrained`
→ high-power simultaneous charging becomes inadmissible
→ throttling/defer/redirection remain accessible.

`neighbouring site capacity becomes available`
→ redirection transformation becomes admissible
→ a different charging trajectory becomes accessible.

`EV departure requirement becomes tighter`
→ some delayed charging transformations become inadmissible
→ alternative sites or charging rates may become necessary.

`V2G capability becomes available`
→ discharge-to-grid transformations become admissible
→ the system's accessible energy-management space expands.

Formally:

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`.

A controlled transition in grid or mobility state should then produce a measurable difference between `T_acc,t` and `T_acc,t+1`.

## 7. Bidirectional coupling

C05 is particularly useful because coupling can potentially operate in both directions:

`grid → mobility`

Grid congestion can close or restrict charging transformations.

and:

`mobility → grid`

EV demand concentration can close or restrict grid operating transformations or consume shared capacity needed for other grid actions.

This can be represented as:

`ΔS_energy → ΔT_acc,mobility`

and

`ΔS_mobility → ΔT_acc,energy`.

The existence of such constraints is already well represented in conventional optimisation/control literature. The TGCV-specific question is whether the **change in accessible transformation space** provides a useful common abstraction across the two domains.

## 8. Multidomain coexistence vs transformational coupling

Unlike a generic system containing transport and energy data, this case has an explicit physical coupling mechanism: shared capacity and demand constraints. Current research explicitly models these interactions, including shared transformer limits, cross-site redirection and coupled power/transport operations. citeturn0search0turn0search3turn0search12

Therefore the **coupling hypothesis is structurally stronger here** than simple multidomain coexistence.

However, the stronger hypothesis still needs discrimination from established formulations such as:

- constrained optimisation;
- model predictive control;
- network flow/capacity models;
- demand-response control;
- game-theoretic resource allocation;
- multi-agent reinforcement learning;
- V1G/V2G scheduling.

## 9. Critical TGCV discrimination test

The question should be framed narrowly:

> Does a TGCV transformation-space representation expose a reusable cross-domain state-transition property that is not equivalently visible in the conventional constraint/optimisation representation?

This is deliberately stricter than asking whether TGCV can describe the system.

A conventional optimisation model may already encode exactly which actions are feasible under capacity constraints. If so, merely renaming the feasible-action set `T_acc` does not establish differential value.

The possible additional contribution would have to concern **trajectory implications of changing accessibility**, especially when one domain's state transition changes the future action space of another domain and that effect propagates through subsequent decisions.

## 10. Minimum next proof

**EV–Grid Cross-Domain Transformation Mapper — synthetic bounded benchmark.**

Use:

1. two charging sites;
2. one simplified distribution-grid capacity constraint;
3. finite EV arrival/session states;
4. finite charging transformations;
5. explicit mobility/detour constraints;
6. outcome-independent `Pτ` predicates;
7. `T_acc,0` reconstruction;
8. one controlled grid-capacity transition;
9. `T_acc,1` reconstruction;
10. one controlled mobility-demand transition;
11. `T_acc,2` reconstruction;
12. downstream trajectory simulation;
13. conventional constrained-optimisation baseline;
14. comparison of represented accessibility changes and trajectory implications.

A minimal intervention matrix can use:

| Factor | State 0 | State 1 |
|---|---|---|
| Grid capacity | available | constrained |
| EV demand | low | high |
| Neighbour capacity | available | unavailable |
| Departure constraint | relaxed | tight |

The experiment should vary one factor at a time before testing combined transitions.

## 11. Why C05 may be a stronger demonstration candidate

The candidate has three useful properties:

1. **Explicit coupling:** shared grid capacity directly constrains mobility-side transformations.
2. **Bidirectionality:** mobility demand can also alter energy-side possibilities.
3. **Finite reconstruction:** a small synthetic system can enumerate candidate charging transformations without requiring a realistic national-scale model.

This makes C05 a particularly suitable candidate for an Applied Demonstration Cycle.

But these properties also make the conventional baseline unusually strong. The burden for showing differential TGCV contribution is therefore correspondingly high.

## 12. Maturation route

**Primary route: Applied Demonstration.**

The smallest useful artefact is a synthetic two-site EV-grid mapper, not a production charging optimiser.

A scientific route could follow if the mapper identifies a generalisable transformation-space/trajectory property that survives comparison with constrained optimisation and control representations.

No operational deployment or value claim is implied.

## 13. Current disposition

**WP2-C05 — COUPLING-CANDIDATE.**

Reason: C05 presents the clearest structural example so far of resource coupling and constraint propagation across domains. Current literature explicitly models the relevant energy–mobility coupling, including capacity constraints and cross-site transformation alternatives. citeturn0search0turn0search3turn0search12

At the same time, conventional optimisation/control models already represent feasible action spaces under constraints. Therefore C05 is **not evidence of differential TGCV value**. Its importance for WP2 is as a demanding discrimination case.

## 14. Cross-case observation after C01–C05

Across four screened cases, the same candidate abstraction now appears as:

- C01: orchestration-induced accessibility changes;
- C03: permission/tool-induced accessibility changes;
- C04: physical/resource-induced maintenance accessibility changes;
- C05: shared-resource/constraint-induced energy–mobility accessibility changes.

This recurrence increases the value of testing the abstraction systematically, but it does not by itself validate TGCV. The next case, **C08**, changes the structure again by introducing institutional authority and inter-organisational workflow constraints.

**Next case:** WP2-C08 — Cross-agency public-service / criminal-justice digital transformation.
