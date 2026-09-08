# D-OPS-10 — Railway State-Identity / Historical-Version Reconstruction Audit v0.1

**Status:** CLOSED — LONGITUDINAL BRIDGE NOT ESTABLISHED
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Scope

D-OPS-10 tests whether the public ADIF railway-network resources identified in D-OPS-9 can provide a common, historically comparable state representation, and whether that state representation can be paired consistently with the independently governed EULYNX rule layer.

No dataset was downloaded or executed. The audit is based on public catalogue/provenance evidence only.

## 2. Historical resources identified

The official Spanish open-data catalogue exposes a **Red de Transporte Ferroviario de Adif** resource whose April 2018 entry provides WFS/WMS services and identifies the resource as an INSPIRE Transport Networks dataset. citeturn0search1

A separate catalogue entry identifies the same ADIF resource as **version July 2024**, with a public INSPIRE metadata record. citeturn0search3turn0search13

This establishes that historical/versioned public representations exist at least at catalogue level.

## 3. EULYNX rule-layer reconstruction

EULYNX Baseline Set 4 Release 4 was published in June 2025 and is described as having reached stable maturity and being closed to functional changes/new features. The release includes 25 jointly published specifications plus additional EULYNX specifications and supporting artefacts; requirements are available in ReqIF and model-based deliverables have model exports. citeturn0search0turn0search31

EULYNX documentation explicitly identifies signalling/interlocking system concepts, including interlocking system boundaries, routes and flank-protection-related concepts. citeturn0search33turn0search7

Therefore, the rule layer has strong version/provenance structure.

## 4. State-identity reconstruction assessment

| Criterion | Result | Finding |
|---|---|---|
| D10-1 Historical state artefacts identifiable | PASS | 2018 and 2024 ADIF catalogue resources are identifiable. |
| D10-2 Exact raw distributions/hashes | FAIL | Catalogue evidence identifies services/metadata, but does not provide sufficient evidence here for exact immutable 2018/2024 distribution bytes and hashes. |
| D10-3 Common state schema | CONDITIONAL | Both are INSPIRE railway transport-network representations, which strongly suggests a common conceptual schema, but exact field-level historical equivalence has not been demonstrated. |
| D10-4 Stable object identity across versions | FAIL/OPEN | The current evidence does not establish that persistent identifiers can be matched exhaustively and unambiguously across the two historical versions. |
| D10-5 Geometry/topology comparability | CONDITIONAL | Both represent railway transport networks, but geometric/feature changes cannot be treated as canonical state changes without a frozen identity and normalization procedure. |
| D10-6 EULYNX rule compatibility across historical states | FAIL/OPEN | EULYNX Baseline Set 4 R4 is a 2025 rule release; applying it retrospectively to 2018/2024 infrastructure would require an explicit historical compatibility justification. |
| D10-7 Independent Uτ | CONDITIONAL | A bounded signalling/interlocking transformation universe remains possible, but cannot yet be anchored to stable historical object identities. |
| D10-8 Non-trivial Pτ | CONDITIONAL | EULYNX provides an independent rule layer, but the exact subset applicable to the reconstructed historical state is not frozen. |
| D10-9 Longitudinal ΔT_acc | FAIL | Without D10-4 and D10-6, exact comparison of accessibility spaces at two historical states would be underdetermined. |
| D10-10 Reach separability | CONDITIONAL | Structural successors are conceptually possible, but successor identity inherits the unresolved state/object identity problem. |
| D10-11 Reproducibility | CONDITIONAL | Rule releases are well versioned; historical ADIF distributions require stronger archival provenance for byte-level reproduction. |
| D10-12 Cross-domain information gain | PASS | Railway engineering remains genuinely external to Rust package evolution. |

## 5. Critical result

The strategy change from **dataset-first** to **rule-layer-first** was productive: D-OPS-9 established that EULYNX supplies a materially stronger independent rule layer than the previously rejected domains.

However, D-OPS-10 shows that the missing piece is now narrower and decisive:

> **We do not yet possess an auditable longitudinal railway state identity that can be paired with the rule layer without retrospective semantic assumptions.**

The existence of 2018 and 2024 catalogue versions is not sufficient to establish a common canonical state space.

## 6. Decision

**D-OPS-10 = CLOSED — NO EMPIRICAL SELECTION.**

Current railway route:
- EULYNX rule layer: **RETAINED**;
- ADIF historical state resources: **RETAINED AS ARCHIVAL CANDIDATES**;
- common historical state identity: **NOT ESTABLISHED**;
- longitudinal `ΔT_acc`: **NOT IDENTIFIABLE YET**;
- operational specification: **NOT FROZEN**;
- dataset execution: **NOT AUTHORIZED**.

No TGCV claim is upgraded.

## 7. Methodological consequence

At this point, the empirical replication problem has decomposed into two independently necessary assets:

1. an independently governed rule layer defining `Pτ`;
2. an auditable longitudinal state history with stable identity.

Rust currently satisfies both sufficiently for its bounded empirical result. Railway engineering satisfies the first strongly but not the second. This is itself useful methodological information: **rule-layer identifiability and longitudinal-state identifiability are separate gates and must not be conflated.**

## 8. Next controlled operation

Open **D-OPS-11 — Longitudinal State Archive Discovery / Railway Historical Data Recovery Audit**.

D-OPS-11 should search specifically for immutable historical railway-network archives, snapshots, versioned geospatial packages or dated infrastructure datasets that can establish stable object identity across time. It should not redesign the EULYNX rule layer unless new evidence requires it.

Selection remains prohibited until both the rule-layer and longitudinal-state gates pass.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
