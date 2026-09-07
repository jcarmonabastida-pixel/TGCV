# SLR-1 Source Dossier — SRC-PHASE-001

**Status:** RECONSTRUCTED / WORKING
**Source:** *Designing Distributed Applications Using a Phase-Aware, Reversible System* (KTH / Beernet line; accessible paper version).
**Classification:** **AC2 — VERY STRONG STRUCTURAL EQUIVALENCE; AC3 NOT ESTABLISHED**

## Why this source is decisive

This source gives an unusually explicit formal construction in which a system's **available operations are a function of its current phase configuration**. It therefore provides a direct antecedent to the relation:

`system condition/configuration → set of available operations`.

The source defines a phase configuration `P_c(t)` and states that, when sufficiently informative, the available-operation set can be defined as a function of that phase configuration:

`O_pavail = F_rev(S(t)) ≈ F_phase(P_c(t))`.

It further defines `F_phase` as a total function mapping each phase configuration to an operation set/vector, with each element representing the available operations at a node. citeturn2search24turn2search25

## Key evidence

- A phase is a local system property whose value changes as the node experiences changes in its local environment.
- A system phase configuration is the vector of node phases and is time-dependent.
- The available-operation set is explicitly modeled as a function of the current phase configuration.
- The source gives a concrete ordered universe of functionalities and represents the available operations at a node as a subset of that universe. citeturn2search24

This is substantially stronger than a generic possibility-space or affordance analogy.

## TGCV mapping

| TGCV element | Source analogue | Assessment |
|---|---|---|
| `S` | distributed system / current system condition | strong |
| `C` | phase configuration / environmental stress | strong |
| `T_acc` | available-operation set `O_pavail` | **very strong direct analogue** |
| accessibility predicate | membership in `O_pavail`, defined through phase/configuration | strong operational analogue |
| `ΔT_acc` | change in phase configuration producing changed available functionality | strong implied/operational analogue |
| `Reach` | reversible system behaviour / eventual success | partial |
| `Trajectory` | system evolution through phase transitions | partial |
| `Outcome` | available functionality / successful operation | partial |
| `Value` | application utility/predictable behaviour under stress | not equivalent to TGCV value layer |
| mechanism | environmental stress and maintenance/self-healing mechanisms | domain-specific |

## AC2 assessment

**AC2 — VERY STRONG STRUCTURAL EQUIVALENCE CONFIRMED.**

The source contains an explicit construction equivalent to:

`P_c(t) → O_pavail(t)`

where `O_pavail(t)` is a set/vector of currently available operations and `P_c(t)` is a time-varying system configuration.

This materially falsifies any TGCV claim that the mere analytical relation

`T_acc = F(S,C)`

is unprecedented.

Likewise, the source demonstrates that an operational system can move through changing configurations/phases while its available functionality changes accordingly. citeturn2search24turn2search26

## AC3 assessment

**AC3 — NOT ESTABLISHED.**

Despite the unusually close structural match, full TGCV architectural absorption is not established.

### 1. Operation availability is not a general transformation-space theory

The source concerns available functionality/operations of a distributed overlay system. It does not formulate a domain-independent transformation space covering arbitrary system transformations.

### 2. The transformation/accessibility distinction is not generalized

`O_pavail` is an available-operation set, but the source does not establish a general predicate of the form:

`τ ∈ T_acc ⇔ P_τ(S,C,L)=1`.

### 3. `ΔT_acc` is not isolated as the central analytical object

The source models changing functionality through phase transitions, but it does not make the **change in the accessible-operation space itself** the central transversal explanatory variable.

### 4. No general downstream architecture

The source does not establish the full TGCV relation:

`mechanism → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.

### 5. Domain and purpose remain specific

The construction is designed for reversibility/self-healing and predictable degradation in distributed systems. Its contribution is not presented as a transversal theory of value construction across generative/technical ecosystems.

## Falsification significance

This source is one of the strongest prior-art anchors found so far. TGCV can no longer claim novelty for:

- representing available operations as a function of current system conditions;
- treating available-operation sets as time-varying;
- relating system phase/configuration changes to changes in available functionality;
- using a configuration-dependent operation set to reason about system behaviour.

The remaining candidate boundary is narrower:

> **Does prior literature generalize this construction from an available-operation/functionality set in a particular system to a domain-independent accessible transformation space, explicitly treat its change `ΔT_acc` as an analytical object, and connect that change to future reachability, trajectories, outcomes and value?**

## Supporting adjacent evidence

The 2023 ACM Computing Surveys work on component-based distributed software reconfiguration independently confirms that configurations consist of runtime entities/dependencies, reconfiguration changes configuration at runtime, and reconfiguration languages specify operations applicable to the current configuration. It also notes that the available reconfiguration operations form a specific language. citeturn1search0

Brusaferri, Ballarino & Carpanzano (2011) provide a complementary industrial antecedent: their responsive manufacturing system dynamically updates resource models and updates available operations according to evolving execution states and/or reconfigurations. citeturn1search1turn1search27

Together these sources make the reconfiguration/available-operation antecedent a convergent cluster rather than an isolated result.

## Decision

- `AC2`: **VERY STRONG / CONFIRMED**.
- `AC3`: **NOT ESTABLISHED**.
- Broad novelty claim concerning `T_acc = F(S,C)` is **absorbed** by prior art.
- Broad novelty claim concerning changing available operations is **absorbed**.
- TGCV Core: unchanged.
- EXT-1.1 result: not used.

## Next controlled operation

The search should now test the final remaining structural bridge: **whether formal reconfiguration literature explicitly represents the enabled/available transformation relation itself as a changing relation and propagates that change into reachable state/trajectory structure**. Priority targets are reconfigurable transition systems, dynamic Petri nets, runtime-adaptive software architectures, and formal models where the enabled-transition relation is recomputed after reconfiguration.
