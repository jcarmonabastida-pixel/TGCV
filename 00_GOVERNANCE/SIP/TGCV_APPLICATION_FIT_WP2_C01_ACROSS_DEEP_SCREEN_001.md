# TGCV — WP2-C01 ACROSS Deep-Screen 001

**Status:** PROVISIONAL — COUPLING-CANDIDATE / RECONSTRUCTION INCOMPLETE
**Date:** 2026-09-17
**Parent screen:** `TGCV_APPLICATION_FIT_WP2_DEEP_SCREENING_001.md`
**Candidate register:** `TGCV_APPLICATION_FIT_WP2_CANDIDATE_REGISTER_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.12 / RMA traceability v3.35

## 1. Evidence boundary

ACROSS is a completed EU-funded project (grant agreement 101097122; project period 2023-01-01 to 2025-12-31). CORDIS describes an end-to-end service-management platform based on distributed domain-level orchestrators overseen by a cloud-managed multi-domain orchestrator, with deep telemetry, AI-driven intelligence, cross-domain zero-touch provisioning and secure/trusted orchestration across heterogeneous cloud-edge deployments. CORDIS also reports an ESO-L and DO-L, AI-based traffic classification/DDoS detection/SLA management, a Network Digital Twin, telemetry for network and compute resources, and security mechanisms including DDoS mitigation and secure container migration. [External evidence: CORDIS project and results pages, retrieved 2026-09-17.]

These facts establish a technically multidomain architecture and documented cross-domain orchestration capability. They do **not** by themselves establish a TGCV `T_acc` or `ΔT_acc` result.

## 2. Decision-time boundary

A useful TGCV screening boundary is an orchestration decision at time `t`, before a concrete zero-touch provisioning/reconfiguration action is selected.

The relevant frozen information would include:

- network/service state;
- compute/edge state;
- telemetry and AI-derived event state available at the decision point;
- security/trust state;
- service/SLA requirements;
- currently deployed domain orchestrators and their interfaces;
- applicable policies and resource constraints.

This boundary is conceptually reconstructable from the architecture description, but the public material reviewed here does not provide one frozen, fully specified decision instance sufficient for an empirical `T_acc,t` reconstruction.

## 3. Candidate state representation

A bounded analytical representation is:

`S_t = {network configuration, compute/edge configuration, deployed services, security/trust configuration}`

`C_t = {telemetry/events, SLA/service requirements, policies, resource constraints, orchestration interfaces}`

`L = {platform and domain-level admissibility rules}`

This is a screening abstraction, not a claim about ACROSS's native ontology.

## 4. Candidate transformations

Concrete candidate transformations suggested by the documented architecture include:

- deploy or provision a service across available network/compute resources;
- instantiate or migrate a container/VNF;
- modify routing or service placement;
- apply DDoS mitigation;
- modify a service configuration in response to telemetry/AI events;
- alter resource allocation to satisfy service/SLA constraints;
- perform trusted orchestration when attestation/security conditions are satisfied.

These are **candidate transformations inferred from documented functions**. They are not yet a verified enumeration of `U_τ`.

## 5. Accessibility/admissibility hypothesis

The potentially TGCV-relevant mechanism is not simply that ACROSS coordinates several domains. The stronger hypothesis is:

`change in domain state / security / resource constraint → change in admissibility of a concrete transformation → change in accessible transformations in another domain`

For example, if an edge/resource/security state changes such that a service placement or secure migration becomes admissible in one domain, while an alternative placement becomes inadmissible, then the accessible transformation space of the coupled system changes.

Formally, the target reconstruction would be:

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`

followed by a transition to `(S_t+1,C_t+1)` and comparison with `T_acc,t+1`.

## 6. What the current evidence supports

The CORDIS material explicitly reports cross-domain zero-touch provisioning, programmable hooks driven by raw telemetry and AI-processed events, and intertwined network/compute system states. This makes a **transformational-coupling interpretation structurally plausible** rather than merely naming several coexisting technologies.

However, the available public summary does not yet identify a single frozen event sequence of the form:

`state A → domain transition → admissible transformation changes → state B`

with enough detail to establish `ΔT_acc` independently of subsequent performance or outcome.

Therefore the current result is **COUPLING-CANDIDATE**, not a qualified TGCV application or scientific evidence.

## 7. Multidomain coexistence vs transformational coupling

### Coexistence explanation

ACROSS could be represented entirely as a sophisticated orchestration architecture in which several domain controllers exchange information and coordinate resource/configuration decisions. Under this explanation, multidomain presence does not require a distinct TGCV layer.

### Coupling explanation

A stronger interpretation becomes justified only if a domain transition changes the set of transformations that another domain can legitimately or technically perform. Examples would include:

`security state → secure-migration admissibility`

`edge-resource state → service-placement admissibility`

`network state → feasible service configuration/routing transformations`

`SLA state → admissible resource-allocation transformations`

The discriminating issue is therefore not whether the domains interact, but whether their interaction changes the **space of subsequently accessible transformations**.

## 8. Alternative-explanation test

At present, ordinary concepts from network orchestration, policy-driven automation, resource management, workflow/event processing and control can describe much of the documented ACROSS architecture.

TGCV would add analytical differentiation only if the same case can be represented through a common transformation-space construct that makes an otherwise hidden cross-domain change in future accessibility explicit and testable.

This remains unresolved.

## 9. Minimum next proof

The smallest useful Applied Demonstration is a synthetic **ACROSS Cross-Domain Transformation Mapper** with two or three coupled domains, for example:

`network ↔ compute/edge ↔ security`

The mapper should define:

1. a frozen initial state `S0,C0`;
2. a finite candidate transformation catalogue `Uτ`;
3. explicit outcome-independent admissibility predicates `Pτ`;
4. initial `T_acc,0`;
5. one controlled state/constraint transition in a single domain;
6. reconstructed `T_acc,1`;
7. the cross-domain transformations newly opened, closed or reordered;
8. a downstream trajectory generated from the changed accessibility structure;
9. a baseline representation using conventional orchestration/workflow concepts;
10. a record of what explanatory information is added by the transformation-space representation.

The decisive comparison is not performance of the demo but whether the TGCV representation identifies a cross-domain accessibility change that the baseline representation does not already expose equivalently.

## 10. Current disposition

**WP2-C01 — COUPLING-CANDIDATE.**

Reason: ACROSS provides unusually explicit evidence of federated multi-domain orchestration and cross-domain zero-touch provisioning, including coupled network/compute state and event-driven actions. The public evidence is sufficient to motivate the transformational-coupling hypothesis, but insufficient to reconstruct an empirical `ΔT_acc` instance.

**Maturation route:** Applied Demonstration first; scientific route remains conditional.

**No claim upgrade:** This screen does not modify Core, RMA, Evidence→Claim Matrix, C09, or any existing scientific result.

## 11. Next case

Proceed to **WP2-C03 — Production AI agents / Coupa Sentinel on AWS**, using the same reconstruction template. Its structural contrast is important because the candidate accessibility space is an agent's action/tool space rather than a federated network orchestration space.
