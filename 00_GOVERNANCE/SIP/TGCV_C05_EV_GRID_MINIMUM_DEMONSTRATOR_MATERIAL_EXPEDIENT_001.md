# TGCV — C05 EV–Grid Minimum Demonstrator — Material Expediente 001

**Case:** `C05_EV_GRID_SYNTHETIC_MINIMUM_DEMONSTRATOR_V001`  
**Status:** `EXECUTION COMPLETE — PASS WITH METHODOLOGICAL LIMITATIONS`  
**Evidence class:** bounded synthetic application-fit / methodological evidence; not empirical causal evidence.  
**Runner:** `03_EXPERIMENTS/TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_MINIMUM_DEMONSTRATOR_V001.py`  
**Runner commit:** `e8e55f50f82b9bdf69eeca4d48deb9d23799672e`  
**SPEC_COMMIT:** `5aa2c7e20ea3f5775b2d6e60797f9be9efe10e05`  
**FIXTURE_COMMIT:** `9dd6e9b6bb8d0b7a7e686c4dc61926fc627fa8b6`  
**Execution:** `C05_EXECUTION_COMPLETE`  
**Python:** `3.8.10`  
**Platform:** `Windows-10-10.0.26200-SP0`  
**Output SHA-256:** `27025e638c05458e19a125c00d9d86d89906bc418eec5670eddec14c89e96880`  
**Preflight:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_RUNNER_PREFLIGHT_001.md`  
**Post-execution audit:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_POST_EXECUTION_AUDIT_001.md`

## 1. Purpose, research role and frozen scope

C05 is the executed EV–Grid Minimum Demonstrator for TGCV application-fit. Its purpose is to instantiate the TGCV translation chain in a compact synthetic domain while preserving the distinction among system/context state, candidate transformations, admissibility, accessible transformation space (`T_acc`), transition, post-transition state/context and bounded subsequent trajectory.

Its evidentiary role is methodological and application-fit oriented. It is not a real-world EV-grid study, causal identification experiment, value/ROI test, explanatory- or predictive-superiority comparison, generality test, industrial validation, or deployment-readiness assessment. No claim-level validation is inferred from execution completion. The synthetic nature of the domain, transformation universe, admissibility predicates, transitions and trajectory generation is part of the evidence boundary.

## 2. Frozen transformation universe and operational contract

The frozen candidate transformation universe `U_tau` contains exactly:

`accept_A`, `accept_B`, `defer`, `reduce_power`, `shift_window`, `redirect_A_to_B`, `redirect_B_to_A`, `reserve_capacity`, `release_capacity`, `v1g_discharge`, `v2g_discharge`, `reject`.

For each frozen scenario, candidate transformations are evaluated through an explicit admissibility rule and `T_acc` is the admissible subset of `U_tau`. The execution contract records initial state/context, candidate transformation universe, admissibility/accessibility results, transition identifier, post-transition state/context, `T_acc_1`, `Delta T_acc`, bounded trajectory fields, baseline fields, controls and explicit non-claims.

The analytical separation tested by the demonstrator is therefore:

`state/context → admissibility → T_acc → transition → post-transition state/context → bounded trajectory fields`.

The experiment does not treat downstream outcome or value as a substitute for accessibility.

## 3. Provenance and execution integrity

The frozen runner executed to `C05_EXECUTION_COMPLETE` under Python `3.8.10` on `Windows-10-10.0.26200-SP0`. Runner, specification and fixture provenance are pinned by the commits above. The execution output is identified by SHA-256 `27025e638c05458e19a125c00d9d86d89906bc418eec5670eddec14c89e96880`.

The preflight and post-execution audit record execution-integrity PASS, runtime-contract PASS, transition-coverage PASS, negative-control PASS and observed-accessibility-delta PASS. These are execution/audit classifications within the frozen demonstrator and do not constitute broader scientific validity.

## 4. Scenario coverage and quantitative findings

The frozen execution contains scenarios `T1`–`T6` plus negative controls `NC1` and `NC2`. The material positive result is concentrated in T3.

Under **T3**:

- `|T_acc,0| = 8`;
- `|T_acc,1| = 6`;
- `Delta |T_acc| = -2`;
- closed transformations: `accept_B` and `redirect_A_to_B`.

