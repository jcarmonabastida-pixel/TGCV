# TGCV — Current Research Architecture

## Status

**FOUNDATIONAL / STABILIZED CONCEPTUAL ARCHITECTURE**

The architecture is intentionally domain-independent at its core. Application domains provide empirical instantiations and constraints rather than redefining the central object. This record is not a claim of universal empirical validation or demonstrated originality.

## Central research object

Interactions that modify the set of transformations accessible to a system.

## 1. Ontological minimum

`Core_ontological = S`

`S` denotes the relevant state/configuration of the system.

Context, conditions, relations, reachability, trajectories and value are not introduced as independent ontological primitives.

## 2. Analytical object

The relevant analytical object is the **structure of accessible transformations**:

`T_acc = F(S,C,L)`

A candidate transformation `τ` is accessible when its relevant realization conditions are satisfied:

`τ ∈ T_acc iff P_τ(S,C,L)=1`

Accessibility is therefore a derived property, not a definition by circular reference to accessibility itself.

TR-131 provides empirical support that the frozen B representation used in the Rust structural snapshot does not uniquely determine the resulting canonical `T_acc` membership set. This supports analytical indispensability of explicit `T_acc` representation for comparing `ΔT_acc`; it does not establish ontological independence of `T_acc` from `S`.

## 3. Central phenomenon

`T_acc,t ≄ T_acc,t+1`

TGCV investigates modification of the structure of accessible transformations of a system.

The change is sign-neutral and may involve:

- expansion;
- contraction;
- reconfiguration;
- substitution.

It is not equivalent to a mere state change, adaptation, growth, or increased possibility.

## 4. Dynamic consequence

`ΔT_acc → ΔReach → ΔTrajectory`

A modification of transformational structure may alter the region of outcomes reachable under relevant conditions and the subsequent trajectories through the system's evolving state space.

`T_acc` is a derived structural representation, not an independently postulated ontological cause.

## 5. Mechanisms

TGCV does not require a single primitive mechanism. Interaction, learning, reconfiguration, resource acquisition, organizational change, institutional change and evolutionary processes may all generate transitions.

`I` is therefore an explanatory mechanism/occasion, **not a Core primitive**.

## 6. Value extension

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

Value is a downstream evaluative layer. It must not be used retrospectively to justify the ontological Core.

## 7. Scientific status

TR-129 and TR-130 remain incorporated in the stabilized architecture. TR-131 is now **CONCEPTUAL PASS + EMPIRICAL EXECUTION CLOSED + SCIENTIFIC INTEGRATION COMPLETE**. Its empirical support is limited to the frozen B representation and Rust structural snapshot used in the authorized experiment.

The broader empirical programme does not constitute universal validation of TGCV. External replication and/or empirical-domain replication remain required. TR-139 remains a Conditional Pass on architectural novelty; full originality requires systematic literature comparison.

## 8. Experimental status

The TR-131 real-dataset execution is technically closed. Primary integrity, deterministic replay, execution-result audit and scientific integration have passed their respective gates. No further TR-131 rerun is required by the current governance state.

The TR-131 result must not be used to reinterpret the separate predictive findings of EXT-1.1 as validation of the Core. Predictive, causal, outcome and value claims remain separately gated.

## 9. Integrity constraints

1. Do not reintroduce interaction as a Core primitive.
2. Do not add `C`, `R`, `Reach`, `Trajectory` or `Value` as ontological primitives without an explicit evidence/gate decision.
3. Do not modify the Core merely because a literature source contains a similar term.
4. Do not treat application outcomes as retrospective proof of the Core.
5. Do not infer universal validity from the Rust result.
6. Preserve all superseded versions for traceability.
7. Any substantive Core revision requires a new version and an explicit governance decision.
