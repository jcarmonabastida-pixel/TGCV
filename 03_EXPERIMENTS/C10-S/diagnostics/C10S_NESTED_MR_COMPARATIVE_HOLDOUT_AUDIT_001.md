# C10-S — Tier A C0/C1/C5 comparative holdout: execution audit and adjudication

**Record:** C10S-NESTED-MR-COMPARATIVE-HOLDOUT-AUDIT-001  
**Date:** 2026-11-19  
**Status:** EXECUTION INTEGRITY PASS / SCIENTIFIC HOLDOUT NOT VALIDATED  
**Work branch:** `research/c10s-f1-integrated-correction-20261119`  
**Authorized execution branch:** `research/c10s-nested-mr-comparative-auth-C10S-HOLDOUT-20261119-001`  
**Protocol:** `C10S-NESTED-MR-COMPARATIVE-HOLDOUT-PROTOCOL-001`, v1.0  
**Workflow run:** [44572812481](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44572812481)  
**Artifact:** `c10s-tier-a-holdout.zip`, artifact ID `14555769269`

## 1. Executive adjudication

The authorization-gated Tier A execution and clean-source replay completed. The computational/provenance checks performed for this audit pass, but the prespecified statistical acceptance rule is not met.

- 8 cells × K=1,000 = **8,000 primary datasets**.
- Replay contains the same 8,000 datasets and matches the primary cell files and checkpoint index exactly.
- 32 confirmatory method × cell × component combinations were assessed (within and untruncated raw-between).
- **10/32 combinations pass all three numeric criteria** (conditional coverage in [0.93,0.97], two-sided 95% Wilson interval contains 0.95, and interval emission ≥0.95). All 32 also satisfy the dataset-accounting, roster, finite-interval and raw-between-preservation checks.
- The protocol's no-pooling rule applies: no family/method is validated unless every required component cell passes.

**Disposition:** C1/F1 within is validated across its six declared cells only as a component-specific bounded result. C0/F1, C0/F5 and C5/F5 are not validated as complete method/family procedures. C1/F1 raw-between is not validated. Therefore the Tier A comparative holdout as a whole is **NOT_VALIDATED**.

This is not a C10 causal result and does not authorize Tier B or C10 Generator/Analyzer/Evaluator execution.

## 2. Execution identity and artifact integrity

| Item | Audited value |
|---|---|
| GitHub Actions run | `44572812481` — completed successfully |
| Authorization ID | `C10S-HOLDOUT-20261119-001` |
| Authorization SHA-256 | `45d15c681fb067fca55893ac487c63b1cce6353c5d85ee21b2976c311fb47ba2` |
| Approved code commit | `4ea44f82ed0947c64c67303ecd3acbbd5f0b00e3` |
| Protocol SHA-256 | `fe1534ae8f98d1745bafce98a1610763524aa434c1aa58340a1c756a92d0724b` |
| Result JSON SHA-256 | `0660cfb7607f893000393a80f598507aef44db310cc19713427dd0f56086f12e` |
| Primary/replay digest in result | `2c24547199885f1e70a8169cba81bb02cb58af36c6cf085ebfd2ce2cb3c566d6` |
| Downloaded ZIP SHA-256 | `72176a267d0a1e4d32e682d22b31f5e34bad3810666aeb7579adf37943799681` |
| Artifact ID | `14555769269` |

Independent checks against the downloaded ZIP:

1. The result JSON digest matches `final/run_manifest.json`.
2. Each of the eight primary cell files matches its declared `records_sha256`.
3. Every primary cell file is byte-identical to its replay counterpart; both checkpoint indexes are byte-identical.
4. The sum of cell record counts is exactly 8,000; each cell has 1,000 records and no duplicate dataset IDs.
5. Each record's dataset ID agrees with its comparison and independent truth record; expected two-method roster is present for every dataset.
6. All emitted within/raw-between interval endpoints are finite. No non-finite interval was silently accepted.
7. The raw-between target was not truncated: the raw records retain negative point estimates (959 observed) and negative lower interval endpoints (4,015 observed).

These checks support **execution integrity and exact replay**, not scientific validity of the interval procedures.

## 3. Independent recomputation method

