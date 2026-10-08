# TGCV — Ω-primary Architectural Comparative Review 001

**Document ID:** TGCV_OMEGA_PRIMARY_ARCHITECTURAL_COMPARATIVE_REVIEW_001  
**Date:** 2026-10-08  
**Status:** WORKING / PROPOSED / NON-CANONICAL / ARCHITECTURAL REVIEW  
**Scientific execution:** NOT AUTHORIZED BY THIS DOCUMENT  
**Scope:** comparative architectural review and decision gate  
**Base architecture:** post-TR-140 stabilized architecture  
**Current Evidence→Claim Matrix:** v1.47

> This document is a comparative architectural review. It does not adopt Ω-primary as canonical, does not modify the TGCV Core, does not modify claim status, and does not authorize a new scientific execution. Its purpose is to determine whether Ω-primary is best understood as (a) a representational reformulation, (b) an additional analytical layer, (c) an architectural transition requiring a governed gate, or (d) an insufficiently operationalized proposal.

## 1. Decision question

The decision question is:

> **Is Ω-primary merely a richer representation of the existing transformational-accessibility architecture, an additional analytical layer, or a genuinely different architecture requiring a formal transition gate?**

The review must not begin from the assumption that Ω-primary is correct.

The relevant alternatives are:

1. **Representational extension:** Ω-primary represents information already contained in the existing architecture without changing its ontological or analytical organization.
2. **Analytical extension:** Ω-primary introduces a useful non-ontological structure that is not equivalent to T_acc, while Core_ontological = S remains intact.
3. **Architectural transition:** Ω-primary requires a new structural object that cannot be adequately treated as a representation or analytical layer under the current architecture.
4. **Non-operationalized proposal:** Ω-primary may be conceptually coherent but cannot presently be identified, reconstructed or falsified with sufficient independence.

The review is successful only if it can distinguish these outcomes.

## 2. Governance position before the review

The current architecture remains:

Core_ontological = S

with the analytical structure:

T_acc = F(S,C,L)

and the established dynamic chain:

ΔT_acc → ΔReach → ΔTrajectory

with downstream outcome/value analysis kept separate.

The current architecture does **not** contain Ω-primary as a canonical Core primitive.

Ω-primary therefore enters this review as:

**PROPOSED / NON-CANONICAL / UNDER INVESTIGATION.**

No existing claim is upgraded, downgraded or redefined by this document.

## 3. Candidate Ω-primary representation

The candidate object is:

Ω_T,t = (U_t, ≡_T, R_t)

where, provisionally:

- U_t = identifiable universe of candidate transformations at time t;
- ≡_T = identity/equivalence relation over transformations;
- R_t = structural relations among transformations.

The candidate temporal dynamics are:

Ω_T,t → τ → Ω_T,t+1

and a provisional decomposition is:

ΔΩ_T = (ΔU, Δ≡_T, ΔR, ΔT_acc)

This decomposition is a working hypothesis, not a frozen definition.

The critical point is that T_acc would become a property or projection derived from a broader transformational structure rather than necessarily being the primary represented object.

## 4. Comparison A — current Core = S

The stabilized architecture deliberately separates ontological minimality from analytical structure:

Core_ontological = S

while transformational structure is represented analytically.

This follows the post-TR-140 governance boundary: the fact that an object is analytically necessary does not automatically make it a new ontological primitive.

Ω-primary does not, by itself, require replacing S.

The candidate interpretation can therefore remain:

S → Ω_T → T_acc → Reach → Trajectory

without introducing Ω as a new ontological primitive.

**Preliminary result: no demonstrated ontological contradiction.**

Ω-primary is compatible with Core_ontological = S at least at the level of the present proposal.

Therefore the existence of Ω-primary does **not** by itself justify reopening the ontological Core.

## 5. Comparison B — T_acc = F(S,C,L)

The current accessibility representation is:

T_acc = {τ | P_τ(S,C,L)=1}

or equivalently:

T_acc = F(S,C,L)

This representation has already passed the conceptual non-circularity/determinacy boundary in the prior architecture.

The issue is therefore not that T_acc is invalid.

The question is whether it is the **most informative primary representation** for a domain in which transformations have identities, dependencies, relations and longitudinal structural change.

Ω-primary proposes:

Ω_T = (U, ≡_T, R)

followed by a derivation such as:

T_acc = 𝔽(Ω_T,S,C,L)

The comparison is therefore one of representational ordering and information content, not a correction of a known logical error in T_acc.

**Preliminary result:** Ω-primary is not refuted by the validity of T_acc. Conversely, the existence of Ω does not establish that T_acc is insufficient.

