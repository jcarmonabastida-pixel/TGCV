---
content_id: TV-CH-03
language_pair_id: TV-CH-03
title: "The Space of Accessible Transformations"
language: en
content_type: chapter
status: draft
version: 0.8
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
  - TV-LR-001
  - TV-LR-002
references:
  - TV-REF-001
  - TV-REF-002
  - TV-REF-003
  - TV-REF-006
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
  - 00_GOVERNANCE/rma/TGCV_RMA_v3.38.md
  - 00_GOVERNANCE/SIP/TGCV_C09_CLAIM_LEVEL_CONSOLIDATION_RECORD_001.md
  - 00_GOVERNANCE/SIP/C10C002_BOUNDED_CAUSAL_EXPERIMENT_CLOSURE_001.md
  - 00_GOVERNANCE/SIP/TGCV_MT5_DYNAMIC_TRANSFORMATION_SPACE_RECONSTRUCTION_RESULT_001.md
  - 03_EXPERIMENTS/EXT-1.1_Rust/execution/RUST-DYN-2_SCIENTIFIC_INTEGRATION_CLOSURE_v01.md
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

Consider an organisation that has so far delivered a service only in person. It then introduces a digital platform, trains some of its staff, obtains permission to operate through another channel and adapts its processes. The organisation may continue serving customers in person. Yet its situation has changed: transformations that were not previously available under the same conditions may now be accessible. It may be able to serve customers remotely, coordinate distributed teams or provide certain services beyond its former operating hours. Whether each of these transformations is genuinely accessible depends on whether the specific conditions required for its realisation are satisfied. Having a platform or permission is not enough if the necessary capabilities, resources or operational integration are missing.

If we observed only the activities actually performed, we could describe what the organisation had done. We would not fully capture the structural change: some transformations have become accessible.

The distinction matters across many kinds of systems. Infrastructure may enable new forms of movement; a service network may make new financial operations accessible; a software system may acquire new functions; a person may develop capabilities that expand the tasks they can perform.

In each case, two questions should be kept separate:

1. Which transformations has the system actually realised?
2. Which transformations are available for the system to realise under the conditions being considered, regardless of whether they are eventually realised?

The second question is not a wish list or an unlimited catalogue of imaginable possibilities. It concerns transformations defined precisely enough for their accessibility to be assessed in relation to the system and its conditions.

Studying this space describes a dimension of change that cannot be reduced to observed activity. It also helps avoid a common error: inferring what a system could do from what it eventually did. A realised transformation may provide relevant evidence, but it does not by itself describe all the alternatives that were available.

## 2. From candidate transformations to accessible transformations

The starting point is a set of candidate transformations. We use \(\tau\) to denote a candidate: an identifiable change that could occur in the system. It must be specified clearly enough to ask what conditions would allow it to be realised.

Not every imaginable transformation belongs in the analysis. The candidate universe is delimited according to the system under study, the research question and the required level of detail. In some cases, the relevant alternatives can be enumerated. In others, it may be sufficient to define a family of transformations and an explicit procedure for identifying which ones meet the accessibility conditions.

A transformation is accessible when the relevant conditions for its realisation are satisfied. In the current analytical model, the space is represented as a function of system state and relevant conditions and constraints:

\[
T_{acc}=F(S,C,L)
\]

Here, \(S\) denotes the relevant state or configuration of the system; \(C\), the contextual conditions being considered; and \(L\), the constraints, resources and operational conditions that matter to the analysis. The notation does not make each element an independent entity. It expresses that accessibility is assessed in relation to a specified configuration and set of conditions.

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

Once candidate transformations have been delimited and an accessibility criterion specified, we can represent the set—or structure—of transformations the system can perform under the conditions being considered. We call this representation the **accessible transformation space**, denoted by \(T_{acc}\).

The word *space* does not necessarily imply a geometric space or a collection that must be exhaustively enumerated. It refers to an analytical structure of delimited possibilities. Depending on the domain, that structure may be represented through sets, relations, functions, admissibility states or other suitable forms.

Its content depends on three methodological decisions:

1. **System boundary:** which elements and relationships belong to the unit being analysed.
2. **Candidate transformation universe:** which changes are relevant to the question.
3. **Accessibility rule:** which conditions must be satisfied for each transformation to be considered available.

These decisions must be explicit and defensible. It will not always be possible to observe every relevant condition or identify every conceivable transformation. The absence of exhaustive enumeration does not automatically invalidate the analysis, but it requires the scope and excluded transformations to be stated.

The accessible transformation space is a representation derived from system state and relevant conditions. It is not an additional force acting on the system, nor an independent ontological component. Its value lies in making analytically visible which changes are available under a particular configuration.

