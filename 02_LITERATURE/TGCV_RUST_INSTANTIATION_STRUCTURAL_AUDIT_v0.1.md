# TGCV — Rust Instantiation Structural Audit v0.1

**Status:** CONDITIONAL PASS — STRUCTURAL FEASIBILITY ESTABLISHED; SEMANTIC VALIDATION OPEN  
**Date:** 2026-09-07  
**Phase:** Domain instantiation and empirical validation preparation

## 1. Purpose

Audit whether the Rust data and previously established structural infrastructure can support the newly frozen TGCV Rust instantiation contract, without using any outcome, predictive model, or post-origin result to validate present accessibility.

This audit is deliberately conservative: prior EXT-1.1 evidence may establish technical feasibility, but it cannot silently establish the new TGCV semantic contract.

## 2. Evidence boundary

The audit uses two existing structural evidence records from the frozen Rust work:

- DR-020 candidate-universe audit;
- DR-026A T_acc representation audit.

DR-020 independently constructed a candidate universe from 91,437 packages, 607,498 versions and 3,618,523 dependency rows, yielding 194,371,905 unique candidates with zero future-timestamp violations and no use of the resolver for candidate membership. fileciteturn222file0L2-L7

DR-026A reconstructed a canonical relational T_acc representation for all 607,498 origins, preserving 114,626 empty origins and 421,044 unresolved edges, with no future targets, deterministic serialization, row-order invariance and no outcome/post-origin/model inputs. fileciteturn223file0L2-L7

These records establish structural feasibility and reproducibility of the underlying data operations. They do **not** by themselves prove that the newly specified Rust `τ` and `P_τ` semantics are the correct TGCV instantiation.

## 3. Audit matrix

| Audit item | Result | Basis / limitation |
|---|---|---|
| RA-1 unit identity | PASS | package-version identity already canonicalized |
| RA-2 transformation identity | CONDITIONAL PASS | tuple `(origin_version_id,target_package_id,target_version_id)` is independently identifiable; adequacy as TGCV transformation remains open |
| RA-3 independent U_tau | PASS | DR-020 construction is independent of accessibility and outcome |
| RA-4 candidate uniqueness | PASS | 194,371,905 unique candidate keys; zero duplicates |
| RA-5 temporal validity | PASS | zero future timestamp violations in candidate universe |
| RA-6 non-circular candidate construction | PASS | resolver/accessibility excluded from candidate construction |
| RA-7 P_tau non-circularity | CONDITIONAL PASS | structural separation demonstrated, but new dependency-resolution semantics still require explicit freeze |
| RA-8 membership-level T_acc | PASS | canonical relational representation demonstrated in DR-026A |
| RA-9 empty T_acc | PASS | 114,626 empty origins preserved |
| RA-10 unresolved handling | PASS | 421,044 unresolved edges explicitly retained |
| RA-11 future-target exclusion | PASS | no future targets in audited T_acc |
| RA-12 deterministic serialization | PASS | canonical ordering and deterministic representation established |
| RA-13 row-order invariance | PASS | set semantics plus permutation smoke test established |
| RA-14 accessibility/execution separation | CONDITIONAL PASS | no execution used in structural construction; direct empirical observation of accessible-but-unexecuted cases not yet established |
| RA-15 outcome/value exclusion | PASS | audits explicitly excluded outcome/model information |
| RA-16 Reach/Trajectory separation | OPEN | not reconstructed in these Rust audits |
| RA-17 temporal T_acc,t / T_acc,t+1 reconstruction | OPEN | prior audit establishes one origin-time representation, not the new paired temporal protocol |
| RA-18 EXT-1.1 semantic independence | PASS | new contract explicitly rejects automatic inheritance of old outcome/model/features/window |
| RA-19 provenance | PASS | source dataset and audit implementations are recorded |
| RA-20 reproducibility | PASS | DR-020 and DR-026A provide repeatability evidence |

## 4. Critical findings

### 4.1 Independent candidate universe — established

The Rust ecosystem can support an independently constructed candidate universe. DR-020 demonstrates deterministic candidate generation, canonical identity, temporal filtering and separation from resolver/accessibility and outcome information. fileciteturn222file0L2-L7

### 4.2 Membership-level T_acc — established structurally

DR-026A demonstrates that a canonical relational accessible-transformation representation can be constructed at scale, including empty sets, unresolved edges, deterministic ordering and future-target exclusion. fileciteturn223file0L2-L7

### 4.3 New semantic contract is not yet fully audited

The newly specified Rust contract defines accessibility as permission under frozen dependency-resolution semantics at the origin time. The existing DR-026A evidence establishes resolver-faithful structural construction under the prior EXT-1.1 protocol, but the new TGCV contract has intentionally not yet frozen the exact dependency-resolution grammar, precedence rules, observation pairing and temporal window.

