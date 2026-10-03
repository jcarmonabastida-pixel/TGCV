# TGCV VIATRA v002 Concrete Fixture Materialization & Byte Audit

**Status:** SUPERSEDED — HISTORICAL MATERIALIZATION AUDIT

The byte hashes recorded here remain useful provenance, but the audit's source revisions are not the current canonical V002 packaging/source chain. The canonical fixture byte identity is maintained by `fixtures/TGCV_VIATRA_V002_FIXTURE_BYTE_HASH_MANIFEST_001.md`.
**Date:** 2026-10-02
**Core revision:** `ffa111dbb160c0bc55e89ea16430e97a38908662`
**Examples revision:** `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`
**Fixture specification:** `TGCV_VIATRA_MINIMAL_FIXTURE_v002`

## 1. Scope

This audit verifies the materialized v002 CPS, Deployment and CPSToDeployment XMI artifacts against the concrete VIATRA metamodel and the v002 semantic specification.

It is a fixture/materialization gate only. It does not authorize instrumentation or scientific execution.

## 2. Materialized artifacts

| Artifact | SHA-256 of exact UTF-8 bytes | UTF-8 bytes |
|---|---|---:|
| CPS | `8d432da0d3fd49ba88f809611f222614ef588809691e66bcc954a4cd509f66bb` | 316 |
| Deployment INITIAL | `fea5bc84929e99145ebe07f4eabeb1d04eaceb805b3e35d7975aff793bd9af8e` | 187 |
| Traceability INITIAL | `1ce4c0c69f324e43d87b41dee2561a55668d06c815294919011a2d5c3d1d88c1` | 500 |
| Deployment EXPECTED | `92addffad49e828a8c3c7f0ca7b00c870f00e9c419415c3b997e06cc36b0e966` | 240 |
| Traceability EXPECTED | `29ebb291e72ff061618aa809af2e16527464f2475e21bfe558de00bd36de33e3` | 720 |

These are byte-level SHA-256 digests of the exact UTF-8 contents committed to GitHub. Git blob SHAs are not used as substitutes.

## 3. Structural checks

### PASS — CPS

- root class: `CyberPhysicalSystem`;
- exactly one `HostType`;
- HostType identifier: `Rawsberry.PI`;
- exactly one `HostInstance`;
- HostInstance identifier: `Aragorn`;
- HostInstance nodeIp: `152.66.102.6`;
- no application/request/state/transition content.

### PASS — Deployment INITIAL

- root class: `Deployment`;
- zero `DeploymentHost` elements.

### PASS — Traceability INITIAL

- root class: `CPSToDeployment`;
- `cps` references the CPS root;
- `deployment` references the initial Deployment root;
- zero `CPS2DeploymentTrace` elements.

### PASS — Deployment EXPECTED

- root class: `Deployment`;
- exactly one `DeploymentHost`;
- actual metamodel ID attribute: `DeploymentHost.ip`;
- value: `152.66.102.6`.

### PASS — Traceability EXPECTED

- root class: `CPSToDeployment`;
- exactly one `CPS2DeploymentTrace`;
- exactly one `cpsElements` reference;
- exactly one `deploymentElements` reference;
- source reference resolves to HostInstance `Aragorn`;
- target reference resolves to DeploymentHost `152.66.102.6`;
- no invented trace identifier attribute.

## 4. Rule correspondence

The expected delta corresponds directly to the concrete `HostMapping` CREATED action:

`HostInstance.nodeIp -> DeploymentHost.ip`

followed by:

`HostInstance -> CPS2DeploymentTrace.cpsElements`

and:

`DeploymentHost -> CPS2DeploymentTrace.deploymentElements`

No v001-style `CPS2DeploymentTrace(cpsElement, deploymentElement)` pseudo-class is used.

## 5. Canonical semantic delta

The expected semantic delta contains exactly:

1. creation of one DeploymentHost;
2. assignment of `ip=152.66.102.6`;
3. creation of one CPS2DeploymentTrace;
4. one CPS source-element reference;
5. one Deployment target-element reference.

No unrelated model mutation is represented.

## 6. Important boundary

The EXPECTED XMI is a deterministic **semantic post-state fixture**, not yet evidence of a serializer-generated runtime output.

In particular, serialization details such as URI normalization, resource ordering and EMF-generated fragment conventions must be verified when the actual instrumented VIATRA transformation is run.

Therefore this gate establishes:

**materialization and byte integrity PASS**

but does not establish:

**runtime equivalence PASS**.

## 7. Transformation identity verification

The v002 transformation identity input was independently hashed:

`23af6acbbeb9b641d3d4cced837c98cc4feee4b953c8a6866fa9a88f72af2f7f`

This exactly matches the digest declared in `TGCV_VIATRA_MINIMAL_FIXTURE_SPECIFICATION_v002.md`.

## 8. Scientific firewall

No fixture artifact contains:

- U_t;
- T_acc;
- accessibility labels;
- future assignment;
- outcome;
- utility;
- reward;
- value;
- scientific performance metrics.

## 9. Decision

**PASS — MATERIALIZATION/BYTE AUDIT**

The v002 fixture artifacts are now materially defined and byte-hash recorded.

**Not authorized:** instrumentation implementation or scientific execution.

**Next gate:** **VIATRA v002 Runtime Equivalence Preflight** — load the materialized artifacts under the concrete VIATRA metamodel, verify the root mapping and HostMapping match cardinality, and establish that the actual CREATED activation produces the specified semantic delta before any runtime observation capture is admitted.