The discriminating question is whether Ω contains structurally relevant information that is not adequately represented by T_acc and whether that information can be independently observed.

## 6. Representation versus ontology

The review adopts the following integrity rule:

> **Representational richness is not ontological necessity.**

A structure may be derivable from S, reconstructible from T_acc, more convenient to analyze, or more expressive for certain questions without becoming a new ontological primitive.

Likewise:

> **Operational usefulness is not ontological necessity.**

A new object should be promoted to the ontological Core only if the comparison demonstrates that the current ontology cannot adequately account for the phenomenon without it.

At present, no such demonstration has been established.

## 7. Historical levels

Historical TGCV material contains an antecedent distinction between systems that merely change state and systems whose future transformation possibilities are modified.

Two historical formulations are especially relevant.

### Four-level formulation

- Level 0 — static systems;
- Level 1 — regulative systems;
- Level 2 — adaptive systems;
- Level 3 — generative systems.

### Later compact formulation

Change → Adaptation → Generation

These formulations are historical conceptual antecedents, not the current canonical taxonomy.

A possible correspondence such as:

ΔS

ΔT_acc

ΔΩ_T

for different levels is therefore a **hypothesis to test**, not an established mapping.

Historical continuity cannot be used as evidence that Ω-primary is ontologically necessary.

## 8. Comparison C — Rust Omega

Rust Omega is relevant because it confronts the representation of transformation structure computationally.

The appropriate questions are:

1. Which elements of U can actually be identified?
2. Which transformation identities/equivalences can be reproduced?
3. Which relations R can be reconstructed independently?
4. Which parts of Ω are derivable from S?
5. Does Ω distinguish cases that an explicit T_acc representation does not?
6. Are observed differences genuinely discriminating, or merely different encodings of the same information?

The methodological rule is:

not discriminated ≠ refuted

If Ω can be reconstructed from S, this does not by itself prove that Ω is analytically redundant. It may instead show that Ω is a derived but potentially superior representation.

Conversely, a richer representation is not evidence of a new ontology unless its non-reducibility has been demonstrated.

**Preliminary disposition:** Rust Omega is relevant evidence for the representability question, not ontological validation of Ω-primary.

## 9. Comparison D — VIATRA V002

VIATRA V002 provides a different kind of evidence: operational identification and replay of a transformation through a traceable structure of the form:

pre-state → τ → post-state

This matters because Ω-primary treats transformations as identifiable structural objects rather than merely as differences between snapshots.

The decisive questions are:

- Can τ be identified independently of its outcome?
- Can multiple transformations be related structurally?
- Can transformation identity remain stable across executions?
- Can relations among transformations be reconstructed without using future outcomes?
- Can changes in the transformational structure be observed longitudinally?

A positive answer to these questions would strengthen the operational plausibility of Ω-primary.

It would not, however, establish a new ontology.

**Preliminary disposition:** VIATRA V002 provides bounded operational evidence relevant to transformation observability and replay, not evidence that Ω-primary is a canonical ontology.

## 10. Why the accessibility-predicate problem matters

In real domains, an accessibility predicate may depend on:

- resources;
- dependencies;
- composition;
- precedence;
- constraints;
- contextual conditions;
- temporal availability;
- prior transformations;
- incompatibilities;
- relations among transformations.

As this relational structure becomes explicit, a collection of independent predicates may become an indirect encoding of a richer transformation structure.

This creates a legitimate architectural question:

> Is P_τ(S,C,L) the natural primary representation, or is it more natural to represent the transformation space and derive accessibility from it?

This is a motivation for comparison, not evidence for Ω-primary.

Representation difficulty must not be confused with falsification of the existing architecture.

## 11. Candidate architectural alternatives

### A. Current architecture retained

S → T_acc → Reach → Trajectory

Ω is closed as a representational reformulation or auxiliary notation if no independent analytical gain is demonstrated.

### B. Analytical Ω layer

S → Ω_T → T_acc → Reach → Trajectory

Here:

- S remains the ontological Core;
- Ω is an explicit analytical structure;
- T_acc is derived from Ω plus conditions;
- no ontological transition is required.

### C. Ω-primary architectural transition

S → Ω_T → ...

would become the principal architecture only if comparison demonstrates that Ω captures a necessary structural dimension that cannot be adequately represented as a derived/auxiliary object under the current architecture.

This outcome would require a formal transition gate.

### D. Ω remains open

If Ω cannot yet be independently identified or discriminated, the correct disposition is to keep it as a non-canonical hypothesis rather than forcing a decision.

## 12. Discriminating criterion

The strongest conceptual discriminator identified at this stage is a case in which:

