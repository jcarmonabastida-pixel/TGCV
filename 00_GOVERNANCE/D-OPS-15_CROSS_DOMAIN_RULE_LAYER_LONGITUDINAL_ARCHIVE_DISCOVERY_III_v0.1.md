# D-OPS-15 — Cross-Domain Rule-Layer + Longitudinal-Archive Discovery III v0.1

**Status:** CLOSED — ETHEREUM / BLOCKCHAIN RETAINED AS PRIMARY CANDIDATE FOR IDENTIFIABILITY AUDIT
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Purpose

Extend cross-domain discovery after the railway public-history blocker and the legal/regulatory `P_tau` circularity blocker.

The stricter filter is:

1. independently governed formal rule layer;
2. public longitudinal state archive;
3. stable state/object identity;
4. independently enumerable transformation universe U_tau;
5. non-circular pre-execution P_tau;
6. downstream Reach distinguishable from T_acc;
7. reproducible public evidence.

## 2. Historical reconstruction

The current TGCV evidence matrix identifies independent replication/cross-domain generalisation as the highest-information open direction. RUST-DYN-2 remains E1 only within its frozen Rust operationalization. Existing cross-domain reconstruction already establishes the formal schema but does not constitute independent empirical replication.

Previous discovery blockers:

- Process mining: observed traces could not provide an independent U_tau/P_tau.
- ABAC/cybersecurity: public reproducibility and independent policy semantics were insufficient.
- Configurable software: operationally strong but too close to software/configuration semantics.
- Protein evolution: P_tau became either trivial or outcome/fitness-dependent.
- Power grid: electrical feasibility variables absent from public topology state.
- Railway/RINF: rule layer strong, but historical public state retrieval for a second comparable state was not demonstrated.
- Legal/regulatory: historical archive and rule layer strong, but independent non-circular U_tau/P_tau remained unresolved.

Therefore this search prioritizes domains whose rule system itself defines valid state transitions.

## 3. Candidate A — Ethereum transaction/state-transition system

### Rule layer

Ethereum is explicitly specified as a transaction-based state machine. The Yellow Paper defines a state transition function `sigma_(t+1) = Upsilon(sigma_t, T)` and distinguishes valid state transitions from invalid state changes. Transaction validity includes independently specified protocol conditions such as encoding validity, signature validity, nonce validity, sender constraints and gas requirements.

The Ethereum consensus specifications are versioned by protocol upgrade/fork, with stable specifications for Phase0, Altair, Bellatrix, Capella, Deneb, Electra and Fulu. Reference tests are also published.

### Longitudinal state archive

Ethereum archive nodes are explicitly defined as archives of all historical states. Blocks and transactions form the historical journal from which states are deterministically reconstructed. Historical state queries are a standard use case of archive nodes.

### TGCV mapping candidate

`S_t` = canonical Ethereum execution state at a declared block/transaction boundary.

`U_tau` = typed candidate protocol transactions/operations independently enumerated from the transaction grammar and protocol operation types.

`P_tau(S_t,C_t,L)` = protocol validity/admissibility of the candidate transaction under the applicable fork rules and the pre-state, excluding whether the transaction was actually included in a block and excluding downstream outcomes.

`T_acc,t` = valid candidate transactions/operations from the frozen universe under the pre-state.

`Reach` = successor execution states/configurations produced by valid candidate transformations under a declared horizon.

`Trajectory` = sequence of successor states under successive valid transformations.

### Key unresolved issues

1. The candidate universe `U_tau` must not be defined merely as transactions historically observed on-chain. It must be independently generated from the protocol transaction/operation grammar.
2. `P_tau` must be evaluated without using historical inclusion, gas-price success, receipts, logs, balances after execution or other downstream outcomes.
3. Candidate transaction space is potentially enormous. A deterministic bounded universe/profile must be frozen before empirical execution.
4. State identity must be canonical and fork-aware.
5. The boundary between accessibility and actual execution is unusually clean conceptually, but must be operationalized carefully: a valid transaction need not have been submitted or included.

### Preliminary assessment

