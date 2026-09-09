# D-OPS-24 — Directed Documentary Accessibility Search Result v0.1

**Date:** 2026-09-09  
**Status:** COMPLETED / BOUNDED DOCUMENTARY SEARCH  
**Scientific impact:** NO SCIENTIFIC CLAIM CHANGE

## 1. Execution scope

The search was executed against a finite set of documentary architectures selected directly from the frozen D-OPS-24 search families. The target was not an industrial case or favorable technology, but an operational domain in which Class-A normative/operational evidence might independently specify admissible alternatives and, together with public state/context evidence, distinguish an unobserved candidate from an inaccessible one.

Screened domains:

1. **Aviation flight planning / EUROCONTROL RAD** — Route Availability Document, flight-planning requirements and AIRAC material.
2. **Railway signalling / route setting** — public railway signalling and interlocking rules specifying route-setting conditions.
3. **Electricity transmission system operation / remedial actions** — EU System Operation Guideline and ENTSO-E operational-model documentation.

Previously screened event-log families were not re-opened as candidates; their prior failures remain unchanged and served only as the frozen exclusion baseline.

## 2. Result matrix

| ID | Domain | System / unit | Class-A specification | State/context closure | Accessibility/admissibility closure | Adjudication | Disposition |
|---|---|---|---|---|---|---|---|
| D24-01 | EUROCONTROL flight planning | One flight-plan route decision for a bounded AIRAC period | **PASS-BOUND** — RAD provides coordinated routing rules and availability constraints; IFPS specification defines route validation against RAD rules | **FAIL / INCOMPLETE** — public documentary material does not expose all decision-time aircraft/operator constraints, temporary operational state and complete IFPS input state needed to reconstruct accessibility for a specific decision | Cannot distinguish every unselected route from an inaccessible route using public documentary evidence alone | **INCONCLUSIVE** | Not retained for IT-G1 |
| D24-02 | Railway signalling / interlocking | One route-setting decision at a bounded signalling control point | **PASS-BOUND** — published signalling rules define preconditions for route setting and interlocking protection | **FAIL / INCOMPLETE** — public rules specify required conditions, but the complete contemporaneous interlocking/track-circuit/route-locking state for a real decision is not independently available in the documentary corpus | Rules do not by themselves establish which candidate routes were accessible at the exact decision time | **INCONCLUSIVE** | Not retained for IT-G1 |
| D24-03 | Electricity transmission remedial action | One bounded TSO operational-security decision | **PASS-BOUND** — EU regulation specifies system states, remedial-action categories, selection criteria and required analyses | **FAIL / INCOMPLETE** — operational state estimation, detailed observability area, available remedial-action set and some TSO-specific limits/conditions are not fully reconstructable from public documentary sources at decision time | Normative action categories do not independently close the actual accessible transformation set | **INCONCLUSIVE** | Not retained for IT-G1 |

## 3. Source basis

### D24-01 — Aviation

EUROCONTROL states that the RAD is a central source for route-network availability, utilisation rules and free-route-airspace information, maintained and published ahead of AIRAC cycles. The EUROCONTROL Initial Flight Plan specification states that the RAD provides an integrated list of routing rules and requirements and that submitted flight plans are validated against RAD rules. These sources establish a strong Class-A normative layer. They do not, however, expose the complete aircraft/operator/temporary operational state required to determine the accessible set for a specific flight-planning decision.

Sources:
- EUROCONTROL RAD: https://www.nm.eurocontrol.int/RAD/
- EUROCONTROL Initial Flight Plan Specification v3.0: https://www.eurocontrol.int/sites/default/files/2024-03/eurocontrol-ifpl-specification-v3-0.pdf
- EUROCONTROL RAD/DCT documentation: https://www.eurocontrol.int/publication/direct-routing-dct-chart-route-availability-document-rad-airac-2014

### D24-02 — Railway signalling

RSSB signalling material provides explicit route-setting/interlocking principles. The published ERTMS signalling regulation specifies preconditions before setting routes or issuing movement authorities, including conflict protection, interlocking availability and route closure conditions. This is strong Class-A operational specification. The documentary corpus does not independently provide the complete contemporaneous signalling state necessary to enumerate all routes accessible at a particular real-world decision time.

Sources:
- RSSB Interlocking Principles: https://www.rssb.co.uk/standards-catalogue/CatalogueItem/GKRT0060-Iss-3
- RSSB signalling regulation / route setting material: https://consultations.rssb.co.uk/_entity/sharepointdocumentlocation/355b21ce-483e-f111-88b5-000d3ab84277/2ab10dab-d681-4911-b881-cc99413f07b6?file=09.+GERT8000-TS10.pdf

### D24-03 — Electricity transmission

EU Regulation 2017/1485 establishes system-state definitions, remedial-action categories and selection criteria, including availability, timing, risk and operational-security constraints. ENTSO-E publishes CGMES documentation supporting network-model exchange. Nevertheless, the regulation explicitly relies on real-time state estimation, TSO-specific operational-security limits, observability areas and available remedial actions. These decision-time inputs are not completely reconstructable from the public documentary corpus alone.

Sources:
- EUR-Lex Regulation (EU) 2017/1485: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32017R1485
- ENTSO-E CGMES Library: https://www.entsoe.eu/data/cim/cim-for-grid-models-exchange/

## 4. Adjudication logic

No candidate reached documentary **PASS** because every otherwise promising Class-A architecture retained a material Class-B/state-context gap at the decision time. In each case, the evidence supports the existence of normative admissibility rules but does not independently close the complete accessible transformation set for an actual decision instance.

The result therefore does **not** establish that industrial accessibility is impossible or that normative specifications are insufficient in principle. It establishes only that, within this finite search scope, the public documentary evidence did not close the additional state/context conditions required by the frozen D-OPS-24 criterion.

## 5. Stop condition

No candidate reached the threshold for a separately governed IT-G1 review. The authorized documentary scope is therefore exhausted without a PASS candidate.

## 6. Anti-rescue confirmation

- TGCV Core: unchanged.
- C01–C16: unchanged.
- O3 status: unchanged / not closed.
- Industrial utility: remains UNPROVEN / OPEN.
- No dataset execution.
- No partner evidential engagement.
- No causal or value inference.
- No criterion relaxation.
- No retrospective reinterpretation of prior failures.

**D-OPS-24 RESULT = COMPLETED / NO DOCUMENTARY ACCESSIBILITY PASS / NO IT-G1 CANDIDATE GENERATED**