ΔT_acc = 0

while:

ΔΩ_T ≠ 0

and the difference is:

1. operationally identifiable;
2. reproducible;
3. independent of future outcomes;
4. structurally meaningful;
5. capable of affecting subsequent accessibility or trajectory.

Such a case would show that Ω contains information not exhausted by the instantaneous accessible-transformations set.

The converse case is also important: if every relevant change in Ω is adequately captured by the current T_acc representation for the intended scientific questions, then Ω may remain a useful but non-essential representation.

Neither case should be assumed before analysis.

## 13. Comparative decision matrix

| Finding | Architectural disposition |
|---|---|
| Ω is equivalent to T_acc for the intended questions | Close Ω as a reformulation |
| Ω is richer but fully reducible and analytically redundant | Retain current architecture; Ω may remain auxiliary |
| Ω is richer, reducible, but materially improves representation/analysis | Retain Core; evaluate Ω as an analytical layer |
| Ω is non-reducible as an analytical object but not ontologically necessary | Open analytical architecture review |
| Ω requires a new ontological entity | Open formal architectural transition gate |
| Ω cannot be independently identified | Keep as non-operationalized proposal |
| Evidence is insufficient to discriminate | Keep Ω open; design only the minimum discriminating analysis |

The decision must be based on evidence, not preference for elegance or implementation convenience.

## 14. Falsification and closure conditions

Ω-primary should be considered weakened or closed if:

- its apparent additional information is only a relabelling of T_acc;
- its structural relations cannot be identified independently;
- its identity relation cannot be operationalized reproducibly;
- it requires future outcomes to define present transformations;
- its proposed advantage disappears under a strong current-architecture representation;
- no discriminating scientific question can be formulated.

Ω-primary should be strengthened, but not yet canonized, if:

- transformation identities are independently observable;
- structural relations are reproducible;
- Ω changes can be measured longitudinally;
- Ω distinguishes cases not represented adequately by T_acc;
- the distinction survives strong controls and alternative encodings.

## 15. Relationship to Transformational Space Dynamics

If Ω survives the comparative review as a useful non-redundant analytical object, the next research direction can be formulated as:

Transformational Space → Transformational Space Dynamics

with:

Ω_T,t → Ω_T,t+1

The subsequent question of Transformational Intelligence remains a separate research programme:

Transformational Space Dynamics → Transformational Intelligence

No causal or construct-validity claim is implied by this conceptual chain.

## 16. Methodological order

The required order is:

Disquisition → Comparative Review → Architectural Decision → Gate (if required) → Experimental Design

not:

Experiment → representation problem → post-hoc architecture change

This ordering protects the programme from circularly treating an operational difficulty as evidence for a new architecture.

## 17. Current assessment

On the evidence currently available, the review does **not** justify:

- modifying Core_ontological = S;
- replacing T_acc = F(S,C,L);
- promoting Ω-primary to canonical status;
- introducing a new ontological primitive;
- authorizing a new scientific execution.

At the same time, the present evidence is sufficient to justify a **formal comparative review of Ω as a candidate analytical representation**, because:

- the candidate structure is explicitly defined;
- there is a historical conceptual antecedent;
- Rust Omega provides relevant computational/structural evidence;
- VIATRA V002 provides relevant operational transformation evidence;
- the distinction between T_acc and a broader transformation structure is a discriminable conceptual question.

This is therefore an **open architectural investigation**, not a transition.

## 18. Required next step

Before any new experiment, the review should be completed against the strongest available material records, explicitly tabulating for each architecture:

- primitive/object represented;
- required inputs;
- derived outputs;
- information added;
- information lost;
- observability;
- reproducibility;
- reducibility;
- leakage risks;
- falsification criterion;
- scientific question enabled.

The minimum comparison set is:

1. Core = S;
2. T_acc = F(S,C,L);
3. P_τ(S,C,L);
4. Ω_T = (U,≡_T,R);
5. Rust Omega;
6. VIATRA V002;
7. historical levels.

Only after this comparison should the programme decide whether a dedicated architectural transition gate is warranted.

## 19. Governance disposition

**Current status:** OPEN — NON-CANONICAL ARCHITECTURAL INVESTIGATION

**Core:** unchanged.

**Claims:** unchanged.

**Evidence→Claim Matrix:** unchanged by this document.

**Scientific execution:** not authorized.

**Decision:** pending completion of the comparative discrimination described above.

**Integrity rule:** historical continuity, representational convenience, implementation success, or conceptual elegance are not by themselves grounds for architectural promotion.


## 20. Material evidence reconciliation

