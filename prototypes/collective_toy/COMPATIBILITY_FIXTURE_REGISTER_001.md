# Collective Toy — compatibility fixture register 001

**Status:** Current synthetic compatibility evidence only; no verified historical artifact has been admitted.  
**Scope:** Synthetic prototype package/replay contract only.

## 1. Version inventory at this revision

| Component | Declared version | Evidence | Compatibility conclusion |
|---|---|---|---|
| Browser package schema | `collective-toy-browser-run-001` | `prototypes/collective_toy/web/index.html` and cross-runtime tests | Current schema only |
| Python package schema | `collective-toy-run-package-001` | `prototypes/collective_toy/collective_toy_engine_001.py` | Current schema only |
| Browser engine | `collective-toy-engine-001` | Browser result metadata | Current engine only |
| Python engine | `ENGINE_VERSION` in the Python engine module | Python engine module and tests | Must be checked against the literal constant at fixture capture time |

Browser and Python packages deliberately have different envelope schemas. Their fields must not be compared as though the envelopes were identical; compare shared semantic outputs and each runtime's own envelope contract.

## 2. Current regression coverage

The current CI suite checks:

- Repeated execution determinism for selected synthetic fixtures.
- Browser/Python scenario-result agreement.
- Supported-package replay assessment.
- Unknown engine declaration: integrity/structural inspection only, with replay unavailable.
- Unknown package schema: reject, even after recalculating the package fingerprint.
- Unsupported rule profile: reject even after recalculating input, result, and package fingerprints.
- Rejection of inconsistent result declarations and tampered semantic fields.

These are regression fixtures constructed by the current test suite. They are **not** historical packages from a released prior engine version and do not prove cross-version compatibility.

## 3. Historical fixture admission criteria

A fixture may be called historical only if all of the following are recorded:

1. The original package bytes and SHA-256, captured from an identified prior commit/release or preserved artifact.
2. Original package schema version, engine version, runtime, and creation provenance.
3. A read-only copy of the original input and result; do not silently regenerate the historical result with the current engine.
4. Independently preserved expected scenario outputs and result fingerprints.
5. The current importer's explicit disposition: replay-verified, inspect-only/replay-unavailable, or rejected.
6. Browser/Python comparison only for fields whose schemas and semantics are defined to correspond.
7. CI evidence on the exact commit that adds or changes the fixture.

If no original artifact and provenance exist, label a fixture **baseline/current**, not historical. Never invent historical hashes or infer old behavior from the current implementation. The existing Rust Ω operationalization can support a provenance-backed real-data integration fixture once its dataset/license/identifiability gate and exact input/result manifests are reconciled; do not relabel that output as a historical package from a prior Collective Toy version.

## 4. Compatibility decision matrix

| Case | Expected disposition |
|---|---|
| Known schema + supported exact engine/profile + all checks pass | Replay may be verified |
| Known schema + unknown engine + safe integrity/structural checks pass | Inspect only; replay forbidden |
| Unknown schema | Reject |
| Unsupported rule profile | Reject |
| Hash, structure, or semantic consistency failure | Reject |
| Claimed historical version without original artifact/provenance | No compatibility claim; fixture admission blocked |

## 5. Next evidence gate

Before implementing a compatibility adapter, identify an actual prior package artifact and provenance. If none exists, first preserve a current baseline fixture with its exact source commit, original bytes, and independently recorded expected output; then continue to treat historical compatibility as untested. Any adapter proposal must add a new versioned decision and fixtures, not weaken the default fail-closed policy.

All examples remain synthetic. This register makes no claim about TGCV scientific validity, empirical performance, or the correctness of the theory.