Under **T1, T2, T4, T5 and T6**, the frozen execution reports no accessibility delta. The same absence of an accessibility delta is reported for **NC1 and NC2**.

Thus the demonstrator does not classify every represented state/context change as an accessibility-space change. The observed delta depends on the frozen admissibility structure.

## 5. Interpretation of the result

The T3 result concerns the identity and cardinality of the accessible candidate-transformation space, not downstream operational outcomes. Closing `accept_B` and `redirect_A_to_B` is evidence of a bounded synthetic `T_acc` change. It is not evidence that an EV-grid intervention caused a real-world reliability, mobility, energy, economic or value outcome.

The principal methodological contribution is the executable preservation of distinctions among `U_tau`, admissibility, `T_acc`, transition, post-transition state/context and bounded trajectory fields.

## 6. Baseline reconstruction limitation

The frozen implementation defines `baseline(s,c,l)` by returning `admissible(s,c,l)`. Consequently `baseline_equivalent=true` is an implementation identity, not an independently constructed baseline model.

It cannot be counted as independent baseline evidence and cannot support independent validation, explanatory superiority, predictive superiority or comparative advantage. The baseline comparison establishes consistency with the same admissibility implementation rather than an independent comparator.

## 7. Negative controls and trajectory-policy limitation

`NC1` and `NC2` show no accessibility delta in the frozen execution. `NC2` specifies `selection_tiebreak=reverse_lexical`, but the frozen `trajectory()` implementation does **not consume that field**.

Consequently NC2 is **not** a valid trajectory-policy sensitivity test. It is only a negative-control execution under the frozen implementation. C05 therefore does not establish trajectory-policy robustness, sensitivity of trajectory conclusions to selection policy, a causal `Delta T_acc -> trajectory` estimand, or any downstream causal trajectory effect.

## 8. Evidence-to-claim propagation

**C02 — bounded qualification.** C05 supplies synthetic application-fit evidence that explicit candidate transformations, admissibility/accessibility and `T_acc` can be represented and executed, including the T3 reduction from 8 to 6. It does not establish general empirical accessibility or an independently validated admissibility predicate.

**C07 — bounded qualification.** C05 supplies synthetic evidence that `T_acc` can change between frozen states/contexts, specifically 8→6 under T3, with `accept_B` and `redirect_A_to_B` closing. It does not establish temporal change of accessible transformation spaces in real systems.

**C08 — bounded qualification.** C05 represents transition, post-transition accessibility and bounded trajectory fields. Because the demonstrator is synthetic and NC2 is not a genuine trajectory-policy sensitivity test, it does not establish a causal `Delta T_acc -> trajectory` estimand.

**C16 — bounded methodological contribution.** C05 preserves an executable distinction among candidate transformations, admissibility, `T_acc`, transition, bounded trajectory, controls and explicit non-claims in an EV-grid application-fit domain. It strengthens the translation-protocol evidence without establishing transversal validity.

No propagation is made to C01, C03, C04, C05, C06, C09, C10, C11, C12, C13, C14 or C15. No claim-level status or level is changed.

## 9. Scientific boundaries and explicit non-claims

C05 does **not** establish empirical causality, generality, transversal validity, value creation, ROI, downstream operational performance, explanatory superiority, predictive superiority, real-world EV-grid validity, industrial validation, deployment readiness, or a causal `Delta T_acc -> Delta V` pathway.

It does not independently validate the baseline because the baseline implementation is identical to the admissibility function. It does not establish trajectory-policy robustness because `selection_tiebreak` is not consumed by `trajectory()`. It does not establish that the synthetic admissibility predicates correspond to an independently identified real-world EV-grid mechanism.

## 10. Governance disposition and closure

C05 is closed as **bounded synthetic methodological/application-fit evidence**. Its material result is retained because it qualifies the evidentiary basis of C02, C07, C08 and C16 without warranting a claim-level upgrade. No completed C05 gate is reopened by this enrichment, and no Core/RMA modification follows.

**Claim routing:** `C02`, `C07`, `C08`, `C16` only.

## 11. GL-07 disposition

This file is the developed material expediente for C05 and is intended to support restoration of the full autocontained C05 section in the cumulative Evidence-to-Claim Matrix. The matrix section itself remains the canonical routing/index layer and must contain the developed evidence, not merely a reference to this file, under persistent GL-07.
