# TGCV — C09 Controlled Execution Protocol / Freeze Audit 001

**Status:** `AUDIT PASS — EXECUTION PROTOCOL FROZEN / EXECUTION NOT AUTHORIZED BY THIS ARTIFACT`
**Date:** 2026-09-14
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Parent:** `TGCV_C09_CONTROLLED_DOMAIN_DESIGN_AUDIT_001.md`
**Audited package:** `03_EXPERIMENTS/C09_OPERATIONAL_BUNDLE_003/`

## 1. Audit objective

Verify that the concrete C09 controlled execution bundle contains the minimum frozen protocol components required for a bounded causal execution, that its dependencies are explicit, and that no unresolved protocol ambiguity remains that would permit researcher discretion during execution.

This audit is a protocol/freeze decision. It is not a causal result and does not upgrade C09.

## 2. Frozen experimental definition

The bundle specifies a finite synthetic transformation system with 256 independent replicas and fixed horizon `H=1`. The candidate universe is frozen as `U={A,B,C}`. Baseline state/context, transformation effects, scores, accessibility requirements, policy, transition and endpoint are explicitly defined.

The accessibility contrast is:

- `Z=0`: `T_acc={A,C}`;
- `Z=1`: `T_acc={A,B,C}`.

`B` alone requires `R1`; `A` and `C` do not.

**Finding: PASS.**

## 3. Intervention and direct-effect firewall

The protocol restricts treatment to the accessibility predicate. The treatment flag is forbidden as an input to transition, score, policy, metric, observation or randomization. The policy is `P(S,C,T_acc)` and therefore receives the accessible set rather than treatment status.

The transition is invariant: `S1=S0+delta(selected)`, with context unchanged.

**Finding: PASS — direct-effect pathway is explicitly prohibited.**

## 4. Assignment specification

The assignment is frozen as deterministic SHA256-based Fisher-Yates with seed `130917`, balanced 128/128, applied after baseline freezing. The exact digest encoding, integer interpretation and range reduction are supplied by the frozen successor randomization specification `C09_RANDOMIZATION_SPECIFICATION_001.md`.

This closes the previously identified randomization-definition ambiguity without modifying Bundle 003 retroactively.

**Finding: PASS.**

## 5. Endpoint and estimand

The endpoint is the integer final state `Y=S1`. The primary contrast is:

`tau = mean(Y | Z=1) - mean(Y | Z=0)`.

The trajectory is the one-step ordered structure `(S0, selected_transformation, S1)`. No `H>1` inference is permitted.

**Finding: PASS.**

## 6. Null and falsification controls

The null run uses the same units, assignment and frozen generator while setting `R1=false` for both arms, preserving `T_acc={A,C}`. A nonzero null contrast is explicitly permitted and is not an integrity failure.

Hard blocks include accessibility failure, treatment leakage, baseline mismatch, transition/policy/score changes, post-treatment classification, unreconstructible trajectory, metric/observation contamination, unexplained null accessibility change, or hash/reproducibility failure.

**Finding: PASS.**

## 7. Integrity and provenance freeze

The bundle includes a hash manifest covering the canonical fixture, execution specification and Executor-1 source. The manifest requires exact SHA-256 equality before a scientific estimate can be emitted.

Frozen identifiers:

- fixture SHA-256: `3E3AC9601F893B7E01F75813499BB3F539D7B192AE18F0332DC6365AAA5EBD49`
- execution specification SHA-256: `D1621DBBCB9DD840828D0F3C431949D7DDA2B73F3E4B43EA86F35FC07A87E10B`
- Executor-1 SHA-256: `94534CC29FA31E86A9936DE8615D8B0114D44F183942C2126E817E507BF62AC3`
- randomization specification SHA-256: `D07E7CA400A5B1902329237DE6CFFD84B0AE1A7FE8FE44F7F80328887E77F74F`

Git provenance is separately recorded through the corresponding blob identifiers.

**Finding: PASS.**

## 8. Independent reconstruction contract

The protocol requires Executor-2 to reconstruct fixture, assignment, accessibility, policy, transition, endpoint and integrity checks without consuming Executor-1 output. The completed Executor-2 reconstruction is retained as bounded methodological evidence and confirms operational reconstructability, but is not treated as an authorization source for itself.

**Finding: PASS.**

## 9. Runtime and execution environment

Execution is constrained to CPython 3.11+ and the standard library, with no network, external dataset, external package or mutable service. Runtime fingerprinting is required and is treated as provenance, not an experimental degree of freedom.

**Finding: PASS.**

## 10. Authorization boundary

The bundle itself is marked `FROZEN — EXECUTION NOT YET AUTHORIZED`. This audit does not retroactively authorize the already completed Bundle 003 reconstruction and does not authorize a new execution merely because the protocol is frozen.

The previously completed Executor-2 result is evidence already registered under the bounded methodological evidence boundary. No additional Bundle 003 rerun is justified.

**Finding: PASS — authorization boundary preserved.**

## 11. Mandatory freeze criteria

| Criterion | Result |
|---|---|
| Domain frozen | PASS |
| Fixture frozen | PASS |
| Candidate universe frozen | PASS |
| Accessibility intervention frozen | PASS |
| Treatment/control assignment frozen | PASS |
| Exact randomization specification available | PASS |
| Transition invariant | PASS |
| Scoring invariant | PASS |
| Policy invariant | PASS |
| Direct-effect exclusion | PASS |
| Endpoint/estimand frozen | PASS |
| Horizon frozen | PASS |
| Null control frozen | PASS |
| Falsification/stop criteria frozen | PASS |
| Integrity/hash contract frozen | PASS |
| Independent reconstruction contract frozen | PASS |
| Runtime constraints frozen | PASS |
| Scientific scope boundary preserved | PASS |
| Execution authorization boundary preserved | PASS |

## 12. Disposition

**CONTROLLED EXECUTION PROTOCOL / FREEZE AUDIT = PASS.**

The C09 operational protocol is sufficiently complete and unambiguous to be treated as **FROZEN** for the bounded controlled-domain experiment.

This audit does **not** authorize a new scientific execution. The historical Bundle 003 execution/reconstruction remains separately registered evidence and must not be rerun merely to satisfy this audit.

## 13. Next stage

The protocol-design/freeze stage is closed. Any future execution must receive an explicit execution authorization record referencing this frozen protocol and must occur under its frozen inputs without modification.

If the programme continues with the already completed evidence, the next governance operation is **C09 execution-result closure/reconciliation**, not another experiment.

## 14. Scientific status

`C09 = OPEN — CAUSAL CLAIM NOT ESTABLISHED`

`TGCV CORE = UNCHANGED`

`RMA = UNCHANGED`

`EVIDENCE→CLAIM MATRIX CLAIM LEVEL = UNCHANGED`

`NEW EXECUTION AUTHORIZATION = NONE`

No causal, universality, value, industrial-superiority or cross-domain claim is established by this audit.