Nor should it be confused with a general measure of capability. A system may have many accessible transformations in one domain and be severely constrained in another. Quantity, diversity, importance and distribution are different questions. Interpreting them requires understanding what each transformation means and the context in which it can be realised.

## 4. Accessibility is not execution

Consider a system that can perform four transformations: \(A\), \(B\), \(C\) and \(D\). Their presence in its accessible space does not mean that all four will be realised. The system may choose (B), take no action, postpone a decision or follow a different trajectory at another time.

Five levels should be kept distinct:

1. **Accessibility:** which transformations are available under the specified conditions.
2. **Realisation:** which transformation actually occurs.
3. **Trajectory:** the observed sequence of realised transformations and successive states.
4. **Outcome:** a specific consequence in the domain being considered.
5. **Value:** an evaluation of that consequence against relevant criteria, actors and time horizons.

No level should be defined retrospectively from the next. The realisation of a transformation may confirm that certain conditions held in that instance, but it does not automatically reconstruct the full space of alternatives. Similarly, a favourable outcome does not by itself demonstrate that every preceding transformation was accessible or that a particular change in the accessible space caused the outcome.

The distinction also works in the opposite direction. A transformation may be accessible but not realised because there is no demand, because a decision is deliberately made not to act, because of uncertainty or opportunity costs, or because the system prioritises another trajectory. Non-realisation does not necessarily show that the transformation was inaccessible.

In some domains, it is also necessary to distinguish the **adoption or use** of a service or capability from its structural availability. The fact that infrastructure or a service is available does not mean that people or organisations will use it. Observed use may be relevant to the analysis of a trajectory or outcome, but it should not automatically be used to define which transformations were accessible.

This separation avoids two symmetrical errors: treating every possibility as an action, and treating every observed action as if it exhausted the system's possibilities.

## 5. How an accessible space can change

The accessible transformation space need not remain constant. It can change when the system's state or any relevant condition changes. Such change can take several forms:

- **Expansion:** transformations become accessible that were not accessible before.
- **Contraction:** some transformations cease to be available.
- **Reconfiguration:** the composition of the space changes even though its total size remains the same.
- **Substitution:** some transformations cease to be accessible and others take their place.

The term **latent possibilities** is sometimes used for transformations that are already accessible but have not yet been realised. It should be used carefully: it does not refer to a mysterious capability or a merely imaginable possibility. It is meaningful only where the accessibility conditions can be justified independently. A transformation that becomes accessible for the first time may be described as newly enabled; one that no longer meets the relevant conditions ceases to belong to the accessible space.

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

The sequence distinguishes the initial state, the accessible transformations, the transformation actually realised, the resulting state and the accessible space under the new conditions. The arrows organise the analysis; they should not be read as a universal causal law. The relationship between a realised transformation, the successor state and subsequent accessibility must be examined in each case.

Where transformations can be identified consistently across two points in time, change can be described using several indicators:

\[
\begin{aligned}
A_t &= |T_{acc,t}| \\
A_{t+1} &= |T_{acc,t+1}| \\
G_t &= |T_{acc,t+1} \setminus T_{acc,t}| \\
L_t &= |T_{acc,t} \setminus T_{acc,t+1}| \\
P_t &= |T_{acc,t} \cap T_{acc,t+1}| \\
R_t &= G_t + L_t \\
D_t &= A_{t+1}-A_t = G_t-L_t
\end{aligned}
\]

Here, \(A_t\) and \(A_{t+1}\) are the initial and successor cardinalities; \(G_t\) counts added identities; \(L_t\), removed identities; \(P_t\), persistent identities; \(R_t\), total identity turnover; and \(D_t\), the net change in cardinality. These quantities describe different aspects of change: net change alone does not reveal how many identities have been replaced, while turnover does not indicate whether the space has increased or decreased overall.

There is no need to reduce all dynamics to a single indicator. A system may retain the same number of transformations while undergoing substantial substitution. Another may expand its space by adding options that barely alter the trajectories it can actually follow. The choice of descriptors should respond to the analytical question, data quality and domain semantics. None of these descriptors is, by itself, a score of quality, capability or value.

Some analyses also examine **potential one-step reach**: the set of structurally possible successor states under a specified representation. This construct is not equivalent to observed execution or effective runtime reachability. Available evidence shows that changes in the accessible space and changes in this potential reach can be distinguished; they should therefore not be treated as the same quantity.