- domain independence: PASS
- formal rule layer: PASS
- public longitudinal state archive: PASS
- state transition semantics: PASS
- independent U_tau: CONDITIONAL
- non-circular P_tau: CONDITIONAL/PROMISING
- stable state identity: PASS/CONDITIONAL, fork-aware
- reproducibility: PASS in principle
- information gain beyond Rust: HIGH

**Disposition: RETAIN — PRIMARY CANDIDATE.**

## 4. Candidate B — Machine-readable standards / geospatial constraint systems

OGC's current machine-readable standards work provides formal schemas, SHACL/Schematron/JSON-path constraints and executable conformance rules. This is a strong rule layer.

However, the public evidence found does not yet establish a sufficiently strong longitudinal archive of independently versioned real-world states with stable object identity suitable for direct `Delta T_acc` reconstruction.

**Disposition: RETAIN AS SECONDARY, NOT SELECTED.**

## 5. Candidate C — Scientific/clinical conformance datasets

CDISC CORE provides machine-executable conformance rules and a rule engine. The rule layer is strong and independently specified. However, the available evidence does not establish a public longitudinal sequence of comparable real study states whose transformation universe can be defined independently of observed data corrections or outcomes.

**Disposition: NOT SELECTED.**

## 6. Decision matrix

| Criterion | Ethereum | OGC/geospatial | CDISC/clinical |
|---|---|---|---|
| Independent domain | PASS | PASS | PASS |
| Formal rule layer | PASS | PASS | PASS |
| Public longitudinal state archive | PASS | CONDITIONAL | CONDITIONAL |
| Stable state identity | PASS/COND. | CONDITIONAL | CONDITIONAL |
| Independent U_tau | CONDITIONAL | CONDITIONAL | CONDITIONAL |
| Non-circular P_tau | CONDITIONAL/PROMISING | CONDITIONAL | CONDITIONAL |
| Downstream Reach | CONDITIONAL | CONDITIONAL | CONDITIONAL |
| Reproducibility | PASS | PASS | PASS |
| Information gain beyond Rust | HIGH | HIGH | MEDIUM/HIGH |
| Selection | **PRIMARY** | Secondary | Reject for now |

## 7. Scientific decision

**D-OPS-15 = CLOSED — ETHEREUM RETAINED AS PRIMARY EXTERNAL-DOMAIN CANDIDATE.**

This is a candidate-selection decision, not an empirical result and not a claim that Ethereum satisfies the TGCV architecture.

The decisive advantage is structural: the domain has an explicit formal state-transition rule system and an independently maintained public history of states. This combination was missing or blocked in the previously audited candidates.

## 8. Next controlled operation

**D-OPS-18 — Ethereum Transaction Universe & Pre-Execution Admissibility Identifiability Audit.**

The audit must establish before any dataset execution:

1. a finite, independently defined `U_tau`;
2. a canonical transaction/operation identity;
3. a pre-execution `P_tau` that excludes historical inclusion and downstream outcomes;
4. a canonical state boundary and fork rule;
5. exact `T_acc` construction;
6. a downstream successor/Reach definition that does not collapse into observed blockchain history;
7. an explicit computational-feasibility bound.

If these conditions fail, Ethereum is rejected and discovery resumes.

**REAL-DATA EXECUTION AUTHORIZED: NO.**

## 9. Sources

- Ethereum Yellow Paper / state transition formalization: https://ethereum.org/content/developers/tutorials/yellow-paper-evm/yellow-paper-berlin.pdf
- Ethereum Consensus Specifications: https://github.com/ethereum/consensus-specs
- Ethereum Execution APIs: https://github.com/ethereum/execution-apis
- Ethereum archive nodes / historical state: https://ethereum.org/developers/docs/nodes-and-clients/archive-nodes
- Ethereum Whitepaper / state transition overview: https://ethereum.org/whitepaper/
- OGC machine-readable standards and executable constraints: https://docs.ogc.org/techpaper/26-021/26-021.html
- CDISC CORE / Open Rules: https://www.cdisc.org/core
