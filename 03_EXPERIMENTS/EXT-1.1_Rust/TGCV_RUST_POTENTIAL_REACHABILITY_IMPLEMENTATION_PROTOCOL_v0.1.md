# TGCV — Rust Potential Reachability Implementation Protocol v0.1

**Status:** RECONSTRUCTED / WORKING — EX ANTE

## Purpose

Freeze the implementation semantics for the first bounded computation of potential structural Reach in Rust, following the accepted successor/closure feasibility result.

## Locked architecture

`Core_ontological = S`

`T_acc,t = {(e_o, τ_id) | P_τ(e_o,t)=1}`

`ΔT_acc = T_acc,t1 ≄ T_acc,t0`

`T_acc → Reach → Trajectory → Outcome → Value`

Only the Reach layer is authorized here. Trajectory, Outcome, Value and model fitting remain blocked.

## 1. Reach object

For a focal package-version `e_o` at time `t`, define potential Reach as the finite set of structurally reachable dependency configurations induced by accessible dependency transformations under the frozen Rust semantics.

The construction is counterfactual/potential. It does not represent observed runtime execution.

## 2. Successor semantics

The selected successor representation is **Configuration Successor (Option A)**.

Applying an accessible dependency transformation produces a deterministic structural configuration successor by adding or replacing the corresponding dependency relation in the current configuration.

A package-version target is an element referenced by the transformation; it is not itself treated as an observed execution successor.

## 3. Initial configuration

The initial structural configuration is the dependency-declaration configuration of the focal package-version at the relevant frozen observation time.

Only records available at that observation time and admitted by the frozen data contract may contribute.

## 4. Candidate transformations

Transformation identity remains:

`τ_id = (origin_version_id, target_package_id, target_version_id)`.

Candidate identity is independent of declaration text.

Accessibility is inherited from the frozen Rust accessibility predicate and R* v0.2. Reach does not redefine accessibility.

## 5. Closure boundary

The closure is finite and bounded by the independently observed package-version/dependency universe.

No candidate may be invented outside that universe.

Recursive expansion must terminate when:

- no new structural configuration is produced;
- the frozen candidate boundary is exhausted; or
- a previously visited configuration is encountered.

## 6. Cycles

Configurations are canonicalized deterministically. A configuration already present in the visited set is not expanded again.

Cycles therefore terminate without being interpreted as successful runtime execution.

## 7. Unsupported / unresolved cases

`UNSUPPORTED` and `UNRESOLVED` records are never silently converted to inaccessible or reachable.

They are excluded from the resolved structural closure and counted explicitly in the audit output.

## 8. Temporal comparison

For paired focal versions:

`t0 = origin timestamp`

`t1 = next release timestamp of the same package`.

Reach is constructed independently at both frozen times, using the corresponding present accessibility relation.

`ΔReach = Reach_t1 ≄ Reach_t0`.

Terminal focal versions are excluded from paired comparison.

## 9. Required outputs

The implementation must report at minimum:

- paired focal units;
- valid/invalid structural cases;
- Reach construction coverage;
- number of configurations at `t0` and `t1`;
- additions/removals between Reach sets;
- unchanged/changed Reach pairs;
- empty Reach cases;
- unsupported/unresolved exclusions;
- deterministic canonical hashes;
- execution/outcome/value/model firewall flags.

## 10. Required distinctions

The implementation must preserve:

`T_acc ≠ Reach`

`Reach ≠ Trajectory`

`accessible ≠ executed`

`reachable ≠ realized`

`outcome/value ≠ accessibility condition`.

## 11. Explicit prohibitions

The computation must not use:

- observed dependency-resolution events;
- build success/failure;
- later package activity;
- later outcomes;
- the EXT-1.1 180-day outcome window;
- the previous EXT-1.1 predictive model;
- outcome-derived features;
- value labels;
- post-hoc parameter optimization;
- modifications to R* v0.2.

## 12. Falsifiers

**F-RCH1:** deterministic configuration successors cannot be produced from frozen records.

**F-RCH2:** finite closure cannot be guaranteed within the independent candidate boundary.

**F-RCH3:** Reach requires execution or outcome information.

**F-RCH4:** Reach collapses into T_acc membership under correct semantics.

**F-RCH5:** unresolved/unsupported cases require silent recoding.

**F-RCH6:** temporal Reach comparison cannot be performed consistently at t0/t1.

## 13. Gate criteria

| Criterion | Status |
|---|---|
| RCH-G1 successor semantics frozen | PASS |
| RCH-G2 finite boundary frozen | PASS |
| RCH-G3 cycle termination frozen | PASS |
| RCH-G4 accessibility inherited independently | PASS |
| RCH-G5 unsupported/unresolved handling frozen | PASS |
| RCH-G6 temporal pairing inherited | PASS |
| RCH-G7 Reach implementation authorized | PASS — bounded structural only |
| RCH-G8 actual Reach computation | OPEN — next execution |
| RCH-G9 ΔReach computation | OPEN — next execution |
| RCH-G10 trajectory computation | BLOCKED |
| RCH-G11 outcome/model computation | BLOCKED |
| RCH-G12 causal inference | NOT CLAIMED |

## Decision

**PASS — EX ANTE REACH IMPLEMENTATION PROTOCOL FROZEN.**

The next authorized operation is the bounded Rust Potential Reach Structural Audit v0.1. No outcome/model execution is authorized.

## Integrity lock

Core, T_acc, ΔT_acc, R* v0.2, SLR-1, and the previously accepted EXT-1.1 results remain unchanged. This protocol does not reinterpret the previous predictive experiment.
