# 2026-09-09 — TR-132 Design Decision

## Decision

Following the convergence of the scientific and industrial operational bottleneck on `T_acc`, the next controlled operation is to formalize **TR-132 — T_acc Operational Identifiability Test** before attempting another dataset or industrial case.

## Rationale

The current architecture retains `T_acc = F(S,C,L)` and `ΔT_acc` as its analytical object and central phenomenon. Prior governed work has shown that realized transformations and normative specifications do not by themselves close the effective decision-time accessible set. D-OPS-24 reached the same bounded documentary boundary across aviation, railway signalling and electricity transmission without producing an IT-G1 candidate.

The methodological question is therefore whether the difficulty is:

1. full-space empirical identifiability;
2. identifiability of a bounded subset/change; or
3. an inadequacy in the current operational formulation.

The design must answer these in that order.

## Guardrail

No modification of the Core is proposed at this stage. No new empirical execution is authorized by this decision.

## Intended outputs

- formal distinction among `T_poss`, `T_adm`, `T_acc` and `T_obs`;
- criterion for full-space identifiability;
- criterion for bounded `T_acc^+` / `ΔT_acc^+` identification;
- non-circularity conditions;
- mapping of existing claims to the minimum identification level they require;
- explicit PASS / BOUNDED PASS / FAIL / INCONCLUSIVE outcomes.
