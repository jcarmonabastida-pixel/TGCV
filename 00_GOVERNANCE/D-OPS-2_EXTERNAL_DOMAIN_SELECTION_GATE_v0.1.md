# D-OPS-2 — External Domain Selection Gate v0.1

**Status:** DESIGN / SELECTION GATE — NO EXECUTION AUTHORIZED  
**Date:** 2026-09-08  
**Canonical repository:** `jcarmonabastida-pixel/TGCV`

## 1. Purpose

Select, ex ante and by explicit criteria, a second empirical domain for TGCV after closure of EXT-1.1 Rust / RUST-DYN-2, without recreating work already answered by the literature architecture or silently reusing a semantically incompatible operationalization.

This gate selects a domain for subsequent operational design. It does **not** authorize dataset execution, downloading, sampling, implementation of an executor, or scientific claims beyond the existing evidence state.

## 2. Historical reconstruction prerequisite

The following historical state is treated as canonical input to this gate:

- `01_CORE/architecture/TGCV_ARCHITECTURE_DEVELOPMENT_OPERATIONALIZATION_GATE_v0.1.md`: architecture operationalization target established; next operation was domain operational specification.
- `02_LITERATURE/TGCV_CROSS_DOMAIN_ARCHITECTURE_CLOSURE_CONTRIBUTION_NON_REDUNDANCY_GATE_v0.1.md`: bounded cross-domain architectural closure already established; generic prior-art structures must not be rediscovered as if new.
- `02_LITERATURE/TGCV_REACHABILITY_LINK_TRAJECTORY_SUFFICIENCY_GATE_v0.1.md`: bounded Reach/Trajectory distinction already specified.
- `02_LITERATURE/TGCV_VALUE_LINK_OUTCOME_SUFFICIENCY_GATE_v0.1.md`: Outcome/Value downstream distinction already specified.
- `02_LITERATURE/SLR-1_ORGANIZATIONAL_CAPABILITY_ARCHITECTURAL_COMPARISON_v0.1.md`: organizational capability/opportunity is already represented as a prior-art comparison candidate, but no complete empirical operationalization is thereby established.
- `02_LITERATURE/SLR-1_REACTS_ARCHITECTURAL_COMPARISON_v0.1.md`: reactive/self-adaptive architecture is already represented in prior-art reconstruction; it cannot be treated as independent merely because it is a different software domain.
- Historical Rust Potential Reach work and DR-041/DR-042 established the reusable Rust semantics; this gate must not alter them.
- RUST-DYN-2 is technically closed with primary + mandatory replay and its current evidence is bounded to structural/informational distinguishability in the frozen Rust operationalization.

Historical reconstruction therefore yields: **no second domain is currently execution-ready in the canonical repository**. Selection must precede new empirical work.

## 3. Selection principle

The second domain must maximize **scientific information gain**, not convenience or availability of another dataset.

A candidate is admissible only if it can support an independent operationalization of the same TGCV analytical architecture while remaining sufficiently semantically distinct from Rust and from already absorbed prior-art structures.

## 4. Frozen selection criteria

Score each candidate against the following criteria before any implementation or real-data execution:

| ID | Criterion | Required condition |
|---|---|---|
| D2-1 | Domain independence | Phenomenon is materially different from Rust package dependency evolution. |
| D2-2 | System observability | A defensible system state/domain S can be reconstructed from observed data. |
| D2-3 | Condition observability | C and relevant L conditions can be specified without importing future outcomes. |
| D2-4 | Independent transformation universe | Uτ can be defined independently of observed success/outcome. |
| D2-5 | Canonical transformation identity | τ has a deterministic identity independent of execution outcome. |
| D2-6 | Pre-execution accessibility | Pτ can be evaluated without executing the transformation and without retrospective success labels. |
| D2-7 | T_acc construction | Exact or otherwise formally justified T_acc membership can be reconstructed. |
| D2-8 | ΔT_acc | Temporal or counterfactual comparison of T_acc can be defined without arbitrary selection. |
| D2-9 | Downstream Reach | Reach can be defined independently from T_acc as a successor/configuration object where required. |
| D2-10 | Reproducibility | A stable, versioned, legally accessible and computationally reproducible dataset is realistically obtainable. |
| D2-11 | Information firewall | Future activity, outcome, value and predictive information can be excluded from accessibility construction. |
| D2-12 | Falsifiability | Candidate permits genuine non-trivial falsifiers, including cases where TGCV distinctions collapse. |

