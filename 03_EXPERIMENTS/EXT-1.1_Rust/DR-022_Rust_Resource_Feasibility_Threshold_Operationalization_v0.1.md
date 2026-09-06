# DR-022 — EXT-1.1 Rust resource feasibility / threshold operationalization

**Status:** PROPOSED NEW EXPERIMENTAL DECISION  
**Scope:** Resource component of the Rust accessibility predicate for the dependency-resolution transformation family defined by DR-020/DR-021

## 1. Decision status

This record is a **proposal only**. It does not accept or freeze any Rust resource variable, threshold, or resource predicate. Scientific execution remains blocked until this proposal is audited and the decision is explicitly accepted.

## 2. Governing question

The question is:

> What resources, if any, are observable exclusively from the pre-outcome state and are necessary to establish feasibility of the dependency-resolution transformation represented by `T_acc^(R*)`, without using the subsequent outcome or introducing an outcome-tuned threshold?

The generic TGCV logical form remains:

`Accessible(τ | S_t,C_t,L_t) = Pre_τ ∧ Target_τ ∧ Resource_τ`.

DR-021 operationalizes the current Rust dependency-accessibility layer through `T → R* → T_acc^(R*)` but deliberately leaves the resource term uninstantiated. fileciteturn115file0

## 3. Scope boundary

DR-022 applies **only** to the transformation family currently represented by EXT-1.1: package-level dependency target selection under the accepted candidate universe `T` and frozen R* semantics.

It does not decide:

- the candidate universe `T` (DR-020);
- R* SemVer semantics or implementation (DR-017 / DR-021);
- outcome or outcome horizon;
- sampling or exclusion rules;
- baseline `B`;
- representation `R`;
- other Rust transformation families such as arbitrary build, execution, deployment, acquisition, learning, or recombination operations.

## 4. Candidate resource classes

A variable may qualify as a resource term only if all of the following hold:

1. **Pre-outcome observability:** it can be reconstructed from the frozen dataset and information available no later than the origin release observation boundary.
2. **Transformation relevance:** it represents a resource genuinely required for the transformation family, rather than merely correlated with later success.
3. **Non-circularity:** its value does not depend on downstream adoption, downloads, popularity, future releases, later dependency resolution, or the eventual outcome.
4. **Membership effect:** the variable can, in principle, change whether a candidate transformation is feasible/accesssible; a descriptive statistic that cannot affect feasibility is not a resource predicate.
5. **Ex-ante specification:** any threshold or rule is justified independently of the experimental outcome and cannot be selected by inspecting confirmatory results.
6. **Reproducibility:** the value and predicate can be computed deterministically from the frozen inputs.

Potentially observable quantities such as dependency count, graph size, metadata size, version count, or other structural measures are **not resources merely because they are measurable**. They must not be promoted to resource constraints without a domain-specific feasibility justification.

## 5. Default decision candidate: resource predicate inactive / vacuous

For the current dependency-resolution transformation family, the strongest non-circular position is that **no independent resource predicate has yet been demonstrated to be necessary**.

The transformation defined by DR-020 is the availability/selection of an already observable target release subject to temporal eligibility and the frozen R* requirement semantics. DR-021 therefore currently determines accessibility through the admissible candidate set and maximal-version selection. fileciteturn115file0

Accordingly, DR-022 proposes **not to invent a Rust resource variable or threshold solely to populate the generic `Resource` slot**. Unless an independently justified pre-outcome resource constraint is identified and audited, the resource predicate for this EXT-1.1 transformation family should be treated as **vacuous / inactive**:

`Resource_τ(S_t,C_t,L_t) = TRUE`.

Under this interpretation:

`T_acc^(R*) = T_acc^(R*,Resource=TRUE)`.

This is not a claim that resources are irrelevant to Rust software in general. It is a scope-limited claim that the current empirical transformation definition does not require an additional resource constraint to identify the accessible dependency target.

## 6. Threshold policy

No numerical resource threshold is authorised by this proposal.

In particular, EXT-1.1 must not introduce thresholds based on:

- outcome-derived optimisation;
- post-outcome quantiles;
- confirmatory-sample performance;
- arbitrary convenience cut-offs;
- thresholds selected after inspecting the result.

If a future resource variable is shown to be necessary, its threshold must be specified ex ante from a reproducible external/domain rule or from a structural constraint intrinsic to the transformation definition. A new versioned decision is required before implementation.

## 7. Falsification / auditability gate

A DR-022 audit must establish all mandatory criteria below:

### R1 — Pre-outcome availability
Any proposed resource variable is reconstructible using only information available at the release observation boundary.

### R2 — Transformation necessity
There is an explicit domain argument showing why the dependency-resolution transformation cannot be regarded as feasible without the proposed resource condition.

### R3 — No outcome leakage
The variable and any proposed threshold are independent of outcome, downstream adoption, future releases, and post-cutoff registry state.

### R4 — Non-redundancy with R*
The proposed resource predicate is not simply a restatement of the already accepted temporal/R* admissibility conditions.

### R5 — Ex-ante threshold
Any non-trivial threshold has a justification that can be frozen before confirmatory execution and does not use confirmatory outcomes.

### R6 — Determinism
Two executions over identical frozen inputs produce identical resource values and accessibility decisions.

### R7 — Membership relevance
The resource predicate can actually alter `T_acc` for at least one structurally valid transformation case; otherwise it should not be introduced as an active predicate.

### R8 — Minimality
No weaker resource representation is sufficient to express the claimed feasibility condition. Conversely, no resource variable is retained merely because it is available in the dataset.

## 8. Acceptance rule

DR-022 should be accepted with **Resource inactive/vacuous** if the audit finds no independently justified, pre-outcome resource constraint that is necessary for the current dependency-resolution transformation family.

If the audit identifies a necessary resource constraint, this proposal must instead remain unresolved until the variable, threshold, provenance, and deterministic implementation are explicitly specified and audited in a versioned amendment.

## 9. Scientific rationale

This decision protects the distinction between a generic TGCV logical form and a domain-specific operationalization. A generic predicate may contain `Resource`, but a particular transformation family need not instantiate every conjunct with an independent empirical variable.

Treating a merely measurable structural feature as a resource would risk manufacturing accessibility restrictions, changing `T_acc` for reasons unrelated to the transformation definition, and introducing researcher degrees of freedom before the confirmatory test. Conversely, forcing a resource threshold where none is necessary would weaken rather than strengthen falsifiability.

The proposed inactive/vacuous treatment therefore follows the fail-closed principle: unresolved resource semantics are not silently converted into arbitrary code, while the possibility of a genuinely necessary resource constraint remains open to falsification.

## 10. Explicit non-claims

This proposal does not claim:

- that dependency resolution has no computational resource requirements in practice;
- that package complexity cannot affect build or runtime feasibility;
- that resource constraints are absent from other TGCV transformation families;
- that `Resource=TRUE` has been empirically validated;
- that EXT-1.1 is scientifically frozen.

## 11. Next action

Run a **DR-022 resource audit** against the accepted EXT-1.1 definitions and frozen dataset schema, without using outcome or confirmatory results. The audit should first test whether any independently justified resource variable is necessary for the currently defined dependency-resolution transformation. If none is found, prepare an acceptance amendment recording `Resource=TRUE` for this transformation family and leave other transformation families outside scope.
