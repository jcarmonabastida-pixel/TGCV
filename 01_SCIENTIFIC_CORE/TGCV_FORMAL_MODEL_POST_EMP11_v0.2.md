# TGCV — Formal Model Post-EMP-1.1 v0.2

**Status:** Formalisation draft — NOT FROZEN

## 1. Purpose

Provide a mathematically explicit scaffold for TGCV while keeping the empirical boundary visible. The model is stratified into defined, operationalised and hypothetical layers.

## 2. Basic system representation

Let a system at time `t` be represented by:

`S_t = (X_t, C_t, L_t)`

where `X_t` denotes the system's conventional state variables, `C_t` contextual conditions, and `L_t` constraints/resources relevant to possible transformations.

These components are modelling primitives, not yet claims of a universal ontology.

## 3. Transformation universe

Let `T` be a declared universe of candidate transformations for the experimental or analytical domain.

For a given system condition:

`T_acc(S_t,C_t,L_t) = { τ ∈ T : P_τ(S_t,C_t,L_t) = 1 }`

where `P_τ` is a pre-specified accessibility predicate.

The predicate must be evaluable without using the outcome whose relation to accessibility is being tested.

## 4. Accessibility change

Given consecutive conditions:

`ΔT_acc(t) = T_acc(S_{t+1},C_{t+1},L_{t+1}) − T_acc(S_t,C_t,L_t)`

For analysis where direction matters, the corresponding gained and lost sets may be defined as:

`G_t = T_acc(t+1) \ T_acc(t)`

`L_t^− = T_acc(t) \ T_acc(t+1)`

This distinction should not be collapsed into a scalar unless the research question explicitly requires a summary statistic.

## 5. Trajectory layer

Let a trajectory be a sequence:

`Ω = (S_0,S_1,...,S_n)`.

TGCV proposes that changes in accessible transformations may alter the set of feasible future trajectories. A general relation may therefore be represented as:

`Ω_{t+1:n} ∈ Reach(S_t, T_acc(t), E_t)`

where `E_t` denotes environmental or exogenous conditions.

**Status:** theoretical/hypothetical. EMP-1.1 did not directly establish this trajectory relation.

## 6. Value layer

Let `V(Ω, E)` denote a domain-specific value functional over trajectories and environment.

The programme investigates whether:

`ΔT_acc → ΔReach → ΔΩ → ΔV`

can be identified and estimated under appropriate conditions.

**Status:** open research problem. No value claim is inferred from EMP-1.1.

## 7. Empirical layer supported by EMP-1.1

EMP-1.1 tested a concrete operationalisation in which accessibility information was represented computationally and evaluated through predictive performance. The positive result supports the proposition that the tested accessibility representation contains useful information beyond the tested baseline.

The formal scaffold must therefore distinguish:

- **semantic model:** the equations above;
- **experimental instantiation:** the sealed EMP-1.1 implementation;
- **future instantiation:** independently specified replication implementations.

They are not interchangeable.

## 8. Falsifiability conditions

The model is vulnerable to empirical failure if, under appropriate controls and independently specified operationalisations:

1. accessibility representations add no reproducible information beyond conventional state/resource variables;
2. relational structure provides no advantage over suitable null representations;
3. predicted trajectory effects fail systematically;
4. apparent effects disappear under valid leakage-free evaluation;
5. the constructs cannot be operationalised with domain-independent semantics where such generality is claimed.

## 9. Formalisation priorities

The next formal work should address:

- properties of `F` and accessibility predicates;
- equivalence and invariance between different representations of `T`;
- conditions under which `ΔT_acc` changes reachable trajectories;
- causal identification where appropriate;
- domain-specific definitions of value;
- boundary conditions and impossibility results.

## 10. Freeze rule

No equation in this document should be treated as a final theorem merely because it provides a convenient representation. Formal claims become candidates for freeze only after their assumptions, semantics and empirical consequences are explicitly tested or justified.

## 11. Current status

**Formal scaffold:** established.

**Accessibility formulation:** operationally supported in one tested setting.

**Trajectory formulation:** hypothesis.

**Value formulation:** hypothesis/open problem.

**Full mathematical theory:** not yet complete.
