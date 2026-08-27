# TR-181E — B/R Separation Gate v0.1

**Status:** GATE SPECIFICATION — NOT PASSED

## Purpose

Establish that baseline representation `B` and accessibility representation `R` are not duplicate encodings of the same measured object.

## Formal distinction

`B` describes the baseline/pre-outcome state variables required by the experiment.

`R` describes the set of candidate transformations accessible from that state:

`B = representation(S,C,L)`

`R = representation(T_acc(S,C,L))`.

R may depend on S because accessibility is conditioned on state. The requirement is that R represents a derived relational object—the set of transformations admitted by the frozen candidate universe and predicates—rather than simply copying baseline variables.

## Required checks

1. Every R field has a provenance path through `T_acc`.
2. No R field directly copies a B variable.
3. Removing a baseline variable irrelevant to all candidate predicates leaves R unchanged.
4. States can share B-level marginal summaries while differing in R when their admissible transformation sets differ.
5. Changes in B that do not alter any predicate do not alter R.
6. Candidate IDs denote transformation hypotheses, not state-variable IDs.

## Current assessment

The minimal engine satisfies the representational intention at code level: canonical R consists of accessible candidate IDs plus cardinality. The gate cannot yet be certified because the authoritative B schema has not yet been jointly mapped field-by-field against the final candidate predicates.

## Decision

**B/R conceptual separation:** PLAUSIBLE

**B/R formal separation:** NOT YET CERTIFIED

**Experiment:** BLOCKED

**Next:** retrieve/fix the authoritative B schema, produce a field-level provenance matrix, and add automated anti-duplication checks before R freeze.
