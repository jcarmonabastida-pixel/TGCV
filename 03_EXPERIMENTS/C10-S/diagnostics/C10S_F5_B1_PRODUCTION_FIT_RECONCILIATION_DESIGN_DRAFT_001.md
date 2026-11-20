# C10-S — F5 B1 production-fit reconciliation design draft 001

**Status:** RESEARCH DESIGN DRAFT — NOT FROZEN / NOT IMPLEMENTED  
**Date:** 2026-11-20  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Scope:** static implementation design and deterministic controls only  
**Frozen development specification:** `C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md`, v1.0 — unchanged  
**Historical numerical result:** B2/B3 run `44615173745` — immutable, failed frozen C5 gates

## 1. Purpose

Close the B1 traceability gap identified by the coordinated F5 diagnosis: the current per-dataset audit records the C5 production fit and a separate analytic-gradient fit, but does not directly reconcile them in one explicit record. This draft specifies the minimum additive diagnostic contract before code changes.

It does not select a new estimator, change C5 production fitting, change interval construction, define a weak-identification threshold, alter frozen acceptance criteria, or authorize numerical execution.

## 2. Three paths must remain distinct

For each dataset, retain three separately named operations:

1. **Production fit (P):** the exact finite-difference L-BFGS-B multi-start operation used by C5 to generate bootstrap draws.
2. **Analytic-gradient fit (A):** the existing L-BFGS-B multi-start diagnostic using the analytic Jacobian in (mean-logit, log-concentration) coordinates.
3. **Independent-coordinate check (I):** the existing BFGS diagnostic in (log-alpha, log-beta) coordinates, initialized from A's selected solution.

I is a local coordinate/optimizer cross-check, not an independently initialized global search. No report or field may describe it as a global optimizer.

P remains the production source for the historical C5 result. A and I remain diagnostic. No diagnostic fit may silently replace P.

## 3. Additive per-dataset reconciliation record

Add a nested object, tentatively `production_analytic_reconciliation`, to the existing F5 fit-diagnostics record. Preserve every current field and its meaning.

### 3.1 Identity and status fields

- `schema`: stable versioned schema identifier.
- `production_fit_source`: finite-difference L-BFGS-B.
- `analytic_fit_source`: analytic-Jacobian L-BFGS-B.
- `independent_check_source`: BFGS in log-shape coordinates, initialized from A.
- `production_fit_status`, `analytic_fit_status`, `independent_check_termination_status`: raw status labels, not collapsed into one Boolean.
- `reconciliation_status`: descriptive only; allowed values should distinguish missing data, boundary contact, production/analytic likelihood agreement, parameter divergence on a flat profile, material likelihood disagreement, and indeterminate comparison. This field must not itself turn a frozen unresolved state into PASS.

### 3.2 Production fit (P) raw fields

Retain the selected production fit's:
- alpha, beta, mean probability and concentration;
- log-likelihood and negative log-likelihood;
- selected start index and original optimizer message;
- all three start outcomes: success flag, termination message, terminal coordinates, objective, gradient information when available, and distances to each configured bound.

If a quantity is not exposed by SciPy or not currently calculated, serialize it as null with a typed reason; do not reconstruct or fabricate it.

### 3.3 Analytic fit (A) raw fields

Retain the existing complete A record:
- selected mean-logit and log-concentration;
- alpha, beta, mean probability and concentration;
- log-likelihood;
- all three start outcomes and their raw termination messages;
- score vector/norm, observed Hessian, eigenvalues/eigenvectors;
- nuisance-profile curvature and boundary likelihood contrasts;
- distances to configured bounds.

Do not infer concentration identification from convergence, score size, or a single Hessian eigenvalue.

### 3.4 Direct P-versus-A comparisons

Calculate and serialize, without thresholding:
- signed and absolute log-likelihood difference, P minus A;
- signed differences in mean-logit and log-concentration where transformable;
- signed log-alpha and log-beta differences;
- signed and absolute differences in mean probability and concentration;
- production and analytic score vectors/norms evaluated at their own terminal points; where a common-coordinate score can be evaluated at both points, retain it explicitly as a separate cross-evaluation;
- boundary distances for both selected fits;
- whether either fit is at a configured numerical bound.

Raw differences are descriptive. Do not introduce a tolerance or a PASS/FAIL cutoff in this draft.

## 4. Keep three adjudication dimensions separate

The implementation must not conflate:

**A. Termination:** did the numerical routine report success, failure, precision loss, iteration limit, or another terminal state?

**B. Numerical agreement:** how close are the terminal objective values and parameter coordinates? Preserve each metric continuously; do not infer agreement solely from the Boolean success flag.

**C. Statistical identification:** what do the profile likelihood, curvature, boundary contrasts and data support imply about concentration? Retain `INDETERMINATE` where no scale-aware rule with justified operating characteristics exists.

