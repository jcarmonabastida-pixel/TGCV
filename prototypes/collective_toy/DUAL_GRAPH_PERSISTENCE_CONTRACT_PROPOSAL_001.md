# Dual-graph persistence contract proposal 001

**Status:** proposal for review; not an implementation authorization.  
**Branch:** design/condition-evaluator-contract-001-20261021  
**Scope:** define the minimum import/export and stale-result rules required before introducing a separate TGCV graph into the collective-toy demonstrator.

## 1. Compatibility principle

The current browser package contains one system input model and its execution/result layers. Preserve that meaning. Do not silently treat an existing single-model export as a dual-graph package, and do not infer a TGCV graph merely by renaming system states or transitions.

Existing imports remain readable under their current schema/package validators. A future dual-graph package must identify its own package version explicitly.

## 2. Proposed package shape

The names below are logical contract fields for discussion, not a final serialized schema or code-level commitment.

- `package_version`: explicit dual-graph package version, separate from the existing browser package version.
- `system_model`: the existing system input model, unchanged in meaning.
- `tgcv_model`: a separately typed TGCV graph model, with its own stable identifiers for transformations and typed relations.
- `mapping_records`: explicit cross-layer correspondences; each record identifies its source and target objects and the mapping origin.
- `derivation_rules`: optional named/versioned rules that generated a mapping or TGCV object.
- `derived_results`: outputs from a named computation, tied to the exact input identities and rule versions.
- `provenance`: provenance needed to distinguish user-declared, rule-derived, illustrative, and unresolved information.
- `integrity`: hashes/identity metadata for package components, following the existing demonstrator's integrity conventions.

Do not require all TGCV information to be present at initial import. An unresolved or absent TGCV graph is a valid state of the user workflow, but must be labelled as such and must not be displayed as a completed derivation.

## 3. Mapping and provenance rules

Every mapping record must make explicit:

1. source layer and source object ID;
2. target layer and target object ID;
3. mapping kind or declared meaning;
4. provenance status: `user_declared`, `rule_derived`, `illustrative`, or `unresolved`;
5. rule ID and version when `rule_derived`;
6. enough origin detail to reproduce or review the mapping.

No implicit mapping is allowed based only on similar names, matching IDs, or visual proximity. An illustrative mapping remains illustrative after export/import; it must never be upgraded to observed or validated evidence by serialization.

## 4. Identity and stale-result invalidation

A result is current only if the identities of all inputs and rules it depends on still match. At minimum, dependency identity must cover:

- system model content and relevant scenario;
- TGCV model content;
- mapping records;
- derivation/trajectory rule IDs and versions;
- computation configuration that affects the result.

When any dependency changes, mark the dependent result stale or unavailable. Do not silently recompute in the background and present a result as if it were the prior one. A changed model hash alone is not sufficient user-facing behavior: the interface must identify which output is stale and which dependency changed.

Changes to the outcome or contextual value assessment must not invalidate unrelated graph structure results unless the declared dependency model explicitly says they do. Conversely, changing TGCV accessibility or its derivation rule must invalidate TGCV reachability/trajectory outputs that depend on it.

## 5. Import behavior

- **Legacy single-model package:** validate and load as the system model and existing result package only. TGCV graph status is “not supplied”; do not invent one.
- **Valid dual-graph package:** validate package version, each layer independently, mapping endpoints, provenance, rule references, and result dependencies before enabling derived outputs.
- **Partially specified dual-graph package:** retain valid supplied data for inspection, but mark missing/invalid mappings and dependent results unresolved or stale. Never silently repair semantic links.
- **Unsupported future version or invalid integrity metadata:** reject as executable/current data, while offering an inspect-only error report where the existing UI supports it.
- **Imported result with mismatched dependencies:** do not label it current or replay-verified. Preserve the supplied bytes for inspection only if the existing import policy permits it.

## 6. Export behavior

- Export both graph layers and mapping/provenance data in one versioned package, without merging their identifiers or semantics.
- Include rule versions and the dependency identities for derived results.
- Preserve the current package's explicit execution/outcome/value distinctions.
- Do not claim that exported or replay-verified synthetic results constitute empirical TGCV validation.
- Round-trip acceptance must compare semantic content, provenance, and dependency state, not only whether JSON parses.

## 7. Minimum adversarial acceptance cases

1. A legacy single-model export imports without fabricating a TGCV graph.
2. Two objects with the same string ID in different layers remain distinct.
3. A mapping to a nonexistent object is rejected or explicitly unresolved; it is never silently redirected.
4. A mapping with `rule_derived` provenance but missing rule/version is not treated as reproducible.
5. Editing only the system graph marks dependent mappings/results stale where required, but does not erase unrelated TGCV data.
6. Editing only the TGCV graph invalidates TGCV reachability/trajectory results but does not rewrite system execution history.
7. Changing a derivation rule version invalidates outputs that cite the previous version.
8. Illustrative objects and mappings remain visibly illustrative after export/import.
9. Tampered dependency hashes prevent a result from being presented as current.
10. A package with a valid system graph but incomplete TGCV graph can still be inspected without implying that the TGCV derivation is complete.

## 8. Implementation boundary

This contract does not authorize:
- changes to `main`, the current schema, or the existing package format;
- a new package version or schema migration;
- TGCV engine calculations, condition evaluation, or value-causality claims;
- scientific execution.

## 9. Required review before code

Review this proposal alongside:
- `MINIMAL_DUAL_GRAPH_DATA_CONTRACT_001.md`;
- `TGCV_GRAPH_DERIVATION_CONTRACT_001.md`;
- `DUAL_GRAPH_CURRENT_SOURCE_AUDIT_001.md`;
- `DUAL_GRAPH_ADAPTATION_MATRIX_001.md`.

If accepted, the next implementation plan should identify the smallest increment that can render a separately typed TGCV graph with the illustrative case while leaving system execution unchanged. Persistence changes should follow only after the package contract is accepted.
