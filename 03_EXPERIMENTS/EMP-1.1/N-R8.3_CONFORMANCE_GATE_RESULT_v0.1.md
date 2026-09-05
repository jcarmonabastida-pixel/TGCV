# N-R8.3 — Conformance Gate Result v0.1

**Status:** PASS / CLOSED  
**Date:** 2026-09-05  
**Parent:** N-R8.2 Operationalisation Specification v0.1  
**Runner:** `N_R8_CONFORMANCE_RUNNER_v0.3`

## 1. Decision

**PASS / CLOSED.**

N-R8.3 implementation and conformance testing are complete. All required conformance checks executed by the frozen runner passed. The implementation is therefore eligible for the next controlled gate, N-R8.4 corpus construction and integrity freeze.

This gate does **not** authorize scientific execution and does not authorize generation of the N-R8 scientific corpus until N-R8.4 is independently frozen and closed.

## 2. Conformance evidence

The user-executed N-R8.3 conformance run returned **21/21 PASS**.

Implementation SHA-256 observed at execution:

`f0301a81a39a8b26c5a5d9a29e95df9b532b1941a545849debf874fe734cf157`

Key checks passed:

- implementation existence;
- deterministic G2 regeneration;
- canonical G2 schema;
- G2 distribution differs from G1;
- representation of all six transformation families;
- unit-step resource semantics;
- resource boundary semantics;
- source-preserving REWIRE semantics;
- normative incidence mapping for all six families;
- component-add and component-remove semantics;
- objective invariance;
- deterministic `T_acc` enumeration;
- R2 dimension = 24;
- empty `T_acc` => 24 zero features;
- deterministic R2;
- independent R2 incidence and resource statistics;
- no learner dependency;
- no result/trajectory dependency;
- no sealed N-R7 result literals;
- implementation hash recordability.

## 3. Normative reconciliation

Before closure, N-R8.2 was explicitly reconciled with clarification N-R8.2.1. The parent specification now incorporates, rather than merely references, the normative semantics for:

- `src(τ)` / `dst(τ)` for every transformation family;
- source-preserving `REWIRE_EDGE(u,v,w)`;
- unit-step `MODIFY_RESOURCE(i,d)` with `d ∈ {-1,+1}`;
- exact 24-dimensional R2 feature ordering;
- empty-`T_acc` zero rule;
- Jaccard and population-standard-deviation conventions.

Reconciled N-R8.2 commit:

`5de365c54316b986b806946b463f7c30e04f6dea`

## 4. Scientific boundary

N-R8.3 establishes implementation/conformance only. It does not establish:

- robustness of the N-R7 predictive signal;
- generator independence;
- causal identification;
- absence of proxy explanations;
- representation independence;
- cross-domain validity;
- historical Cargo equivalence;
- universality of TGCV;
- validation of the full TGCV value chain.

No N-R8 corpus, learner, prediction, outcome, or scientific result is implied by this gate.

## 5. Next permitted gate

The next permitted activity is **N-R8.4 — controlled corpus construction and integrity freeze**.

N-R8.4 must freeze and independently verify the required G2 corpus and matched-pair constructions, including all specified hashes, schemas, joins, seed separation, matching conditions, provenance, and fail-closed controls before N-R8.5 execution authorization.

**Decision:** N-R8.3 IMPLEMENTATION/CONFORMANCE PASS — CLOSED. SCIENTIFIC EXECUTION REMAINS BLOCKED PENDING N-R8.4 AND N-R8.5.
