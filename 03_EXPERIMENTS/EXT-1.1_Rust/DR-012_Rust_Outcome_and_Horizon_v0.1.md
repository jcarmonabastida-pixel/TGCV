# DR-012 — EXT-1.1 Rust outcome and observation horizon

**Status:** PROPOSED NEW EXPERIMENTAL DECISION

## Decision

Define the primary outcome as the **observed change in package-level adoption/success during a fixed post-release horizon**, operationalized only from observations that occur after the package-release cutoff.

For the first confirmatory specification, use a fixed horizon of **six subsequent release observations** for the same package when these observations exist; the horizon is truncated only under a predeclared censoring rule. The exact success/adoption measure remains to be frozen in DR-013 after verifying its observability and missingness properties in the selected Rust dataset.

## Temporal separation

At prediction time `t`, all of `S_t`, `B_t`, `T_t`, `T_acc,t` and `R_t` are constructed exclusively from information available at or before the release cutoff. The outcome is evaluated only from observations strictly after `t`.

## Why the outcome is not yet fully frozen

The Rust domain offers several possible downstream outcomes (subsequent release survival, dependency adoption, downloads, reverse dependencies, etc.). Selecting one without checking dataset observability could create avoidable censoring or measurement artefacts. Therefore the outcome family and horizon structure are fixed here, while the exact scalar outcome and censoring rule are delegated to the next decision record.

## Prohibitions

No outcome variable may be used in candidate generation, accessibility, baseline construction, R construction, sampling eligibility, or feature normalization at time `t`.

## Provenance

This is a **NEW DECISION for EXT-1.1** and does not claim to reproduce the historical EMP-1.1 outcome definition.

## Gate status

Outcome temporal direction: **PASS**.

Exact outcome measure: **OPEN**.

Censoring rule: **OPEN**.

Confirmatory freeze: **BLOCKED** until DR-013 resolves these fields.