Coverage and interval emission were recomputed from each per-dataset record in the downloaded primary cell JSON files, using the independent truth field and the method-specific interval endpoints. For each method × cell × component:

- numerator = number of emitted intervals containing the record's independent truth;
- conditional-coverage denominator = number of emitted intervals;
- emission denominator = K=1,000;
- two-sided 95% Wilson interval recomputed from the binomial count;
- pass requires all three frozen numerical criteria and all structural/integrity conditions in Protocol §5.

For F5/C5 at M10/R5, 16/1,000 intervals are typed abstentions; conditional coverage uses 984 emitted intervals and emission is 98.4%. Abstentions are not silently counted as covered. The unconditional cover rate remains a separate operational metric and does not replace conditional coverage.

## 4. Full confirmatory results

Each cell below reports the two confirmatory components. Format: **coverage (95% Wilson interval); emission; disposition**. Percentages are rounded to two decimals; the exact binomial counts and intervals are in the immutable source records.

| Cell | Method | Within | Raw between |
|---|---|---|---|
| F1 balanced M10/R5 | C0 | 83.10% [80.65,85.30]; 100%; FAIL | 92.40% [90.59,93.89]; 100%; FAIL |
| F1 balanced M10/R5 | C1 | 94.90% [93.36,96.10]; 100%; PASS | 98.80% [97.91,99.31]; 100%; FAIL |
| F1 balanced M30/R20 | C0 | 95.40% [93.92,96.53]; 100%; PASS | 93.00% [91.25,94.42]; 100%; FAIL |
| F1 balanced M30/R20 | C1 | 95.10% [93.58,96.27]; 100%; PASS | 97.30% [96.10,98.14]; 100%; FAIL |
| F1 high-between M10/R5 | C0 | 85.50% [83.18,87.55]; 100%; FAIL | 80.30% [77.72,82.65]; 100%; FAIL |
| F1 high-between M10/R5 | C1 | 95.40% [93.92,96.53]; 100%; PASS | 97.70% [96.57,98.46]; 100%; FAIL |
| F1 high-between M30/R20 | C0 | 95.00% [93.47,96.19]; 100%; PASS | 88.90% [86.80,90.70]; 100%; FAIL |
| F1 high-between M30/R20 | C1 | 95.10% [93.58,96.27]; 100%; PASS | 96.70% [95.40,97.64]; 100%; FAIL |
| F1 low-between M10/R5 | C0 | 84.70% [82.34,86.80]; 100%; FAIL | 97.20% [95.98,98.06]; 100%; FAIL |
| F1 low-between M10/R5 | C1 | 95.50% [94.03,96.62]; 100%; PASS | 99.40% [98.70,99.72]; 100%; FAIL |
| F1 low-between M30/R20 | C0 | 95.00% [93.47,96.19]; 100%; PASS | 89.00% [86.91,90.79]; 100%; FAIL |
| F1 low-between M30/R20 | C1 | 95.00% [93.47,96.19]; 100%; PASS | 99.00% [98.17,99.46]; 100%; FAIL |
| F5 beta22 M10/R5 | C0 | 94.00% [92.35,95.31]; 100%; PASS | 99.10% [98.30,99.53]; 100%; FAIL |
| F5 beta22 M10/R5 | C5 | 98.37% [97.38,99.00]; 98.40%; FAIL | 98.88% [98.01,99.37]; 98.40%; FAIL |
| F5 beta22 M30/R20 | C0 | 93.50% [91.80,94.87]; 100%; FAIL | 96.40% [95.06,97.39]; 100%; FAIL |
| F5 beta22 M30/R20 | C5 | 93.50% [91.80,94.87]; 100%; FAIL | 92.70% [90.92,94.15]; 100%; FAIL |

### 4.1 Aggregate disposition by method

| Method/family | Within cells passing | Raw-between cells passing | Complete disposition |
|---|---:|---:|---|
| C0 / F1 | 3/6 | 0/6 | NOT_VALIDATED |
| C1 / F1 | 6/6 | 0/6 | NOT_VALIDATED |
| C0 / F5 | 1/2 | 0/2 | NOT_VALIDATED |
| C5 / F5 | 0/2 | 0/2 | NOT_VALIDATED |

The 10 passing combinations are six C1/F1 within cells, three C0/F1 within cells, and one C0/F5 within cell. No raw-between combination passes.