The preceding sections define the comparison logic. This section anchors that logic to governed material records already present in the repository. These records are evidence inputs to the review; listing them does not create new claims.

### 20.1 Current inherited architecture

**Primary records:**

- `01_CORE/architecture/TGCV_CORE_v_current.md`
- `01_CORE/architecture/TGCV_ARCHITECTURE_CURRENT.md`

These establish the current baseline:

`Core_ontological = S`

`T_acc = F(S,C,L)`

`τ ∈ T_acc iff P_τ(S,C,L)=1`

and:

`ΔT_acc → ΔReach → ΔTrajectory`

The current architecture treats `T_acc` as an analytical representation rather than an independently postulated ontological primitive.

**Review implication:** Ω-primary must demonstrate something more specific than the already admitted ability to represent changes in `T_acc`.

### 20.2 Ω-primary candidate definition

**Primary record:**

`00_GOVERNANCE/architecture/TGCV_OMEGA_PRIMARY_DEFINITION_AND_ARCHITECTURAL_MEANING_001.md`

This defines:

`Ω_T,t = (U_t, ≡_T, R_t)`

and explicitly distinguishes Ω from `T_acc`, Reach and `ΔReach`.

It proposes:

`Ω_T,t → T_acc,t`

with accessibility derived from Ω and current conditions.

**Review implication:** this is the conceptual definition being compared, not empirical proof of its necessity.

### 20.3 Ω-primary boundary admissibility

**Primary record:**

`00_GOVERNANCE/architecture/TGCV_OMEGA_PRIMARY_BOUNDARY_ADMISSIBILITY_REVIEW_v0.1.md`

Disposition:

**FORMALLY ADMISSIBLE / EMPIRICALLY NOT YET ADMITTED.**

The record identifies four empirical bottlenecks:

1. reproducible transformation identity;
2. independently observable structural relations;
3. longitudinal correspondence;
4. survival of a state-only reconstruction test.

**Review implication:** formal coherence is established at the governance-design level; empirical discrimination remains unresolved.

### 20.4 Rust Ω-primary sequence

The governed Rust sequence decomposes the problem as follows:

| Record | Established contribution | Limitation for architectural discrimination |
|---|---|---|
| `TGCV_OMEGA_PRIMARY_DOMAIN_INSTANTIABILITY_REVIEW_v0.1.md` | Rust is the strongest retained domain candidate; package/version/dependency records are native structural observations | Complete Ω tuple not yet instantiated |
| `TGCV_RUST_OMEGA_PRIMARY_SEMANTIC_INSTANTIABILITY_REVIEW_v0.1.md` | Candidate transformation `τ=(origin_version_id,target_package_id,target_version_id)` can be defined independently of accessibility | `≡_T` semantic adequacy remains open |
| `TGCV_RUST_OMEGA_PRIMARY_TRANSFORMATION_EQUIVALENCE_AND_RELATION_SCHEMA_REVIEW_v0.1.md` | Canonicalisation rule, typed `R_t`, provenance and outcome-blind construction are specified | Longitudinal `κ` and empirical independence remain open |
| `TGCV_RUST_OMEGA_PRIMARY_STATE_REDUCIBILITY_AND_NON_CIRCULARITY_AUDIT_v0.1.md` | Explicit A-vs-Ω reducibility test is defined; non-circularity requirements are frozen | Matched `A_1=A_2` / `Ω_1≠Ω_2` construction was not demonstrated |

The decisive Rust result is therefore **NOT DISCRIMINATED**, not refuted.

### 20.5 Domain-level evidence

`TGCV_OMEGA_PRIMARY_DOMAIN_INSTANTIABILITY_REVIEW_v0.1.md` reports:

- MT5: blocked;
- C10C-004: blocked;
- KGFS: blocked;
- Rust: conditional candidate.

This prevents combining partial observations from different domains into a synthetic Ω-primary proof.

### 20.6 VIATRA evidence

**Primary record:**

`00_GOVERNANCE/architecture/TGCV_RUNTIME_SYSTEM_CANDIDATE_VIATRA_EVIDENCE_REVIEW_001.md`

The record establishes that VIATRA exposes transformation activity and runtime callbacks around activation firing, but at the evaluated candidate-selection stage it remained **DEFERRED** for scientific admission.

The key limitation was the absence, at that stage, of an independently frozen temporal observation boundary suitable for the TGCV architectural discrimination programme.

Later V002 work may provide relevant operational evidence of transformation observation and replay, but it must not be retroactively interpreted as proof of Ω-primary's ontological superiority.

**Review implication:** VIATRA is evidence for operational observability of transformation events, not by itself evidence for architectural non-reducibility.

