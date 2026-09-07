# TGCV SLR-1 — Evidence Bank Schema v0.1

**Status:** RECONSTRUCTED / WORKING
**Purpose:** normative schema for recording source-grounded evidence independently from normalized facts and interpretation.

## Evidence record

Each evidence item receives a unique `evidence_id` and contains:

1. `evidence_id`
2. `source_id`
3. `evidence_type` — definition / formalism / empirical finding / architectural statement / relation / limitation / other.
4. `location` — page, section, table, figure or stable document location.
5. `source_text` — short quotation where necessary and permitted, otherwise faithful paraphrase.
6. `context` — minimal surrounding context needed to interpret the evidence.
7. `claim_supported` — the precise factual proposition supported.
8. `directness` — explicit / strongly implied / weakly implied.
9. `scope` — construct / structure / architecture / application.
10. `tgcv_component_candidate` — S / T_acc / ΔT_acc / ΔReach / ΔTrajectory / Outcome / Value / mechanism / none.
11. `counterevidence_or_qualification` — limitations or conditions stated by the source.
12. `retrieval_metadata` — database/query/chaining provenance.
13. `integrity_metadata` — optional local snapshot/hash.

## Evidence discipline

- One evidence record should support one principal factual proposition whenever practical.
- Evidence must remain attributable to the source.
- Interpretation must not be inserted into `source_text` or `claim_supported`.
- If evidence is ambiguous, ambiguity must be recorded rather than resolved silently.
- Evidence that only supports terminology similarity must be explicitly marked as such.
- Evidence used to support AC2/AC3 absorption must identify the exact architectural relation being supported.

## Required distinction

`Evidence ≠ Fact ≠ Interpretation`

Evidence is what is located in the source. A Fact Bank entry normalizes one or more evidence items. An absorption decision is a subsequent analytical judgement.
