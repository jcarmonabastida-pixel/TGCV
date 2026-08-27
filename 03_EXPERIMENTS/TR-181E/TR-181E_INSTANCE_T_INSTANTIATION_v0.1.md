# TR-181E — Instance-Level T Instantiation v0.1

**Status:** PRE-FREEZE — NOT FROZEN

## Purpose
Instantiate the candidate universe without allowing observed outcomes to determine candidate inclusion.

## Instantiation rule

A concrete candidate `τ` is generated only from a pre-declared scenario configuration and the candidate-family grammar. The transformation is defined before test evaluation.

The instance record is:

`τ = <id, class, target, pre, resource, eff>`

## Scenario-local candidate set

For a frozen scenario with components `c1`, `c2`, and resources `r1`, `r2`, the following minimal candidate set is admissible as a template for instance construction:

| ID | Class | Target | Precondition | Resource requirement | Effect metadata |
|---|---|---|---|---|---|
| T01 | ACTIVATE | c1 | c1 exists and is inactive | none | activate c1 |
| T02 | ACTIVATE | c2 | c2 exists and is inactive | none | activate c2 |
| T03 | COMPOSE | c1+c2 | c1 and c2 exist; compatibility declared | none | compose c1,c2 |
| T04 | RECONFIGURE | c1 | c1 exists; permitted configuration transition declared | r1 threshold if specified by scenario | alter c1 configuration |
| T05 | ACQUIRE | c3 | acquisition route declared | r2 threshold if specified by scenario | obtain c3 capability |
| T06 | LEARN | c1 | learning mechanism declared | r1 threshold if specified by scenario | update capability of c1 |
| T07 | RECOMBINE | c1+c2 | c1 and c2 exist; recombination constraint declared | none unless scenario requires | re-use c1,c2 in new role/configuration |

## Important status qualification

This table is a **construction template**, not the final experimental inventory. It deliberately uses placeholders such as `inactive`, `compatibility`, `declared transition`, and resource thresholds that must be resolved from the authoritative TR-181E scenario specification.

No row may enter the frozen `T` unless every such placeholder has a single pre-declared operational definition.

## Anti-leakage rule

Candidate inclusion, exclusion, target assignment, predicate thresholds and effect metadata MUST be determined before test outcomes are inspected.

## Anti-post-hoc-pruning rule

A candidate that is accessible but empirically unsuccessful remains in `T`. Conversely, a candidate is not added because an observed outcome suggests that it would have been useful.

## Freeze gate for T

Before freeze, certify:

- every ID is unique;
- every class has an operational definition;
- every target is explicit;
- every predicate is pre-outcome evaluable;
- every resource threshold is fixed;
- no candidate depends on outcome or trajectory;
- the inventory is independent of observed test performance;
- the inventory reconciles with the B/R provenance matrix.

## Decision

**Instance construction method:** ACCEPTED

**Concrete experimental T:** NOT YET CERTIFIED

**R freeze:** NO-GO until all placeholders are resolved from the authoritative scenario.
