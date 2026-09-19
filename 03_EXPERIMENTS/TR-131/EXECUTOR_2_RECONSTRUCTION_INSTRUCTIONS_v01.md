# TGCV TR-131 — Executor-2 Reconstruction Instructions v0.1

**Status:** CANDIDATE — NOT FROZEN  
**Scientific execution:** NOT AUTHORIZED

## Boundary

Executor-2 must receive only the frozen scientific package and must not receive Executor-1 outputs, trajectory results, interpretation, or post-execution modifications.

## Inputs

Executor-2 may use only:
- protocol reference;
- scientific bundle specification;
- scientific runner v0.2;
- scientific policy definitions;
- scientific execution configuration;
- environment specification;
- integrity manifest;
- G8 authorization-record schema (template only; no authorization);
- scientific execution-output schema;
- X declaration schema;
- trace schema;
- execution command template;
- audit worksheet;
- freeze audit;
- this reconstruction instruction.

## Execution command boundary

The command template is supplied for post-G8 use only. Executor-2 must not execute scientific mode while the package is candidate-only or without the formally bound G8 authorization record.

## Reconstruction

1. Verify repository/package identifiers and integrity references.
2. Reconstruct A and B from the declared X policies using the frozen scientific runner/configuration definitions. Do not execute unless the package is formally frozen and the Executor-2 procedure explicitly authorizes reconstruction.
3. Independently derive T_real,A and T_real,B.
4. Independently derive H_A and H_B.
5. Verify S0, C and T_acc equality across A/B.
6. Verify both realized transformations are admissible.
7. Produce a reconstruction record containing all hashes, traces and H values.
8. Record any deviation without modifying the package.

## Prohibited information

Executor-2 must not receive:
- Executor-1 output;
- Executor-1 hashes produced after execution;
- interpretation of expected results;
- coaching about expected H_A/H_B;
- any post-execution adjustment.

## Failure rule

Any undeclared difference in S0, C, T_acc, transformation definitions, admissibility, transition rule, environment or analysis procedure blocks reconstruction.

## Output

The Executor-2 output must be sufficient for an independent auditor to compare the reconstruction against the frozen package without relying on Executor-1 interpretation.

Scientific execution remains unauthorized until the package is frozen and the authorization gate is passed.
