# Dual-graph adaptation matrix 001 — current prototype to proposed contract

**Status:** design/audit artifact; no implementation authorized.  
**Branch:** `design/condition-evaluator-contract-001-20261021`  
**Purpose:** map the minimal dual-graph contract to the current prototype, distinguish reusable behavior from semantic gaps, and define a bounded implementation sequence.

## 1. Evidence boundary

This matrix was initially based on `CONDITION_EVALUATOR_IMPLEMENTATION_AUDIT_001.md`. A fresh bounded inspection of `main:prototypes/collective_toy/web/index.html` is now recorded in [DUAL_GRAPH_CURRENT_SOURCE_AUDIT_001.md](DUAL_GRAPH_CURRENT_SOURCE_AUDIT_001.md). That audit pins the exact fetched file object by Git blob SHA `6e79802dec5d399638757518dfd2c8b94214613d`; the fetch did not provide the current main HEAD commit, so no HEAD SHA is claimed. The audit is source inspection only; no runtime behavior has changed.

Status meanings:
- **Reported present:** the existing source audit explicitly records this behavior.
- **Design required:** the proposed contract requires it, but the audit does not establish implementation.
- **Reverify:** current source must be checked again before coding.
- **Paused:** explicitly not authorized for implementation at this gate.

## 2. Adaptation matrix

| Area | Current prototype evidence | Target contract | Gap / decision | Status |
|---|---|---|---|---|
| Graph 1: system graph | Existing graph is generated from user input or a loaded example; source audit records state/transition model and conditional-edge labeling | Preserve system states, directed transitions, and conditions in the first graph | Keep this graph's semantics and current entry path; verify current renderer and import/export behavior before edits | Reported present; reverify |
| Condition display | Conditional transitions are labelled `CONDICIÓN NO EVALUADA` | Show execution guards as system-layer information; don't imply evaluation if none occurs | Retain honest unresolved label unless a reviewed Layer B evaluator is separately authorized | Reported present |
| Condition evaluation | Audit says conditional edges are omitted from temporal exploration and concrete execution loop does not evaluate `tr.condition` | Optional system simulation may evaluate explicit conditions only under an approved contract | Do not silently implement as part of the TGCV graph work | Paused |
| Graph 2: TGCV objects | Audit does not establish a distinct transformation-space graph | Separate transformation nodes, typed relations, accessibility snapshots, interactions/rules, and TGCV trajectories | New semantic model and presentation are needed; do not reuse state nodes/transition edges without explicit types | Design required |
| Mapping bridge | No audited evidence of explicit system-to-TGCV mapping records | Every cross-layer correspondence is user-declared or derived by a named/versioned rule | Add traceable mapping representation; absence of mapping must remain unresolved | Design required |
| `T_acc` snapshots | No audited evidence of explicit before/after accessible transformation sets | Represent accessible transformation IDs for a defined system/domain and scenario | Add minimal TGCV model object; don't derive from system edges by default | Design required |
| Accessibility change | No audited evidence of rule-governed `ΔT_acc` | Show before/after sets and a reproducible difference only when declared inputs/rule support it | Derivation logic needed and must expose rule/provenance | Design required |
| Relations and trajectories | Current prototype has system transition exploration/execution, but that is not equivalent to TGCV trajectory semantics | Typed transformation relations and trajectories under an explicit trajectory rule | Keep result types distinct; define permitted relation types before path computation | Design required |
| Provenance | The proposed contract defines illustrative, user-declared, rule-derived, unresolved; current implementation support is not established by the audit | Preserve origin labels and derivation sources through UI and serialization | Add provenance to TGCV inputs/results; verify existing package metadata before deciding placement | Design required |
| Two user routes | Existing example loading exists; separate curated TGCV illustrative route is not established | Offer “explore illustrative example” and “build TGCV graph for my system” without overwriting system data | Reuse example loading only after confirming separation and labels; otherwise add route selection and independent model state | Partial / reverify |
| Stale results | Audit says model identity includes full input model and hashes it | Mark TGCV-derived outputs stale when relevant inputs/rules change | Reuse hash/version invalidation only after verifying dependency coverage; a changed hash alone is not a user-facing stale-state design | Reverify |
| Import/export | Audit identifies schema versions v001/v002 and model hashing; package round-trip semantics need further audit | Preserve both graph layers, mapping records, provenance, rules, and version references without reinterpretation | Audit package validation/round-trip before schema design; no migration authorized | Reverify |
| Value display/dashboard | Functional review flags unclear dependence on system paths vs TGCV trajectories vs observer/context | Do not show a TGCV value result until its inputs and semantics are explicit | Separate or suspend existing value display in the dual-graph demonstration unless its meaning is documented | Design decision pending |
| Scientific claims | Existing synthetic tests may exercise implementation only | Clearly state illustrative/model-derived outputs are not empirical TGCV validation | Include user-facing limitation; don't describe toy acceptance as scientific evidence | Required boundary |

## 3. Recommended bounded implementation plan after approval

### Gate A — source re-verification (no behavior changes)

At a pinned main commit, inspect only the relevant source areas:
- model validation and schema dispatch;
- graph renderer and graph data model;
- example loading and user input;
- scenario exploration and concrete execution handlers;
- import/export, package validation, hashing and stale-result handling;
- existing value dashboard and trajectory display.

Record exact file paths, functions/DOM IDs, and current behavior. Avoid a full-tree search or speculative refactor.

### Gate B — separate TGCV data model and presentation

Add a separately typed TGCV model alongside the existing system model on a design branch. First render the two graphs and their provenance with the illustrative case; do not infer TGCV data from system edges. Preserve the existing Graph 1 flow.

### Gate C — one deterministic end-to-end case

Implement the case in `TGCV_FIRST_DEMONSTRATION_CASE_001.md`: declared `T_acc_before={a,b}`, relation `(a,b)`, interaction rule adding `c) and `(b,c)`, then verify `T_acc_after={a,b,c}`, `ΔT_acc={c}`, and newly reachable `[a,b,c]` under the stated example-only trajectory rule.

### Gate D — adversarial and persistence checks

Check semantic type separation, absence of silent mapping, unresolved-rule handling, stale-result invalidation, and export/import preservation. Synthetic CI may establish software-contract conformance only.

### Gate E — reconsider optional condition evaluator

Only after the dual-graph case is accepted, decide whether Layer B condition evaluation is needed for the first useful demonstration. If yes, revisit the earlier typed-condition proposal separately; don't bundle its schema migration with the first TGCV graph implementation without a demonstrated dependency.

## 4. Explicit non-actions

This matrix does not:
- modify `main` or runtime code;
- change the current input schema or package format;
- authorize schema v003 or condition-evaluator implementation;
- alter the TGCV Core;
- run scientific experiments or assert empirical validity.

## 5. Next acceptance gate

Gate A source inspection is documented in [DUAL_GRAPH_CURRENT_SOURCE_AUDIT_001.md](DUAL_GRAPH_CURRENT_SOURCE_AUDIT_001.md). The minimum persistence/stale-result rules are now proposed separately in [DUAL_GRAPH_PERSISTENCE_CONTRACT_PROPOSAL_001.md](DUAL_GRAPH_PERSISTENCE_CONTRACT_PROPOSAL_001.md). Before implementation, review these contracts and decide whether the first increment should be limited to a separately typed TGCV model and second graph renderer, leaving system execution and condition evaluation unchanged. No code should be changed until this design gate is accepted.
