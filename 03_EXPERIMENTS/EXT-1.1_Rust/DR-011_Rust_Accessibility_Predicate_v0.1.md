# DR-011 — EXT-1.1 Rust accessibility predicate

**Status:** PROPOSED NEW EXPERIMENTAL DECISION

## Decision

For a package-release snapshot `S_t`, a candidate transformation `τ` is accessible iff its complete precondition is satisfied using only information available at the observational cutoff:

`Accessible(τ | S_t,C_t,L_t) = Pre_τ(S_t,C_t,L_t) ∧ Target_τ(S_t,C_t,L_t) ∧ Resource_τ(S_t,C_t,L_t)`.

## Operational rule

A candidate is accessible when:

1. its target component(s)/version(s) are identifiable from the frozen snapshot or frozen pre-cutoff registry;
2. all family-specific preconditions are satisfied at `t`;
3. all required resources are available at `t` under the frozen resource policy;
4. no post-cutoff observation is required to establish feasibility.

## Family-specific interpretation

- **ACTIVATE:** target component is observable but inactive under the predeclared package/feature state, and activation prerequisites are satisfied.
- **COMPOSE:** both target components are observable and the frozen compatibility predicate is satisfied.
- **RECONFIGURE:** the current configuration and the proposed configuration are observable and the transition belongs to the predeclared admissible transition set.
- **ACQUIRE:** the target package/component/version is available from the frozen pre-cutoff registry snapshot and satisfies the predeclared acquisition constraints.
- **LEARN:** the required observable inputs/state for the learning operation exist at `t`; the operation is not defined by its eventual performance.
- **RECOMBINE:** all constituent components are observable and the predeclared recombination/compatibility/resource predicates are satisfied.

## Explicit prohibitions

Accessibility must not depend on:

- future package releases;
- future dependency graphs;
- downstream adoption or success;
- download counts or popularity measured after `t`;
- outcome values;
- future trajectory information;
- model performance after the transformation.

## Important limitation

This decision freezes the **logical form** of accessibility, not every Rust-specific predicate or threshold. Those parameters must be resolved in subsequent decision records and included in the final freeze manifest.

## Scientific rationale

The predicate operationalizes TGCV's distinction between the state and the set of transformations accessible from that state. It preserves non-circularity while allowing domain-specific feasibility conditions.

## Provenance

This is a **NEW DECISION for EXT-1.1**, not a claim about the historical MVE implementation.
