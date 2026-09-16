# TGCV — TRANSVERSAL METHODOLOGY CANDIDATE EXTRACTION 001

**Status:** CURRENT_INDEPENDENT_ANALYSIS  
**Date:** 2026-09-17  
**Scope:** Extraction of a candidate transversal methodology from already closed TGCV evidence.  
**Governance status:** Independent analytical synthesis; not normative methodology.  

## 1. Purpose

This artifact extracts a candidate methodological chain from evidence already audited and closed across SWIM, C09/KGFS, C10C-002 and IT-G1. It does not modify TGCV Core, RMA, Evidence-to-Claim Matrix, STATUS, or any scientific claim status.

The extraction is deliberately conservative. Domain-specific variables, observed outcomes, treatment effects, and terminology are not relabeled as TGCV constructs unless the underlying operation is independently supported.

## 2. Frozen evidence basis

The analysis relies on the already closed evidence available in the TGCV programme, including:

- SWIM Uτ/Pτ formalization and bounded T_acc reconstruction;
- SWIM bounded trajectory-linkage reconstruction;
- C09 operational architecture and KGFS exact local-variable audit (74/74 files);
- C10C-002 bounded structural T_acc reconstruction and negative bounded causal result;
- IT-G1 independent ex-ante accessibility/admissibility closure and its separate, inconclusive utility analysis.

The KGFS variable audit is treated as a technical reproducibility/audit layer. Its trajectory-variable matches are not themselves treated as a TGCV trajectory definition.

## 3. Candidate methodological chain

```text
S / relevant conditions
        ↓
Uτ — candidate transformation universe
        ↓
Pτ — ex-ante admissibility predicate
        ↓
T_acc — accessible transformations
        ↓
T_acc,0 / T_acc,1 → ΔT_acc
        ↓
executed transformation / subsequent state
        ↓
trajectory
        ↓
outcome
        ↓
Value
```

The final link from `ΔT_acc` to `ΔV` remains an open research question and is not included as an established methodological rule.

## 4. Candidate rules

### M0 — Reconstruct state and relevant conditions

**Rule:** Reconstruct the state/configuration and conditions relevant to the transformation problem before defining candidate transformations.

**Category:** Evidence-supported translation rule.

**Support:** Multidomain bounded support across the frozen evidence set.

**Boundary:** The state representation remains domain-specific at implementation level; no domain variable is automatically a TGCV state primitive.

### M1 — Define candidate transformation universe Uτ

**Rule:** Define the candidate transformation universe before evaluating accessibility or observed outcomes.

**Category:** Evidence-supported translation rule.

**Support:** Explicit in SWIM and C10C-002; compatible with the C09 operational architecture.

**Boundary:** The candidate universe is operationally defined per case; it is not equivalent to the set of transformations actually observed.

### M2 — Define ex-ante admissibility predicate Pτ

**Rule:** Define accessibility/admissibility conditions independently of subsequent outcome or value.

**Category:** Evidence-supported translation rule; empirical gate.

**Support:** Explicit in SWIM and IT-G1; structurally explicit in C09; C10C-002 provides a bounded reconstruction/control case.

**Boundary:** A domain-specific eligibility condition is not automatically a TGCV Pτ unless it functions as an ex-ante accessibility/admissibility criterion.

### M3 — Derive T_acc from Uτ and Pτ

**Rule:** Reconstruct accessible transformations as the candidate transformations satisfying the operational accessibility predicate.

**Category:** Evidence-supported transversal translation rule candidate.

**Support:** SWIM explicit reconstruction; C09 architecture and closed causal evidence; C10C-002 explicit reconstruction; IT-G1 explicit independent accessibility/admissibility closure.

**Boundary:** Observed execution does not define T_acc; outcome does not define T_acc.

### M4 — Compare T_acc states and reconstruct ΔT_acc

**Rule:** Where the design contains comparable states, reconstruct `T_acc,0`, `T_acc,1` and their change `ΔT_acc` independently of outcome.

**Category:** Evidence-supported translation rule; empirical gate.

**Support:** Explicit in SWIM and C10C-002; part of the C09 operational causal architecture.

**Boundary:** A change in observed configuration or treatment is not automatically `ΔT_acc`.

### M5 — Separate ΔT_acc from executed transformation

**Rule:** Keep accessibility change analytically distinct from the transformation actually selected/executed/observed.

**Category:** Bounded transversal translation rule candidate.

