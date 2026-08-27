# TR-181E — B/R Provenance Matrix v0.1

**Status:** ANALYTICAL DRAFT — NOT FROZEN
**Purpose:** Field-level provenance test for the separation between baseline representation `B` and accessibility representation `R`.

## Authoritative baseline B

TR-181E inherits the baseline boundary from the experimental lineage: B is the conventional pre-outcome snapshot representation and deliberately excludes accessible-transformation/relational structure. The exact field schema must remain tied to the authoritative source used for the new experiment.

## Provenance matrix

| B field / component | Used directly by candidate predicate? | Mediates accessibility? | Appears directly in R? | Separation assessment |
|---|---|---|---|---|
| component count | No, unless an explicitly frozen predicate requires it | No in current minimal engine | No | Clean |
| resource values | Yes, for `resource_min` predicates | Yes | No | Legitimate conditioning, not duplication |
| objective identity | No in current minimal predicate vocabulary | No | No | Excluded from R; clean |
| component identity/list | Yes, for `component_exists` and `component_pair` | Yes | No | Conditioning input; candidate IDs remain transformation-level |
| outcome | Must not be used | No | No | Leakage prohibited |
| trajectory/future state | Must not be used | No | No | Leakage prohibited |

## R provenance

| R element | Immediate source | B copy? | Interpretation |
|---|---|---|---|
| accessible candidate ID | membership in `T_acc` | No | identity of an accessible transformation hypothesis |
| cardinality | `|T_acc|` | No | number of accessible candidate transformations |

## Important qualification

The table above demonstrates **structural separation in the current candidate implementation**, not yet empirical discriminant validity. B variables can legitimately condition R. The anti-duplication requirement is that R encodes the resulting transformation-accessibility relation rather than re-reporting B variables.

## Gate tests

1. Change `resource_1` while keeping all resource predicates false: R must remain invariant.
2. Change a B field not referenced by any predicate: R must remain invariant.
3. Change a predicate-relevant B field across its threshold: R may change only through the affected candidate(s).
4. Replace candidate IDs while preserving state values: R changes because the transformation universe changed; this is not B duplication.
5. Inject outcome/trajectory differences with identical pre-outcome state: R must remain invariant.

## Current decision

**Structural B/R separation:** PASS, subject to final schema reconciliation.

**Leakage separation:** PASS at design level.

**Formal freeze:** NOT YET CERTIFIED.

The remaining requirement is to reconcile this matrix against the final authoritative B schema and final candidate-transformation schema before R is frozen.
