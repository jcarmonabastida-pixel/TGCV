# DEC-C10-095 — A/B architecture for C10-S Value scope

**Status:** ACCEPTED — DESIGN-ARCHITECTURE ONLY.  
**Date:** 2026-11-11.  
**Scope:** C10-S / C-Value / synthetic DGP architecture.  
**Approval basis:** explicit user acceptance in the project conversation on 2026-11-11, following review of C10-S-VALUE-MIN-001 and the P179/P182/P183 crosswalk.

## Decision

1. **Variant A remains the unchanged reference DGP.** It preserves the accepted Opción A microdomain and its existing service contract, roster, causal architecture and versioned evidence. No beneficiary, consumer, stakeholder, preference, Value indicator or valuation rule is inferred or added to A.
2. **Variant B is authorized for separate design and specification as a distinct, versioned synthetic DGP extension.** B may introduce an explicitly stipulated synthetic consumer/beneficiary role and its relation to the service and experimental unit, together with pre-Z demand and an ex-ante valuation perspective/criterion. These elements are not yet specified or accepted.
3. A and B must remain separately identifiable and comparable. B must not rewrite, supersede or silently extend A, DEC-C10-068, or the accepted Opción A roster.
4. Results from B can establish at most whether the Analyzer recovers the causal relationship stipulated in B's known synthetic DGP. They do not establish external validity, real-user preferences, real-world Value, or the general empirical claim ΔT_acc→Value.
5. P179 remains controlling: preserve dimension-specific Value and trade-offs during identification; no scalar index or weights by default. P182 and P183 remain transversal contracts for measurement validity/error/invariance and missingness/censoring/identification respectively.
6. A can continue to support accessibility/ΔT_acc, Reach, trajectories and technical Outcomes when their contracts are operationalized. A cannot support a confirmatory claim about contextual Value while Value remains uninstantiated.
7. The architecture decision does not select Value dimensions, beneficiary identity, demand distribution, criterion, scale, indicator, weights, horizon, causal paths, estimand, or DGP parameters. Those require subsequent explicit proposals and acceptance.

## Alternatives considered

- A only: preserves the accepted domain but cannot test ΔT_acc→Value.
- B only or retroactive modification of A: rejected because it would conflate an extension with the accepted reference domain and weaken traceability.
- A plus separately versioned B: accepted because it preserves A while permitting a controlled synthetic test of Value attribution.

## Consequences and required follow-up

- C / C-Value: maintain separate claims for A's technical Outcomes and B's stipulated Value; specify the minimum B contract without inventing choices.
- D: consume the versioned A/B contracts and keep truth-generation separate from Analyzer-visible evidence; do not infer a schema before semantic closure.
- E: integrate only after A/B contracts, estimands, measurement and adjudication are explicit; preserve separate result provenance by variant.
- Update the C10-S master, Decision Log, plan, Value reconciliation matrix and Closure Control Matrix consistently.
- Retain P179/P182/P183 and §224 as governing contracts.
- MED-02 and MED-03 remain OPEN. No Design Freeze, implementation, fixtures, simulation or scientific execution is authorized.

**State flags:** architecture A/B accepted; B substantive DGP specification OPEN; operationalization OPEN; implementation NOT AUTHORIZED; scientific_execution=false; execution_authorized=false.