### 20.7 Architectural transition evidence already assessed

**Primary records:**

- `TGCV_ARCHITECTURAL_TRANSITION_EVIDENCE_ASSESSMENT_v0.1.md`
- `TGCV_ARCHITECTURAL_TRANSITION_GATE_RECORD_v0.1.md`
- `TGCV_ARCHITECTURAL_DISCRIMINATION_CRITERIA_v0.1.md`

These records already distinguish bounded evidence, non-discriminating evidence, A-equivalent constructions, the closed O4/E3 shortcut, and the requirement for independent measurement plus A-reconstruction failure.

In particular, ARCH-DISC-002 is recorded as **A-EQUIVALENT**, and the isolated E3 route is closed.

**Review implication:** the present Ω-primary review must not reopen either path by relabelling an A-derived descriptor as an independent Ω object.

## 21. Consolidated comparison matrix

| Dimension | Current Core / A | Ω-primary candidate | Rust evidence | VIATRA evidence |
|---|---|---|---|---|
| Primary object | `S` | `Ω_T=(U,≡_T,R)` | Candidate constructible conditionally | Transformation events observable operationally |
| Accessibility | Primary analytical object `T_acc=F(S,C,L)` | Derived from Ω plus conditions | Candidate accessibility separated from U | Runtime execution provides event context, not complete Ω boundary |
| Transformation identity | Defined relative to accessibility predicate | Explicit canonical identity/equivalence required | Observational identity specified; semantic equivalence open | TGCV identity schema required independently |
| Relations | Auxiliary/mechanistic where governed | Explicit typed `R_t` | Dependency relation is native candidate | Runtime/event relations observable, but independence must be demonstrated |
| Longitudinal correspondence | Via state/time and derived contrasts | Explicit `κ` required | Conditional/open | Temporal observation boundary was initially not admitted |
| Outcome blindness | Required | Explicit firewall | Design satisfied conditionally | Candidate can be evaluated without value/reward |
| Reducibility test | Baseline | Must survive A reconstruction | Not passed | Not yet a discriminating result |
| Architectural status | Current | Proposed/non-canonical | Conditional candidate | Operationally supportive, not architectural proof |
| Empirical admission | Current | Not granted | Not granted | Not granted as Ω-primary evidence |

## 22. Updated discrimination statement

The material record permits a sharper conclusion than the initial conceptual review:

**Ω-primary is formally coherent and operationally motivated, but the decisive architectural discriminator has not yet passed.**

The strongest existing negative evidence is not that Ω cannot be constructed. It is that the current candidate Rust `Ω` has **not demonstrated information irreducible to the inherited `A=(S,T_acc)` representation** under a frozen reconstruction rule.

The strongest positive evidence is that the Ω construction changes the observation boundary conceptually: candidate transformations can be defined before accessibility, and structural relations can be represented explicitly.

These two facts are compatible.

Therefore the present comparative review should not force a binary choice between “Ω is false” and “Ω replaces A”. The evidence supports the intermediate status:

> **Ω-primary remains an open candidate analytical architecture whose non-reducibility has not yet been demonstrated.**

## 23. Architectural decision checkpoint

The review therefore reaches the following checkpoint:

**Current disposition: ANALYTICAL-CANDIDATE / NON-CANONICAL / NON-DISCRIMINATED.**

This is stronger than merely “conceptually interesting” but weaker than “architectural transition justified”.

A transition gate should be opened only if a future controlled comparison establishes all of the following:

1. an independently observable Ω component;
2. a frozen construction independent of accessibility and outcomes;
3. a reproducible longitudinal correspondence;
4. failure of the admissible A-reconstruction;
5. a scientific consequence of that non-reducible structure;
6. independent or materially distinct replication.

Until then:

`Core = S`

`T_acc = F(S,C,L)`

and the inherited dynamic chain remain current.

## 24. Governance correction

This review uses **Evidence→Claim Matrix v1.47** as its current governance baseline. Several inherited historical records retain older version references (notably v1.44); those labels are preserved for traceability and are not rewritten merely to synchronize historical documents.

Thus:

- **current governance state:** Matrix v1.47;
- **historical evidence records:** preserve their original version labels;
- **this review:** uses v1.47 as its current governance baseline.

No scientific content or claim is altered by this correction.


## 25. Three-stage architectural discrimination

The comparative review now separates three questions that must not be collapsed:

### 25.1 Representability

**Question:** Can the proposed Ω object be instantiated, observed or reconstructed in a real domain?

This is the weakest threshold.

A positive result establishes that Ω is not merely syntactically defined. It does **not** establish that Ω adds information beyond the current architecture.