Therefore the audit cannot legitimately mark the new `P_tau` semantics or `ΔT_acc` temporal comparison as fully validated.

### 4.4 Temporal reconstruction remains the main structural gap

The previous evidence establishes `T_acc` at the origin level, but the new TGCV instantiation requires reconstruction under identical rules at two defined observation points and a frozen change operator:

`T_acc,t → T_acc,t+1 → ΔT_acc`.

That paired construction has not yet been executed under the new contract and must remain outcome-blind.

### 4.5 Reach and Trajectory are intentionally outside this audit

The Rust instantiation contract preserves `Reach` and `Trajectory` as distinct objects, but no Rust-specific reconstruction has yet been performed. This is not a failure of the current representation contract; it is a subsequent operationalization requirement.

## 5. Falsifier status

**RF-1:** not triggered; candidate transformation identity is independently representable.

**RF-2:** not triggered; candidate universe construction is independent.

**RF-3:** not yet testable conclusively; exact new resolver semantics remain to be frozen.

**RF-4:** not triggered structurally; accessibility construction is separated from execution, but the new predicate semantics remain open.

**RF-5:** not triggered; membership-level T_acc representation is feasible.

**RF-6:** not yet testable conclusively; new paired temporal ΔT_acc reconstruction remains open.

**RF-7:** not triggered; unresolved relations are explicitly represented.

**RF-8:** not triggered; the new specification explicitly prevents automatic inheritance of EXT-1.1 as universal representation.

**RF-9:** conditional; structural data permit separation, but accessible-but-unexecuted empirical cases must be demonstrated where the data support them.

**RF-10:** not triggered; reproducibility and provenance evidence are available.

## 6. Gate criteria

| Criterion | Result |
|---|---|
| RSA-G1 | Unit identity operationally identifiable — PASS |
| RSA-G2 | Independent candidate universe constructible — PASS |
| RSA-G3 | Candidate identity unique — PASS |
| RSA-G4 | Temporal candidate validity — PASS |
| RSA-G5 | Accessibility structurally separated from candidate existence — PASS |
| RSA-G6 | Membership-level T_acc reconstructable — PASS |
| RSA-G7 | Empty/unresolved cases preserved — PASS |
| RSA-G8 | Deterministic/reproducible construction — PASS |
| RSA-G9 | Outcome/post-origin leakage excluded — PASS |
| RSA-G10 | New P_tau semantics fully frozen and audited — NOT YET |
| RSA-G11 | Paired T_acc,t / T_acc,t+1 reconstruction audited — NOT YET |
| RSA-G12 | ΔT_acc classification audited — NOT YET |
| RSA-G13 | Reach/Trajectory reconstructed — NOT YET |
| RSA-G14 | Accessibility/execution distinction empirically demonstrated — NOT YET |
| RSA-G15 | EXT-1.1 inheritance firewall preserved — PASS |

## 7. Audit decision

**CONDITIONAL PASS — RUST DATA ARE STRUCTURALLY SUITABLE FOR TGCV INSTANTIATION, BUT THE NEW SEMANTIC AND TEMPORAL CONTRACT IS NOT YET FULLY VALIDATED.**

This is the strongest conclusion justified by the current evidence. A full PASS would improperly convert prior EXT-1.1 structural evidence into validation of the newly specified TGCV semantics.

## 8. Scientific consequence

Rust remains the selected first empirical domain.

The current evidence supports the proposition:

> The Rust ecosystem contains sufficient longitudinal and relational structure to attempt a TGCV reconstruction of candidate transformations, accessibility and accessible-transformation membership at scale.

It does **not** yet support the stronger proposition:

> The newly specified Rust `P_tau` and `ΔT_acc` operational definitions are fully valid and empirically identifiable.

That stronger proposition remains falsifiable and must be tested before any outcome/model protocol is specified.

## 9. Immediate next controlled operation

**TGCV Rust Accessibility Semantics Freeze Gate v0.1**.

That Gate must freeze, before any new outcome is inspected:

1. exact dependency requirement grammar;
2. version-range semantics;
3. resolver precedence and admissibility rules;
4. treatment of yanked/deleted/unresolved versions;
5. origin-time information boundary;
6. candidate temporal rule;
7. exact observation pairing `t → t+1`;
8. exact `ΔT_acc` comparison operator;
9. deterministic canonicalization;
10. treatment of empty and unresolved cases.

Only after this semantics freeze may the paired temporal structural audit be executed.

## 10. Integrity lock

No outcome, model, predictive feature set, value measure or hypothesis may be selected from this audit. No post-hoc interpretation of EXT-1.1 may be used to alter the frozen Rust semantics.
