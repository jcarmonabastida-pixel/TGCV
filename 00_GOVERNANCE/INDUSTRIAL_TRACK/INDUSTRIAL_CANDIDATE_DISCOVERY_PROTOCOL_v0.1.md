# TGCV — Industrial Candidate Discovery Protocol v0.1

**Date:** 2026-09-09  
**Status:** CURRENT / OPERATIVE — DESIGN-ONLY  
**Execution:** NOT AUTHORIZED  
**Origin:** EXT-UPD-4.9 strategic disposition; IT-G1 FAIL for C-IND-01

## 1. Purpose

Define a pre-selection protocol for identifying industrial candidates that can support a future IT-G1 Case Identifiability review without adapting the case to favorable TGCV results.

The protocol searches for a **naturally bounded industrial unit of analysis**, not for a technology that can be made to fit TGCV.

## 2. Authorization boundary

This protocol authorizes only candidate discovery, documentary screening and governance recording. It does not authorize:

- industrial execution or intervention;
- dataset acquisition or execution;
- partner evidential engagement;
- further O3 accessibility execution;
- Stage C/D;
- utility, causal or value assessment;
- Core modification or claim upgrades.

## 3. Selection principle

A candidate is interesting only if its identity and evidential reconstruction can be closed **before** observing a favorable TGCV result.

The preferred structure is:

`(S_t, C_t) → candidate transformation → accessibility/admissibility → (S_{t+1}, C_{t+1}) → observed outcome`

The protocol does not require a positive `ΔT_acc`; it requires that the candidate permit its independent identification to be tested.

## 4. Mandatory discovery filters

A candidate must be screened against all eight filters:

1. **Natural boundary:** a concrete industrial process, decision, transaction, release, configuration change or other unit exists without being invented for TGCV.
2. **State reconstructability:** relevant initial and subsequent states can in principle be specified independently.
3. **Transformation identity:** the candidate transformation can be defined without using `ΔT_acc`, Reach, outcome or utility as its definition.
4. **Accessibility observability:** admissibility/accessibility conditions can be stated ex ante and potentially evidenced independently.
5. **Temporal closure:** a finite observation window and decision horizon can be specified.
6. **Evidence independence:** decisive evidence does not depend solely on a favorable interpretation produced by TGCV.
7. **Downstream separation:** transformation-space change can be distinguished from Reach, trajectory, outcome and utility.
8. **Access robustness:** initial identifiability does not require privileged partner access as a logical premise. Restricted access may later constrain execution, but it must not be the only way to define the case.

## 5. Automatic discard criteria

Discard the candidate before IT-G1 if any of the following applies:

- unit of analysis is a broad programme, technology category or strategic ambition;
- system boundary `S` cannot be stated concretely;
- transformation identity depends on the result being tested;
- accessibility is synonymous with observed use or success;
- temporal horizon is open-ended;
- decisive evidence can only exist after an intervention not yet authorized;
- utility is required to establish the identity of the transformation;
- the candidate can only be reconstructed from privileged information unavailable independently;
- the candidate requires changing TGCV definitions, thresholds or falsification criteria.

## 6. Candidate screening matrix

Every candidate must be recorded before selection using:

| Field | Required question |
|---|---|
| Candidate ID | Is the candidate uniquely identified? |
| Industrial context | What concrete process/decision is bounded? |
| Unit of analysis | What single event/process unit is reconstructed? |
| System boundary `S` | What is inside/outside the system? |
| State variables | What can be observed at t and t+1? |
| Candidate transformation | What exactly changes? |
| Accessibility | What makes the transformation admissible/accessible? |
| Temporal window | What finite period closes the analysis? |
| Independent evidence | What evidence exists without TGCV interpretation? |
| Downstream separation | Can Reach/trajectory/outcome/utility remain separate? |
| Access dependency | Is privileged access logically necessary for identifiability? |
| Risks | What could make the case indeterminate? |
| Screening disposition | RETAIN / DISCARD / CONDITIONAL |

## 7. Screening rule

`RETAIN` requires all mandatory filters to pass at documentary level. `CONDITIONAL` may be retained only where the missing condition is explicitly identifiable and can be tested at IT-G1 without execution. `DISCARD` is mandatory when an automatic discard criterion applies.

Retention is **not admission**. A retained candidate must subsequently undergo the formal IT-G1 gate.

## 8. Anti-rescue rule

Candidate discovery must not begin from a desired industrial result and work backwards toward a case definition. C-IND-01's failure is therefore not to be repaired by progressively narrowing its wording unless the resulting unit is independently natural and observable.

No candidate may be scored using empirical results from TGCV as evidence of its own admissibility.

## 9. Output of the protocol

The output is a versioned discovery matrix containing only candidate-screening information and a disposition. It does not constitute industrial evidence, utility evidence or scientific validation.

## 10. Next gate

After documentary screening, at most one candidate should be proposed for a controlled IT-G1 review at a time, unless governance explicitly authorizes a broader batch.

**Current state:** discovery protocol operational as design infrastructure; no candidate is admitted and no execution is authorized.
