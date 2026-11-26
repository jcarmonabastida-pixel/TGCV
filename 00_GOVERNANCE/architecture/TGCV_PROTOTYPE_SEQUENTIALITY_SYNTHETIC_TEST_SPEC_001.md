# Synthetic acceptance-test specification — sequentiality profile proposal 001

- **Status:** TEST DESIGN PROPOSAL; not implemented or executed.
- **Date:** 2026-10-14.
- **Depends on:** TGCV_PROTOTYPE_INTERACTIVE_SEQUENTIALITY_CONTRACT_001.md and TGCV_PROTOTYPE_SEQUENTIALITY_RECONCILIATION_MATRIX_001.md.
- **Purpose:** define small, hand-checkable fixtures before changing the engine. Existing profile-1/profile-2 behavior must remain unchanged.

## 1. Proposed temporal rule

Proposed profile name: `temporal_prerequisite_graph`, version `1`.

Proposed relation shape:
- `id`: stable relation ID;
- `type`: `requires_prior_execution`;
- `transition_id`: transition whose applicability is constrained;
- `requires_transition_id`: transition that must already have occurred.

At a sequence prefix ending in state s, transition t is applicable only if:
1. the current state equals t.source;
2. t is not disabled in the active scenario;
3. for every temporal prerequisite relation targeting t, the required transition ID appears at least once among the transitions earlier in this **same sequence prefix**;
4. all other rules in the selected profile are satisfied.

A transition does not satisfy its own prerequisite at the instant it is being checked. Occurrences in a different scenario, a different explored path, a prior run, or the model declaration do not count. This is a proposed profile rule, not a modification of profile 2 or of TGCV's scientific Core.

## 2. Shared base fixture

States: A, B, C, D.

Initial state: A.

Transitions:
- `t_prep`: A → B
- `t_bypass`: A → C
- `t_to_c`: B → C
- `t_use`: C → D

Temporal relation:
- `r_use_requires_prep`: `t_use` requires prior execution of `t_prep`.

No transitions are disabled. Max depth and trajectory count are set high enough that no fixture below is truncated.

## 3. Required tests

### TSEQ-001 — ordered valid sequence

Sequence:
A —t_prep→ B —t_to_c→ C —t_use→ D

Expected:
- valid;
- exact transition order: [t_prep, t_to_c, t_use];
- exact state order: [A, B, C, D];
- t_use is applicable because t_prep occurred earlier in this same sequence.

### TSEQ-002 — prerequisite not present in sequence prefix

Attempted sequence:
A —t_bypass→ C —t_use→ D

Expected:
- t_bypass is applicable;
- t_use is blocked at step index 2 (1-based);
- failure reason identifies unmet prerequisite t_prep for t_use;
- no valid trajectory includes the blocked t_use step;
- the model and scenario remain unchanged.

### TSEQ-003 — declaration is not execution

Input contains t_prep and the relation, but the sequence is A —t_bypass→ C.

Expected:
- the mere presence of t_prep in the model does not satisfy the relation;
- no execution record is created for t_prep;
- no t_use step is implied.

### TSEQ-004 — scenario-local disablement

Create an intervention disabling t_prep.

Expected:
- baseline and intervention have separate immutable configuration records;
- the baseline valid sequence in TSEQ-001 remains reproducible;
- under intervention, t_prep cannot execute and the TSEQ-001 sequence is not valid;
- the base transition definition is not deleted or mutated;
- no temporal prerequisite is satisfied by a disabled/unexecuted t_prep.

### TSEQ-005 — prerequisite is path-local

Compare these prefixes ending at C:
- prefix 1: A —t_prep→ B —t_to_c→ C
- prefix 2: A —t_bypass→ C

Expected:
- t_use is applicable after prefix 1;
- t_use is blocked after prefix 2;
- shared current state C alone is insufficient to merge the two histories for temporal-rule evaluation.

### TSEQ-006 — repeatability and canonical sequence record

Run the same model, scenario, profile version, initial state, exploration limits and engine version twice.

Expected:
- same ordered possible-sequence results and same canonical semantic result hash;
- each invocation has a distinct run identifier/metadata record;
- timestamps/run IDs may differ and must not be mistaken for scientific output differences;
- the full configuration needed for replay is retained.

### TSEQ-007 — possible versus executed

Explore the base fixture without selecting a concrete execution.

Expected:
- possible-sequence results may include the valid path through t_prep;
- no concrete execution trace is created merely by enumeration.

Then select and execute A —t_prep→ B —t_to_c→ C —t_use→ D.

Expected:
- one concrete trace records the actual ordered steps;
- the trace points to the exact model/scenario/profile snapshot;
- the exploration result and execution trace have different record types.

### TSEQ-008 — descriptive relation is inert

Add a relation explicitly marked descriptive that does not belong to the temporal rule profile.

Expected:
- possible sequences and concrete execution semantics remain identical;
- any canonical input hash may differ because the input metadata differs, but the canonical semantic output must remain equal;
- do not conflate input hash equality with semantic output equality.

### TSEQ-009 — truncation is not completeness

Set the maximum depth so the valid path can only be partially explored, or set a trajectory cap that leaves unexplored alternatives.

Expected:
- result marks exploration as truncated according to the engine's documented exact-boundary rules;
- the UI does not present discovered paths as exhaustive;
- comparisons involving the truncated result display the limitation.

### TSEQ-010 — profile-version isolation

Run existing profile 2 with its existing scenario-level guard fixtures, then run the proposed temporal profile on TSEQ-001/TSEQ-002.

Expected:
- profile 2 results remain byte/canonically consistent with the approved historical fixtures;
- temporal semantics are activated only by the new explicit profile/version;
- unknown profile versions fail closed with a clear validation error.

## 4. Test harness expectations

Each test must store:
- fixture ID and fixture bytes;
- expected validation status;
- expected ordered state and transition sequences, where applicable;
- expected blocked step and typed reason, where applicable;
- expected truncation status;
- expected run-record distinctions;
- selected profile and version;
- canonicalization/version details for comparing results.

Where both Python and browser engines implement the new profile, run the same fixture inputs through both and compare canonical semantic outputs, including ordered steps, blocked reasons, truncation and configuration snapshots. Existing profile-1/profile-2 regression fixtures must continue to pass unchanged.

## 5. Acceptance boundary

A PASS establishes only that the implementation conforms to these synthetic sequentiality cases. It does not establish that TGCV is scientifically valid, that T_acc is equivalent to the graph's enabled edges, or that a trajectory creates value.

**State:** criteria defined for review; no implementation, test run or scientific execution is claimed.