Cross-domain comparison requires an additional precaution. The same analytical structure may be usable in different systems without assuming that their specific transformations are equivalent. Consistency should be sought in the role played by the concepts—state, accessibility, realisation and successor state—not by imposing identical labels on different phenomena.

## 7. What bounded evidence shows—and what it does not

The available evidence comes from distinct studies and analyses. It is not one combined test, and their sample sizes or scopes cannot be pooled. Each result addresses a different question.

**A common representation across two computational domains.** A bounded study reconstructed 36 transitions across two structurally different domains. Validation found no invalid records, and an independent mathematical audit found no discrepancies in the calculated descriptors. Both domains showed changes in the identity of accessible transformations. In the probabilistic coordination model, identities changed without a change in cardinality; the grid-planning domain also showed identity turnover and some net reductions. The domain-specific audit of the latter found that its changes could be fully reconstructed from the native state-and-action model: distinct representational gain was not demonstrated. Taken together, the result supports the possibility of operationalising a common transition structure in these two cases, not its superiority or universal validity.

**Temporal evidence from a software-package ecosystem.** An analysis of 516,061 adjacent temporal package-version pairs, constructed from a historical Rust dataset, examined changes in the accessible transformation space under a one-step operationalisation. It identified 438,203 non-persistent pairs (approximately 84.91%): 77,858 persistence cases, 8,295 expansions, 3,786 contractions and 426,122 reconfigurations. The comparison also distinguished changes in the accessible space from changes in one-step potential reach (\(Reach^{1}_{pot}\)): the accessible space changed without a change in one-step potential reach in 159,921 pairs; both changed in 278,282 pairs. In a further 266,201 pairs, potential reach had the same cardinality but different membership. The primary execution and its mandatory replay produced identical structured results. Within this frozen representation and one-step horizon, the analysis supports the empirical distinction between changes in the accessible space and changes in potential successor reach, and shows that cardinality alone does not describe composition. It does not establish runtime reachability, trajectory sufficiency at longer horizons, causality, predictive capacity, effects on outcomes or Value, or universal validity. The [companion research note](../../../learning-resources/research-notes/en/temporal-analysis-of-a-software-package-ecosystem.md) documents the operationalisation, provenance and limits of the result.

**Bounded causal evidence concerning subsequent trajectories.** An experimental evaluation of rural financial-services expansion in southern India used randomised branch openings to change local infrastructure for access to formal financial services. TGCV's consolidated evidence interprets this structural intervention as an expansion of accessibility and finds bounded causal support that it affected subsequent household trajectories in the setting studied. The interpretation keeps structural access separate from later use of financial products and from observed changes in employment, economic activity and income. This is evidence for a bounded relationship in a specific setting; it does not establish that every accessibility change produces a trajectory change, or that accessibility is its only cause.

**A non-detectable causal result in urban infrastructure.** A second TGCV analysis used the replication data from an experiment involving infrastructure investment in urban neighbourhoods in Mexico. On the basis of a bounded structural feasibility operationalisation—six infrastructure dimensions and twelve elementary opening or closure families—it estimated the effect of treatment assignment on the net cardinality change of that set, not on a complete reconstruction of the accessible transformation space. The estimate was not statistically detectable: the effect was approximately \(-0.031\) (clustered standard error: 0.165; p-value: 0.849), and the 95% confidence interval included both negative and positive effects. Wild-cluster-bootstrap inference also did not detect an effect. This does not show that the true effect is exactly zero or refute the general proposition. Possible interference between units remains unresolved, and minimal structural feasibility is not a complete mechanistic identification of the accessibility predicate. This TGCV analysis has its own estimand and must not be confused with the original authors' published results on infrastructure access, housing investment or property values.

**A case of partial identification in street paving.** In the experimental study of residential street paving in Acayucan, Mexico, candidate functions—such as enabling vehicle, pedestrian and bicycle movement—could be specified in advance, and longitudinal changes in connectivity could be reconstructed. However, the data did not permit independent identification of the complete accessibility predicate or reconstruction of the full accessible transformation space. The case shows why a physical intervention and an observed change in connectivity do not automatically amount to an identified change in \(T_{acc}\).

**A synthetic illustration of non-equivalence.** In a controlled synthetic environment, an intervention changed the accessible space while the specified realised trajectory remained unchanged and the value outcome defined for that exercise did not change. This illustration shows that the analytical levels can vary independently under particular rules. It is not evidence about real-world behaviour and does not demonstrate that accessibility changes generally have no effect on trajectories or value.

Taken together, these results support bounded operations and relationships: representing changes in identity, distinguishing accessibility from potential reach, and a bounded causal relationship with subsequent trajectories in one real-world setting. They also show limits of identification and non-detectable results. They do not demonstrate a universal theory of transformation dynamics or resolve the relationship between accessibility and value.

