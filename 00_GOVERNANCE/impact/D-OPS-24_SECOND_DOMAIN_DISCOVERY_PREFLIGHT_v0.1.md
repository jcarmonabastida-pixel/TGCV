# D-OPS-24 — Second Independent Domain Discovery Preflight v0.1

**Date:** 2026-09-09
**Status:** CLOSED / PREFLIGHT PASS — EXECUTION NOT AUTHORIZED
**Design:** `D-OPS-24_SECOND_DOMAIN_DISCOVERY_DESIGN_v0.1.md`
**Parent decision:** `EXT-UPD-4.6_SECOND_DOMAIN_ROUTE_DECISION_v0.1.md`

## Preflight checks

| ID | Control | Result |
|---|---|---|
| PF-01 | Current TGCV scientific state consulted | PASS |
| PF-02 | EXT-UPD-4.5/D1 closure consulted | PASS |
| PF-03 | C-01 A/B/C protected | PASS |
| PF-04 | Core/TR-130/TR-131 protected | PASS |
| PF-05 | Second-domain independence explicitly required | PASS |
| PF-06 | Rust excluded from independent-domain pool | PASS |
| PF-07 | C-01 aircraft/control domain excluded | PASS |
| PF-08 | Prior TGCV instantiations/historical records must be checked | PASS |
| PF-09 | Native-first discovery preserved | PASS |
| PF-10 | Outcome-blind candidate selection preserved | PASS |
| PF-11 | MTE-1..MTE-10 unchanged | PASS |
| PF-12 | Reach/Trajectory/Outcome/Value not required for discovery | PASS |
| PF-13 | Search and screening separated | PASS |
| PF-14 | No dataset acquisition during discovery | PASS |
| PF-15 | Cumulative 12-QF budget defined | PASS |
| PF-16 | Cumulative 30-record budget defined | PASS |
| PF-17 | Maximum 3 QFs per candidate family defined | PASS |
| PF-18 | No budget reset by engine/session/operator | PASS |
| PF-19 | Exact QFs reserved for execution authorization | PASS |
| PF-20 | Candidate record schema required | PASS |
| PF-21 | Stop/deviation rule defined | PASS |
| PF-22 | Eligible/rejected/indeterminate classes defined | PASS |
| PF-23 | Multiple-candidate selection remains outcome-blind | PASS |
| PF-24 | Material evidence requires Evidence→Claim impact | PASS |
| PF-25 | No external asset update during execution | PASS |
| PF-26 | No empirical/causal/predictive/value escalation | PASS |
| PF-27 | Execution requires separate explicit authorization | PASS |
| PF-28 | No second-domain scientific execution hidden in preflight | PASS |

## Frozen controls

1. Independence is evidential, not nominal.
2. Historical scientific/external-science records must be consulted before candidate acceptance.
3. Discovery is documentary and outcome-blind.
4. The v0.5 MTE boundary is unchanged.
5. No dataset is acquired or processed during discovery.
6. Search budget is cumulative and cannot reset.
7. Exact query families are fixed only in the execution authorization.
8. Any material query change consumes a new QF.
9. A candidate cannot be promoted because it appears likely to confirm TGCV.
10. Every material evidence-bearing closure receives explicit Evidence→Claim impact assessment.

## Conclusion

**PREFLIGHT PASS at control level.**

The instrument is ready for a separate execution-authorization record. **Search execution remains NOT AUTHORIZED.**

The next controlled operation is to issue the explicit execution authorization containing the exact query families and search budget, then execute only those frozen queries.
