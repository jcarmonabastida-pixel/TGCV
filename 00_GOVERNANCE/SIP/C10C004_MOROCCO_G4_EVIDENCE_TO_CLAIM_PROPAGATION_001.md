# C10C-004 — Morocco Gate G4 — Evidence-to-Claim Propagation 001

**Case:** `C10C-004 — Morocco microcredit / women's empowerment`
**Gate:** `G4`
**Status:** `CLOSED — OPERATIONAL RECONSTRUCTION VERIFIED`
**Date:** 2026-09-16
**Result artifact:** `00_GOVERNANCE/SIP/C10C004_MOROCCO_G4_WOMENS_EMPOWERMENT_RECONSTRUCTION_RESULT_001.md`
**Matrix predecessor:** `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` v1.10
**Propagation rule:** material evidence is added to the cumulative matrix without automatic claim-level upgrade.

## Material evidentiary contribution

C10C-004 provides a closed, independently reconstructed operationalisation of a women's-empowerment construct from a non-software empirical study. The reconstruction links questionnaire semantics, physical endline variables, observed coding, historical Stata construction rules and an independent Python implementation.

The evidence establishes the bounded transformation:

`J1...J9 responses across F1-F11 → women_1...women_9 → standardized outcomes → historical women_index`

with `J9b → women_10` separately and `J10...J13 → women_11...women_14` under their documented 3/4 rule. The historical duplicate `outcome2` and omission of `outcome3` are preserved rather than corrected.

The endline source is `Microcredit_EL_mini_anonym.dta`, N=5,551. Independent reconstruction reproduced the historical index specification and yielded no missing values in the reconstructed `women_index`.

## Claim propagation

### C01 — state/context/conditions/resources

**Impact:** Material methodological evidence, bounded.

C10C-004 demonstrates that a substantive empirical construct can be traced from instrument-level semantics through physical variables to an executable derived outcome. This supports the methodological discipline of explicit state/variable mapping but does not establish TGCV state representation or modify C01 status.

**Status:** unchanged.

### C02 — accessibility represented by transformations satisfying an independently defined admissibility predicate

**Impact:** No direct positive evidence; bounded methodological relevance only.

The women's-empowerment construct is not an independently defined TGCV accessibility predicate `P_tau(S,C,L)`. J1-J9 encode observed responses about activity autonomy, and the derived index is a study outcome. It must not be promoted to `T_acc` merely because its semantics concern capability/autonomy.

C10C-004 therefore does not establish or identify TGCV `T_acc` and does not upgrade C02.

**Status:** unchanged.

### C07 — accessible transformation spaces change over time

**Impact:** No direct evidence.

The audited G4 result concerns endline operationalisation of the empowerment construct. It does not reconstruct a TGCV transformation universe `U_tau`, an admissibility predicate or `Delta T_acc`. No C07 evidence is claimed.

**Status:** unchanged.

### C08 — accessibility changes modify reachable future trajectories

**Impact:** No direct evidence.

The empowerment index is an outcome/construct in the historical study and does not constitute a TGCV reachable-trajectory variable. No trajectory causal estimand is established.

**Status:** unchanged.

### C09 — accessibility changes causally affect subsequent trajectories

**Impact:** No evidence contribution.

C10C-004 is an operational reconstruction audit and contains no TGCV causal estimate. It is excluded from positive C09 support.

**Status:** unchanged.

### C10 — accessibility changes generate/predict value

**Impact:** No evidence contribution.

No causal or predictive `Delta T_acc → Delta V` pathway is tested or established by this gate. The women's-empowerment index is not treated as value evidence.

**Status:** unchanged.

### C11 — TGCV is domain-independent / transversal

**Impact:** Bounded methodological contribution.

C10C-004 adds a distinct non-software empirical domain in which a complex construct is reconstructed from instrument semantics to physical variables and executable derived outcome. This strengthens the documented methodological evidence base for cross-domain translation, but the construct is not itself a TGCV accessibility construct and the result does not establish transversal validity.

**Status:** unchanged.

### C12 — superior explanatory representation

**Impact:** No evidence contribution.

The case contains no controlled comparison of TGCV against an alternative explanatory representation. No ranking, superiority or claim upgrade is made.

**Status:** unchanged.

### C16 — transversal analytical translation protocol preserving distinctions

**Impact:** Material methodological evidence.

C10C-004 provides an independent worked example of explicit distinction between instrument semantics, raw variables, derived study outcomes and TGCV constructs. It demonstrates that a historical empirical outcome can be reconstructed without silently relabeling it as accessibility, trajectory or value. The retained code anomaly further demonstrates preservation of historical specification rather than post-hoc correction.

**Status:** unchanged.

## Explicit exclusions

C10C-004 is not propagated as positive evidence to C02, C07, C08, C09 or C10. It does not modify TGCV Core, RMA, the accessibility definition, the causal chain, or any claim-level status.

## Matrix action

The next cumulative matrix version must preserve all v1.10 content and add this C10C-004 evidence record. No predecessor evidence may be removed, collapsed or downgraded. The matrix version increment should therefore be **v1.11**, unless another canonical governance rule requires a different version number.
