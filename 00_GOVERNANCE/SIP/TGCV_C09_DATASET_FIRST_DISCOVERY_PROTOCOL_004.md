# TGCV C09 — Dataset-First Discovery Protocol 004

**Date:** 2026-09-14  
**Status:** FROZEN — CROSS-SOURCE DATA-FUSION ROUTE ADOPTED AS SECONDARY C09 DISCOVERY PATH  
**Supersedes:** `TGCV_C09_DATASET_FIRST_DISCOVERY_PROTOCOL_003.md` for future C09 discovery  
**Scope:** C09 real-world candidate discovery only

## 1. Purpose

Protocol 003 remains the primary route: search for one public, reproducible real-world case containing the structural accessibility transition and an independent downstream trajectory in a causally identifiable architecture.

Protocol 004 adds a **secondary data-fusion route** for the common real-world situation in which the upstream accessibility transition and the downstream outcome/value trajectory are generated, measured or governed by different organisations and therefore reside in different public datasets.

This is not a relaxation of C09 identification. It is an explicit recognition that the empirical chain

`accessibility / transformation → downstream outcome / value`

may cross institutional and data-system boundaries.

The methodological literature explicitly recognises causal inference with multiple heterogeneous datasets and settings in which no single dataset contains all relevant variables. Data fusion can therefore be legitimate, but only under explicit linkage, transportability and identification conditions. citeturn0search0turn0search5

## 2. Strategic decision

The discovery route is now:

`single-source candidate search → D6-E → D1–D5`

with a secondary branch:

`cross-institutional data-fusion candidate → D6-E-F → D1–D5-F → D6`

The secondary branch is activated when repeated otherwise-promising candidates fail **only because the downstream trajectory Y is not contained in the same public source as the structural transition**, while the institutional/data architecture makes a reproducible linkage to a second public source plausible.

A data-fusion candidate must never be admitted merely because two datasets can be joined. The joined evidence must support the same bounded C09 causal estimand and must preserve the temporal and causal ordering.

## 3. C09 data-fusion target

The target remains:

`Z → ΔT_acc → Y`

but the observed evidence may be distributed as:

- **Source A — upstream/structural:** `unit, t0, t1, S0, S1, T_acc,0, T_acc,1, Z`;
- **Source B — downstream:** `unit, t>1, Y` and the baseline variables required for causal identification/transportability;
- optionally **Source C — bridge/confounding:** common identifiers, geography, institutional identifiers, baseline covariates, cohort information, or mechanism variables.

The sources may belong to different organisations. This is admissible in principle and may be the empirically natural representation of the system under study.

## 4. D6-E-F — Early fusion-feasibility gate

Before investing in D1–D5-F, verify:

1. Source A is publicly accessible at the required unit/time granularity.
2. Source B is publicly accessible at the required unit/time granularity.
3. A reproducible linkage key exists between A and B: stable unit ID, facility/school/municipality ID, geographic key, address/geocode or another defensible linkage mechanism.
4. The linkage does not require private credentials, proprietary crosswalks or case-by-case author intervention.
5. The linkage preserves the temporal ordering `t0 → t1 → t>1`.
6. Source A contains the structural transition and intervention variables.
7. Source B contains an independently defined downstream trajectory/value outcome.
8. The variables needed to address major confounding, selection, spillover and mechanism-identification threats are available in at least one source or can be bounded by design.
9. Source identity, versions and transformations can be frozen and audited independently for each source.

D6-E-F statuses:

- **PASS:** both public sources and a reproducible linkage path are demonstrably available.
- **CONDITIONAL:** both sources are public, but one narrow linkage/variable issue requires bounded D1 verification.
- **FAIL:** either core source, linkage, or essential identification variable is restricted, proprietary, aggregate-only or unavailable.
- **UNKNOWN:** public availability/linkage is not yet established; only minimal targeted verification is authorised.

## 5. D1-F — Cross-source structural transition

The same causal unit must support:

`S_A,t0 → S_A,t1 → Y_B,t>1`.

`T_acc,0` and `T_acc,1` must be defined from Source A without using downstream observations from Source B.

The downstream source must not be used retrospectively to redefine the accessibility representation.

Where Source B observes outcomes for persons/cohorts attached to a structural unit rather than the same physical entity, the unit-to-cohort mapping must be explicit and the estimand must state whether C09 is interpreted at structural-unit, person or cohort level.

## 6. D2-F — Intervention separation

`Z` must be identifiable from Source A or from a reproducible cross-source linkage.

If different organisations control different stages of the causal chain, their interventions must be represented separately where relevant:

`Z_A → ΔT_acc` and `Z_B / institutional process → Y`.

A second dataset must not be used to hide an unresolved direct pathway from the original intervention.

## 7. D3-F — Stable cross-source unit

The linkage must establish a stable unit or a defensible hierarchical mapping:

`unit_A,i,t0 → unit_A,i,t1 → unit_B,i,t>1`.

Preferred linkage hierarchy:

1. exact persistent unit identifier;
2. official stable institutional identifier;
3. reproducible geographic unit with deterministic crosswalk;
4. validated probabilistic linkage with quantified linkage uncertainty.

Purely aggregate geographic correlation without a defensible unit/time mapping is not sufficient for ordinary C09 admission.

## 8. D4-F — Independent downstream trajectory

Source B must provide a genuine downstream trajectory/value variable that is conceptually independent of the structural transition measured in Source A.

