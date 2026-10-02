# TGCV VIATRA Fixture Canonicalization Preflight

**Status:** UNDERDETERMINED — fixture not frozen; implementation not authorized  
**Date:** 2026-10-02  
**Framework revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`

## Evidence reviewed

The frozen VIATRA documentation confirms the CPS-to-Deployment metamodel usage and the relevant semantic fields:

- `HostInstance.identifier`
- `HostInstance.nodeIp`
- `DeploymentHost.ip`
- CPS-to-Deployment trace links
- CREATED activation for the event-driven host rule.

The documented rule explicitly reads the source HostInstance IP and creates a DeploymentHost whose IP is derived from that value, then creates a trace entry linking source and target elements.

## Preflight assessment

| Item | Result | Finding |
|---|---|---|
| CPS source fields | PASS | Identifier and nodeIp are explicitly used by the documented rule. |
| Deployment target field | PASS | DeploymentHost.ip is explicitly assigned by the rule. |
| Traceability fields | PASS | Source/target trace links are explicit. |
| Pre-state scope | PASS | Required source state and explicit absence of output/trace can be represented. |
| Post-state scope | PASS | Required target and trace state can be represented. |
| Transformation semantic identity | PASS AT DESIGN LEVEL | Rule and CREATED state provide a stable semantic basis independent of runtime object identity. |
| Activation instance identity | PASS | Can remain observer-assigned and run-local. |
| Canonical ordering | PASS AT DESIGN LEVEL | Projection can be sorted by declared record tuple. |
| Exact value encoding | UNDERDETERMINED | The contract still needs an explicit byte-level encoding for delimiters, escaping and length prefixes. |
| Model-element keys | UNDERDETERMINED | The fixture needs a frozen semantic key policy; arbitrary EMF object identity is excluded. |
| Fixture bytes | UNDERDETERMINED | No concrete fixture artifact has yet been frozen in TGCV. |
| Completeness | PASS AT DESIGN LEVEL | Event/run manifest contract already defines completeness requirements. |

## Important boundary finding

The current documentation establishes the transformation semantics but does **not** itself provide a canonical byte representation of a concrete model instance. Therefore the TGCV fixture cannot yet be treated as frozen merely from the documentation.

The next artifact must be a concrete fixture specification that defines:
- exact model instance contents;
- semantic identifiers;
- exact initial-state records;
- exact expected post-state records;
- exact byte-level canonical encoding;
- expected transformation identity inputs.

## Decision

**UNDERDETERMINED.**

The proposed semantic projection is compatible with the documented transformation, but the actual fixture and byte-level canonicalization remain to be frozen.

## Next gate

Create the **TGCV VIATRA Minimal Fixture Specification v001**, including the exact one-HostInstance model, expected pre/post canonical records, byte encoding rules, and transformation identity inputs. Then audit that fixture specification before implementation.
