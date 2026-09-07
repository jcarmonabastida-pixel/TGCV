# TGCV SLR-1 — Source Dossier Schema v0.1

**Status:** RECONSTRUCTED / WORKING
**Purpose:** normative schema for documenting candidate prior-art sources.

## Required fields

1. `source_id` — stable internal identifier.
2. `bibliographic_identity` — authors, title, venue, year.
3. `stable_identifier` — DOI, ISBN, URL or equivalent.
4. `retrieval_context` — database/search family, query identifier, retrieval date.
5. `publication_temporal_status` — publication date and relation to SLR cutoff.
6. `domain` — empirical/theoretical domain addressed by the source.
7. `source_type` — article, book/chapter, conference paper, review, framework/specification, other.
8. `full_text_status` — full text available / partial / abstract only.
9. `screening_decision` — include / exclude / contextual.
10. `exclusion_reason` — mandatory when excluded.
11. `candidate_construct` — source's own name for the relevant construct.
12. `construct_definition` — source-grounded definition.
13. `state_or_condition_representation` — how the source represents system state/conditions.
14. `transformation_representation` — what counts as an action/transformation/option.
15. `accessibility_representation` — how possible/accesssible transformations are defined.
16. `execution_accessibility_distinction` — explicit / implicit / absent.
17. `transformation_space_representation` — set, graph, capability structure, affordance structure, other.
18. `transformation_space_change` — explicit / derivable / absent.
19. `reachability_or_trajectory` — explicit / implicit / absent.
20. `mechanism_role` — how interactions/mechanisms alter conditions or possibilities.
21. `outcome_or_value_role` — if present.
22. `evidence_refs` — page/section/table/figure/paragraph locations.
23. `evidence_extracts` — short source-grounded extracts/paraphrases.
24. `tgcv_mapping` — mapping to S, T_acc, ΔT_acc, ΔReach, ΔTrajectory, Outcome, Value.
25. `absorption_level` — AC0, AC1, AC2 or AC3 according to SLR-1 protocol.
26. `absorption_rationale` — explicit comparative reasoning.
27. `substantive_remainder` — what TGCV would still add if source is relevant.
28. `ambiguities` — unresolved interpretive issues.
29. `review_status` — pending / reviewed / adjudicated.
30. `provenance_hash_or_snapshot` — optional integrity identifier when local source capture exists.

## Rules

- Facts about the source must be separated from interpretation.
- No absorption level may be assigned without evidence references.
- Terminology alone cannot establish AC2/AC3.
- A source discovered through citation chaining must retain its discovery provenance.
- Duplicate versions must be linked rather than counted as independent evidence.
- Missing full text cannot be silently treated as absence of evidence.
