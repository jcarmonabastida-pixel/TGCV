# TI-001 V012 NEXT4 — Experimental Specification 001

**Status:** SPECIFICATION DRAFT FROZEN FOR DESIGN REVIEW — NOT EXECUTION AUTHORIZED  
**Date:** 2026-09-30  
**Predecessor evidence:** TI-001 V012 NEXT3 Q1–Q5  
**Purpose:** Define the first discriminating experiment that tests whether the action–profile reorganisation observed in NEXT3 is specifically coupled to an explicit representation of future transformation structure, rather than being explainable by a static profile→action rule.

## 1. Scientific question

NEXT3 Q5 established a very strong action_identity × profile_id × condition interaction, while Q1/Q3 did not detect a marginal profile_id × condition effect. Q4 additionally established strong domain dependence.

NEXT4 therefore asks:

> When the visible profiles and candidate actions are held constant, does changing only the future transformation structure associated with those profiles cause the action–profile correspondence to reorganise?

The discriminating target is not greater global use of profile information. It is whether the **conditional mapping from profiles to actions follows a reassignment of future transformation structure**.

## 2. Competing explanations

### H_static — static profile→action rule

Decision selection is explained by a stable or condition-dependent association between profile identity and action identity. Reassigning a future structure to a profile does not systematically move the action–profile correspondence with that future structure.

### H_future — future-structure-conditioned reorganisation

Decision selection is sensitive to the future transformation structure associated with a profile. When future structures are reassigned across otherwise equivalent profiles, the action–profile correspondence reorganises in the direction implied by the reassignment.

NEXT4 is designed to discriminate these explanations. It does not assume in advance that H_future is true.

## 3. Core experimental manipulation

Each decision unit contains:

- four candidate actions: A, B, C, D;
- four structural profiles: slot_1, slot_2, slot_3, slot_4;
- an explicit future-structure descriptor assigned to each profile;
- one observed decision/action;
- no value, reward, utility or performance signal.

The key manipulation has two matched states.

### 3.1 Stable mapping

profile_i → future_structure_i

### 3.2 Future reassignment

The same profiles and actions are retained, but the future structures are permuted:

profile_i → future_structure_{π(i)}

The reassignment permutation must be independently specified and balanced. The surface identity, order, position and presentation of profiles must not reveal the reassignment.

The critical comparison therefore changes the **profile–future correspondence**, not the action set or profile set.

## 4. Required control structure

NEXT4 must contain at least the following conditions:

1. **STATIC_CONTROL** — future structures are fixed and consistently mapped.
2. **FUTURE_REASSIGNED** — future structures are reassigned across profiles.
3. **SURFACE_CONTROL** — presentation/permutation changes without changing the profile–future mapping.
4. **UNINFORMATIVE_NULL** — no informative profile–future correspondence.

The final fixture may add a fifth negative/control condition only if it is specified before freeze and does not introduce an additional inferential family without corresponding multiplicity control.

## 5. Future-structure representation

The future-structure variable must satisfy all of the following before fixture generation:

- be explicitly reconstructable from the fixture;
- represent a transformation or trajectory relation rather than an outcome/value;
- be independent of the observed action;
- not encode reward, utility, success, performance or preference;
- admit balanced reassignment across profiles;
- remain semantically identical under reassignment;
- permit a direct audit of which future structure was associated with each profile;
- permit a blinded/surface-equivalent control;
- be simple enough that its identity cannot be inferred merely from presentation position.

NEXT4 must **not** label this variable T_acc, Reach, Trajectory or another TGCV construct until its operational semantics have been separately audited. The initial variable is therefore provisionally named **future_structure**.

## 6. Primary discriminating estimand

The primary estimand is the change in the action–profile association induced by future-structure reassignment.

Conceptually:

action_identity × profile_id × future_structure_mapping

The primary contrast must test whether the action–profile interaction changes between the stable and reassigned mappings in a way that tracks the reassignment itself.

A successful discrimination requires more than a generic condition effect. The inferential target is specifically the **alignment between action–profile reorganisation and the known future-structure permutation**.

## 7. Identification requirement

The design must permit independent identification of:

- action identity;
- profile identity;
- future-structure identity;
- profile→future mapping;
- condition;
- presentation;
- domain;
- operationalisation;
- replicate.

All relevant action×profile and profile×future combinations must have sufficient representation for the declared interaction.

Before any scientific fit:

