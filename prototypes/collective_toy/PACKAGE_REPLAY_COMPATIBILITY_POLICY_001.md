# Collective Toy — package and replay compatibility policy 001

**Status:** Experimental software contract for the synthetic prototype.  
**Scope:** Package inspection, replay eligibility, and version compatibility. This is not a canonical TGCV architecture decision or a scientific claim.

## 1. Purpose

Cryptographic integrity, structural validity, semantic validity, and replay compatibility are distinct checks. A valid SHA-256 fingerprint proves only that the hashed representation matches that fingerprint; it does not establish that a consumer understands the declared schema or can reproduce the execution semantics.

The importer must keep these outcomes distinct and must fail closed when the package schema is unknown.

## 2. Required decision order

1. **Parse and validate the envelope.** Reject malformed JSON, missing required envelope fields, invalid version identifiers, or unsupported package schema versions.
2. **Verify package integrity.** Recompute and compare the package SHA-256 using the canonical serialization specified by the implementation.
3. **Validate structural and semantic invariants.** Validate referenced IDs, trajectory-edge continuity, relation-effect consistency, and consistency of effective disabled transitions. Recomputed hashes do not bypass these checks.
4. **Determine replay eligibility.** Replay is allowed only when the package schema is supported and the declared engine version is explicitly supported for that package/profile.
5. **Expose the outcome.** If the schema is supported but the engine version is unknown or unsupported, allow integrity/structure inspection only when those checks can be performed safely; clearly mark replay as unavailable and do not execute the package. If the schema is unknown, reject it rather than guessing its field semantics.

## 3. Outcome matrix

| Package schema | Engine version | Expected disposition |
|---|---|---|
| Supported | Explicitly supported for this profile | Validate and permit replay, subject to all integrity and semantic checks |
| Supported | Unknown or unsupported | Inspection only if validation is safe; replay forbidden |
| Unknown or unsupported | Any | Reject; do not infer schema semantics |
| Supported | Supported label but incompatible profile/contract | Reject replay; inspection only if safe validation is available |
| Any | Integrity or semantic validation fails | Reject |

“Inspection only” is not a successful replay and must never be presented as proof that the original computation can be reproduced.

## 4. Compatibility guarantees and non-guarantees

- Exact-version replay is the default policy for the prototype.
- No backward- or forward-compatibility guarantee is implied by matching hashes or by a version string that looks familiar.
- A future compatibility exception requires an explicit, versioned adapter or compatibility declaration, a documented mapping of semantics, historical fixtures, and cross-runtime tests against known expected results.
- Any adapter must be deterministic, auditable, and explicit about fields or semantics it cannot preserve. Lossy conversion must not silently authorize replay.
- An engine version must not be treated as compatible merely because it can parse a package.
- Unsupported package schema versions are rejected even if the package SHA-256 has been recalculated correctly.
- Unknown engine versions may be inspected but must not be replayed by the current engine.

## 5. Reproducibility contract

For the same supported engine version, profile, canonical input, configuration, and deterministic execution environment, repeated executions should produce identical canonical scenario results and result fingerprints. Browser/Python fixtures must agree on scenario results and hashes.

This is a scoped software-test guarantee for the fixtures and environments actually tested. It does not establish bit-for-bit reproducibility across arbitrary operating systems, runtime versions, or future engine versions unless those environments are separately tested.

## 6. Required evidence before changing this policy

Any change to replay compatibility requires:

1. A specific proposal stating the source and target package/engine versions.
2. Historical input/output fixtures with independently recorded expected fingerprints.
3. Tests for supported replay, inspect-only handling, unknown schema rejection, tampered hashes, and semantic inconsistency.
4. Browser/Python agreement for every applicable fixture.
5. Governance review and an auditable CI record on the exact commit.
6. A separate explicit decision before any promotion to `main`.

## 7. Current verified scope

The current prototype tests cover repeated-run determinism for selected fixtures; semantic rejection of tampered relation effects and trajectory edges; and the distinction between an unknown engine version (no replay) and an unknown package schema (reject). These checks do not establish compatibility with historical versions, cross-platform reproducibility, or scientific validity of TGCV.

**Acceptance-scope clarification (2026-10-19):** for the current Full Chain demonstrator, the required compatibility target is the explicitly supported current package schema/engine/profile, including export, import, integrity/semantic validation, and independent replay. Unknown or unsupported formats must continue to fail closed. Backward compatibility with historical Full Chain execution packages is not an acceptance requirement unless an actual prior package format is identified and a future scope decision explicitly adds it. Earlier limited model/run JSON files are not automatically historical execution packages; any model-import requirement is separate.

All results remain synthetic and prototype-scoped. No empirical dataset processing or scientific execution is authorized by this document.
