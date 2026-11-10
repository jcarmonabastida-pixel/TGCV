# C10-S — AB residual input and closure ledger

**ID:** C10-S-AB-RESIDUAL-LEDGER-001  
**Version:** Draft 001  
**Date:** 2026-11-10  
**Branch:** `research/c10-s-consolidation-draft`  
**Status:** INTEGRATED WORKING LEDGER / NOT APPROVED AS DESIGN FREEZE / NOT IMPLEMENTABLE.  
**Authority:** DEC-C10-093 and DEC-C10-094; master C10-S §§216–233; accepted DEC-C10-068/069/071–079/090–092; D2 policy DEC-C10-066/067.  
**Purpose:** identify, in one place, which AB requirements are resolved at the documentary-design level, which remain material inputs, what evidence would close them, and which inputs must transfer to C. This ledger does not create a new scientific decision or replace the governing contracts.

## 1. Governing interpretation

AB-01…AB-09 are one integrated package, not nine independent redesign exercises. DEC-C10-093 accepts the working specialization baseline; DEC-C10-094 accepts the integrated material design resolutions. These decisions settle the conceptual choices within their scope. They do **not** establish that the relevant inventories, snapshots, policies, probabilities, routes, oracle or evidence exist in a materialized instance.

Use the following status vocabulary:

- **DESIGN RESOLVED:** the documentary rule/architecture is accepted; no conceptual reopening absent a documented contradiction.
- **MATERIAL INPUT OPEN:** the design specifies what must be supplied, but the actual value, instance, source or evidence is missing.
- **EVIDENCE GATE OPEN:** a claim such as completeness, isolation, invariance, independence or correctness requires evidence not yet present.
- **TRANSFER TO C:** the input is handed to the causal/measurement/statistical package; AB retains its source identity, version, definition and uncertainty.
- **NOT AUTHORIZED:** no executable fixture, parser, validator, code, simulation or experiment is authorized by this ledger.

A design-resolved row is not IMPLEMENTED, EXECUTED, AUDITED or ACCEPTED as an empirical result.

## 2. Integrated AB-01…AB-09 disposition

