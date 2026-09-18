# A Bundle Freeze Manifest 001

**Status:** FREEZE CANDIDATE — NOT FROZEN
**Date:** 2026-09-19

## Immutable components
- EXECUTION_SPEC.md
- execute.py
- EXECUTOR_2_RECONSTRUCTION_SPEC.md
- frozen A VSL reference

## Repository integrity
Git blob identifiers are the immutable repository identifiers for the current committed contents. Byte-level SHA-256 must be generated from the exact execution checkout at final freeze.

## Environment
Python 3.x standard library only; exact interpreter version must be recorded at freeze.
OS/platform must be recorded at freeze.
Network access: prohibited.

## Seeds
582031 is fixed as bundle identifier. No treatment/control random assignment exists.

## Freeze blockers
- exact checkout commit;
- exact interpreter version;
- byte-level SHA-256 values;
- executor-2 delivery boundary;
- final manifest hash.

**Execution authorization:** NO