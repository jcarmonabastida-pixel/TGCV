# TGCV — MT-4 Candidate Domain Selection — 001

**Status:** CANDIDATE SELECTED — EVIDENCE FREEZE PENDING — EXECUTION NOT STARTED  
**Date:** 2026-09-16  
**Purpose:** Select a genuinely new heterogeneous domain for the prospective MT-4 domain-transfer test and define the evidence package that must be frozen before any TGCV translation is attempted.

## 1. Selected candidate

**Domain:** historical national electricity-system transitions / energy-system technology change.

**Primary source candidate:** Jaxa-Rozen, Wen & Trutnevyte, *Historic data of the national electricity system transitions in Europe in 1990–2019 for retrospective evaluation of models*, Zenodo record 6696776, version v2.

The dataset covers 31 European countries over 1990–2019 and provides harmonized country, technology, resource/fuel-price/CO2 and load-profile data. The published description states that the package contains 1,359 processed and harmonized data files and is intended for retrospective electricity-system modelling and empirical analysis. The public dataset is 10.6 MB in the v2 presentation. Source identification must be frozen by DOI/version and, where technically feasible, by downloaded-file SHA-256 before scientific execution.

## 2. Why this domain qualifies as a prospective transfer candidate

This domain is materially different from the software/self-adaptive, industrial IT, infrastructure/accessibility, household empowerment and microcredit cases used to construct the candidate methodology.

It is useful for MT-4 because the empirical material potentially contains:

- a system state represented by technology stocks, demand, economic and resource conditions;
- a candidate universe of technology/system transformations;
- constraints that may determine which transformations are technically/economically admissible;
- realized technology changes observable over time;
- subsequent system trajectories;
- downstream outcome measures such as energy demand, technology mix, emissions and economic variables.

The domain therefore provides a genuine test of whether the methodological sequence can be translated without simply renaming adoption or observed structural change as accessibility.

## 3. Critical methodological risk

The dataset does **not** by itself establish TGCV accessibility.

In particular, installed capacity, technology adoption, technology shares or observed system changes must not automatically be interpreted as `T_acc` or `ΔT_acc`.

The MT-4 execution must first determine whether a defensible candidate universe `Uτ` and independently specified admissibility predicate `Pτ(S,C,L)` can be constructed from pre-outcome information. If that cannot be done, the correct result is a bounded methodological boundary or transfer failure, not semantic substitution.

This makes the domain informative for MT-4 rather than merely convenient.

## 4. Proposed evidence-freeze package

Before any TGCV mapping, freeze at minimum:

1. the exact source record and version;
2. downloaded source archive/file(s), with SHA-256 where feasible;
3. source metadata and data dictionary/documentation;
4. country and technology dimensions included;
5. temporal coverage 1990–2019;
6. all variables proposed as potential state/context candidates;
7. all variables proposed as potential transformation/realization candidates;
8. all variables proposed as potential downstream outcome/value candidates;
9. source provenance and any transformations already performed by the dataset creators;
10. the temporal information boundary to be respected by MT4-5.

No variable is assigned a TGCV role during the freeze itself. The freeze is an empirical inventory, not a conceptual interpretation.

## 5. Preliminary MT-4 eligibility assessment

| Gate | Current status | Reason |
|---|---|---|
| MT4-1 Domain novelty | PROVISIONAL PASS | New domain relative to methodology-construction cases; final novelty check before execution. |
| MT4-2 Frozen evidence | NOT YET CLOSED | Exact source package must be downloaded and hashed. |
| MT4-3 Independent semantic mapping | NOT STARTED | Must occur only after freeze. |
| MT4-4 Semantic non-substitution | NOT STARTED | Central test; technology adoption/realization must not be renamed accessibility. |
| MT4-5 Temporal non-leakage | NOT STARTED | Must define pre/post information sets before mapping. |
| MT4-6 Independent reproducibility | NOT STARTED | Executor-2 comes after Executor-1 package is frozen. |
| MT4-7 Downstream separation | POTENTIALLY TESTABLE | Longitudinal 1990–2019 structure provides temporal material; exact executable variables to be established after freeze. |
| MT4-8 Value isolation | POTENTIALLY TESTABLE / OPEN | Economic variables exist, but a valid TGCV Value construct must not be assumed. |

## 6. Evidence status

**No MT-4 scientific execution has occurred.**

The candidate selection is based on public source metadata only. The evidence package is not yet declared frozen because the exact downloaded archive and its cryptographic hash have not yet been established in the TGCV execution environment.

Accordingly, no `S_t`, `Uτ`, `Pτ`, `T_acc`, `ΔT_acc`, trajectory or Value variable is being declared from this source at this stage.

## 7. Next authorized operation

The next operation is purely evidentiary:

**Acquire the exact public source package, verify provenance/version, compute SHA-256, preserve the immutable source package, and register the resulting freeze manifest.**

Only after that operation is closed may MT4-3 begin.

## 8. Governance non-upgrade

This candidate selection does not modify TGCV Core, RMA v3.35, Evidence-to-Claim Matrix v1.11, C09/C10/C11/C12/C16 status, or the open `ΔT_acc → Value` layer.