| Gate | Accepted documentary resolution | Remaining material input / evidence | Closure evidence and acceptance rule | Handoff |
|---|---|---|---|---|
| **AB-01 — CMP/PAR/REF/RUL/MET roster** | Reference identity is fixed by DEC-C10-069. Logical nucleus: one CMP, ENABLED and PROFILE PARs, one REQUIRE RUL, two semantically mandatory typed operand bindings, MET mandatory; POL outside minimal confirmatory nucleus. REF objects are not inferred from UDG references, FKs or EDGE. | Snapshot-scoped physical roster; whether the two operand bindings serialize as typed REF objects or AST links; IAM applicability/cardinality rows; exact record identities and coverage denominators. | Reconcile the governing accepted AST profile/grammar with DEC-C10-076/077/078; represent each operand relation exactly once; enumerate all applicable rows by stage, route and snapshot; prove coverage. REF=0 only if exhaustive inventory and IAM support it. | C receives frozen roster IDs, snapshot bindings, applicability and UNKNOWN/coverage status. |
| **AB-02 — C_src/C_dst/M, states and IAM** | ENABLED is BOOL without coercion. PROFILE mapping is total/injective over the accepted finite symbols: STD→STANDARD, RO→READ_ONLY, OFF→DISABLED. Preserve ABSENT/NULL/DEFAULT/VALUE distinctions. IAM is a logical, layered applicability contract. | Physical source/destination schemas and namespaces; canonical serialization for configuration payloads; resolved DEFAULT semantics; complete IAM rows/cardinalities; actual source/destination values and mapping coverage. | Every mandatory field has an explicit typed mapping or explicit failure/NA rule; no implicit defaults, lossy collapse or orphan references. Apply JCS only within DEC-C10-074's accepted UDG-01 envelope scope; do not extend it automatically to configuration payloads. | C receives versioned M, states, mapping statuses and measurement error/unknowns. |
| **AB-03 — F1/F2/A1/A2 and transformation identity** | Route roles and composition are accepted: F1→F2 focal, A1→A2 baseline alternative; B does not execute any route. DEC-C10-090/091/092 separate endpoint/interface/service, format/payload/events and A2 capability/implementation/execution. | Concrete transformation TID/SID/RID, versions, actors, artifacts, source/destination formats, pre/postconditions, dependencies, windows, errors, reversibility and route-specific event contracts. | Four versioned cards must be mutually compatible with the same source, destination, C0/G/H, mapping, IAM and F*. No alias or conceptual capability is treated as an observed/implemented transformation. | C receives route/version identities and any common-support or route-comparability limits. |
| **AB-04 — ID/REL/COND/AUTH/RES/DEP/BLOCK** | Predicate families, trivalent logic and distinction between focal DEP and alternative routes are specified. C_dep is not A_f; A_f is not execution or success. Functional authorization, technical ACL/credentials and agent knowledge remain distinct. | Field-level operationalization by unit, stage, route and snapshot; actual evidence sources; resource/capacity values; endpoint/dependency topology; authorization truth; coverage and adjudication. | Each applicable predicate has a definition, unit, time, domain, truth rule, observable evidence, coverage denominator and adjudication rule. Missing evidence propagates ?; it is not 0 or NA. | C receives independently measured A_f/D_f/ΔT_acc and their observation status, not inferred values. |
| **AB-05 — F*, C0, G, H and oracle** | F* is common and non-compensatory across both routes; FP-01…07 are functional, FP-08 is a separate evidence gate. G is the complete logical service unit/accepted roster. C0 is a pre-Z/pre-B immutable baseline with the fields enumerated in DEC-C10-094. | Atomic FP property profile and applicability; concrete C0 snapshot; H* anchor, value and unit; common tolerances/windows where relevant; oracle implementation-independent specification, validation evidence, blinding feasibility and adjudication record. | All required properties have ex-ante rules; same F* and H apply to F/A; any FP-01…07 failure yields F*=0, unresolved required property yields ?, all required properties=1 yields F*=1. FP-08 cannot alter F*. Oracle must be route/outcome-independent and versioned before fixtures. | C receives outcome-independent F* and event timing; H and measurement limitations enter estimand definitions. |
| **AB-06 — D2 policy/event mechanism** | D2 assignment policy is accepted. Z, B assignment, programming, receipt, compliance, attempt, actor, artifact/version, installation, retries, partial failure, rollback, background provision and crossover are distinct events. B does not execute F1/F2/A1/A2. | Actual actor/role, adapter artifact/version/hash, receipt protocol, time window, retry/failure/rollback rules, background-provision detection and material event evidence. | Event log must preserve the entire sequence and deviations; Z=1 must not be equated with receipt/attempt/success; Z=0 must not be equated with no background provision. | C receives the complete assignment/receipt/attempt/install event history and policy versions. |
| **AB-07 — joint technical distribution** | C_dep* is the conjunction of installation, integrity, compatibility and operability. A conditional joint distribution (16 cells per relevant stratum or validated equivalent) is required; independence and s=.80 are not assumed. | Numerical joint probabilities by arm/history/stratum, structural zeros if any, calibration rationale or explicit synthetic stipulation, sensitivity ranges and parameter provenance. | Distribution normalized; each cell in [0,1]; margins and conditional dependencies reported; sensitivity justified; no historical .20/.80 or s=.80 inserted as fact. | Transfer full joint distribution and sensitivity scenarios to C; retain AB source/version. |
| **AB-08 — eligibility, q_X*, units and interference** | Eligibility uses C0 pre-Z variables only. P*_τ2, P*_F and q_X* are distinct. Assignment, analysis and interference units are separate. Shared infrastructure requires cluster/exposure modelling, not assumed independence. | Executable-in-principle eligibility algorithm (documentary first), target population and strata, q_X* distribution/weights, positivity/support table, assignment/analysis/cluster topology and exposure mapping. | Reproducible pre-Z rule; no post-Z exclusions; common support explicitly enumerated; unsupported cells not extrapolated silently; interference unit matches shared resources/dependencies. | Direct transfer to C with population, support, cluster and q_X* version. |
| **AB-09 — alternatives, R0–R3 and truth/observed** | Alternative-route logic, finite-universe coverage rule, R0–R3 reuse, truth/observed separation and Generator/Analyzer/Evaluator separation are specified. Reach=0 requires exhaustive coverage; otherwise ?. | Material alternative universe and route inventory; scenario truth tables; measurement/missingness process; oracle validation, blinding and adjudication; Analyzer firewall proof. | Truth and observed datasets remain separate; no scenario labels or truth leak to Analyzer; each 1/0/? generated from explicit rules; no absence from missing records; R0/R1/R2/R3 classifications have declared universe and evidence. | C receives truth-sealed DGP scenario metadata only through Evaluator; Analyzer receives observed variables. |

## 3. Cross-gate dependencies and no-double-counting rules

