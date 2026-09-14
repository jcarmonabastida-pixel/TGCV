# TGCV C09 — D5.2 Representation Correction 001

**Date:** 2026-09-14
**Status:** ADOPTED — PROSPECTIVE METHODOLOGICAL CORRECTION
**Scope:** C09 D5.2 and future candidate re-evaluation

## 1. Trigger

The C09 candidate screens exposed a methodological risk: requiring `Delta T_acc` to exist as a native dataset variable can systematically reject the TGCV analytical object for reasons unrelated to the scientific question.

`Delta T_acc` is an analytical construct of TGCV. Real-world datasets were generally not designed around TGCV terminology and therefore need not contain a field called `T_acc`, `Delta T_acc`, accessibility-space, or an equivalent mediator.

The absence of such a native field is therefore **not itself evidence against TGCV**.

## 2. Corrected D5.2 representation rule

D5.2 must distinguish:

1. **representation:** whether `T_acc,0`, `T_acc,1` and `Delta T_acc` can be reconstructed from observed structural states; and
2. **causal identification:** whether the contribution of that reconstructed `Delta T_acc` to `Y` can be identified or meaningfully bounded.

The admissible representation is:

`observed structural states -> explicit T_acc representation -> Delta T_acc`

A candidate passes the representation component when the reconstruction is:

- defined independently of the downstream outcome;
- based on structural accessibility/capability rather than realized behaviour or adoption;
- reproducible from public data;
- auditable at unit/time level;
- theoretically defensible under the TGCV definition of accessible transformations.

A native accessibility variable is sufficient but **not necessary**.

## 3. Corrected causal question

D5.2 asks:

> Can the causal contribution of a reproducibly reconstructed `Delta T_acc` to the downstream trajectory/outcome be identified or bounded within the multicausal system?

It does **not** ask whether the dataset already contains a variable explicitly named `Delta T_acc`.

A simple regression of `Y` on reconstructed `Delta T_acc` remains insufficient. The candidate must still satisfy a defensible causal architecture: independent randomization, factorial/separate randomization, valid IV/encouragement, controlled/interventional mediation, principal-stratum identification, measured path-specific identification, or informative partial-identification bounds.

## 4. Relation to mediation methodology

This correction is consistent with established causal-mediation methodology: causal contributions can be defined through manipulated or interventional mediator distributions rather than requiring the mediator to have been conceived as a TGCV variable in the original study. Interventional direct/indirect effects can be identified under explicit assumptions, including randomized exposure and appropriate mediator-outcome/confounding conditions. Multiple mediators and longitudinal mediators can likewise be handled under explicit identification frameworks. See: causal mediation with multiple mediators and interventional effects, and mediation with time-varying exposures/mediators. citeturn0search0turn0search1turn0search5

## 5. Consequence for prior candidates

No prior candidate result is rewritten automatically.

Indian Rural Roads remains **D5-C diagnostic only** under the evidence already assessed. It may be retrospectively re-evaluated if the existing public data can reconstruct `T_acc,0/T_acc,1` and `Delta T_acc` under this rule and the existing design supplies a valid D5-A/D5-B contribution architecture.

The same retrospective check applies to the previously strongest candidates before initiating a broad new search.

## 6. Strategic implication

C09 is not a search for a pre-existing dataset that happens to contain a variable matching TGCV vocabulary.

It is a search for real-world empirical architectures in which:

`S_t -> T_acc,t`

can be reconstructed,

`(S_t,C_t) -> (S_{t+1},C_{t+1})`

can be observed or identified,

`Delta T_acc`

can be constructed reproducibly, and its downstream causal contribution can be identified/bounded despite concurrent mechanisms.

This is a materially better match to TGCV's ontological status as an analytical framework.

## 7. Governance effect

This document is a methodological correction to the interpretation of D5.2. It does not upgrade C09, TGCV Core, RMA, Evidence→Claim Matrix or STATUS. Those updates require completion of the applicable scientific gates.

The next operation is retrospective re-evaluation of the strongest candidates under this corrected representation rule, without repeating experiments.
