# TGCV — Industrial Candidate Discovery Protocol v0.2

**Date:** 2026-09-11  
**Status:** CURRENT / OPERATIVE — DESIGN-ONLY  
**Execution:** NOT AUTHORIZED  
**Supersedes:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.1.md`  
**Normative dependency:** TR-132-MOD-1 — CLOSED / BOUNDED PASS (L3)

## 1. Purpose

Define a pre-selection protocol for identifying industrial candidates that can support a future IT-G1 Case Identifiability review without adapting the case to favorable TGCV results.

The protocol searches for a **naturally bounded industrial unit of analysis**, not for a technology that can be made to fit TGCV.

## 2. Authorization boundary

This protocol authorizes only candidate discovery, documentary screening and governance recording. It does not authorize industrial execution, dataset execution, partner evidential engagement, utility/causal/value assessment, Core modification or claim upgrades.

## 3. Selection principle

A candidate is interesting only if its identity and evidential reconstruction can be closed **before** observing a favorable TGCV result.

Preferred structure:

`(S_t, C_t) → candidate transformation → accessibility/admissibility → (S_{t+1}, C_{t+1}) → observed outcome`

The protocol does not require a positive `ΔT_acc`.

## 4. TR-132 accessibility-sufficiency rule

**Exhaustive ex-ante reconstruction of the complete accessible transformation structure `T_acc(S_t)` is NOT a mandatory discovery or screening requirement.**

After TR-132-MOD-1, candidate screening shall not discard a candidate merely because the complete set of accessible alternatives cannot be enumerated before the event.

For retention, the screening must instead establish that the **observed/candidate transformation `τ_i`** can be identified and that its accessibility/admissibility can be evaluated from pre-outcome information available in `(S_t, C_t)`, without defining that accessibility from the subsequent outcome.

The minimum relevant chain is therefore:

`(S_t, C_t) → τ_i → (S_{t+1}, C_{t+1})`

with sufficient evidence to assess:

1. transformation identity;
2. relevant state/context conditions;
3. accessibility/admissibility of `τ_i` under those conditions;
4. outcome-independence of that accessibility assessment;
5. observable/reconstructible state transition.

Partial observability of alternative transformations is **not, by itself, a rejection criterion**.

This rule does not permit retrospective inference from the observed outcome, does not weaken transformation identity, and does not authorize changing TGCV definitions or falsification criteria.

## 5. Mandatory discovery filters

A candidate must be screened against all eight filters:

1. **Natural boundary:** a concrete industrial unit exists without being invented for TGCV.
2. **State reconstructability:** relevant initial and subsequent states can in principle be specified independently.
3. **Transformation identity:** the candidate transformation can be defined without using `ΔT_acc`, Reach, outcome or utility as its definition.
4. **Accessibility sufficiency:** the accessibility/admissibility of the candidate transformation can be assessed from pre-outcome state/context; exhaustive enumeration of all alternatives is not required.
5. **Temporal closure:** a finite observation window and decision horizon can be specified.
6. **Evidence independence:** decisive evidence does not depend solely on a favorable interpretation produced by TGCV.
7. **Downstream separation:** transformation-space change can be distinguished from Reach, trajectory, outcome and utility.
8. **Access robustness:** initial identifiability does not require privileged partner access as a logical premise.

## 6. Automatic discard criteria

Discard before IT-G1 if:

- unit of analysis is a broad programme, technology category or strategic ambition;
- system boundary `S` cannot be stated concretely;
- transformation identity depends on the result being tested;
- accessibility is synonymous with observed use or success;
- accessibility/admissibility of the candidate transformation cannot be assessed independently from pre-outcome information;
- temporal horizon is open-ended;
- decisive evidence can only exist after an unauthorized intervention;
- utility is required to establish transformation identity;
- the candidate can only be reconstructed from privileged information unavailable independently;
- the candidate requires changing TGCV definitions, thresholds or falsification criteria.

**Absence of a complete ex-ante alternative-space enumeration is explicitly excluded from automatic discard.**

## 7. Candidate screening matrix

Every candidate must record at least:

| Field | Required question |
|---|---|
| Candidate ID | Is the candidate uniquely identified? |
| Industrial context | What concrete process/decision is bounded? |
| Unit of analysis | What single event/process unit is reconstructed? |
| System boundary `S` | What is inside/outside the system? |
| State variables | What can be observed at t and t+1? |
| Candidate transformation | What exactly changes? |
| Accessibility/admissibility | Can `τ_i` be assessed as accessible from pre-outcome `S_t,C_t`? |
| Alternative-space completeness | Is `T_acc` complete, partial, or unknown? Is that incompleteness actually material to the test? |
| Outcome independence | Is accessibility assessed without using the outcome? |
| Temporal window | What finite period closes the analysis? |
| Independent evidence | What evidence exists without TGCV interpretation? |
| Downstream separation | Can Reach/trajectory/outcome/utility remain separate? |
| Access dependency | Is privileged access logically necessary for identifiability? |
| Risks | What could make the case indeterminate? |
| Screening disposition | RETAIN / DISCARD / CONDITIONAL |

## 8. Screening rule

`RETAIN` requires all mandatory filters to pass at documentary level. `CONDITIONAL` may be retained where the missing condition is explicitly identifiable and can be tested at IT-G1 without execution. `DISCARD` is mandatory only when an automatic discard criterion applies.

Retention is not admission. A retained candidate must subsequently undergo the formal IT-G1 gate.

## 9. Anti-rescue rule

Candidate discovery must not begin from a desired industrial result and work backwards toward a case definition. No candidate may be scored using empirical TGCV results as evidence of its own admissibility.

## 10. Output and next gate

The output is a versioned discovery matrix containing candidate-screening information and disposition. It does not constitute industrial evidence, utility evidence or scientific validation.

After documentary screening, at most one candidate should be proposed for controlled IT-G1 review at a time unless governance explicitly authorizes a broader batch.

**Current state:** discovery protocol operational as design infrastructure; no candidate is admitted and no execution is authorized.