1. **AB-01 ↔ AB-02:** the roster and mapping must use the same object/record identities, version and snapshot. An AST operand link is not counted again as a REF object; a UDG reference or U_G FK is not a configuration REF by default.
2. **AB-02 ↔ AB-03:** M maps declared source/intermediate/destination semantics; it does not itself prove F1/F2/A1/A2 execution or applied state.
3. **AB-03 ↔ AB-04:** route existence/capability does not prove predicate satisfaction. DEP is focal-route dependency, not proof that no A1/A2 route exists.
4. **AB-04 ↔ AB-05:** A_f* is adjudicated from its necessary predicates; F* is the separate functional endpoint for the complete route. Neither is inferred from C_dep* alone.
5. **AB-05 ↔ AB-06:** B cannot alter the oracle, F*, C0, IAM, permissions or baseline conditions under the isolated D2 design. Any observed change is a collateral path, not silently absorbed into the focal mechanism.
6. **AB-06 ↔ AB-07:** the joint C_dep distribution is conditional on the actual event mechanism; it cannot be reduced to one “success rate” without a justified factorization.
7. **AB-07 ↔ AB-08:** technical success and accessibility may vary with baseline history/strata; marginal probabilities do not establish positivity or transport.
8. **AB-08 ↔ AB-09:** alternative-route truth and Reach depend on the closed universe, population, horizon and coverage. An unknown route keeps the relevant absence/Reach result unknown.
9. **All gates ↔ C:** preserve the distinction among ITT_Z(D2), package effect, first stages, LATE_f, θ_Af(q_X*), θ_A(q), and mediation. No AB result licenses causal attribution to ΔT_acc→Value.

## 4. Material input register — no invented defaults

The following are the current hard blockers. Each requires a sourced value, explicit synthetic stipulation, or justified NOT_APPLICABLE decision; absence of input is not permission to choose a conventional default.

| Input ID | Required input | Current status | Permitted resolution |
|---|---|---|---|
| AB-M01 | REF versus AST physical representation | OPEN | Grammar/schema reconciliation; choose one encoding per operand, never both |
| AB-M02 | C_src/C_dst/M physical schema and canonicalization | OPEN | Explicit schema/encoding decision; do not extend UDG-01 JCS by assumption |
| AB-M03 | TID/SID/RID and concrete transformation cards | OPEN | Source-backed identity/version contracts or explicitly bounded synthetic specification |
| AB-M04 | Predicate field roster and source/capture method | OPEN | Field-by-field mapping to U/R/C/X/E_T and evidence coverage |
| AB-M05 | H* common anchor, value and unit | OPEN | Explicit pre-specified protocol decision; same for F and A |
| AB-M06 | MD-C1/MD-C4 isolation and A1/A2 non-affectation | OPEN | Material manifests, before/after snapshots and functional equivalence evidence |
| AB-M07 | D2 event probabilities and joint C_dep distribution | OPEN | Calibration or explicit DGP stipulation plus sensitivity; no inherited .20/.80 or .80 |
| AB-M08 | Eligibility algorithm, q_X*, support and strata | OPEN | C0-only algorithm and explicit population distribution/support |
| AB-M09 | Assignment/analysis/interference units | OPEN | Topology-backed cluster/exposure definition |
| AB-M10 | Independent oracle, blinding and adjudication | OPEN | Pre-fixture versioned specification and validation plan/evidence |
| AB-M11 | R0–R3 truth tables and observation/missingness model | OPEN | Scenario-by-scenario truth and observation rules; keep truth sealed |

## 5. Handoff contract AB → C

C must consume, not recreate, the AB outputs below with their exact IDs and versions:

- instance/roster/M/IAM/C0/G/H and snapshot identities;
- transformation cards and route universe;
- predicate definitions and independent A_f/D_f/ΔT_acc measurement contracts;
- D2 event history and joint C_dep distribution;
- eligibility, population, q_X*, support and interference structure;
- R0–R3 truth/observed scenario definitions and oracle/adjudication provenance.

Any unresolved AB field enters C as OPEN/UNKNOWN with its source and scope. C may perform sensitivity or partial-identification analysis around it, but may not silently fill it.

## 6. Next integrated operation

The next operation remains within AB and should resolve, in one coordinated pass, the highest-dependency documentary items before requesting unavailable material values:

1. reconcile AB-M01/02 against the current accepted AST, REF, UDG and mapping contracts, including the limited scope of DEC-C10-074;
2. consolidate the four transformation cards and their source/destination contracts without inventing TID/SID/RID;
3. complete the predicate-to-field/evidence crosswalk for AB-04;
4. prepare the exact minimal decision set for H*, MD-C1/MD-C4, D2 joint probabilities, q_X*/population and cluster topology.

Only after this pass should remaining user decisions or external material inputs be requested. No implementation is implied.

## 7. Authorization and status

AB remains **IN_PROGRESS / DESIGN RESOLVED IN PART / MATERIAL INPUTS AND EVIDENCE OPEN**. This ledger is a documentary reconciliation, not Design Freeze, not implementation readiness and not scientific evidence.

`scientific_execution=false`; `execution_authorized=false`.

No code, parser, validator, executable fixture, simulation or experiment is created or authorized by this ledger.
