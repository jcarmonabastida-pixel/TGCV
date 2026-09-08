# D-OPS-3 — Alternative External Domain Compatibility Audit v0.1

**Status:** CLOSED — NO DOMAIN SELECTED  
**Date:** 2026-09-08

## 1. Decision

The three D-OPS-3 candidates were audited against D2-1…D2-12.

**Decision: NO SELECTION.**

None currently satisfies the minimum rule for an independent empirical TGCV replication.

This is a bounded rejection of the present candidates, not a rejection of TGCV and not a claim that these domains are intrinsically unsuitable.

## 2. Candidate A — Process mining / operational workflows

Public process-mining repositories provide numerous event logs, including BPI Challenge logs, hospital logs and traffic-fine management logs. This establishes reproducible data availability. However, the event logs primarily record observed executions/traces. urlIEEE Task Force on Process Mining event-log cataloguehttps://www.tf-pm.org/resources/logs

| Criterion | Result | Finding |
|---|---|---|
| D2-1 independence | PASS | Materially different empirical object from Rust package evolution. |
| D2-2 S observability | CONDITIONAL | Case/event state can be reconstructed, but depends on log semantics. |
| D2-3 C/L observability | CONDITIONAL | Context exists in some logs but is dataset-specific. |
| D2-4 independent Uτ | FAIL | Event logs expose observed activities; enabled/possible actions are not independently observed. |
| D2-5 τ identity | CONDITIONAL | Event/activity identity is available. |
| D2-6 pre-execution Pτ | FAIL | Deriving admissibility from observed traces risks circularity. |
| D2-7 T_acc | FAIL | Cannot currently construct a defensible upstream T_acc independently of observed execution. |
| D2-8 ΔT_acc | FAIL | Consequently no non-circular temporal comparison. |
| D2-9 Reach | CONDITIONAL | Reach/trajectory can be reconstructed from traces, but this does not solve upstream accessibility. |
| D2-10 reproducibility | PASS | Public event-log catalogues are available. |
| D2-11 firewall | FAIL | Execution traces are themselves the primary data; separating accessibility from observed execution is not presently demonstrated. |
| D2-12 falsifiability | PASS | Formal falsifiers exist, but upstream identifiability fails. |

**Disposition: REJECTED FOR CURRENT EMPIRICAL SELECTION.**

## 3. Candidate B — Cybersecurity / access-control policy systems

Recent work demonstrates contextual access-event representations containing role, resource, location, time and action, together with expected accept/reject decisions. However, the cited 2026 dataset transformation work states that the resulting data are to be made available on request, weakening immediate reproducibility. More importantly, accept/reject labels are downstream decision information and cannot define upstream accessibility. citeturn0search9

| Criterion | Result | Finding |
|---|---|---|
| D2-1 independence | PASS | Distinct from Rust dependency evolution. |
| D2-2 S observability | PASS | Resource/policy context can be represented. |
| D2-3 C/L observability | PASS | Role, resource, location, time and action provide rich context. |
| D2-4 independent Uτ | CONDITIONAL | Candidate actions can define Uτ, but policy/data coverage must be frozen. |
| D2-5 τ identity | PASS | Action/resource identity can be canonicalized. |
| D2-6 pre-execution Pτ | CONDITIONAL | Possible in principle from policy rules, but requires a dataset exposing policy semantics independently of accept/reject outcomes. |
| D2-7 T_acc | CONDITIONAL | Potentially strong, but not demonstrated from a currently reproducible public dataset. |
| D2-8 ΔT_acc | CONDITIONAL | Policy-version comparison is possible in principle. |
| D2-9 Reach | CONDITIONAL | Successor access/configuration semantics require a separate frozen construction. |
| D2-10 reproducibility | FAIL | Current identified dataset availability is on-request rather than directly reproducible. |
| D2-11 firewall | CONDITIONAL | Accept/reject and observed activity can be firewalled, but this must be proven by the actual dataset. |
| D2-12 falsifiability | PASS | Strong potential falsifiers exist. |

**Disposition: REJECTED FOR CURRENT EMPIRICAL SELECTION; RETAIN AS FUTURE CANDIDATE.**

## 4. Candidate C — Configurable software systems / software product lines

This domain has strong empirical infrastructure. A published study analyzes 190 releases of 12 configurable real-world systems and their configuration spaces over time. A public community dataset provides configurable-system artifacts including feature models, source code, tests and configurations. Recent work also reports a curated dataset spanning Linux kernel versions and large configuration spaces. citeturn0search1turn0search2turn0search10

However, the literature is unusually close to the TGCV architecture: feature models define configuration spaces, configuration evolution is explicitly studied, and formal work already treats configuration evolution and update operations. citeturn0search0turn0search5

| Criterion | Result | Finding |
|---|---|---|
| D2-1 independence | CONDITIONAL | Different from Rust dependency evolution, but remains within software configuration/evolution. |
| D2-2 S observability | PASS | Feature/configuration state is directly representable. |
| D2-3 C/L observability | PASS | Feature constraints and configuration rules can be represented. |
| D2-4 independent Uτ | PASS | Candidate feature/configuration transformations can be defined independently of observed performance. |
| D2-5 τ identity | PASS | Feature/configuration operations can receive canonical identities. |
| D2-6 pre-execution Pτ | PASS | Configuration validity/constraint satisfaction can be evaluated before product execution. |
| D2-7 T_acc | PASS | A formally defined accessible transformation set is feasible. |
| D2-8 ΔT_acc | PASS | Feature-model/configuration evolution supplies temporal comparison points. |
| D2-9 Reach | PASS | Successor configurations can be represented independently from transformation identity. |
| D2-10 reproducibility | PASS | Multiple public datasets exist. |
| D2-11 firewall | PASS | Performance/outcome data can be excluded from accessibility construction. |
| D2-12 falsifiability | PASS | Non-redundancy, persistence and collapse cases can be constructed. |

**Disposition: CONDITIONALLY ADMISSIBLE, BUT NOT SELECTED.**

The decisive blocker is D2-1/D2-12 at the scientific-information-gain level: the domain is so close to existing software configuration/evolution theory that a second empirical result could reproduce the same architectural phenomenon without materially increasing transversal evidence. Prior work explicitly studies configuration spaces and their evolution. citeturn0search0turn0search5

## 5. Comparative decision

| Candidate | Minimum rule | Main blocker | Decision |
|---|---|---|---|
| Process mining | FAIL | Uτ/Pτ cannot currently be separated from observed traces | REJECT |
| Cybersecurity / ABAC | FAIL | Current reproducibility + policy-semantics availability | REJECT / RETAIN |
| Configurable software | CONDITIONAL | High semantic proximity / limited cross-domain information gain | NOT SELECTED |

## 6. Scientific conclusion

The current candidate search has not produced a sufficiently independent, reproducible and non-circular second empirical domain.

This strengthens rather than weakens the governance conclusion: **do not force a second domain merely to obtain replication.** The current Rust result remains E1, while C11 domain-independence remains H.

The evidence-to-claim matrix therefore remains unchanged:

- C03–C07: E1 within Rust operationalization;
- C11 domain independence: H;
- C13 originality: O;
- causal/predictive/value claims: H.

## 7. Next controlled operation

Open a broader but still bounded **D-OPS-4 — Cross-Domain Discovery Search**, explicitly seeking a domain outside software configuration, process logs and access-control systems, with priority on an observable rule-governed system where admissible transformations can be specified before execution and a public longitudinal dataset exposes the relevant state/context.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
