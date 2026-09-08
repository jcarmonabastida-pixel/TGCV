# D-OPS-5 — Protein-Evolution Admissibility & Transformation Identifiability Audit v0.1

**Status:** CLOSED — CANDIDATE REJECTED FOR CURRENT EMPIRICAL REPLICATION
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED

## 1. Scope

Audit whether longitudinal protein-evolution data can instantiate the TGCV operational architecture independently of observed outcomes, while preserving the distinction between `Uτ`, `Pτ`, `T_acc`, `ΔT_acc` and downstream Reach/Trajectory.

No dataset was downloaded, sampled or executed.

## 2. Evidence reviewed

### A. HIV-1 protease longitudinal dataset

Dryad provides longitudinal HIV-1 protease sequences collected from the same patients before and after treatment/untreated conditions, as well as sequences spanning 1998–2006. The dataset is public and reproducible. citeturn0search0turn0search14

The source explicitly describes sequences before/after treatment and separate treated/untreated populations. This is useful for longitudinal state reconstruction, but treatment status and observed sequence changes are downstream observations and cannot define accessibility.

### B. Empirical fitness landscapes

Public protein fitness-landscape datasets exist, including large intragenic landscapes and experimentally characterized protein/RNA landscapes. citeturn0search10turn0search3turn0search5

These data make it possible to define neighbouring genotypes and experimentally measured fitness, but using measured fitness to define `Pτ` would introduce an outcome-dependent accessibility predicate. That would violate the TGCV firewall for pre-execution accessibility.

### C. Theoretical mutational accessibility

The evolutionary-literature notion of an accessible mutational path commonly uses fitness increase at each mutational step. citeturn0academia42turn0search6

This is conceptually close to TGCV Reach/accessibility but is not independently admissible for the present audit because fitness would enter the accessibility predicate. It therefore cannot simply be imported as `Pτ` without changing TGCV semantics.

## 3. Identifiability audit

| Criterion | Result | Reason |
|---|---|---|
| D5-1 Independent domain | PASS | Biological evolution is genuinely external to Rust/software configuration. |
| D5-2 Observable system state S | PASS | Protein/genotype sequences are directly represented. |
| D5-3 Independent transformation universe Uτ | PASS | Point substitutions can be enumerated independently of observed evolutionary paths. |
| D5-4 Canonical τ identity | PASS | A mutation can be canonically represented as position + source residue + target residue (with sequence context as required). |
| D5-5 Pre-execution Pτ independent of outcomes | FAIL / CONDITIONAL | Biologically meaningful admissibility requires structural/biophysical assumptions; observed fitness, treatment response or observed future mutations cannot be used. A trivial predicate accepting every point substitution would be formally non-circular but scientifically weak and would collapse the accessibility distinction. |
| D5-6 T_acc independently constructible | FAIL under current evidence | Without a justified non-trivial Pτ, T_acc is either the full mutational neighbourhood or becomes outcome/fitness-derived. |
| D5-7 Longitudinal ΔT_acc | FAIL under current operationalization | Longitudinal sequences provide changing S, but do not by themselves provide independently defined changing admissibility constraints. |
| D5-8 Reach as downstream object | CONDITIONAL | Mutational-neighbour configurations can be enumerated, but independence from T_acc becomes trivial if Reach is only the mutation neighbourhood. |
| D5-9 Public reproducibility | PASS | The reviewed Dryad datasets are publicly available. citeturn0search0turn0search10 |
| D5-10 Information gain beyond Rust | PASS | Domain is genuinely different and would test whether the architecture survives outside software. |
| D5-11 Firewall compliance | PASS in principle | A valid protocol can prohibit fitness, treatment outcome, later observations and predictive labels from Pτ. |
| D5-12 Falsifiability | PASS | A non-trivial independent Pτ could be falsified by showing that accessibility cannot be identified without outcome leakage. |

## 4. Decision

**PROTEIN EVOLUTION IS NOT CURRENTLY EXECUTION-READY.**

The blocker is not data availability. The blocker is **independent non-trivial admissibility**.

Two alternatives were considered and both are inadequate:

1. `Pτ = 1` for every point mutation. This is non-circular but makes `T_acc` essentially the complete mutational neighbourhood, providing insufficient evidence for a meaningful TGCV accessibility predicate.
2. `Pτ` based on measured fitness, treatment response, observed future mutations or experimentally observed evolutionary success. This creates outcome leakage and violates the pre-execution accessibility requirement.

A future protein experiment would therefore require a separately frozen mechanistic admissibility model — for example, a structural/biophysical constraint system — whose rules are specified independently of the longitudinal outcomes and whose assumptions are themselves auditable.

## 5. Scientific consequence

This audit strengthens rather than weakens the methodological result: **a public longitudinal dataset is not sufficient for a TGCV empirical test.** The decisive requirement is independent identifiability of `Uτ` and non-circular `Pτ`.

Rust currently remains the only empirical domain with a closed operationalization and completed primary/replay execution supporting bounded E1 claims.

Current claim status remains:
- Rust bounded structural distinction: E1.
- Domain independence: H.
- Causality: H.
- Predictive superiority: H.
- Value linkage: H.
- Universal validity: H.
- Originality/no equivalent prior architecture: O.

## 6. Next controlled operation

Open **D-OPS-6 — Cross-Domain Discovery Search II**, but with a stricter filter:

> Search only for domains where the admissibility predicate can be specified from an independently governed rule system or mechanistic constraint set, rather than inferred from observed behaviour, fitness, outcomes or future states.

Priority should therefore shift toward domains with explicit rule systems, formal constraints, engineering feasibility rules, or independently documented transition laws.

**REAL-DATA EXECUTION AUTHORIZED: NO.**
