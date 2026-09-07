# DR-028 — Rust Scientific Interpretation and Next-Test Gate v0.2

**Status:** ACCEPTED — EX-ANTE INTERPRETATION BOUNDARY / NO NEW EXECUTION AUTHORIZED
**Date:** 2026-09-07
**Supersedes:** `DR-028_Rust_Scientific_Interpretation_and_Next_Test_Gate_v0.1.md` as the governing accepted decision

## 1. Acceptance basis

DR-028 v0.1 was reviewed against:

- `EXT-1.1_SCIENTIFIC_RECONCILIATION_v0.1.md`;
- closed EXT-1.1 confirmatory evidence under DR-027C;
- the stabilized TGCV Core;
- TR-130 and the established Core integrity constraints;
- the role of TR-131 as a distinct irreducibility question rather than a result established by EXT-1.1.

No contradiction requiring modification of the DR-028 interpretation boundary was identified.

## 2. Accepted empirical interpretation

EXT-1.1 provides reproducible, protocol-local evidence that the frozen operational representation of `T_acc^(R*)` did not improve out-of-sample predictive performance relative to the frozen baseline `B` for the predefined outcome `Y_180` in the Rust package-release population.

Confirmed primary result:

`ΔLogLoss = LogLoss(B) - LogLoss(T_acc) = -0.006122732273119991`

with:

- `LogLoss(B) = 0.40512255638027656`
- `LogLoss(T_acc) = 0.41124528865339655`
- `Brier(B) = 0.12862999557185928`
- `Brier(T_acc) = 0.13123035232566702`
- `AUC(B) = 0.7671989511641575`
- `AUC(T_acc) = 0.759314009238935`

Under the frozen DR-026C sign convention, the negative primary difference is descriptively unfavorable to the tested `T_acc` operationalization.

## 3. Scope of the conclusion

The accepted conclusion is deliberately bounded:

> In the tested Rust operationalization, explicit representation of `T_acc` did not demonstrate incremental predictive utility for subsequent release activity over the frozen baseline.

This does NOT establish that:

1. `T_acc` is ontologically unnecessary;
2. the TGCV Core is false;
3. accessible transformations have no causal, explanatory, or value-relevant role;
4. `T_acc` can never contain analytically relevant information beyond conventional state representations;
5. the result generalizes to other domains, transformation families, outcomes, horizons, representations, resolvers, learners, or populations;
6. the observed difference is statistically significant at the population level;
7. B is causally superior to `T_acc`.

No inferential or causal claim is authorized by DR-028.

## 4. Consequence for the TGCV Core

EXT-1.1 does not require a substantive revision of the stabilized conceptual Core.

The accepted conceptual formulation remains:

- `Core_ontological = S`;
- `T_acc = F(S,C,L)` as a derived analytical object;
- `I` as explanatory mechanism/occasion rather than Core primitive;
- central phenomenon: change in transformational accessibility, `ΔT_acc`;
- analytical chain: `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.

The distinction between ontological/descriptive relevance and predictive utility for a particular operational test is mandatory.

## 5. Relation to TR-130 and TR-131

The acceptance is consistent with TR-130: interaction is not reintroduced as an ontological primitive.

TR-131 remains an independent question concerning whether `T_acc` is irreducible relative to `S`. EXT-1.1 does not resolve that question because its confirmatory criterion was incremental predictive performance for `Y_180`, not ontological irreducibility.

Therefore neither a positive nor negative TR-131 conclusion is inferred from EXT-1.1.

## 6. Historical documentation conflict

The reconciliation artifact `EXT-1.1_SCIENTIFIC_RECONCILIATION_v0.1.md` is now part of the current scientific traceability record.

Historical documents containing pre-result positive wording remain preserved unchanged. They are not treated as the current empirical interpretation where they conflict with the closed EXT-1.1 evidence.

## 7. Authorization boundary

DR-028 authorizes no new empirical execution.

Any future work requires a separate ex-ante decision establishing at minimum:

- exact proposition;
- theoretical criterion and its connection to the proposition;
- outcome or non-predictive criterion;
- population and observational unit;
- baseline and `T_acc` representations, if applicable;
- resolver, horizon and temporal protocol, if applicable;
- learner/evaluation method, if applicable;
- primary metric or decision criterion;
- exclusions and missing-data rules;
- reproducibility requirements;
- falsification condition;
- explicit separation from information revealed by EXT-1.1.

Post-hoc selection of an outcome, horizon, model, representation, or sampling rule because it is expected to reverse the observed EXT-1.1 result is prohibited.

## 8. Accepted next-test options

The following remain legitimate research directions, subject to independent ex-ante justification:

**A. Localized negative evidence:** retain EXT-1.1 as bounded evidence against incremental predictive utility of the tested `T_acc` operationalization for `Y_180`.

**B. Independent theoretical test:** test whether `T_acc` represents a property theoretically distinct from conventional state variables without making predictive improvement the sole criterion.

**C. New predictive test:** test a theoretically justified outcome with all design choices frozen before observing new results.

**D. Theory revision:** narrow the empirical scope of the predictive formulation if subsequent evidence warrants it.

No single option is selected by this acceptance.

## 9. Temporal split note

The previously identified discrepancy between the DR-026C audit boundary and the executed boundary is retained as a documentation/audit-reference issue. The executed partition over the DR-024 eligible population is the authoritative execution evidence and is preserved under DR-027C.

No execution artifact is retroactively modified.

## 10. Governance consequences

This acceptance closes the interpretation-gate question without changing the TGCV Core and without authorizing further computation.

Any substantive change to the scientific state, Core, empirical claim, outcome, baseline, `T_acc` operationalization, model, inference procedure, or empirical scope requires a new versioned governance decision.

## 11. Decision

**DR-028 ACCEPTED.**

The current scientific interpretation of EXT-1.1 is a localized negative empirical result for the tested predictive operationalization of `T_acc` on `Y_180`, with no theory-level refutation and no universal ontological conclusion.

**NO NEW EXECUTION IS AUTHORIZED BY DR-028.**
