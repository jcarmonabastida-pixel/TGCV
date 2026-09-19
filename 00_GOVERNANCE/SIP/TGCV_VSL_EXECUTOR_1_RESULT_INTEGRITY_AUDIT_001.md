# TGCV VSL Executor-1 A/B Result Integrity Audit 001

## Status

**PASS — EXECUTOR-1 A/B STRUCTURAL EXECUTION AND NETWORK CONTROL VERIFIED**

Date: 2026-09-19

## Frozen execution package

Canonical frozen package commit:

`a1e5005d4d924e0c725671bfca05506a4616e5ff`

Execution environment:

- Python: `3.8.10`
- OS: `Windows-10-10.0.26200-SP0`
- Network isolation: **PASS**
- Direct TCP target: `1.1.1.1:443`
- TCP result: `BLOCKED`
- Network evidence UTC: `2026-09-19T01:00:19.488679+00:00`

## Executor-1 outputs

### A

Path:

`03_EXPERIMENTS/VSL/A_EXECUTION_RESULT_002.json`

- N = 100
- rows = 100
- fixture count = 100
- control/treatment T_acc sizes = (7, 8) for all fixtures
- `delta_t_acc = 1` for all fixtures
- `delta_V_star` present for all fixtures
- file SHA-256:
  `9d365a0f3a99f5442962f38c29be8a10bfb5d327a13fc1b161782eb05e5fadce`
- dataset SHA-256:
  `6b51f7f46e75c76bfbb9e0428f8828d0b2641805c545f8cd7436a59b2cfdea58`

### B

Path:

`03_EXPERIMENTS/VSL/B_EXECUTION_RESULT_002.json`

- N = 100
- rows = 100
- fixture count = 100
- control/treatment T_acc sizes = (7, 8) for all fixtures
- `delta_t_acc = 1` for all fixtures
- `delta_V_star` present for all fixtures
- file SHA-256:
  `743d499f7ea56d439eb85376967acc3d2eb0fd62d4530351f86d8fdac4a26818`
- dataset SHA-256:
  `a3c7cefa75cf01ce7bd6944d845a578b652d499e6fa01ff38443c7c15e5cda03`

## Network-isolation evidence

Local evidence file:

`03_EXPERIMENTS/VSL/NETWORK_ISOLATION_CHECK_001.txt`

- file SHA-256:
  `0e66606221b8c1d34569c54408569f187e7f7efec343e35b27005ba78174bf54`
- recorded `NETWORK_PROHIBITED=PASS`
- recorded `TCP_RESULT=BLOCKED`
- recorded HEAD = frozen package commit.

## Interpretation boundary

This audit records execution integrity only.

It does **not** interpret `delta_V_star`, establish causal Value effects, establish predictive validity, or upgrade any TGCV claim.

Executor-2 remains pending and must be executed under its independent reconstruction boundary without access to Executor-1 outputs, interpretations, or expected effect direction.

The three local evidence files above must be transferred to the canonical repository without byte modification before final reconciliation. Any SHA mismatch is a STOP condition.

## Governance

No change to TGCV Core, RMA, Evidence-to-Claim Matrix, C09, VSL-SPEC-01, or VSL-EXP-01.
