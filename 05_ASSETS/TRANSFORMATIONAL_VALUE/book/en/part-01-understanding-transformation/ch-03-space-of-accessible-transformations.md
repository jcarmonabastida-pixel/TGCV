---
content_id: TV-CH-03
language_pair_id: TV-CH-03
title: "The Space of Accessible Transformations"
language: en
content_type: chapter
status: draft
version: 0.1
created: 2026-11-26
updated: 2026-11-26
authors: []
reviewers: []
summary: "Explains how to represent the transformations a system can perform under specified conditions, and why accessibility, realisation, trajectory, outcome and value must remain distinct."
part: TV-P1
chapter: TV-CH-03
parent_id: TV-P1-OV
tags:
  - accessible-transformations
  - transformation-space
  - systems-engineering
concepts:
  - TV-TERM-001
prerequisites: []
related:
  - TV-CH-02
  - TV-CH-04
  - TV-CH-05
  - TV-CH-06
references: []
epistemic_status:
  - analytical_definition
  - bounded_empirical_evidence
  - open_hypothesis
source_assets:
  - 01_CORE/architecture/TGCV_CORE_v_current.md
  - 05_ASSETS/ARM/TGCV-EXT-ARM-001_v0.2.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_TRANSFORMATION_SPACE_DYNAMICS_FORMAL_SPEC_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_TRANSFORMATION_SPACE_DYNAMICS_ANALYSIS_001.md
  - 00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md
  - 00_GOVERNANCE/SIP/TGCV_CROSS_DOMAIN_END_TO_END_ACCESSIBILITY_OUTCOME_VALUE_MAP_001.md
license: null
---

# The Space of Accessible Transformations

## Chapter purpose

A system is not defined only by what it has done. It also matters which transformations it can perform under specified conditions, even if it has not yet performed them. This distinction makes it possible to study how a system's effective possibilities change and how those changes may relate to its subsequent trajectories.

This chapter develops an analytical representation of those possibilities. It explains how to delimit candidate transformations, what it means for a transformation to be accessible, how an accessible space can change, and what can—and cannot—be inferred from such change.

The central idea is simple but consequential: **an accessible transformation is not necessarily realised; a realised transformation does not necessarily produce a valuable outcome.**

### Learning objectives

By the end of this chapter, you should be able to:

- distinguish candidate, accessible and realised transformations;
- explain why accessibility depends on system state and relevant conditions;
- interpret the accessible transformation space as an analytical representation rather than an independent cause;
- describe changes in composition, expansion, contraction and substitution;
- separate evidence about accessibility, realisation, trajectory, outcome and value;
- recognise the limits of inferences drawn from bounded studies.

## 1. Why look at transformations a system can access?

Consider an organisation that has so far delivered a service only in person. It then introduces a digital platform, trains some of its staff, obtains permission to operate through another channel and adapts its processes. The organisation may continue serving customers in person. Yet its situation has changed: transformations that were not previously available under the same conditions may now be accessible. It may be able to serve customers remotely, coordinate distributed teams or provide certain services beyond its former operating hours.

If we observed only the activities actually performed, we could describe what the organisation had done. We would not fully capture the structural change: some transformations have become accessible.

The distinction matters across many kinds of systems. Infrastructure may enable new forms of movement; a service network may make new financial operations accessible; a software system may acquire new functions; a person may develop capabilities that expand the tasks they can perform.

In each case, two questions should be kept separate:

1. Which transformations has the system actually realised?
2. Which transformations could it realise under the conditions being considered, regardless of whether it eventually does so?

The second question is not a wish list or an unlimited catalogue of imaginable possibilities. It concerns transformations defined precisely enough for their accessibility to be assessed in relation to the system and its conditions.

Studying this space describes a dimension of change that cannot be reduced to observed activity. It also helps avoid a common error: inferring what a system could do from what it eventually did. A realised transformation may provide relevant evidence, but it does not by itself describe all the alternatives that were available.

## 2. From candidate transformations to accessible transformations

The starting point is a set of candidate transformations. We use \(\tau\) to denote a candidate: an identifiable change that could occur in the system. It must be specified clearly enough to ask what conditions would allow it to be realised.