Current disposition:

**Conditionally supported.**

Rust provides the strongest retained candidate for domain instantiation, while VIATRA provides bounded evidence that transformation events can be operationally observed and replayed. Neither result establishes the complete Ω tuple independently.

### 25.2 Reducibility

**Question:** When Ω is instantiated, can the relevant Ω information be reconstructed from the inherited architecture under a frozen, outcome-blind rule?

The relevant inherited object is:

`A = (S,T_acc)`

The test is therefore not whether Ω can be computed from the state in some unrestricted sense. The test is whether the Ω information that is claimed to matter can be recovered from A without introducing the very Ω information being tested.

The decisive comparison is consequently:

`A_1 = A_2`

versus

`Ω_1 ≠ Ω_2`

under a pre-registered construction and without access to downstream outcomes.

If such a pair is reproducibly demonstrated, Ω has passed the key non-reducibility discriminator.

If no such pair can be constructed, that does not prove that Ω is conceptually false; it means that the proposed architectural distinction has not been demonstrated.

Current disposition:

**NOT DEMONSTRATED.**

### 25.3 Architectural necessity

**Question:** Even if Ω is representable and non-reducible, does the scientific programme require Ω to occupy a primary architectural position?

This is a stronger threshold than non-reducibility.

A structure may be non-reducible for a particular representation while still being appropriately governed as an analytical layer rather than as an ontological or canonical Core primitive.

Architectural necessity therefore requires an additional argument:

1. Ω contains a discriminating structural component;
2. that component cannot be recovered from the inherited architecture;
3. the component changes or enables a scientific question central to TGCV;
4. the scientific consequence survives alternative representations and controls;
5. treating Ω as merely auxiliary would materially obscure or invalidate the target analysis.

Current disposition:

**NOT ESTABLISHED.**

## 26. Discrimination ladder

The review can therefore be represented as the following ladder:

`Representability → Reducibility → Analytical necessity → Architectural necessity`

The thresholds have different meanings:

| Threshold | What a PASS establishes | What it does not establish |
|---|---|---|
| Representability | Ω can be instantiated/observed | Ω adds indispensable information |
| Non-reducibility | Ω contains information not recovered by A under the frozen test | Ω must become canonical |
| Analytical necessity | Ω materially enables a scientific analysis not adequately supported by A | New ontology |
| Architectural necessity | Current architecture is inadequate without Ω as a primary structure | Any downstream value/causal claim |

This ladder prevents a common category error: treating successful implementation as evidence of architectural necessity.

## 27. Consequence for the current decision

The present evidence occupies the ladder approximately as follows:

- **Representability:** conditionally supported;
- **Non-reducibility:** not demonstrated;
- **Analytical necessity:** not established;
- **Architectural necessity:** not established.

Therefore the current evidence cannot legitimately trigger an architectural transition gate.

At the same time, the review has identified a precise empirical discriminator rather than leaving Ω-primary at the level of conceptual preference.

## 28. Minimum decisive test

If the programme later decides that an experiment is warranted, the experiment should be designed around the smallest possible discriminating construction:

`A_1 = A_2`

while:

`Ω_1 ≠ Ω_2`

with the following controls:

- Ω construction frozen before execution;
- no downstream outcome/value information;
- identical state representation;
- identical accessibility representation;
- identical observation window;
- independently defined transformation identity/equivalence;
- reproducible relation construction;
- deterministic reconstruction procedure;
- explicit audit of leakage from Ω into A.

A failed attempt to produce the pair is informative only if the search space and reconstruction rule were sufficiently complete to support the conclusion.

No scientific execution is authorized by this section.

## 29. Decision rule after the minimum test

The future result should be interpreted as follows:

| Result | Disposition |
|---|---|
| No reproducible `A_1=A_2, Ω_1≠Ω_2` pair | Ω remains non-discriminated |
| Pair exists, but distinction has no scientific consequence | Ω may remain an analytical auxiliary |
| Pair exists and enables a material scientific distinction | Open analytical architecture review |
| Pair exists, distinction is indispensable to the target construct, and auxiliary treatment fails | Consider formal architectural transition gate |
| Construction depends on outcome/future information | Reject the discrimination as circular |
| Identity/equivalence is unstable or non-reproducible | Ω-primary remains non-operationalized |

This preserves the asymmetry between **evidence for non-reducibility** and **evidence for architectural promotion**.

## 30. Interim architectural conclusion

The comparative review therefore does not conclude:

> “Ω-primary is the new architecture.”

Nor does it conclude:

> “Ω-primary has been refuted.”

Its current conclusion is narrower and more useful:

