# C10-S — Coverage-first small-sample screening policy 001

**Date:** 2026-11-27  
**Status:** DEVELOPMENT SCREENING POLICY — NOT A TIER-A VALIDATION METHOD

## 1. Purpose

Use small, bounded development samples to discard clearly poor interval-method candidates or identify candidates worth a separately justified validation. Do not spend hours on a large batch before learning whether the method has plausible emission, fit stability, endpoint behaviour and coverage direction.

## 2. Two distinct statistical questions

**Screening:** Is there an obvious reason to reject the candidate (very low emission, systematic directional misses, severe undercoverage, unstable intervals, or excessive runtime)? A small sample can provide useful negative evidence and diagnostic clues.

**Validation:** Does the method meet the frozen Tier-A coverage criteria with adequate precision? A small sample generally cannot answer this. Do not call a screening result PASS, validated, calibrated or Tier-A-ready.

For reference, at true coverage 95%, the approximate standard error of an empirical coverage estimate is sqrt(0.95*0.05/K): about 3.9 percentage points at K=30, 3.1 points at K=50, and 2.2 points at K=100. A small screen therefore detects gross departures, not small deviations around 95%. Wilson intervals must always be reported.

## 3. Default staged screen

Unless the method's cost profile requires a smaller probe:
- Stage 0: K=5, B=10 for smoke/runtime/abstention diagnostics only; not coverage evidence.
- Stage 1: K=30, B=25 for a directional coverage screen, with every dataset retained and all abstentions reported.
- Stage 2: only if Stage 1 is promising, consider K=50, B=50 as a further development screen. It is still not validation.
- Any prospective Tier-A calibration/validation must be separately designed with MCSE/sample-size justification, fresh seeds, frozen protocol, and explicit authorization.

The exact B must be sufficient to keep bootstrap Monte Carlo noise from dominating interval endpoints; if it is not, reduce K rather than silently accepting unstable quantiles. Record per-dataset runtime and endpoint stability where possible.

## 4. Screening interpretation

A screen is **clearly adverse** if emission is far below the frozen 95% threshold, there is pronounced directional undercoverage, or the coverage estimate is materially below 95% with Wilson evidence inconsistent with the target. Such a result can discard a candidate, but cannot prove general failure outside the tested DGP/cell.

A screen is **promising only** if point coverage is near 95%, emission is plausible, and no strong directional or fit-state pathology appears. This is a reason to design a fresh independent validation, not to accept the method.

A screen is **inconclusive** if K is too small to distinguish the observed estimate from 95%, or if bootstrap endpoint Monte Carlo noise is material. Do not increase compute by default; first identify whether the uncertainty comes from K, B, or fit failures.

Always report: K, B, hits/denominator, point coverage, Wilson 95%, emission and abstention classes, lower/upper miss counts, interval width, runtime, seed provenance, and tested DGP/cell. Any post-fit strata are exploratory only and cannot become acceptance strata post hoc.

## 5. Runtime discipline

- Maximum 30 minutes per new development run, including setup.
- Prefer one cell and one method per run.
- Use measured cost from the previous completed run; do not extrapolate an optimistic pilot estimate.
- Emit per-dataset checkpoints/progress and preserve partial diagnostic outputs if interrupted.
- No parallel duplicates, no automatic reruns, no silent K/B expansion.
- If the required screen cannot fit 30 minutes, simplify the diagnostic question or method; do not raise the timeout.

## 6. Current M30/R20 run

Run `45976887796` (K=400, B=100, timeout 165 minutes) is a legacy oversized run and violates this policy. Stop it; do not duplicate or expand it. If GitHub Actions cancellation cannot be performed through the connected integration, report that limitation rather than implying it was cancelled. No subsequent run is permitted until the small-sample runner and checkpoint design are in place.

## 7. Governance

This policy changes operational screening only. It does not change Tier-A acceptance criteria, estimands, DGPs, confidence level, causal hypotheses or execution authorization. Screening data are development-only and cannot be repurposed as confirmatory holdout data.
