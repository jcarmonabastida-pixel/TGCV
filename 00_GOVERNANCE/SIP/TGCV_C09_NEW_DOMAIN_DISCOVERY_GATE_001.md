# TGCV — C09 New-Domain Discovery Gate 001

**Status:** `COMPLETED — NEW SEARCH CRITERION ADOPTED / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Purpose:** change C09 candidate discovery after closure of the retrospective lottery pool

## 1. Decision context

The retrospective candidate pool is closed for current public-package execution. Repeatedly screening additional lottery studies with the same data-provenance structure is not informative enough to justify another cycle.

The search criterion is therefore changed from **"strong randomized accessibility intervention"** to **"strong randomized accessibility intervention + directly reconstructible bounded accessibility state from admissible operational data"**.

## 2. Mandatory discovery criteria

A candidate is only eligible for detailed screening if, before any execution authorization, there is credible evidence of:

1. randomized or otherwise credible causal intervention;
2. an intervention that changes accessibility to a bounded class of transformations;
3. an operationally definable `U*` fixed before outcome inspection;
4. reconstructible `T_acc,0` and `T_acc,1` at the unit or treatment-cluster level from admissible data;
5. an independently defined downstream trajectory endpoint;
6. public or already-governed data access, without assuming restricted-data approval;
7. no need to substitute treatment assignment, take-up, realized behavior, or published effects for `T_acc`;
8. a plausible TR-132 omitted-path sufficiency argument.

## 3. Initial discovery results

### A. Santiago fare-free public transport RCT — HIGH INTEREST / DATA PROVENANCE AUDIT REQUIRED

The study randomly assigned 106 workers to a two-week unlimited fare-free transit pass and 101 controls. The intervention directly changes the price/admissibility of transit-use transformations, and detailed travel diaries provide individual-level trip outcomes. Accessibility heterogeneity was explicitly examined using proximity to the subway network. citeturn3search0turn3search4

This is materially closer to the new criterion than the previously screened housing/benefit lottery cases because the bounded transformation class and intervention rule are operationally concrete. However, current public evidence does **not** establish that the participant-level diaries and assignment data are openly reproducible. Therefore it is not yet admitted; it requires a focused data-provenance audit.

### B. King County free-transit RCT — NOT A NEW CANDIDATE

The 2025 study has a replication package, but OpenICPSR explicitly states that some data are not included because of legal limitations. This reproduces the already documented provenance blocker and therefore is not reopened. citeturn1search2

### C. trips4health — NOT ADMITTED FOR DISCOVERY

The trial used smartcard administrative data and survey/clinic data, but the published availability statement says the datasets are available from the corresponding author on request with approvals. It therefore fails the new public-admissibility criterion at discovery stage. citeturn0search0turn0search1

### D. Julkine — NOT YET ELIGIBLE

The trial uses open-data measures of public-transport accessibility to match schools before randomization, but the intervention is a multi-component behavioural programme rather than a clean accessibility intervention. It therefore does not presently satisfy the causal accessibility criterion. citeturn2search0

## 4. Decision

**NEW-DOMAIN DISCOVERY GATE = ADOPTED.**

The next detailed operation is not another retrospective lottery audit. It is a **Santiago fare-free RCT data-provenance audit**, with one question only: can the randomized assignment, bounded transit transformation universe, pre-treatment accessibility state, post-intervention accessibility state and independent trajectory endpoint be reconstructed from an admissible public package?

No execution authorization is created by this gate.
No C09 result is created.
No matrix upgrade.
No Core change.
