# TGCV C10-C — C10C-001 Structural Reconstruction Protocol 001

## Status

`FROZEN — PRE-EXECUTION STRUCTURAL RECONSTRUCTION PROTOCOL`

## Purpose

Define the controlled reconstruction required to determine whether the frozen C10C-001 replication archive supports an ex-ante, outcome-independent operationalization of:

- `S_0` / pre-intervention state;
- `S_1` / post-intervention state;
- `T_acc,0` / accessible transformations before the intervention;
- `T_acc,1` / accessible transformations after the intervention;
- `ΔT_acc` / change in accessible transformation space.

This protocol does **not** authorize causal estimation, replication of published estimates, or claim-level upgrade.

## Source boundary

The source is the frozen C10C-001 archive recorded in:

`00_GOVERNANCE/SIP/TGCV_C10C001_SOURCE_VERSION_FREEZE_001.md`

Source DOI: `10.7910/DVN/QOGMVI`  
Archive: `JPAL_3813.zip`  
Archive SHA-256: `B528F933BD72022AD16F320C55FEB20DB8B410AB2C5816137D0DAD7061A73AB5`

The archive and its member hashes are frozen. The replication `.do` files may be inspected but must not be executed under this protocol.

## Reconstruction principle

The reconstruction MUST distinguish:

`observed configuration` ≠ `candidate transformation` ≠ `accessible transformation`.

Absence of an observed configuration MUST NOT by itself be interpreted as inaccessibility.

A transformation may enter `T_acc` only when its admissibility/accessibility predicate is independently defined from information available at the relevant pre-outcome state boundary.

Downstream outcomes MUST NOT be used to define either `T_acc,0` or `T_acc,1`.

## Candidate state representation

The inspected replication code exposes the following potentially relevant state dimensions:

- `thread_quantity`
- `difficulty_control`
- `product_type`
- `colors_no`
- `luxs_or_sha3by`
- `thread_type`
- baseline production/productivity variables
- baseline quality measures
- treatment/takeup status where temporally admissible
- experiment/stratum identifiers
- other documented baseline controls

These variables are candidate state descriptors only. Their admission to `S_0` or `S_1` requires variable-level provenance and temporal validation.

## Candidate transformation representation

The replication code constructs `productgroup` from:

`thread_quantity × difficulty_control × product_type × colors_no × luxs_or_sha3by × thread_type`

and repeatedly uses this grouping as a fixed-effect structure.

For TGCV reconstruction, this grouping is treated only as a **candidate transformation identity space**. It is not automatically accepted as `T_acc`.

A candidate transformation identity `τ` must be represented independently of the outcome attached to the resulting observation.

## Required reconstruction objects

### A. Candidate universe `U_τ`

Construct the finite candidate universe from explicitly documented transformation-defining dimensions. Record:

1. dimensions;
2. coding/categories;
3. missing-value treatment;
4. whether categories are pre-intervention observable;
5. whether a category combination represents a transformation identity or merely a descriptive state.

### B. Pre-state `S_0`

Freeze the variables and observation boundary used to characterize the system immediately before treatment exposure.

### C. Post-state `S_1`

Freeze the corresponding post-intervention state boundary without using downstream economic outcomes to define the state.

### D. Accessibility predicate `P_τ`

For every candidate transformation, define the rule determining whether `τ` is admissible/accessibly realizable from the relevant state/context.

The predicate must be:

- ex-ante relative to the outcome being tested;
- reproducible from frozen source data;
- independent of treatment-effect estimates;
- independent of published outcome rankings;
- explicit about missing/unobserved combinations.

### E. `T_acc,0` and `T_acc,1`

Enumerate the candidate transformations satisfying the frozen predicate at each state boundary.

### F. `ΔT_acc`

Record additions, removals and unchanged transformations separately:

`opened = T_acc,1 \ T_acc,0`

`closed = T_acc,0 \ T_acc,1`

`ΔT_acc = (opened, closed)`

A scalar net cardinality is insufficient as the primary representation.

## Required anti-leakage checks

The reconstruction MUST fail/stop if any of the following is detected:

1. post-outcome variables are used to define pre-treatment accessibility;
2. treatment assignment is used as an implicit accessibility predicate without explicit justification;
3. takeup is substituted for accessibility;
4. observed product combinations are treated as exhaustive evidence of accessibility;
5. outcome magnitude is used to select transformation identities;
6. transformations are defined only after inspecting estimated treatment effects;
7. missing observations are silently coded as inaccessible;
8. a published regression specification is treated as the TGCV structural definition without independent reconstruction.

## Evidence classification

Possible outcomes of the reconstruction:

- `PASS — BOUNDED STRUCTURAL RECONSTRUCTION`: both `T_acc,0` and `T_acc,1` are reproducibly defined under an explicit predicate and `ΔT_acc` is identifiable within the frozen universe;
- `PARTIAL — STRUCTURAL RECONSTRUCTION`: a bounded subset is reconstructable but one or more dimensions remain unresolved;
- `FAIL — INSUFFICIENT STRUCTURAL OBSERVABILITY`: the archive does not support an outcome-independent accessibility reconstruction;
- `BLOCKED — INFRASTRUCTURE`: the required frozen source cannot be inspected/extracted under the controlled environment.

No outcome in this protocol by itself upgrades C02, C07, C08, C09, C10, C11 or C16.

## Execution sequence

1. Extract the frozen archive into a separate inspection directory.
2. Verify archive/member hashes against the frozen source record.
3. Inspect README and data dictionaries/documentation.
4. Inspect variable metadata in the Stata datasets without running replication `.do` files.
5. Identify all candidate transformation dimensions and their temporal availability.
6. Construct and freeze `U_τ`.
7. Define candidate `P_τ` rules using only pre-outcome information.
8. Reconstruct `T_acc,0` and `T_acc,1`.
9. Produce `opened`, `closed`, and bounded `ΔT_acc`.
10. Run anti-leakage and missingness checks.
11. Record the reconstruction result in a separate result artifact.
12. Only after structural closure, decide whether the protocol permits a subsequent causal/outcome linkage stage.

## Explicit non-authorizations

This protocol does not authorize:

- execution of `Replication_File.do`;
- execution of `Replication_File_Appendix.do`;
- reproduction of published regression tables;
- estimation of treatment effects;
- selection of transformations using outcome results;
- value estimation;
- modification of the TGCV Core;
- claim-level upgrade;
- reopening of C09 or previously closed tests.

## Current assessment

Based on non-executing inspection of the replication code supplied for C10C-001, the archive appears to contain a potentially sufficient set of structural dimensions for a bounded reconstruction. This remains a **candidate feasibility assessment**, not a structural result.

The next authorized action is controlled extraction and metadata/data inspection within this protocol.