**Support:** Explicit temporal separation in SWIM; structural/treatment separation in C10C-002; causal architecture in C09.

**Boundary:** This rule does not assert that accessibility change causes execution or any later outcome.

### M6 — Reconstruct subsequent state / trajectory separately

**Rule:** After reconstructing accessibility and execution, reconstruct subsequent states or trajectories as a temporally distinct layer.

**Category:** Bounded transversal translation rule candidate.

**Support:** Strong bounded trajectory linkage in SWIM; longitudinal variable/audit support and causal architecture in C09/KGFS; bounded state/transition structure in C10C-002.

**Boundary:** KGFS variable-name matches are discovery/audit aids only; they do not by themselves constitute a TGCV trajectory definition. No causal trajectory rule is asserted.

### M7 — Reconstruct outcome independently

**Rule:** Treat the conventional outcome endpoint as a distinct reconstruction layer after the state/trajectory layer.

**Category:** Evidence-supported translation rule.

**Support:** Present as an explicit separation in the frozen cases.

**Boundary:** Outcome definitions remain domain-specific and are not automatically TGCV Value.

### M8 — Do not substitute outcome for Value

**Rule:** Do not identify a conventional outcome with TGCV Value without a separate value construction/validation argument.

**Category:** Evidence-supported boundary/translation rule.

**Support:** Multidomain non-substitution in the cross-domain evidence synthesis and closed case boundaries.

**Boundary:** The existence of an outcome endpoint is not evidence that `ΔV` has been demonstrated.

### M9 — ΔT_acc → ΔV remains open

**Rule status:** OPEN HYPOTHESIS / RESEARCH QUESTION.

No current evidence in this extraction establishes a transversal causal rule from accessibility change to value change.

## 5. Empirical gates associated with the candidate methodology

The following are gates or controls rather than ontology primitives:

1. Ex-ante accessibility/admissibility definition.
2. Outcome-independent reconstruction of T_acc.
3. Temporal ordering between accessibility, execution, subsequent state/trajectory and outcome.
4. Non-circularity: outcome/value variables must not be used to define accessibility.
5. Provenance and reproducibility of source variables and transformations.
6. Independent reconstruction where the evidentiary design requires it.
7. Explicit handling of interference, comparability, and other design-specific threats where applicable.

## 6. Optional conventions

The following are notation/implementation conventions, not TGCV ontological commitments:

- notation `Uτ` for candidate transformation universe;
- notation `Pτ` for accessibility/admissibility predicate;
- snapshot representation of `T_acc`;
- case-specific encoding of transformations, variables and outcomes.

## 7. Core ontology boundary

This extraction does not add new Core primitives. It preserves the current Core boundary around state and accessible transformations and treats interactions/mechanisms and domain-specific operational variables as explanatory or implementation-level material unless independently shown irreducible.

## 8. Open hypotheses and unresolved claims

The extraction does not close or upgrade:

- `ΔT_acc → ΔV`;
- transversal causal value construction;
- C11 transversal validity;
- C12 explanatory superiority;
- C13 originality;
- C16 H-level;
- any claim requiring a stronger causal or value endpoint than the frozen evidence supplies.

## 9. Non-substitution rules

The following substitutions are prohibited without separate evidence:

- observed transformation → accessible transformation;
- eligibility/administrative condition → Pτ;
- structural change/treatment/take-up/adoption → ΔT_acc;
- longitudinal variable match → TGCV trajectory;
- conventional outcome → TGCV Value;
- temporal association → causal effect;
- domain-specific semantics → TGCV primitive.

## 10. Provisional methodological disposition

| Rule | Disposition |
|---|---|
| M0 | Supported candidate |
| M1 | Supported candidate |
| M2 | Supported candidate |
| M3 | Supported — transversal candidate |
| M4 | Supported candidate |
| M5 | Bounded — transversal candidate |
| M6 | Bounded — transversal candidate |
| M7 | Supported candidate |
| M8 | Supported — transversal boundary candidate |
| M9 | Open |

These dispositions are analytical only and do not authorize governance propagation.

## 11. Governance disposition

`CURRENT_INDEPENDENT_ANALYSIS`

No Core, RMA, Evidence-to-Claim Matrix, STATUS, or canonical pointer is modified by this artifact.

The next authorized operation is a Governance Compatibility Audit of M0–M9 to determine whether any rule can be propagated in a controlled manner.
