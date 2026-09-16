# TGCV MT5 — Downstream Value Endpoint Protocol 001

**Status:** PROTOCOL — FROZEN FOR SOURCE SELECTION
**Purpose:** attack the principal unresolved TGCV value-layer bottleneck without reopening completed MT4 gates.

## 1. Research target

Test whether an independently defined downstream outcome/value endpoint can support the analytical chain:

`S_t → U_tau → P_tau → T_acc,t → ΔT_acc → subsequent transformation/trajectory → Outcome/Value`

The test must not define accessibility from the value endpoint, and must not use downstream value information to construct `P_tau` retrospectively.

## 2. Required evidence architecture

A candidate source is admissible only if it can support, independently and in temporal order:

1. **Pre-treatment/pre-decision state** `S_t`.
2. **Candidate transformations** `U_tau`, defined independently of outcomes.
3. **Admissibility rule** `P_tau(S,C,L)`, frozen before inspecting downstream outcomes.
4. **Accessible transformation space** `T_acc,t` or a defensible bounded approximation.
5. **Change in accessibility** `ΔT_acc` between ordered states or periods.
6. **Subsequent realization/trajectory**, occurring after the accessibility change.
7. **Independently measured downstream outcome/value** `V_{t+k}`.

## 3. Mandatory anti-circularity controls

### Control A — Value blindness
Variables used to define `P_tau` or `T_acc` must not be selected because they correlate with, predict, or are consequences of the downstream value endpoint.

### Control B — Temporal non-leakage
Information observed after the accessibility-changing event must not enter the earlier definition of `P_tau`, `U_tau`, `T_acc,t` or baseline state.

### Control C — Endpoint separation
The value/outcome endpoint must not be reused as a component of accessibility, candidate transformation identity or state definition.

### Control D — Transformation/realization separation
Observed implementation, take-up or realized transformation must not automatically be treated as accessibility.

### Control E — Pre-specification
The candidate accessibility representation and value endpoint must be frozen before the final downstream effect is interpreted.

## 4. Preferred causal design

A source is preferred when it contains an exogenous, randomized or otherwise independently identified intervention that changes an accessibility-relevant structural condition, followed by a downstream outcome/value measurement.

The target estimand is conceptually:

`ΔT_acc → subsequent trajectory → ΔV`

where the accessibility layer is independently reconstructed and the value endpoint is downstream and independently defined.

A conventional treatment effect alone is insufficient if the treatment cannot be translated into an independently defined accessibility change.

## 5. Value endpoint requirements

The endpoint must be:

- downstream of the accessibility-changing event;
- independently measured or constructed from frozen source variables;
- substantively interpretable as an outcome/value consequence rather than an input constraint;
- temporally ordered after the accessibility change;
- reproducible from the frozen source and code where available;
- separable from treatment assignment and implementation.

Economic variables used as model inputs, prices, costs or technical parameters are not automatically `ΔV`.

## 6. Exclusion rules

Reject a candidate if any of the following is unavoidable:

- `P_tau` can only be defined using downstream outcomes;
- the proposed accessibility measure is merely treatment assignment, take-up, installation or observed realization;
- the endpoint is contemporaneous with or prior to the accessibility change with no defensible downstream interpretation;
- the only value measure is itself an input to the transformation/admissibility rule;
- temporal ordering cannot be established;
- the source requires post-hoc selection of the accessibility representation after inspecting outcome effects.

## 7. Decision states

- **MT5-CANDIDATE PASS:** source satisfies the frozen source-selection architecture and can proceed to operationalization.
- **MT5-BOUNDARY:** source provides useful downstream/value evidence but cannot independently close the accessibility layer.
- **MT5-FAIL:** source violates a mandatory control or cannot support a downstream value endpoint.
- **MT5-BLOCKED:** source package/provenance is insufficient for a defensible audit.

## 8. Required execution sequence

**MT5-1:** candidate-source discovery.

**MT5-2:** source freeze and provenance audit.

**MT5-3:** pre-outcome state and candidate-transformation reconstruction.

**MT5-4:** independent `P_tau` / `T_acc` reconstruction.

**MT5-5:** temporal separation and trajectory audit.

**MT5-6:** downstream value endpoint reconstruction.

**MT5-7:** causal/value-link analysis, only if all preceding gates pass.

**MT5-8:** independent reproducibility audit.

## 9. Governance boundary

MT5 must not modify TGCV Core, RMA or claim levels merely because a candidate source passes source-selection or operationalization gates. Any evidence propagation and any claim-level consolidation must be recorded separately.

## 10. Relation to MT4

MT4 is closed as a bounded methodological transfer result. MT5 therefore does **not** reopen MT4's temporal audit, CORE6 coverage, collision analysis, downstream separation or value-isolation gates. MT4's unresolved value boundary is the motivation for this new prospective test.

## 11. Success criterion

The scientifically informative outcome is not necessarily a positive value effect. A successful MT5 execution may yield a positive, null or bounded result. What matters is whether the complete analytical distinction between accessibility change and independently measured downstream value can be reconstructed without circularity or temporal leakage.
