# D-OPS-9 — Railway Rule-Layer / Longitudinal-State Compatibility Audit v0.1

**Status:** CLOSED — RAILWAY DOMAIN NOT EXECUTION-READY
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Audit target

Rule layer: **EULYNX / EU-Rail System Pillar signalling and interlocking specifications**.
State resource candidates: **ADIF Railway Transport Network / Spanish INSPIRE rail-network data**, supplemented by RINF/transport-network resources.

EULYNX publishes versioned Baseline Sets. Baseline Set 4 Release 4 (2025) is described as a stable specification set closed to functional changes/new features; requirements specifications have ReqIF artefacts, model-based deliverables have model exports, and field-element specifications have simulators for verification/validation. citeturn0search1turn0search4

The EULYNX model contains explicit interlocking concepts and safety constraints: routes are set and locked by interlocking according to functional rules, flank protection and track sections are part of route safety, and approach locking/release procedures are explicitly modelled. citeturn1search4turn1search8turn1search9

ADIF provides a public railway-network spatial dataset under INSPIRE. The catalogue exposes versions including April 2018 and July 2024, establishing at least two public snapshots of the infrastructure representation. citeturn1search0turn1search3

## 2. Compatibility matrix

| Criterion | Result | Finding |
|---|---|---|
| D9-1 Exact S | PASS/CONDITIONAL | Infrastructure/signalling configuration can be represented as structured railway objects and relations. |
| D9-2 Temporal boundary | CONDITIONAL | Public ADIF resources expose dated/versioned snapshots (2018, 2024), but this is not yet a validated continuous or semantically stable longitudinal series. |
| D9-3 Rule release | PASS | EULYNX Baseline Sets provide explicit release/version boundaries. citeturn0search0turn0search1 |
| D9-4 Independent Uτ | CONDITIONAL | Route-setting/interlocking transformations are conceptually enumerable, but a complete finite transformation universe requires fixing the engineering scope and object model. |
| D9-5 Canonical τ | CONDITIONAL | EULYNX provides typed railway objects and route properties, but a TGCV canonical transformation identity still has to be frozen. |
| D9-6 Non-trivial Pτ | PASS/CONDITIONAL | EULYNX contains explicit safety/locking rules that can define admissibility without using observed success. However, national implementation rules and the exact rule subset must be fixed. citeturn1search4turn1search9turn1search25 |
| D9-7 T_acc constructible | CONDITIONAL | Potentially yes for a bounded signalling subsystem, but only after a closed object/rule scope is selected. |
| D9-8 Longitudinal ΔT_acc | FAIL for current public pairing | ADIF 2018/2024 snapshots establish state versions, but the evidence does not establish that the same EULYNX semantics and object identity can be applied across both snapshots with complete historical rule compatibility. |
| D9-9 Reach separable | CONDITIONAL | A route-setting successor configuration can be structurally represented, but exact successor semantics need an independently frozen configuration model. |
| D9-10 Provenance/reproducibility | PASS/CONDITIONAL | EULYNX releases are versioned; ADIF data are public. Full reproducibility depends on access to the exact historical distributions and rule release. citeturn0search1turn1search3 |
| D9-11 Information gain beyond Rust | PASS | Railway signalling/interlocking is an external engineering domain with an independently governed rule layer. |
| D9-12 Firewall | PASS | Observed train movements, operational success, delays and outcomes can be excluded from Pτ. |
| D9-13 Falsifiability | PASS | A frozen railway rule/configuration model can produce direct falsifiers for T_acc/Reach distinction. |

## 3. Critical finding

The rule-layer side is substantially stronger than in the previous domains. EULYNX is not merely a collection of observed railway trajectories: it contains a versioned engineering model with explicit requirements and safety/interlocking semantics. This satisfies the strategic objective of D-OPS-8 much better than datasets where admissibility had to be inferred from observed behaviour. citeturn0search1turn1search25

However, the **longitudinal bridge remains insufficient**.

The existence of public ADIF snapshots from 2018 and 2024 is not enough to conclude that a single canonical railway state representation, with stable object identity and a compatible EULYNX rule layer, can be reconstructed at both times. The current evidence establishes versioned data resources, not yet a validated longitudinal population of comparable states.

## 4. Important semantic boundary

A tempting shortcut would be to define:

`τ = observed route used by a train`

and

`Pτ = route was actually set successfully`.

This is explicitly rejected. It would make accessibility depend on observed execution/outcome and would reproduce the circularity already excluded in previous D-OPS gates.

The admissibility predicate must instead be based on the frozen engineering/interlocking state and rules **before execution**.

## 5. Decision

**D-OPS-9 = CLOSED — RAILWAY RULE LAYER VALID, LONGITUDINAL EMPIRICAL BRIDGE NOT YET VALIDATED.**

Therefore:

- railway engineering remains a viable conceptual external domain;
- EULYNX is retained as a serious candidate rule layer;
- ADIF is retained as a candidate state resource;
- no dataset is selected;
- no operational specification is frozen;
- no implementation is authorized;
- no real data are downloaded or executed;
- TGCV scientific claim levels remain unchanged.

## 6. Next controlled operation

Open **D-OPS-10 — Railway State-Identity / Historical-Version Reconstruction Audit**.

The next audit should not broaden the search. It should determine whether the 2018 and 2024 ADIF railway representations can be reconstructed into a common canonical state space with stable object identity and whether the relevant EULYNX signalling/interlocking rule subset can be applied consistently to both states.

Required outputs:
1. exact historical dataset artefacts and hashes, if publicly recoverable;
2. common state schema;
3. object-identity continuity;
4. rule-version compatibility matrix;
5. candidate `Uτ` and `Pτ` scope;
6. explicit reasons for PASS/FAIL on longitudinal comparability;
7. no execution authorization.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
