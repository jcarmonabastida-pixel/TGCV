# TGCV SLR-1 — Fact Bank Schema v0.1

**Status:** RECONSTRUCTED / WORKING
**Purpose:** normative schema for normalized factual statements derived from documented evidence.

## Fact record

Each fact receives a unique `fact_id` and contains:

1. `fact_id` — stable internal identifier.
2. `source_id`
3. `evidence_ids` — one or more supporting evidence records.
4. `fact_statement` — concise normalized factual statement.
5. `fact_scope` — construct / structure / architecture / mechanism / trajectory / outcome / value.
6. `subject`
7. `predicate`
8. `object_or_value`
9. `conditions` — state/context/constraints under which the fact holds.
10. `temporal_scope`
11. `explicitness` — explicit / derived with minimal normalization.
12. `confidence` — high / medium / low, reflecting evidence quality rather than agreement with TGCV.
13. `contradictions` — conflicting facts/evidence, if any.
14. `interpretation_status` — factual / interpretive; only factual entries qualify as Fact Bank records.
15. `review_status`

## Normalization rules

- A fact must be traceable to one or more Evidence Bank records.
- Normalization may simplify wording but must not add an unsupported relation.
- Source terminology may be translated into neutral analytical language only when the original meaning is preserved.
- A statement that a source is "equivalent to TGCV" is never a fact; it belongs to the interpretation/absorption layer.
- Absence of a construct in a source may not be recorded as a fact unless the source explicitly establishes the relevant scope and absence.
- Conflicting source claims remain separate facts linked through `contradictions`.

## Analytical hand-off

The Fact Bank is the controlled input to architectural comparison. The comparison layer maps facts to TGCV components and assigns AC0–AC3 only after the underlying evidence and facts are documented.
