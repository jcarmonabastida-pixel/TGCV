# N-R8.1 — Robustness & Mechanism Discrimination Specification v0.1

**Status:** PROPOSED — NOT FROZEN
**Date:** 2026-09-05
**Depends on:** N-R7 epistemic interpretation and claim boundary v0.1

## 1. Purpose

N-R8 is the next scientific block after the sealed N-R7 executions. Its purpose is not to improve the N-R7 result, but to attack the principal alternative explanations that remain compatible with N-R7.

N-R8 must therefore be designed as a falsification/robustness program. No N-R7 artifact, feature, threshold, learner, seed, or result may be altered as part of N-R8.

## 2. Frozen N-R7 claim under attack

N-R7 authorized the controlled-domain claim H1-N:

> In the controlled Branch N domain, certain structural properties of the accessible-transformation structure `T_acc` contain incremental information for predicting future controlled outcomes beyond the frozen baseline state representation `B`.

N-R8 asks whether this interpretation survives controlled attacks on:

- generator dependence;
- latent/proxy explanations;
- representation dependence;
- structural confounding by simple graph/cardinality properties.

## 3. Scientific alternatives

N-R8 distinguishes four live explanations:

**A — Structural signal:** information in structural properties of `T_acc` is genuinely relevant to future outcomes.

**B — Generator artifact:** the N-R7 signal is mainly induced by the particular snapshot/trajectory generator distribution.

**C — Proxy explanation:** `R` predicts because it encodes latent generator/state properties correlated with outcome, rather than because accessible-transformation structure is itself explanatory.

**D — Representation effect:** the result depends materially on the particular 58-dimensional encoding rather than on the structural object represented.

The purpose of N-R8 is to make these alternatives empirically distinguishable. It does not assume A is true.

## 4. Design principle: preserve the scientific boundary

N-R8 must preserve:

1. the same Branch N semantic domain unless an extension is explicitly frozen;
2. predictor/outcome separation;
3. no future information in predictors;
4. no use of N-R7 test outcomes for design tuning;
5. deterministic, hashed, auditable artifacts;
6. exact provenance for every generated corpus;
7. independent seeds for every new corpus;
8. fail-closed behavior on schema/hash/join violations.

## 5. N-R8-A — Generator distribution attack

### Question

Does the incremental predictive signal survive when the generator distribution is changed while the semantic transformation system remains unchanged?

### Design

Construct at least one independently specified generator distribution G2 that differs materially from N-R4A in state-generation statistics while preserving the exact N-R4B semantic transition/outcome definitions and the same predictor representation semantics.

G2 must be specified before inspecting N-R8-A results. Examples of admissible distribution changes include altered component-count probabilities, edge-density distribution, resource distribution, and objective distribution, provided the change is fully specified and does not introduce outcome leakage.

The original N-R4A generator remains immutable and serves as G1.

### Decision logic

Evidence for persistence under G2 weakens explanation B. Failure under G2 does not prove B, but materially weakens the controlled-domain generality of H1-N.

## 6. N-R8-B — Matched `T_acc` intervention

### Question

Can changing the accessible-transformation structure while holding the baseline state representation fixed alter future outcome predictions?

### Design requirement

Construct matched initial states with identical `B` but distinct `T_acc` structures. The intervention must modify accessibility structure through admissible transformations while preserving the frozen baseline fields represented by `B`.

The construction must not select pairs using future outcomes or learner predictions.

Primary comparison:

`P(Y | B, R_A)` versus `P(Y | B, R_B)` for matched pairs where `B_A = B_B` but `T_acc,A != T_acc,B`.

### Important restriction

This is an intervention on the controlled synthetic system, not a causal identification claim about real-world systems. The design may support stronger mechanistic inference only if the intervention itself passes its own balance, manipulation, and outcome-blindness gates.

## 7. N-R8-C — Structural confounding attack

### Question

Does the signal survive when simple structural statistics are explicitly matched or controlled?

### Design

Construct matched/counterfactual states in which the following are held fixed wherever feasible:

- number of accessible transformation families;
- total number of accessible transformations;
- component count;
- edge count;
- family cardinalities;
- component incidence statistics;
- other pre-specified low-order structural summaries.

