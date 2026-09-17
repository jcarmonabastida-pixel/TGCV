# TGCV — MT5 VSL Specification Completeness and Reproducibility Gate 001

**Date:** 2026-09-17  
**Status:** `FROZEN GATE — NOT EXECUTED`  
**Programme:** TGCV — Teoría de Construcción de Valor de Sistemas Generativos

## 1. Trigger

MT5-11 closed with bounded underdetermination of `V*`: two independent analysts agreed that the frozen C09/KGFS evidence did not determine a valuation objective, direction rule, or reproducible `O → V*` mapping. MT5-VSL-01 subsequently identified a candidate external Valuation Specification Layer (`VSL`) to make those missing substantive inputs explicit and independently auditable.

This gate tests whether a frozen VSL can be complete enough to support reproducible construction of a domain-bounded `V*` without contaminating `T_acc` or embedding the observed treatment effect.

## 2. Scope boundary

Candidate architecture:

`T_acc / trajectory → outcome O → frozen VSL → V*`

The VSL is external to the transformational core. The gate cannot modify the operational definitions of `Pτ`, `T_acc`, `ΔT_acc`, treatment, trajectory, or outcome.

The gate does not test causal identification of `ΔT_acc → ΔV`.

## 3. Gate A — specification completeness

A VSL is **complete for execution** only if all fields below are explicitly frozen before analyst execution.

| Gate | Requirement | Pass condition |
|---|---|---|
| A1 | Reference entity | Unit of valuation explicitly named and operationally identifiable |
| A2 | Valuation objective | Substantive objective explicitly stated; not inferred from outcome improvement |
| A3 | Direction rule | Increasing/decreasing/neutral interpretation explicitly defined |
| A4 | Outcome selection | Outcome variable(s) eligible for valuation explicitly designated without redefining `T_acc` |
| A5 | `O → V*` mapping | Deterministic or explicitly parameterized mapping stated |
| A6 | Reference frame | Comparator, horizon, population/domain and relevant baseline fixed |
| A7 | Measurement rule | Reproducible endpoint/index/vector/contrast/estimand specified |
| A8 | Decision rule | Exact rule for producing `V*` from the specified outcome representation stated |
| A9 | Provenance | Source/rationale/version/effective period of substantive valuation specification recorded |
| A10 | Non-circularity | No treatment effect, `ΔT_acc`, downstream conclusion or outcome result embedded in definition |
| A11 | Domain boundary | Domain, population and substantive scope explicitly bounded |
| A12 | Version separation | VSL version can be frozen and distinguished from empirical evidence version |

**Gate A decision rule:** all A1–A12 must PASS. Any unresolved substantive field is a BLOCK for analyst execution, not a discretionary interpretation.

## 4. Gate B — reproducibility design

Only after Gate A passes may independent execution proceed.

Required controls:

1. frozen empirical outcome bundle;
2. frozen VSL specification and hash;
3. blank Analyst 1 and Analyst 2 worksheets;
4. independent execution without cross-analyst communication;
5. no access to prior interpretation results during execution;
6. explicit recording of any execution ambiguity;
7. adjudication only after both worksheets are frozen.

## 5. Reproducibility criteria

The resulting `V*` is considered reproducible only if both analysts recover materially equivalent results under the same frozen VSL and outcome evidence, including:

- same reference entity;
- same eligible outcome representation;
- same valuation direction;
- same mapping;
- same reference frame;
- same measurement rule;
- same `V*` construction or materially equivalent representation under a predeclared equivalence rule.

Failure to reproduce because the VSL itself is underspecified is classified as a **specification failure**, not as evidence about the empirical outcome.

## 6. Separation tests

The executed gate must separately verify:

### S1 — Outcome invariance

Applying the VSL does not alter the previously frozen empirical outcome measurement.

### S2 — T_acc invariance

Applying the VSL does not alter `T_acc`, `ΔT_acc`, `Pτ`, treatment assignment, or accessibility reconstruction.

### S3 — Trajectory invariance

Applying the VSL does not retrospectively redefine the reconstructed trajectory.

### S4 — Specification sensitivity

If the VSL is changed in a controlled methodological comparison while empirical evidence remains fixed, any resulting change is attributable to valuation specification rather than empirical reconstruction.

## 7. Decision classes

The gate may produce only one of:

- `PASS — VSL COMPLETE AND REPRODUCIBLE`
- `PARTIAL — VSL EXECUTABLE BUT REPRODUCTION DIVERGES`
- `FAIL — VSL INCOMPLETE`
- `BLOCKED — FROZEN INPUTS OR SPECIFICATION INSUFFICIENT`

No decision class authorizes a universal substantive Value definition.

## 8. Failure conditions

Immediate failure or block if:

- objective or direction is implicit rather than specified;
- `O → V*` cannot be executed from the frozen specification;
- analyst execution requires unstated normative choices;
- VSL changes `T_acc` or treatment definitions;
- the observed treatment effect is used to define Value;
- substantive provenance is absent where required;
- VSL and empirical evidence cannot be independently versioned;
- analyst independence is compromised.

## 9. Governance controls

The gate itself authorizes no changes to:

- TGCV Core;
- RMA;
- Evidence→Claim Matrix;
- STATUS;
- C09 status;
- M9 `ΔT_acc → ΔV`.

Any future claim-level consequence requires a separate closure record after execution.

## 10. Current disposition

**MT5-VSL-02: `FROZEN GATE — NOT EXECUTED`.**

The gate is now the controlled instrument for testing the VSL candidate. No analyst execution is authorized until a concrete VSL instance and its empirical input bundle have been frozen and Gate A has been audited as PASS.

## 11. Authorized next movement

Construct and freeze a **domain-bounded VSL instance** for a selected existing case, together with its exact empirical outcome input bundle. Then execute Gate A before any independent analyst reconstruction.
