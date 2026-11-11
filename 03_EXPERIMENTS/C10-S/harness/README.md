# C10-S focal harness — implementation slice 001

**Scope:** methodological software slice for the focal randomized accessibility-mixture contrast on the synthetic B1 value instance (V_{B1}=Q_{B1}).  
**Status:** IMPLEMENTED_IN_RESEARCH_BRANCH / NOT_EXECUTED / NOT_CONFIRMATORY / NOT_DESIGN_FROZEN.

## Components

- `focal_harness.py`: explicit scenario and analysis contracts; focal DGP; restricted truth bundle; allow-list projector; evidence sealer; Analyzer; Evaluator.
- `test_focal_harness.py`: 15 software-contract tests for null, positive, negative, direct-path, unknown-direct-path, package-level abstention, Welch critical values, full-configuration run identity, truth projection and fail-closed configuration.

## Separation contract

1. Generator returns three distinct objects: run manifest, restricted `TruthBundle`, and `GeneratedSource`.
2. Projector emits only `unit_id`, randomized assignment, observed `Q_B1`, and observation status.
3. Sealer validates the allow-list and hashes the observed bundle.
4. Analyzer accepts only `SealedEvidence` plus a public `AnalysisContract`; its API has no truth, potential-outcome, signature, seed or generator-parameter argument. Run identity hashes the complete declared scenario configuration, including its parameters and seed.
5. Analyzer reports package ITT and focal-attribution outputs in separate fields. The package ITT estimate/interval remain available when focal attribution is not identified; focal estimate/interval are populated only when all focal identification gates pass.
6. Evaluator receives truth only after Analyzer has returned its result and checks run identity and output seal.

This is an application-level boundary, not a demonstrated security boundary. It does not replace the PE threat model, process/storage separation, effective ACLs, side-channel tests or G-ROLE acceptance.

## Focal DGP

The scenario config requires every parameter; there are no silent numerical defaults. It generates two potential (Q_{B1}) values per unit under (Z=0,1), with a two-state Markov availability process, policy-dependent probability of signature (d1), focal transition effects ((\alpha_{01},\alpha_{10})), and optional direct transition effects ((\gamma_{01},\gamma_{10})).

The focal truth is the analytical contrast under the common direct-path regime (\gamma=0):
[
\theta_A=(\lambda_1-\lambda_0)\{\mu_Q(d1)-\mu_Q(d0)\}.
]
The realized assignment contrast is separately retained as the package ITT truth. Focal attribution is emitted only when the direct path is declared absent, the common regime is established, positivity and version consistency are established, measurement is ideal, and interference is absent. A declared direct path blocks focal attribution; an unknown direct-path status or a failed focal gate forces indeterminacy. Evaluator adjudication applies the same package-level gates before judging focal identification, and separately detects a false declaration of no direct path against DGP truth.

## Explicit limitations

- This slice instantiates only the B1 scalar valuation case (V_{B1}=Q_{B1}); it does not instantiate general vector Value or a general (\Delta T_{acc}\to Value) claim.
- It is not the complete D2 material scenario, full transformation graph/Reach/trajectory reconstruction, full event ledger, missingness/censoring engine, cluster/interference engine, or general U_G store.
- The Analyzer reports a Welch–Satterthwaite two-sided 95% interval for the package ITT difference in arm means. When focal identification gates pass, the same estimate and interval are also explicitly exposed as focal outputs; otherwise focal outputs are null. The implementation is covered by deterministic critical-value contract tests, but it has not yet been executed or validated against P178's benchmark data; P178 remains a separate reference benchmark.
- The software tests are not Monte Carlo calibration, scientific execution, confirmatory execution, or evidence for a TGCV claim.

## Local software check

From this directory, with Python 3.10+:

```bash
python -m unittest -v
```

This command is documented only. The 15 tests are persisted but have not been run as a suite; no test-suite PASS or scientific run is claimed.
