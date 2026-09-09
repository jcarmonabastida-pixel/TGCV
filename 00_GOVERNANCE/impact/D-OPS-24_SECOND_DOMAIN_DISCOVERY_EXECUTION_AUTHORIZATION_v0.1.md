# D-OPS-24 — Second Independent Domain Discovery Execution Authorization v0.1

**Date:** 2026-09-09
**Status:** AUTHORIZED / EXECUTION RELEASED
**Parent decision:** `EXT-UPD-4.6_SECOND_DOMAIN_ROUTE_DECISION_v0.1.md`
**Design:** `D-OPS-24_SECOND_DOMAIN_DISCOVERY_DESIGN_v0.1.md`
**Preflight:** `D-OPS-24_SECOND_DOMAIN_DISCOVERY_PREFLIGHT_v0.1.md`

## 1. Authorization scope

One controlled documentary discovery pass is authorized to identify candidates for the second independent TGCV domain. This authorization does not authorize translation, dataset acquisition, empirical execution, or downstream conformance testing.

## 2. Frozen search families

The first release uses four discovery families, selected to maximize domain diversity while preserving native-first discovery:

- **QF-01 Biological/ecological adaptive systems**
- **QF-02 Technological infrastructure/network reconfiguration**
- **QF-03 Manufacturing/process reconfiguration**
- **QF-04 Organizational/coordination systems**

For each family, the executed query must combine the fixed conceptual dimensions: native state/configuration, transformation/change/reconfiguration, feasibility/accessibility/constraint, temporal ordering, and the family-specific native terminology. Exact engine syntax may vary only for mechanical adaptation (for example, quotation marks or documented search-field syntax); semantic query content may not be broadened or changed without recording a new QF.

## 3. Source restrictions

Discovery is restricted to scholarly/documentary sources with identifiable provenance, prioritizing primary papers/reports and authoritative repositories or publishers. Search-result inspection and following a candidate's primary-source link are permitted. No candidate is accepted from an unattributed secondary claim alone.

## 4. Budget

- Total authorized QFs: **4 / 12 maximum**.
- Candidate records: **maximum 30** across this release.
- Maximum QFs per candidate family: **3**.
- Budget is cumulative across engines, sessions and operators.
- No reuse/reset of the historical v0.4 F2 budget.
- This authorization consumes QF budget only when an exact QF is executed.

## 5. Candidate record

Each candidate record must capture, at minimum:

1. candidate ID;
2. native domain/system description;
3. primary source/provenance;
4. evidence of independence from Rust/C-01/prior TGCV instantiations;
5. native state/configuration construct;
6. native transformation/change construct;
7. native feasibility/accessibility concept;
8. temporal/state ordering evidence;
9. preliminary MTE readiness;
10. preliminary independence status;
11. decision class;
12. exclusion/failure reason where applicable.

## 6. Outcome-blindness

Search and candidate screening must not use observed success, performance, value, empirical confirmation, or expected TGCV compatibility as a selection criterion. If such information appears in a source, it may be recorded only where needed to distinguish the native construct, and cannot determine candidate selection.

## 7. Stop rules

Stop the release immediately if:

- a material query change would be required;
- QF budget would be exceeded;
- candidate-record budget would be exceeded;
- a candidate cannot be screened without outcome-defined accessibility;
- independence cannot be assessed without importing prior TGCV constructs;
- dataset acquisition or empirical execution would become necessary;
- the operator encounters a governance ambiguity affecting eligibility.

Any deviation creates a separate governance record before continuation.

## 8. Candidate decision rule

A candidate can become **ELIGIBLE FOR TRANSLATION TRACE** only after documentary Stage A, MTE and TR screening under the frozen v0.5 architecture. Otherwise classify as REJECTED or INDETERMINATE according to the design.

Discovery itself does not establish TGCV conformance, generalization, causality, prediction, value creation, originality, or superiority.

## 9. Evidence governance

The executed discovery log and any material candidate-screening evidence shall receive explicit Evidence→Claim impact assessment before the resulting scientific state is propagated and closed.

## 10. Explicit exclusions

Not authorized:

- dataset download or processing;
- empirical execution;
- causal or predictive analysis;
- value optimization or value inference;
- modification of TGCV Core;
- revision of C-01 A/B/C;
- downstream ETC execution;
- external-asset refresh;
- opening a further domain route without a new governance decision.

## 11. Release

**EXECUTION RELEASED for QF-01 through QF-04 only, under the frozen controls above.**