> **Ω-primary has crossed the threshold of a serious architectural candidate, but has not crossed the threshold of demonstrated non-reducibility, analytical necessity, or architectural necessity.**

Accordingly, the current TGCV architecture remains unchanged while Ω-primary remains under governed investigation.


## 31. Final comparative audit: what would actually change

The review must distinguish **what Ω changes in representation** from **what Ω changes in the scientific object of inquiry**.

### 31.1 If Ω is only a reordering

If:

Core representation is derivable from the same information

and:

T_acc is recoverable from Ω plus the same conditions,

without introducing an independently discriminating object, then Ω primarily changes the order in which the same information is represented.

In that case the appropriate disposition is:

**representational reformulation / auxiliary notation.**

No architectural transition is warranted.

### 31.2 If Ω exposes relations hidden by T_acc

If Ω makes explicit:

- transformation identity;
- equivalence classes;
- dependencies;
- compatibility/incompatibility;
- compositional structure;
- temporal correspondence;

and those relations cannot be adequately recovered from the inherited A representation, then Ω may constitute a genuine **analytical layer**.

The relevant consequence would not be “Ω is more elegant”, but:

> a scientific question about transformation-space structure becomes materially tractable only when Ω is explicitly represented.

That would justify an analytical architecture review while leaving the current ontological Core intact.

### 31.3 If Ω changes the primitive of explanation

A much stronger result would occur if the target phenomenon could no longer be adequately formulated as:

state → accessible transformations → reachable trajectories

and instead required:

transformation-space → space dynamics → subsequent accessibility

as the explanatory primitive.

Only that result would provide a serious basis for considering Ω-primary as an architectural transition.

Even then, the transition would require its own governance gate.

## 32. Information accounting

The comparative test should therefore record, for each representation, four distinct categories:

| Category | Question |
|---|---|
| Input information | What must already be known to construct the representation? |
| Explicit information | What structure is directly represented? |
| Derived information | What can be reconstructed from it? |
| Lost/implicit information | What distinctions disappear or become inaccessible? |

This is more informative than comparing formulas alone.

A representation can be mathematically equivalent while being scientifically different in **observability**, **auditability**, or **construct isolation**.

Conversely, a representation can be operationally convenient while containing no genuinely new information.

## 33. The critical asymmetry

The review identifies an important asymmetry:

> To reject Ω as architecturally necessary, it is sufficient to show that its claimed scientific distinctions are reproducibly recoverable from the inherited architecture under the frozen reconstruction rule.

> To promote Ω architecturally, it is not sufficient merely to show that Ω is richer or easier to use; one must demonstrate a non-reducible, scientifically consequential structural distinction.

This asymmetry should govern any subsequent experiment and prevents the burden of proof from being inverted.

## 34. Architectural status after comparative audit

The review therefore records the following provisional state:

**Current TGCV architecture**

Core = S

T_acc = F(S,C,L)

ΔT_acc → ΔReach → ΔTrajectory

**Ω-primary**

Ω_T,t = (U_t, ≡_T, R_t)

Status:

**PROPOSED / NON-CANONICAL / ANALYTICAL-CANDIDATE / NON-DISCRIMINATED**

**Architectural transition:**

**NOT JUSTIFIED**

**Scientific execution:**

**NOT AUTHORIZED**

## 35. Closure condition for this review

This comparative review should not be kept open indefinitely merely because Ω-primary is interesting.

It can be closed in either of two scientifically clean ways:

### Closure A — reduction

A controlled analysis demonstrates that every claimed Ω distinction relevant to TGCV can be recovered from the inherited architecture under the frozen reconstruction rule.

Disposition:

**Ω-primary closed as non-essential reformulation/auxiliary representation.**

### Closure B — transition evidence

A controlled analysis demonstrates a reproducible non-reducible Ω distinction with material scientific consequence, followed by independent replication and architectural analysis.

Disposition:

**Open formal architectural transition gate.**

Until one of these conditions is met, the correct state is:

**OPEN / NON-DISCRIMINATED.**

## 36. Review boundary

This document deliberately does **not** decide:

- whether transformational space exists as an ontological entity in nature;
- whether Transformational Space Dynamics is a valid scientific construct;
- whether Transformational Intelligence follows from such dynamics;
- whether Ω-related dynamics cause Value;
- whether any observed Ω distinction has downstream causal significance.

Those are subsequent scientific questions.

The present review asks only:

> **Does Ω-primary provide a sufficiently distinct and necessary representation to justify changing TGCV's current architecture?**

At present, the answer is:

**Not yet demonstrated.**


## 37. Evidence sufficiency audit

