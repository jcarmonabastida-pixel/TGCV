# TGCV — MT-4 Domain Transfer Test Protocol — 001

**Status:** ANALYSIS PROTOCOL — PRE-REGISTRATION CANDIDATE, NOT GOVERNANCE-NORMATIVE  
**Date:** 2026-09-16  
**Purpose:** Define, before case selection and execution, the prospective methodological transfer test required to assess whether the candidate transversal translation-and-audit sequence can be applied to a genuinely new heterogeneous domain without unsupported semantic substitution.

## 1. Governance boundary

This protocol is downstream of `TGCV_TRANSVERSAL_METHODOLOGY_MATRIX_CANDIDATE_001.md` and does not modify TGCV Core, RMA v3.35, Evidence-to-Claim Matrix v1.11, claim levels, or any existing causal conclusion.

MT-4 is a test of **methodological transfer**, not a test of whether TGCV is true in the selected domain. A successful result would support the portability of the analytical procedure within the tested scope; it would not establish transversal validity of TGCV. A bounded or failed transfer is evidence about methodological applicability and limits, not by itself a refutation of TGCV.

## 2. Target methodological sequence

The protocol tests the prospective application of:

`S_t → Uτ → Pτ(S,C,L) → T_acc,t → ΔT_acc → realization/execution → subsequent state/trajectory → Outcome → Value`

The arrows are procedural dependencies. They are not assumed causal relations.

## 3. Preconditions

### MT4-0 — Protocol freeze

Before inspecting the selected case for TGCV constructs:

1. this protocol is frozen;
2. the candidate case/domain is recorded;
3. the source package is identified and hashed where technically feasible;
4. the pre-outcome and post-outcome evidence boundary is declared;
5. no TGCV interpretation is retroactively added to the frozen source package.

No execution is considered valid if the methodology is adapted after seeing the downstream result without recording the adaptation as a deviation.

## 4. Gates

### MT4-1 — Domain novelty

**Question:** Is the selected domain sufficiently new relative to the cases used to formulate the candidate methodology?

**PASS condition:** The domain was not previously used to construct the methodological rules being tested.

**BOUNDARY:** A previously used domain is not eligible for the primary prospective MT-4 test, even if a different dataset is available, unless the test is explicitly designated a replication rather than a transfer test.

### MT4-2 — Frozen evidence

**Question:** Can the empirical source material be frozen before the TGCV translation is performed?

**PASS condition:** A reproducible source package exists, with provenance and a declared temporal boundary separating information available for defining earlier layers from later outcome/value information.

**FAIL condition:** The source material is mutable or its temporal provenance is insufficient to establish what information was available when earlier constructs would have been defined.

### MT4-3 — Independent semantic mapping

**Question:** Can the domain be mapped prospectively into `S_t`, `Uτ`, `Pτ`, and `T_acc` without importing unsupported meanings?

**PASS condition:** Domain variables/objects are explicitly mapped to TGCV analytical roles, with definitions and provenance, and `Uτ` and `Pτ` are specified before inspecting downstream outcome/value results.

**BOUNDARY:** If only state/change/outcome can be reconstructed but accessibility cannot be independently identified, record the boundary rather than substituting a nearby empirical construct.

### MT4-4 — Semantic non-substitution

**Question:** Are accessibility and its neighboring empirical concepts kept distinct?

The audit must explicitly test whether any of the following are being used as substitutes for `T_acc` without an independent admissibility basis:

- treatment/intervention;
- adoption/take-up;
- realized or executed transformation;
- observed configuration;
- structural change;
- outcome;
- value endpoint.

**PASS condition:** Each substitution is either rejected or independently justified by a domain-specific `Pτ` that preserves the TGCV meaning.

### MT4-5 — Temporal non-leakage

**Question:** Are earlier analytical layers defined without information from later states, realization, trajectory, outcome, or value?

**PASS condition:** For every `T_acc,t` definition, the information set used is documented and contains no post-t information that would not have been available at the relevant time.

**FAIL condition:** Later information is required to determine earlier accessibility, unless the construct is explicitly reclassified as retrospective/descriptive rather than prospective accessibility.

### MT4-6 — Independent reproducibility

**Question:** Can a second executor independently reconstruct the same operational objects and rules from the frozen package?

**PASS condition:** Executor 2, operating without Executor 1's interpretations or results, reproduces the declared state representation, candidate transformation universe, admissibility rules, accessibility representation, and derived change within the pre-specified scope.

**BOUNDARY:** Agreement on labels alone is insufficient; the operational object and rule must be reproducible.

### MT4-7 — Downstream separation

**Question:** Where longitudinal data permit, can the downstream layers be reconstructed separately?

The analysis must distinguish:

`ΔT_acc → realization/execution → subsequent state/trajectory → Outcome`

without assuming that an observed association establishes any arrow causally.