## 8. Limits, assumptions and open questions

Analysing the accessible transformation space depends on decisions that must be made visible.

**System boundary and candidate universe.** If the system boundary is inappropriate, decisive external conditions may be omitted, or capabilities that depend on other actors and infrastructure may be attributed to the system itself. The candidate transformation universe must be delimited in a way that is defensible for the question being studied. It will not always be possible to enumerate every conceivable transformation; the analysis must explain what is included, what is excluded and why the operational closure is sufficient for its stated purpose.

**Transformation identity and equivalence.** To compare spaces over time, we need to know when a transformation persists, when it changes and when it should be treated as different. Across domains, labels cannot be equated automatically: a common analytical structure does not imply semantic identity between transformations.

**Accessibility criterion.** The predicate must be defined independently of realisation and downstream outcomes. If it is constructed from what happened, the analysis risks becoming circular. Structural availability must also be distinguished from adoption or actual use.

**Interference and external dependence.** A transformation may depend on other systems, actors, networks or infrastructure. An intervention assigned to one unit may affect other units or depend on shared conditions. If these dependencies are unobserved or cannot be ruled out, they limit causal interpretation and must be stated.

**Measurement and scalarisation.** Cardinality is only one descriptor. It can conceal substitution, changes in identity and semantic differences. Reducing the space to one number may be useful for a specific estimand, but it is not equivalent to measuring its full structure. Results based on a scalar operationalisation must be interpreted within that boundary.

**Cross-domain heterogeneity.** A common analytical structure does not mean that mechanisms, transformations or their meanings are identical across systems. Generality must be tested, not assumed.

**Relationship with trajectories.** Bounded causal evidence exists that a structural expansion of accessibility affected subsequent trajectories in one studied setting. Other analyses provide structural or methodological evidence, but do not all identify a causal relationship. The generality of the relationship, and the conditions under which it holds, remain open questions.

**Relationship with value.** Value requires an additional evaluation: which outcomes count, for whom, against which criteria and over what time horizon. The fact that a transformation is accessible—or even realised—does not determine the value of its consequences. The causal or predictive relationship between changes in the accessible space and changes in value remains open.

These limitations do not make the concept unusable. They define the conditions under which it can be applied rigorously and identify the additional evidence that would be needed.

## 9. Synthesis and reflection

The accessible transformation space represents which transformations a system can perform under a specified state and set of conditions. It is derived from the relevant system configuration and an explicit accessibility criterion; it is neither an independent cause nor an unlimited list of imaginable possibilities.

Its composition may change through expansion, contraction, reconfiguration or substitution. For this reason, observing only the number of transformations may be insufficient: it also matters which transformations appear, which disappear and which persist. Nor should accessible-space dynamics be confused with changes in the potential reach of successor states or with observed execution.

The available evidence provides bounded methodological support for representing these changes and bounded causal support for a relationship with subsequent trajectories in one real-world setting. The temporal software-package analysis also shows that changes in accessible space and one-step potential reach are empirically distinguishable under the operationalisation examined. The evidence also includes non-detectable results and cases where accessibility can only be partially identified. These differences matter: not all evidence answers the same question or permits the same conclusion.

The fundamental distinction must be maintained throughout the analysis:

**accessibility is not realisation; realisation is not trajectory; trajectory is not outcome; outcome is not automatically value.**

The relationship between changes in the accessible space and value creation remains open and requires further evidence and evaluation.

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

- Field, E., & Pande, R. *Evaluating the economic impacts of rural banking: experimental evidence from southern India*. 3ie Impact Evaluation Report 85. https://doi.org/10.23846/OW3IE85
- McIntosh, C., Alegría, T., Ordóñez, G., & Zenteno, R. (2018). The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico. *American Economic Journal: Applied Economics, 10*(3), 263–286. https://doi.org/10.1257/app.20160429
- Gonzalez-Navarro, M., & Quintana-Domeque, C. (2016). Paving Streets for the Poor: Experimental Analysis of Infrastructure Effects. *The Review of Economics and Statistics, 98*(2), 254–267. https://doi.org/10.1162/REST_a_00553. Replication data: https://doi.org/10.7910/DVN/6TC8RO
- Figshare. *Full dataset* [historical Rust software-package ecosystem dataset]. https://springernature.figshare.com/articles/dataset/Full_dataset/21345990. Declared licence: CC0.

The TGCV computational analyses cited in this chapter are documented through companion research notes describing their sources, methods, results and limits. These notes are project research documentation and should not be confused with independent external publications.