Not every imaginable transformation belongs in the analysis. The candidate universe is delimited according to the system under study, the research question and the required level of detail. In some cases, the relevant alternatives can be enumerated. In others, it may be sufficient to define a family of transformations and an explicit procedure for identifying which ones meet the accessibility conditions.

A transformation is accessible when the relevant conditions for its realisation are satisfied. In the current analytical model, the space is represented as a function of system state and relevant conditions and constraints:

\[
T_{acc}=F(S,C,L)
\]

Here, (S) denotes the relevant state or configuration of the system; (C), the contextual conditions being considered; and (L), the constraints, resources and operational conditions that matter to the analysis. The notation does not make each element an independent entity. It expresses that accessibility is assessed in relation to a specified configuration and set of conditions.

An accessibility predicate can be defined for each candidate transformation:

\[
\tau \in T_{acc} \quad \text{if and only if} \quad P_{\tau}(S,C,L)=1
\]

The predicate must be specified independently of downstream outcomes. It would be invalid to define a transformation as accessible simply because we observe that it succeeded, or to conclude that it was available because the system eventually achieved a favourable result. That would introduce retrospective reasoning and confuse starting conditions with what happened afterwards.

Accessibility may depend on several dimensions:

- **Capability and knowledge:** the system has the skills or knowledge required.
- **Resources:** the necessary material, financial, energy or information resources are available.
- **Permission and authority:** rules and institutions permit the transformation.
- **Technical conditions:** the necessary components, interfaces and infrastructure work together.
- **Operational readiness:** the transformation can be carried out under the actual conditions of the case, not merely in theory.

These dimensions are neither a universal checklist nor an automatic formula. Their relevance depends on the transformation and the system. An option may be technically feasible but not practically accessible because authorisation, coordination, resources or time are missing. Conversely, a transformation may be available even though the system has not yet selected it.

For this reason, the accessibility criterion should be declared before examining outcomes. The analysis must explain what counts as a transformation, which conditions are necessary and how their fulfilment is determined.

## 3. The accessible transformation space

Once candidate transformations have been delimited and an accessibility criterion specified, we can represent the set—or structure—of transformations the system can perform under the conditions being considered. We call this representation the **accessible transformation space**, denoted by (T_{acc}).

The word *space* does not necessarily imply a geometric space or a collection that must be exhaustively enumerated. It refers to an analytical structure of delimited possibilities. Depending on the domain, that structure may be represented through sets, relations, functions, admissibility states or other suitable forms.

Its content depends on three methodological decisions:

1. **System boundary:** which elements and relationships belong to the unit being analysed.
2. **Candidate transformation universe:** which changes are relevant to the question.
3. **Accessibility rule:** which conditions must be satisfied for each transformation to be considered available.

These decisions must be explicit and defensible. It will not always be possible to observe every relevant condition or identify every conceivable transformation. The absence of exhaustive enumeration does not automatically invalidate the analysis, but it requires the scope and excluded transformations to be stated.

The accessible transformation space is a representation derived from system state and relevant conditions. It is not an additional force acting on the system, nor an independent ontological component. Its value lies in making analytically visible which changes are available under a particular configuration.

Nor should it be confused with a general measure of capability. A system may have many accessible transformations in one domain and be severely constrained in another. Quantity, diversity, importance and distribution are different questions. Interpreting them requires understanding what each transformation means and the context in which it can be realised.

## 4. Accessibility is not execution

Consider a system that can perform four transformations: (A), (B), (C) and (D). Their presence in its accessible space does not mean that all four will be realised. The system may choose (B), take no action, postpone a decision or follow a different trajectory at another time.

Five levels should be kept distinct:

1. **Accessibility:** which transformations are available under the specified conditions.
2. **Realisation:** which transformation actually occurs.
3. **Trajectory:** the observed sequence of realised transformations and successive states.
4. **Outcome:** a specific consequence in the domain being considered.
5. **Value:** an evaluation of that consequence against relevant criteria, actors and time horizons.

No level should be defined retrospectively from the next. The realisation of a transformation may confirm that certain conditions held in that instance, but it does not automatically reconstruct the full space of alternatives. Similarly, a favourable outcome does not by itself demonstrate that every preceding transformation was accessible or that a particular change in the accessible space caused the outcome.

