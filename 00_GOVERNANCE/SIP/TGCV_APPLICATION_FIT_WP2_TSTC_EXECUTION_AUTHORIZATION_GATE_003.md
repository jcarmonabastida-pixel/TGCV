# TGCV APPLICATION FIT — WP2 TSTC
## EXECUTION AUTHORIZATION GATE 003

**Status:** AUTHORIZATION PASSED — TSTC EXECUTION v004 AUTHORIZED; EXECUTION NOT PERFORMED
**Fixture:** Fixture-003
**Supersedes:** no prior gate; Gate-002 remains the authorization record for v003.

### 1. Purpose

This gate authorizes the execution of `TSTC_EXECUTION_v004` after the v003 post-execution audit identified a machine-readable output-contract non-conformance.

v004 is a contract-correction execution. It does not modify or supersede the frozen Fixture-003 definition and does not reinterpret the completed v003 execution.

### 2. Preconditions verified

- Minimum Demonstrator Specification 001 remains the governing specification.
- Synthetic Fixtures Freeze-003 remains frozen and is the execution fixture.
- Fixture-003 transformation universes are unchanged.
- TSTC execution v003 remains preserved as historical execution evidence.
- Post-execution schema audit identified the v003 output-contract deficiency.
- TSTC execution v004 was created specifically to satisfy the missing output fields and comparison dimensions.
- Static audit v004 returned `TSTC_EXECUTION_V004_STATIC_AUDIT=PASS`.
- Static audit v004 explicitly confirms `NO_TSTC_EXECUTION_PERFORMED=True`.

### 3. v004 corrections authorized

The authorized v004 run shall:

1. emit the required per-connector machine-readable record;
2. include `fixture_id`, `connector_id`, `L_version`, `U_tau`, `transition`, `baseline_model`, `baseline_representation`, `baseline_reconstruction`, and `comparison_observations`;
3. reconstruct the conventional baseline through independent domain-specific feasibility rules rather than calling the TGCV `tacc()` implementation for the baseline;
4. report the eight comparison dimensions required by the Minimum Demonstrator Specification;
5. retain the existing positive interventions, negative controls, and two distinct cross-domain scenarios;
6. preserve the synthetic bounded boundary and all non-claim restrictions;
7. generate an output hash over the complete result including execution metadata.

### 4. Mandatory invariants

The run must stop if any of the following occurs:

- Fixture version differs from 003.
- `U_tau` differs from the frozen Fixture-003 universe.
- A declared-variable-only intervention is violated.
- A trajectory uses an inaccessible transformation.
- Negative control produces non-empty `Delta_T_acc`.
- Baseline reconstruction does not reproduce the same bounded admissible sets under the same frozen information.
- Required output-contract fields are absent.
- Cross-domain propagation is inferred rather than explicitly represented.
- Reproducibility metadata is incomplete.
- Any result requires reopening or modifying Core, RMA, Evidence→Claim Matrix, or STATUS.

### 5. Scientific boundary

Authorization is strictly for bounded applicability demonstration and output-contract verification. It does not authorize claims of scientific validity, empirical causality, superiority, generality, value creation, ROI, or industrial validation.

### 6. Execution status

**AUTHORIZED:** YES

**EXECUTION PERFORMED:** NO

**NEXT ACTION:** run `03_EXPERIMENTS/TSTC/tstc_execution_v004.py` locally under the frozen fixture and capture the complete machine-readable output.
