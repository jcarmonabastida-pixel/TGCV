# C09 — Conversation Record: D5.2 Representation Correction

**Date:** 2026-09-14
**Status:** RECORDED — CANONICAL CONTINUITY NOTE

## Context

During the C09 Indian Rural Roads candidate evaluation, D5.2 was initially interpreted as requiring isolation of the causal contribution of `Delta T_acc` while treating accessibility as if it should already exist as an observed dataset variable.

The discussion identified a conceptual problem: `Delta T_acc` is a TGCV analytical construct. Existing real-world datasets were not designed around TGCV and therefore should not be expected to contain a native variable with that name or ontology.

## Key methodological conclusion

The absence of a native `Delta T_acc` field is not evidence against TGCV and must not itself cause a D5.2 failure.

The correct empirical target is:

`observed structural states -> explicit representation of T_acc -> Delta T_acc -> causal contribution to Y`

The representation and causal-identification questions must be separated.

### Representation requirement

A candidate can satisfy the representation component if `T_acc,0`, `T_acc,1` and `Delta T_acc` can be reconstructed reproducibly from observed structural states, provided that the reconstruction:

- is defined independently of downstream outcome/behaviour;
- represents structural accessibility/capability;
- is reproducible from public data;
- is auditable at unit/time level;
- is theoretically defensible under TGCV.

### Causal requirement

Reconstruction alone does not establish causality. D5.2 still requires a defensible causal contribution architecture, such as independent/factorial randomization, valid IV/encouragement, controlled/interventional mediation, principal-stratum identification, path-specific identification under stated assumptions, or informative partial-identification bounds.

## Consequence for Indian Rural Roads

The candidate remains D5-C under the evidence already assessed. No prior result is automatically rewritten. However, the candidate may be retrospectively re-evaluated under the corrected rule using only existing public evidence and without rerunning experiments.

## Strategic consequence for C09

C09 is not a search for datasets that already contain TGCV terminology. It is a search for empirical architectures from which TGCV's analytical object can be reconstructed and whose causal contribution can then be identified or bounded in a multicausal system.

## Governance action

The correction was recorded in:

`00_GOVERNANCE/SIP/TGCV_C09_D5_2_REPRESENTATION_CORRECTION_001.md`

The C09 Dataset-First Discovery Protocol 005 is to be amended correspondingly. No automatic Core/RMA/Evidence Matrix/STATUS upgrade is authorized.

## Next operation

Retrospectively re-evaluate the strongest previously screened C09 candidates under the corrected D5.2 representation rule, prioritizing KGFS Rural Banking, El Salvador Rural Electrification and Peru Domestic Internet, and optionally checking Indian Rural Roads because its public data may support reconstructable `T_acc`.
