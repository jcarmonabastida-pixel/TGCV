# N-R4B.2 — Implementation Conformance Gate Result v0.1

**Date:** 2026-09-05  
**Status:** PASS / CLOSED  
**Scope:** Branch N controlled reconstruction only.  
**Scientific execution:** NOT PERFORMED.

## 1. Decision

N-R4B.2 is **PASS / CLOSED**.

The prospective R4B trajectory/outcome implementation conforms to the currently frozen semantic decisions of N-R4B.1 as exercised by conformance runner v0.3. No scientific corpus generation, learner fitting, model comparison, or confirmatory inference was performed.

## 2. Evidence

Runner: `03_EXPERIMENTS/EMP-1.1/tools/run_n_r4b_conformance.py`  
Runner version: `N_R4B_CONFORMANCE_RUNNER_v0.3`  
Runner content SHA-256: `215d4ca35634d4c7290848b69c89324975b60db1`  
Implementation: `03_EXPERIMENTS/EMP-1.1/src/branch_n_r4b_trajectory_v01.py`  
Implementation content SHA-256: `85c551437514bf38cc1312e3072a698986532023`

The user-executed v0.3 conformance run returned `status=PASS` with all registered checks passing:

- objective codebook;
- state-dependent goal semantics;
- trajectory-seed derivation;
- same snapshot + same seed determinism;
- seed change without snapshot change;
- objective-independent transition selection under a goal-disabled fixture;
- empty-`T_acc` terminal semantics;
- distinct transformation identities mapped to the same successor remain selectable;
- success after one or more transitions;
- horizon and record schema;
- predictor/learner dependency exclusion at source level;
- success at `h=0`;
- deterministic state hashing.

## 3. Interpretation

The implementation is accepted as a conforming implementation of the prospective Branch N R4B trajectory/outcome specification. This does **not** establish historical recovery of MVE-1.0 and does **not** validate the scientific hypothesis.

The duplicate-successor check is a contract-level fixture: it monkeypatches two distinct abstract transformation identities to the same successor. It verifies the specified sampling boundary but is not evidence that the native Branch N transformation system currently contains such a pair.

The `no_learner_dependency` check is a static source-token check. It is not a full predictor/trajectory integration test. R4B itself contains no learner-fitting stage; the predictor/outcome separation will be checked again at the corpus/evaluation integration boundary.

These limitations do not reopen N-R4B.2 because they concern fixture strength and later integration, not a demonstrated violation of the R4B.1 contract.

## 4. Scientific boundary

No 30,000-train / 10,000-test corpus has been generated under this gate. No learner has been fitted. No historical EMP-1.1 result has been used as a tuning target. No change has been made to R* v0.2, N-R1.x, N-R2, N-R3, or N-R4A.

## 5. Next authorized gate

The next authorized step is **N-R4B.3: controlled full trajectory/outcome corpus specification**, covering the prospective 30,000-train + 10,000-test corpus and its provenance, deterministic serialization, integrity checks, leakage checks, and acceptance criteria. Scientific learner fitting remains blocked until the subsequent gates explicitly authorize it.
