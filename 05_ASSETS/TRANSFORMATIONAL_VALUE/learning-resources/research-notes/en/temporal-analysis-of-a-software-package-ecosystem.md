---
content_id: TV-LR-002
language_pair_id: TV-LR-002
title: "Temporal analysis of a software-package ecosystem"
language: en
content_type: research_note
status: draft
version: 0.1
created: 2026-11-26
updated: 2026-11-26
authors: []
reviewers: []
summary: "A bounded empirical analysis of changes in accessible transformation space and one-step potential reach, using temporal pairs of software package versions."
concepts:
  - accessible-transformation-space
references:
  - TV-REF-006
related:
  - TV-CH-03
epistemic_status:
  - bounded_structural_empirical_evidence
---

# Temporal analysis of a software-package ecosystem

## Question and scope

Do structurally accessible transformations change over time in a software-package ecosystem? And when they do, does that change necessarily coincide with a change in the set of potential successor states?

The analysis examined 516,061 adjacent temporal package-version pairs constructed from a historical dataset of the Rust ecosystem, with a reference date of 7 September 2022. The comparison was limited to a one-step horizon and to the structural operationalisation frozen for the study.

The unit of analysis is the temporal version pair and its associated dependency structure. It should not be interpreted as a direct observation of software execution, successful compilation or the actual use of a capability.

## Structural findings

Across the 516,061 pairs examined:

| Classification | Pairs |
|---|---:|
| Persistence | 77,858 |
| Expansion | 8,295 |
| Contraction | 3,786 |
| Reconfiguration | 426,122 |
| Total | 516,061 |

Overall, 438,203 pairs (approximately 84.91%) were non-persistent. Reconfiguration was the predominant category. Observing only the size of the space therefore does not adequately describe the stability of its composition.

## Distinguishing accessible space from potential reach

The analysis distinguished changes in the accessible transformation space from changes in one-step potential reach:

- In 159,921 pairs, the accessible space changed but one-step potential reach did not.
- In 278,282 pairs, both the accessible space and potential reach changed.
- In 266,201 pairs, potential reach retained the same cardinality but changed membership.

The first two groups sum to the 438,203 non-persistent pairs. The third finding shows that equal cardinality does not imply equal composition.

These results support a bounded empirical distinction between changes in accessible space and changes in the potential set of successor states. They are not interchangeable measures of the same object.

## Integrity and reproducibility

The primary execution and its mandatory replay produced identical structured results across all compared fields. The reproducibility statement is limited to this structured-result agreement; no byte-level comparison of two independent raw JSON files is claimed.

The local archive used was checked against the published Figshare file by filename, file size and MD5. The dataset record identifies the published item as *Full dataset* and declares a CC0 licence. This correspondence supports the identification of the source used. It does not replace a description of the operationalisation, nor does it make the derived analysis universally valid by itself.

## Interpretation and limits

Within the frozen representation and one-step horizon, the evidence supports the following bounded statements:

1. the composition of the accessible transformation space can change substantially between adjacent versions;
2. accessible-space change can occur without a change in one-step potential reach, and vice versa;
3. the cardinality of potential reach is insufficient to describe the identity of its members;
4. agreement between the primary execution and its mandatory replay provides a consistency check on the structured results.

The evidence does not establish:

- effective runtime reachability;
- successful execution of the transformations;
- trajectory sufficiency at horizons greater than one step;
- causality between accessible-space changes and downstream outcomes;
- predictive capacity or superiority over other representations;
- package adoption, package success, economic impact or Value creation;
- universal validity beyond the operationalisation and dataset examined.

One-step potential reach is a structural construct of possible successors under the specified representation. It is not equivalent to states observed during actual software execution.

## Relationship to governance of other uses of the dataset

This note documents a closed, bounded empirical result from the temporal analysis described above. It does not present a distinct operationalisation derived from the same dataset as admitted, nor does it authorise the processing, publication or reuse of other derived artefacts. Any further scientific use of those objects remains subject to its own governance and review process.

This separation does not alter the status of the result documented here and does not imply causality or Value creation.

## Data source and reference

The historical dataset used corresponds to the *Full dataset* item published on Figshare:

https://springernature.figshare.com/articles/dataset/Full_dataset/21345990

The licence declared for that item is CC0. Describing the source does not imply that all derived artefacts, subsequent analyses or software products automatically carry the same licence.

**Editorial status:** research-note draft pending scientific, bibliographic and editorial review.