The decisive question is now whether the material already accumulated is sufficient to close Ω-primary by reduction, or whether the minimum discrimination test remains necessary.

### 37.1 Evidence sufficient for Closure A?

**No.**

The existing material does establish that:

- Ω can be formally specified;
- parts of Ω can be instantiated conditionally;
- transformation identity and relations can be operationally discussed;
- the inherited architecture can represent accessible transformations;
- prior A-equivalent constructions do not establish Ω non-reducibility.

However, the existing material does **not** establish the stronger proposition:

> every scientifically relevant Ω distinction can be reconstructed from A under a frozen, outcome-blind reconstruction rule.

Absence of an observed counterexample is not equivalent to a proof of reducibility.

Therefore Closure A would currently be premature.

### 37.2 Evidence sufficient for architectural transition?

**No.**

The existing material does not establish:

- a reproducible A1=A2, Ω1≠Ω2 construction;
- an independent scientific consequence of that distinction;
- replication of such a distinction;
- failure of the inherited architecture as an adequate analytical framework.

Therefore Closure B is also premature.

### 37.3 What remains genuinely unresolved?

The unresolved proposition is now sharply bounded:

> **Can Ω contain an empirically identifiable structural distinction that survives reconstruction from the inherited A representation?**

This is narrower than asking whether Ω is philosophically real, whether Ω is useful, or whether transformation space exists.

### 37.4 Minimum evidence required

The minimum evidence required to resolve the question is therefore not another broad experiment.

It is a **controlled architectural discrimination test** with:

A1=A2

and:

Ω1≠Ω2

plus independent verification that:

1. the two cases are genuinely equivalent under A;
2. the Ω difference is not an encoding artifact;
3. the Ω construction is frozen before observing downstream consequences;
4. transformation identity/equivalence is reproducible;
5. the Ω distinction has a measurable structural consequence relevant to TGCV.

### 37.5 Decision

The comparative review therefore reaches a precise methodological conclusion:

> **The existing evidence is insufficient to close Ω-primary by reduction and insufficient to justify an architectural transition. A minimum controlled discrimination test is therefore warranted in principle, but no scientific execution is authorized by this review.**

The next governance action, if the programme chooses to continue, is to define the test specification and its pre-execution gate—not to execute it directly.


## 38. Reconciliation with prior architectural discriminators

The review must explicitly prevent a false restart of previously exhausted discriminator routes.

### 38.1 D1 is historical/superseded

The former D1 route tested:

`T_acc^(1)=T_acc^(2)`

with a proposed difference in:

`G_τ^(1)≠G_τ^(2)`

That route is recorded as **HISTORICAL / SUPERSEDED / NON-OPERATIVE**.

It must not simply be revived under Ω-primary terminology.

### 38.2 ARCH-DISC-002 is not a pending Ω proof

The later ARCH-DISC-002 route established bounded identifiability of its candidate `G_T/O_T`, but its decisive A-reconstruction question remained unresolved at the readiness stage and the subsequent governance record classifies the relevant construction as **A-EQUIVALENT**.

Therefore it cannot serve as positive evidence of Ω non-reducibility.

### 38.3 Consequence for the present review

The minimum discrimination test identified in Sections 28–37 is therefore **not** a request to rerun D1 or ARCH-DISC-002.

A future test must begin from the current Ω definition:

`Ω_T=(U,≡_T,R)`

and ask whether a component of this object remains empirically distinct **after** the strongest admissible reconstruction from:

`A=(S,T_acc)`

has been exhausted.

The candidate must therefore be selected from the Ω structure itself, rather than inherited from a previously superseded TSDI discriminator.

## 39. New discriminator-selection requirement

Before drafting any execution specification, the programme must select exactly one Ω component or relation class satisfying all of the following:

1. it is part of the frozen Ω definition;
2. it is not merely a renamed `T_acc`, `ΔT_acc`, Reach or Trajectory;
3. it is independently constructible before downstream outcome observation;
4. it has a reproducible identity/equivalence rule;
5. it admits an explicit A-reconstruction attempt;
6. it has a potential scientific consequence distinct from set membership alone.

The candidate-selection record must then classify it as:

**ADMISSIBLE CANDIDATE / A-EQUIVALENT / A-NON-EQUIVALENT / UNDERDETERMINED**

before any scientific execution is considered.

## 40. Immediate methodological consequence

The correct next activity is therefore **not execution design**.

It is:

`Ω component inventory → candidate selection → A-reconstruction preflight → only then experimental specification if necessary`

This is a materially narrower and safer route than launching another broad architectural experiment.

No execution authorization is created by this review.
