# TGCV — SWIM Uτ / Pτ Formalization Gate

**Date:** 2026-09-11  
**Status:** `PREPARED — NOT EXECUTED`  
**Programme surface:** SIP-L2 / Self-Adaptive Domain Instantiation  
**Domain:** SWIM — Simulator of Web Infrastructure and Management  
**Purpose:** formalize a bounded candidate transformation universe `Uτ` and an independent pre-outcome accessibility predicate `Pτ` before any empirical execution.

## 1. Governance boundary

This document is a G0/G1 methodological gate. It does **not** authorize a SWIM experiment, dataset execution, Docker execution, or empirical claim.

Closed TGCV experiments and evidence surfaces remain closed and are not reopened. Rust/EXT-1.1 is not a candidate domain for new execution.

## 2. Canonical SWIM observations

The SWIM configuration defines an adaptation loop with a 60-second evaluation period, response-time threshold of 0.75 s, maximum 3 servers, initial 3 servers, 5 brownout levels, and deterministic boot delays. The configuration exposes `ReactiveAdaptationManager` and `ReactiveAdaptationManager2` as adaptation-manager variants. These are source-level semantics, not TGCV assumptions.

The `ReactiveAdaptationManager` evaluates pre-decision model state: dimmer factor, active servers, configured servers, maximum servers, utilization and average response time. Its control logic can construct `AddServer`, `SetDimmer(factor)` or `RemoveServer` tactics subject to explicit conditions.

`AddServerTactic` executes `addServer()`. `RemoveServerTactic` executes `removeServer()`. `SetDimmerTactic(factor)` executes `setBrownout(1.0-factor)` and retains the factor as part of tactic identity.

## 3. Bounded candidate transformation universe Uτ

For this gate, `Uτ` is defined as the **candidate transformation identity space**, not as the set of transformations actually selected by the native adaptation manager.

Let a bounded SWIM state be represented by the components relevant to the candidate transformations:

`S_t = (n_t, a_t, d_t, b_t, u_t, r_t, m_t, q_t, ...)`

where:
- `n_t` = configured/known server count relevant to pool state;
- `a_t` = active server count;
- `d_t` = dimmer factor;
- `b_t` = server-booting condition/state;
- `u_t` = utilization observation;
- `r_t` = average response-time observation;
- `m_t` = maximum server count;
- `q_t` = other configuration constraints required by the concrete execution semantics.

The bounded candidate transformation identities are:

1. `τ_add = AddServer`
2. `τ_remove = RemoveServer`
3. `τ_dimmer(k) = SetDimmer(k)`, where `k` is the target dimmer factor representable by SWIM's dimmer-level semantics.

The parameter `k` is part of transformation identity. Therefore `SetDimmer` is not treated as one unparameterized transformation when distinct target factors are possible.

`Uτ = {τ_add, τ_remove} ∪ {τ_dimmer(k) | k ∈ K_SWIM}`

where `K_SWIM` is the finite representable dimmer-factor domain induced by the SWIM model/configuration. Exact cardinality of `K_SWIM` is intentionally not fixed here unless independently established from the model definition.

This definition avoids conflating **candidate existence** with **current accessibility** or **selection**.

## 4. Pre-outcome accessibility predicate Pτ

For each candidate `τ ∈ Uτ`, define:

`Pτ(S_t,C_t) ∈ {0,1,unknown}`

where `C_t` contains the configuration/constraint context available before the transformation is selected or executed.

### 4.1 AddServer

`P_add(S_t,C_t)=1` iff the pre-decision state satisfies the native execution constraints needed for adding a server, in particular:

- no server is currently booting;
- configured/available servers are below `maxServers`.

This predicate is evaluated independently of whether `ReactiveAdaptationManager` actually selects `AddServer`.

### 4.2 RemoveServer

`P_remove(S_t,C_t)=1` iff the pre-decision state satisfies the native execution constraints needed for removing a server, in particular:

- no server is currently booting;
- the server pool permits removal (`servers > 1` in the observed manager logic);
- any additional execution-level constraint required by the concrete SWIM implementation is observable and satisfied.

The response-time condition and spare-utilization condition used by `ReactiveAdaptationManager` to **select** a tactic are not, by themselves, the definition of transformational accessibility. They belong to the native policy-selection layer unless the experiment establishes that they are genuine execution admissibility constraints.

### 4.3 SetDimmer(k)

`P_dimmer(k)(S_t,C_t)=1` iff:

- target factor `k` is representable by the SWIM dimmer configuration/model;
- the corresponding brownout/dimmer transition is executable from the current state;
- no independent execution constraint blocks the transition.

The current manager's use of `dimmer > 0`, `dimmer < 1`, and the discrete `dimmerStep` determines which target factor it proposes in a given policy branch. Those policy conditions must not automatically be promoted to TGCV accessibility conditions.

## 5. Separation required by the gate

The following four predicates/relations must remain distinct:

1. **Candidate existence:** `τ ∈ Uτ`.
2. **Accessibility:** `Pτ(S_t,C_t)=1`.
3. **Policy selection:** the native adaptation manager chooses `τ`.
4. **Outcome:** execution produces `(S_{t+1},C_{t+1})` and measurable consequences.

Therefore:

`τ ∈ Uτ` does not imply `Pτ=1`; `Pτ=1` does not imply selection; selection does not define accessibility; and outcome data must not be used to retroactively define pre-outcome accessibility.

## 6. Non-redundancy test to be applied next

The scientific question is **not** whether TGCV can rename SWIM tactics. It is whether TGCV's explicit representation of candidate transformations plus pre-outcome accessibility adds an analytically distinct object relative to SWIM's native adaptation-space/policy representation.

### PASS condition

A non-redundancy PASS requires at least one distinction expressible as:

`τ ∈ Uτ` + `Pτ(S_t,C_t)`

that is not merely a textual renaming of the native tactic/policy logic, while remaining independently reconstructable from pre-decision state and constraints.

### FALSIFIER

If every TGCV distinction collapses exactly into SWIM's native tactic identities and native admissibility/selection logic, with no independent accessibility representation or analytical gain, then the SWIM instantiation is locally redundant and must not be used as evidence of TGCV non-redundancy.

## 7. Current result

`Uτ = FORMALIZED — BOUNDED`  
`Pτ = FORMALIZED — PRE-OUTCOME / PROVISIONAL`  
`SELECTION ≠ ACCESSIBILITY = PASS`  
`OUTCOME NOT USED TO DEFINE Pτ = PASS`  
`NON-REDUNDANCY = NOT YET TESTED`  
`EXECUTION = NOT AUTHORIZED`

## 8. Next operation

Perform the **SWIM local non-redundancy test**: compare the formal `Uτ/Pτ` representation against the native SWIM adaptation manager and execution semantics. No simulation run is required for this gate.

A failure closes SWIM as a redundant instantiation candidate without affecting TGCV Core. A bounded pass permits the next controlled step toward empirical observability/execution authorization.
