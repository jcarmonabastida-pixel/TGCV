# EXT-UPD-4.1 — D-OPS-24 v0.5 Design Audit v0.1

**Status:** CLOSED / DESIGN AUDIT — CONDITIONAL PASS WITH REQUIRED REFINEMENTS
**Date:** 2026-09-09
**Audited artifact:** `D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.5.md`

## 1. Audit objective

Determine whether v0.5 removes the potential discovery bottleneck identified after F2 while preserving a sufficiently discriminating scientific gate.

## 2. Result

**CONDITIONAL PASS.** The staged architecture is methodologically preferable to v0.4 and is aligned with the transversal object of TGCV. However, v0.5 must be refined before freeze in four places.

## 3. Findings

### A1 — Object of evaluation
PASS. The protocol now tests whether an external domain can support an independent translation of the TGCV analytical core rather than whether the domain already contains the complete TGCV architecture.

### A2 — Minimum gate is materially lighter
PASS. Requiring only the minimum structure needed to construct `S_D`, `Uτ,D`, `T_acc,D` and `ΔT_acc,D` avoids premature rejection based on downstream objects.

### A3 — Risk of over-permissiveness
OPEN / REFINEMENT REQUIRED. MTE-1..MTE-10 are individually appropriate but do not yet specify a compact mechanical decision rule for what constitutes an adequate `Uτ,D` and accessibility predicate. The next version must operationalize these two points sufficiently to prevent generic state-transition literature from becoming automatically eligible.

### A4 — Gate separation
PASS. Reach, Trajectory, Outcome and Value are correctly moved from discovery prerequisites to downstream translation/conformance tests.

### A5 — Circularity protection
PASS WITH REFINEMENT. Outcome-defined accessibility is excluded, but the next version should require that the candidate's native accessibility criterion be documented independently of the TGCV translation record and preferably be identifiable before the outcome variable is consulted.

### A6 — Native-domain distinction
PASS. Silent proxy substitution is explicitly prohibited. The next version should require a named native construct and a statement of what it does NOT represent when mapping is PARTIAL or PROXY.

### A7 — Temporal requirement
PASS. Two ordered observations are a minimum feasibility condition, not evidence of a demonstrated dynamic effect. This distinction must remain explicit.

### A8 — Search breadth
PASS. The protocol no longer embeds the semantic vocabulary of one family into the discovery query itself. This is necessary to avoid query-induced domain exclusion.

### A9 — Redundancy control
PASS. Existing TGCV instantiations remain excluded, while genuinely distinct native domains remain possible.

### A10 — Indeterminate state
PASS. INDETERMINATE prevents evidence scarcity from being converted into a false scientific failure.

## 4. Required refinements before freeze

R1. Define a minimal adequacy test for `Uτ,D`: transformations must be independently enumerable/specifiable at the chosen unit of analysis without reference to observed outcomes.

R2. Define a minimal adequacy test for `Pτ,D`: accessibility must be evaluable from pre-outcome state/context information and must distinguish at least feasible from non-feasible transformations.

R3. Add a **Translation Readiness** sub-gate between MTE and the full trace, requiring one worked documentary example showing that at least one native state admits at least two distinguishable candidate transformations whose accessibility can be assessed without outcome information. This is a feasibility demonstration, not empirical validation.

R4. Explicitly prohibit “state transition = transformation accessibility” as an automatic identification. A domain may contain observed transitions while lacking an independently specified accessible transformation space.

## 5. Scientific interpretation

The audit does not conclude that v0.4 was scientifically invalid. It concludes that v0.4 may have imposed a discovery bottleneck by asking documentary discovery to establish downstream conformance too early.

The v0.5 staged architecture is therefore a better test of the transversal hypothesis because it allows the external domain to remain natively specified until the translation stage.

## 6. Decision boundary

v0.5 should not be frozen until R1-R4 are incorporated. No search authorization follows from this audit.

## 7. Next gate

Produce D-OPS-24 v0.5 revised design incorporating R1-R4, then perform a final preflight and consistency propagation before any execution authorization.
