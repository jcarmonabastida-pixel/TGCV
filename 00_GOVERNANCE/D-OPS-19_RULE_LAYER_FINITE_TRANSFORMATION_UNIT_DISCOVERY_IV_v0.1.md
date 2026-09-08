# D-OPS-19 — Rule-Layer + Finite Transformation-Unit Discovery IV v0.1

**Status:** CLOSED — NO EXECUTION-READY EXTERNAL DOMAIN SELECTED
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Purpose

Extend cross-domain discovery after the Ethereum failure identified by D-OPS-18.

The decisive new filter is **transformational-unit identifiability**:

> A candidate domain must provide an independently governed rule layer from which a finite, canonical and computationally tractable transformation universe U_tau can be defined before observing which transformations actually occurred.

It must also provide a public longitudinal state archive sufficient to compare T_acc across time.

## 2. Historical reconstruction

Current governance state:

- RUST-DYN-2 provides E1 evidence only within the frozen Rust operationalization.
- Cross-domain formal reconstruction is already established; no new literature gate is required.
- Railway failed primarily on public longitudinal-state retrieval.
- Legal/regulatory failed on independent non-circular U_tau/P_tau.
- Ethereum failed because the protocol rule layer is strong, but the unconstrained transaction universe is too large and historical-transaction restriction would be circular.

Therefore D-OPS-19 must search for domains where the transformation primitive is naturally finite or finitely parameterizable.

## 3. Candidate A — Classical planning / PDDL

Public PDDL benchmark collections provide formal domain descriptions and problem instances. The PDDL operator/action schema explicitly contains parameters, preconditions and effects, and planning semantics define applicable actions and successor states. Public IPC collections cover many domains and are programmatically accessible. Sources include planning.domains and the public IPC benchmark repositories.

Assessment:

- independent domain: PASS
- formal rule layer: PASS
- finite/canonical U_tau: PASS for a frozen grounded planning problem
- non-circular P_tau: PASS
- exact T_acc: PASS
- Reach: PASS
- reproducibility: PASS
- longitudinal real-state archive: FAIL

The problem instances are benchmark initial states, not longitudinal observations of an evolving real system. Consequently this candidate is excellent for **formal/conformance validation** but not a direct independent empirical replication of Rust's longitudinal phenomenon.

**Disposition: RETAIN AS FORMAL VALIDATION CANDIDATE; NOT EMPIRICAL DOMAIN SELECTION.**

## 4. Candidate B — Engineering/product lifecycle configuration

Engineering lifecycle systems expose explicit lifecycle states and rules controlling which transactions are permitted in each state. Product lifecycle documentation confirms that allowed transactions can depend on lifecycle state and engineering version.

However, the publicly available evidence does not establish a sufficiently open longitudinal archive of real product states plus stable object identity and complete transformation histories that can be used without proprietary PLM data.

**Disposition: REJECT FOR PUBLIC EMPIRICAL REPLICATION.**

## 5. Candidate C — Versioned transformation-process ontologies

Public datasets such as TransformON expose multiple public ontology versions describing transformation processes and their products. This provides strong versioned formal representation and a finite vocabulary of modeled process concepts.

However, ontology version changes are changes in the representation/rule artifact itself, not necessarily longitudinal changes in an independently existing transformation system. Using ontology edits as observed system transformations would risk changing the unit of analysis from system evolution to documentation evolution.

**Disposition: REJECT FOR CURRENT EMPIRICAL REPLICATION; RETAIN AS METHODOLOGICAL COMPARISON.**

## 6. Decision matrix

| Candidate | Rule layer | Finite U_tau | Non-circular P_tau | Reach | Longitudinal real state | Decision |
|---|---|---|---|---|---|---|
| PDDL / classical planning | PASS | PASS | PASS | PASS | FAIL | Formal-only |
| Engineering/product lifecycle | PASS | PASS/COND. | PASS/COND. | CONDITIONAL | FAIL | Reject |
| TransformON/versioned ontologies | PASS | PASS | CONDITIONAL | CONDITIONAL | FAIL | Reject |

## 7. Scientific decision

**D-OPS-19 = CLOSED — NO EXECUTION-READY EXTERNAL DOMAIN SELECTED.**

This is not a falsification of TGCV. It establishes that the current public candidate pool still does not simultaneously satisfy:

`independent rule layer + finite U_tau + non-circular P_tau + public longitudinal real-state archive + stable identity`.

The result is scientifically useful because it separates two previously conflated requirements:

1. **formal transformational identifiability**, and
2. **empirical longitudinal identifiability**.

PDDL demonstrates that the first can be achieved very cleanly, but not the second. Railway demonstrates the opposite combination in part. Ethereum demonstrates a strong rule/state combination but fails finite transformation-unit identifiability at the required empirical scale.

## 8. Governance consequence

Do not force a second empirical domain merely to obtain cross-domain replication.

Current evidence therefore remains:

- Rust empirical result: E1, bounded to frozen operationalization.
- Cross-domain generality: H.
- Formal TGCV architecture: established at E0/formal level.
- Independent empirical replication: OPEN.
- Causal, predictive, value and universal claims: OPEN/H.
- Originality: OPEN.

## 9. Next controlled operation

**D-OPS-20 — Formal-to-Empirical Bridge Audit.**

Instead of continuing unconstrained domain search, audit whether a formal domain such as PDDL can supply the missing methodological bridge: a controlled, independently specified transformation universe and accessibility predicate, followed by a separately governed empirical longitudinal source in the same domain or a domain with equivalent state identity.

The audit must determine whether this bridge would constitute legitimate cross-domain evidence or merely formal replication. If it cannot produce genuine longitudinal empirical evidence, the project should explicitly close the external-domain search as **NO EXECUTION-READY DOMAIN CURRENTLY IDENTIFIED** rather than continue candidate churn.

**REAL-DATA EXECUTION AUTHORIZED: NO.**

## 10. Evidence consulted

- Planning.domains public PDDL repository/API.
- Public IPC PDDL benchmark repositories.
- Engineering lifecycle state/transaction documentation.
- TransformON public versioned transformation-process ontology dataset.
