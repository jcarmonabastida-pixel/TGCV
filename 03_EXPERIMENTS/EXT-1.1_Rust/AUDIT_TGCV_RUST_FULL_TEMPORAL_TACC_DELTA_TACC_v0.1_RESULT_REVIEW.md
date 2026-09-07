# TGCV — Rust Full Temporal T_acc / ΔT_acc Structural Audit v0.1 — Result Review

**Status:** CONDITIONAL PASS — FULL TEMPORAL T_acc / ΔT_acc RECONSTRUCTION COMPLETED; STRUCTURAL EVIDENCE ACCEPTED WITH FROZEN COVERAGE LIMITATION

## 1. Execution identity

The audit was executed against the frozen Rust dataset and the frozen outcome-blind structural protocol.

- ZIP: `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`
- R* version: `v0.2`
- T_acc representation: membership-level
- Temporal rule: origin timestamp → next release of same package
- Outcome computed: False
- Model fitted: False
- Value computed: False
- Execution used: False
- Future activity used: False
- Old EXT-1.1 resolver used: False
- Old EXT-1.1 outcome/window/model used: False
- R* modified: False
- Row-order invariant: True

## 2. Dataset integrity result

The execution reported:

- 91,437 packages
- 607,498 versions
- 3,618,523 dependency rows scanned
- 0 malformed rows
- 0 duplicate rows
- 0 temporal ordering violations
- 516,061 paired origins
- 91,437 terminal origins

These checks support deterministic structural processing of the supplied dataset under the frozen protocol.

## 3. Universe and accessibility result

The audit evaluated **178,490,042 candidate evaluations**.

`UNIVERSE_MEMBERSHIP_DRIVEN_BY_DECLARATION = False`

`CANDIDATE_IDENTITY_INCLUDES_DECLARATION = False`

`TARGET_RELEASE_CUTOFF_USED_AS_CHANGE_DRIVER = False`

The audit excluded **5,296,541 target-version evaluations** because the target version was unsupported by the frozen R* v0.2 version grammar. These are coverage exclusions, not classifications of inaccessibility.

The R* grammar remains frozen and no unsupported version was silently coerced.

## 4. Full T_acc reconstruction

The membership-level reconstruction produced:

- `TACC_T0_MEMBERSHIP_COUNT = 26,112,590`
- `TACC_T1_MEMBERSHIP_COUNT = 25,464,303`
- `EMPTY_TACC_T0_PAIRS = 86,153`
- `EMPTY_TACC_T1_PAIRS = 102,690`

The primary analytical object was therefore reconstructed as an explicit membership relation rather than only a cardinality statistic.

## 5. Full ΔT_acc result

The temporal membership difference produced:

- additions (`0→1` membership): **827,361**
- removals (`1→0` membership): **1,475,648**

Pair classifications:

- persistence: **312,377**
- expansion: **23,332**
- contraction: **144,381**
- reconfiguration/substitution: **35,971**
- changed pairs: **203,684**
- unchanged pairs: **312,377**

This is materially different from the first temporal construction, where removals were structurally impossible. The present construction therefore successfully avoids the earlier monotonicity artifact.

## 6. Scientific structural finding

The result supports the following bounded structural proposition:

> Under the frozen Rust R* v0.2 semantics, fixed transformation identities can aggregate into temporal accessible-transformation sets whose membership changes over successive states of the focal package-version, including expansion, contraction and reconfiguration, without using target-release appearance as the temporal change driver and without using execution, outcome, value or future activity.

The observation is structural and domain-bounded. It does not establish a universal TGCV law.

## 7. Important interpretation boundary

The result must not be interpreted as proof that:

- every Rust dependency relation is a TGCV transformation;
- R* v0.2 is a complete historical model of Rust dependency semantics;
- unsupported target versions were inaccessible;
- `ΔT_acc` universally causes changes in Reach or Trajectory;
- accessibility causes positive outcomes or value;
- TGCV has predictive superiority;
- TGCV is universally novel or ontologically irreducible.

## 8. Coverage limitation

The **5,296,541 unsupported target-version evaluations** are materially relevant to coverage. They remain explicitly excluded/unresolved under the current grammar.

This limitation does not invalidate the structural result for the resolved subset, but it prevents a claim of complete historical semantic coverage of all target version strings in the dataset.

Any expansion of R* requires a separate ex-ante grammar gate and a new rerun. No such expansion is authorized by this review.

## 9. Canonical integrity hashes

- T_acc,t0: `bab428f17458a0e53615435e9c791b14019336c12e69f08b77ff44bdbcf1d443`
- T_acc,t1: `a937d967c1fb4512b4f1c1924878363f7197557ad22e88de9e15ec564c01fd05`
- Add: `23412b30a34d5fd26768af8fa1699cb77101e20764f53cbae505845a2954232d`
- Rem: `ce4b95e86e7155845dac1ac12188bef26c2e128c47cbcc48601e2005137fad1e`
- Pairs: `d2f5ea668bd5dbf80329b5811a787d06e2adc88c826de962ebad8d333ae66a8d`
- Report: `ad4e8d20691b02e1fcaee334ee3fd93fe91b38b3e5e44e6440776804c816ac4d`

## 10. Decision

**CONDITIONAL PASS — FULL TEMPORAL T_acc / ΔT_acc STRUCTURAL RECONSTRUCTION ACCEPTED FOR THE RESOLVED ANALYTICAL SUBSET.**

The audit establishes the structural behavior required to continue the Rust instantiation: `T_acc` can be reconstructed at paired times and `ΔT_acc` can contain both additions and removals, producing persistence, expansion, contraction and reconfiguration classes.

The result is stronger than the preceding shadow audit because the complete paired T_acc membership relations and their differences have now been reconstructed.

## 11. What is authorized next

A separate gate may now specify the next downstream structural test, provided it remains outcome-blind until explicitly authorized.

The natural next operation is:

**TGCV Rust ΔT_acc → ΔReach / ΔTrajectory Structural Link Gate v0.1**

That gate must determine how reachable futures and trajectory structure can be reconstructed without conflating them with T_acc, and must not introduce outcome/value/predictive variables prematurely.

## 12. Integrity lock

- Core remains `S`.
- T_acc remains a derived analytical object.
- ΔT_acc remains the primary differentiated candidate.
- I remains explanatory.
- SLR-1 remains closed.
- TR-130–TR-140 remain closed.
- EXT-1.1 predictive result remains excluded.
- R* v0.2 remains frozen.
- No post-hoc grammar change.
- No outcome/model/value execution authorized by this review alone.
