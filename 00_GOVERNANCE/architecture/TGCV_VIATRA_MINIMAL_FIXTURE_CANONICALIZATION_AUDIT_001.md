# TGCV VIATRA Minimal Fixture Canonicalization Audit

**Status:** UNDERDETERMINED — fixture specification requires correction before freeze  
**Date:** 2026-10-02  
**Framework revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`  
**Fixture specification:** `TGCV_VIATRA_MINIMAL_FIXTURE_SPECIFICATION_v001`

## Audit result

The semantic intent of the fixture is compatible with the documented CPS-to-Deployment example, but the current v001 specification cannot yet be treated as a canonical concrete EMF fixture.

### Confirmed

- The VIATRA repository contains the CPS-to-Deployment tutorial/example material at the frozen revision.
- The documented transformation uses HostInstance data to create/update deployment-side elements and traceability.
- The proposed observer boundary remains independent of U_t/T_acc/value/outcome channels.

### Not yet established

1. The exact generated Java/metamodel package paths for every proposed fixture class were not verified at the frozen revision.
2. The proposed semantic keys `deploymentHost:DH001` and `trace:T001` are TGCV fixture identifiers, not identifiers supplied by VIATRA; their mapping to actual model attributes must therefore be made explicit.
3. The v001 record grammar and byte encoding are specified conceptually but have not yet been generated and hash-verified from a concrete EMF/XMI artifact.
4. The expected CREATED action must be checked against the actual rule implementation at the frozen revision before the target object identity can be declared deterministic.
5. Therefore the current v001 document must not be interpreted as proof that a valid VIATRA model instance exists with exactly those records.

## Important correction

The canonical fixture must distinguish:

- **semantic fixture identifiers**, controlled by TGCV;
- **actual metamodel attributes**, controlled by VIATRA;
- **runtime EMF object identity**, which remains excluded.

No assumed TGCV key may be silently treated as an existing VIATRA model attribute.

## Decision

**UNDERDETERMINED.**

No immutable fixture artifact is frozen, and no instrumentation implementation or scientific execution is authorized.

## Next gate

Perform a **Concrete VIATRA Example Artifact Discovery Review**: locate the actual CPS example model/metamodel files and the exact HostRule implementation at the frozen revision. Then revise the fixture specification so every canonical field is backed by a concrete source artifact or explicitly declared TGCV-derived identifier.
