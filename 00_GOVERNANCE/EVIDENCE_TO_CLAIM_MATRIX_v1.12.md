# TGCV — Evidence-to-Claim Matrix — v1.12

**Status:** GOVERNANCE CONTROL ARTIFACT — CUMULATIVE VERSION
**Date:** 2026-09-16
**Predecessor:** v1.11
**Construction rule:** v1.12 preserves v1.11 as immutable predecessor and adds the complete MT4 evidence-propagation layer below. No v1.11 evidence, schema, claim status or prior propagation is retired, collapsed or downgraded.

> **Canonical assembly note:** This version is the additive cumulative successor to v1.11. The immutable predecessor remains `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.11.md`. The current alias must ultimately contain the predecessor's complete content followed by this v1.12 addition; no simplified derivative is authorized.

## v1.12 update — complete MT4 domain-transfer evidence

**Primary result:** `00_GOVERNANCE/SIP/TGCV_MT4_DOMAIN_TRANSFER_RESULT_001.md`

**Propagation record:** `00_GOVERNANCE/SIP/TGCV_MT4_EVIDENCE_TO_CLAIM_PROPAGATION_001.md`

**Status:** `BOUNDED PASS — METHODOLOGICAL TRANSFER DEMONSTRATED WITH EXPLICIT LIMITS`

MT4 demonstrates transfer of the candidate TGCV analytical methodology to a genuinely heterogeneous historical national electricity-system domain while preserving the separation among state, candidate transformations, admissibility/accessibility, realized transformations, trajectory/state evolution and downstream economic/value-related variables.

### MT4 gate record

- **MT4-1:** PASS
- **MT4-2:** PASS
- **MT4-3:** PASS
- **MT4-4:** PASS — BOUNDED
- **MT4-5:** OPEN / BOUNDED
- **MT4-6:** PASS — independent reproducibility
- **MT4-7:** BOUNDED PASS — downstream separation
- **MT4-8:** BOUNDED PASS — value isolation

### Frozen source

Primary source: Jaxa-Rozen, Wen & Trutnevyte, *Historic data of the national electricity system transitions in Europe in 1990–2019 for retrospective evaluation of models*, Zenodo record 6696776, v2, DOI `10.5281/zenodo.6696776`.

Frozen local package: `C:\Users\pedri\Downloads\TGCV_MT4_energy_public-dataset_v2.zip`

SHA256: `691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`

The source covers 31 European countries, 1990–2019, 1,359 processed/harmonized data files and 528 original references. Technology records include candidate technical parameters, realized transformations, state/trajectory variables and economic/value-related variables.

### MT4-4 bounded operationalization result

The frozen source contains state variables, candidate transformation attributes, technical/economic constraints, resource relations, legal/planning information and historical realizations. However, it does not establish a complete clean `(S_t,C_t,L_t,U_tau) → P_tau` construction without temporal or semantic qualification.

Important temporal boundaries were identified:

- `Buildrates` frequently incorporates historical maxima and therefore is not automatically ex ante.
- `Potential_installed` is heterogeneous and can mix technical potential, current capacity, planned plants, legal status and master plans.
- `Potential_annual` contains retrospective corrections and historical-value assumptions and therefore cannot automatically be treated as ex ante accessibility.
- `Actual_*` variables are observed/reconstructed realization variables, not accessibility.
- The technical inventory does not by itself prove sufficiency for a complete `P_tau`.

### MT4-5 bounded structural result

The temporal audit found 39,960 relevant records, with 2,101 initially flagged as future leakage, 12,840 retrospective and 5,059 requiring review. The protocol explicitly treats these counts as review signals rather than final leakage counts because some records such as `Based on 2010 estimate` may be misclassified when the reference year is contemporaneous with the audited year.

The CORE6 candidate technical layer was:

`Fuel_efficiency | LF_min | LF_max | Peak_contr | Ramp_rate | Resource`

Coverage across 13,320 country-technology-year cells was:

- complete CORE6: 12,331
- incomplete CORE6: 989
- coverage: 92.58%

CORE6+Lifetime was complete in only 411 cells (3.09%); CORE6+Potential_installed in 3,507 cells (26.33%). Therefore `SUFFICIENT_FOR_P_tau = UNDETERMINED`.

The initial 802 `LF_min > LF_max` anomalies were diagnosed as parser/culture artifacts. With the corrected invariant parser, `LF_INCONSISTENCY_CELLS=0`; no data repair or imputation was performed.

The 989 CORE6 incomplete cells have structured missingness: 89 missing `Fuel_efficiency` records, all CHE gas/hard-coal/oil cases, and 900 missing `Ramp_rate` records, all Storage. Storage `Ramp_rate` is not treated as conceptually irrelevant merely because it is missing; the source/reference structure indicates a genuine missing-source/model parameter boundary.

CORE6 variation/discrimination showed:

- `Fuel_efficiency`: 13,231 nonblank / 4,605 unique numeric values
- `LF_min`: 13,320 / 722
- `LF_max`: 13,320 / 1,189
- `Peak_contr`: 13,320 / 10
- `Ramp_rate`: 12,420 / 4
- `Resource`: 13,320 / 19 categorical values

Across 930 country-year groups with at least two technologies, 930 had distinct CORE6 signatures; only one group contained a duplicate signature: Estonia 1990 HydroRoR/HydroDam. The duplicate was resolved diagnostically by `Potential_annual`, but no additional collision search was authorized.

### MT4-6 independent reproducibility

The independent reproducibility audit reproduced:

- 13,320 country-technology-year cells
- 12,331 complete CORE6 cells
- 989 incomplete CORE6 cells
- 92.58% CORE6 coverage
- 89 missing `Fuel_efficiency`
- 900 missing `Ramp_rate`
- 930 multi-technology country-year groups
- 930 groups with distinct CORE6 signatures
- 1 group with duplicate CORE6 signature

MT4-6 is therefore PASS as an independent structural reproducibility result. It does not establish full `P_tau`.

### MT4-7 downstream separation

The frozen source was structurally partitioned into:

- technology parameter rows: 254,421
- candidate technical rows: 79,920
- realized transformation rows: 26,640
- state/trajectory rows: 26,640
- economic/value-related rows: 39,960
- other rows: 81,261

Candidate technical variables were `Fuel_efficiency`, `LF_min`, `LF_max`, `Peak_contr`, `Ramp_rate`, `Resource`.

Realized transformations were `Actual_new_capacity`, `Actual_retired_capacity`.

State/trajectory variables were `Actual_capacity`, `Actual_generation`.

Economic/value-related variables were `Inv`, `Fixed_OM_annual`, `Variable_OM`.

Candidate-rule/actual overlap violations were zero. Outcome layer was not established by this structural audit, and no trajectory causal estimand was produced.

### MT4-8 value isolation

The value-isolation audit found:

- CORE6 rows: 79,920
- `Inv`: 13,320
- `Fixed_OM_annual`: 13,320
- `Variable_OM`: 13,320
- actual rows: 53,280
- CORE6/value overlap violations: 0

The value-related parameters span 1990–2019, but their common temporal span does not by itself establish that they are downstream value outcomes; they may be economic model inputs. Therefore the endpoint remains `NOT_ESTABLISHED_AS_TGCV_DELTA_V` and any causal value effect remains untested.

### Claim propagation

**C01 — bounded methodological support.** MT4 demonstrates that system state/conditions and transformation-related constraints can be reconstructed in a heterogeneous electricity-system domain, with explicit boundaries. No claim-level upgrade.

**C02 — bounded qualification.** MT4 independently demonstrates that candidate technical constraints can be separated from realized transformations and that a full admissibility predicate remains unresolved. CORE6 is only partially formalized; full `P_tau` remains undetermined. No upgrade.

**C07 — boundary qualification.** MT4 preserves the distinction between observed/realized technology change and accessibility-space change. It does not establish positive `Delta T_acc` as a TGCV result. No upgrade.

**C08 — bounded methodological support only.** MT4 demonstrates downstream/state-trajectory separation but does not establish a trajectory causal estimand. No upgrade.

**C09 — no positive propagation.** MT4 contains no independent causal test of accessibility change on subsequent trajectories. No upgrade or extension of the bounded C09 causal result.

**C10 — material boundary qualification.** MT4 structurally isolates economic/value-related variables from CORE6 candidate accessibility variables, but does not establish an independently downstream `Delta V` endpoint or `Delta T_acc → Delta V`. No upgrade.

**C11 — bounded cross-domain methodological evidence.** MT4 demonstrates transfer to a heterogeneous historical electricity-system domain, strengthening the documented domain-transfer record but not establishing general transversal validity. No upgrade.

**C16 — material methodological evidence.** MT4 preserves the distinctions among state, candidate transformations, accessibility, realization, trajectory and value-related variables and provides a new independent-domain application of the candidate translation protocol. No upgrade.

No positive propagation is made to C03, C04, C05, C06, C12, C13, C14 or C15.

### v1.12 claim-status preservation

The claim-status vector remains unchanged from v1.11:

`C01 E0; C02 E0; C03 E1; C04 E1; C05 E1; C06 E1; C07 E1; C08 H; C09 PASS — BOUNDED EMPIRICAL CAUSAL SUPPORT; C10 H; C11 H; C12 H; C13 O; C14 F; C15 F; C16 H.`

No Core modification. No RMA claim-level modification. No transversal-validity closure. No value-layer closure.

## v1.12 methodological routing after MT4 closure

The principal unresolved analytical bottlenecks remain:

1. independent formalization of a full `P_tau` where feasible; and/or
2. an independently defined downstream outcome/value endpoint capable of testing the downstream value layer without using value information to construct accessibility.

The second bottleneck is routed to **MT5** under the frozen protocol `00_GOVERNANCE/SIP/TGCV_MT5_DOWNSTREAM_VALUE_ENDPOINT_PROTOCOL_001.md`.