### Minimum rule

No candidate may be selected for empirical execution unless **D2-1 through D2-9 and D2-11 are PASS**, and D2-10 is at least operationally viable. D2-12 must be PASS for scientific admissibility.

## 5. Candidate set for first comparison

### Candidate A — Organizational capability / opportunity space

**Rationale:** already present in the SLR architecture as a meaningful cross-domain comparison and potentially independent of software dependency evolution.

**Current state:** prior-art/comparative representation exists; no frozen empirical Uτ/Pτ/dataset protocol exists in the current canonical state.

**Primary risk:** capability/opportunity constructs may become post-hoc explanatory labels unless transformations, admissibility conditions and observable state changes are defined independently.

**Gate implication:** candidate remains viable, but must pass a new operational identifiability test before any dataset work.

### Candidate B — Reactive / self-adaptive systems

**Rationale:** strong relevance to changing accessible transformation/adaptation spaces.

**Current state:** substantial prior-art absorption already exists through the SLR and architecture reconstruction.

**Primary risk:** semantic overlap with existing adaptive/reconfiguration/action-space literature may make an empirical replication low in information gain unless a genuinely independent observable unit and non-circular accessibility predicate can be established.

**Gate implication:** candidate is viable only if independence from already absorbed architectural constructs is demonstrated explicitly.

### Candidate C — Social/communication network domain (historical CollegeMsg candidate)

**Rationale:** historically associated with EXT-1.0 and therefore useful as a candidate for cross-domain testing.

**Current state:** historical candidate only; the prior experiment failed and its canonical current operationalization/dataset compatibility is not established in this gate.

**Primary risk:** interaction/outcome structure can easily make future activity, observed response, or network success leak into accessibility; historical failure must not be bypassed by silently changing semantics.

**Gate implication:** candidate cannot be revived merely by reusing EXT-1.0. It requires explicit historical reconciliation and a fresh domain operational specification if selected.

## 6. Decision procedure

1. For each candidate, reconstruct historical artifacts and unresolved questions.
2. Map the candidate to D2-1…D2-12.
3. Mark each criterion **PASS / CONDITIONAL / FAIL / UNKNOWN** with evidence.
4. Reject convenience-based selection.
5. Prefer the candidate with the largest expected reduction in uncertainty about the TGCV architecture, not necessarily the easiest dataset.
6. If no candidate satisfies the minimum rule, return **NO SELECTION** and open a bounded search for an alternative domain.
7. Selection does not authorize execution. After selection, create a separate domain operational specification and subsequent preflight/authorization gates.

## 7. Prohibited actions during D-OPS-2

- No real dataset execution.
- No sampling.
- No outcome/value/predictive analysis.
- No modification or deletion of historical artifacts.
- No silent reuse of EXT-1.0 semantics.
- No claim that a candidate is novel or absent from prior art.
- No dataset choice based only on availability.
- No authorization of implementation or execution through this document.

## 8. Required output

The closure of D-OPS-2 must contain:

- candidate comparison matrix;
- evidence/provenance for every PASS or FAIL;
- explicit uncertainty list;
- selected domain **or NO SELECTION**;
- scientific-information-gain rationale;
- next controlled operation;
- explicit statement that real execution remains unauthorized.

## 9. Current decision

**OPEN — CANDIDATE COMPARISON REQUIRED.**

No empirical domain is selected by this document alone. The next controlled operation is the completion of the candidate comparison under D2-1…D2-12, followed by a separate decision record if a domain is selected.
