$ErrorActionPreference='Stop'
$repo='jcarmonabastida-pixel/TGCV'
$root=(Get-Location).Path
$raw='https://raw.githubusercontent.com/'+$repo+'/main/00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md'
$rawV12='https://raw.githubusercontent.com/'+$repo+'/main/00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.12.md'
$current=(Invoke-WebRequest -UseBasicParsing -Uri $raw).Content
$v12=(Invoke-WebRequest -UseBasicParsing -Uri $rawV12).Content
if($current -notmatch 'Current v1\.11'){ throw 'REMOTE_CURRENT_IS_NOT_V1.11' }
if($v12 -notmatch 'v1\.12'){ throw 'V12_ARTIFACT_NOT_FOUND_OR_INVALID' }
$mt4=@'
## Material empirical/methodological evidence — MT4 Domain Transfer: Historical National Electricity-System Transitions

**Primary result:** `00_GOVERNANCE/SIP/TGCV_MT4_DOMAIN_TRANSFER_RESULT_001.md`
**Propagation:** `00_GOVERNANCE/SIP/TGCV_MT4_EVIDENCE_TO_CLAIM_PROPAGATION_001.md`
**Source freeze:** `00_GOVERNANCE/SIP/TGCV_MT4_SOURCE_FREEZE_MANIFEST_001.md`
**Status:** `BOUNDED PASS — METHODOLOGICAL TRANSFER DEMONSTRATED WITH EXPLICIT LIMITS`
**Source:** Jaxa-Rozen, Wen & Trutnevyte, *Historic data of the national electricity system transitions in Europe in 1990–2019 for retrospective evaluation of models*, Zenodo 6696776, v2.
**Frozen package SHA-256:** `691F950A314015A7DE9D4CBABCC177846D74ABF7036B6A89E192B152A88E6D30`

MT4 applies the candidate TGCV analytical methodology to a genuinely heterogeneous historical national electricity-system domain. The transfer preserves the distinction among state, candidate transformations, admissibility/accessibility, realized transformations, state/trajectory evolution and downstream economic/value-related variables. MT4 is a methodological domain-transfer result, not transversal scientific validation and not a claim-level upgrade.

### MT4 gate record

- **MT4-1:** PASS — source/domain discovery and admissibility.
- **MT4-2:** PASS — provenance/source freeze.
- **MT4-3:** PASS — structural/schema reconstruction.
- **MT4-4:** PASS — BOUNDED operationalization readiness.
- **MT4-5:** OPEN / BOUNDED — full `P_tau` remains undetermined.
- **MT4-6:** PASS — independent reproducibility.
- **MT4-7:** BOUNDED PASS — downstream separation.
- **MT4-8:** BOUNDED PASS — value isolation.

### MT4-4 — bounded operationalization

The frozen package contains country state/economic data, technology parameters, resource/fuel/CO2 data, load profiles and historical realizations. The technology inventory includes `Actual_capacity`, `Actual_generation`, `Actual_new_capacity`, `Actual_retired_capacity`, `Buildrates`, `Fuel_efficiency`, `LF_max`, `LF_min`, `Peak_contr`, `Ramp_rate`, `Resource`, `Potential_annual` and `Potential_installed` among other parameters. These support candidate transformation and feasibility analysis, but the source does not demonstrate a clean, complete ex-ante mapping `(S_t,C_t,L_t,U_tau) -> P_tau`.

`Actual_*` variables are realized/observed quantities and are not accessibility. `Potential_installed` is heterogeneous and can mix technical potential, current capacity, planned plants and legal/master-plan information. `Buildrates` are frequently retrospective. `Potential_annual` includes documented retrospective corrections/adjustments in some records. Therefore these variables cannot be promoted wholesale to `T_acc` or `P_tau`.

### MT4-5 — temporal and structural sufficiency audit

Frozen temporal audit totals: `TOTAL_RECORDS=39960`, `FUTURE_LEAKAGE_RECORDS=2101`, `RETROSPECTIVE_RECORDS=12840`, `REVIEW_REQUIRED_RECORDS=5059`. These are audit flags, not a final leakage determination; the `Based on 2010 estimate` rule can overclassify observations whose reference year is contemporaneous with the observation year.