The compared states must nevertheless differ in higher-order organization of `T_acc`.

No matching variable may be selected after examining outcomes.

### Decision logic

Persistence would weaken explanation based on simple structural confounding. Failure would identify an important limitation of the N-R7 interpretation.

## 8. N-R8-D — Representation robustness

### Question

Does the signal persist under independently specified encodings of the same accessible-transformation structure?

### Design

Define at least one representation R2 before inspecting N-R8 results. R2 must encode the same `T_acc` semantics without importing future outcome information. Candidate forms may include graph-structural summaries, canonical transformation-set statistics, or another independently specified representation.

R2 must have its own conformance specification. No R2 may be selected because it improves N-R7 performance.

### Decision logic

Persistence across semantically equivalent encodings weakens explanation D. Divergence does not invalidate H1-N but makes the claim representation-dependent and therefore weaker.

## 9. Required negative controls

N-R8 must retain explicit negative controls sufficient to detect accidental predictive leakage or generator-specific artifacts. At minimum:

- outcome-independent permutation control;
- baseline-only control;
- family-count control;
- representation-independent structural summary control where applicable.

Any additional negative control must be frozen before execution.

## 10. Statistical discipline

N-R8 must use pre-specified evaluation metrics and thresholds. No threshold may be selected after observing N-R8 results.

Where paired comparisons are used, the pairing rule must be deterministic and outcome-blind. Any permutation/sign-flip procedure must specify its seed, number of permutations, tail convention, and p-value formula before execution.

No multiple-comparison correction is specified by this document because the exact confirmatory hierarchy has not yet been frozen. N-R8.2 must explicitly define which tests are primary, secondary, and exploratory before the execution gate.

## 11. Required data separation

Every N-R8 predictor dataset must exclude:

- future trajectory states;
- terminal state;
- outcome Y;
- terminal reason;
- number of steps actually taken;
- any post-snapshot field;
- any field generated using knowledge of the future trajectory.

Outcome labels may enter only through the separately frozen outcome corpus and only after exact join validation.

## 12. Required provenance

Every N-R8 corpus and result package must record:

- specification version/hash;
- source corpus hashes;
- generator implementation hash;
- representation implementation hash;
- learner implementation/specification hash;
- exact seeds;
- Python/runtime versions;
- platform;
- file SHA-256 hashes;
- generation timestamp;
- whether any result was inspected before generation/freeze;
- join statistics and failed joins;
- execution status.

## 13. Mandatory gates before execution

N-R8 execution is BLOCKED until all of the following are separately passed and frozen:

1. N-R8.1 specification review/freeze;
2. N-R8.2 operationalisation of G2, matched intervention, confounding controls and R2;
3. N-R8.3 implementation conformance;
4. N-R8.4 corpus construction/integrity freeze;
5. N-R8.5 execution authorization.

No scientific execution is authorized by this document alone.

## 14. Interpretation matrix

| Result pattern | Interpretation |
|---|---|
| Signal survives G2, matched intervention, structural matching and R2 | Strongest support for A within Branch N; B/C/D substantially weakened |
| Survives G2 but not structural matching | Generator dependence weakened; simple structural confounding remains |
| Survives structural matching but not G2 | Possible generator dependence remains |
| Survives only original R encoding | Representation dependence remains |
| Fails all attacks | H1-N substantially weakened/falsified in current form |
| Mixed results | Claim must be narrowed to the conditions actually supported |

These are interpretation rules, not outcome predictions.

## 15. Explicit non-claims

Even a successful N-R8 does not establish:

- historical equivalence to Cargo;
- causal validity in real systems;
- cross-domain validity;
- universality of TGCV;
- novelty of TGCV;
- value creation as a demonstrated causal consequence;
- empirical validation of the complete TGCV theory.

Those require separate evidence and gates.

## 16. Next action

The immediate next step is **N-R8.2**, which must convert this scientific design into exact operational specifications for:

- G2 generator;
- matched `T_acc` intervention;
- structural-confounding matching;
- independent representation R2;
- confirmatory hierarchy and statistical thresholds;
- corpus sizes and seeds;
- exact artifact schemas and integrity checks.

**Decision:** N-R8 design direction APPROVED FOR OPERATIONALISATION; execution remains BLOCKED.