The distinction also works in the opposite direction. A transformation may be accessible but not realised because there is no demand, because a decision is deliberately made not to act, because of uncertainty or opportunity costs, or because the system prioritises another trajectory. Non-realisation does not necessarily show that the transformation was inaccessible.

This separation avoids two symmetrical errors: treating every possibility as an action, and treating every observed action as if it exhausted the system's possibilities.

## 5. How an accessible space can change

The accessible transformation space need not remain constant. It can change when the system's state or any relevant condition changes. Such change can take several forms:

- **Expansion:** transformations become accessible that were not accessible before.
- **Contraction:** some transformations cease to be available.
- **Reconfiguration:** the composition of the space changes even though its total size remains the same.
- **Substitution:** some transformations cease to be accessible and others take their place.

Suppose that, at an initial point, the system has transformations (A), (B), (C) and (D) available. Later, (C) and (D) are no longer accessible, while (E) and (F) become accessible:

\[
T_{acc,t}=\{A,B,C,D\}
\]
\[
T_{acc,t+1}=\{A,B,E,F\}
\]

Both spaces contain four transformations. Looking only at their size would suggest that nothing changed. Their composition, however, is different: two transformations persist, two disappear and two new ones are added. Reconfiguration has occurred while cardinality is conserved.

This introduces an important distinction: **the number of transformations does not, by itself, describe the identity or structure of the space**. Two spaces of equal size may contain different transformations. An increase in number does not necessarily imply improvement either: the new transformations may be irrelevant, costly, harmful or less valuable to some stakeholders.

Where transformations can be identified consistently across time, it is useful to distinguish:

- added transformations;
- removed transformations;
- persistent transformations;
- the net change in the number of elements;
- the combined volume of identity substitution or turnover.

These are structural descriptions, not quality scores. The appropriate way to compare them depends on how transformation identities are defined in each domain. Different labels should not automatically be treated as different transformations, and identical labels do not guarantee semantic equivalence.

## 6. Observing transformation-space dynamics

To study change over time, we can compare the accessible space at two successive points. One useful analytical sequence is:

\[
S_t \rightarrow T_{acc,t} \rightarrow T_{real,t}
\rightarrow S_{t+1} \rightarrow T_{acc,t+1}
\]

The sequence distinguishes the initial state, the accessible transformations, the transformation actually realised, the resulting state and the accessible space under the new conditions.

The arrows organise the analysis; they should not be read as a universal causal law. In particular, the relationship between a realised transformation, the successor state and subsequent accessibility must be examined in each case. The representation helps formulate questions and test relationships, but it does not replace the evidence needed to answer them.

When transformations can be identified across time, change can be described using a small set of quantities. Let (A_t) denote the number of accessible transformations at the initial point, (G_t) the added identities, (L_t) the removed identities and (P_t) the persistent identities. The net change in size is the difference between the number of elements in the successor space and the initial space. Identity turnover, by contrast, considers additions and removals together.

There is no need to reduce all dynamics to a single indicator. Doing so may conceal important differences. A system may retain the same number of accessible transformations while undergoing substantial substitution. Another may expand its space by adding options that barely change the trajectories it can actually follow. The choice of descriptors should respond to the analytical question, data quality and domain semantics.

Cross-domain comparison requires an additional precaution. The same analytical structure may be usable in different systems without assuming that their specific transformations are equivalent. Consistency should be sought in the role played by the concepts—state, accessibility, realisation and successor state—not by imposing identical labels on different phenomena.

## 7. What bounded evidence shows—and what it does not

The available evidence illustrates different levels of support that should not be conflated.

**Operationalisation in two computational domains.** A bounded study reconstructed 36 transition records across two structurally different domains. Validation found no invalid records, and an independent mathematical audit found no discrepancies in the calculated descriptors. Both domains showed changes in the identity of accessible transformations. In one, identities were substituted without a change in the total number of transformations. This supports the bounded proposition that a common transition-level representation can operationalise changes in the space in the cases examined. It does not establish universal validity, superiority over other representations or applicability in every domain.