The bounded CORE6 candidate set is `Fuel_efficiency|LF_min|LF_max|Peak_contr|Ramp_rate|Resource`. There are `13320` country-technology-year cells: `12331` complete (`92.58%`) and `989` incomplete. `CORE6+Lifetime` coverage is `411/13320 (3.09%)`; `CORE6+Potential_installed` coverage is `3507/13320 (26.33%)`. Full `P_tau` therefore remains `UNDETERMINED`.

The initial 802 `LF_min > LF_max` findings were a parser/culture artifact. The corrected invariant audit gives `LF_INCONSISTENCY_CELLS=0`; no repair or imputation was performed.

Missingness is structured: `Fuel_efficiency` missing in 89 cells, all CHE Gas/HardCoal/Oil; `Ramp_rate` missing in 900 cells, all Storage across 30 countries × 30 years. Storage `Ramp_rate` is not automatically N/A because the frozen source/reference material contains storage technologies for which ramp-rate information exists elsewhere. This is structured source/model missingness, not a random-missingness assumption.

CORE6 discrimination audit: `COMPLETE_CORE6_CELLS=12331`, `COUNTRY_YEAR_GROUPS=930`, `GROUPS_2PLUS_TECH=930`, `GROUPS_2PLUS_DISTINCT_SIGNATURES=930`, `GROUPS_WITH_DUPLICATE_SIGNATURES=1`, `GLOBAL_UNIQUE_SIGNATURES=5945`. The sole duplicate is `EST|1990` for HydroRoR and HydroDam; CORE6 is identical, while `Potential_annual` differs (`1746.027163` vs `589.783628`). No future/retrospective marker was identified in the targeted temporal audit for those two records. This leaves full `P_tau` unresolved rather than licensing post-hoc addition of `Potential_annual`.

### MT4-6 — independent reproducibility

The independent auditor reproduced the structural totals without using a prior audit output as an input: `TOTAL_COUNTRY_TECHNOLOGY_YEAR_CELLS=13320`, `COMPLETE_CORE6_CELLS=12331`, `INCOMPLETE_CORE6_CELLS=989`, `CORE6_COVERAGE_PCT=92.58`, with missingness counts `Fuel_efficiency=89`, `LF_min=0`, `LF_max=0`, `Peak_contr=0`, `Ramp_rate=900`, `Resource=0`, `COUNTRY_YEAR_GROUPS_2PLUS_TECH=930`, `GROUPS_2PLUS_DISTINCT_SIGNATURES=930`, `GROUPS_WITH_DUPLICATE_SIGNATURES=1`. MT4-6 is PASS.

### MT4-7 — downstream separation

The structural audit classified `Fuel_efficiency|LF_min|LF_max|Peak_contr|Ramp_rate|Resource` as candidate technical variables; `Actual_new_capacity|Actual_retired_capacity` as realized transformations; `Actual_capacity|Actual_generation` as state/trajectory variables; and `Inv|Fixed_OM_annual|Variable_OM` as economic/value-related variables. The audit found `CANDIDATE_RULE_ACTUAL_OVERLAP_VIOLATIONS=0`. Outcome and value endpoints were deliberately not inferred from this structural classification. MT4-7 is BOUNDED PASS.

### MT4-8 — value isolation

The value-isolation audit covered `254421` technology-parameter rows, `79920` CORE6 rows, `13320` each for `Inv`, `Fixed_OM_annual`, `Variable_OM`, and `53280` actual rows. `CORE6_VALUE_OVERLAP_VIOLATIONS=0`. The three economic variables span 1990–2019, but common time span does not establish downstream temporal ordering or a TGCV `Delta V` endpoint. They remain downstream/economic variables and are prohibited from entering `P_tau` merely because of correlation or economic relevance. MT4-8 is BOUNDED PASS.

### MT4 claim propagation