**PASS condition:** The layers are separately observable or operationalizable and their temporal ordering is auditable.

**BOUNDARY:** Missing downstream layers do not invalidate a successful upstream translation; they limit the scope of the transfer result.

### MT4-8 — Value isolation

**Question:** Can Value or `ΔV` be introduced only after the preceding layers have been independently defined?

**PASS condition:** Value endpoints are excluded from the construction of `Uτ`, `Pτ`, `T_acc`, and `ΔT_acc`.

**BOUNDARY:** Absence of a valid value measure leaves the value layer open; it must not be manufactured from an outcome merely to complete the chain.

## 5. Required execution record

The MT-4 execution package must contain, at minimum:

1. domain-selection rationale and novelty declaration;
2. frozen source inventory and hashes where feasible;
3. temporal information-set declaration;
4. raw empirical semantic inventory;
5. `S_t` definition;
6. `Uτ` definition and universe boundary;
7. `Pτ(S,C,L)` definition for each admissible transformation class;
8. `T_acc,t` reconstruction;
9. `ΔT_acc` representation preserving transformation identity;
10. realization/execution variables and explicit separation from accessibility;
11. trajectory reconstruction, if available;
12. Outcome definition, if available;
13. Value definition, if available;
14. non-substitution audit;
15. temporal non-leakage audit;
16. independent Executor-2 reconstruction;
17. discrepancies and deviations, including any methodological adaptation;
18. final gate-by-gate disposition.

## 6. Decision rules

### PASS — Prospective methodological transfer

All mandatory gates MT4-1 through MT4-6 pass, and MT4-7/MT4-8 pass or are explicitly bounded by unavailable downstream data. No unsupported semantic substitution or temporal leakage occurs.

Interpretation: the candidate methodology has been prospectively instantiated in the tested new domain within the declared scope. This is **not** a claim of general transversal validity and does not upgrade C11 or C16 automatically.

### BOUNDED PASS — Transfer with explicit methodological boundary

The upstream translation and audit are reproducible, but one or more downstream layers or transformation-space elements are not identifiable in the new domain. The boundary is demonstrated rather than hidden by substitution.

Interpretation: positive evidence for applicability of the tested methodological subset, with a documented limit. No generalization beyond the tested scope.

### FAIL — Methodological transfer failure

The protocol requires unsupported semantic equivalence, cannot establish the frozen information boundary, or independent executors cannot reproduce the essential operational objects/rules.

Interpretation: evidence that the candidate methodology, in its current form, does not transfer cleanly to the tested domain. This is a methodological limitation result, not by itself a refutation of TGCV's ontology or existing empirical claims.

### INVALID / REJECTED

The case fails preconditions before scientific execution, for example because the domain is not genuinely novel for MT-4, the source package cannot be frozen, or the execution boundary is contaminated by prior interpretation.

Interpretation: no methodological result.

## 7. Prohibited practices

The MT-4 execution must not:

- choose `T_acc` after inspecting which representation best predicts the outcome;
- define accessibility as whatever was actually adopted or executed;
- define accessibility from treatment assignment alone;
- define `Pτ` using downstream outcome or value;
- rename an observed structural change as `ΔT_acc` without transformation-level identification;
- infer causal links merely because adjacent layers are correlated;
- use an outcome/value endpoint to repair an otherwise missing accessibility construct;
- silently change the methodology after observing results;
- use prior executor interpretations to coach Executor 2.

## 8. Evidence interpretation

MT-4 evaluates the **methodological procedure**, not the truth of every TGCV proposition.

Accordingly:

- a clean transfer supports portability of the tested analytical distinctions within scope;
- a bounded transfer supports only the identifiable subset and its boundary;
- a transfer failure identifies an applicability limitation or an operationalization defect to investigate;
- none of these outcomes, by themselves, establishes or refutes general TGCV validity.

## 9. Relation to current governance state

No claim upgrade is authorized by this protocol alone.

In particular, MT-4 execution must not automatically modify:

- TGCV Core;
- RMA v3.35;
- Evidence-to-Claim Matrix v1.11;
- C09 bounded causal status;
- C10 status;
- C11 transversal-validity status;
- C12 superiority status;
- C16 methodological/originality status;
- the open `ΔT_acc → Value` layer.

Any later propagation requires a separate evidence-to-claim audit after the MT-4 result is closed.

## 10. Next authorized action

**Do not execute MT-4 yet.**

The next authorized step is to select a genuinely new heterogeneous domain and freeze its evidence package under MT4-1/MT4-2. Only after that freeze may the prospective translation gates be executed.

The selected domain should ideally contain enough temporal structure to permit, without requiring it, an auditable downstream sequence from transformation-space change to subsequent trajectory and an independently defined outcome/value layer.

**Current status:** PROTOCOL DEFINED — CASE NOT YET SELECTED — EXECUTION NOT STARTED.