Examples may include:

- educational attainment/performance after infrastructure access;
- productivity or labour outcomes after transport/digital access;
- health or welfare outcomes after service accessibility;
- firm performance after infrastructure/capability access;
- economic/value outcomes after a structural transformation.

The downstream variable must not simply be the same structural access variable, an immediate adoption/use measure, or an intermediate implementation step.

## 9. D5-F — Fusion-specific mechanism-identification gate

Data fusion does not by itself identify `ΔT_acc → Y`. The following must be addressed explicitly:

### D5-F.1 Linkage validity

The linkage between Source A and Source B must be sufficiently accurate for the estimand. If linkage is probabilistic, uncertainty must be incorporated or bounded.

### D5-F.2 Causal transportability / common mechanism

If Source A and Source B are drawn from different populations, institutions or sampling systems, the analysis must state why the relevant causal mechanism is transportable between them, or restrict the estimand to a common target population.

The existence of common variables is not sufficient evidence of causal transportability.

### D5-F.3 Confounding and selection

The fusion design must address selection into Source B and any variables that jointly affect accessibility and Y. If a variable is available only in one source, the identification strategy must explicitly account for that limitation.

### D5-F.4 Alternative pathways

The analysis must enumerate direct effects of Z, complementary interventions, institutional changes, adoption/use, spillovers and other mechanisms. Cross-source separation is admissible only if these pathways are separately measured, randomized, blocked, bounded or otherwise identified.

### D5-F.5 Fusion classification

- **D5-F-A — IDENTIFIED:** cross-source linkage and causal bridge are identified under defensible assumptions/design.
- **D5-F-B — BOUNDED / ASSUMPTION-EXPLICIT:** point identification unavailable, but the accessibility-mediated contribution is meaningfully bounded.
- **D5-F-C — DIAGNOSTIC ONLY:** fusion produces informative association/diagnostic evidence but causal bridge remains unresolved.
- **D5-F-FAIL:** the fused evidence supports only total treatment/access effects or cross-sectional association.

C09 candidate admission requires D5-F-A or D5-F-B.

## 10. Data-fusion configurations to prioritise

D0 ranking should prioritise, in order:

1. **Same stable structural unit, different institutional data owners:** e.g. infrastructure provider + education/health/labour outcome system.
2. **Factorial or separately randomized upstream intervention + independent longitudinal downstream registry/survey.**
3. **Infrastructure/accessibility administrative source + public longitudinal household/firm outcome source with deterministic linkage.**
4. **Common geographic unit with repeated pre/post observations and an exogenous accessibility intervention, only when the geographic linkage is sufficiently fine and the estimand is explicitly defined.**
5. **Distributed datasets with shared instruments/anchors supporting formal data-fusion identification.**

The literature confirms that causal inference can be performed when treatment, mediator, outcome and relevant covariates are distributed across heterogeneous sources, but identification requires explicit assumptions about linkage and causal transportability. citeturn4search0turn4search1turn4academia12

## 11. Important distinction: dataset fusion versus evidence stitching

The following are **not** admissible as C09 data fusion:

- combining unrelated studies because they concern the same broad intervention;
- using an effect from Source A and a different effect from Source B without a common unit/population linkage;
- inferring `ΔT_acc → Y` from two separate papers;
- using aggregate treatment effects from one source and aggregate outcomes from another without a causal bridge;
- assuming that similar populations imply transportability;
- replacing missing unit-level linkage with narrative institutional plausibility.

The minimum requirement is a reproducible statistical/data linkage architecture connecting the upstream structural transition to the downstream outcome population.

## 12. Mandatory discovery table — extension

For data-fusion candidates the standard table is extended with:

| Candidate | Source A | Source B | Unit key | t0 | t1 | tY | T_acc,0 | T_acc,1 | Z | Y | Linkage type | Linkage uncertainty | Transportability basis | D6-E-F | D5-F | D6 | C09 potential |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

The original Protocol 003 table remains mandatory for single-source candidates.

## 13. Trigger for the secondary route

The data-fusion route becomes the **preferred secondary route** when at least three materially different otherwise-promising real-world candidates have failed D4 because the upstream accessibility transition and the independent downstream trajectory are held by different public/institutional data systems, while D0, D6-E and D1–D3 are otherwise promising.

This trigger is a search-policy rule, not a scientific stopping rule. A clearly superior fusion candidate may be screened earlier if encountered.

## 14. Interpretation discipline

The central distinction remains:

`Z → Y` ≠ `Z → ΔT_acc → Y`.

With two datasets, an additional distinction is required:

`Source A + Source B` ≠ causal bridge.

The bridge requires stable linkage, temporal ordering, causal identification/bounding and, where populations differ, defensible causal transportability.

A data-fusion design may therefore provide a **more realistic representation of real-world value construction** while simultaneously making the identification problem harder. The protocol must preserve that tension rather than treating data fusion as a shortcut.

## 15. Decision

**Protocol 004 adopts cross-source data fusion as a controlled secondary C09 discovery route.**

It does not modify the C09 scientific claim, lower the D5 standard, reopen rejected candidates, or authorize execution.

The next discovery operation is therefore:

`continue single-source D0 + D6-E search; in parallel, record promising cross-institutional architectures and activate D6-E-F when the three-failure trigger is reached or when an exceptionally strong fusion candidate appears.`

No automatic Core/RMA/Evidence Matrix/STATUS update is authorized by this protocol.