- **C01:** Material bounded methodological evidence for state/condition reconstruction in a heterogeneous non-software domain. No upgrade.
- **C02:** Material bounded qualification. MT4 supports candidate accessibility operationalization but does not establish a complete independent `P_tau` or general `T_acc`. No upgrade.
- **C07:** Material methodological support for temporal transformation-space analysis, bounded by unresolved full `P_tau`. No upgrade.
- **C08:** No positive trajectory-causal evidence; downstream trajectory separation is preserved but not causally tested. No upgrade.
- **C09:** No positive causal contribution. MT4 does not test accessibility change causing subsequent trajectories. No upgrade.
- **C10:** No value causal contribution. No independently downstream `Delta V` endpoint is established. No upgrade.
- **C11:** Material cross-domain methodological evidence. The methodology transfers to national electricity-system transitions, but this remains bounded domain transfer, not transversal validation. No upgrade.
- **C16:** Material methodological evidence supporting preservation of state → candidate transformation → accessibility → realization → trajectory → outcome/value distinctions in a heterogeneous domain. No upgrade.

No propagation is made to C03, C04, C05, C06, C12, C13, C14 or C15. No TGCV Core/RMA modification is authorized by MT4.

### MT4 closure and routing

MT4 is closed as a **BOUNDED PASS — METHODOLOGICAL TRANSFER DEMONSTRATED WITH EXPLICIT LIMITS**. The unresolved analytical bottlenecks are (1) independent formalization of full `P_tau` where feasible and (2) a genuinely downstream independently defined outcome/value endpoint capable of testing the accessibility-to-value layer. Completed MT4 gates must not be repeated merely to seek a stronger status.

'@
$out=$current
$out=$out -replace 'Evidence-to-Claim Matrix — Current v1\.11','Evidence-to-Claim Matrix — Current v1.12'
$out=$out -replace '\*\*Predecessor:\*\* v1\.10','**Predecessor:** v1.11'
$out=$out -replace '(\*\*Incremental governance update:\*\*).*',"**Incremental governance update:** v1.12 preserves the complete material evidentiary content and schema of v1.11 and adds the complete MT4 domain-transfer evidence layer. No prior evidence is deleted, collapsed, or downgraded. No claim-level status is upgraded by MT4 propagation."
if($out -match '## Material empirical/methodological evidence — MT4 Domain Transfer'){ throw 'MT4_ALREADY_PRESENT_IN_CURRENT' }
$marker='## Claim boundary'
$pos=$out.IndexOf($marker)
if($pos -lt 0){ throw 'CLAIM_BOUNDARY_MARKER_NOT_FOUND' }
$out=$out.Substring(0,$pos)+$mt4+$out.Substring($pos)
$out=$out -replace 'The v1\.10 update preserves the full evidence/claim structure of v1\.9','The v1.12 update preserves the full evidence/claim structure of v1.11 and adds the complete MT4 domain-transfer evidence layer'
$out=$out -replace 'v1\.11 adds C10C-004 bounded methodological evidence propagation\. None','v1.11 adds C10C-004 bounded methodological evidence propagation, and v1.12 adds MT4 bounded domain-transfer evidence propagation. None'
$out=$out -replace 'The scientific Core remains unchanged\.$','The scientific Core remains unchanged. MT4 does not alter claim status, RMA or Core ontology.'
$path=Join-Path $root '00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md'
[IO.File]::WriteAllText($path,$out,(New-Object Text.UTF8Encoding($false)))
$check=Get-Content $path -Raw
foreach($needle in @('Current v1.12','MT4-1','MT4-8','92.58%','MT4-6 — independent reproducibility','MT4-7 — downstream separation','MT4-8 — value isolation','CORE6_VALUE_OVERLAP_VIOLATIONS=0','No TGCV Core/RMA modification is authorized by MT4')){ if($check.IndexOf($needle) -lt 0){ throw ('MATRIX_VALIDATION_MISSING: '+$needle) } }
git add -- 00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md
git commit -m 'Reconcile cumulative evidence matrix CURRENT to v1.12'
git push origin main
Write-Host 'MATRIX_CURRENT_V1_12_RECONCILED_AND_PUSHED'
git rev-parse HEAD
