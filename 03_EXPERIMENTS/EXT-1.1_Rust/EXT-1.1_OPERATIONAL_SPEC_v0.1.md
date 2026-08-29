# EXT-1.1 Rust — Operational Specification v0.1

## Purpose

Test whether an explicitly represented change in the space of accessible transformations can be identified in a real generative/technical ecosystem, independently of the subsequent observed outcome.

## Unit of analysis

A package version state at time t. The system is represented by the package/version and its declared dependency constraints as observable in the historical crates.io index state.

## State S_t

For package p at time t, S_t comprises the observable version/dependency configuration relevant to resolution: available versions, yanked status, dependency requirements, target/feature constraints where present, and package/version identity.

## Candidate transformation

A candidate transformation is the transition from one valid package-version configuration to another configuration that can be resolved under the dependency constraints and repository/package metadata available at the observation time.

## Accessibility

A transformation is accessible at t iff its required package/version configuration is observationally admissible under the historical dependency constraints and resolution rules encoded by the index state at t. Accessibility is determined without using download counts, future outcomes, or post-cutoff metadata.

## T_acc

T_acc,t is the set of candidate transformations satisfying the accessibility predicate at t.

## Change

Delta T_acc(t,t') = T_acc,t' minus T_acc,t, together with the reverse difference when transformations cease to be accessible. A state change that leaves this set unchanged is explicitly classified as a non-transformational-space change for TGCV purposes.

## Outcome

Daily version downloads are an external observational outcome. They are never used to define accessibility or T_acc.

## Temporal rule

Structural inputs are evaluated only from the historical index snapshot fixed by the experimental cutoff. Outcome observations are taken from the separately archived daily-download series. No future structural metadata may enter the construction of T_acc.

## Censoring

Versions introduced after the structural cutoff are not allowed to retroactively define T_acc at the cutoff. Versions with incomplete outcome observation windows are flagged rather than silently imputed.

## Falsification conditions

The operationalization fails if any of the following holds:

1. T_acc cannot be computed from observable historical structural data alone.
2. Accessibility requires download outcomes or future information.
3. The same historical input produces non-deterministic T_acc under the frozen resolver.
4. Changes in S cannot be distinguished from changes in T_acc.
5. The representation collapses to a trivial restatement of version existence and adds no independent information about accessible transformations.

## Status

This specification is frozen for pre-data pipeline development. Any change after inspection of the real outcome data requires a new version and explicit justification.