## 5. Interpretation bounded to this holdout

### 5.1 F1/C1

C1's exact pivotal within interval meets all criteria in all six F1 cells. This is a bounded component result for the declared Gaussian random-intercept fixtures and the two M/R designs per parameter regime.

C1's conservative raw-between interval does not pass in any of the six cells. Its empirical coverage is 96.7–99.4%, and its Wilson intervals lie above 95% in those cells. The conservative interval therefore overcovers relative to the frozen acceptance rule. The corresponding mean interval widths are also materially larger than C0 in several cells (e.g. balanced M10/R5: 4.532 versus 1.968; high-between M10/R5: 7.293 versus 2.779). This is not an emission failure: C1 emits 100% of intervals.

### 5.2 F5/C5

At M10/R5, C5 overcovers both targets (98.37% within; 98.88% raw-between) and has 16 typed abstentions (15 optimizer non-convergences and one upper-bound concentration fit). Its emission rate is 98.4%, above the frozen minimum, but the coverage criteria fail.

At M30/R20, C5 undercovers both targets (93.5% within; 92.7% raw-between). The Wilson intervals do not contain 95%. Thus the direction of the calibration error changes across the two declared M/R designs; neither cell passes.

### 5.3 Baseline C0

C0 also fails the full-family rule. F1 within passes only in the three M30/R20 cells; F1 raw-between fails all six cells. In F5, only within at M10/R5 passes; raw-between fails both designs. C0 is retained as the frozen comparator, not selected as a validated method.

## 6. Manifest discrepancy — evidence traceability reservation

The artifact's `final/run_manifest.json` reports:

```
COMPUTED_NOT_AUTHORIZED_NOT_EXECUTED_AS_HOLDOUT
```

The primary comparative result reports:

```
EXECUTED_UNDER_APPROVED_AUTHORIZATION
```

The result JSON digest matches the manifest, so this is not file corruption. It is a semantic status mismatch in the manifest writer. The manifest also contains only a minimal field set and does not itself carry the full source/hash inventory required by Protocol §7; some of that inventory is present in the result object and the externally downloadable per-cell bundle.

The mismatch is preserved as observed. No raw output or original artifact was edited to repair it. This audit record is a downstream annotation, not a replacement manifest and not a retroactive modification of the execution.

**Traceability disposition:** CONDITIONAL / DOCUMENTED DEFECT. The independent ZIP, result, per-cell hashes, authorization and replay checks above provide strong evidence of what ran and what it produced, but the original manifest is not semantically self-consistent and is not a fully self-contained protocol-compliant manifest.

## 7. Overall gate and next operation

**Tier A comparative holdout: NOT_VALIDATED.**

- Computational execution and replay integrity: PASS within the checks listed in §2.
- Confirmatory statistical acceptance: FAIL at family/method level under the frozen no-pooling rule.
- Manifest traceability: CONDITIONAL due to the status/inventory defect in §6.
- No winner is selected from this holdout.
- No Tier B or C10 causal scientific execution is authorized.

Next operation is a **separate instrumental correction/design review**, not a rerun of this holdout. Preserve this run and replay as immutable evidence. Diagnose C1 raw-between conservatism and C5's M/R-dependent calibration/convergence behaviour in a development namespace, without changing the frozen v1.0 protocol or reusing its holdout outcomes for tuning. Any subsequent confirmatory validation must use a new protocol version, fresh independent datasets, new seeds, and a new one-use authorization.

The bounded C1 within result may be retained as component-specific evidence; it does not validate the full variance-component inference pipeline and does not answer the causal C10 question ΔT_acc → Value.

## 8. Non-claims

This audit does not establish:
- that nested M/R assumptions hold in real systems;
- general variance-component estimator validity outside the declared fixtures;
- any causal contribution of accessibility or ΔT_acc to trajectory, outcome or Value;
- any TGCV Core change, universal claim, predictive claim or value-creation claim;
- scientific execution or calibration of the C10 Generator/Analyzer/Evaluator.

**Source artifacts:** the frozen protocol and authorization on the dedicated authorization branch; GitHub Actions run 44572812481; downloaded artifact 14555769269. The downloaded ZIP is preserved unchanged with SHA-256 recorded in §2.