A precision-loss message with virtually identical terminal likelihoods is not automatically a materially different solution. Conversely, similar likelihoods on a flat concentration ridge do not identify concentration.

## 5. Multi-start gate discrepancy — do not resolve by assumption

The current runner's `_optimizer_diagnostic_is_resolved` requires all three analytic-gradient starts to report success. The frozen B1 wording requires retaining and comparing all three outcomes; it does not explicitly require every start to succeed. Frozen F5 acceptance nevertheless requires no unresolved numerical optimizer/identifiability state.

Therefore:
- preserve all three raw outcomes, including failures;
- do not equate “one start failed” with “all fits disagree”;
- do not equate “successful starts agree” with “the complete numerical state is resolved” without an explicit rule;
- do not remove the existing fail-closed gate or retroactively change B2/B3;
- before changing the gate, map its exact predicate to frozen B1 and §8 acceptance wording and document the interpretation in a separately reviewed design decision;
- if the available raw fields cannot distinguish a clearly noncompetitive failed start from a potentially competitive unresolved start, retain an indeterminate state.

No numeric concordance tolerance is authorized by this draft.

## 6. Deterministic adversarial fixture matrix

The static suite should exercise the complete record-building path, not only a serializer helper.

| Fixture | Required construction | Required assertion | Must not assert |
|---|---|---|---|
| P/A concordant, I precision-loss | Fixed deterministic count vector and injected I termination message | Raw I failure retained; P/A and A/I objective/parameter differences remain finite and independently visible | Automatic frozen PASS |
| Weak concentration ridge | Existing high-concentration/binomial-limit fixture | Near-zero profile curvature and boundary likelihood contrast remain separate from optimizer status; concentration identification remains indeterminate absent a justified rule | Binary weak-identification classification |
| Genuine P/A disagreement | Deterministic injected optimizer outcomes with distinct terminal objective/coordinates | Direct P/A divergence is present and not hidden by A/I agreement | Automatic selection of A |
| Upper numerical bound contact | Deterministic fit at configured upper log-concentration bound | Boundary distance/status preserved for P and A; no interior-fit label | Treating bound contact as identified finite concentration |
| Failed but noncompetitive start | Deterministic multi-start result with one failed terminal outcome and successful starts at a better objective | All outcomes retained; raw objective ordering visible | Treating failure as harmless absent an explicit adjudication rule |
| Missing diagnostic path | Inject audit failure through comparison engine | Production comparison remains traceable; missing audit is typed and cannot silently become resolved | Deleting the production output |

For analytic score/Hessian assertions, reuse the existing central-finite-difference and independent log-shape tests. Do not recreate already verified likelihood-limit fixtures.

## 7. Separate C5 interval diagnosis

The M30/R20 upper fitted-concentration tail is not the same signature as M10/R5's near-binomial weak-identification ridge.

- M10/R5: investigate the concentration likelihood ridge and P/A path divergence. The upper decile's near-zero profile curvature and near-zero advantage over the binomial limit support weak concentration identification in that post-fit stratum.
- M30/R20: the upper-decile profile remains separated from the binomial limit, while C5 conditional coverage is severely low and intervals are narrower than matched C0. This points to a distinct conditional calibration failure in the plug-in interval construction.

The current parametric bootstrap conditions on fitted alpha/beta. Increasing B reduces endpoint Monte Carlo error but does not propagate uncertainty in those fitted parameters. B3 already provides evidence that endpoint shifts are modest; it does not diagnose or repair the plug-in distributional approximation.

No replacement interval method is selected here. A profile-based, refit-based, or otherwise uncertainty-propagating alternative would require a separate method-design record, explicit estimand/coverage target, and fresh disjoint development data after static controls are complete.

## 8. Implementation sequence

1. Add the additive P/A reconciliation object without changing the production fit or bootstrap path.
2. Add deterministic tests for field completeness, signed-difference correctness, null/typed-missing handling, boundary contact and all three start outcomes.
3. Add the adversarial fixture matrix in §6, reusing existing limit/oracle fixtures.
4. Reconcile the runner's all-starts-success predicate against the frozen specification; do not change the gate until the interpretation is explicit and testable.
5. Run only the exact-commit static suite and compile checks; record commit, dependency identity and workflow result.
6. Review the static implementation against frozen B1 and F5 §8 before considering any new method-design decision.

No resource preflight, calibration bank, bootstrap bank, replay, holdout, Tier B, or C10 scientific execution belongs to this work package.

## 9. Non-actions and evidence boundary

- B2/B3 run `44615173745` remains unchanged and failed under its frozen gates.
- No historical row is relabelled PASS.
- No C0 fallback is promoted.
- No threshold, estimator, interval rule, DGP, K, B, seed, or frozen specification is changed.
- No weak-identification binary threshold is introduced.
- No claim about TGCV causal accessibility-to-value is advanced by this numerical-methods work.

**Draft disposition:** suitable as the bounded implementation contract for static review; not frozen, not implemented, and not execution-authorizing.
