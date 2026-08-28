# EXT-1.1 Rust — Current Experimental Baseline v0.1

**Status:** WORKING BASELINE — NOT FROZEN
**Purpose:** Establish the current executable decision boundary for EXT-1.1 while preserving historical provenance and preventing circular reconstruction.

## 1. Governance rule

Historical MVE/EMP records are evidence, not automatically the current executable specification. Where records conflict, the historical facts remain preserved and the current experiment adopts an explicitly versioned decision.

## 2. Research role

EXT-1.1 is an external/domain replication-oriented experiment for testing whether the structure of accessible transformations contains predictive information beyond a conventional baseline representation.

It is not permitted to silently reinterpret historical EMP-1.1 results as Rust results.

## 3. Current status by element

| Element | Status | Source / treatment |
|---|---|---|
| Scientific question | RECOVERED | TGCV current research architecture |
| Core object `T_acc` | RECOVERED | MVE semantic specification |
| Candidate families | RECOVERED | six-family inventory |
| Candidate schema | RECOVERED | `<id,class,target,pre,resource,eff>` |
| Accessibility form | RECOVERED | `Pre ∧ Target ∧ Resource` |
| Baseline B | RECOVERED | component count + 3 resources + objective identity |
| R | RECOVERED | accessible IDs + cardinality |
| Rust domain | NEW DECISION | chosen external domain for EXT-1.1 |
| Rust observational unit | OPEN | must be frozen before data acquisition |
| Concrete candidate universe T | OPEN | domain-specific instantiation required |
| Rust accessibility predicate | OPEN | operationalization required |
| Outcome | OPEN | must be pre-declared |
| Pilot size / seed | OPEN | TR-181E decision required |
| Dataset | OPEN | no canonical dataset frozen |

## 4. Historical inconsistencies / continuity notes

Known historical records contain changing terminology, provisional candidate inventories, and interrupted analysis sessions. These are not overwritten. The current baseline supersedes them operationally only when a new decision is explicitly recorded.

## 5. New decisions required for EXT-1.1

The following may legitimately be decided anew:

1. exact Rust observational unit;
2. admissible transformation families/instances in Rust;
3. operational meaning of component presence, activation, composition, reconfiguration, acquisition, learning and recombination in Rust;
4. resource variables and thresholds;
5. pre-outcome accessibility rules;
6. outcome variable and observation horizon;
7. sampling and exclusions;
8. pilot sample size and seed;
9. baseline feature encoding;
10. R serialization.

Every such decision must receive a decision-record identifier and must be frozen before confirmatory data are opened.

## 6. Decision hierarchy

1. Canonical historical fact is preserved.
2. Explicit later decision governs the current experiment where applicable.
3. Unresolved inconsistency triggers a decision record.
4. New experimental choices are permitted only when necessary for execution and must be labelled NEW DECISION.
5. No new choice may be presented as historical MVE fact.

## 7. Freeze gate

EXT-1.1 cannot be declared frozen until every executable-path field is one of RECOVERED, DERIVED or NEW DECISION with a recorded rationale, and no OPEN/NOT RECOVERED dependency remains.

## 8. Current decision

**Baseline v0.1:** accepted as the working control document.

**Scientific freeze:** NO-GO.

**Next action:** create decision records for the open Rust operationalisation fields, then freeze the complete candidate universe and accessibility predicate before dataset acquisition/analysis.