1. construct every declared design matrix;
2. verify full rank;
3. verify that the future reassignment is not aliased with presentation;
4. verify that domain is balanced across mapping conditions;
5. verify that action identities are balanced;
6. verify that no future-structure identifier is perfectly predictive of action;
7. verify that the null condition contains no recoverable future correspondence.

Any failure blocks execution. No post-hoc recoding, term removal or alternative model is permitted.

## 8. Domain control

NEXT3 Q4 showed very strong domain dependence. NEXT4 therefore treats domain as a design factor, not merely a nuisance covariate.

The fixture must:

- retain multiple domains;
- balance stable/reassigned mappings within every domain;
- balance future-structure permutations within every domain;
- prevent a particular future structure from being associated preferentially with one domain;
- report domain-specific estimates descriptively;
- preserve a pre-specified pooled primary estimand only if the design matrix remains identifiable.

NEXT4 does not claim to establish transversal validity merely by including multiple domains.

## 9. Presentation controls

The reassignment must be orthogonal to:

- order;
- position;
- orientation;
- format.

Presentation permutations must be balanced independently of the future-structure mapping.

A surface control must reproduce the relevant presentation changes without changing the underlying profile→future mapping.

## 10. Secondary analyses

Secondary analyses may examine:

- action×profile association under each mapping;
- domain-specific modulation;
- operationalisation-specific modulation;
- replicate stability;
- surface-control effects;
- descriptive correspondence between the observed action reassignment and the known future permutation.

These are secondary unless explicitly promoted into the frozen primary family before execution.

## 11. Interpretation rules

### Positive discriminating result

A result supports H_future only if the action–profile reorganisation is specifically aligned with the independently imposed future-structure reassignment and survives the frozen surface controls and multiplicity policy.

### Null discriminating result

A null result weakens the hypothesis that the NEXT3 Q5 interaction is specifically driven by future-structure reassignment, but does not establish that static profile→action rules are the only explanation.

### Generic condition effect

A difference between STATIC_CONTROL and FUTURE_REASSIGNED without alignment to the known reassignment is **not sufficient** evidence for H_future.

### Presentation effect

A difference explained by presentation is treated as a control/artifact result, not evidence for future-structure sensitivity.

## 12. TGCV interpretation boundary

NEXT4 is intended to test a mechanism relevant to the Transformational Intelligence research programme.

It does not, by itself, establish:

- Transformational Intelligence;
- a unique cognitive or agent-level mechanism;
- causal value generation;
- a causal ΔT_acc → Value pathway;
- transversal validity;
- generalisation beyond the frozen experimental population.

If the future-structure representation later passes a separate semantic audit, its relation to TGCV constructs may be analysed without retroactively relabelling the original experiment.

## 13. Statistical governance

The final statistical analysis plan must be frozen in a separate execution-level specification after the future-structure representation and fixture design are fully specified.

That specification must declare:

- exact model formulae;
- reference levels;
- primary contrast;
- degrees of freedom;
- multiplicity family;
- covariance/fit method;
- rank and singularity rules;
- coefficient and confidence-interval reporting;
- missing/invalid record rules;
- immutable join key;
- fixture and execution hashes.

No scientific execution is authorized by this document.

## 14. Required pre-execution gates

Before any fixture freeze or scientific execution:

1. **Semantic gate:** audit the future-structure representation.
2. **Counterfactual gate:** prove that stable and reassigned conditions differ only in the intended mapping.
3. **Leakage gate:** prove future structure does not encode action, reward, utility, performance or presentation.
4. **Balance gate:** verify domain/action/presentation/future-structure balance.
5. **Identifiability gate:** construct and rank-check all declared models.
6. **Implementation-equivalence gate:** verify implementation against the frozen statistical specification.
7. **Fixture freeze gate:** hash and freeze the complete fixture.
8. **Scientific execution gate:** require explicit authorization after all previous gates pass.

## 15. Decision criterion for progression

NEXT4 should progress to fixture construction only if the design review confirms that the future-structure reassignment constitutes a genuine intervention on the explanatory variable while preserving the action and profile spaces.

The next artifact after this specification should therefore be a **future-structure semantic/control specification**, not a scientific execution result.

## 16. Non-claims

This specification does not claim that NEXT3 demonstrated future-structure processing.

It does not claim that the proposed future-structure variable is already T_acc.

It does not claim that NEXT4 will demonstrate Transformational Intelligence.

It defines a falsifiable experiment intended to distinguish two explanations for the NEXT3 Q5 interaction.
