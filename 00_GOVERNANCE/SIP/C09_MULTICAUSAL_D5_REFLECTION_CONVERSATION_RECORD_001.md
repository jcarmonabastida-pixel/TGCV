# TGCV C09 — Multicausal D5 Reflection / Methodological Correction Record 001

**Date:** 2026-09-14
**Status:** RECORDED — METHODOLOGICAL CORRECTION AUTHORIZED
**Scope:** C09 real-world candidate discovery / D5 interpretation only

## 1. Trigger

After the sequential screening of multiple real-world candidates, including El Salvador rural electrification, Peru domestic Internet, KGFS rural banking, and other factorial or infrastructure cases, the repeated D5-C / diagnostic-only outcome exposed a potentially over-restrictive interpretation of the mechanism-identification gate.

The recurring assumption was effectively that the accessibility component `T_acc` had to constitute the uniquely isolable causal bridge from intervention to outcome. That is not a realistic requirement for ordinary real-world systems, where outcomes/value normally depend on multiple simultaneous determinants, mechanisms, parameters and interactions.

## 2. Methodological reflection

A realistic causal structure is multicausal:

`Y = f(T_acc, X1, X2, ..., Xk, interactions, epsilon)`

The existence of other causal determinants does not imply that the causal contribution of `T_acc` is unidentifiable.

The scientifically relevant question for TGCV C09 should therefore be:

> Can the causal contribution of a change in `T_acc` to a downstream trajectory/outcome be identified, bounded or otherwise defensibly characterized while explicitly accounting for other relevant causal mechanisms?

This is different from requiring:

`Z -> T_acc -> Y`

to be the only causal path.

## 3. Revised interpretation

TGCV does not need to impose a monocausal ontology on a real system.

The relevant causal structure may contain:

`Z -> T_acc -> Y`

alongside:

`Z -> X1 -> Y`
`Z -> X2 -> Y`
`X3 -> Y`
`T_acc <-> other system mechanisms`

The C09 question is whether the **incremental causal contribution associated with the structural transformation-space change** can be identified or bounded within that multicausal system.

## 4. Consequence for D5

D5 should therefore become a **Causal Contribution / Mechanism Identification Gate** rather than a requirement that `T_acc` be the exclusive causal bridge.

Proposed classification:

- **D5-A — IDENTIFIED CONTRIBUTION:** causal contribution of `Delta T_acc` identified under a defensible estimand/design/assumption set while relevant competing mechanisms are addressed.
- **D5-B — BOUNDED / ASSUMPTION-EXPLICIT:** contribution not point-identified but meaningfully bounded or identified within a clearly defined interventional/principal-stratum estimand.
- **D5-C — DIAGNOSTIC ONLY:** first-stage and mediator evidence exist but the causal contribution remains unresolved.
- **D5-D — TOTAL EFFECT ONLY:** only `Z -> Y` (possibly plus `Z -> Delta T_acc`) is established, without a defensible contribution estimand.

The presence of other causal pathways is therefore not itself a D5 failure. The failure is inability to distinguish, identify or bound the contribution of `Delta T_acc` from those pathways.

## 5. Relation to causal-methodology literature

Modern causal mediation methodology explicitly distinguishes total, direct, indirect and path-specific/interventional effects in settings with multiple mediators and concurrent pathways. The literature also emphasizes that definition, identification and estimation are separate tasks and that multiple pathways can be analysed without requiring a single mediator to explain the total effect.

Relevant methodological references include:

- Zhou, X. (2022), *Semiparametric Estimation for Causal Mediation Analysis with Multiple Causally Ordered Mediators*, JRSS B, DOI: 10.1111/rssb.12487.
- Daniel, R.M. et al. / multiple-mediator causal mediation literature, including path-specific and interventional effects.
- *Causal Mediation Analysis with Multiple Mediators*, Biometrics 71(1), 2015, DOI: 10.1111/biom.12248.
- Recent methodological work on multiple mediators and interventional effects reinforces the distinction between total effects and mediator-specific contributions.

These references support the methodological plausibility of the revised D5 framing; they do not constitute TGCV evidence.

## 6. TGCV implication

The correction may be more consequential than simply relaxing a gate.

A practical value-construction theory should be applicable to systems where value/outcomes arise from interacting mechanisms rather than from a single causal driver. TGCV can therefore seek to represent:

`Delta T_acc -> Delta Pi -> Delta V`

as one causally identifiable contribution within a multicausal system, rather than claiming that `Delta T_acc` is the sole determinant of `Y` or `V`.

This strengthens the potential industrial applicability of TGCV while remaining scientifically falsifiable: the contribution must still be identified, bounded or rejected under an explicit estimand.

## 7. Candidate re-evaluation authorization

The following already-screened strong candidates may be **re-read under the revised D5 estimand without repeating their experiments**:

1. El Salvador Rural Electrification — prior D5-C.
2. Peru Domestic Internet — prior D5-C.
3. KGFS Rural Banking, Tamil Nadu — prior D5-C.

Historical results remain immutable. The re-evaluation is methodological reinterpretation / estimand analysis only.

Candidates rejected earlier for D6-E/D6, D1/D2 or other hard gates are not reopened by this record.

## 8. Governance constraint

This record does not itself upgrade C09, TGCV Core, RMA, Evidence Matrix or STATUS.

The methodological correction is to be frozen in a new C09 Dataset-First Discovery Protocol revision, preserving Protocols 002–004 as historical frozen artifacts.
