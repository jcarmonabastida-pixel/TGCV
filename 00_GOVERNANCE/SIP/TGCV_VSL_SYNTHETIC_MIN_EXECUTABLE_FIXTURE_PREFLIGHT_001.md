# TGCV — VSL Synthetic Minimum v0.1
## Executable Fixture Preflight 001

**Status:** PRE-RUN PREFLIGHT — PASS BY STATIC INSPECTION  
**Executable fixture:** `03_EXPERIMENTS/VSL_SYNTHETIC_MIN_V001/vsl_synthetic_min_fixture_v01.py`  
**Fixture commit:** `1b2990e067fdc7ae862c84c58be04848dde339d3`

## Controls

| Control | Result |
|---|---|
| Frozen baseline `(10,10)` | PASS |
| Frozen outcome `O=q+0.5r` | PASS |
| Frozen VSL `V*=O` | PASS |
| T1–T4 coverage | PASS |
| NC1/NC2 coverage | PASS |
| Outcome inputs restricted to final `q,r` | PASS |
| T4 exogenous factor not consumed by outcome | PASS |
| Required contrasts encoded | PASS |
| No experiment execution in fixture | PASS |
| No causal interpretation in fixture | PASS |

## Boundary

This is a static preflight based on source inspection. It is not runtime execution evidence.

The next authorized operation is to execute the fixture's own validation entry point in a controlled environment and record the runtime result before constructing the experimental runner.