**Bounded causal evidence concerning subsequent trajectories.** In a study of the randomised expansion of a rural financial-services network, the intervention changed local infrastructure and structural access to certain services. The consolidated evidence provides bounded causal support for the proposition that accessibility changes can affect subsequent trajectories in that setting. The result must remain within the limits of the study: it does not establish a general law or demonstrate that accessibility change necessarily creates value.

**A case of partial identification.** In the reconstruction of an urban street-paving intervention, candidate functions—such as enabling vehicle, pedestrian or bicycle movement—could be specified in advance, and longitudinal connectivity changes could be reconstructed. However, the data did not permit independent identification of the complete accessibility predicate or the full transformation space. The case shows why an observed physical change does not automatically amount to an identified change in (T_{acc}).

**A synthetic illustration of non-equivalence.** In a controlled synthetic environment, an intervention changed the accessible space while the specified realised trajectory remained unchanged and the value outcome defined for that exercise did not change. This illustration shows that the analytical levels can vary independently under particular rules. It is not evidence about real-world behaviour and does not demonstrate that accessibility changes generally have no effect on trajectories or value.

Taken together, these results support certain bounded operations and relationships. They do not demonstrate a universal theory of transformation dynamics, establish that every accessibility change modifies a trajectory, or resolve the relationship between accessibility and value.

## 8. Limits, assumptions and open questions

Analysing the accessible transformation space depends on decisions that must be made visible.

**System boundary.** If the system boundary is inappropriate, decisive external conditions may be omitted, or capabilities that depend on other actors and infrastructure may be attributed to the system itself.

**Transformation identity.** To compare spaces over time, we need to know when a transformation persists, when it changes and when it should be treated as a different transformation. This is not always straightforward.

**Accessibility criterion.** The predicate must be independent of realisation and downstream outcomes. If it is constructed from what happened, the analysis risks becoming circular.

**Operational closure.** It is not always possible to enumerate every conceivable transformation. The analysis must state which universe was considered, why it is appropriate and what lies outside it.

**Cross-domain heterogeneity.** A common analytical structure does not mean that mechanisms, transformations or their meanings are identical across systems. Generality must be tested, not assumed.

**Relationship with trajectories.** Bounded causal evidence exists that accessibility changes can affect subsequent trajectories in one studied context. The generality of this relationship, and the conditions under which it holds, remain open questions.

**Relationship with value.** Value requires an additional evaluation: which outcomes count, for whom, against which criteria and over what time horizon. The fact that a transformation is accessible—or even realised—does not determine the value of its consequences. The causal or predictive relationship between changes in the accessible space and changes in value remains open.

These limitations do not make the concept unusable. They define the conditions under which it can be applied rigorously and identify the additional evidence that would be needed.

## 9. Synthesis and reflection

The accessible transformation space represents which transformations a system can perform under a specified state and set of conditions. It is derived from the relevant system configuration and an explicit accessibility criterion; it is neither an independent cause nor an unlimited list of imaginable possibilities.

Its composition may change through expansion, contraction, reconfiguration or substitution. For this reason, observing only the number of transformations may be insufficient: it also matters which transformations appear, which disappear and which persist.

The fundamental distinction must be maintained throughout the analysis:

**accessibility is not realisation; realisation is not trajectory; trajectory is not outcome; outcome is not automatically value.**

The available evidence provides bounded support for operationalising the space and for certain relationships with subsequent trajectories. It does not justify generalising those findings to all systems or claiming that expanding possibilities necessarily creates value.

### Reflection questions

1. Think of a system you know. Which transformations can it perform today that it could not perform a year ago? Which conditions changed?
2. How would you distinguish a technically possible transformation from one that is genuinely accessible under the system's conditions?
3. Could the accessible space change substantially without changing its total number of transformations? Construct an example.
4. What information would you need to determine whether a transformation was accessible before it was realised?
5. What errors might arise if you used observed outcomes to define accessibility retrospectively?
6. What additional evidence would be needed to claim that a change in the accessible space contributed to value creation?

### Transition to the next chapter

The accessible space depends on conditions, resources, relationships and constraints. The next chapter examines these elements in greater detail and shows how they interact to enable or limit a system's transformations.

## References and further reading

Full bibliographic references for the empirical studies described and the supporting conceptual work will be added after their primary records and relevance have been verified. This is a working draft, not a publication-approved version.
